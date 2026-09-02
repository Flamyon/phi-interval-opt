# tests for src/reference_fronts.py, subpart b2.
# the module encodes docs/b1_phi_efficient_sets.md sections 2.1 to 2.6 as the map
# w -> x(w) and a weight sample. these tests check the encoding against b1 from
# the other side: the closed-form regions of b1 section 2.4 are written out here
# and nowhere in the module, so a test passing means the sampled points landed
# where the derivation says they should and not that one file agrees with itself.
#
# b2-b adds the sampling mode, and it is parametrised over rather than fixed: the
# farthest-point mode is a subsample of a larger draw through the same map, so it
# changes which points are kept and no property of them, and a test that ran under
# one mode only would leave the other mode's front unchecked. the two tests that
# are the mode's own are the subsequence check and the nearest-neighbour spread
# comparison, and they are the last two in the file.

import numpy as np
import pytest

from phi_transforms import phi_registry
from problems_tier0 import p0, p1, p1_default_params
from reference_fronts import (
    derivation_rho,
    dirichlet_mode,
    efficient_set,
    farthest_point_mode,
    oversampling_factor,
    reference_front,
    sampling_modes,
    simplex_weights,
    singular_segments,
    singular_share,
    stationarity_systems,
    stationary_points,
    transformed_image,
)

phi_names = ("lu", "ls", "cw")
# the two sampling modes, b2-b. every test that does not name one runs under both:
# the farthest-point mode changes which of the sampled points are kept and nothing
# else, so every property the dirichlet mode has to satisfy it has to satisfy too.
modes = sampling_modes
# the point count most tests run at. large enough that the weight sample reaches
# the neighbourhood of every extreme of b1 section 2.4, small enough that the
# dense-sample dominance test stays a few seconds.
sample_size = 2000
# b1 section 2.4's extreme values, 4/5, 1 and 4/3, as exact doubles
four_fifths = 4.0 / 5.0
four_thirds = 4.0 / 3.0


# the residual of b1 section 2.4's phi_ls inequality, 7 x_1 x_2 - 4 x_1 + 12 x_2 - 16
def ls_form(points):
    x_1, x_2 = points[:, 0], points[:, 1]
    return 7.0 * x_1 * x_2 - 4.0 * x_1 + 12.0 * x_2 - 16.0


# the residual of b1 section 2.4's lower bound on X_lu, 4 x_1 - x_1 x_2 - 20 x_2 + 16
def lu_lower_form(points):
    x_1, x_2 = points[:, 0], points[:, 1]
    return 4.0 * x_1 - x_1 * x_2 - 20.0 * x_2 + 16.0


# how far outside its own closed-form region of b1 section 2.4 a point set lies.
# every entry is a constraint residual, so the largest one being at most zero is
# membership and its size is the violation.
def region_excess(phi_name, points):
    x_1, x_2 = points[:, 0], points[:, 1]
    if phi_name == "lu":
        # X_lu = {x_1 >= 0, 4 x_1 - x_1 x_2 - 20 x_2 + 16 <= 0, ls form <= 0}
        residuals = [-x_1, lu_lower_form(points), ls_form(points)]
    elif phi_name == "ls":
        # X_ls = {0 <= x_1 <= 4/3, 0 <= x_2 <= 4/3, ls form <= 0}
        residuals = [-x_1, -x_2, x_1 - four_thirds, x_2 - four_thirds, ls_form(points)]
    else:
        # X_cw = the unit square
        residuals = [-x_1, -x_2, x_1 - 1.0, x_2 - 1.0]
    return float(np.max([np.max(r) for r in residuals]))


# the gradient of the weighted sum of the 2m image coordinates, by central differences.
# condition (15) is stationarity of exactly that sum, b1 section 0, and the sum is
# a quadratic in x for every phi, b1 section 1.1, so a central difference is exact
# up to rounding. the columns come from problem.evaluate through the phi record,
# so what is differentiated is what the code evaluates and not a retyped formula.
def weighted_gradient(problem, points, record, weights, params, step=1e-5):
    gradient = np.zeros_like(points)
    for k in range(problem.n_vars):
        offset = np.zeros(problem.n_vars)
        offset[k] = step
        forward = transformed_image(problem, points + offset, record, params)
        backward = transformed_image(problem, points - offset, record, params)
        gradient[:, k] = np.sum(weights * (forward - backward), axis=1) / (2.0 * step)
    return gradient


# a dense uniform sample of a problem's decision box
def dense_box_sample(problem, size, seed):
    lower, upper = problem.bounds()
    generator = np.random.default_rng(seed)
    return generator.uniform(lower, upper, size=(size, problem.n_vars))


# the count of front rows some sample row dominates, usual pareto relation.
# no tolerance and no rounding, per d-02 and the project rule: a tolerance here
# would hide exactly the failure this test exists to catch.
def dominated_count(front, sample_image, block=100):
    total = 0
    for start in range(0, len(front), block):
        rows = front[start:start + block]
        not_worse = np.all(sample_image[None, :, :] <= rows[:, None, :], axis=2)
        strictly_better = np.any(sample_image[None, :, :] < rows[:, None, :], axis=2)
        total += int(np.count_nonzero(np.any(not_worse & strictly_better, axis=1)))
    return total


# one call of efficient_set per distinct set of arguments, shared by the tests
# that ask for the same set. efficient_set is a pure function of its arguments and
# test_the_front_is_reproducible asserts exactly that, without the cache; the
# reason for caching is cost, the farthest-point selection being O(n_points^2) in
# the oversample and 2.2 s at n_points = 2000 measured, so recomputing it once per
# test would put a minute in the fast run for nothing.
sample_cache = {}


def sampled_set(phi_name, n_points, include_singular, mode):
    key = (phi_name, n_points, include_singular, mode)
    if key not in sample_cache:
        sample_cache[key] = efficient_set(p1, phi_name, n_points, include_singular,
                                          mode)
    return sample_cache[key]


# the nearest-neighbour distance of every point of a set to the rest of it
def nearest_neighbour_distances(points, block=256):
    out = np.empty(len(points))
    for start in range(0, len(points), block):
        rows = points[start:start + block]
        distances = np.sqrt(np.sum((rows[:, None, :] - points[None, :, :]) ** 2,
                                   axis=2))
        # a point's distance to itself is zero and is not its nearest neighbour
        distances[np.arange(len(rows)), np.arange(start, start + len(rows))] = np.inf
        out[start:start + len(rows)] = np.min(distances, axis=1)
    return out


# every sampled point satisfies condition (15) with the weight recorded beside it
@pytest.mark.parametrize("phi_name", phi_names)
@pytest.mark.parametrize("include_singular", (False, True))
@pytest.mark.parametrize("mode", modes)
def test_condition_15_holds_at_every_sampled_point(phi_name, include_singular, mode):
    points, weights = sampled_set(phi_name, sample_size, include_singular, mode)
    gradient = weighted_gradient(p1, points, phi_registry[phi_name], weights,
                                 p1_default_params)
    # the weights sum to one on the regular part and to one on the singular ray
    # too, so the gradient is on the scale of the image coordinates themselves and
    # the bound is absolute. central differences on a quadratic at step 1e-5 carry
    # a rounding error of order eps |g| / step, which is about 1e-11 here.
    assert np.max(np.abs(gradient)) < 1e-7


# the recorded weights are the admissible ones of example 3.9, w >= 0 and not all zero
@pytest.mark.parametrize("phi_name", phi_names)
@pytest.mark.parametrize("mode", modes)
def test_recorded_weights_are_admissible(phi_name, mode):
    _, weights = sampled_set(phi_name, sample_size, True, mode)
    assert np.min(weights) >= 0.0
    assert np.min(np.sum(weights, axis=1)) > 0.0


# every sampled point lies inside b1 section 2.4's closed form for its own phi
@pytest.mark.parametrize("phi_name", phi_names)
@pytest.mark.parametrize("include_singular", (False, True))
@pytest.mark.parametrize("mode", modes)
def test_sampled_points_lie_in_the_derived_region(phi_name, include_singular, mode):
    points, _ = sampled_set(phi_name, sample_size, include_singular, mode)
    # the residual is a polynomial in coordinates of size one, so its rounding is
    # a few eps; the bound is not a tolerance on membership but on that rounding.
    assert region_excess(phi_name, points) <= 1e-12


# no point of a dense random sample of the box dominates any reference front point.
# this is the test that catches a wrong derivation, CONTEXT.md section 10 b2 and
# b1 section 8, and it is run under every phi and under both settings of the flag.
# the sample is random and not a lattice, which is what CONTEXT.md section 10 b2
# asks for and is also the only form that measures the derivation rather than the
# arithmetic. a lattice collides with the singular segment's own lattice: at
# n_points = 2000 the phi_ls segment point x_1 = 0.3333333333333333 and the a4
# 61 x 61 grid point x_1 = 0.33333333333333337 are 5.6e-17 apart, three of their
# four image columns are bitwise equal and the fourth differs by 4.4e-16, so the
# grid point dominates by one rounding step. that is d-02's subject and not this
# test's: the relation carries no tolerance, by rule, so two points an ulp apart
# are ordered by the rounding and the fix is to keep the test set off the
# fixture's lattice, never to add a tolerance here.
# a 20000-point diagnostic and not a correctness check, so it is marked slow
@pytest.mark.slow
@pytest.mark.parametrize("phi_name", phi_names)
@pytest.mark.parametrize("include_singular", (False, True))
@pytest.mark.parametrize("mode", modes)
def test_no_dense_sample_point_dominates_the_front(phi_name, include_singular, mode):
    sample = dense_box_sample(p1, 20000, seed=20260901)
    sample_image = transformed_image(p1, sample, phi_registry[phi_name],
                                     p1_default_params)
    front = reference_front(p1, phi_name, sample_size, include_singular, mode)
    assert dominated_count(front, sample_image) == 0


# the containment of docs/a_close_containment.md, asserted on the encoded sets.
# b1 section 5 verified it on the closed forms; it is asserted here because an
# encoding bug would break it, and it is a check on this module and never
# evidence for the containment itself, which stands on s-11.
@pytest.mark.parametrize("phi_name", ("lu", "cw"))
@pytest.mark.parametrize("mode", modes)
def test_lu_and_cw_points_satisfy_the_ls_region(phi_name, mode):
    points, _ = sampled_set(phi_name, sample_size, False, mode)
    assert region_excess("ls", points) <= 1e-12


# b1 section 2.4's extreme values, as (phi, coordinate, value, reduction)
extremes = (
    ("lu", 0, four_thirds, "max"),
    ("lu", 1, four_thirds, "max"),
    ("lu", 1, four_fifths, "min"),
    ("ls", 0, four_thirds, "max"),
    ("ls", 1, four_thirds, "max"),
    ("cw", 0, 1.0, "max"),
    ("cw", 1, 1.0, "max"),
)


# b1 section 2.4's extreme values are approached as the sampling density rises
@pytest.mark.parametrize("phi_name,coordinate,target,reduce_name", extremes)
def test_extreme_points_are_approached_with_density(phi_name, coordinate, target,
                                                    reduce_name):
    errors = []
    for n_points in (200, 2000, 20000):
        points, _ = efficient_set(p1, phi_name, n_points, False, dirichlet_mode)
        reached = getattr(np, reduce_name)(points[:, coordinate])
        errors.append(abs(reached - target))
    # convergence, not equality at a fixed n: the error never grows with density
    # and is negligible at the top of the range. a weight sample reaches these
    # values only in the limit, b1 section 2.4, since each needs a zero weight.
    assert errors[1] <= errors[0]
    assert errors[2] <= errors[1]
    assert errors[2] < 1e-3


# the farthest-point mode approaches the same extreme values with density
@pytest.mark.parametrize("phi_name,coordinate,target,reduce_name", extremes)
def test_the_farthest_point_mode_approaches_the_extremes(phi_name, coordinate,
                                                         target, reduce_name):
    # the same convergence as the test above, asserted of the other mode at the two
    # densities it is affordable at. the mode is not parametrised into that test
    # and this is why: it runs at 20000 points, where the selection chooses 20000
    # of a 200000-point draw and takes 189 s measured, which is not a fast-run
    # cost. the assertion is not that the selection reaches an extreme more
    # closely than the draw of the same size does, and that is false as often as
    # not: the selection keeps the points farthest apart in objective space and an
    # extreme of one decision coordinate is not one of those, so at 2000 points
    # the phi_ls maximum of x_1 is 5.5e-06 from 4/3 under the selection and
    # 2.8e-08 under the draw. what holds of both modes is that the error falls
    # with density and is negligible at the top of the range.
    errors = []
    for n_points in (200, sample_size):
        points, _ = sampled_set(phi_name, n_points, False, farthest_point_mode)
        errors.append(abs(getattr(np, reduce_name)(points[:, coordinate]) - target))
    assert errors[1] <= errors[0]
    assert errors[1] < 1e-3


# reference_front returns (k, 2m) in the column order the solvers produce
@pytest.mark.parametrize("phi_name", phi_names)
@pytest.mark.parametrize("mode", modes)
def test_reference_front_shape_and_column_order(phi_name, mode):
    points, _ = efficient_set(p1, phi_name, 500, False, mode)
    front = reference_front(p1, phi_name, 500, False, mode)
    assert front.shape == (len(points), 2 * p1.n_obj)
    # the columns, built here from problem.evaluate and the phi record directly,
    # in the order (Lambda_1^T f, B_1^T f, Lambda_2^T f, B_2^T f) of b1 section 0.
    route = getattr(phi_registry[phi_name], "of_" + p1.representation)
    pairs = [route(*pair) for pair in p1.evaluate(points, p1_default_params)]
    expected = np.stack([pairs[0][0], pairs[0][1], pairs[1][0], pairs[1][1]], axis=-1)
    assert np.array_equal(front, expected)


# the four columns are p1's own image coordinates, b1 section 1.1, objective by objective
@pytest.mark.parametrize("mode", modes)
def test_columns_are_b1s_image_coordinates(mode):
    points, _ = efficient_set(p1, "cw", 500, False, mode)
    front = reference_front(p1, "cw", 500, False, mode)
    x_1, x_2 = points[:, 0], points[:, 1]
    rho, delta = p1_default_params["rho"], p1_default_params["delta"]
    # b1 section 1.1, phi_cw: g_1 = c_1, g_2 = r_1, g_3 = c_2, g_4 = r_2, and
    # r_1 is driven by x_2 while r_2 is driven by x_1. a transposed column order
    # would put a centre where a half-width belongs and this is where it shows.
    assert np.allclose(front[:, 0], x_1 ** 2 + (x_2 - 1.0) ** 2)
    assert np.allclose(front[:, 1], rho * x_2 ** 2 + delta)
    assert np.allclose(front[:, 2], (x_1 - 1.0) ** 2 + (x_2 - 1.0) ** 2)
    assert np.allclose(front[:, 3], rho * x_1 ** 2 + delta)


# the singular segment is b1 section 2.3's ray for phi_ls and phi_cw and absent for phi_lu
@pytest.mark.parametrize("phi_name", phi_names)
@pytest.mark.parametrize("mode", modes)
def test_the_flag_adds_the_segment_of_b1_section_2_6(phi_name, mode):
    without, _ = sampled_set(phi_name, sample_size, False, mode)
    with_segment, weights = sampled_set(phi_name, sample_size, True, mode)
    assert len(without) == len(with_segment) == sample_size
    if singular_segments[phi_name] is None:
        # b1 section 2.3: phi_lu has no singular weight at all, so the flag is a
        # no-op there and the two sets are the same object.
        assert singular_share(phi_name, sample_size, True) == 0
        assert np.array_equal(without, with_segment)
        return
    n_segment = singular_share(phi_name, sample_size, True)
    segment = with_segment[sample_size - n_segment:]
    assert np.count_nonzero(with_segment[:, 1] == 0.0) >= n_segment
    assert np.array_equal(segment[:, 1], np.zeros(n_segment))
    assert np.array_equal(weights[sample_size - n_segment:],
                          np.tile(singular_segments[phi_name][0], (n_segment, 1)))
    assert np.max(segment[:, 0]) == singular_segments[phi_name][1]


# the flag has no silent default and refuses anything that is not a stated bool
@pytest.mark.parametrize("value", (None, 1, "yes"))
def test_the_flag_must_be_stated_as_a_bool(value):
    with pytest.raises(ValueError, match="must be stated as True or False"):
        efficient_set(p1, "ls", 100, value, dirichlet_mode)


# p0 is refused, with the reason and not just a failure
def test_p0_is_refused_by_both_entry_points():
    for call in (efficient_set, reference_front):
        with pytest.raises(ValueError) as raised:
            call(p0, "lu", 100, False, dirichlet_mode)
        message = str(raised.value)
        assert "p1 only" in message
        assert "section 7.4" in message
        assert "smoke test" in message


# an unknown phi is refused
def test_an_unknown_phi_is_refused():
    with pytest.raises(ValueError, match="unknown phi"):
        efficient_set(p1, "identity", 100, False, dirichlet_mode)


# a rho other than the one b1 derived at is refused, and delta is free
@pytest.mark.parametrize("mode", modes)
def test_rho_is_fixed_and_delta_is_free(mode):
    assert derivation_rho == p1_default_params["rho"]
    with pytest.raises(ValueError, match="rho"):
        reference_front(p1, "lu", 100, False, mode, params={"rho": 0.5})
    shifted = reference_front(p1, "lu", 100, False, mode, params={"delta": 0.25})
    base = reference_front(p1, "lu", 100, False, mode)
    # delta enters every image coordinate as an additive constant, b1 section 1.2,
    # so under phi_lu it moves c - r down and c + r up by delta - delta_0, here
    # 0.25 - 0.125, and never moves the set of decision points. under the
    # farthest-point mode it also says the selection did not move: a translation
    # of the image leaves every distance in it unchanged, so the same rows are
    # kept, and had the selection been made in the caller's delta rather than the
    # derivation's the two fronts would hold different points and the difference
    # would not be constant.
    assert np.allclose(shifted[:, 0] - base[:, 0], -0.125)
    assert np.allclose(shifted[:, 1] - base[:, 1], 0.125)


# the same call twice gives the same front, so a metric computed against it is reproducible
@pytest.mark.parametrize("phi_name", phi_names)
@pytest.mark.parametrize("mode", modes)
def test_the_front_is_reproducible(phi_name, mode):
    first = reference_front(p1, phi_name, 500, True, mode)
    second = reference_front(p1, phi_name, 500, True, mode)
    assert np.array_equal(first, second)
    # bitwise and at the same seed, so a metric computed against it is
    # reproducible, and the two modes are two fronts and not one: the selection
    # keeps a tenth of a draw ten times the size, so the rows differ.
    third = reference_front(p1, phi_name, 500, True, mode, seed=20260903)
    assert not np.array_equal(first, third)
    assert set(stationarity_systems) == set(phi_names)


# the mode has no silent default and refuses anything that is not a stated value
@pytest.mark.parametrize("value", (None, True, "farthest", "dirichlet ", 0))
def test_the_sampling_mode_must_be_stated(value):
    with pytest.raises(ValueError, match="sampling_mode must be stated"):
        efficient_set(p1, "ls", 100, False, value)
    with pytest.raises(ValueError, match="sampling_mode must be stated"):
        reference_front(p1, "ls", 100, False, value)


# the kept front is a subsequence of the draw it was selected from, r-13
@pytest.mark.parametrize("phi_name", phi_names)
def test_the_selection_is_a_subsequence_of_the_oversample(phi_name):
    # the oversample is rebuilt here from the module's own draw and map at
    # oversampling_factor times the size and the same seed, so this test says the
    # farthest-point mode kept rows of that draw and invented none. it is the
    # check that the correction changed which points survive and nothing about
    # where they come from: every kept point is still x(w) at a drawn w, which is
    # what keeps the module an encoding of b1 section 2.2 and not of section 2.4.
    n_points = 500
    weights = simplex_weights(phi_name, n_points * oversampling_factor, 20260901)
    oversample = stationary_points(phi_name, weights)
    kept, kept_weights = efficient_set(p1, phi_name, n_points, False,
                                       farthest_point_mode)
    assert len(kept) == n_points
    position = 0
    for point, weight in zip(kept, kept_weights):
        while position < len(oversample) and not np.array_equal(oversample[position],
                                                                point):
            position += 1
        assert position < len(oversample)
        assert np.array_equal(weights[position], weight)
        position += 1


# the front's nearest-neighbour distances are tighter under the selection, r-13
@pytest.mark.parametrize("phi_name", phi_names)
@pytest.mark.parametrize("include_singular", (False, True))
def test_the_selection_spaces_the_front_more_evenly(phi_name, include_singular):
    # the density r-13 is about, measured directly and in objective space, since
    # that is where igd averages. the assertion is a comparison between the two
    # modes and never against a number: what the correction claims is that the
    # spacing is more even, not that it reaches any particular value, and the
    # spread is taken relative to the mean because the two modes do not have the
    # same mean spacing, the selection spreading the same count over the same
    # front more widely. docs/b2b_reference_density.md section 4 has the
    # distributions the two coefficients of variation summarise.
    drawn = reference_front(p1, phi_name, 1000, include_singular, dirichlet_mode)
    selected = reference_front(p1, phi_name, 1000, include_singular,
                               farthest_point_mode)
    drawn_distances = nearest_neighbour_distances(drawn)
    selected_distances = nearest_neighbour_distances(selected)
    drawn_spread = np.std(drawn_distances) / np.mean(drawn_distances)
    selected_spread = np.std(selected_distances) / np.mean(selected_distances)
    assert selected_spread < drawn_spread
    # and the largest gap between neighbouring points is smaller, which is the
    # same statement without a ratio. the smallest gap is not asserted with it:
    # with the flag on the segment is placed by linspace and not selected, and
    # where it runs close to the selected part of the front it makes the smallest
    # gap in the set, docs/b2b_reference_density.md section 4.
    assert np.max(selected_distances) < np.max(drawn_distances)
