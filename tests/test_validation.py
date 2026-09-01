# c3, the validation gate, as c3-b restates it. this file is not a report on the
# solvers: it is the check that decides whether phase e starts. it runs all three
# solvers on p1 under all three phi at the budget r-15 fixed, over a stated seed
# list, and compares the recovered decision vectors against the sets
# docs/b1_phi_efficient_sets.md derived and src/reference_fronts.py encodes.
#
# what c3-b changes, and it is only what is asserted and what is reported: no
# phi, no problem, no derivation, no solver and no dominance relation is touched,
# and nothing here produces a number c3 did not produce. c3 asserted both
# hausdorff directions against the tolerance and twelve of forty-five
# configurations failed, every one of them forward. that assertion cannot pass,
# and the reason is a fact about filtering a finite sample rather than a fact
# about the solvers.
#
# the mechanism, in one paragraph, because the reason has to survive this file.
# under phi_cw the four image columns are (c_1, r_1, c_2, r_2) and under phi_ls
# they are (c_1 - r_1, 2 r_1, c_2 - r_2, 2 r_2), so both carry a column that is a
# function of one decision variable alone: r_2 = rho x_1^2 + delta does not move
# with x_2 and r_1 = rho x_2^2 + delta does not move with x_1. in any finite set
# of candidates the point of smallest |x_1| is then the strict minimiser of that
# column, so no other candidate is no worse in every column and no candidate can
# dominate it, whatever its x_2 is. it survives every filter and it enters every
# front. its x_2 ranges over the whole box, [-1/2, 3/2], while b1 section 2.4
# puts X_cw's x_2 in [0, 1], so the forward distance carries a floor of up to 1/2
# that no solver and no budget removes. c3 measured 0.5000154 at mopso, phi_ls,
# seed 11, which is that overhang exactly. phi_lu has no such column, its four
# being (c_1 - r_1, c_1 + r_1, c_2 - r_2, c_2 + r_2), and that is why c3's phi_lu
# outliers were the only ones off the two singular lines.
# test_one_image_column_is_a_function_of_one_variable_under_ls_and_cw and
# test_the_extreme_points_of_a_finite_sample_survive_the_filter assert both halves
# of that argument, so it is checked here and not merely narrated.
#
# so the gate asserts, pass or fail, in both directions of the pipeline:
#   reference to solver   was what exists found. the largest distance from a point
#                         of the derived set to the recovered set, against the
#                         tolerance c3 derived and c3-b does not adjust. this is
#                         the convergence question and it passes in all ninety
#                         measurements.
#   no solver point       a solver cannot beat the analytic answer. asserted in c1
#   dominates the         and c2 already, and asserted here as well because the
#   derived set           gate is where the claim that the derivation and the
#                         solvers agree is actually made.
#
# and the gate reports, never asserts:
#   the forward hausdorff, per configuration, bounded below by the artifact above
#       and therefore not a quality measure.
#   the count of solver front points dominated by the reference front, as a
#       fraction of front size, for all three solvers. this is the quality
#       measure: a solver point dominated by a known-efficient point is one the
#       solver should have improved on, and no sampling artifact produces one.
#   the front cardinality beside every number, r-16.
# both are carried in the message of the asserted tests, so a failure prints them
# without anything being rerun, and docs/c3_validation.md tables them in full.
#
# and the gate asserts one trend, for the population methods only: the dominated
# fraction does not rise when the budget is quadrupled, for nsga-ii and mopso, per
# phi and per setting of the singular flag, read over the five seeds and not per
# seed. monotone improvement and not a threshold, because what a population method
# should do with four times the budget is stop returning points a known-efficient
# point beats. random search is excluded and
# test_random_search_keeps_its_extreme_points_at_four_times_the_budget is the
# reason: its front always contains the sample's column-wise extreme points, no
# budget removes them, and c3 measured its forward distance unchanged to four
# decimal places at 20000 evaluations.
#
# that trend assertion currently fails in three of its twelve cells, all phi_cw,
# and the failure is reported rather than accommodated: r-18 and
# docs/c3_validation.md section 6. nothing about the assertion was moved to make
# it pass, and pooling over phi as well as over seeds, which would make both
# solvers pass, is exactly the adjustment that was refused.
#
# recovery is measured by hausdorff distance in the decision space and never by
# igd, CONTEXT.md section 10 c3 and r-13: b2 samples through b1's weight map,
# whose density in objective space is the parametrisation's and not the front's,
# and igd averages over reference points, so it weights a densely sampled region
# more heavily. hausdorff is a maximum and is insensitive to that.
#
# the tolerance and where it comes from, unchanged from c3 and not adjusted to
# make anything pass. both sets in every comparison are finite samples of the same
# two-dimensional region, and each carries its own resolution floor:
#   h_reference   the covering radius of the derived region by b2's reference
#                 sample at reference_points. no distance to that sample can be
#                 read as smaller than this, whatever the solver did.
#   h_design      the covering radius of the derived region by a front of
#                 front_design_size points drawn uniformly from it. this is what
#                 a perfect solver returning a design-sized front achieves in the
#                 reference-to-solver direction, and it is a property of the
#                 region and not of any solver.
# the tolerance is their sum, per phi, with no free multiplier: every term is
# measured, at a size fixed in advance, on the region b1 derived. front_design_size
# is nsga-ii's population, which is the smallest front the design fixes before a
# run rather than reads off one, mopso's archive bound being 200 and random
# search's count being whatever is non-dominated. the sum rather than either
# alone: c3 floored the forward direction by h_reference and the reverse by
# h_design and needed room for both. r-17 stands, the verdict being sensitive to
# the reading of h_design within a factor of about 1.5, and it now bites only on
# the reverse direction, which passes with margin under both readings.
#
# front cardinality is reported beside every number, r-16, and nothing is
# truncated to a common size. r-16 is about objective-space metrics that move
# with the number of rows; hausdorff is a maximum over two sets and truncating
# either of them here would discard real coverage, which is the d1 addition
# CONTEXT.md section 10 d1 now records.
#
# p0 is a smoke test and not a fixture, b1 section 7.4, and this file treats it as
# one: it checks that a solver finds the published anchor x = 0 and nothing more.
# under phi_lu and phi_ls p0's optimal set is the whole decision box, so finding
# the anchor is a weaker statement than it looks, and docs/c3_validation.md says so.
#
# every test that runs a solver is marked slow. the runs are cached per solver,
# phi and budget, so each grid is executed once and not once per assertion.

import numpy as np
import pytest

from phi_transforms import phi_registry
from problems_tier0 import p0, p0_anchor, p1, p1_default_params
from random_search import (non_dominated_indices, phi_image, run_random_search,
                           sample_decision_space)
from reference_fronts import efficient_set, reference_front
from runners import run_mopso, run_nsga2

phi_names = ("lu", "ls", "cw")
# the budget r-15 fixed for e1 and e2, and the population c2-b timed it at. the
# gate runs at the budget the experiments will run at, because a gate passed at a
# budget nothing else uses says nothing about the runs that follow it.
gate_pop_size = 100
gate_n_gen = 50
gate_n_evals = gate_pop_size * gate_n_gen
# the multiple the trend is asserted across. four, because c3 measured the budget
# question at four times the budget and this is the same measurement read on the
# dominated count rather than on the forward distance.
budget_multiple = 4
# the stated seed list. five rather than one, CONTEXT.md section 10 c2: a single
# run gives no variance and a failure on one seed of five is a different finding
# from a failure on all five, which is what the diagnosis order in the c3 brief
# turns on.
gate_seeds = (11, 12, 13, 14, 15)
# the reference sample size, the one tests/test_runners.py already uses.
reference_points = 1000
# nsga-ii's population, the smallest front size the design fixes in advance.
front_design_size = 100
# the uniform region sample the two floors are measured on, and the draw count
# and seed that make that measurement reproducible.
tolerance_sample_size = 20000
tolerance_draws = 20
tolerance_seed = 20260903
# p0's anchor tolerance, on the same principle as p1's and in one dimension: the
# box is [-1, 1], of length 2, and a design-sized front resolves it to
# 2 / front_design_size. under phi_cw the anchor is the whole optimal set and a
# solver should do far better than this; under phi_lu and phi_ls the whole box is
# optimal and the front merely has to have a point there.
anchor_tolerance = 2.0 / front_design_size

# the three solvers behind one call signature, so no solver is tested less than
# another. random search is the control, CONTEXT.md section 10 c1, and is in the
# grid on the same terms as the other two.
solver_ids = ("random_search", "nsga2", "mopso")
# the population methods, the only ones the budget trend is asserted for. random
# search is excluded because its front contains the sample's column-wise extreme
# points by construction, which is the mechanism at the head of this file, and no
# budget removes them: c3 measured its forward distance unchanged to four decimal
# places at 20000 evaluations, and
# test_random_search_keeps_its_extreme_points_at_four_times_the_budget is that
# evidence carried in the file rather than quoted from a document.
population_solver_ids = ("nsga2", "mopso")
run_cache = {}
tolerance_cache = {}
# the measurements of one run, cached by configuration. the gate reads the same
# numbers from three tests and the trend reads them again at two budgets, so
# without this the hausdorff distances and the dominated counts of one run are
# recomputed five times.
recovery_cache = {}

# b1 section 2.4's closed-form regions, written out here and not imported from
# src/. tests/test_reference_fronts.py carries the same forms for the same
# reason: a region the module also holds would make the check a file agreeing
# with itself. the two copies are the same three inequalities from the same
# section, and c2's precedent for copying a helper between test files rather than
# sharing it is followed here rather than reopened.
four_thirds = 4.0 / 3.0

# the two points c3 recorded as s-13, in the order c3 lists them: the worst point
# of random search under phi_cw at seed 15 and of mopso under phi_cw at seed 13.
# both lie on the singular line x_2 = 0 beyond x_1 = 1.
s13_points = np.array([[1.42192, -0.00039], [1.50000, 0.00026]])


# whether each point lies in the closed region b1 section 2.4 derived for one phi
def in_region(phi_name, points):
    x_1, x_2 = points[:, 0], points[:, 1]
    ls_form = 7.0 * x_1 * x_2 - 4.0 * x_1 + 12.0 * x_2 - 16.0
    if phi_name == "lu":
        return (x_1 >= 0.0) & (4.0 * x_1 - x_1 * x_2 - 20.0 * x_2 + 16.0 <= 0.0) \
            & (ls_form <= 0.0)
    if phi_name == "ls":
        return (x_1 >= 0.0) & (x_2 >= 0.0) & (x_1 <= four_thirds) \
            & (x_2 <= four_thirds) & (ls_form <= 0.0)
    return (x_1 >= 0.0) & (x_2 >= 0.0) & (x_1 <= 1.0) & (x_2 <= 1.0)


# a uniform sample of one derived region, by rejection from p1's decision box
def region_sample(phi_name, size, seed):
    # uniform on the region and not on b2's weight simplex on purpose. the weight
    # sample is dirichlet at concentration 0.3, src/reference_fronts.py, so its
    # density in the decision space is the parametrisation's; a covering radius
    # measured against it would inherit that density, and the floors here are
    # meant to be properties of the region.
    lower, upper = p1.bounds()
    generator = np.random.default_rng(seed)
    kept = []
    total = 0
    while total < size:
        block = generator.uniform(lower, upper, size=(4 * size, p1.n_vars))
        inside = block[in_region(phi_name, block)]
        kept.append(inside)
        total += len(inside)
    return np.concatenate(kept)[:size]


# the directed hausdorff distance, the largest distance from a point of a to b
def directed_hausdorff(set_a, set_b, block=256):
    # euclidean, in the decision space, which is the space common to every phi,
    # CONTEXT.md section 5 step 5. blocked for memory only: the comparison is
    # against the whole of set_b either way.
    a = np.atleast_2d(np.asarray(set_a, dtype=float))
    b = np.atleast_2d(np.asarray(set_b, dtype=float))
    worst = 0.0
    for start in range(0, len(a), block):
        chunk = a[start:start + block]
        distances = np.sqrt(np.sum((chunk[:, None, :] - b[None, :, :]) ** 2, axis=2))
        worst = max(worst, float(np.max(np.min(distances, axis=1))))
    return worst


# the count of rows of one image set that some row of another image set dominates
def dominated_count(rows, by_rows, block=200):
    # the ordinary pareto relation on doubles, the project's one relation,
    # CONTEXT.md section 5 and d-02, with no tolerance anywhere. read in the
    # direction the argument needs at each call site: with the solver front first
    # it counts the solver points a reference point beats, and with the reference
    # front first it counts the reference points a solver beats, which must be
    # zero.
    a = np.asarray(rows, dtype=float)
    b = np.asarray(by_rows, dtype=float)
    total = 0
    for start in range(0, len(a), block):
        chunk = a[start:start + block]
        not_worse = np.all(b[None, :, :] <= chunk[:, None, :], axis=2)
        strictly_better = np.any(b[None, :, :] < chunk[:, None, :], axis=2)
        total += int(np.count_nonzero(np.any(not_worse & strictly_better, axis=1)))
    return total


# the covering radius of one derived region by a given point set
def covering_radius(phi_name, points, sample):
    return directed_hausdorff(sample, points)


# the two resolution floors and the gate tolerance they sum to, for one phi
def tolerance_terms(phi_name):
    if phi_name not in tolerance_cache:
        sample = region_sample(phi_name, tolerance_sample_size, tolerance_seed)
        reference, _ = efficient_set(p1, phi_name, reference_points, False)
        h_reference = covering_radius(phi_name, reference, sample)
        generator = np.random.default_rng(tolerance_seed)
        radii = [covering_radius(phi_name,
                                 sample[generator.choice(len(sample), front_design_size,
                                                         replace=False)], sample)
                 for _ in range(tolerance_draws)]
        h_design = float(np.mean(radii))
        tolerance_cache[phi_name] = (h_reference, h_design, h_reference + h_design)
    return tolerance_cache[phi_name]


# the gate tolerance for one phi, the sum of the two measured floors
def gate_tolerance(phi_name):
    return tolerance_terms(phi_name)[2]


# one solver's runs on one problem under one phi at one budget, over the seeds
def solver_runs(solver_id, problem, params, phi_name, multiple=1):
    key = (solver_id, problem.name, phi_name, multiple)
    if key not in run_cache:
        seeds = list(gate_seeds)
        n_gen = gate_n_gen * multiple
        if solver_id == "random_search":
            runs = run_random_search(problem, phi_name, params,
                                     gate_n_evals * multiple, seeds)
        elif solver_id == "nsga2":
            runs = run_nsga2(problem, phi_name, params, n_gen, gate_pop_size, seeds)
        else:
            runs = run_mopso(problem, phi_name, params, n_gen, gate_pop_size, seeds)
        run_cache[key] = runs
    return run_cache[key]


# the run of one solver under one phi at one seed and one budget
def one_run(solver_id, problem, params, phi_name, seed, multiple=1):
    runs = solver_runs(solver_id, problem, params, phi_name, multiple)
    return runs[list(gate_seeds).index(seed)]


# every number the gate asserts and every number it reports, for one run
def recovery(solver_id, phi_name, seed, include_singular, multiple=1):
    key = (solver_id, phi_name, seed, include_singular, multiple)
    if key not in recovery_cache:
        run = one_run(solver_id, p1, p1_default_params, phi_name, seed, multiple)
        reference, _ = efficient_set(p1, phi_name, reference_points, include_singular)
        front = reference_front(p1, phi_name, reference_points, include_singular)
        recovered = run.decision_vectors
        recovery_cache[key] = {
            "solver_to_reference": directed_hausdorff(recovered, reference),
            "reference_to_solver": directed_hausdorff(reference, recovered),
            "dominated": dominated_count(run.front, front),
            "beats_reference": dominated_count(front, run.front),
            "k_solver": len(recovered), "k_reference": len(reference)}
    return recovery_cache[key]


# one line carrying everything the gate asserts and everything it reports
def report_line(solver_id, phi_name, seed, include_singular, measured, tolerance):
    return ("{} on p1 under phi_{}, seed {}, include_singular_segments {}: "
            "reference to solver {:.4f} against tolerance {:.4f}; reported, solver "
            "to reference {:.4f}, which carries the finite-sample floor and is not "
            "a quality measure, and {} of {} front points dominated by the "
            "reference front, {:.1%}; k_solver {}, k_reference {}"
            .format(solver_id, phi_name, seed, include_singular,
                    measured["reference_to_solver"], tolerance,
                    measured["solver_to_reference"], measured["dominated"],
                    measured["k_solver"],
                    measured["dominated"] / measured["k_solver"],
                    measured["k_solver"], measured["k_reference"]))


# how many points of the phi_lu non-dominated set are absent from the phi_ls one
def lu_points_outside_ls(problem, points, params):
    # docs/a_close_containment.md corollary 1 makes ND_lu a subset of ND_ls
    # exactly, in real arithmetic, so this count is zero as an identity and any
    # positive value is a violation of an identity in doubles. it is a diagnostic
    # of the pipeline's arithmetic and never a result about phi, CONTEXT.md
    # section 10 c3. the sets are index sets over one evaluation of one array,
    # which is the form the containment is a statement about; an intersection of
    # value tuples would be a weaker and different claim.
    pairs = problem.evaluate(points, params)
    sets = {name: frozenset(non_dominated_indices(phi_image(problem, pairs, record)).tolist())
            for name, record in phi_registry.items()}
    return len(sets["lu"] - sets["ls"]), len(sets["lu"]), len(sets["ls"])


# the indices of the points of smallest |x_1| and of smallest |x_2| in a set
def extreme_point_indices(points):
    # these are the two the mechanism at the head of this file is about: under
    # phi_ls and phi_cw they are the strict minimisers of a width column, so they
    # are non-dominated in the set they are drawn from whatever their other
    # coordinate is.
    return (int(np.argmin(np.abs(points[:, 0]))), int(np.argmin(np.abs(points[:, 1]))))


# the gate, direction one: every part of the derived set is reached by the solver
@pytest.mark.slow
@pytest.mark.parametrize("solver_id", solver_ids)
@pytest.mark.parametrize("phi_name", phi_names)
@pytest.mark.parametrize("seed", gate_seeds)
@pytest.mark.parametrize("include_singular", (False, True))
def test_the_derived_set_is_reached_by_the_solver(solver_id, phi_name, seed,
                                                  include_singular):
    # the convergence question, and the only distance the gate asserts. the
    # forward direction is reported in the same message and is never asserted:
    # the head of this file derives its floor and
    # test_one_image_column_is_a_function_of_one_variable_under_ls_and_cw asserts
    # the mechanism that produces it.
    measured = recovery(solver_id, phi_name, seed, include_singular)
    tolerance = gate_tolerance(phi_name)
    assert measured["reference_to_solver"] <= tolerance, \
        report_line(solver_id, phi_name, seed, include_singular, measured, tolerance)


# the gate, direction two: no solver point dominates any point of the derived set
@pytest.mark.slow
@pytest.mark.parametrize("solver_id", solver_ids)
@pytest.mark.parametrize("phi_name", phi_names)
@pytest.mark.parametrize("seed", gate_seeds)
@pytest.mark.parametrize("include_singular", (False, True))
def test_no_solver_point_dominates_the_derived_set(solver_id, phi_name, seed,
                                                   include_singular):
    # a solver cannot beat the analytic answer. tests/test_runners.py asserts this
    # at one seed as a check on the solvers; the gate asserts it over the whole
    # grid, because the gate is where the claim that the derivation and the
    # solvers agree is made. if it ever fails, the first thing to check is whether
    # the offending points sit on a boundary of the derived region,
    # docs/b1_phi_efficient_sets.md section 2.4, and only then whether the
    # derivation is wrong.
    measured = recovery(solver_id, phi_name, seed, include_singular)
    tolerance = gate_tolerance(phi_name)
    assert measured["beats_reference"] == 0, \
        report_line(solver_id, phi_name, seed, include_singular, measured, tolerance)


# the dominated count of one solver and phi at one budget, pooled over the seeds
def pooled_dominated(solver_id, phi_name, include_singular, multiple):
    measured = [recovery(solver_id, phi_name, seed, include_singular, multiple)
                for seed in gate_seeds]
    return (sum(m["dominated"] for m in measured),
            sum(m["k_solver"] for m in measured),
            [m["dominated"] for m in measured])


# the population methods return fewer dominated points at four times the budget
@pytest.mark.slow
@pytest.mark.parametrize("solver_id", population_solver_ids)
@pytest.mark.parametrize("phi_name", phi_names)
@pytest.mark.parametrize("include_singular", (False, True))
def test_the_dominated_fraction_falls_when_the_budget_is_quadrupled(solver_id,
                                                                    phi_name,
                                                                    include_singular):
    # monotone improvement and not a threshold. the fraction of a front that a
    # known-efficient point beats is the one quality measure here that carries no
    # sampling artifact, v-53, so what a population method should do with four
    # times the budget is not raise it.
    # read over the seed list and not per seed, and that is the project's own
    # rule and not a choice made to make this pass: CONTEXT.md section 10 c2 puts
    # five seeds in the design because one run gives no variance, so a trend read
    # at one seed is a trend read on one run. the per-seed numbers move by up to
    # six points of a hundred in both directions and docs/c3_validation.md section
    # 6.1 tables all thirty; the pooled fraction is the unit the seed list exists
    # to supply.
    # random search is excluded and
    # test_random_search_keeps_its_extreme_points_at_four_times_the_budget carries
    # the reason.
    before, k_before, per_seed_before = pooled_dominated(solver_id, phi_name,
                                                        include_singular, 1)
    after, k_after, per_seed_after = pooled_dominated(solver_id, phi_name,
                                                     include_singular,
                                                     budget_multiple)
    assert after / k_after <= before / k_before, (
        "{} on p1 under phi_{}, include_singular_segments {}: the dominated "
        "fraction rises from {} of {}, {:.2%}, at budget {} to {} of {}, {:.2%}, "
        "at budget {}. per seed {} against {} over seeds {}"
        .format(solver_id, phi_name, include_singular, before, k_before,
                before / k_before, gate_n_evals, after, k_after, after / k_after,
                gate_n_evals * budget_multiple, per_seed_before, per_seed_after,
                list(gate_seeds)))


# the reason random search is excluded from the trend, measured rather than quoted
@pytest.mark.parametrize("phi_name", ("ls", "cw"))
@pytest.mark.parametrize("seed", gate_seeds)
def test_random_search_keeps_its_extreme_points_at_four_times_the_budget(phi_name,
                                                                         seed):
    # the control's front contains the sample's column-wise extreme points at
    # every budget, and a larger sample supplies a new pair rather than removing
    # the old one. that is why quadrupling the budget left c3's forward distance
    # unchanged to four decimal places, and it is why the trend above is asserted
    # for the population methods only.
    # this runs no solver and it does not need to: src/random_search.py's
    # search_once draws exactly sample_decision_space(problem.bounds(), n_evals,
    # seed) and returns the non-dominated subset of it, so a point of that sample
    # is in the front exactly when no row of the sample dominates it. checking the
    # one point against the sample is that statement, at linear cost instead of
    # the quadratic cost of the filter.
    sample = sample_decision_space(p1.bounds(), gate_n_evals * budget_multiple, seed)
    image = phi_image(p1, p1.evaluate(sample, p1_default_params),
                      phi_registry[phi_name])
    for name, index in zip(("smallest |x_1|", "smallest |x_2|"),
                           extreme_point_indices(sample)):
        beaten = dominated_count(image[index:index + 1], image)
        assert beaten == 0, (
            "phi_{}, seed {}: the point of {}, {}, is dominated in a sample of {}, "
            "so it would not enter random search's front at that budget"
            .format(phi_name, seed, name, sample[index], len(sample)))


# phi_ls and phi_cw carry a width column and phi_lu does not, which is the cause
@pytest.mark.parametrize("phi_name", phi_names)
def test_one_image_column_is_a_function_of_one_variable_under_ls_and_cw(phi_name):
    # the first half of the mechanism at the head of this file, asserted. holding
    # x_1 fixed and moving x_2 leaves r_2 = rho x_1^2 + delta unchanged, so a
    # column that is r_2 up to a positive factor is constant along that move.
    # phi_cw's fourth column is r_2 and phi_ls's is 2 r_2; phi_lu's are c_2 -+ r_2
    # and c_2 moves with x_2, so none of its four is constant. the same holds with
    # the variables exchanged, r_1 driving the second column.
    record = phi_registry[phi_name]
    fixed_x_1 = np.array([[0.4, -0.5], [0.4, 0.3], [0.4, 1.5]])
    fixed_x_2 = np.array([[-0.5, 0.4], [0.3, 0.4], [1.5, 0.4]])
    constant_along_x_2 = [column for column, values in
                          enumerate(phi_image(p1, p1.evaluate(fixed_x_1, p1_default_params),
                                              record).T)
                          if np.ptp(values) == 0.0]
    constant_along_x_1 = [column for column, values in
                          enumerate(phi_image(p1, p1.evaluate(fixed_x_2, p1_default_params),
                                              record).T)
                          if np.ptp(values) == 0.0]
    if phi_name == "lu":
        assert constant_along_x_2 == [] and constant_along_x_1 == []
    else:
        assert constant_along_x_2 == [3] and constant_along_x_1 == [1]


# the extreme points of a finite sample survive the filter under ls and cw
@pytest.mark.parametrize("phi_name", phi_names)
@pytest.mark.parametrize("seed", gate_seeds)
def test_the_extreme_points_of_a_finite_sample_survive_the_filter(phi_name, seed):
    # the second half of the mechanism, on the very sample random search filters,
    # so the statement is about the pipeline and not about an invented set. under
    # phi_ls and phi_cw both extreme points are non-dominated by construction and
    # the assertion is that they are; under phi_lu neither column is a width
    # column and the same two points are in fact dominated at every gate seed,
    # which is the contrast that makes this a measurement rather than a
    # restatement, CONTEXT.md section 11's evidence rule.
    sample = sample_decision_space(p1.bounds(), gate_n_evals, seed)
    image = phi_image(p1, p1.evaluate(sample, p1_default_params),
                      phi_registry[phi_name])
    kept = set(non_dominated_indices(image).tolist())
    smallest_x_1, smallest_x_2 = extreme_point_indices(sample)
    survives = (smallest_x_1 in kept, smallest_x_2 in kept)
    if phi_name == "lu":
        assert survives == (False, False), (
            "phi_lu has no width column, so nothing forces these two points into "
            "the front; at seed {} they are {}".format(seed, survives))
    else:
        assert survives == (True, True), (
            "phi_{} carries a width column, so both extreme points must survive "
            "the filter; at seed {} they are {}".format(phi_name, seed, survives))


# the extreme point that survives can sit far outside the derived set
@pytest.mark.parametrize("phi_name", ("ls", "cw"))
def test_the_surviving_extreme_point_can_lie_outside_the_derived_region(phi_name):
    # what the two halves together cost the forward direction. the surviving
    # point's other coordinate ranges over the whole box, [-1/2, 3/2], while b1
    # section 2.4 puts X_cw inside [0, 1]^2 and X_ls inside [0, 4/3]^2, so the
    # forward distance carries whatever overhang that draw produced. the
    # assertion is the mechanism and not a number: over the five gate seeds at
    # least one surviving extreme point lies outside the derived region, and the
    # message carries every overhang so the size of the floor can be read.
    region = region_sample(phi_name, 4000, tolerance_seed)
    overhangs = []
    for seed in gate_seeds:
        draw = sample_decision_space(p1.bounds(), gate_n_evals, seed)
        for index in extreme_point_indices(draw):
            point = draw[index:index + 1]
            if not in_region(phi_name, point)[0]:
                overhangs.append((seed, tuple(np.round(point[0], 5)),
                                  directed_hausdorff(point, region)))
    assert overhangs, (
        "no surviving extreme point of any gate seed lies outside X_{}, so this "
        "test no longer observes the floor it is about".format(phi_name))
    assert max(row[2] for row in overhangs) > 0.0, overhangs


# the two points c3 raised as s-13 are dominated by points of the derived set
def test_the_points_raised_as_s13_are_dominated_by_the_derived_set():
    # c3 recorded these two as dominated by nothing in the derived set, but that
    # was read off b2's 1000-point sample, which reaches x_1 = 1 only in the
    # limit, docs/b1_phi_efficient_sets.md section 2.4. read against b1's closed
    # form instead the answer is different and s-13 dissolves: X_cw is
    # [0, 1]^2 minus the open segment {(x_1, 0) : 0 < x_1 <= 1}, so
    # (0.999, 0.0001) is in it, and under phi_cw's columns (c_1, r_1, c_2, r_2)
    # it is strictly better than both points in all four.
    witness = np.array([[0.999, 0.0001]])
    assert np.all(in_region("cw", witness))
    assert witness[0, 1] > 0.0
    record = phi_registry["cw"]
    witness_image = phi_image(p1, p1.evaluate(witness, p1_default_params), record)
    points_image = phi_image(p1, p1.evaluate(s13_points, p1_default_params), record)
    assert dominated_count(points_image, witness_image) == len(s13_points)
    assert np.all(witness_image[0] < points_image)


# the published anchor x = 0 is found on p0, which is all p0 is asked
@pytest.mark.slow
@pytest.mark.parametrize("solver_id", solver_ids)
@pytest.mark.parametrize("phi_name", phi_names)
@pytest.mark.parametrize("seed", gate_seeds)
def test_the_published_anchor_is_found_on_p0(solver_id, phi_name, seed):
    # b1 section 7.4: p0 is a smoke test and not a fixture. under phi_lu and
    # phi_ls its optimal set is the whole decision box, so a front containing a
    # point near the origin is a weak statement; under phi_cw the optimal set is
    # the anchor alone and the statement is the whole answer. the check is the
    # same in all three cases and the reading is not, and
    # docs/c3_validation.md carries the distinction.
    run = one_run(solver_id, p0, None, phi_name, seed)
    distance = float(np.min(np.abs(run.decision_vectors[:, 0] - p0_anchor[0])))
    assert distance <= anchor_tolerance, (
        "{} on p0 under phi_{}, seed {}: nearest point to the anchor x = 0 is at "
        "{:.5f}, tolerance {:.5f}, k_solver {}"
        .format(solver_id, phi_name, seed, distance, anchor_tolerance,
                len(run.decision_vectors)))


# the phi_lu non-dominated set has no point outside the phi_ls one, on p1
@pytest.mark.slow
@pytest.mark.parametrize("solver_id", solver_ids)
@pytest.mark.parametrize("phi_name", phi_names)
@pytest.mark.parametrize("seed", gate_seeds)
def test_no_lu_point_falls_outside_the_ls_set_on_p1(solver_id, phi_name, seed):
    run = one_run(solver_id, p1, p1_default_params, phi_name, seed)
    outside, in_lu, in_ls = lu_points_outside_ls(p1, run.decision_vectors,
                                                 p1_default_params)
    assert outside == 0, (
        "{} on p1 under phi_{}, seed {}: {} of {} phi_lu points are absent from "
        "the phi_ls set of {}. this is numerical noise in the pipeline and never "
        "a result about phi".format(solver_id, phi_name, seed, outside, in_lu, in_ls))


# the same count on p0, the other tier 0 problem the diagnostic covers
@pytest.mark.slow
@pytest.mark.parametrize("solver_id", solver_ids)
@pytest.mark.parametrize("phi_name", phi_names)
@pytest.mark.parametrize("seed", gate_seeds)
def test_no_lu_point_falls_outside_the_ls_set_on_p0(solver_id, phi_name, seed):
    run = one_run(solver_id, p0, None, phi_name, seed)
    outside, in_lu, in_ls = lu_points_outside_ls(p0, run.decision_vectors, None)
    assert outside == 0, (
        "{} on p0 under phi_{}, seed {}: {} of {} phi_lu points are absent from "
        "the phi_ls set of {}. this is numerical noise in the pipeline and never "
        "a result about phi".format(solver_id, phi_name, seed, outside, in_lu, in_ls))


# the two settings of include_singular_segments really are two different sets
@pytest.mark.parametrize("phi_name", phi_names)
def test_the_singular_flag_changes_the_reference_set_except_under_lu(phi_name):
    # CONTEXT.md section 11's evidence rule: a test that runs both settings of a
    # flag has to demonstrate the two settings differ, or it is asserting a
    # property it cannot observe. b1 section 2.3 finds no singular ray at all for
    # phi_lu, so there the flag is a no-op and that is what is asserted; for
    # phi_ls and phi_cw the sets differ and the count of differing rows is the
    # evidence that the gate's two settings are two measurements.
    without, _ = efficient_set(p1, phi_name, reference_points, False)
    with_segment, _ = efficient_set(p1, phi_name, reference_points, True)
    assert len(without) == len(with_segment) == reference_points
    differing = int(np.count_nonzero(np.any(without != with_segment, axis=1)))
    if phi_name == "lu":
        assert differing == 0
    else:
        assert differing >= int(np.ceil(np.sqrt(reference_points)))


# the tolerance is the sum of two measured floors and neither term is negligible
@pytest.mark.parametrize("phi_name", phi_names)
def test_the_tolerance_is_the_sum_of_two_measured_floors(phi_name):
    # the derivation asserted rather than described: both terms are positive,
    # both are measured on the region and not on the weight sample, and the
    # tolerance is a fraction of the box side rather than a number of its order.
    # the box is [-0.5, 1.5]^2, of side 2, docs/a1_uncertainty_model.md. r-17
    # records that reading h_design as the largest of the twenty draws rather than
    # their mean raises the tolerance by about a factor of 1.5; the reverse
    # direction, which is the only one the gate asserts, passes under both.
    h_reference, h_design, tolerance = tolerance_terms(phi_name)
    assert h_reference > 0.0 and h_design > 0.0
    assert tolerance == h_reference + h_design
    assert h_reference < h_design
    assert tolerance < 0.25 * 2.0


# every point of the region sample the floors are measured on lies in the region
@pytest.mark.parametrize("phi_name", phi_names)
def test_the_region_sample_lies_in_the_derived_region(phi_name):
    sample = region_sample(phi_name, 2000, tolerance_seed)
    assert len(sample) == 2000
    assert np.all(in_region(phi_name, sample))
    points, _ = efficient_set(p1, phi_name, 500, False)
    assert np.all(in_region(phi_name, points))


# the directed hausdorff distance is a maximum of minima and is not symmetric
def test_directed_hausdorff_is_a_maximum_and_is_directional():
    # the property the whole gate rests on, checked on a case where the two
    # directions are known and different: b contains a, so every point of a is at
    # distance zero from b, while the extra point of b is at distance 3 from a.
    set_a = np.array([[0.0, 0.0], [1.0, 0.0]])
    set_b = np.array([[0.0, 0.0], [1.0, 0.0], [4.0, 0.0]])
    assert directed_hausdorff(set_a, set_b) == 0.0
    assert directed_hausdorff(set_b, set_a) == 3.0
    assert directed_hausdorff(set_a, set_a, block=1) == 0.0


# the dominance counter is directional and counts rows and not pairs
def test_the_dominance_counter_is_directional_and_counts_rows():
    # the measure the gate reports as its quality number, checked on a case where
    # the answer is known: the second row is beaten by the first in both columns
    # and the third ties it, so one row of three is dominated in one direction and
    # none in the other.
    beaten = np.array([[0.0, 0.0], [1.0, 1.0], [0.0, 0.0]])
    beating = np.array([[0.0, 0.0]])
    assert dominated_count(beaten, beating) == 1
    assert dominated_count(beating, beaten) == 0
    assert dominated_count(beaten, beaten, block=1) == 1
