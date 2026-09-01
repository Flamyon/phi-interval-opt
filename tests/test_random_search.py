# tests for src/random_search.py, subpart c1.
# the module is the control of slide 17 and its job is to be identical across
# phi, so most of what is checked here is sameness rather than quality: the same
# seed giving the same front bitwise, one sample carrying three filters, and the
# budget being the number the caller asked for. the two tests that are not about
# the module at all are the last two, which put the containment of
# docs/a_close_containment.md and the reference front of b2 against solver output
# for the first time.

import numpy as np
import pytest

from phi_transforms import phi_registry
from problems_tier0 import p0, p1, p1_default_params
from problems_tier1 import dtlz2_interval, zdt1_interval
from random_search import (SearchResult, filter_one_sample_under_every_phi,
                           non_dominated_indices, phi_image, run_random_search,
                           sample_decision_space)
from reference_fronts import reference_front

phi_names = ("lu", "ls", "cw")
# the budget every test runs at. it is a test size and not a project budget:
# CONTEXT.md section 10 c1 fixes the real one as pop_size * n_gen of whichever
# c2 run the control is compared against, and that is stated at the call site.
n_evals = 2000
# a list, never a scalar, which is the module's own rule as well.
seeds = [11, 12, 13]
# the tier 1 level the containment is checked at. it is one of a1's five,
# src/problems_tier1.py, and no level is distinguished; the containment is a
# statement about the orders and holds at every level.
tier1_params = {"eps": 0.10}
# the problems the contract tests run over, one of each representation: p0 and
# its "endpoints", p1 and both tier 1 benchmarks and their "centre_radius".
problem_cases = ((p0, None), (p1, p1_default_params),
                 (zdt1_interval, tier1_params), (dtlz2_interval, tier1_params))
problem_ids = ("p0", "p1", "zdt1", "dtlz2")


# the non-dominated rows found by an explicit pair loop, no broadcasting
def brute_force_non_dominated(rows):
    keep = []
    for i in range(len(rows)):
        others = [j for j in range(len(rows)) if j != i]
        dominated = any(
            all(rows[j][c] <= rows[i][c] for c in range(rows.shape[1]))
            and any(rows[j][c] < rows[i][c] for c in range(rows.shape[1]))
            for j in others)
        if not dominated:
            keep.append(i)
    return keep


# the count of front rows some row of the given set dominates, usual pareto relation.
# no tolerance and no rounding, per d-02: a tolerance here would hide exactly the
# failure the reference-front test exists to catch.
def dominated_count(front, candidate_image, block=100):
    total = 0
    for start in range(0, len(front), block):
        rows = front[start:start + block]
        not_worse = np.all(candidate_image[None, :, :] <= rows[:, None, :], axis=2)
        strictly_better = np.any(candidate_image[None, :, :] < rows[:, None, :], axis=2)
        total += int(np.count_nonzero(np.any(not_worse & strictly_better, axis=1)))
    return total


# a copy of a problem that records the population size of every evaluate call
def counting_problem(problem):
    counted = []

    # the problem's own evaluate, with the population size recorded first
    def evaluate(x, params=None):
        counted.append(np.asarray(x).shape[0])
        return problem.evaluate(x, params)

    return problem._replace(evaluate=evaluate), counted


# the same seed gives the same front bitwise, so a metric computed on it is reproducible
@pytest.mark.parametrize("problem,params", problem_cases, ids=problem_ids)
@pytest.mark.parametrize("phi_name", phi_names)
def test_the_same_seed_gives_the_same_front(problem, params, phi_name):
    first = run_random_search(problem, phi_name, params, n_evals, [seeds[0]])[0]
    second = run_random_search(problem, phi_name, params, n_evals, [seeds[0]])[0]
    assert np.array_equal(first.front, second.front)
    assert np.array_equal(first.decision_vectors, second.decision_vectors)


# different seeds give different fronts, which is what makes variance across seeds real
@pytest.mark.parametrize("problem,params", problem_cases, ids=problem_ids)
def test_different_seeds_give_different_fronts(problem, params):
    results = run_random_search(problem, "lu", params, n_evals, seeds)
    for first, second in zip(results, results[1:]):
        assert not np.array_equal(first.decision_vectors, second.decision_vectors)


# the sample lies inside the decision box the problem states, on every coordinate
@pytest.mark.parametrize("problem,params", problem_cases, ids=problem_ids)
def test_the_sample_lies_in_the_box(problem, params):
    lower, upper = problem.bounds()
    sample = sample_decision_space(problem.bounds(), n_evals, seeds[0])
    assert sample.shape == (n_evals, problem.n_vars)
    assert np.all(sample >= lower) and np.all(sample <= upper)


# no coordinate is confined to a sub-interval of its own range
@pytest.mark.parametrize("problem,params", problem_cases, ids=problem_ids)
def test_the_sample_covers_every_coordinate(problem, params):
    lower, upper = problem.bounds()
    sample = sample_decision_space(problem.bounds(), n_evals, seeds[0])
    span = upper - lower
    # a uniform sample of n points leaves a gap of about span / n at each end, so
    # at n_evals = 2000 a twentieth of the span at either end is four decades of
    # slack. what this rules out is a coordinate drawn on the wrong interval,
    # held fixed, or collapsed by a shape error, not a thin tail.
    assert np.all(np.min(sample, axis=0) < lower + 0.05 * span)
    assert np.all(np.max(sample, axis=0) > upper - 0.05 * span)


# the shapes are (k, 2m) and (k, n_vars) with matching k, one result per seed
@pytest.mark.parametrize("problem,params", problem_cases, ids=problem_ids)
@pytest.mark.parametrize("phi_name", phi_names)
def test_the_result_shapes_are_the_contract(problem, params, phi_name):
    results = run_random_search(problem, phi_name, params, n_evals, seeds)
    assert len(results) == len(seeds)
    assert [result.seed for result in results] == seeds
    for result in results:
        assert isinstance(result, SearchResult)
        k = result.front.shape[0]
        assert result.front.shape == (k, 2 * problem.n_obj)
        assert result.decision_vectors.shape == (k, problem.n_vars)
        assert 0 < k <= n_evals


# every front row is the image of the decision vector printed beside it
@pytest.mark.parametrize("problem,params", problem_cases, ids=problem_ids)
@pytest.mark.parametrize("phi_name", phi_names)
def test_each_front_row_is_the_image_of_its_decision_vector(problem, params, phi_name):
    # the pairing is what d2 and e3 rest on: every metric comparable across phi is
    # computed on the decision vectors, so a front row beside the wrong vector
    # would corrupt the only measurement the research question is answered from.
    result = run_random_search(problem, phi_name, params, n_evals, [seeds[0]])[0]
    record = phi_registry[phi_name]
    recomputed = phi_image(problem, problem.evaluate(result.decision_vectors, params),
                           record)
    assert np.array_equal(result.front, recomputed)


# nothing the caller passes in is written to
@pytest.mark.parametrize("problem,params", problem_cases[1:], ids=problem_ids[1:])
def test_the_inputs_are_not_mutated(problem, params):
    lower, upper = problem.bounds()
    bounds = (np.array(lower), np.array(upper))
    given_params = dict(params)
    given_seeds = list(seeds)
    run_random_search(problem, "cw", given_params, n_evals, given_seeds)
    sample = sample_decision_space(bounds, n_evals, seeds[0])
    sample += 1.0
    assert np.array_equal(bounds[0], lower) and np.array_equal(bounds[1], upper)
    assert given_params == params
    assert given_seeds == seeds


# the dominance relation on a hand-checked case, with ties and duplicate rows
def test_non_dominated_indices_on_a_hand_checked_case():
    rows = np.array([
        [0.0, 0.0],   # 0, better than 2, 3 and 5 and tied with 1
        [0.0, 0.0],   # 1, a duplicate of 0: neither dominates the other
        [0.0, 1.0],   # 2, tied with 0 in the first column and worse in the second
        [1.0, 0.0],   # 3, the same the other way round
        [2.0, -1.0],  # 4, worse in the first column and strictly better in the second
        [3.0, 3.0],   # 5, worse than 0 in both
    ])
    # 0 and 1 survive because a duplicate is not a dominator, no row being
    # strictly better anywhere, and 4 survives on its second column alone. 2 and
    # 3 are the tie cases: equal in one column is "not worse", so 0 dominates
    # them. this is the relation with no tolerance, CONTEXT.md section 5, and a
    # rounding step or an epsilon would change 2 and 3.
    assert non_dominated_indices(rows).tolist() == [0, 1, 4]


# the dominance relation against an explicit pair loop, on arrays with and without ties
@pytest.mark.parametrize("kind", ("continuous", "integer"))
def test_non_dominated_indices_against_brute_force(kind):
    generator = np.random.default_rng(20260901)
    if kind == "continuous":
        rows = generator.uniform(-1.0, 1.0, size=(300, 4))
    else:
        # small integers on purpose: at 300 rows over 5 values per column the
        # array carries duplicate rows and column ties in quantity, which is
        # where a wrong strictness test shows.
        rows = generator.integers(0, 5, size=(300, 3)).astype(float)
    assert non_dominated_indices(rows).tolist() == brute_force_non_dominated(rows)


# one sample is filtered under every phi, and the three index sets index that one array
@pytest.mark.parametrize("problem,params", problem_cases, ids=problem_ids)
def test_one_sample_is_filtered_under_every_phi(problem, params):
    filtered = filter_one_sample_under_every_phi(problem, params, n_evals, seeds[0])
    assert set(filtered.indices) == set(phi_registry)
    assert filtered.decision_vectors.shape == (n_evals, problem.n_vars)
    # the isolation this function exists for: the sets are index sets into the
    # single returned sample, so the three fronts differ only through phi. the
    # check is that each index is a row of that array and that the rows it names
    # are that array's own rows, which no dict of value tuples could establish.
    sample = sample_decision_space(problem.bounds(), n_evals, seeds[0])
    for indices in filtered.indices.values():
        assert 0 < len(indices) <= n_evals
        assert np.all(indices >= 0) and np.all(indices < n_evals)
        assert len(set(indices.tolist())) == len(indices)
        assert np.array_equal(filtered.decision_vectors[indices], sample[indices])


# the one-sample filter and the per-phi runs are the same run, seed for seed
@pytest.mark.parametrize("problem,params", problem_cases, ids=problem_ids)
@pytest.mark.parametrize("phi_name", phi_names)
def test_the_one_sample_filter_agrees_with_run_random_search(problem, params, phi_name):
    # the sample is a pure function of the box, the budget and the seed, so the
    # two entry points search identically by construction. this asserts that,
    # because it is the property the whole isolation argument rests on.
    filtered = filter_one_sample_under_every_phi(problem, params, n_evals, seeds[0])
    result = run_random_search(problem, phi_name, params, n_evals, [seeds[0]])[0]
    indices = filtered.indices[phi_name]
    assert np.array_equal(result.decision_vectors, filtered.decision_vectors[indices])


# the containment of docs/a_close_containment.md, on solver output for the first time
@pytest.mark.parametrize("problem,params", problem_cases[1:], ids=problem_ids[1:])
@pytest.mark.parametrize("seed", seeds[:2])
def test_the_containment_holds_on_random_search_output(problem, params, seed):
    # corollaries 1 and 2 of docs/a_close_containment.md: ND_lu and ND_cw are
    # both contained in ND_ls, from the criterion that phi_B = M phi_A with M
    # entrywise non-negative and invertible makes phi_A-dominance imply
    # phi_B-dominance. the sets here are index sets over one sample, which is the
    # form the containment is a statement about, and this is the cheapest
    # end-to-end check in the project: an error in the sample, in the route
    # pairing, in the column order or in the dominance relation breaks it.
    # exact equality is asserted rather than a band, unlike a5's 0.99 on its
    # constructed lattice samples. that band exists because a lattice puts points
    # on dtlz2's face x_1 = 1, where the centre (1 + g) cos(pi/2) is 6.1e-17 and
    # the subtraction c - r inside phi_ls's first coordinate rounds a strict
    # inequality to a tie; a uniform sample reaches no such point, and the
    # containment was measured exact here at every level of both benchmarks and
    # at three seeds. it is a check on this module and on nothing else: the
    # containments themselves are s-11 to the supervisors.
    filtered = filter_one_sample_under_every_phi(problem, params, n_evals, seed)
    sets = {name: frozenset(indices.tolist())
            for name, indices in filtered.indices.items()}
    assert sets["lu"] <= sets["ls"]
    assert sets["cw"] <= sets["ls"]
    # containments and not equalities, docs/a_close_containment.md section 5.
    assert sets["lu"] < sets["ls"] and sets["cw"] < sets["ls"]


# no random-search front point dominates any point of b2's reference front
@pytest.mark.parametrize("phi_name", phi_names)
@pytest.mark.parametrize("include_singular", (False, True))
def test_no_random_search_point_dominates_the_reference_front(phi_name, include_singular):
    # a solver cannot beat the analytic answer. if it does, either b1's
    # derivation or this search is wrong, and this is the only test in the
    # project that can tell the two apart from outside b2. the candidate set is a
    # uniform sample's non-dominated subset and never a lattice, for the reason
    # recorded in tests/test_reference_fronts.py: a lattice collides with the
    # singular segment's own lattice and is then ordered by a rounding step,
    # which is d-02's subject and not this test's.
    result = run_random_search(p1, phi_name, p1_default_params, n_evals, [seeds[0]])[0]
    front = reference_front(p1, phi_name, 1000, include_singular)
    assert dominated_count(front, result.front) == 0


# the budget is stated and is the number of evaluations actually performed
@pytest.mark.parametrize("problem,params", problem_cases, ids=problem_ids)
def test_the_budget_is_the_requested_number_of_evaluations(problem, params):
    counted_problem, counted = counting_problem(problem)
    results = run_random_search(counted_problem, "ls", params, n_evals, seeds)
    # n_evals is what the caller asked for, is carried on every result so that a
    # table can print it beside the front, and is the population every evaluate
    # call saw, once per seed and no more.
    assert [result.n_evals for result in results] == [n_evals] * len(seeds)
    assert counted == [n_evals] * len(seeds)


# the one-sample filter evaluates that sample once for all three phi
@pytest.mark.parametrize("problem,params", problem_cases, ids=problem_ids)
def test_the_one_sample_filter_spends_one_budget_and_not_three(problem, params):
    counted_problem, counted = counting_problem(problem)
    filter_one_sample_under_every_phi(counted_problem, params, n_evals, seeds[0])
    assert counted == [n_evals]


# seeds is a list, never a scalar, and never empty
@pytest.mark.parametrize("value", (7, None, 7.0, [], ()))
def test_seeds_must_be_a_non_empty_list(value):
    with pytest.raises(ValueError, match="seeds must"):
        run_random_search(p1, "lu", p1_default_params, 10, value)


# an unknown phi is refused, and a budget below one point with it
def test_an_unknown_phi_and_an_empty_budget_are_refused():
    with pytest.raises(ValueError, match="unknown phi"):
        run_random_search(p1, "identity", p1_default_params, 10, seeds)
    with pytest.raises(ValueError, match="n_evals must be at least 1"):
        run_random_search(p1, "lu", p1_default_params, 0, seeds)
