# c2: nsga-ii and mopso from pymoo, on the transformed real problem theorem 3.1
# of [1] licenses solving. the two solvers of slide 17 that are not the control.
#
# what this module is and is not. it is a wrapper: no operator, survival rule,
# archive rule or dominance test of pymoo's is replaced, and the one override in
# the file, SeededArchiveMopso below, changes which generator an existing pymoo
# truncation draws from and nothing else. what the module owns is the problem
# handed to pymoo, the budget the run is stopped at, and the record the run is
# returned in, and all three are shared with c1 so that the three solvers are
# comparable by construction. the transform is
# random_search.phi_image, the record is random_search.SearchResult and the seed
# rule is random_search.require_seeds; none of them is defined a second time
# here. three solvers returning two different shapes is how analysis code
# acquires branches, and d1, d2 and d3 are written against one shape.
#
# phi drives the search here and not only the ordering, which is the difference
# from c1 stated at the head of src/random_search.py: the population that
# survives generation one is already phi's, so every later candidate is phi's
# too, and a difference between two runs of this module is a difference of orders
# and of trajectories at once. the isolation of the order lives in c1 and nowhere
# else, and nothing in this module should be read as separating the two.
#
# the budget, and why the termination is on evaluations and not on generations.
# CONTEXT.md section 5 step 4 gives all three solvers the same budget,
# pop_size * n_gen function evaluations. under pymoo's ("n_gen", n) termination
# nsga-ii spends exactly that and mopso_cd spends one population more, measured
# in this session at pop_size = 20: 60, 100 and 200 evaluations for nsga-ii at
# n_gen 3, 5 and 10 against 80, 120 and 220 for mopso_cd, which is the initial
# swarm being evaluated outside the generation count. a budget that is 10 per
# cent larger for one solver is not budget parity, and the number carried on the
# record would then be nominal rather than true. terminating on
# MaximumFunctionCallTermination(pop_size * n_gen) makes both solvers spend
# exactly the stated budget, 60, 100 and 200 for both, and the count pymoo itself
# reports is asserted in the tests rather than assumed. n_gen and pop_size stay
# in the signature because they are what CONTEXT.md section 10 c2 states and
# because pop_size is a real parameter of both algorithms; only the stopping rule
# is expressed in the currency the budget is stated in.
#
# mopso_cd's archive, which is a reproducibility matter and not a tuning one.
# pymoo 0.6.2's Algorithm.advance, core/algorithm.py line 249, adds every infill
# to the algorithm's archive, and MultiObjectiveArchive truncates itself with
# RandomTruncation once it passes max_size, util/archive.py lines 86 and 87 inside
# Archive.add, the class itself being at lines 16 to 19. that truncation is
# decorated with default_random_state and is called with no random_state, so it
# draws from np.random.default_rng(None), a generator seeded from the operating
# system that neither minimize(seed=s) nor numpy.random.seed reaches. the run is
# therefore not reproducible once the archive overflows: measured on p1 under
# phi_ls at pop_size 40 and n_gen 20, five runs at one seed gave five different
# fronts, 179, 178, 184, 194 and 189 rows, diverging at generation 17 with the
# seeded generator's state still identical at that point, which is what rules out
# the seeded stream as the cause. nsga-ii holds no archive and is unaffected.
#
# what c2 did about it, and why c2-b reversed it. c2 set archive_size to the whole
# evaluation budget, so that the archive could never overflow and the truncation
# was never reached. that works and it is reproducible, but it is the larger
# intervention of the two, and c2 justified it with a rule it had inverted. the
# archive is mopso's leader pool: leaders are drawn from it by binary tournament,
# _select_diverse_leaders, so taking it from 200 to the 6295 rows c2 measured at
# budget 20000 changes what the search does, and it costs, the archive being
# re-sorted for non-domination every generation. seeding the truncation changes
# nothing but the generator it draws from: the same uniform choice, without
# replacement, of the same number of rows from the same archive of the same size.
# the option c2 chose modifies the algorithm's behaviour and the option c2
# rejected preserves it, so c2-b takes the second and mopso runs at pymoo's own
# archive_size of 200.
#
# how it is installed, and why a subclass is needed at all. pymoo's Algorithm does
# accept an archive object as a constructor argument, core/algorithm.py line 34
# and line 58, and MOPSO_CD passes **kwargs through to it, so an archive can be
# handed in. it does not survive: MOPSO_CD._setup overwrites it at line 77 with
# MultiObjectiveArchive(max_size=self.archive_size), and _update_archive builds
# another fresh one at lines 216 to 219 on every generation, so an archive given
# at construction is discarded twice. the only place the truncation can be fixed
# is therefore the archive that _update_archive installs, which is what
# SeededArchiveMopso below overrides, in three lines and by delegation: pymoo's
# own _update_archive runs unchanged and the archive it returns is reinstalled
# with a seeded truncation. the truncate_size is pymoo's, 100, because
# MultiObjectiveArchive computes min(max_size, 100) either way.
# the generator is the algorithm's own seeded one rather than a second generator
# of this module's, so the run stays a single seeded stream and there is no second
# seed for a table to have to record.
#
# what the reversal costs and saves, measured in c2-b on p1 under phi_lu at
# pop_size 100, the three arms run back to back in one process. seconds, and the
# rows the run returns, at budgets 500, 1000, 2000, 4000 and 20000:
#     seeded truncation, archive 200   0.09  0.30  0.82  2.05   11.71   k <= 200
#     c2's resize, archive = budget    0.08  0.32  1.18  6.61  187.78   k to 6295
#     pymoo default, archive 200       0.08  0.32  0.82  1.91   10.35   k <= 200
# the seeded arm tracks pymoo's own default, which is the point: the two differ
# only in which generator the truncation draws from, and the gap between them at
# budget 20000, 11.71 against 10.35 seconds, is the cost of that and of one extra
# archive object per generation. against c2's resize it is a factor of 16 at
# budget 20000, and the front comes back at pymoo's archive size rather than at
# 6295 rows. the absolute seconds are lower than the ones c2 recorded, 228.84 for
# the resize at budget 20000, because c2 measured with three processes running;
# the ratios are what carry across.
#
# the seed is set twice, through numpy.random.seed and through minimize.
# CONTEXT.md section 10 c2 asks for both and s-10 records that the stated reason
# is inverted, v-38 having measured minimize(seed=s) to be bit-reproducible on
# its own. the instruction is kept because the global state costs nothing and
# because the archive finding above shows that pymoo 0.6.2 does reach generators
# neither call controls, so removing either call on the strength of one
# measurement is not warranted. neither call fixes the archive; only the seeded
# truncation does.
#
# no endpoint is rebuilt from a centre and a radius anywhere, d-02: the problem
# names the representation its intervals are computed in and phi_image asks the
# phi record for that route by name. no tolerance is introduced either, here or
# in pymoo, which compares raw doubles; CONTEXT.md section 5 records that its
# NonDominatedSorting epsilon argument is a translation and cannot change a
# front. the front this module returns is pymoo's own and is not re-filtered:
# tests/test_runners.py asserts that the project's dominance relation is the
# identity on it, and re-filtering would hide a disagreement rather than report
# one.
#
# [1] is papers/new_preference_order_relationships_paper.txt, costa,
# osuna-gomez and chalco-cano, fuzzy sets and systems 477 (2024) 108812.

import numpy as np
from pymoo.algorithms.moo.mopso_cd import MOPSO_CD
from pymoo.algorithms.moo.nsga2 import NSGA2
from pymoo.core.problem import Problem as PymooProblem
from pymoo.optimize import minimize
from pymoo.termination.max_eval import MaximumFunctionCallTermination
from pymoo.util.archive import MultiObjectiveArchive, Truncation

from phi_transforms import phi_registry
from random_search import SearchResult, phi_image, require_phi, require_seeds


# the transformed real problem of theorem 3.1, in the form pymoo minimises
class TransformedProblem(PymooProblem):

    # builds the 2m-objective real problem of one interval problem under one phi
    def __init__(self, problem, record, params):
        # the box comes from the problem and is never hardcoded, CONTEXT.md
        # section 10 c2: p0's is [-1, 1], p1's is [-0.5, 1.5]^2 and both tier 1
        # benchmarks are on the unit cube. n_obj is 2m and not m, the doubling
        # being phi's, which is the confusion src/problems_tier0.py warns about
        # at the interface where it would be made.
        lower, upper = problem.bounds()
        super().__init__(n_var=problem.n_vars, n_obj=2 * problem.n_obj,
                         xl=np.asarray(lower, dtype=float),
                         xu=np.asarray(upper, dtype=float))
        self.interval_problem = problem
        self.record = record
        self.params = params

    # evaluates the interval problem once and hands pymoo the 2m columns of phi
    def _evaluate(self, x, out, *args, **kwargs):
        pairs = self.interval_problem.evaluate(x, self.params)
        out["F"] = phi_image(self.interval_problem, pairs, self.record)


# the budget in evaluations, pop_size * n_gen, refused unless both are at least one
def evaluation_budget(n_gen, pop_size):
    generations, population = int(n_gen), int(pop_size)
    if generations < 1 or population < 1:
        raise ValueError(
            "n_gen and pop_size must both be at least 1; got n_gen = {} and "
            "pop_size = {}".format(n_gen, pop_size))
    return generations * population


# nsga-ii at one population size, pymoo's defaults otherwise
def make_nsga2(pop_size, n_evals):
    return NSGA2(pop_size=int(pop_size))


# pymoo's random archive truncation, drawn from a generator the caller controls
class SeededTruncation(Truncation):

    # keeps the generator the truncation is to draw from
    def __init__(self, random_state):
        super().__init__()
        self.random_state = random_state

    # the uniform choice without replacement of util/archive.py lines 16 to 19
    def __call__(self, sols, k):
        # RandomTruncation's own line, with the generator supplied instead of
        # left to default_random_state, which would build one from the operating
        # system. same distribution, same archive, same count; nothing about the
        # search changes.
        return self.random_state.choice(sols, size=k, replace=False)


# mopso_cd with the archive truncation drawn from the algorithm's seeded generator
class SeededArchiveMopso(MOPSO_CD):

    # pymoo's own archive update, with the seeded truncation reinstalled on it
    def _update_archive(self, pop):
        # the delegation is the whole of the override: mopso's non-dominated
        # sorting, its crowding-distance pruning and its archive size are pymoo's
        # and are not reimplemented here. only the truncation the base class will
        # reach through Archive.add is replaced, and only in the generator it
        # draws from.
        archive = super()._update_archive(pop)
        return MultiObjectiveArchive(individuals=archive, max_size=self.archive_size,
                                     truncation=SeededTruncation(self.random_state))


# mopso_cd at one population size, at pymoo's own archive size, seeded throughout
def make_mopso(pop_size, n_evals):
    # archive_size is left at pymoo's default of 200 on purpose, c2-b: the
    # reproducibility problem is the unseeded generator and not the size, and
    # resizing the archive would change the leader pool and the cost. n_evals is
    # taken for one factory signature with make_nsga2 and is not used.
    return SeededArchiveMopso(pop_size=int(pop_size))


# one seed of one pymoo algorithm on the transformed problem, as a SearchResult
def solve_once(problem, record, params, make_algorithm, n_gen, pop_size, seed):
    n_evals = evaluation_budget(n_gen, pop_size)
    # both seeding calls, per CONTEXT.md section 10 c2 and s-10.
    np.random.seed(seed)
    result = minimize(TransformedProblem(problem, record, params),
                      make_algorithm(pop_size, n_evals),
                      MaximumFunctionCallTermination(n_evals),
                      seed=seed, verbose=False)
    front = np.atleast_2d(np.asarray(result.F, dtype=float))
    decision_vectors = np.atleast_2d(np.asarray(result.X, dtype=float))
    return SearchResult(seed=seed, n_evals=n_evals, front=front,
                        decision_vectors=decision_vectors)


# one pymoo algorithm under one phi at a stated budget, one result per seed
def run_solver(problem, phi_name, params, make_algorithm, n_gen, pop_size, seeds):
    require_phi(phi_name)
    require_seeds(seeds)
    record = phi_registry[phi_name]
    return [solve_once(problem, record, params, make_algorithm, n_gen, pop_size, seed)
            for seed in seeds]


# nsga-ii under one phi at a stated budget, one result per seed
def run_nsga2(problem, phi_name, params, n_gen, pop_size, seeds):
    return run_solver(problem, phi_name, params, make_nsga2, n_gen, pop_size, seeds)


# mopso_cd under one phi at a stated budget, one result per seed
def run_mopso(problem, phi_name, params, n_gen, pop_size, seeds):
    # mopso_cd and not pso: pymoo 0.6.2's standard pso is single-objective and
    # asserts a one-column objective matrix, v-36 and v-37, and the class is
    # named MOPSO_CD with the underscore.
    return run_solver(problem, phi_name, params, make_mopso, n_gen, pop_size, seeds)
