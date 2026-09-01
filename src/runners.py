# c2: nsga-ii and mopso from pymoo, on the transformed real problem theorem 3.1
# of [1] licenses solving. the two solvers of slide 17 that are not the control.
#
# what this module is and is not. it is a wrapper: pymoo is used unmodified and
# no operator, survival rule or dominance test of it is replaced. what the module
# owns is the problem handed to pymoo, the budget the run is stopped at, and the
# record the run is returned in, and all three are shared with c1 so that the
# three solvers are comparable by construction. the transform is
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
# decorated with default_random_state and is called with no
# random_state, so it draws from np.random.default_rng(None), a generator seeded
# from the operating system that neither minimize(seed=s) nor numpy.random.seed
# reaches. with mopso_cd's default archive_size of 200 the run is therefore not
# reproducible once the archive overflows: measured here on p1 under phi_ls at
# pop_size 40 and n_gen 20, five runs at one seed gave five different fronts,
# 179, 178, 184, 194 and 189 rows, diverging at generation 17 with the seeded
# generator's state still identical at that point, which is what rules out the
# seeded stream as the cause. sizing the archive to the whole budget means the
# archive can never exceed it, since it holds at most one entry per evaluation,
# so the truncation branch is never entered and the run is bit-reproducible;
# measured on p1, zdt1, dtlz2 and p0 under all three phi. the archive is a stated
# parameter of the algorithm and setting it is not a modification of it, but it
# is a choice, it is not free in either sense, and it is d-03 to the research chat.
#
# what the archive choice costs, measured rather than argued. it changes what
# mopso does and not only what it records: leaders are drawn from the archive by
# binary tournament, so a larger archive is a larger leader pool. and it changes
# what mopso costs, the archive being re-sorted for non-domination every
# generation, which is quadratic in its size. on p1 under phi_lu at pop_size 100,
# budgets 500, 1000, 2000 and 4000 take 0.17, 0.59, 2.58 and 10.60 seconds with
# the archive at the budget against 0.17, 0.64, 1.84 and 3.64 at pymoo's default
# of 200, and at budget 20000 the run takes 228.84 seconds and ends with 6295
# archive rows, against nsga-ii's 1.54 seconds at the same budget. so the cost is
# roughly quadratic in the budget, and it is r-15, which e1 has to plan around.
# the alternative that would keep both the default archive and reproducibility is
# to override mopso_cd's _update_archive so that the archive it installs truncates
# deterministically. it is rejected here and not silently: CONTEXT.md section 10
# c2 says pymoo is used unmodified, and replacing an algorithm's archive policy is
# a modification of the algorithm rather than a setting of it, so it is not a
# change an agent takes on its own.
#
# the seed is set twice, through numpy.random.seed and through minimize.
# CONTEXT.md section 10 c2 asks for both and s-10 records that the stated reason
# is inverted, v-38 having measured minimize(seed=s) to be bit-reproducible on
# its own. the instruction is kept because the global state costs nothing and
# because the archive finding above shows that pymoo 0.6.2 does reach generators
# neither call controls, so removing either call on the strength of one
# measurement is not warranted. neither call fixes the archive; only the size
# does.
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


# mopso_cd at one population size, its archive sized to the whole budget
def make_mopso(pop_size, n_evals):
    # the reproducibility reason is at the head of this module: pymoo 0.6.2
    # truncates an overflowing archive from an unseeded generator, so an archive
    # that cannot overflow is what makes the run reproducible. n_evals is the
    # smallest such size, the archive holding at most one entry per evaluation.
    return MOPSO_CD(pop_size=int(pop_size), archive_size=int(n_evals))


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
