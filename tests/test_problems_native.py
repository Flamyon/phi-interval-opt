# tests for f2's module, src/problems_native.py.
#
# what is worth testing in a module that encodes a paper and a derivation, and
# what is not. the derivation is docs/part2/f2_ibk1_derivation.md's and is
# verified there in exact rational arithmetic; re-deriving it here would be
# checking it against itself. what these tests check is that the encoding is
# faithful to two things outside the encoding:
#
#   the paper. [16] prints one solver-generated point with its objective values,
#   Table 1 printed page 20, and a closed-form curve with eleven points on it,
#   equation (25) and Table 2 printed page 21. the module's objective values must
#   reproduce the printed row at the printed x*, to the printed precision, and
#   that is the check that the transcription of the coefficients is right. it is
#   the only external check the project has ever had on a problem statement.
#
#   the derivation's own implementation check. f2 section 7 hands f3 exactly one:
#   any encoding of X_lu must contain the curve of equation (25) along its whole
#   length, nu = 162/169. and one prohibition: Table 1's x* is **not** a fixture,
#   f2 section 4.2 having shown it is outside all three derived sets and is not a
#   Pareto optimal point of I-BK1 in [16]'s own definition 2.17. so x* is encoded
#   here as a point that must be outside, which is the only way to write it down
#   that a later session cannot mistake for a front to hit.
#
#   the sampling. every point the module samples must satisfy f2 section 2.4's
#   inequalities under the phi it was sampled for, in both sampling modes, and
#   the two containments f2 section 3.1 states must hold on the encoded sets and
#   not merely on the bands they were read from.
#
# no tolerance is used to decide any membership: f2 section 2.4's inequalities
# are cleared of denominators and their coefficients are integers, so
# in_region compares products of a point's own coordinates against small integer
# multiples and rounds nothing. the one numeric comparison in this file with a
# scale on it is the comparison against the paper's printed row, and that scale
# is the paper's last printed place and not a tolerance the project chose.

import numpy as np
import pytest

from problems_native import (band_ends, curve_x_2, derived_bands, efficient_set,
                             farthest_point_mode, ibk1, ibk1_shift, in_region,
                             nu_at, parametrisation_mode, reference_front)

# the three phi in the lu, ls, cw order of examples 2.2, 2.3 and 2.4 of [1]
phi_names = ("lu", "ls", "cw")

# [16] Table 1, printed page 20, last row, k = 12, transcribed in
# docs/part2/lit_review.md section 1.6 and re-read in f2 section 4.2. x* is the
# output of the paper's algorithm 1 and G(x*) is the row printed beside it, in
# the column order (G_1 lower, G_1 upper, G_2 lower, G_2 upper).
printed_x_star = (3.914930, 1.428474)
printed_g_star = (1.736722, 3.677497, 1.393317, 6.731112)

# the paper prints six decimals, so a value recomputed at the printed x* can
# differ from the printed row by the rounding of both. one unit in the last
# printed place is the paper's own precision and is not a tolerance chosen here:
# f2 section 4.2 reports the largest gap as 5.13e-07 and the derivation's verdict
# on x* rests on margins five orders of magnitude larger.
printed_precision = 1e-6

# f2 section 4.2's dominator of x*, found by exhaustive search there and reported
# as the widest-margin one. it is a point of the box and it is here as the
# fixture the run's own measurement is read against, not as a solution.
f2_dominator = (2.897500, 2.397500)

# the exact coefficients of [16] equation (24), re-derived in
# docs/part2/lit_review.md section 1.6 and again in exact rationals in f2 section
# 4.1: the printed 0.15, 0.21667, 0.21667 and 0.3 are 3/20, 13/60, 13/60 and
# 3/10, the middle two being 13/60 = 0.216666... rounded.
curve_a = 3.0 / 20.0
curve_b = 13.0 / 60.0
curve_c = 3.0 / 10.0

# the constant value of nu along equation (25)'s curve, f2 section 4.1:
# nu = a c / b^2 = 162/169, the same number at every alpha.
curve_nu = 162.0 / 169.0

# how many points the sampling tests draw. small enough to stay a fast test and
# large enough that a wedge boundary would be crossed if the encoding were wrong.
sample_points = 400


# the four endpoint values of I-BK1 at one point, in the printed column order
def objective_row(point):
    pairs = ibk1.evaluate(np.array([point], dtype=float))
    return tuple(float(value[0]) for pair in pairs for value in pair)


# equation (25) of [16] at one alpha, from the exact coefficients of (24)
def curve_point(alpha):
    return (ibk1_shift * curve_b * alpha / (curve_a * (1.0 - alpha)
                                            + curve_b * alpha),
            ibk1_shift * curve_c * alpha / (curve_b * (1.0 - alpha)
                                            + curve_c * alpha))


# the problem record says what [16] printed page 27 says
def test_problem_record_matches_the_paper():
    lower, upper = ibk1.bounds()
    assert (ibk1.n_vars, ibk1.n_obj) == (2, 2)
    assert ibk1.representation == "endpoints"
    assert lower.tolist() == [-10.0, -10.0]
    assert upper.tolist() == [10.0, 10.0]


# evaluate returns one endpoint pair per interval objective, over the population
def test_evaluate_returns_m_endpoint_pairs():
    x = np.array([[0.0, 0.0], [1.0, 2.0], [5.0, 5.0]])
    pairs = ibk1.evaluate(x)
    assert len(pairs) == ibk1.n_obj
    for lower, upper in pairs:
        assert lower.shape == (3,)
        assert upper.shape == (3,)
        # every coefficient interval of I-BK1 is non-degenerate on both terms,
        # f2 section 1.2, so the width is zero only where both basis functions
        # vanish, which is the objective's own support point.
        assert np.all(upper >= lower)


# the paper's own printed G(x*) reproduces from the module at the printed x*
def test_printed_objective_row_reproduces():
    # the transcription check, and the only one available: [16] printed page 20
    # prints both x* and G(x*), so the module's coefficients can be read against
    # the paper's own arithmetic rather than against this project's.
    computed = objective_row(printed_x_star)
    for value, printed in zip(computed, printed_g_star):
        assert abs(value - printed) < printed_precision


# f2 section 4.2's dominator beats the paper's printed row in all four values
def test_f2_dominator_is_strictly_below_the_printed_row():
    # not a claim about the paper made here: the claim is f2 section 4.2's and
    # the algebra is there. this asserts that the module's arithmetic is the one
    # that argument was made in, so the run's own measurement is read against the
    # same four numbers.
    computed = objective_row(f2_dominator)
    assert all(value < printed for value, printed in zip(computed, printed_g_star))


# the three bands are f2 section 2.4's, in strict order and none containing another
def test_bands_are_strictly_nested():
    ends = {name: band_ends(name) for name in phi_names}
    assert ends["ls"][0] < ends["lu"][0] < ends["cw"][0]
    assert ends["cw"][1] < ends["lu"][1] < ends["ls"][1]


# the two corners every derived set is pinned at lie in all three
def test_the_two_corners_lie_in_every_region():
    # f2 section 2.4: (0, 0), where the first objective's half-width vanishes,
    # and (5, 5), where the second's does. the cleared inequalities cover them
    # without a case split and that is why the encoding is in that form.
    corners = np.array([[0.0, 0.0], [ibk1_shift, ibk1_shift]])
    for name in phi_names:
        assert in_region(name, corners).tolist() == [True, True]


# equation (25)'s published curve lies inside all three derived sets
def test_published_curve_lies_inside_every_region():
    # f2 section 4.1, the external check that passes and the one f2 section 7
    # hands this module as its implementation check. alpha = 0 and alpha = 1 are
    # the two corners and are covered by the test above.
    alphas = np.linspace(0.0, 1.0, 51)[1:-1]
    points = np.array([curve_point(float(alpha)) for alpha in alphas])
    assert np.allclose(nu_at(points), curve_nu)
    for name in phi_names:
        assert bool(np.all(in_region(name, points)))


# Table 1's x* lies outside all three derived sets and is not a fixture
def test_printed_x_star_lies_outside_every_region():
    # f2 section 4.2. it is written down as an exclusion so that no later session
    # can read it as a point a front should contain: nu(x*) = 0.110854 against
    # band lower ends of 1/2, 2/3 and 3/4.
    point = np.array([printed_x_star])
    assert float(nu_at(point)[0]) < min(band_ends(name)[0] for name in phi_names)
    for name in phi_names:
        assert not bool(in_region(name, point)[0])


# every point of a sampled set satisfies its own phi's inequalities
@pytest.mark.parametrize("phi_name", phi_names)
@pytest.mark.parametrize("mode", (parametrisation_mode, farthest_point_mode))
def test_sampled_points_lie_in_their_region(phi_name, mode):
    points, parameters = efficient_set(phi_name, sample_points, mode)
    assert points.shape == (sample_points, 2)
    assert parameters.shape == (sample_points, 2)
    assert bool(np.all(in_region(phi_name, points)))


# the parameters travel with the points and reproduce them exactly
def test_parameters_reproduce_their_points():
    # the b2 discipline: the caller holds x and the parametrisation value that
    # produced it, so a kept point is still a point of f2's own curve family and
    # not something the selection invented.
    points, parameters = efficient_set("lu", sample_points, farthest_point_mode)
    rebuilt = curve_x_2(parameters[:, 0], parameters[:, 1])
    assert np.array_equal(points[:, 0], parameters[:, 1])
    assert np.array_equal(points[:, 1], rebuilt)


# the correction changes which points survive and not what they are
def test_the_two_modes_differ():
    # docs/part1/b2b_reference_density.md, r-13: the mode names a different
    # object and is why it has no default. if the two returned the same rows the
    # column would be decoration.
    drawn, _ = efficient_set("cw", sample_points, parametrisation_mode)
    kept, _ = efficient_set("cw", sample_points, farthest_point_mode)
    assert not np.array_equal(drawn, kept)


# the containments f2 section 3.1 states hold on the encoded sets
@pytest.mark.parametrize("inner,outer", (("cw", "lu"), ("cw", "ls"), ("lu", "ls")))
def test_derived_sets_are_nested(inner, outer):
    # two of the three are predicted by docs/part1/a_close_containment.md and are
    # checks on the derivation; X_cw inside X_lu is not predicted and is f2
    # section 3.2's finding about I-BK1. all three are asserted on the encoding
    # because a band read wrongly into an inequality would break them.
    points, _ = efficient_set(inner, sample_points, parametrisation_mode)
    assert bool(np.all(in_region(outer, points)))


# the nesting holds on a grid of the quadrant and not only on the sampled sets
def test_nesting_holds_on_a_grid():
    side = np.linspace(0.0, ibk1_shift, 200)
    grid_1, grid_2 = np.meshgrid(side, side, indexing="ij")
    grid = np.column_stack([grid_1.ravel(), grid_2.ravel()])
    inside = {name: in_region(name, grid) for name in phi_names}
    assert bool(np.all(inside["cw"] <= inside["lu"]))
    assert bool(np.all(inside["lu"] <= inside["ls"]))
    # and none of the three is the whole quadrant, f2 section 3.3
    for name in phi_names:
        assert 0 < int(np.count_nonzero(inside[name])) < len(grid)


# the reference front is the image of the derived set, with 2m columns
def test_reference_front_is_the_image_of_the_efficient_set():
    points, _ = efficient_set("ls", sample_points, farthest_point_mode)
    front = reference_front("ls", sample_points, farthest_point_mode)
    assert front.shape == (sample_points, 2 * ibk1.n_obj)
    # the column order is (Lambda_1^T f, B_1^T f, Lambda_2^T f, B_2^T f), and
    # under phi_ls the first column of each objective is that objective's lower
    # endpoint, [1] example 2.3. so column 0 is G_1 lower at the same points.
    lower_1, _ = ibk1.evaluate(points)[0]
    assert np.array_equal(front[:, 0], lower_1)


# a phi with no derived region and an unstated sampling mode are both refused
def test_the_two_guards_raise():
    with pytest.raises(ValueError, match="section 2.4"):
        in_region("centre", np.array([[1.0, 1.0]]))
    with pytest.raises(ValueError, match="sampling_mode"):
        efficient_set("lu", sample_points, None)
    assert sorted(derived_bands) == ["cw", "ls", "lu"]
