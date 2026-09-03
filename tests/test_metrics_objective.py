# tests for src/metrics_objective.py, subpart d1.
# three groups. the first checks each metric against a hand-computed answer and,
# where pymoo ships the indicator the module delegates to, against that indicator
# on the same input, so a wrapper that started normalising or filtering would be
# caught; the two properties the definitions have to satisfy, igd zero against
# the front it is measured on and hypervolume monotone under a non-dominated
# addition, are here too. the second is the truncation of r-16, which every
# comparison across solvers goes through and which therefore has to be exactly
# reproducible. the third is the two regressions: that no reference has a silent
# default, and that the two sampling modes of b2-b still rank a mirror pair in
# opposite orders, which is the reason d1 computes igd against the corrected
# reference and not the drawn one.

import inspect

import numpy as np
import pytest
from pymoo.indicators.hv import HV
from pymoo.indicators.igd import IGD
from pymoo.indicators.spacing import SpacingIndicator

from metrics_objective import (common_cardinality, compute_hv, compute_igd,
                               compute_spread, derive_reference_point,
                               igd_reference, nadir_margin_fraction,
                               nadir_margin_rule, nadir_rule,
                               truncate_to_common_cardinality)
from problems_tier0 import p1, p1_default_params
from random_search import run_random_search
from reference_fronts import (dirichlet_mode, farthest_point_indices,
                              farthest_point_mode, reference_front,
                              weight_sample_seed)

phi_names = ("lu", "ls", "cw")
modes = (dirichlet_mode, farthest_point_mode)
# the reference size the reference-front tests run at. it is a test size and not
# a project one: the farthest-point mode draws ten times it and selects
# quadratically in what it keeps, so 300 keeps the whole file inside the fast run
# while still giving a front the fill-distance bound is not trivial on.
reference_size = 300
# the budget the one solver run in this file uses. the same order as the 2000 of
# tests/test_random_search.py, and it is a test size for the same reason.
n_evals = 2000
seed = 11


# the largest distance from a point of the covering set to the nearest candidate
def fill_distance(candidate, covering, block=512):
    out = np.empty(len(covering))
    for start in range(0, len(covering), block):
        rows = covering[start:start + block]
        gaps = rows[:, None, :] - candidate[None, :, :]
        out[start:start + block] = np.sqrt(np.min(np.sum(np.square(gaps), axis=2),
                                                  axis=1))
    return float(np.max(out))


# every reference front this file has built, so one call serves every test asking
# for the same arguments. the farthest-point selection is quadratic in what it
# keeps and rebuilding it per test would put minutes in the fast run for nothing.
built_references = {}


# one call of reference_front per distinct set of arguments, shared by the tests
def reference_cache(phi_name, n_points, mode, front_seed=weight_sample_seed):
    key = (phi_name, n_points, mode, front_seed)
    if key not in built_references:
        built_references[key] = reference_front(p1, phi_name, n_points, False, mode,
                                                None, front_seed)
    return built_references[key]


# hypervolume of two hand-placed points against a hand-placed reference point
def test_hv_on_a_hand_computed_case():
    # the two points (0, 1) and (1, 0) against the reference point (2, 2). the
    # region dominated by (0, 1) inside the box is 2 by 1 and the region
    # dominated by (1, 0) is 1 by 2, and they overlap in the 1 by 1 square below
    # and right of (1, 1), so the union is 2 + 2 - 1 = 3.
    front = np.array([[0.0, 1.0], [1.0, 0.0]])
    assert compute_hv(front, np.array([2.0, 2.0])) == pytest.approx(3.0)


# hypervolume of one point in four dimensions is the box between it and the point
def test_hv_in_four_dimensions_is_the_box_of_one_point():
    # 2m is four here, which is p1's own image dimension, and one point's
    # dominated region is the product of the four gaps, 1 * 2 * 3 * 4 = 24.
    front = np.array([[0.0, 0.0, 0.0, 0.0]])
    assert compute_hv(front, np.array([1.0, 2.0, 3.0, 4.0])) == pytest.approx(24.0)


# compute_hv is pymoo's indicator on the same input and adds no transformation
@pytest.mark.parametrize("phi_name", phi_names)
def test_hv_matches_pymoos_indicator(phi_name):
    # the wrapper passes the reference point through unnormalised, which is what
    # this pins: pymoo's Hypervolume normalises the point when zero_to_one is
    # enabled, and enabling it would silently change every number in a table.
    front = reference_cache(phi_name, reference_size, farthest_point_mode)
    point = derive_reference_point(front, nadir_margin_rule).point
    assert compute_hv(front, point) == HV(ref_point=point)(front)


# adding a point no member of the front dominates does not lower the hypervolume
@pytest.mark.parametrize("added", ([0.5, 0.5], [-0.5, 1.5], [1.5, -0.5]))
def test_hv_is_monotone_under_adding_a_non_dominated_point(added):
    # monotonicity is the property the metric is read for, so it is asserted and
    # not assumed. each of the three is worse than one of the two rows in one
    # column and better in the other, so none of them is dominated and none
    # dominates, and each adds a region neither of the two covers: the square
    # (0.5, 1) by (0.5, 1) for the first and a slab beyond the box's own corner
    # for the other two.
    front = np.array([[0.0, 1.0], [1.0, 0.0]])
    point = np.array([2.0, 2.0])
    grown = np.concatenate([front, np.array([added])])
    assert compute_hv(grown, point) > compute_hv(front, point)


# the same front against two reference points is two numbers
def test_hv_moves_with_the_reference_point():
    # the reason the point is an argument and is recorded in every table,
    # CONTEXT.md section 10 d1. the box grows by one in each coordinate and the
    # dominated region grows with it, so the two numbers are not the same number.
    front = np.array([[0.0, 1.0], [1.0, 0.0]])
    assert compute_hv(front, np.array([2.0, 2.0])) < compute_hv(front,
                                                                np.array([3.0, 3.0]))


# a row lying beyond the reference point contributes nothing and raises nothing
def test_hv_clips_a_row_beyond_the_reference_point():
    # moocore's behaviour, v-59, asserted here because it is silent: (3, 0.5) is
    # outside the box the point (2, 2) closes, so the number is (0, 1)'s box
    # alone, 2 by 1. a reference point that does not dominate the whole front
    # therefore discards part of it without saying so, which is why the point is
    # an argument, is derived by a stated rule and is recorded in every table.
    front = np.array([[0.0, 1.0], [3.0, 0.5]])
    assert compute_hv(front, np.array([2.0, 2.0])) == pytest.approx(2.0)


# a reference point that is not one point of the front's own image is refused
def test_hv_refuses_a_reference_point_of_the_wrong_dimension():
    front = np.array([[0.0, 1.0, 2.0, 3.0]])
    with pytest.raises(ValueError, match="reference_point must be one point"):
        compute_hv(front, np.array([1.0, 1.0]))


# igd of two hand-placed points against two hand-placed reference points
def test_igd_on_a_hand_computed_case():
    # the reference points are (0, 0) and (1, 1) and the front is (0, 1) and
    # (1, 0). every one of the four distances is 1, so both minima are 1 and the
    # average over the two reference points is 1.
    front = np.array([[0.0, 1.0], [1.0, 0.0]])
    reference = np.array([[0.0, 0.0], [1.0, 1.0]])
    assert compute_igd(front, reference) == pytest.approx(1.0)


# compute_igd is pymoo's indicator on the same input and adds no transformation
@pytest.mark.parametrize("phi_name", phi_names)
def test_igd_matches_pymoos_indicator(phi_name):
    reference = reference_cache(phi_name, reference_size, farthest_point_mode)
    front = truncate_to_common_cardinality(reference, 100, 4242)
    assert compute_igd(front, reference) == IGD(reference)(front)


# igd averages over the reference points and not over the front points
def test_igd_averages_over_the_reference_and_not_over_the_front():
    # the direction is the whole of r-13: docs/b2b_reference_density.md section 1
    # states igd as the average over the reference, which is what makes the
    # reference's density a bias on the number. the two directions are different
    # quantities and this is the check that pymoo computes the one the project
    # means, and not [2]'s M_1^*, equation (17), which averages over the front.
    front = np.array([[0.0, 0.0], [10.0, 10.0]])
    reference = np.array([[0.0, 0.0]])
    # one reference point, at a row of the front, so the average over the
    # reference is zero; the average over the front of the distance to that same
    # reference is (0 + sqrt(200)) / 2, and the two calls give the two numbers.
    assert compute_igd(front, reference) == 0.0
    assert compute_igd(reference, front) == pytest.approx(np.sqrt(200.0) / 2.0)


# igd of the reference front against itself is exactly zero
@pytest.mark.parametrize("phi_name", phi_names)
@pytest.mark.parametrize("mode", modes)
def test_igd_of_the_reference_front_against_itself_is_zero(phi_name, mode):
    # every reference point is a front point, so every minimum is a distance
    # from a row to itself. it is asserted as zero and not as approximately
    # zero: the difference is formed on identical doubles, d-02.
    reference = reference_cache(phi_name, reference_size, mode)
    assert compute_igd(reference, reference) == 0.0


# igd of a subsample of the reference front is bounded by the subsample's fill distance
@pytest.mark.parametrize("phi_name", phi_names)
def test_igd_of_a_subsample_is_bounded_by_its_fill_distance(phi_name):
    # igd is the mean over the reference of the distance to the nearest kept
    # point and the fill distance is the maximum of the same distances, so the
    # bound holds by construction and what it checks is that the two are computed
    # over the same set in the same direction. it is not vacuous: the subsample
    # is a tenth of the front, so both numbers are away from zero.
    reference = reference_cache(phi_name, reference_size, farthest_point_mode)
    subsample = truncate_to_common_cardinality(reference, 30, 7)
    measured = compute_igd(subsample, reference)
    assert 0.0 < measured <= fill_distance(subsample, reference)


# spread of a hand-placed front is the norm of its per-column ranges
def test_spread_on_a_hand_computed_case():
    # [2] definition 6 equation (19): the maximum over pairs of the difference in
    # column i is that column's range, so the metric is sqrt(3^2 + 4^2) = 5 here.
    front = np.array([[0.0, 0.0], [3.0, 4.0], [1.0, 2.0]])
    assert compute_spread(front) == pytest.approx(5.0)


# a front spanning more of its image space has the larger spread
def test_spread_prefers_the_wider_front():
    # the direction [2] page 181 gives: M_3^* is the range the front spreads out
    # over, so larger is wider. the two fronts carry the same eleven points and
    # differ only in the interval they occupy, the clustered one sitting inside
    # the middle fifth of the other.
    spread_out = np.column_stack([np.linspace(0.0, 10.0, 11),
                                  np.linspace(10.0, 0.0, 11)])
    clustered = np.column_stack([np.linspace(4.0, 6.0, 11),
                                 np.linspace(6.0, 4.0, 11)])
    assert compute_spread(spread_out) > compute_spread(clustered)


# spread reads the extremes of each column and nothing between them
def test_spread_reads_only_the_extremes_of_each_column():
    # the limitation of the definition, asserted so that it is recorded rather
    # than discovered by a table: a front that piles its interior points into one
    # cluster scores exactly as one that distributes them, the two extremes being
    # the same. [2]'s own distribution metric is M_2^*, equation (18), and it
    # takes a neighbourhood parameter, which the signature CONTEXT.md section 10
    # d1 fixes has no room for.
    even = np.column_stack([np.linspace(0.0, 1.0, 5), np.linspace(1.0, 0.0, 5)])
    piled = np.array([[0.0, 1.0], [0.5, 0.5], [0.5, 0.5], [0.5, 0.5], [1.0, 0.0]])
    assert compute_spread(piled) == compute_spread(even)


# compute_spread is not pymoo's spacing indicator, which is a different quantity
def test_spread_is_not_pymoos_spacing():
    # pymoo 0.6.2 ships indicators/spacing.py, a spread of the nearest-neighbour
    # distances in the cityblock metric normalised by the number of points. that
    # quantity is defined in none of the papers this project has read, so it is
    # not what compute_spread returns, and the difference is pinned here rather
    # than left to a reader who assumes every pymoo indicator was used.
    # v-59's numbers: on these four rows the nearest-neighbour distances in the
    # cityblock metric are 3, 1.5, 1.5 and 2.5, whose spread about their mean of
    # 2.125 is 0.649519052838329 normalised by n and 0.75 normalised by n - 1.
    # pymoo returns the first, and compute_spread returns neither, being the norm
    # of the per-column ranges, sqrt(4^2 + 3^2) = 5.
    front = np.array([[0.0, 3.0], [1.0, 1.0], [2.0, 0.5], [4.0, 0.0]])
    assert SpacingIndicator()(front) == pytest.approx(0.649519052838329)
    assert compute_spread(front) == pytest.approx(5.0)


# the truncation returns exactly the cardinality it was asked for
@pytest.mark.parametrize("n_keep", (1, 17, 100))
def test_the_truncation_returns_exactly_the_requested_cardinality(n_keep):
    reference = reference_cache("lu", reference_size, farthest_point_mode)
    assert len(truncate_to_common_cardinality(reference, n_keep, 3)) == n_keep


# every row the truncation returns is a row of its input, in the input's order
def test_the_truncation_returns_a_subset_of_its_input():
    # a subsequence and not a reordering, so a caller holding the front and the
    # truncation can pair them by walking both once.
    reference = reference_cache("cw", reference_size, farthest_point_mode)
    kept = truncate_to_common_cardinality(reference, 40, 5)
    position = 0
    for row in kept:
        while position < len(reference) and not np.array_equal(reference[position],
                                                               row):
            position += 1
        assert position < len(reference)
        position += 1


# the truncation is bitwise reproducible at a fixed seed and moves with the seed
def test_the_truncation_is_reproducible_bitwise_at_a_fixed_seed():
    # every metric compared across solvers goes through this function, so a draw
    # that was not reproducible would make the whole comparison unrepeatable.
    reference = reference_cache("ls", reference_size, farthest_point_mode)
    first = truncate_to_common_cardinality(reference, 50, 20260903)
    second = truncate_to_common_cardinality(reference, 50, 20260903)
    assert np.array_equal(first, second)
    other = truncate_to_common_cardinality(reference, 50, 20260904)
    assert not np.array_equal(first, other)


# the truncation refuses a cardinality it cannot reach by dropping rows
@pytest.mark.parametrize("n_keep, message", ((0, "at least 1"), (-3, "at least 1"),
                                             (reference_size + 1, "never upward")))
def test_the_truncation_refuses_an_impossible_cardinality(n_keep, message):
    reference = reference_cache("lu", reference_size, farthest_point_mode)
    with pytest.raises(ValueError, match=message):
        truncate_to_common_cardinality(reference, n_keep, 1)


# the common cardinality is the smallest front over the whole comparison
def test_common_cardinality_is_the_smallest_front_in_the_comparison():
    # taken across phi and not per phi, r-16: the fronts of the three phi go into
    # one call, and the answer is one number every one of them is cut to.
    fronts = [reference_cache(name, size, farthest_point_mode)
              for name, size in zip(phi_names, (reference_size, 120, 200))]
    assert common_cardinality(fronts) == 120
    assert common_cardinality(fronts[:1]) == reference_size


# the reference point rules are the hand-computed ones and carry their own name
def test_derive_reference_point_states_its_rule():
    # the two columns run over (1, 3) and (2, 6), so the ranges are 2 and 4 and
    # are not the nadir itself, which is what separates the two rules here
    rows = np.array([[1.0, 6.0], [3.0, 2.0]])
    strict = derive_reference_point(rows, nadir_rule)
    assert strict.rule == nadir_rule
    assert strict.n_rows == 2
    # the nadir is the componentwise maximum, (3, 6)
    assert np.array_equal(strict.point, np.array([3.0, 6.0]))
    # and the margin rule adds a tenth of each range, giving (3.2, 6.4)
    margin = derive_reference_point(rows, nadir_margin_rule)
    assert margin.rule == nadir_margin_rule
    assert margin.point == pytest.approx(np.array([3.2, 6.4]))
    assert nadir_margin_fraction == 0.1


# a reference point rule the module does not name is refused
@pytest.mark.parametrize("rule", (None, "nadir", "", 0))
def test_derive_reference_point_refuses_an_unnamed_rule(rule):
    with pytest.raises(ValueError, match="rule must be stated"):
        derive_reference_point(np.array([[0.0, 1.0]]), rule)


# no parameter of any entry point carries a default, so no reference is implicit
def test_no_reference_argument_has_a_default():
    # the rule CONTEXT.md section 10 d1 states, made mechanical: sampling_mode,
    # include_singular_segments and the hypervolume reference point are the three
    # named there, and the seed, the point count and the rule are reporting
    # parameters on the same footing. a default on any of them would let a table
    # carry a metric whose reference nobody stated.
    entry_points = (compute_hv, compute_igd, compute_spread, derive_reference_point,
                    igd_reference, truncate_to_common_cardinality)
    for function in entry_points:
        for name, parameter in inspect.signature(function).parameters.items():
            assert parameter.default is inspect.Parameter.empty, (function, name)


# a metric called without its reference raises rather than choosing one
def test_the_metrics_refuse_to_run_without_their_reference():
    front = reference_cache("lu", reference_size, farthest_point_mode)
    with pytest.raises(TypeError):
        compute_hv(front)
    with pytest.raises(TypeError):
        compute_igd(front)
    with pytest.raises(TypeError):
        truncate_to_common_cardinality(front, 10)
    with pytest.raises(TypeError):
        igd_reference(p1, "lu", 100, False, farthest_point_mode, None)


# the igd reference states its mode and its flag and refuses either unstated
def test_igd_reference_carries_and_refuses_its_reporting_parameters():
    # the values are on the record and not only at the call site, so a table
    # built from it prints them beside the size, r-12, r-13 and s-12.
    record = igd_reference(p1, "cw", 120, True, farthest_point_mode, None,
                           weight_sample_seed)
    assert (record.phi_name, record.n_points) == ("cw", 120)
    assert (record.include_singular_segments, record.sampling_mode) == (
        True, farthest_point_mode)
    assert record.seed == weight_sample_seed
    assert record.front.shape == (120, 4)
    # and src/reference_fronts.py's own refusals travel through unchanged
    with pytest.raises(ValueError, match="sampling_mode must be stated"):
        igd_reference(p1, "cw", 120, True, None, None, weight_sample_seed)
    with pytest.raises(ValueError, match="include_singular_segments must be stated"):
        igd_reference(p1, "cw", 120, None, farthest_point_mode, None,
                      weight_sample_seed)


# a decision set is refused where a front is asked for
@pytest.mark.parametrize("rows", (np.zeros((0, 4)), np.zeros(4)))
def test_the_metrics_refuse_something_that_is_not_a_front(rows):
    with pytest.raises(ValueError, match="front must"):
        compute_spread(rows)


# the two halves the mirror pair of docs/b2b_reference_density.md section 6 is built on
def mirror_pair_fronts(phi_name, n_ref, pool_size, k, m_dense):
    drawn = reference_cache(phi_name, n_ref, dirichlet_mode)
    corrected = reference_cache(phi_name, n_ref, farthest_point_mode)
    pool = reference_cache(phi_name, pool_size, dirichlet_mode, 5001)
    median = float(np.median(corrected[:, 0]))
    lower = pool[pool[:, 0] <= median]
    upper = pool[pool[:, 0] > median]
    # the dense half is the one the drawn reference overfills, counted and not
    # assumed: docs/b2b_reference_density.md section 6.1 finds it the upper half
    # under phi_lu and the lower half under phi_ls and phi_cw.
    dense_is_lower = int(np.count_nonzero(drawn[:, 0] <= median)) > len(drawn) / 2
    dense, sparse = (lower, upper) if dense_is_lower else (upper, lower)

    # m points of the dense half and k - m of the sparse one, each half selected
    # by b2-b's own farthest-point selection so that within a half the points are
    # as evenly spread as the correction itself would make them
    def build(m):
        return np.concatenate([dense[farthest_point_indices(dense, m)],
                               sparse[farthest_point_indices(sparse, k - m)]])

    return build(m_dense), build(k - m_dense), drawn, corrected, dense_is_lower


# the two sampling modes rank a mirror pair in opposite orders, b2-b's headline
@pytest.mark.parametrize("phi_name", ("ls", "cw"))
def test_the_two_sampling_modes_rank_the_mirror_pair_oppositely(phi_name):
    # docs/b2b_reference_density.md section 6.3 at reduced size: 400 reference
    # points against 2000, a candidate front of 60 against 200 and an allocation
    # of 45 against 15 in place of 150 against 50. the two candidates are subsets
    # of the same exact front and place the same two counts on the two halves the
    # other way round, so they differ only in where they put their points. the
    # density-free quality measure is the fill distance against an independent
    # covering draw, which is c3's measure and the one section 6.1 uses.
    # measured here: fill 0.462182 against 0.345423 under phi_ls and 0.280172
    # against 0.212935 under phi_cw, so the sparse-favouring front leaves the
    # smaller hole under both.
    dense_front, sparse_front, drawn, corrected, dense_is_lower = mirror_pair_fronts(
        phi_name, 400, 4000, 60, 45)
    assert dense_is_lower
    covering = reference_cache(phi_name, 4000, dirichlet_mode, 5002)
    assert fill_distance(sparse_front, covering) < fill_distance(dense_front,
                                                                 covering)
    # the drawn reference prefers the front weighted into the half it oversamples
    assert compute_igd(dense_front, drawn) < compute_igd(sparse_front, drawn)
    # and the corrected one prefers the other, agreeing with the fill distance.
    # this is why d1 computes igd against the farthest-point mode, r-13, and if
    # it ever stops holding the reason has gone with it.
    assert compute_igd(sparse_front, corrected) < compute_igd(dense_front,
                                                              corrected)


# phi_lu is the phi whose mirror pairs do not flip, and it is the same measurement
def test_the_mirror_pair_does_not_flip_under_phi_lu():
    # docs/b2b_reference_density.md section 6.3: under phi_lu the oversampled
    # half is also the half a front genuinely needs more points in, so the fill
    # distance and both references prefer the same candidate, 16 pairs of 16. it
    # is asserted with the other two so that the flip is read as the property of
    # phi_ls and phi_cw that b2-b measured and not as a property of the code.
    dense_front, sparse_front, drawn, corrected, dense_is_lower = mirror_pair_fronts(
        "lu", 400, 4000, 60, 45)
    assert not dense_is_lower
    covering = reference_cache("lu", 4000, dirichlet_mode, 5002)
    assert fill_distance(dense_front, covering) < fill_distance(sparse_front,
                                                                covering)
    assert compute_igd(dense_front, drawn) < compute_igd(sparse_front, drawn)
    assert compute_igd(dense_front, corrected) < compute_igd(sparse_front,
                                                             corrected)


# all three metrics move with the number of rows the front carries, r-16
def test_every_metric_moves_with_cardinality():
    # v-52's measurement at reduced size, and the reason
    # truncate_to_common_cardinality exists. one fixed front from one fixed
    # search, 290 rows of random search on p1 under phi_lu at budget 2000 and
    # seed 11, subsampled uniformly at random: igd 0.1101, 0.0735, 0.0534 and
    # 0.0306 and hypervolume 4.3008, 4.5243, 4.6390 and 4.7228 at 25, 50, 100 and
    # 290 rows, the mean over five draws. the points are the same points and the
    # search is the same search, so the movement is cardinality and nothing else,
    # and it is larger than the differences a solver comparison would report.
    front = run_random_search(p1, "lu", p1_default_params, n_evals, [seed])[0].front
    reference = reference_cache("lu", 400, farthest_point_mode)
    point = derive_reference_point(reference, nadir_margin_rule).point
    scores = []
    for n_keep in (25, 50, 100, len(front)):
        draws = [truncate_to_common_cardinality(front, n_keep, 1000 + draw)
                 for draw in range(5)]
        scores.append((float(np.mean([compute_igd(rows, reference) for rows in draws])),
                       float(np.mean([compute_hv(rows, point) for rows in draws])),
                       float(np.mean([compute_spread(rows) for rows in draws]))))
    for smaller, larger in zip(scores, scores[1:]):
        # igd falls and hypervolume and spread rise, on cardinality alone
        assert larger[0] < smaller[0]
        assert larger[1] > smaller[1]
        assert larger[2] > smaller[2]
