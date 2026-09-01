# tests for src/runners.py, subpart c2.
# the module is a wrapper around two pymoo algorithms, so most of what is checked
# here is the contract it shares with c1 rather than the quality of a front: the
# same seed giving the same front bitwise, the shapes d1 and d2 are written
# against, the budget actually spent, and the column order every metric assumes.
# the test this session exists to make is
# test_the_project_filter_is_the_identity_on_the_pymoo_front: pymoo's
# non-domination and the project's must agree exactly, neither applying a
# tolerance, and phase e depends on knowing which relation produced its numbers.
# every test that runs a solver is marked slow, so the suite runs fast by default
# and in full before a commit.

import numpy as np
import pytest

from phi_transforms import phi_registry
from problems_tier0 import p0, p1, p1_default_params
from problems_tier1 import dtlz2_interval, zdt1_interval
from random_search import SearchResult, non_dominated_indices, phi_image
from reference_fronts import reference_front, transformed_image
from runners import SeededTruncation, run_mopso, run_nsga2

phi_names = ("lu", "ls", "cw")
# the run size every test uses. it is a test size and not a project budget:
# CONTEXT.md section 5 step 4 fixes the real one and e1 states it at the call
# site. 40 times 10 is 400 evaluations, a fifth of the 2000 c1's tests draw.
pop_size = 40
n_gen = 10
n_evals = pop_size * n_gen
# a list, never a scalar, which is c1's require_seeds rule and is reused here.
seeds = [11, 12]
# the tier 1 level the tests run at, one of a1's five and distinguished by
# nothing, src/problems_tier1.py.
tier1_params = {"eps": 0.10}
# the problems the contract tests run over, one of each representation: p0 and
# its "endpoints", p1 and both tier 1 benchmarks and their "centre_radius".
problem_cases = ((p0, None), (p1, p1_default_params),
                 (zdt1_interval, tier1_params), (dtlz2_interval, tier1_params))
problem_ids = ("p0", "p1", "zdt1", "dtlz2")
# the two solvers, run through one parametrisation so neither is tested less than
# the other. random search is not here: it is c1's control and has its own file.
solvers = (run_nsga2, run_mopso)
solver_ids = ("nsga2", "mopso")


# the count of front rows some row of the given set dominates, usual pareto relation.
# no tolerance and no rounding, per d-02. this is c1's helper, copied rather than
# imported for the reason recorded in that session: whether the test files should
# share their local copies is a separate decision and was not taken there.
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


# the non-dominated index set of one point set under each phi, over one array
def indices_under_every_phi(problem, points, params):
    # the form the containments of docs/a_close_containment.md are statements
    # about: three index sets over one array, from one evaluation. the two
    # functions are c1's and are not reimplemented here.
    pairs = problem.evaluate(points, params)
    images = {name: phi_image(problem, pairs, record)
              for name, record in phi_registry.items()}
    return {name: frozenset(non_dominated_indices(image).tolist())
            for name, image in images.items()}


# the same seed gives the same front bitwise, so a metric computed on it is reproducible
@pytest.mark.slow
@pytest.mark.parametrize("run_solver", solvers, ids=solver_ids)
@pytest.mark.parametrize("problem,params", problem_cases, ids=problem_ids)
@pytest.mark.parametrize("phi_name", phi_names)
def test_the_same_seed_gives_the_same_front(run_solver, problem, params, phi_name):
    # this is where pymoo 0.6.2's unseeded archive truncation would show. at this
    # run size the archive does not overflow on every case, so the test that puts
    # the truncation itself under a seed is
    # test_the_archive_truncation_is_seeded_and_is_reached below; this one is the
    # grid, every problem and every phi.
    first = run_solver(problem, phi_name, params, n_gen, pop_size, [seeds[0]])[0]
    second = run_solver(problem, phi_name, params, n_gen, pop_size, [seeds[0]])[0]
    assert np.array_equal(first.front, second.front)
    assert np.array_equal(first.decision_vectors, second.decision_vectors)


# the archive truncation is reached and is reproducible when it is, c2-b
@pytest.mark.slow
def test_the_archive_truncation_is_seeded_and_is_reached(monkeypatch):
    # the reproducibility grid above is worth only as much as the truncation it
    # exercises, and at 400 evaluations pymoo's Archive.add never overflows
    # mopso's 200-row archive on any of the four problems. p1 under phi_ls at 800
    # evaluations does overflow it, so this is the case that actually runs
    # src/runners.py's SeededTruncation, counted here rather than assumed. without
    # the seed this is the run that gave five different fronts at one seed, c2 and
    # v-48.
    calls = []
    original = SeededTruncation.__call__

    # the module's own truncation, with each call recorded before it runs
    def counted(self, sols, k):
        calls.append(k)
        return original(self, sols, k)

    monkeypatch.setattr(SeededTruncation, "__call__", counted)
    first = run_mopso(p1, "ls", p1_default_params, 20, 40, [seeds[0]])[0]
    reached = len(calls)
    repeats = [run_mopso(p1, "ls", p1_default_params, 20, 40, [seeds[0]])[0]
               for _ in range(2)]
    assert reached > 0, "the archive never overflowed, so nothing was truncated"
    assert len(calls) == reached * 3
    for repeat in repeats:
        assert np.array_equal(first.front, repeat.front)
        assert np.array_equal(first.decision_vectors, repeat.decision_vectors)


# mopso's front is bounded by pymoo's own archive size and is not resized, c2-b
@pytest.mark.slow
@pytest.mark.parametrize("problem,params", problem_cases, ids=problem_ids)
@pytest.mark.parametrize("phi_name", phi_names)
def test_the_mopso_front_stays_within_the_default_archive(problem, params, phi_name):
    # c2 sized the archive to the budget, which took the front to thousands of
    # rows and the leader pool with it; c2-b seeds the truncation instead and
    # leaves the size at pymoo's 200. the front mopso returns is its archive, so
    # this is the assertion that the size is pymoo's and not this project's.
    result = run_mopso(problem, phi_name, params, n_gen, pop_size, [seeds[0]])[0]
    assert result.front.shape[0] <= 200


# different seeds give different fronts, which is what makes variance across seeds real
@pytest.mark.slow
@pytest.mark.parametrize("run_solver", solvers, ids=solver_ids)
@pytest.mark.parametrize("problem,params", problem_cases[1:], ids=problem_ids[1:])
def test_different_seeds_give_different_fronts(run_solver, problem, params):
    # p0 is left out and not excused: under phi_cw its front is the single anchor
    # point x = 0, which every seed finds and should, docs/b1_phi_efficient_sets.md
    # section 7.4, so a difference between seeds is not a property of that case.
    results = run_solver(problem, "lu", params, n_gen, pop_size, seeds)
    for first, second in zip(results, results[1:]):
        assert not np.array_equal(first.decision_vectors, second.decision_vectors)


# the shapes are (k, 2m) and (k, n_vars) with matching k, one result per seed
@pytest.mark.slow
@pytest.mark.parametrize("run_solver", solvers, ids=solver_ids)
@pytest.mark.parametrize("problem,params", problem_cases, ids=problem_ids)
@pytest.mark.parametrize("phi_name", phi_names)
def test_the_result_shapes_are_the_contract(run_solver, problem, params, phi_name):
    # the same record and the same two shapes as c1's, asserted here because three
    # solvers returning two different shapes is how analysis code acquires branches.
    results = run_solver(problem, phi_name, params, n_gen, pop_size, seeds)
    assert len(results) == len(seeds)
    assert [result.seed for result in results] == seeds
    for result in results:
        assert isinstance(result, SearchResult)
        k = result.front.shape[0]
        assert result.front.shape == (k, 2 * problem.n_obj)
        assert result.decision_vectors.shape == (k, problem.n_vars)
        assert 0 < k <= n_evals


# the budget carried on the record is the number of evaluations actually performed
@pytest.mark.slow
@pytest.mark.parametrize("run_solver", solvers, ids=solver_ids)
@pytest.mark.parametrize("problem,params", problem_cases, ids=problem_ids)
def test_the_budget_is_pop_size_times_n_gen(run_solver, problem, params):
    # budget parity is the point: a random-search run and a solver run are only
    # comparable if the number on the record is the number spent. under pymoo's
    # ("n_gen", n) termination mopso_cd spends one population more than nsga-ii,
    # which is why src/runners.py terminates on the evaluation count instead.
    counted_problem, counted = counting_problem(problem)
    results = run_solver(counted_problem, "ls", params, n_gen, pop_size, seeds)
    assert [result.n_evals for result in results] == [n_evals] * len(seeds)
    assert sum(counted) == n_evals * len(seeds)
    assert set(counted) == {pop_size}


# every front row is the image of the decision vector printed beside it
@pytest.mark.slow
@pytest.mark.parametrize("run_solver", solvers, ids=solver_ids)
@pytest.mark.parametrize("problem,params", problem_cases, ids=problem_ids)
@pytest.mark.parametrize("phi_name", phi_names)
def test_each_front_row_is_the_image_of_its_decision_vector(run_solver, problem,
                                                            params, phi_name):
    # the pairing is what d2 and e3 rest on: every metric comparable across phi is
    # computed on the decision vectors, so a front row beside the wrong vector
    # would corrupt the only measurement the research question is answered from.
    result = run_solver(problem, phi_name, params, n_gen, pop_size, [seeds[0]])[0]
    recomputed = phi_image(problem, problem.evaluate(result.decision_vectors, params),
                           phi_registry[phi_name])
    assert np.array_equal(result.front, recomputed)


# the column order is b2's, asserted through b2's own code and not assumed
@pytest.mark.slow
@pytest.mark.parametrize("run_solver", solvers, ids=solver_ids)
@pytest.mark.parametrize("phi_name", phi_names)
def test_the_column_order_is_the_one_reference_front_produces(run_solver, phi_name):
    # (Lambda_1^T f, B_1^T f, Lambda_2^T f, B_2^T f), src/reference_fronts.py. a
    # transposition here corrupts every metric in the project, so the solver's
    # front is recomputed through the function reference_front itself calls and
    # compared bitwise, rather than the order being inferred from a shape.
    result = run_solver(p1, phi_name, p1_default_params, n_gen, pop_size, [seeds[0]])[0]
    through_b2 = transformed_image(p1, result.decision_vectors, phi_registry[phi_name],
                                   p1_default_params)
    assert through_b2.shape == result.front.shape
    assert np.array_equal(through_b2, result.front)


# pymoo's non-domination and the project's agree exactly, the filter being the identity
@pytest.mark.slow
@pytest.mark.parametrize("run_solver", solvers, ids=solver_ids)
@pytest.mark.parametrize("problem,params", problem_cases, ids=problem_ids)
@pytest.mark.parametrize("phi_name", phi_names)
def test_the_project_filter_is_the_identity_on_the_pymoo_front(run_solver, problem,
                                                               params, phi_name):
    # the check this session exists to make. pymoo applies no tolerance,
    # CONTEXT.md section 5 recording that its NonDominatedSorting epsilon argument
    # is a translation and cannot change a front, and the project applies none
    # either, so the two relations should agree row for row. if they ever do not,
    # the count is the finding: a front that is non-dominated under one relation
    # and not under the other means every metric in phase e has to name which
    # relation produced it.
    result = run_solver(problem, phi_name, params, n_gen, pop_size, [seeds[0]])[0]
    keep = non_dominated_indices(result.front)
    assert len(keep) == len(result.front), (
        "{} rows of {} in the pymoo front are dominated under the project's "
        "relation, on {} under phi_{}".format(len(result.front) - len(keep),
                                              len(result.front), problem.name, phi_name))
    assert np.array_equal(result.front[keep], result.front)


# the containment of docs/a_close_containment.md, on both solvers' output
@pytest.mark.slow
@pytest.mark.parametrize("run_solver", solvers, ids=solver_ids)
@pytest.mark.parametrize("problem,params", problem_cases[1:], ids=problem_ids[1:])
@pytest.mark.parametrize("seed", seeds)
def test_the_containment_holds_on_solver_output(run_solver, problem, params, seed):
    # corollaries 1 and 2 of docs/a_close_containment.md: ND_lu and ND_cw are both
    # contained in ND_ls. this is a check on the transform and the filter and not
    # evidence about the solvers, because it holds for the non-dominated sets of
    # any finite point set whatever produced it; what it catches is an error in
    # the route pairing, in the column order or in the dominance relation. the
    # containments themselves are s-11 to the supervisors and nothing is built on
    # them. no strictness is asserted, unlike c1's uniform sample: the point set
    # here is already one phi's front and the three sets can coincide on it.
    result = run_solver(problem, "lu", params, n_gen, pop_size, [seed])[0]
    sets = indices_under_every_phi(problem, result.decision_vectors, params)
    assert sets["lu"] <= sets["ls"]
    assert sets["cw"] <= sets["ls"]


# no solver front point dominates any point of b2's reference front
@pytest.mark.slow
@pytest.mark.parametrize("run_solver", solvers, ids=solver_ids)
@pytest.mark.parametrize("phi_name", phi_names)
@pytest.mark.parametrize("include_singular", (False, True))
def test_no_solver_point_dominates_the_reference_front(run_solver, phi_name,
                                                       include_singular):
    # a solver cannot beat the analytic answer. c1 could assert this on a uniform
    # draw because such a draw lands on a face with probability zero; a
    # metaheuristic can converge onto one, so if this ever fails the first thing
    # to check is whether the offending points sit on a boundary of the derived
    # region, docs/b1_phi_efficient_sets.md section 2.4, and only then whether the
    # derivation is wrong. it holds exactly as written at both settings of the
    # singular flag, s-12 and r-12, which is why both are run.
    result = run_solver(p1, phi_name, p1_default_params, n_gen, pop_size, [seeds[0]])[0]
    front = reference_front(p1, phi_name, 1000, include_singular)
    assert dominated_count(front, result.front) == 0


# seeds is a list, never a scalar, and never empty, which is c1's rule reused
@pytest.mark.parametrize("run_solver", solvers, ids=solver_ids)
@pytest.mark.parametrize("value", (7, None, 7.0, [], ()))
def test_seeds_must_be_a_non_empty_list(run_solver, value):
    with pytest.raises(ValueError, match="seeds must"):
        run_solver(p1, "lu", p1_default_params, n_gen, pop_size, value)


# an unknown phi is refused, and a budget below one evaluation with it
@pytest.mark.parametrize("run_solver", solvers, ids=solver_ids)
def test_an_unknown_phi_and_an_empty_budget_are_refused(run_solver):
    with pytest.raises(ValueError, match="unknown phi"):
        run_solver(p1, "identity", p1_default_params, n_gen, pop_size, seeds)
    with pytest.raises(ValueError, match="n_gen and pop_size"):
        run_solver(p1, "lu", p1_default_params, 0, pop_size, seeds)
    with pytest.raises(ValueError, match="n_gen and pop_size"):
        run_solver(p1, "lu", p1_default_params, n_gen, 0, seeds)


# the bounds handed to pymoo are the problem's own and are never the unit box
@pytest.mark.parametrize("problem,params", problem_cases, ids=problem_ids)
def test_the_pymoo_problem_carries_the_problem_bounds(problem, params):
    # p1's box is [-0.5, 1.5]^2 and p0's is [-1, 1], so a runner that defaulted to
    # the unit box would search the wrong region on both and would still look
    # plausible on tier 1, whose box is the unit cube.
    from runners import TransformedProblem
    lower, upper = problem.bounds()
    wrapped = TransformedProblem(problem, phi_registry["lu"], params)
    assert wrapped.n_var == problem.n_vars and wrapped.n_obj == 2 * problem.n_obj
    assert np.array_equal(wrapped.xl, lower) and np.array_equal(wrapped.xu, upper)


# nothing the caller passes in is written to
@pytest.mark.slow
@pytest.mark.parametrize("run_solver", solvers, ids=solver_ids)
@pytest.mark.parametrize("problem,params", problem_cases[1:], ids=problem_ids[1:])
def test_the_inputs_are_not_mutated(run_solver, problem, params):
    lower, upper = problem.bounds()
    given_params = dict(params)
    given_seeds = list(seeds)
    run_solver(problem, "cw", given_params, n_gen, pop_size, given_seeds)
    assert given_params == params
    assert given_seeds == seeds
    assert np.array_equal(problem.bounds()[0], lower)
    assert np.array_equal(problem.bounds()[1], upper)
