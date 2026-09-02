# tests for src/metrics_decision.py, subpart d2.
# the module is arithmetic on point sets and most of what is checked here is that
# arithmetic against a hand-computed answer or an explicit loop, on identical
# sets, disjoint sets and one set strictly inside another, which are the three
# cases every set-geometry measure has to get right before any of it means
# anything. the three tests that are not about the arithmetic are the cross
# evaluation of the containment, which uses docs/a_close_containment.md as a unit
# test of cross_evaluate, the fill-distance bound against b2's own efficient set,
# and the labelling of the two phi_ls pairs, which is the property r-06 requires
# of anything a table is built from.

import numpy as np
import pytest

from metrics_decision import (check_status, compare_phi_on_one_sample,
                              compute_coverage, compute_hausdorff, compute_overlap,
                              containments, cross_evaluate, finding_status,
                              phi_pairs)
from problems_tier0 import p1, p1_default_params
from random_search import filter_one_sample_under_every_phi, sample_decision_space
from reference_fronts import efficient_set

phi_names = ("lu", "ls", "cw")
# the budget the sample-based tests run at. it is a test size and not a project
# budget: CONTEXT.md section 10 c1 fixes the real one, and e1 states it at the
# call site. 800 keeps the whole file inside the fast run while still giving
# fronts of 150, 412 and 290 rows, which is enough for the containment to bite.
n_evals = 800
seed = 11
# a delta stated once here for the same reason the module refuses a default: it
# is a twentieth of the side of p1's box, [-0.5, 1.5]^2, and the number means
# nothing without that scale beside it.
delta = 0.1


# the largest distance from a point of set_a to the nearest point of set_b, by loops
def brute_force_directed_hausdorff(set_a, set_b):
    worst = 0.0
    for a in set_a:
        nearest = min(float(np.sqrt(sum((a[c] - b[c]) ** 2 for c in range(len(a)))))
                      for b in set_b)
        worst = max(worst, nearest)
    return worst


# three small sets in the plane: one set, an identical copy, and a disjoint one
def hand_checked_sets():
    set_a = np.array([[0.0, 0.0], [1.0, 0.0], [0.0, 1.0]])
    identical = np.array([[0.0, 0.0], [1.0, 0.0], [0.0, 1.0]])
    disjoint = np.array([[10.0, 10.0]])
    return set_a, identical, disjoint


# the hausdorff distances of a set to an identical copy are all zero
def test_hausdorff_on_identical_sets_is_zero():
    set_a, identical, _ = hand_checked_sets()
    measured = compute_hausdorff(set_a, identical)
    assert measured == (0.0, 0.0, 0.0)


# the hausdorff distances of two disjoint sets are the hand-computed ones
def test_hausdorff_on_disjoint_sets_is_hand_computed():
    set_a, _, disjoint = hand_checked_sets()
    # the farthest point of set_a from (10, 10) is (0, 0), at
    # sqrt(100 + 100) = sqrt(200), and the nearest point of set_a to (10, 10) is
    # either of (1, 0) and (0, 1), at sqrt(81 + 100) = sqrt(181). the two
    # directions differ, which is why both are returned.
    measured = compute_hausdorff(set_a, disjoint)
    assert measured.a_to_b == pytest.approx(np.sqrt(200.0))
    assert measured.b_to_a == pytest.approx(np.sqrt(181.0))
    assert measured.symmetric == max(measured.a_to_b, measured.b_to_a)


# a strict subset is at distance zero from its superset and not the reverse
def test_hausdorff_on_a_strict_subset_is_directional():
    _, superset, _ = hand_checked_sets()
    subset = superset[:2]
    measured = compute_hausdorff(subset, superset)
    # every member of the subset is a member of the superset, so the forward
    # distance is exactly zero; the reverse is the distance from the dropped
    # point (0, 1) to the nearest kept one, (0, 0), which is 1.
    assert measured.a_to_b == 0.0
    assert measured.b_to_a == pytest.approx(1.0)
    assert measured.symmetric == pytest.approx(1.0)


# both directed distances against an explicit pair loop, on random arrays
@pytest.mark.parametrize("n_vars", (2, 5))
def test_hausdorff_against_brute_force(n_vars):
    generator = np.random.default_rng(20260902)
    set_a = generator.uniform(-1.0, 1.0, size=(60, n_vars))
    set_b = generator.uniform(-0.5, 1.5, size=(40, n_vars))
    measured = compute_hausdorff(set_a, set_b)
    assert measured.a_to_b == pytest.approx(brute_force_directed_hausdorff(set_a, set_b))
    assert measured.b_to_a == pytest.approx(brute_force_directed_hausdorff(set_b, set_a))
    # the symmetric distance is the maximum of the two and is not computed a
    # second way, so this asserts the field rather than the definition.
    assert measured.symmetric == max(measured.a_to_b, measured.b_to_a)


# coverage is one on identical sets, zero on far-apart ones, and one on a subset
def test_coverage_on_the_three_hand_checked_cases():
    set_a, identical, disjoint = hand_checked_sets()
    assert compute_coverage(set_a, identical, 0.0) == 1.0
    assert compute_coverage(identical, set_a, 0.0) == 1.0
    assert compute_coverage(set_a, disjoint, 1.0) == 0.0
    assert compute_coverage(disjoint, set_a, 1.0) == 0.0
    # the subset is covered completely at delta zero and the superset is not:
    # two of its three points are in the subset and the third, (0, 1), is at
    # distance 1 from the nearest of them.
    subset = set_a[:2]
    assert compute_coverage(subset, set_a, 0.0) == 1.0
    assert compute_coverage(set_a, subset, 0.0) == pytest.approx(2.0 / 3.0)


# the two directions of coverage differ on a constructed case
def test_coverage_is_asymmetric():
    # set_a is one point of set_b, so all of set_a is covered by set_b at any
    # delta, while half of set_b sits ten units away from set_a and is covered by
    # it at none. asymmetry is not a detail here: CONTEXT.md section 10 d2
    # reports coverage both ways because the two questions are different.
    set_a = np.array([[0.0, 0.0]])
    set_b = np.array([[0.0, 0.0], [10.0, 10.0]])
    assert compute_coverage(set_a, set_b, 0.5) == 1.0
    assert compute_coverage(set_b, set_a, 0.5) == 0.5


# overlap is one on identical sets, zero on far-apart ones, and 2|a|/(|a|+|b|) on a subset
def test_overlap_on_the_three_hand_checked_cases():
    set_a, identical, disjoint = hand_checked_sets()
    assert compute_overlap(set_a, identical, 0.0) == 1.0
    assert compute_overlap(set_a, disjoint, 1.0) == 0.0
    subset = set_a[:2]
    # both members of the subset are covered and so are the same two members of
    # the superset, so the intersection is 4 of a union of 5. this is the number
    # the two check pairs of phi_pairs are pinned to by the containment and it is
    # arithmetic rather than a measurement, which is why they are labelled.
    assert compute_overlap(subset, set_a, 0.0) == pytest.approx(4.0 / 5.0)
    assert compute_overlap(set_a, subset, 0.0) == pytest.approx(4.0 / 5.0)


# coverage and overlap never fall as delta grows
def test_coverage_and_overlap_are_non_decreasing_in_delta():
    generator = np.random.default_rng(20260902)
    set_a = generator.uniform(0.0, 1.0, size=(40, 2))
    set_b = generator.uniform(0.5, 2.0, size=(30, 2))
    deltas = (0.0, 0.01, 0.05, 0.1, 0.25, 0.5, 1.0, 2.0, 5.0)
    forward = [compute_coverage(set_a, set_b, d) for d in deltas]
    reverse = [compute_coverage(set_b, set_a, d) for d in deltas]
    overlaps = [compute_overlap(set_a, set_b, d) for d in deltas]
    for series in (forward, reverse, overlaps):
        assert all(later >= earlier for earlier, later in zip(series, series[1:]))
    assert forward[0] < forward[-1] and overlaps[-1] == 1.0


# b2's efficient set is at distance zero from itself under every phi
@pytest.mark.parametrize("phi_name", phi_names)
@pytest.mark.parametrize("include_singular", (False, True))
def test_hausdorff_of_the_efficient_set_against_itself_is_zero(phi_name, include_singular):
    points, _ = efficient_set(p1, phi_name, 400, include_singular)
    measured = compute_hausdorff(points, points)
    assert measured == (0.0, 0.0, 0.0)


# the distance to a subsample of the efficient set is the subsample's fill distance
@pytest.mark.parametrize("phi_name", phi_names)
def test_hausdorff_against_a_subsample_is_bounded_by_its_fill_distance(phi_name):
    # the subsample is a subset, so the reverse distance is exactly zero and the
    # forward one is the largest distance from a point of the set to the nearest
    # kept point, which is the fill distance of the subsample with respect to the
    # set it was drawn from. that quantity is computed here by an explicit loop
    # and not by the module, so the bound is against an independent number. it is
    # asserted as the bound the metric has to respect and then as the equality it
    # actually is, with no slack added to either: the two routes to the same real
    # number agree bitwise on all three phi here, and a slack term would be the
    # tolerance CONTEXT.md section 5 refuses, in the one place it is not needed.
    points, _ = efficient_set(p1, phi_name, 400, False)
    generator = np.random.default_rng(20260902)
    subsample = points[generator.choice(len(points), 80, replace=False)]
    measured = compute_hausdorff(points, subsample)
    fill = brute_force_directed_hausdorff(points, subsample)
    assert measured.b_to_a == 0.0
    assert measured.a_to_b <= fill
    assert measured.a_to_b == pytest.approx(fill)
    assert measured.symmetric == measured.a_to_b


# a set non-dominated under one phi is entirely non-dominated under a phi containing it
@pytest.mark.parametrize("inner", ("lu", "cw"))
def test_cross_evaluate_returns_one_on_a_contained_set(inner):
    # ND_lu and ND_cw both sit inside ND_ls, exactly and for every problem,
    # docs/a_close_containment.md corollaries 1 and 2, so every member of either
    # is non-dominated under phi_ls's order in the whole sample and therefore in
    # any subset of it. the containment is used here as a unit test of
    # cross_evaluate and nothing is claimed from it: it is s-11 to the
    # supervisors, and if the criterion is refuted this test goes with it and no
    # result of the project moves, because none was ever claimed from it.
    sample = filter_one_sample_under_every_phi(p1, p1_default_params, n_evals, seed)
    contained = sample.decision_vectors[sample.indices[inner]]
    assert cross_evaluate(contained, "ls", p1, p1_default_params) == 1.0
    # the reverse direction is not fixed and is not asserted to a value; it is
    # only asserted to be a proper fraction, which is what makes the phi_ls pairs
    # checks in one direction and measurements in the other.
    outer = sample.decision_vectors[sample.indices["ls"]]
    assert 0.0 < cross_evaluate(outer, inner, p1, p1_default_params) < 1.0


# cross_evaluate on a hand-checked pair of points, one dominating the other
def test_cross_evaluate_on_a_hand_checked_case():
    # p1 at rho = 1/4 and delta = 1/8. at x = (1, 1) the centres are
    # c_1 = 1 and c_2 = 0 and the half-widths are r_1 = r_2 = 3/8; at
    # x = (3/2, 3/2) they are c_1 = 5/2, c_2 = 1/2 and r_1 = r_2 = 11/16. the
    # first is strictly smaller in all four of (c_1, r_1, c_2, r_2) and therefore
    # in all four columns of every one of the three phi, each being a fixed
    # linear map of the same pair, so the second point is dominated under all
    # three and exactly one of the two survives.
    kept = np.array([[1.0, 1.0]])
    dominated = np.array([[1.0, 1.0], [1.5, 1.5]])
    for phi_name in phi_names:
        assert cross_evaluate(kept, phi_name, p1, p1_default_params) == 1.0
        assert cross_evaluate(dominated, phi_name, p1, p1_default_params) == 0.5


# the three sets compared are index sets into one sample, which is the isolation
def test_compare_phi_on_one_sample_measures_over_one_sample():
    # the whole reason the comparison is made on random search: the sample is a
    # pure function of the box, the budget and the seed, so the three sets differ
    # only through the order. this asserts it the way tests/test_random_search.py
    # does, by naming the rows of the sample the indices index, which no dict of
    # value tuples could establish.
    comparison = compare_phi_on_one_sample(p1, p1_default_params, n_evals, seed, delta)
    drawn = sample_decision_space(p1.bounds(), n_evals, seed)
    assert comparison.sample.decision_vectors.shape == (n_evals, p1.n_vars)
    assert np.array_equal(comparison.sample.decision_vectors, drawn)
    for phi_name in phi_names:
        indices = comparison.sample.indices[phi_name]
        assert comparison.sizes[phi_name] == len(indices)
        assert np.array_equal(comparison.sample.decision_vectors[indices],
                              drawn[indices])
    assert comparison.delta == delta and comparison.n_evals == n_evals
    assert comparison.seed == seed and comparison.problem == "p1"


# the two phi_ls pairs are labelled checks and the phi_lu against phi_cw pair a finding
def test_the_phi_ls_pairs_are_labelled_checks_and_not_findings():
    # r-06 and CONTEXT.md section 10 e3. a table built from this return value
    # must not be able to present either phi_ls pair as a measured difference,
    # so the label is a field on every pair and not a footnote a caller may drop,
    # and the note names the containment, r-11's rounding artefact and s-11.
    comparison = compare_phi_on_one_sample(p1, p1_default_params, n_evals, seed, delta)
    labels = {(pair.phi_a, pair.phi_b): pair.status for pair in comparison.pairs}
    assert labels == {("lu", "ls"): check_status, ("ls", "cw"): check_status,
                      ("lu", "cw"): finding_status}
    assert tuple(labels) == phi_pairs
    for pair in comparison.pairs:
        if pair.status == check_status:
            assert pair.containment == containments[(pair.phi_a, pair.phi_b)]
            assert "r-06" in pair.note and "r-11" in pair.note and "s-11" in pair.note
        else:
            assert pair.containment is None and pair.containment_violations is None
            assert "headline" in pair.note


# on a check pair the contained direction is fixed at one before anything runs
def test_the_containment_fixes_one_direction_on_the_check_pairs():
    # this is what the label exists for. the coverage of the contained set in the
    # containing one is 1.0 at delta zero and stays 1.0 at every delta, and the
    # cross evaluation of it under the containing phi is 1.0, both of them fixed
    # by docs/a_close_containment.md before a line runs. the violation count is
    # r-11's artefact counted rather than described: it is exact in real
    # arithmetic, fails by rounding in doubles at one point of 1565 measured, and
    # a nonzero value is arithmetic and never a result about phi.
    comparison = compare_phi_on_one_sample(p1, p1_default_params, n_evals, seed, 0.0)
    for pair in comparison.pairs:
        if pair.status != check_status:
            continue
        inner, _ = pair.containment
        fixed = pair.coverage_a_in_b if inner == pair.phi_a else pair.coverage_b_in_a
        crossed = (pair.cross_a_under_b if inner == pair.phi_a
                   else pair.cross_b_under_a)
        assert fixed == 1.0 and crossed == 1.0
        assert pair.containment_violations == 0


# every metric carries the cardinality it was computed at, r-16
def test_every_pair_carries_its_two_cardinalities():
    comparison = compare_phi_on_one_sample(p1, p1_default_params, n_evals, seed, delta)
    for pair in comparison.pairs:
        assert pair.n_a == comparison.sizes[pair.phi_a]
        assert pair.n_b == comparison.sizes[pair.phi_b]
        assert 0 < pair.n_a <= n_evals and 0 < pair.n_b <= n_evals


# nothing the caller passes in is written to
def test_the_inputs_are_not_mutated():
    set_a = np.array([[0.0, 0.0], [1.0, 0.5]])
    set_b = np.array([[0.25, 0.25], [2.0, 2.0], [1.0, 0.5]])
    given_a, given_b = np.array(set_a), np.array(set_b)
    given_params = dict(p1_default_params)
    compute_hausdorff(given_a, given_b)
    compute_coverage(given_a, given_b, delta)
    compute_overlap(given_a, given_b, delta)
    cross_evaluate(given_a, "cw", p1, given_params)
    compare_phi_on_one_sample(p1, given_params, 200, seed, delta)
    assert np.array_equal(given_a, set_a) and np.array_equal(given_b, set_b)
    assert given_params == p1_default_params


# a front, an empty set and a set over a different decision space are all refused
def test_the_shapes_are_checked():
    set_a = np.array([[0.0, 0.0], [1.0, 1.0]])
    three_vars = np.array([[0.0, 0.0, 0.0]])
    with pytest.raises(ValueError, match="must have shape"):
        compute_hausdorff(np.array([0.0, 1.0]), set_a)
    with pytest.raises(ValueError, match="at least one decision vector"):
        compute_coverage(np.zeros((0, 2)), set_a, delta)
    with pytest.raises(ValueError, match="decision variables"):
        compute_overlap(set_a, three_vars, delta)
    with pytest.raises(ValueError, match="decision variables"):
        cross_evaluate(three_vars, "lu", p1, p1_default_params)


# delta is required, is finite and is not negative, and an unknown phi is refused
def test_delta_is_required_and_the_phi_is_checked():
    set_a = np.array([[0.0, 0.0], [1.0, 1.0]])
    # no default, for the reason include_singular_segments has none, s-12: the
    # value is part of the metric and belongs in every table beside it.
    with pytest.raises(TypeError):
        compute_coverage(set_a, set_a)
    with pytest.raises(TypeError):
        compute_overlap(set_a, set_a)
    for bad in (-0.1, float("nan"), float("inf")):
        with pytest.raises(ValueError, match="delta must be"):
            compute_coverage(set_a, set_a, bad)
    with pytest.raises(ValueError, match="unknown phi"):
        cross_evaluate(set_a, "identity", p1, p1_default_params)
