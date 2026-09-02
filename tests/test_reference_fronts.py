# tests for src/reference_fronts.py, subpart b2.
# the module encodes docs/b1_phi_efficient_sets.md sections 2.1 to 2.6 as the map
# w -> x(w) and a weight sample. these tests check the encoding against b1 from
# the other side: the closed-form regions of b1 section 2.4 are written out here
# and nowhere in the module, so a test passing means the sampled points landed
# where the derivation says they should and not that one file agrees with itself.

import numpy as np
import pytest

from phi_transforms import phi_registry
from problems_tier0 import p0, p1, p1_default_params
from reference_fronts import (
    derivation_rho,
    efficient_set,
    reference_front,
    singular_segments,
    singular_share,
    stationarity_systems,
    transformed_image,
)

phi_names = ("lu", "ls", "cw")
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


# every sampled point satisfies condition (15) with the weight recorded beside it
@pytest.mark.parametrize("phi_name", phi_names)
@pytest.mark.parametrize("include_singular", (False, True))
def test_condition_15_holds_at_every_sampled_point(phi_name, include_singular):
    points, weights = efficient_set(p1, phi_name, sample_size, include_singular)
    gradient = weighted_gradient(p1, points, phi_registry[phi_name], weights,
                                 p1_default_params)
    # the weights sum to one on the regular part and to one on the singular ray
    # too, so the gradient is on the scale of the image coordinates themselves and
    # the bound is absolute. central differences on a quadratic at step 1e-5 carry
    # a rounding error of order eps |g| / step, which is about 1e-11 here.
    assert np.max(np.abs(gradient)) < 1e-7


# the recorded weights are the admissible ones of example 3.9, w >= 0 and not all zero
@pytest.mark.parametrize("phi_name", phi_names)
def test_recorded_weights_are_admissible(phi_name):
    _, weights = efficient_set(p1, phi_name, sample_size, True)
    assert np.min(weights) >= 0.0
    assert np.min(np.sum(weights, axis=1)) > 0.0


# every sampled point lies inside b1 section 2.4's closed form for its own phi
@pytest.mark.parametrize("phi_name", phi_names)
@pytest.mark.parametrize("include_singular", (False, True))
def test_sampled_points_lie_in_the_derived_region(phi_name, include_singular):
    points, _ = efficient_set(p1, phi_name, sample_size, include_singular)
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
def test_no_dense_sample_point_dominates_the_front(phi_name, include_singular):
    sample = dense_box_sample(p1, 20000, seed=20260901)
    sample_image = transformed_image(p1, sample, phi_registry[phi_name],
                                     p1_default_params)
    front = reference_front(p1, phi_name, sample_size, include_singular)
    assert dominated_count(front, sample_image) == 0


# the containment of docs/a_close_containment.md, asserted on the encoded sets.
# b1 section 5 verified it on the closed forms; it is asserted here because an
# encoding bug would break it, and it is a check on this module and never
# evidence for the containment itself, which stands on s-11.
@pytest.mark.parametrize("phi_name", ("lu", "cw"))
def test_lu_and_cw_points_satisfy_the_ls_region(phi_name):
    points, _ = efficient_set(p1, phi_name, sample_size, False)
    assert region_excess("ls", points) <= 1e-12


# b1 section 2.4's extreme values are approached as the sampling density rises
@pytest.mark.parametrize("phi_name,coordinate,target,reduce_name", (
    ("lu", 0, four_thirds, "max"),
    ("lu", 1, four_thirds, "max"),
    ("lu", 1, four_fifths, "min"),
    ("ls", 0, four_thirds, "max"),
    ("ls", 1, four_thirds, "max"),
    ("cw", 0, 1.0, "max"),
    ("cw", 1, 1.0, "max"),
))
def test_extreme_points_are_approached_with_density(phi_name, coordinate, target,
                                                    reduce_name):
    errors = []
    for n_points in (200, 2000, 20000):
        points, _ = efficient_set(p1, phi_name, n_points, False)
        reached = getattr(np, reduce_name)(points[:, coordinate])
        errors.append(abs(reached - target))
    # convergence, not equality at a fixed n: the error never grows with density
    # and is negligible at the top of the range. a weight sample reaches these
    # values only in the limit, b1 section 2.4, since each needs a zero weight.
    assert errors[1] <= errors[0]
    assert errors[2] <= errors[1]
    assert errors[2] < 1e-3


# reference_front returns (k, 2m) in the column order the solvers produce
@pytest.mark.parametrize("phi_name", phi_names)
def test_reference_front_shape_and_column_order(phi_name):
    points, _ = efficient_set(p1, phi_name, 500, False)
    front = reference_front(p1, phi_name, 500, False)
    assert front.shape == (len(points), 2 * p1.n_obj)
    # the columns, built here from problem.evaluate and the phi record directly,
    # in the order (Lambda_1^T f, B_1^T f, Lambda_2^T f, B_2^T f) of b1 section 0.
    route = getattr(phi_registry[phi_name], "of_" + p1.representation)
    pairs = [route(*pair) for pair in p1.evaluate(points, p1_default_params)]
    expected = np.stack([pairs[0][0], pairs[0][1], pairs[1][0], pairs[1][1]], axis=-1)
    assert np.array_equal(front, expected)


# the four columns are p1's own image coordinates, b1 section 1.1, objective by objective
def test_columns_are_b1s_image_coordinates():
    points, _ = efficient_set(p1, "cw", 500, False)
    front = reference_front(p1, "cw", 500, False)
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
def test_the_flag_adds_the_segment_of_b1_section_2_6(phi_name):
    without, _ = efficient_set(p1, phi_name, sample_size, False)
    with_segment, weights = efficient_set(p1, phi_name, sample_size, True)
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
        efficient_set(p1, "ls", 100, value)


# p0 is refused, with the reason and not just a failure
def test_p0_is_refused_by_both_entry_points():
    for call in (efficient_set, reference_front):
        with pytest.raises(ValueError) as raised:
            call(p0, "lu", 100, False)
        message = str(raised.value)
        assert "p1 only" in message
        assert "section 7.4" in message
        assert "smoke test" in message


# an unknown phi is refused
def test_an_unknown_phi_is_refused():
    with pytest.raises(ValueError, match="unknown phi"):
        efficient_set(p1, "identity", 100, False)


# a rho other than the one b1 derived at is refused, and delta is free
def test_rho_is_fixed_and_delta_is_free():
    assert derivation_rho == p1_default_params["rho"]
    with pytest.raises(ValueError, match="rho"):
        reference_front(p1, "lu", 100, False, params={"rho": 0.5})
    shifted = reference_front(p1, "lu", 100, False, params={"delta": 0.25})
    base = reference_front(p1, "lu", 100, False)
    # delta enters every image coordinate as an additive constant, b1 section 1.2,
    # so under phi_lu it moves c - r down and c + r up by delta - delta_0, here
    # 0.25 - 0.125, and never moves the set of decision points.
    assert np.allclose(shifted[:, 0] - base[:, 0], -0.125)
    assert np.allclose(shifted[:, 1] - base[:, 1], 0.125)


# the same call twice gives the same front, so a metric computed against it is reproducible
@pytest.mark.parametrize("phi_name", phi_names)
def test_the_front_is_reproducible(phi_name):
    first = reference_front(p1, phi_name, 500, True)
    second = reference_front(p1, phi_name, 500, True)
    assert np.array_equal(first, second)
    assert set(stationarity_systems) == set(phi_names)
