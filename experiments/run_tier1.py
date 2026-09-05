# e2: the tier 1 run. all three solvers, all three phi, zdt1_interval and
# dtlz2_interval, the full imprecision sweep, over the seed list, at the gate
# budget with one convergence check per problem at four times it. it writes the
# raw results, the tables, the figures and the record. it interprets nothing;
# e3 does that, CONTEXT.md section 10 e3.
#
# what e2 is, in the arc's terms. e1 calibrated the instrument on p1, the one
# problem whose phi-efficient sets are known exactly, and measured what the
# instrument costs. e2 applies that instrument to two standard benchmarks where
# no exact answer exists, at thirty and at twelve variables.
# docs/plan_after_meeting.md sections a1 and a2.
#
# what e2 inherits from e1, and it is the single most useful thing the
# calibration bought. on p1 the exact coverage of X_lu in X_cw is 0.394710 and
# the measurement returns more than that at both budgets, converging toward the
# derived value as the budget rises. **the instrument overstates agreement**, so
# a measured coverage is an upper bound on true sharing and therefore a lower
# bound on how far the two orders differ. every number in this run's tables is
# read subject to that, and the record states it with e1's own figures read back
# out of results/tier0/, never typed.
#
# there is no table 1 here and that is a statement and not an omission. table 1
# is exact and p1 only, docs/plan_after_meeting.md section b3; zdt1 and dtlz2
# have no closed-form phi-efficient set, so they have no exact row, and the
# record says so rather than leaving a reader to wonder where it went.
#
# delta is zero and that is the headline everywhere, d-08. the pair statistics
# are computed on random search's one filtered sample through
# src/metrics_decision.py's compare_phi_on_one_sample, so the three sets are
# index sets over one array: two decision vectors are bitwise identical or they
# are different points, and the coverage at delta zero is exactly the shared
# count over the count. a positive delta is reported only where two different
# samples are compared and it is structurally required, which is the same-phi
# seed-to-seed noise floor and the population solvers' own pairs; there delta
# zero returns zero by construction and the comparison could not be made at all.
# it matters more here than at tier 0: distances in a box grow like the square
# root of the dimension, so a box fraction fixed on p1's 2-box is a different
# quantity on a 30-box, and the sweep in the record measures that rather than
# leaving it as a caveat.
#
# coverage leads and any overlap is named, d-09. coverage is directional and
# unambiguous and is the same functional in the exact and the measured tables.
# d2's compute_overlap is the two covered counts over the two cardinalities,
# which is dice; jaccard is the shared measure over the union, and the two are
# different functionals. jaccard is computed here **from** dice and d2 is not
# changed: with s the shared count and the two cardinalities n_a and n_b, dice
# is 2s / (n_a + n_b) and jaccard is s / (n_a + n_b - s), so jaccard is
# dice / (2 - dice) identically, and at delta zero on one filtered sample both
# reduce to counts of one index set against another.
#
# the noise floor, without which a benchmark row cannot be read at all. for each
# problem and phi, the same coverage statistic between two seeds of the *same*
# phi, so no order difference can appear in it. a cross-phi number that does not
# exceed it is not evidence, and at thirty variables that is a live possibility
# rather than a formality. docs/plan_after_meeting.md section b1.
#
# the solver comparison is separate and is never mixed into the pair numbers.
# in nsga-ii and mopso phi drives the search as well as the ordering, so a
# difference between two of their runs is a difference of orders and of
# trajectories at once. they are run under every phi and reported in their own
# table, with the rank-1 size against the population size beside them:
# CONTEXT.md section 10 e2 requires it because a configuration in which rank 1
# fills the survivor slots is one where dominance-based selection has no
# pressure and the front is a spread result and not a convergence result. the
# series is read out of the algorithm's state after every generation through a
# pymoo Callback, exactly as c3-d read it, docs/c3_validation.md section 5.1;
# **pymoo is not modified and src/runners.py is not modified**: the callback is
# attached to the algorithm c2's own factory built, it writes nothing back, and
# tests/test_run_tier1.py asserts the front comes back bit-identical with it
# installed.
#
# no igd on tier 1, and the reason is b2's scope. src/reference_fronts.py
# derives a reference front for p1 alone, docs/b1_phi_efficient_sets.md section
# 7.4, so there is no reference object to average over here and the metric is
# not computed rather than computed against something invented. the objective
# block therefore carries hypervolume and spread, with the reference size zero.
#
# the objective-space metrics are computed at the common cardinality of each
# comparison, r-16 and CONTEXT.md section 10 d1. all three move with the number
# of rows a solver returns by more than the differences between solvers, random
# search returning between seventeen and several thousand rows here against
# nsga-ii's hundred, and the cardinality is taken over every front of one
# comparison across phi and not per phi, since the smallest is systematically
# phi_lu's. e1 reported at full cardinality with the cardinality printed, which
# is r-16's other rule, so the two objective blocks are not compared and the
# record says so. the decision-space metrics are on the full untruncated sets,
# which is where CONTEXT.md section 10 d1 puts the restriction.
#
# the two registered measurements, and only one of them is computed. m-2, the
# overhang, is computed here on both benchmarks at twenty seeds, which is the
# seed count PROGRESS.md x-02 registers. **m-1 is withdrawn as an instrument at
# x-01's outcome line and is not computed, not revived and not re-thresholded.**
# which columns m-2 is computed on is decided by the free sets, and the free
# sets are measured rather than asserted, by resampling each decision variable
# in turn.
#
# m-2 is measured against two structures and the file names both. the structure
# x-01 registered is {x_2 = ... = x_29 = 0} for zdt1 and {x_3 = ... = x_11 = 1/2}
# for dtlz2, and it is the headline because a registered measurement is not
# edited after registration. a5-b then moved which decision variable each
# objective's half-width reads, so docs/plan_after_meeting.md section f3's own
# domination argument, re-run on a5-b's forms, pins one variable fewer on zdt1
# and two fewer on dtlz2: raising x_i strictly raises the centre columns and
# leaves the width columns alone only while x_i drives no width. the second
# structure is that argument's answer and it is reported beside the first, not
# instead of it.
#
# the raw results are written before any metric is computed, so a metric can be
# recomputed without re-running a solver, and the manifest names every array.
#
# no number is typed into this file that is not a run parameter. the imprecision
# levels are src/problems_tier1.py's own, the budget and the seed list are the
# ones the gate ran at, and every number in docs/e2_tier1_results.md is read back
# out of a file this script wrote.

import argparse
import csv
import sys
import time
from pathlib import Path

import numpy as np
from pymoo.core.callback import Callback
from pymoo.util.nds.non_dominated_sorting import NonDominatedSorting

repository_root = Path(__file__).resolve().parent.parent
source_directory = repository_root / "src"
if str(source_directory) not in sys.path:
    sys.path.insert(0, str(source_directory))

from metrics_decision import (check_status, compare_phi_on_one_sample,
                              compute_coverage, compute_hausdorff, compute_overlap,
                              cross_evaluate, pair_note, pair_status, phi_pairs)
from metrics_objective import (common_cardinality, compute_hv, compute_spread,
                               derive_reference_point, nadir_margin_rule,
                               truncate_to_common_cardinality)
from phi_transforms import phi_registry
from problems_tier1 import default_params, epsilon_levels, problem_registry
from random_search import SearchResult, phi_image, sample_decision_space
from reference_fronts import farthest_point_mode
from reporting import (PlottedFront, PlottedSet, decision_block, format_value,
                       objective_block, plot_decision_sets, plot_fronts,
                       read_metrics_table, save_metrics_table,
                       summarize_across_seeds)
from runners import make_mopso, make_nsga2, run_solver

# the record's two rendering helpers, taken from e1's script rather than
# written again, so that the tier 0 record and the tier 1 record format a
# number the same way and g1 can lift a table from either without
# reconciling two conventions. nothing else of e1 is imported and no metric
# is.
from run_tier0 import markdown_table

# the three phi in the lu, ls, cw order of examples 2.2, 2.3 and 2.4 of [1],
# which is the order every table and every loop in the project uses.
phi_names = ("lu", "ls", "cw")

# the three solvers of slide 17, and the two of them that carry a population.
# random search is the control and is in the grid on the same terms as the other
# two, CONTEXT.md section 10 c1.
solver_names = ("random_search", "nsga2", "mopso")
population_solvers = ("nsga2", "mopso")

# the two tier 1 benchmarks, src/problems_tier1.py's own names
problem_names = ("zdt1_interval", "dtlz2_interval")

# the seed list, the population and the gate budget, all three the ones
# tests/test_validation.py ran the gate at and the ones e1 ran on. a run at a
# budget the gate did not pass would be a run behind an untested gate.
run_seeds = (11, 12, 13, 14, 15)
gate_pop_size = 100
gate_n_gen = 50
gate_budget = gate_pop_size * gate_n_gen

# the convergence check, one per problem: the grid re-measured at four times the
# budget at one imprecision level, which is the multiple c3 reported its budget
# trend at and the scope r-15 priced. the level is src/problems_tier1.py's own
# default and is not chosen here.
convergence_multiple = 4
convergence_eps = float(default_params["eps"])

# the seed count PROGRESS.md x-02 registers for the overhang. it is larger than
# the run's seed list and is spent on this measurement alone, m-2 needing a
# uniform sample and an argmin and no filter at all.
overhang_seeds = tuple(range(11, 31))

# delta, stated as a fraction of the box diameter and never as an absolute
# number, docs/plan_after_meeting.md section b1. it is the value e1 ran at and it
# is not the headline: d-08 makes delta zero the headline everywhere and this
# fraction is what the rows that need a positive delta are computed at.
delta_box_fraction = 0.05

# the fractions the coverage and overlap statistics are also computed at. on tier
# 1 this is the measurement behind d-08's dimension argument and not only a
# caveat: a box fraction on a 30-box is not the quantity it is on a 2-box.
delta_sweep_fractions = (0.0, 0.01, 0.02, delta_box_fraction, 0.10, 0.20)

# the fractions the same-phi noise floor is swept at, which is a wider range than
# the pairs are. the floor compares two independent uniform samples, which share
# no point at all, so it is zero at delta zero by construction and, at thirty and
# at twelve variables, a delta-ball of one twentieth of the box diameter is a
# vanishing fraction of the box. the sweep is what turns "the floor is zero" into
# a statement about how large a ball has to be before it stops being zero, which
# is d-08's dimension argument measured rather than argued.
floor_sweep_fractions = (delta_box_fraction, 0.10, 0.20, 0.30, 0.50)

# zero, and it is not a limiting case. the three sets of one random-search
# comparison are three index sets over one array, so two decision vectors are the
# same point bitwise or they are two points and no tolerance decides it.
zero_delta = 0.0

# the reference-front settings a row states even where there is no reference
# front. b2 derives one for p1 alone, so no igd is computed here and every
# objective-space row carries a reference size of zero; the mode is written
# because d3 requires the field and the row must say which one the configuration
# would have used.
reference_sampling_mode = farthest_point_mode
no_singular_setting = False

# the hypervolume reference point rule. the margin rule and not the strict nadir,
# CONTEXT.md section 10 e1: the strict nadir puts the point on the extremes of the
# rows it is derived from, and a row on an extreme is then clipped.
hv_rule = nadir_margin_rule

# how the free sets and the effective column counts are measured: one resampling
# of each decision variable over a sample of this size at this seed. both are
# structural properties and not reporting parameters, so they take a fixed seed
# and are not summarised over seeds.
dependence_points = 512
dependence_seed = 20260905

# the seed the objective-space truncation of r-16 draws at. it is a reporting
# parameter of the truncation and not of the run, so it is fixed here and stated.
truncation_seed = 20260906

# the registered measurement, named as PROGRESS.md x-01 names it. m-1 is
# withdrawn at x-01's outcome line and appears nowhere in this file.
overhang_name = "m-2_overhang"

# the two structures m-2 is measured against, named in the file it is written to
registered_structure = "registered_x01"
a5b_structure = "a5b_domination_argument"
overhang_structures = (registered_structure, a5b_structure)


# the projections of a stated efficient structure onto each decision variable
def pinned_projections(n_vars, pinned, value):
    # a variable the structure pins carries the degenerate interval [value,
    # value] and every other variable carries the whole of the unit box, which is
    # both benchmarks' box. m-2 is a distance to this and to nothing else.
    return tuple((value, value) if index in pinned else (0.0, 1.0)
                 for index in range(n_vars))


# zdt1's pinned variables under each structure, as indices into the decision vector
def zdt1_pinned(structure):
    # x-01 registers {x_2 = ... = x_29 = 0}, which is indices 1 to 28. a5-b gave
    # the second objective the half-width driver x_29, so section f3's argument,
    # that raising x_i strictly raises the centre columns and moves nothing else,
    # now reaches x_28 and stops: indices 1 to 27.
    last = 28 if structure == registered_structure else 27
    return set(range(1, last + 1))


# dtlz2's pinned variables under each structure, as indices into the decision vector
def dtlz2_pinned(structure):
    # x-01 registers {x_3 = ... = x_11 = 1/2}, which is indices 2 to 10. a5-b gave
    # the second and third objectives the drivers x_11 and x_10, so the same
    # argument now reaches x_9 and stops: indices 2 to 8.
    last = 10 if structure == registered_structure else 8
    return set(range(2, last + 1))


# the per-variable projection of one problem's efficient structure, both versions
def efficient_projections(problem_name, structure):
    if problem_name == "zdt1_interval":
        return pinned_projections(problem_registry[problem_name].n_vars,
                                  zdt1_pinned(structure), 0.0)
    return pinned_projections(problem_registry[problem_name].n_vars,
                              dtlz2_pinned(structure), 0.5)


# the column pairs an objective-space figure projects onto, for a 2m-column image
def figure_col_pairs(n_cols):
    # the 2m columns come in the order (Lambda_1^T f, B_1^T f, Lambda_2^T f, ...),
    # so the even indices are the first image coordinate of each objective and the
    # odd ones the second. consecutive pairs within each parity keep every panel
    # inside one image coordinate of the transform and never plot a first
    # coordinate against a second.
    firsts = tuple(range(0, n_cols, 2))
    seconds = tuple(range(1, n_cols, 2))
    return (tuple(zip(firsts, firsts[1:])) + tuple(zip(seconds, seconds[1:])))


# the run parameters of one invocation, so that no function reads a global budget
def run_settings(seeds, budgets, pop_size, structure_seeds):
    return {"seeds": tuple(int(seed) for seed in seeds),
            "budgets": tuple(int(budget) for budget in budgets),
            "pop_size": int(pop_size),
            "overhang_seeds": tuple(int(seed) for seed in structure_seeds)}


# the parameters one problem is evaluated at, which is its imprecision level
def problem_parameters(eps):
    return {"eps": float(eps)}


# the budgets one imprecision level is run at, the convergence check being one level
def budgets_for(eps, budgets):
    return tuple(budgets) if eps == convergence_eps else (int(budgets[0]),)


# the euclidean diameter of a problem's decision box, the scale delta is stated in
def box_diameter(problem):
    lower, upper = problem.bounds()
    return float(np.sqrt(np.sum(np.square(np.asarray(upper) - np.asarray(lower)))))


# the absolute delta of one problem, the stated fraction of its box diameter
def problem_delta(problem, fraction=delta_box_fraction):
    return float(fraction) * box_diameter(problem)


# jaccard from dice, the two overlap conventions d-09 keeps apart
def jaccard_from_dice(dice):
    # with s the shared count and n_a, n_b the two cardinalities, d2's
    # compute_overlap is 2s / (n_a + n_b) and the shared fraction of the union is
    # s / (n_a + n_b - s), so the second is the first over two minus the first,
    # identically. d2 is not changed and its meaning is not reinterpreted.
    return float(dice) / (2.0 - float(dice))


# writes one csv of dictionaries, every cell formatted as d3 formats a table cell
def write_table(path, fieldnames, rows):
    # format_value is src/reporting.py's, so a float written here round-trips to
    # the same double a metrics table would have written and two runs of this
    # script produce the same bytes.
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle, lineterminator="\n")
        writer.writerow(list(fieldnames))
        for row in rows:
            writer.writerow([format_value(field, row[field]) for field in fieldnames])
    return path


# the rows of a csv this script wrote, read back as a list of dictionaries
def read_table(path):
    with open(path, newline="", encoding="utf-8") as handle:
        return [dict(record) for record in csv.DictReader(handle)]


# a progress line, this being a script and not library code
def announce(message):
    print("[e2] {}".format(message), flush=True)


# one run's rank-1 series, held in an object the algorithm's deep copy shares
class RankRecorder:

    # starts an empty series, with no previous generation's survivors yet
    def __init__(self):
        self.rows = []
        self.previous = None

    # returns itself to a deep copy, so the series survives pymoo copying the run
    def __deepcopy__(self, memo):
        # pymoo's minimize deep-copies the algorithm before running it,
        # optimize.py, so a recorder copied with it would be filled and then
        # discarded. this is the one line that makes the callback's output
        # reachable, and it copies nothing of the algorithm.
        return self


# reads the rank-1 size out of the algorithm's state after every generation
class RankCallback(Callback):

    # keeps the recorder the series is written into
    def __init__(self, recorder):
        super().__init__()
        self.recorder = recorder

    # records one generation's candidate set, its first front and its survivors
    def _update(self, algorithm):
        # pymoo calls this at the end of _post_advance, after survival has run,
        # core/algorithm.py. the candidate set nsga-ii sorted is the previous
        # generation's survivors stacked on this generation's offspring, which
        # pymoo does not keep, so it is rebuilt here and sorted with pymoo's own
        # NonDominatedSorting; nothing is written back to the algorithm.
        survivors = algorithm.pop.get("F")
        offspring = getattr(algorithm, "off", None)
        candidates = candidate_set(self.recorder.previous, offspring, survivors)
        self.recorder.rows.append(rank_series_row(algorithm, candidates, survivors))
        self.recorder.previous = survivors


# the candidate set one generation chose its survivors out of
def candidate_set(previous, offspring, survivors):
    # the first generation has no previous survivors and pymoo runs survival on
    # the initial population alone, so the candidate set there is that population.
    if previous is None or offspring is None:
        return np.asarray(survivors, dtype=float)
    return np.concatenate([np.asarray(previous, dtype=float),
                           np.asarray(offspring.get("F"), dtype=float)])


# one generation's row of the rank-1 series
def rank_series_row(algorithm, candidates, survivors):
    sorting = NonDominatedSorting()
    first = sorting.do(candidates, only_non_dominated_front=True)
    return {"generation": int(algorithm.n_iter), "n_candidates": len(candidates),
            "n_pop": len(survivors), "rank_1_of_candidates": int(len(first)),
            "n_fronts": int(len(sorting.do(candidates))),
            "survivors_from_rank_1": survivors_from_rank_1(algorithm)}


# how many survivors pymoo's own sort placed in rank 1, where it records a rank
def survivors_from_rank_1(algorithm):
    # RankAndCrowding._do writes a rank onto every individual it sorts, so
    # nsga-ii's survivors carry one and the number is read off the state. mopso's
    # survival is crowding distance over an archive and writes no rank, so the
    # field is absent there and is written empty rather than as a zero.
    if "rank" not in algorithm.pop[0].data:
        return None
    return int(np.count_nonzero(algorithm.pop.get("rank") == 0))


# the pymoo algorithm one solver name builds, with a rank-1 callback attached
def make_recording_algorithm(solver, pop_size, n_evals, recorder):
    # the algorithm is src/runners.py's own and nothing about it is changed: the
    # population size, the archive size and the seeded truncation are c2's. only
    # pymoo's own callback attribute is set, which is how the series is read
    # without touching that module or pymoo.
    factory = {"nsga2": make_nsga2, "mopso": make_mopso}[solver]
    algorithm = factory(pop_size, n_evals)
    algorithm.callback = RankCallback(recorder)
    return algorithm


# an algorithm factory that hands every seed of one configuration its own recorder
def recording_factory(solver, recorders):
    # src/runners.py's run_solver takes the factory as an argument and calls it
    # once per seed, so the recorders come back in the seed order and are zipped
    # with the results.
    def factory(pop_size, n_evals):
        recorder = RankRecorder()
        recorders.append(recorder)
        return make_recording_algorithm(solver, pop_size, n_evals, recorder)
    return factory


# the fronts of one filtered sample, one per phi, from a single evaluation
def sample_fronts(problem, params, sample):
    # the isolation of src/random_search.py's filter_one_sample_under_every_phi is
    # carried through to the fronts: the problem is evaluated once and each phi's
    # front is that evaluation's image at that phi's index set, so the three
    # fronts of one seed differ only through the order. this is the same object
    # run_random_search would return at the same seed.
    pairs = problem.evaluate(sample.decision_vectors, params)
    fronts = {}
    for name in phi_names:
        keep = sample.indices[name]
        image = phi_image(problem, pairs, phi_registry[name])
        fronts[name] = (image[keep], sample.decision_vectors[keep])
    return fronts


# random search on one problem at one budget, as one comparison and three results
def random_search_runs(problem, params, budget, seeds, delta):
    comparisons, results = [], {name: [] for name in phi_names}
    for seed in seeds:
        comparison = compare_phi_on_one_sample(problem, params, budget, seed, delta)
        comparisons.append(comparison)
        for name, (front, vectors) in sample_fronts(problem, params,
                                                    comparison.sample).items():
            results[name].append(SearchResult(seed=seed, n_evals=int(budget),
                                              front=front, decision_vectors=vectors))
    return comparisons, results


# one population solver under one phi at one budget, with its rank-1 series
def population_runs(problem, phi_name, params, solver, budget, settings):
    # the budget is spent in evaluations and the generation count follows from it,
    # so both solvers spend exactly the stated budget, src/runners.py.
    pop_size = settings["pop_size"]
    n_gen = int(budget) // int(pop_size)
    recorders = []
    results = run_solver(problem, phi_name, params, recording_factory(solver,
                                                                     recorders),
                         n_gen, pop_size, settings["seeds"])
    return results, recorders


# every run of one problem at one imprecision level and one budget
def execute_cell(problem, eps, budget, settings, runs, comparisons, rank_rows):
    params = problem_parameters(eps)
    found, results = random_search_runs(problem, params, budget, settings["seeds"],
                                        problem_delta(problem))
    comparisons[(problem.name, eps, budget)] = found
    for phi_name in phi_names:
        runs[(problem.name, "random_search", phi_name, eps, budget)] = results[phi_name]
        for solver in population_solvers:
            solved, recorders = population_runs(problem, phi_name, params, solver,
                                                budget, settings)
            runs[(problem.name, solver, phi_name, eps, budget)] = solved
            rank_rows.extend(rank_rows_of(recorders, solved, problem.name, solver,
                                          phi_name, eps, budget))


# every run of the grid, with the comparisons and the rank-1 series beside them
def execute_grid(settings):
    runs, comparisons, rank_rows = {}, {}, []
    for problem_name in problem_names:
        problem = problem_registry[problem_name]
        for eps in epsilon_levels:
            for budget in budgets_for(eps, settings["budgets"]):
                announce("running {} at eps {} and budget {}".format(problem_name,
                                                                    eps, budget))
                execute_cell(problem, eps, budget, settings, runs, comparisons,
                             rank_rows)
    return runs, comparisons, rank_rows


# every generation of every seed of one configuration's rank-1 series, as rows
def rank_rows_of(recorders, results, problem_name, solver, phi_name, eps, budget):
    rows = []
    for recorder, result in zip(recorders, results):
        for entry in recorder.rows:
            rows.append(dict(entry, problem=problem_name, solver=solver,
                             phi=phi_name, eps=float(eps), n_evals=int(budget),
                             seed=int(result.seed)))
    return rows


# the summary of one configuration's rank-1 series over its seeds
def rank_summary_rows(rows):
    summary = []
    keys = sorted({rank_group_key(row) for row in rows})
    for key in keys:
        group = [row for row in rows if rank_group_key(row) == key]
        summary.append(rank_summary_row(key, group))
    return summary


# the key one configuration's rank-1 series is summarised over its seeds by
def rank_group_key(row):
    return (row["problem"], row["solver"], row["phi"], row["eps"], row["n_evals"])


# one configuration's rank-1 summary, with what makes its front a spread result
def rank_summary_row(key, group):
    problem_name, solver, phi_name, eps, budget = key
    seeds = sorted({row["seed"] for row in group})
    per_seed = [seed_rank_summary([row for row in group if row["seed"] == seed])
                for seed in seeds]
    row = {"problem": problem_name, "solver": solver, "phi": phi_name, "eps": eps,
           "n_evals": budget, "n_seeds": len(seeds),
           "pop_size": int(np.median([item["pop_size"] for item in per_seed])),
           "n_generations": int(np.median([item["n_generations"]
                                           for item in per_seed])),
           "saturates_in_every_seed": all(item["saturated"] for item in per_seed),
           "first_saturated_generation": median_or_none(
               [item["first_saturated"] for item in per_seed])}
    row.update(summarize_across_seeds([item["rank_1_late_median"]
                                       for item in per_seed]))
    return row


# the median of the values that are present, or nothing where none is
def median_or_none(values):
    present = [value for value in values if value is not None]
    return float(np.median(present)) if present else None


# one seed's rank-1 series reduced to when it saturated and where it sat after
def seed_rank_summary(rows):
    # saturation is rank 1 holding at least the population size of the candidate
    # set, which is when dominance stops deciding anything: every survivor is then
    # chosen out of one front on crowding distance alone,
    # docs/c3_validation.md section 5.1. the late median is over the second half
    # of the run, which is the window c3-d reported its own medians over.
    ordered = sorted(rows, key=lambda row: row["generation"])
    pop_size = int(np.median([row["n_pop"] for row in ordered]))
    saturated = [row for row in ordered if row["rank_1_of_candidates"] >= pop_size]
    late = ordered[len(ordered) // 2:]
    return {"pop_size": pop_size, "n_generations": len(ordered),
            "saturated": bool(saturated),
            "first_saturated": saturated[0]["generation"] if saturated else None,
            "rank_1_late_median": float(np.median([row["rank_1_of_candidates"]
                                                   for row in late]))}


# the file one configuration's raw arrays are written to
def raw_path(root, key):
    problem_name, solver, phi_name, eps, budget = key
    return root / "raw" / "{}_{}_{}_{}_{}.npz".format(problem_name, solver,
                                                      phi_name, repr(float(eps)),
                                                      budget)


# writes one configuration's fronts and decision vectors, one array pair per seed
def save_raw_runs(root, key, results):
    path = raw_path(root, key)
    path.parent.mkdir(parents=True, exist_ok=True)
    arrays = {"seeds": np.array([result.seed for result in results], dtype=int),
              "n_evals": np.array([result.n_evals for result in results], dtype=int)}
    for result in results:
        arrays["front_{}".format(result.seed)] = result.front
        arrays["decision_vectors_{}".format(result.seed)] = result.decision_vectors
    np.savez_compressed(path, **arrays)
    return path


# reads one configuration back from disk as the results that were written
def load_raw_runs(path):
    with np.load(path) as arrays:
        return [SearchResult(
            seed=int(seed), n_evals=int(n_evals),
            front=arrays["front_{}".format(seed)],
            decision_vectors=arrays["decision_vectors_{}".format(seed)])
            for seed, n_evals in zip(arrays["seeds"], arrays["n_evals"])]


# writes every configuration's raw arrays and the manifest that names them
def save_raw(root, runs):
    rows = []
    for key in sorted(runs):
        path = save_raw_runs(root, key, runs[key])
        problem_name, solver, phi_name, eps, budget = key
        for result in runs[key]:
            rows.append({"problem": problem_name, "solver": solver, "phi": phi_name,
                         "eps": float(eps), "n_evals": result.n_evals,
                         "seed": result.seed,
                         "cardinality": int(len(result.front)),
                         "n_columns": int(result.front.shape[1]),
                         "file": path.relative_to(root).as_posix()})
    write_table(root / "raw" / "manifest.csv",
                ("problem", "solver", "phi", "eps", "n_evals", "seed",
                 "cardinality", "n_columns", "file"), rows)
    return rows


# the 2m image columns of one problem under one phi, at a stated sample
def image_columns(problem, params, phi_name, x):
    return phi_image(problem, problem.evaluate(x, params), phi_registry[phi_name])


# a uniform sample of one problem's box at a stated size and seed
def dependence_sample(problem, n_points, seed):
    lower, upper = problem.bounds()
    generator = np.random.default_rng(seed)
    return generator.uniform(lower, upper, size=(int(n_points), problem.n_vars))


# which decision variables each image column depends on, measured by resampling
def column_dependence(problem, params, phi_name, n_points, seed):
    # a structural property measured rather than asserted. one variable at a time
    # is redrawn uniformly over its own range and a column that does not move at
    # any of the sample's points does not depend on that variable. the free set
    # F_k of docs/plan_after_meeting.md section f2 is the complement of what this
    # returns, and a column that is constant is reported separately, since the
    # protected-minimiser mechanism needs a member that minimises the column
    # strictly and a constant column has none.
    lower, upper = problem.bounds()
    generator = np.random.default_rng(seed)
    x = generator.uniform(lower, upper, size=(int(n_points), problem.n_vars))
    base = image_columns(problem, params, phi_name, x)
    depends = np.zeros((base.shape[1], problem.n_vars), dtype=bool)
    for variable in range(problem.n_vars):
        moved = np.array(x, copy=True)
        moved[:, variable] = generator.uniform(lower[variable], upper[variable],
                                               size=int(n_points))
        depends[:, variable] = np.any(image_columns(problem, params, phi_name, moved)
                                      != base, axis=0)
    constant = np.all(base == base[0], axis=0)
    return depends, constant


# how many of the 2m image columns are distinct functions, on a stated sample
def effective_columns(problem, params, phi_name, n_points, seed):
    # r-20 and a5-b, checked at the run rather than inherited. a5's shared width
    # made two of zdt1's four image columns one function under examples 2.3 and
    # 2.4 and three of dtlz2's six, and the duplication was phi-dependent, so the
    # headline pair compared transformed problems of different dimension. two
    # columns equal at every point of this sample are counted once.
    columns = image_columns(problem, params, phi_name,
                            dependence_sample(problem, n_points, seed))
    distinct = []
    for index in range(columns.shape[1]):
        if not any(np.array_equal(columns[:, index], columns[:, other])
                   for other in distinct):
            distinct.append(index)
    return len(distinct)


# the free set and the effective column count of every problem, phi and level
def structure_rows(settings):
    rows = []
    for problem_name in problem_names:
        problem = problem_registry[problem_name]
        for eps in epsilon_levels:
            params = problem_parameters(eps)
            for phi_name in phi_names:
                rows.extend(structure_rows_of(problem, params, phi_name, eps))
    return rows


# the free-set rows of one problem, phi and imprecision level
def structure_rows_of(problem, params, phi_name, eps):
    depends, constant = column_dependence(problem, params, phi_name,
                                          dependence_points, dependence_seed)
    distinct = effective_columns(problem, params, phi_name, dependence_points,
                                 dependence_seed)
    rows = []
    for column in range(depends.shape[0]):
        free = [str(index) for index in range(problem.n_vars)
                if not depends[column, index]]
        rows.append({"problem": problem.name, "phi": phi_name, "eps": float(eps),
                     "column": column, "n_columns": int(depends.shape[0]),
                     "effective_columns": distinct,
                     "depends_on": " ".join(str(index)
                                            for index in range(problem.n_vars)
                                            if depends[column, index]),
                     "free_set": " ".join(free), "free_set_size": len(free),
                     "constant_column": bool(constant[column])})
    return rows


# the distance from a point to a box, zero inside it
def interval_distance(values, intervals):
    gaps = [max(low - value, 0.0, value - high)
            for value, (low, high) in zip(values, intervals)]
    return float(np.sqrt(np.sum(np.square(gaps)))) if gaps else 0.0


# m-2 for one column: how far the protected member lies outside a stated structure
def column_overhang(vectors, columns, column, free, intervals):
    # x-01's measurement: the argmin of the column in that seed's sample is the
    # protected member, and the overhang is the distance from its free
    # coordinates to the projection of the efficient structure onto them. where
    # the free set is empty the distance is over no coordinates and is zero by
    # construction, which is the case the prediction calls absent.
    protected = int(np.argmin(columns[:, column]))
    point = vectors[protected]
    return interval_distance([point[index] for index in free],
                             [intervals[index] for index in free]), protected


# m-2 over one problem, phi and imprecision level, per seed and per structure
def overhang_rows_of(problem, phi_name, eps, free_rows, settings, budget):
    params = problem_parameters(eps)
    rows = []
    for seed in settings["overhang_seeds"]:
        vectors = sample_decision_space(problem.bounds(), budget, seed)
        columns = image_columns(problem, params, phi_name, vectors)
        for column in range(columns.shape[1]):
            free, constant = free_set_of(free_rows, problem.name, phi_name, eps,
                                         column)
            rows.extend(overhang_rows_for_column(problem, phi_name, eps, seed,
                                                 vectors, columns, column, free,
                                                 constant, budget))
    return rows


# m-2 for one column at one seed, against both structures, with the undefined marked
def overhang_rows_for_column(problem, phi_name, eps, seed, vectors, columns, column,
                             free, constant, budget):
    shared = {"problem": problem.name, "phi": phi_name, "eps": float(eps),
              "column": column, "free_set_size": len(free),
              "constant_column": constant, "n_evals": int(budget),
              "seed": int(seed), "measurement": overhang_name}
    if constant:
        # a constant column has no member minimising it strictly, so the
        # mechanism's hypothesis is unavailable and the measurement is not
        # defined. it is marked and not filled with a zero.
        return [dict(shared, structure=structure, value=None, defined=False,
                     protected_index=None) for structure in overhang_structures]
    rows = []
    for structure in overhang_structures:
        intervals = efficient_projections(problem.name, structure)
        value, protected = column_overhang(vectors, columns, column, free, intervals)
        rows.append(dict(shared, structure=structure, value=value, defined=True,
                         protected_index=protected))
    return rows


# the free set of one column, read back out of the free-set rows
def free_set_of(rows, problem_name, phi_name, eps, column):
    for row in rows:
        if (row["problem"], row["phi"], float(row["eps"]), int(row["column"])) == (
                problem_name, phi_name, float(eps), column):
            return ([int(index) for index in row["free_set"].split()],
                    as_bool(row["constant_column"]))
    raise KeyError("no free set recorded for {} {} eps {} column {}"
                   .format(problem_name, phi_name, eps, column))


# a flag as a boolean, whether it arrives as one or as the text a csv holds
def as_bool(value):
    return value == "True" if isinstance(value, str) else bool(value)


# every per-seed value of m-2, over every problem, phi and imprecision level
def overhang_rows(free_rows, settings):
    rows = []
    budget = settings["budgets"][0]
    for problem_name in problem_names:
        problem = problem_registry[problem_name]
        for eps in epsilon_levels:
            for phi_name in phi_names:
                rows.extend(overhang_rows_of(problem, phi_name, eps, free_rows,
                                             settings, budget))
    return rows


# the median and the mean of m-2 over the seeds, per column and per structure
def overhang_summary_rows(rows):
    summary = []
    keys = sorted({overhang_group_key(row) for row in rows})
    for key in keys:
        group = [row for row in rows if overhang_group_key(row) == key]
        summary.append(overhang_summary_row(key, group))
    return summary


# the key one m-2 measurement is summarised over its seeds by
def overhang_group_key(row):
    return (row["problem"], row["phi"], row["eps"], row["column"], row["structure"],
            row["n_evals"])


# one summarised m-2 row, with the mean and its spread beside the median
def overhang_summary_row(key, group):
    problem_name, phi_name, eps, column, structure, budget = key
    values = [row["value"] for row in group if row["defined"]]
    entry = {"problem": problem_name, "phi": phi_name, "eps": eps, "column": column,
             "structure": structure, "n_evals": budget,
             "measurement": overhang_name,
             "free_set_size": group[0]["free_set_size"],
             "constant_column": group[0]["constant_column"],
             "defined": bool(values)}
    entry.update(summarize_across_seeds(values) if values else
                 {"n_seeds": 0, "median": None, "q1": None, "q3": None,
                  "iqr": None})
    # the mean and the spread of the mean as well as the median, because x-01
    # states its refuting measurement on the mean over seeds and a median cannot
    # be read against a derived constant.
    entry.update(mean_and_spread(values))
    return entry


# the mean over seeds and the standard error a prediction is read against
def mean_and_spread(values):
    if not values:
        return {"mean": None, "standard_deviation": None, "standard_error": None}
    array = np.asarray(values, dtype=float)
    deviation = float(np.std(array, ddof=1)) if array.size > 1 else 0.0
    return {"mean": float(np.mean(array)), "standard_deviation": deviation,
            "standard_error": deviation / float(np.sqrt(array.size))}


# the eight decision-space metrics of one pair, as a mapping from metric to value
def pair_values(pair):
    return {"hausdorff_a_to_b": pair.hausdorff.a_to_b,
            "hausdorff_b_to_a": pair.hausdorff.b_to_a,
            "hausdorff_symmetric": pair.hausdorff.symmetric,
            "coverage_a_in_b": pair.coverage_a_in_b,
            "coverage_b_in_a": pair.coverage_b_in_a, "overlap": pair.overlap,
            "overlap_jaccard": jaccard_from_dice(pair.overlap),
            "cross_a_under_b": pair.cross_a_under_b,
            "cross_b_under_a": pair.cross_b_under_a}


# one per-seed decision-space row, in the shape every later summary reads
def decision_row(problem_name, solver, phi_a, phi_b, metric, eps, budget, seed,
                 n_a, n_b, delta, violations, value):
    return {"problem": problem_name, "solver": solver, "phi_a": phi_a,
            "phi_b": phi_b, "status": pair_status(phi_a, phi_b), "metric": metric,
            "eps": float(eps), "n_evals": int(budget), "seed": int(seed),
            "cardinality_a": int(n_a), "cardinality_b": int(n_b),
            "delta": float(delta), "containment_violations": violations,
            "value": value}


# every per-seed decision-space value of the random-search pair comparisons
def decision_rows_by_seed(comparisons, problem_name, eps, budget):
    rows = []
    for comparison in comparisons:
        for pair in comparison.pairs:
            for metric, value in pair_values(pair).items():
                rows.append(decision_row(problem_name, "random_search", pair.phi_a,
                                         pair.phi_b, metric, eps, budget,
                                         comparison.seed, pair.n_a, pair.n_b,
                                         comparison.delta,
                                         pair.containment_violations, value))
    return rows


# the four delta-dependent pair statistics of one comparison at a stated delta
def pair_rows_at_delta(comparison, problem_name, eps, budget, delta):
    # the same statistics compare_phi_on_one_sample returns, recomputed at a
    # second delta from the sets it already filtered. the metrics that do not move
    # with delta, the three hausdorff distances and the two cross evaluations, are
    # not repeated: they are one number per pair and are already in the rows the
    # comparison produced.
    rows = []
    vectors = comparison.sample.decision_vectors
    for phi_a, phi_b in phi_pairs:
        set_a = vectors[comparison.sample.indices[phi_a]]
        set_b = vectors[comparison.sample.indices[phi_b]]
        for metric, value in delta_values(set_a, set_b, delta).items():
            rows.append(decision_row(problem_name, "random_search", phi_a, phi_b,
                                     metric, eps, budget, comparison.seed,
                                     len(set_a), len(set_b), delta, None, value))
    return rows


# the four statistics that move with delta, between two decision sets
def delta_values(set_a, set_b, delta):
    dice = compute_overlap(set_a, set_b, delta)
    return {"coverage_a_in_b": compute_coverage(set_a, set_b, delta),
            "coverage_b_in_a": compute_coverage(set_b, set_a, delta),
            "overlap": dice, "overlap_jaccard": jaccard_from_dice(dice)}


# the same coverage statistic between two seeds of one phi, the instrument's floor
def noise_floor_rows(comparisons, problem_name, eps, budget):
    # docs/plan_after_meeting.md section b1: a cross-phi number that does not
    # exceed the seed-to-seed disagreement of the same phi is not evidence of
    # anything. each seed is paired with the next one cyclically, so there is one
    # value per seed. it is computed at the positive delta and not at zero,
    # because two independent uniform samples share no point at all and the floor
    # at delta zero is zero by construction, d-08.
    rows = []
    for phi_name in phi_names:
        sets = [comparison.sample.decision_vectors[comparison.sample.indices[phi_name]]
                for comparison in comparisons]
        for index, comparison in enumerate(comparisons):
            other = (index + 1) % len(comparisons)
            for metric, value in delta_values(sets[index], sets[other],
                                              comparison.delta).items():
                rows.append(decision_row(problem_name, "random_search_noise_floor",
                                         phi_name, phi_name, metric, eps, budget,
                                         comparison.seed, len(sets[index]),
                                         len(sets[other]), comparison.delta, None,
                                         value))
    return rows


# the pair statistics of one population solver's own output, per seed
def solver_pair_rows(runs, problem, params, solver, eps, budget, delta):
    rows = []
    for phi_a, phi_b in phi_pairs:
        runs_a = runs[(problem.name, solver, phi_a, eps, budget)]
        runs_b = runs[(problem.name, solver, phi_b, eps, budget)]
        for result_a, result_b in zip(runs_a, runs_b):
            values = solver_pair_values(result_a, result_b, phi_a, phi_b, problem,
                                        params, delta)
            for metric, value in values.items():
                rows.append(decision_row(problem.name, solver, phi_a, phi_b, metric,
                                         eps, budget, result_a.seed,
                                         len(result_a.decision_vectors),
                                         len(result_b.decision_vectors), delta,
                                         None, value))
    return rows


# the metrics between two decision sets a solver returned under two phi
def solver_pair_values(result_a, result_b, phi_a, phi_b, problem, params, delta):
    set_a, set_b = result_a.decision_vectors, result_b.decision_vectors
    hausdorff = compute_hausdorff(set_a, set_b)
    values = {"hausdorff_a_to_b": hausdorff.a_to_b,
              "hausdorff_b_to_a": hausdorff.b_to_a,
              "hausdorff_symmetric": hausdorff.symmetric,
              "cross_a_under_b": cross_evaluate(set_a, phi_b, problem, params),
              "cross_b_under_a": cross_evaluate(set_b, phi_a, problem, params)}
    values.update(delta_values(set_a, set_b, delta))
    return values


# the note a measured pair row carries, naming the solver, the delta and the pair
def measured_note(phi_a, phi_b, solver, delta, fraction, containment_note):
    scale = ("delta is zero, so the row is the shared count over the count, with "
             "no tolerance in it at all; the three sets are index sets over one "
             "array, so two vectors are the same point bitwise or they are two "
             "points" if delta == zero_delta else
             "delta is {} of the box diameter, the box_scale column"
             .format(repr(float(fraction))))
    return ("{}; {}; overlap is dice, the two covered counts over the two "
            "cardinalities, and the jaccard value of the same pair is in "
            "overlap_conventions.csv; containment_violations is the largest count "
            "over the seeds; {}".format(solver_note(solver), scale,
                                        containment_note))


# what the solver a row was measured on lets the row be read as
def solver_note(solver):
    if solver == "random_search":
        return ("measured on random search's one filtered sample, so the two sets "
                "differ only through the order")
    if solver == "random_search_noise_floor":
        return ("noise floor and not a pair: one phi against itself at two seeds, "
                "so no order difference can appear in it and a cross-phi number "
                "that does not exceed it is not evidence. it is labelled a check "
                "because d3 reserves the finding label for the row carrying the "
                "sensitivity signal and this row carries none")
    return ("measured on {}'s own output, where phi drives the search as well as "
            "the ordering, so this is a question about how the solver behaves "
            "under each order and never a pair number of the study".format(solver))


# the key a decision-space row is summarised over its seeds by
def decision_group_key(row):
    return (row["problem"], row["solver"], row["phi_a"], row["phi_b"],
            row["metric"], row["eps"], row["n_evals"], row["delta"])


# the decision-space rows of a table, one per group, summarised over the seeds
def decision_table_rows(by_seed, fraction=delta_box_fraction):
    rows = []
    for key in sorted({decision_group_key(row) for row in by_seed}):
        group = [row for row in by_seed if decision_group_key(row) == key]
        rows.append(decision_table_row(key, group, fraction))
    return rows


# one summarised decision-space row, in d3's decision block
def decision_table_row(key, group, fraction):
    problem_name, solver, phi_a, phi_b, metric, _, budget, delta = key
    row = {"problem": problem_name, "phi_a": phi_a, "phi_b": phi_b,
           "status": group[0]["status"], "metric": metric, "n_evals": budget,
           "cardinality_a": int(np.median([item["cardinality_a"]
                                           for item in group])),
           "cardinality_b": int(np.median([item["cardinality_b"]
                                           for item in group])),
           "delta": delta,
           "box_scale": box_diameter(problem_registry[problem_name]),
           "containment_violations": violation_count(group),
           "note": measured_note(phi_a, phi_b, solver, delta, fraction,
                                 pair_note(phi_a, phi_b))}
    row.update(summarize_across_seeds([item["value"] for item in group]))
    return row


# the largest containment violation count over a group's seeds, absent where none
def violation_count(group):
    counts = [item["containment_violations"] for item in group
              if item["containment_violations"] is not None]
    return int(max(counts)) if counts else None


# the rows d3's decision block admits, which is its own metric list and no others
def block_admissible(rows):
    # jaccard is computed alongside dice and d2 is not changed, d-09, so the
    # metric is not one of d3's eight and does not go into a metrics table. it is
    # written to overlap_conventions.csv instead, beside the dice value of the
    # same pair, and the table's note points there.
    return [row for row in rows if row["metric"] != "overlap_jaccard"]


# the two overlap conventions of one pair side by side, per problem and level
def overlap_convention_rows(by_seed):
    rows = []
    keys = sorted({overlap_key(row) for row in by_seed
                   if row["metric"] == "overlap"})
    for key in keys:
        dice = [row["value"] for row in by_seed
                if overlap_key(row) == key and row["metric"] == "overlap"]
        jaccard = [row["value"] for row in by_seed
                   if overlap_key(row) == key and row["metric"] == "overlap_jaccard"]
        rows.append(overlap_convention_row(key, dice, jaccard))
    return rows


# the key one pair's two overlap conventions are grouped by
def overlap_key(row):
    return (row["problem"], row["solver"], row["phi_a"], row["phi_b"], row["eps"],
            row["n_evals"], row["delta"])


# one row of the overlap file, dice and jaccard of the same pair and the same seeds
def overlap_convention_row(key, dice, jaccard):
    problem_name, solver, phi_a, phi_b, eps, budget, delta = key
    dice_summary = summarize_across_seeds(dice)
    jaccard_summary = summarize_across_seeds(jaccard)
    return {"problem": problem_name, "solver": solver, "phi_a": phi_a,
            "phi_b": phi_b, "status": pair_status(phi_a, phi_b), "eps": eps,
            "n_evals": budget, "delta": delta,
            "box_scale": box_diameter(problem_registry[problem_name]),
            "n_seeds": dice_summary["n_seeds"],
            "dice_median": dice_summary["median"], "dice_q1": dice_summary["q1"],
            "dice_q3": dice_summary["q3"],
            "jaccard_median": jaccard_summary["median"],
            "jaccard_q1": jaccard_summary["q1"],
            "jaccard_q3": jaccard_summary["q3"]}


# the same-phi seed-to-seed coverage over a range of delta, from the raw sets
def floor_sweep_rows(runs, settings):
    # the floor of docs/plan_after_meeting.md section b1, swept. it needs only the
    # per-phi decision sets random search returned, which the raw arrays hold, so
    # it is computed from them and can be rebuilt without re-running a solver. it
    # is computed at the reported budget alone, the cost being quadratic in the
    # set size.
    rows, budget = [], settings["budgets"][0]
    for problem_name in problem_names:
        problem = problem_registry[problem_name]
        for eps in epsilon_levels:
            for phi_name in phi_names:
                key = (problem_name, "random_search", phi_name, eps, budget)
                rows.extend(floor_sweep_of(runs[key], problem, phi_name, eps,
                                           budget))
    return rows


# one configuration's floor, each seed against the next one cyclically
def floor_sweep_of(results, problem, phi_name, eps, budget):
    rows = []
    diameter = box_diameter(problem)
    sets = [result.decision_vectors for result in results]
    for index, result in enumerate(results):
        other = (index + 1) % len(results)
        for fraction in floor_sweep_fractions:
            rows.extend(floor_sweep_values(sets[index], sets[other], problem,
                                           phi_name, eps, budget, result.seed,
                                           fraction, fraction * diameter))
    return rows


# the two directed coverages of one same-phi seed pair at one delta
def floor_sweep_values(set_a, set_b, problem, phi_name, eps, budget, seed,
                       fraction, delta):
    values = {"coverage_a_in_b": compute_coverage(set_a, set_b, delta),
              "coverage_b_in_a": compute_coverage(set_b, set_a, delta)}
    return [{"problem": problem.name, "phi": phi_name, "metric": metric,
             "eps": float(eps), "n_evals": int(budget), "seed": int(seed),
             "delta_box_fraction": fraction, "delta": delta,
             "box_scale": box_diameter(problem), "cardinality_a": len(set_a),
             "cardinality_b": len(set_b), "value": value}
            for metric, value in values.items()]


# the coverage and overlap statistics at a range of delta, as raw rows
def delta_sweep_rows(comparisons, problem, eps, budget):
    # delta is a reporting parameter and the numbers move with it, and on a 30-box
    # a box fraction is not the quantity it is on p1's 2-box, d-08. the movement
    # is measured here rather than left as a caveat, at the reported budget only.
    rows = []
    diameter = box_diameter(problem)
    for comparison in comparisons:
        indices = comparison.sample.indices
        vectors = comparison.sample.decision_vectors
        for phi_a, phi_b in phi_pairs:
            set_a, set_b = vectors[indices[phi_a]], vectors[indices[phi_b]]
            for fraction in delta_sweep_fractions:
                rows.extend(delta_sweep_values(set_a, set_b, fraction * diameter,
                                               fraction, comparison, problem,
                                               phi_a, phi_b, eps, budget))
    return rows


# the delta-dependent statistics of one pair at one delta, as raw rows
def delta_sweep_values(set_a, set_b, delta, fraction, comparison, problem, phi_a,
                       phi_b, eps, budget):
    return [{"problem": problem.name, "phi_a": phi_a, "phi_b": phi_b,
             "status": pair_status(phi_a, phi_b), "metric": metric,
             "eps": float(eps), "n_evals": int(budget),
             "seed": int(comparison.seed), "delta_box_fraction": fraction,
             "delta": delta, "box_scale": box_diameter(problem),
             "cardinality_a": len(set_a), "cardinality_b": len(set_b),
             "value": value}
            for metric, value in delta_values(set_a, set_b, delta).items()]


# every configuration key of one problem and imprecision level, at every budget
def cell_keys(problem_name, eps, settings):
    return [(problem_name, solver, phi_name, eps, budget)
            for solver in solver_names for phi_name in phi_names
            for budget in budgets_for(eps, settings["budgets"])]


# the cardinality every front of one comparison is cut to, r-16
def comparison_cardinality(runs, problem_name, eps, settings):
    # taken over every front of the comparison, across solvers, phi, seeds and
    # both budgets and not per phi: the smallest is systematically phi_lu's, so a
    # per-phi minimum would put a phi-dependent selection inside the comparison.
    # CONTEXT.md section 10 d1. pooling the budgets as well is what makes the
    # convergence check a comparison of two numbers of one measurement.
    fronts = [result.front for key in cell_keys(problem_name, eps, settings)
              for result in runs[key]]
    return common_cardinality(fronts)


# one run's front cut to the comparison's cardinality at the stated seed
def truncated_front(result, n_keep):
    return truncate_to_common_cardinality(result.front, n_keep, truncation_seed)


# the truncated fronts of one problem, phi and level, pooled over the whole grid
def pooled_truncated(runs, problem_name, phi_name, eps, settings, n_keep):
    return [truncated_front(result, n_keep)
            for solver in solver_names
            for budget in budgets_for(eps, settings["budgets"])
            for result in runs[(problem_name, solver, phi_name, eps, budget)]]


# the one hypervolume reference point of a problem, phi and level, or why there is none
def hypervolume_point(rows):
    # derived from every row it will be scored against, so that one point serves
    # the whole comparison. where a pooled column has zero range the margin rule
    # adds nothing to the nadir there, no point can strictly dominate the rows and
    # every box has zero thickness, so no hypervolume is scored and the reason is
    # returned instead. at eps = 0 every half-width is zero, so the second image
    # coordinate of examples 2.3 and 2.4 is identically zero and that is the case.
    pooled = np.concatenate(list(rows), axis=0)
    point = derive_reference_point(pooled, hv_rule)
    ranges = np.max(pooled, axis=0) - np.min(pooled, axis=0)
    if np.all(ranges > 0.0):
        return point, True, ""
    degenerate = [int(index) for index in np.flatnonzero(ranges <= 0.0)]
    return point, False, (
        "no hypervolume is scored: image columns {} are constant over every row, so "
        "the margin rule adds no thickness there, the point cannot strictly "
        "dominate any row and every row's box has zero volume. the point is "
        "recorded because the other metrics' rows state the one the configuration "
        "would have been scored against".format(degenerate))


# raises unless the reference point strictly dominates every row it will score
def require_dominating_point(point, front, label):
    # CONTEXT.md section 10 e1, v-59: moocore clips at the reference point instead
    # of refusing, so a row beyond the point contributes nothing and the number
    # still comes back looking like a hypervolume. a front the point does not
    # dominate is refused here rather than scored.
    if not bool(np.all(np.asarray(front, dtype=float) < np.asarray(point))):
        raise ValueError(
            "the hypervolume reference point {} does not dominate every row of {}; "
            "moocore would clip the rows beyond it and return a number, so this "
            "front is refused and not scored".format(np.asarray(point).tolist(),
                                                     label))


# the objective-space values of one configuration, per seed and per metric
def objective_rows_by_seed(results, key, point, scorable, n_keep):
    problem_name, solver, phi_name, eps, budget = key
    rows = []
    for result in results:
        front = truncated_front(result, n_keep)
        shared = {"problem": problem_name, "phi": phi_name, "solver": solver,
                  "eps": float(eps), "n_evals": int(budget),
                  "seed": int(result.seed), "cardinality": int(len(front)),
                  "full_cardinality": int(len(result.front)), "reference_size": 0,
                  "include_singular_segments": no_singular_setting}
        rows.append(dict(shared, metric="spread", value=compute_spread(front)))
        if scorable:
            require_dominating_point(point.point, front,
                                     "{} {} {} at eps {} budget {} seed {}"
                                     .format(problem_name, phi_name, solver, eps,
                                             budget, result.seed))
            rows.append(dict(shared, metric="hypervolume",
                             value=compute_hv(front, point.point)))
    return rows


# every per-seed objective-space value, with the points the hypervolumes used
def objective_values(runs, settings):
    rows, points, cardinalities = [], {}, {}
    for problem_name in problem_names:
        for eps in epsilon_levels:
            n_keep = comparison_cardinality(runs, problem_name, eps, settings)
            cardinalities[(problem_name, eps)] = n_keep
            for phi_name in phi_names:
                point, scorable, reason = hypervolume_point(
                    pooled_truncated(runs, problem_name, phi_name, eps, settings,
                                     n_keep))
                points[(problem_name, phi_name, eps)] = (point, scorable, reason)
                for key in phi_cell_keys(problem_name, phi_name, eps, settings):
                    rows.extend(objective_rows_by_seed(runs[key], key, point,
                                                       scorable, n_keep))
    return rows, points, cardinalities


# every configuration key of one problem, phi and level, at every budget
def phi_cell_keys(problem_name, phi_name, eps, settings):
    return [(problem_name, solver, phi_name, eps, budget)
            for solver in solver_names
            for budget in budgets_for(eps, settings["budgets"])]


# the key an objective-space row is summarised over its seeds by
def objective_group_key(row):
    return (row["problem"], row["phi"], row["solver"], row["metric"], row["eps"],
            row["n_evals"])


# the objective-space rows of the solver table, summarised over the seeds
def objective_table_rows(by_seed, points):
    rows = []
    for key in sorted({objective_group_key(row) for row in by_seed}, key=repr):
        group = [row for row in by_seed if objective_group_key(row) == key]
        rows.append(objective_table_row(key, group, points))
    return rows


# one summarised objective-space row, in d3's objective block
def objective_table_row(key, group, points):
    problem_name, phi_name, solver, metric, eps, budget = key
    point = points[(problem_name, phi_name, eps)][0]
    row = {"problem": problem_name, "phi": phi_name, "solver": solver,
           "metric": metric, "n_evals": budget,
           "cardinality": int(np.median([item["cardinality"] for item in group])),
           "reference_size": 0, "sampling_mode": reference_sampling_mode,
           "include_singular_segments": no_singular_setting,
           "hv_reference_rule": hv_rule, "hv_reference_point": point.point}
    row.update(summarize_across_seeds([item["value"] for item in group]))
    return row


# the figure directory of one run
def figure_root(root):
    path = root / "figures"
    path.mkdir(parents=True, exist_ok=True)
    return path


# one solver's runs under one phi pooled over the seeds, as one plotted series
def pooled_front(runs, key, label):
    results = runs[key]
    return PlottedFront(label=label, n_seeds=len(results),
                        n_evals=results[0].n_evals,
                        rows=np.concatenate([result.front for result in results]))


# the three solvers' fronts in one phi's image, one figure per problem, phi and level
def front_figures(root, runs, eps, budget):
    paths = []
    for problem_name in problem_names:
        for phi_name in phi_names:
            fronts = [pooled_front(runs, (problem_name, solver, phi_name, eps,
                                          budget), solver)
                      for solver in solver_names]
            path = figure_root(root) / "fronts_{}_{}_{}_{}.png".format(
                problem_name, phi_name, repr(float(eps)), budget)
            plot_fronts(fronts, figure_col_pairs(fronts[0].rows.shape[1]),
                        "{} under phi_{} at eps {}, the three solvers".format(
                            problem_name, phi_name, eps), path)
            paths.append(path)
    return paths


# one solver's decision sets under the three phi, at one seed, largest first
def single_seed_sets(runs, problem_name, solver, eps, budget, seed_index=0):
    # one seed and not the five pooled, and the three ordered by decreasing size.
    # both are about what the figure shows rather than about what was measured:
    # five seeds pooled put tens of thousands of points on the plane, and drawing
    # the sets in the registry's order hides the smallest under the largest,
    # ND_lu sitting inside ND_ls. the legend carries the seed count and the
    # cardinality of each series, so nothing is concealed by either choice.
    sets = []
    for phi_name in phi_names:
        result = runs[(problem_name, solver, phi_name, eps, budget)][seed_index]
        sets.append(PlottedSet(
            label="phi_{}".format(phi_name), problem_name=problem_name,
            phi_name=phi_name, n_seeds=1, n_evals=result.n_evals,
            points=result.decision_vectors))
    return sorted(sets, key=lambda item: -len(item.points))


# the recovered decision sets projected onto the first two variables, per solver
def decision_figures(root, runs, eps, budget):
    # the projection is onto x_1 and x_2 and is stated in the title: there is no
    # derived region to draw behind them, b2 deriving one for p1 alone, and thirty
    # variables do not fit on a plane. the figure is what the sets look like in
    # two of them and it is not a picture of the sets.
    paths = []
    for problem_name in problem_names:
        for solver in solver_names:
            path = figure_root(root) / "decision_sets_{}_{}_{}_{}.png".format(
                problem_name, solver, repr(float(eps)), budget)
            plot_decision_sets(
                single_seed_sets(runs, problem_name, solver, eps, budget),
                "{}, {}, eps {}, the three phi projected on x_1 and x_2".format(
                    problem_name, solver, eps), path)
            paths.append(path)
    return paths


# every figure of the run, each one carrying its own budget and seed count
def all_figures(root, runs, settings):
    paths = []
    for eps in epsilon_levels:
        for budget in budgets_for(eps, settings["budgets"]):
            paths.extend(front_figures(root, runs, eps, budget))
            paths.extend(decision_figures(root, runs, eps, budget))
    return paths


# one key of the summary file, with the file a reader should check it against
def summary_row(key, value, source):
    return {"key": key, "value": value, "source": source}


# the run parameters, one key each, as the record reads them back
def summary_parameters(settings):
    return [summary_row("seeds", " ".join(str(seed) for seed in settings["seeds"]),
                        "run parameter"),
            summary_row("n_seeds", len(settings["seeds"]), "run parameter"),
            summary_row("overhang_seeds",
                        " ".join(str(seed) for seed in settings["overhang_seeds"]),
                        "run parameter, the count PROGRESS.md x-02 registers"),
            summary_row("n_overhang_seeds", len(settings["overhang_seeds"]),
                        "run parameter"),
            summary_row("budgets", " ".join(str(budget)
                                            for budget in settings["budgets"]),
                        "run parameter"),
            summary_row("convergence_eps", convergence_eps,
                        "src/problems_tier1.py's default_params"),
            summary_row("epsilon_levels", " ".join(repr(float(level))
                                                   for level in epsilon_levels),
                        "src/problems_tier1.py's epsilon_levels"),
            summary_row("pop_size", settings["pop_size"], "run parameter"),
            summary_row("delta_box_fraction", delta_box_fraction, "run parameter"),
            summary_row("hv_reference_rule", hv_rule, "run parameter"),
            summary_row("truncation_seed", truncation_seed, "run parameter"),
            summary_row("dependence_points", dependence_points, "run parameter"),
            summary_row("dependence_seed", dependence_seed, "run parameter")]


# each problem's box scale, the absolute delta on it and its column count
def summary_scales():
    rows = []
    for problem_name in problem_names:
        problem = problem_registry[problem_name]
        rows.append(summary_row("box_scale_{}".format(problem_name),
                                box_diameter(problem), "the problem's bounds"))
        rows.append(summary_row("delta_{}".format(problem_name),
                                problem_delta(problem), "run parameter"))
        rows.append(summary_row("n_vars_{}".format(problem_name), problem.n_vars,
                                "the problem"))
        rows.append(summary_row("n_image_columns_{}".format(problem_name),
                                2 * problem.n_obj, "the problem, 2m under any phi"))
    return rows


# the tables written, the truncation cardinalities and the hypervolume verdicts
def summary_artefacts(tables, points, cardinalities):
    rows = [summary_row("table_{}".format(name), path.name, "written here")
            for name, path in sorted(tables.items())]
    for key in sorted(cardinalities):
        rows.append(summary_row("common_cardinality_{}_{}".format(key[0],
                                                                  repr(key[1])),
                                cardinalities[key],
                                "r-16, the smallest front of the comparison"))
    for key in sorted(points):
        _, scorable, reason = points[key]
        rows.append(summary_row("hypervolume_scored_{}_{}_{}".format(
            key[0], key[1], repr(key[2])), scorable,
            reason or "the point dominates every scored row"))
    return rows


# the run parameters and counts, as the keys the record reads its prose from
def summary_rows(settings, runs, tables, points, cardinalities, elapsed):
    counts = [summary_row("n_configurations", len(runs), "the run grid"),
              summary_row("n_runs", sum(len(value) for value in runs.values()),
                          "the run grid"),
              summary_row("wall_seconds", elapsed, "the run grid")]
    return (summary_parameters(settings) + counts + summary_scales()
            + summary_artefacts(tables, points, cardinalities))


# the rows of a written table's decision block, filtered to a stated budget
def decision_rows_at(path, budget=None):
    rows = read_metrics_table(path)[decision_block]
    return [row for row in rows if budget is None or row["n_evals"] == budget]


# what e2 inherits from e1: p1's exact pair statistic against the measured one
def inherited_error_rows(tier0_root):
    # the calibration's own number, read back out of e1's artefacts and never
    # typed. p1 is the only problem where the gap between a derived quantity and
    # the same quantity measured on recovered sets can be computed at all, and
    # every row of this run's tables is read subject to it.
    error_path = Path(tier0_root) / "instrument_error_p1.csv"
    measured_path = Path(tier0_root) / "table_2_measured.csv"
    if not error_path.is_file() or not measured_path.is_file():
        return []
    exact = {(row["phi_a"], row["phi_b"], row["metric"]): float(row["exact"])
             for row in read_table(error_path)
             if float(row["delta"]) == zero_delta}
    measured = [row for row in decision_rows_at(measured_path)
                if row["problem"] == "p1" and row["delta"] == zero_delta
                and (row["phi_a"], row["phi_b"], row["metric"]) in exact]
    return sorted((inherited_row(row, exact) for row in measured), key=repr)


# one inherited row, the exact value beside the measurement and their two gaps
def inherited_row(row, exact):
    value = exact[(row["phi_a"], row["phi_b"], row["metric"])]
    error = row["median"] - value
    return {"problem": row["problem"], "phi_a": row["phi_a"],
            "phi_b": row["phi_b"], "status": row["status"],
            "metric": row["metric"], "n_evals": row["n_evals"],
            "delta": row["delta"], "exact": value,
            "measured_median": row["median"], "error": error,
            "relative_error": error / value if value else None}


# the record's opening: what was run, read back out of summary.csv
def record_opening(summary, tables):
    lines = ["# e2: the tier 1 run", "",
             "generated by experiments/run_tier1.py. every number below is read "
             "back out of a file that script wrote, and the file and the key are "
             "named beside it; nothing here is typed. re-running the script from "
             "the same seeds regenerates this document with the same numbers.", "",
             "## 1. what was run", "",
             "from results/tier1/summary.csv, one key per row:", ""]
    lines.extend(markdown_table(("key", "value", "source"), summary))
    lines.extend(["", "the run grid is every solver of slide 17 under every phi of "
                  "[1] on both tier 1 benchmarks at every imprecision level of "
                  "src/problems_tier1.py, at each seed. eps = 0 is the crisp "
                  "baseline and is labelled one: every half-width is zero there, "
                  "so half of the 2m transformed objectives are constant and the "
                  "three phi coincide with each other and with the crisp order. "
                  "the convergence check is the grid repeated at four times the "
                  "budget at one level, the default of src/problems_tier1.py, with "
                  "the hypervolume reference point derived once across both.", ""])
    lines.extend(["the tables written, all through src/reporting.py's "
                  "save_metrics_table:", ""])
    lines.extend(["- results/tier1/{}".format(path.name)
                  for path in sorted(tables.values(), key=lambda item: item.name)])
    return lines + [""]


# why there is no table 1 here, which is a statement and not an omission
def record_no_exact_table():
    return ["", "## 2. there is no table 1 on tier 1, and that is the statement", "",
            "table 1 of docs/plan_after_meeting.md section b3 is exact and p1 only. "
            "it is the lebesgue measure of the closed-form phi-efficient regions "
            "docs/b1_phi_efficient_sets.md section 2.4 derives, and zdt1 and dtlz2 "
            "have no such derivation: b1 covers p0 and p1, and "
            "src/reference_fronts.py refuses any other problem by name. so the "
            "benchmarks have no exact row, no reference front and therefore no "
            "igd, and every pair number below is a measurement with nothing "
            "derived to be checked against. what stands in for that is section 3, "
            "which is the gap between the derived and the measured value of the "
            "same quantity on the one problem where both exist.", ""]


# the record's inherited instrument error, e1's number read back out of e1's files
def record_inherited(rows, budgets):
    lines = ["## 3. what e2 inherits from e1: the instrument overstates agreement",
             "", "p1's exact pair statistics against the same quantities measured "
             "on recovered sets, at delta zero, at both budgets. source: "
             "results/tier0/instrument_error_p1.csv and "
             "results/tier0/table_2_measured.csv, both written by "
             "experiments/run_tier0.py; nothing here is recomputed and nothing is "
             "typed.", ""]
    if not rows:
        return lines + ["e1's artefacts were not found under results/tier0, so this "
                        "section is empty and the run's own numbers below are to "
                        "be read without it.", ""]
    lines.extend(markdown_table(("phi_a", "phi_b", "status", "metric", "n_evals",
                                 "exact", "measured_median", "error",
                                 "relative_error"), rows))
    lines.extend(["", "**the measurement is larger than the derivation on every "
                  "row where the derivation is not already one, and it falls "
                  "toward the derivation as the budget rises.** so a measured "
                  "coverage is an upper bound on true sharing and therefore a "
                  "lower bound on the difference between two orders. stated for "
                  "the tables below: **the benchmark numbers understate how much "
                  "the orders differ**, by a factor measured once, on the "
                  "calibration problem, at the budgets in the table above. e2 "
                  "records the direction and the size and does not interpret "
                  "either.", "",
                  "the budgets the benchmarks are run at are {}.".format(
                      " and ".join(str(budget) for budget in budgets)), ""])
    return lines


# the record's measured pair tables, one section per imprecision level
def record_measured(tables, budgets):
    lines = ["## 4. table 2, measured, every benchmark and every level", "",
             "measured on random search's one filtered sample, through "
             "src/metrics_decision.py's compare_phi_on_one_sample: one uniform "
             "sample of the box, evaluated once, filtered under each phi in turn, "
             "so the three sets differ only through the order. the per-seed values "
             "behind every median are in "
             "results/tier1/decision_metrics_by_seed.csv.", "",
             "**delta zero is the headline, d-08.** the three sets of one "
             "comparison are index sets over one array, so two decision vectors "
             "are the same point bitwise or they are two points and the coverage "
             "is exactly the shared count over the count. the positive delta is "
             "one twentieth of the box diameter and is there for one reason: the "
             "noise floor and the population solvers' own pairs compare two "
             "different samples, which share no point at all, so at delta zero "
             "they are zero by construction and carry nothing. a floor and a "
             "cross-phi number are read against each other at one delta and never "
             "across two.", "",
             "d3's decision block has no column for the imprecision level, so "
             "there is one table per level rather than one table with a compound "
             "key in the problem column; widening d3 is another subpart's file. "
             "overlap is dice throughout, d-09, and the jaccard value of every "
             "pair is in section 5.", ""]
    for name, path in sorted(tables.items()):
        lines.extend(record_measured_level(name, path, budgets))
    return lines


# one imprecision level's section of table 2, at every budget it was run at
def record_measured_level(name, path, budgets):
    level = name.split("_")[-1]
    lines = ["### eps {}, from results/tier1/{}".format(level, path.name), ""]
    for budget in budgets:
        rows = [row for row in decision_rows_at(path, budget)
                if row["phi_a"] != row["phi_b"] and row["metric"]
                in ("coverage_a_in_b", "coverage_b_in_a", "overlap")]
        if not rows:
            continue
        lines.extend(["budget {}, the cross-phi pairs:".format(budget), ""])
        lines.extend(markdown_table(("problem", "phi_a", "phi_b", "status",
                                     "metric", "cardinality_a", "cardinality_b",
                                     "median", "q1", "q3", "delta", "box_scale"),
                                    rows))
        lines.append("")
    lines.extend(record_level_floor(path))
    lines.extend(record_level_cross(path, budgets[0]))
    return lines


# one level's same-phi seed-to-seed noise floor, at the positive delta
def record_level_floor(path):
    floor = [row for row in decision_rows_at(path)
             if row["phi_a"] == row["phi_b"] and row["metric"]
             in ("coverage_a_in_b", "coverage_b_in_a", "overlap")]
    if not floor:
        return []
    return (["the noise floor, one phi against itself at two seeds:", ""]
            + markdown_table(("problem", "phi_a", "metric", "n_evals",
                              "cardinality_a", "cardinality_b", "median", "q1",
                              "q3", "delta"), floor) + [""])


# one level's cross evaluation and symmetric hausdorff, at the reported budget
def record_level_cross(path, budget):
    rows = [row for row in decision_rows_at(path, budget)
            if row["phi_a"] != row["phi_b"] and row["metric"]
            in ("cross_a_under_b", "cross_b_under_a", "hausdorff_symmetric")]
    if not rows:
        return []
    return (["the cross evaluation and the symmetric hausdorff distance at budget "
             "{}, neither of which moves with delta:".format(budget), ""]
            + markdown_table(("problem", "phi_a", "phi_b", "status", "metric",
                              "cardinality_a", "cardinality_b", "median", "q1",
                              "q3"), rows) + [""])


# the record's two overlap conventions, dice and jaccard of the same pairs
def record_overlap(rows, path, budget):
    lines = ["## 5. the two overlap conventions, dice and jaccard", "",
             "d-09. d2's compute_overlap is the two covered counts over the two "
             "cardinalities, which is dice; the shared fraction of the union is "
             "jaccard. both are correct, they are different functionals, and "
             "jaccard is computed here from dice by the identity jaccard = dice / "
             "(2 - dice) rather than by changing d2. coverage leads in every table "
             "above because it is directional and unambiguous. the rows are random "
             "search's pairs at delta zero and at the reported budget; every pair, "
             "every level, both deltas and both budgets are in "
             "results/tier1/{}.".format(path.name), ""]
    shown = [row for row in rows
             if row["solver"] == "random_search"
             and float(row["delta"]) == zero_delta
             and int(row["n_evals"]) == budget]
    lines.extend(markdown_table(("problem", "eps", "phi_a", "phi_b", "status",
                                 "n_seeds", "dice_median", "jaccard_median"),
                                shown))
    return lines + [""]


# the record's delta sweep, which is d-08's dimension argument as a measurement
def record_delta_sweep(rows, budget):
    lines = ["## 6. how the measured numbers move with delta, at thirty and at "
             "twelve variables", "",
             "delta is a reporting parameter and the numbers move with it. on tier "
             "1 that movement is also the measurement behind d-08: a delta fixed "
             "as a fraction of the box diameter is not the same quantity on a "
             "30-box as on p1's 2-box, distances growing like the square root of "
             "the dimension, so a fraction chosen on the calibration problem would "
             "not carry. the median over the seeds at budget {}, on the pair that "
             "is nested in neither direction, at the reported level. source: "
             "results/tier1/delta_sweep.csv.".format(budget), ""]
    lines.extend(markdown_table(("problem", "eps", "phi_a", "phi_b", "metric",
                                 "delta_box_fraction", "delta", "median"), rows))
    return lines + [""]


# what the solver table may and may not be read as, above the tables themselves
def record_solvers_note():
    return ["## 7. table 3, the solvers, and it is never mixed into the pair "
            "numbers", "",
            "the objective-space metrics are valid for comparing solvers under "
            "one fixed phi and are never a ranking of phi, CONTEXT.md section 5 "
            "step 5. **no igd is computed**: src/reference_fronts.py derives a "
            "reference front for p1 alone, so there is nothing to average over "
            "here and the metric is not computed rather than computed against "
            "something invented; every objective-space row therefore carries a "
            "reference size of zero. **the objective-space metrics are computed "
            "at the common cardinality of each comparison**, r-16 and CONTEXT.md "
            "section 10 d1, taken across solvers, phi, seeds and both budgets and "
            "not per phi, since the smallest front is systematically phi_lu's. e1 "
            "reported at full cardinality instead, so the two objective blocks "
            "are not compared with each other. the decision block of the same "
            "files holds the pair statistics of nsga-ii's and mopso's own output, "
            "where phi drives the search as well as the ordering, so those rows "
            "are a question about the solvers and never a pair number of the "
            "study.", "",
            "the cardinality every front of one comparison was cut to, and "
            "whether a hypervolume was scored at all:", ""]


# the record's solver tables, the objective-space metrics and the solvers' pairs
def record_solvers(tables, points, cardinalities, budget):
    lines = record_solvers_note()
    lines.extend(markdown_table(("key", "value", "source"),
                                cardinalities + points))
    lines.extend(["", "the objective-space metrics at budget {}; the same rows at "
                  "the convergence budget are in the same files. every row is a "
                  "median with its interquartile range over the seeds, and a ratio "
                  "taken across two phi here is a ratio of volumes in two "
                  "different spaces and means nothing.".format(budget), ""])
    for name, path in sorted(tables.items()):
        lines.extend(record_solver_level(name, path, budget))
    return lines


# one imprecision level's objective-space rows and solver pairs
def record_solver_level(name, path, budget):
    level = name.split("_")[-1]
    rows = [row for row in read_metrics_table(path)[objective_block]
            if row["n_evals"] == budget]
    lines = ["### eps {}, from results/tier1/{}".format(level, path.name), ""]
    lines.extend(markdown_table(("problem", "phi", "solver", "metric",
                                 "cardinality", "reference_size", "median", "q1",
                                 "q3"), rows))
    pairs = [row for row in decision_rows_at(path, budget)
             if row["metric"] in ("coverage_a_in_b", "coverage_b_in_a", "overlap")]
    if pairs:
        lines.extend(["", "the two population solvers' own pairs at the same "
                      "budget, at the positive delta because two runs of one "
                      "solver are two different samples:", ""])
        lines.extend(markdown_table(("problem", "phi_a", "phi_b", "status",
                                     "metric", "cardinality_a", "cardinality_b",
                                     "median", "q1", "q3", "delta"), pairs))
    return lines + [""]


# the record's rank-1 series, which says which fronts are spread results
def record_rank(rows, budget):
    lines = ["## 8. the rank-1 size against the population size", "",
             "CONTEXT.md section 10 e2. a configuration in which rank 1 fills the "
             "survivor slots is one where dominance-based selection has no "
             "pressure: every survivor is then chosen out of one front on crowding "
             "distance alone, and the solver's front is a spread result and not a "
             "convergence result. the series is read out of the algorithm's state "
             "after every generation through a pymoo Callback, the instrument "
             "docs/c3_validation.md section 5.1 describes; pymoo is not modified, "
             "src/runners.py is not modified, and the candidate set is the "
             "previous generation's survivors stacked on this generation's "
             "offspring, sorted with pymoo's own NonDominatedSorting. the median "
             "column is the rank-1 size over the second half of the run. source: "
             "results/tier1/rank_one_summary.csv, with the per-generation series "
             "in results/tier1/rank_one_by_generation.csv. "
             "first_saturated_generation is the median over the seeds that "
             "saturated at all and is empty where none did, so it is read "
             "together with saturates_in_every_seed and never alone.", "",
             "at budget {}:".format(budget), ""]
    lines.extend(markdown_table(("problem", "solver", "phi", "eps", "pop_size",
                                 "n_generations", "saturates_in_every_seed",
                                 "first_saturated_generation", "n_seeds", "median",
                                 "q1", "q3"),
                                [row for row in rows
                                 if int(row["n_evals"]) == budget]))
    lines.extend(["", "a row whose saturates_in_every_seed is True is a "
                  "configuration whose front is a spread result from its "
                  "first_saturated_generation onwards. e2 reports the number and "
                  "does not read it.", ""])
    return lines


# the record's free sets and effective column counts, measured and not asserted
def record_structure(rows):
    lines = ["## 9. the free sets and the effective column counts", "",
             "measured by resampling each decision variable in turn: a column that "
             "does not move does not depend on that variable, and its free set is "
             "what is left. the effective column count is how many of the 2m image "
             "columns are distinct functions on the same sample, which is r-20 and "
             "a5-b checked at the run rather than inherited: a5's shared width "
             "made two of zdt1's four columns one function under examples 2.3 and "
             "2.4 and three of dtlz2's six, and the duplication was phi-dependent, "
             "so the headline pair compared transformed problems of different "
             "dimension. source: results/tier1/free_sets.csv. the column order is "
             "the 2m order every module assumes, (Lambda_1^T f, B_1^T f, "
             "Lambda_2^T f, ...).", "",
             "the effective column counts, one row per problem, phi and level:", ""]
    counts = distinct_column_rows(rows)
    lines.extend(markdown_table(("problem", "phi", "eps", "n_columns",
                                 "effective_columns"), counts))
    lines.extend(["", "the free sets, at the level the convergence check was run "
                  "at:", ""])
    lines.extend(markdown_table(("problem", "phi", "column", "free_set_size",
                                 "constant_column", "depends_on"),
                                [row for row in rows
                                 if float(row["eps"]) == convergence_eps]))
    return lines + [""]


# one row per problem, phi and level of the effective column count
def distinct_column_rows(rows):
    seen, counts = set(), []
    for row in rows:
        key = (row["problem"], row["phi"], row["eps"])
        if key in seen:
            continue
        seen.add(key)
        counts.append({"problem": row["problem"], "phi": row["phi"],
                       "eps": row["eps"], "n_columns": row["n_columns"],
                       "effective_columns": row["effective_columns"]})
    return counts


# what m-2 is and which two structures it is measured against, above its table
def record_overhang_note(path):
    return ["## 10. m-2, the overhang, on both benchmarks at twenty seeds", "",
            "PROGRESS.md x-01 registers the protected-minimiser effect and x-02 "
            "registers the seed count. **m-1 is withdrawn as an instrument at "
            "x-01's outcome line and is not computed here, not revived and not "
            "re-thresholded.** m-2 takes the argmin of an image column over one "
            "seed's uniform sample of the box, which is the protected member, and "
            "measures the distance from its free coordinates to the projection of "
            "the efficient structure onto them. a constant column has no member "
            "minimising it strictly, so the measurement is not defined there and "
            "the row is marked rather than filled with a zero. source: "
            "results/tier1/{}, with the per-seed values in "
            "results/tier1/overhang_by_seed.csv.".format(path.name), "",
            "**two structures, and the file names both.** the structure x-01 "
            "registered is x_2 = ... = x_29 = 0 for zdt1 and "
            "x_3 = ... = x_11 = 1/2 for dtlz2, and it is the headline because a "
            "registered measurement is not edited after registration. a5-b then "
            "moved which decision variable each objective's half-width reads, so "
            "docs/plan_after_meeting.md section f3's own domination argument, "
            "re-run on a5-b's forms, pins one variable fewer on zdt1 and two "
            "fewer on dtlz2: raising x_i strictly raises the centre columns and "
            "leaves the width columns alone only while x_i drives no width. the "
            "second structure is that argument's answer and is reported beside "
            "the first and not instead of it.", ""]


# how x-01 reads m-2, printed under the table so that e2 does not read it here
def record_overhang_reading():
    return ["", "x-01 reads m-2 as follows and e2 does not read it: the median "
            "overhang is predicted strictly positive where the condition says the "
            "effect is present and exactly zero where it says absent. the "
            "condition is that some column has a non-empty free set and the "
            "phi-efficient set's projection onto it is a proper subset of the "
            "box's, of positive co-measure. x-01's own analysis of the a5 forms "
            "says present on zdt1 under all three phi, because zdt1's f_1 = x_1 is "
            "separable and the efficient set collapses onto a measure-zero "
            "projection, and present on dtlz2 under examples 2.3 and 2.4 and "
            "absent under example 2.2, whose only free-set column omits a variable "
            "the efficient set does not constrain. reading the numbers above "
            "against that is e3's.", ""]


# the record's m-2, the one registered measurement e2 computes
def record_overhang(rows, path, budget):
    lines = record_overhang_note(path)
    lines.extend(["at budget {}, the columns with a non-empty free set:"
                  .format(budget), ""])
    shown = [row for row in rows
             if int(row["n_evals"]) == budget and int(row["free_set_size"]) > 0]
    lines.extend(markdown_table(("problem", "phi", "eps", "column", "structure",
                                 "free_set_size", "constant_column", "defined",
                                 "n_seeds", "median", "iqr", "mean",
                                 "standard_error"), shown))
    return lines + record_overhang_reading()


# the record's figure list, every figure carrying its own budget and seed count
def record_figures(paths, root):
    lines = ["## 11. the figures", "",
             "every figure is drawn through src/reporting.py and carries the "
             "budget, the seed count and the cardinality of each series inside the "
             "image and never in the filename. the decision-space figures are a "
             "projection onto x_1 and x_2 and carry no derived region behind them: "
             "b2 derives one for p1 alone, and thirty variables do not fit on a "
             "plane. they are drawn at the first seed of the list and with the "
             "three sets in decreasing order of size, because five seeds pooled "
             "bury one another and the registry's order hides the smallest set "
             "under the largest; the legend states the seed count and the "
             "cardinality of every series. the paths are relative to the run's "
             "output root, results/tier1.", ""]
    lines.extend("- {}".format(path.relative_to(root).as_posix())
                 for path in sorted(paths))
    return lines + [""]


# the cross-phi coverage beside the same-phi floor, at one delta and never two
def floor_comparison_rows(tables, budget):
    # docs/plan_after_meeting.md section b1: a cross-phi number that does not
    # exceed the seed-to-seed disagreement of one phi is not evidence of
    # anything. the two are read at the positive delta, where the floor is not
    # zero by construction, and the delta zero value of the same pair is carried
    # beside them so the headline is not lost.
    rows = []
    for name, path in sorted(tables.items()):
        written = decision_rows_at(path, budget)
        floors = {(row["problem"], row["phi_a"]): row["median"] for row in written
                  if row["phi_a"] == row["phi_b"]
                  and row["metric"] == "coverage_a_in_b"}
        rows.extend(floor_rows_of(name, written, floors))
    return rows


# the floor comparison of one imprecision level's table
def floor_rows_of(name, written, floors):
    zero = {(row["problem"], row["phi_a"], row["phi_b"]): row["median"]
            for row in written if row["metric"] == "coverage_a_in_b"
            and row["delta"] == zero_delta}
    rows = []
    for row in written:
        key = (row["problem"], row["phi_a"], row["phi_b"])
        if (row["phi_a"] == row["phi_b"] or row["metric"] != "coverage_a_in_b"
                or row["delta"] == zero_delta or key not in zero):
            continue
        floor = floors.get((row["problem"], row["phi_a"]))
        rows.append({"problem": row["problem"], "eps": name.split("_")[-1],
                     "phi_a": row["phi_a"], "phi_b": row["phi_b"],
                     "status": row["status"], "coverage_at_delta_zero": zero[key],
                     "coverage_at_delta": row["median"], "same_phi_floor": floor,
                     "below_the_floor": None if floor is None
                     else bool(row["median"] < floor)})
    return rows


# how many configurations of one problem and solver saturate in every seed
def saturation_rows(rank_rows, budget):
    rows = []
    keys = sorted({(row["problem"], row["solver"]) for row in rank_rows})
    for problem_name, solver in keys:
        group = [row for row in rank_rows
                 if (row["problem"], row["solver"]) == (problem_name, solver)
                 and int(row["n_evals"]) == budget]
        saturating = [row for row in group
                      if as_bool(row["saturates_in_every_seed"])]
        rows.append({"problem": problem_name, "solver": solver,
                     "n_configurations": len(group),
                     "n_saturating_in_every_seed": len(saturating),
                     "spread_results": len(saturating) == len(group)})
    return rows


# where m-2's median is positive and where it is zero, per problem, phi and level
def overhang_presence_rows(rows, budget):
    presence = []
    keys = sorted({(row["problem"], row["phi"], row["eps"], row["structure"])
                   for row in rows})
    for problem_name, phi_name, eps, structure in keys:
        group = [row for row in rows
                 if (row["problem"], row["phi"], row["eps"], row["structure"])
                 == (problem_name, phi_name, eps, structure)
                 and int(row["n_evals"]) == budget and as_bool(row["defined"])
                 and int(row["free_set_size"]) > 0]
        positive = [row for row in group if float(row["median"]) > 0.0]
        presence.append({"problem": problem_name, "phi": phi_name, "eps": eps,
                         "structure": structure,
                         "columns_with_a_free_set": len(group),
                         "columns_with_a_positive_median": len(positive),
                         "effect_present_on_some_column": bool(positive)})
    return presence


# the record's findings, each one a table this run wrote and none of them a reading
def record_findings(root, tables, budget):
    lines = ["## 12. findings, and none of them a reading", "",
             "each of the three tables below is assembled from files this run "
             "wrote and states a fact about the run. what any of them means for "
             "the study is e3's, CONTEXT.md section 10 e3.", "",
             "**the cross-phi coverage against the same-phi noise floor.** both "
             "at the positive delta, since the floor is zero by construction at "
             "delta zero, with the delta zero value of the same pair carried "
             "beside them. below_the_floor is true where the cross-phi coverage is "
             "smaller than the coverage of one phi's set by the same phi at "
             "another seed, which is the comparison "
             "docs/plan_after_meeting.md section b1 asks for: a cross-phi number "
             "that does not exceed the instrument's own seed-to-seed disagreement "
             "is not evidence of anything. read the floor column first, and read "
             "it with the sweep below it: two independent uniform samples share no "
             "point, so the floor is a count of how many points of one sample fall "
             "within delta of the other, and at thirty and at twelve variables a "
             "ball of one twentieth of the box diameter contains none of them.",
             ""]
    lines.extend(markdown_table(
        ("problem", "eps", "phi_a", "phi_b", "status", "coverage_at_delta_zero",
         "coverage_at_delta", "same_phi_floor", "below_the_floor"),
        floor_comparison_rows(tables, budget)))
    lines.extend(record_findings_floor(root))
    lines.extend(record_findings_rank(root, budget))
    lines.extend(record_findings_overhang(root, budget))
    return lines


# the floor's median over the seeds at each swept delta, per problem, phi and level
def floor_sweep_summary(root):
    rows = [row for row in read_table(root / "noise_floor_sweep.csv")
            if row["metric"] == "coverage_a_in_b"]
    summary = []
    for key in sorted({(row["problem"], row["phi"], row["eps"],
                        row["delta_box_fraction"], row["delta"]) for row in rows}):
        values = [float(row["value"]) for row in rows
                  if (row["problem"], row["phi"], row["eps"],
                      row["delta_box_fraction"], row["delta"]) == key]
        summary.append({"problem": key[0], "phi": key[1], "eps": float(key[2]),
                        "delta_box_fraction": float(key[3]),
                        "delta": float(key[4]),
                        "median": float(np.median(values))})
    return summary


# the swept floor at the level the convergence check was run at, as the record's row
def record_findings_floor(root):
    lines = ["", "**the floor swept, and how large a ball has to be before it "
             "stops being zero.** the same statistic between two seeds of one phi "
             "at a range of delta, at the reported budget and at the level the "
             "convergence check was run at. it is zero at delta zero by "
             "construction, two independent uniform samples sharing no point, and "
             "the sweep says whether that survives a ball of a fifth, a third or a "
             "half of the box diameter at thirty and at twelve variables. source: "
             "results/tier1/noise_floor_sweep.csv, which carries every level.", ""]
    rows = [row for row in floor_sweep_summary(root)
            if row["eps"] == convergence_eps]
    return lines + markdown_table(("problem", "phi", "eps", "delta_box_fraction",
                                   "delta", "median"), rows) + [""]


# the saturation count and the overhang presence, the run's other two findings
def record_findings_rank(root, budget):
    lines = ["", "**how many configurations are spread results.** a configuration "
             "whose rank 1 holds at least the population size of the candidate set "
             "in every seed is one where dominance decides nothing after its "
             "first_saturated_generation, so its front is a spread result. the "
             "count is over the five imprecision levels and the three phi, fifteen "
             "configurations per problem and solver.", ""]
    return lines + markdown_table(
        ("problem", "solver", "n_configurations", "n_saturating_in_every_seed",
         "spread_results"),
        saturation_rows(read_table(root / "rank_one_summary.csv"), budget)) + [""]


# where m-2's median is positive and where it is zero, as the run's third finding
def record_findings_overhang(root, budget):
    lines = ["", "**where m-2's median overhang is positive.** one row per "
             "problem, phi, level and structure, counting the image columns with a "
             "non-empty free set and how many of them carry a strictly positive "
             "median overhang over the twenty seeds. x-01 predicts the effect "
             "present exactly where some such column has one.", ""]
    return lines + markdown_table(
        ("problem", "phi", "eps", "structure", "columns_with_a_free_set",
         "columns_with_a_positive_median", "effect_present_on_some_column"),
        overhang_presence_rows(read_table(root / "overhang_summary.csv"),
                               budget)) + [""]


# what this run settled that the plan did not, in its own artefacts' terms
def record_closing_conventions():
    return [
        "## 13. what this run settled that the plan did not", "",
        "*there is one table 2 per imprecision level and not one table with a "
        "level column.* d3's decision block has fixed columns and none of them is "
        "the level; widening d3 would invalidate every table e1 wrote, since "
        "read_metrics_table checks the column count of every row. the alternative, "
        "a compound key in the problem column, was rejected because a reader "
        "cannot tell a compound label from a problem name. the raw per-seed files "
        "carry a proper eps column and are the provenance for every table.", "",
        "*jaccard is written to its own file and not into a metrics table.* d3's "
        "decision block admits d2's eight metrics and no others, which is the "
        "restriction that keeps a table from carrying a number its module does not "
        "compute. so the jaccard value of every pair is in "
        "overlap_conventions.csv beside the dice value of the same pair and the "
        "same seeds, and each table's note points there. d2 is not changed, d-09.",
        ""]


# the two instrument decisions this run took, and what e2 refuses to do
def record_closing_instruments():
    return [
        "*the objective-space metrics are truncated and the decision-space ones "
        "are not.* r-16's two rules are kept together: the truncation is applied "
        "to the objective block, where all three metrics move with the cardinality "
        "by more than the differences between solvers, and the cardinality is "
        "printed on every row of both blocks. CONTEXT.md section 10 d1 restricts "
        "the truncation to the objective-space metrics, so the pair statistics are "
        "on the full untruncated sets.", "",
        "*no hypervolume is scored at eps = 0 under any phi.* every half-width is "
        "zero there, so the second image coordinate of examples 2.3 and 2.4 is "
        "identically zero, the pooled column has zero range, no point can strictly "
        "dominate any row and every row's box has zero thickness. the point is "
        "still recorded, so the other metrics' rows state the one the "
        "configuration would have been scored against. section 7's table carries "
        "the verdict per problem, phi and level.", "",
        "## 14. what e2 does not do", "",
        "e2 does not interpret. it does not read m-2 against x-01's condition, "
        "does not say whether the difference between two orders is large, does not "
        "compare solvers and does not select anything. it does not compute m-1, "
        "which is withdrawn. that is e3's, CONTEXT.md section 10 e3, and the "
        "tables and the record above are its input.", ""]


# what this session settled and what e2 refuses to do, as the record's close
def record_closing():
    return record_closing_conventions() + record_closing_instruments()


# the delta sweep's median over seeds, on the pair free in both directions
def delta_sweep_summary(root, budget, eps):
    rows = [row for row in read_table(root / "delta_sweep.csv")
            if int(row["n_evals"]) == budget and float(row["eps"]) == eps
            and (row["phi_a"], row["phi_b"]) == ("lu", "cw")]
    summary = []
    for key in sorted({(row["problem"], row["metric"], row["delta_box_fraction"],
                        row["delta"]) for row in rows}):
        values = [float(row["value"]) for row in rows
                  if (row["problem"], row["metric"], row["delta_box_fraction"],
                      row["delta"]) == key]
        summary.append({"problem": key[0], "eps": eps, "phi_a": "lu", "phi_b": "cw",
                        "metric": key[1], "delta_box_fraction": float(key[2]),
                        "delta": float(key[3]),
                        "median": float(np.median(values))})
    return summary


# the summary rows whose key begins with a stated prefix, as the record reads them
def summary_keys(summary, prefix):
    return [row for row in summary if row["key"].startswith(prefix)]


# the tables of one prefix, by the names save_table gave them
def tables_named(tables, prefix):
    return {name: path for name, path in tables.items() if name.startswith(prefix)}


# writes the record, reading every number back out of the files just written
def write_record(record_path, root, tables, paths, settings, tier0_root):
    budget = settings["budgets"][0]
    summary = read_table(root / "summary.csv")
    lines = record_opening(summary, tables)
    lines.extend(record_no_exact_table())
    lines.extend(record_inherited(inherited_error_rows(tier0_root),
                                  settings["budgets"]))
    lines.extend(record_measured(tables_named(tables, "2_measured"),
                                 settings["budgets"]))
    lines.extend(record_overlap(read_table(root / "overlap_conventions.csv"),
                                root / "overlap_conventions.csv", budget))
    lines.extend(record_delta_sweep(delta_sweep_summary(root, budget,
                                                        convergence_eps), budget))
    lines.extend(record_solvers(tables_named(tables, "3_solvers"),
                                summary_keys(summary, "hypervolume_scored"),
                                summary_keys(summary, "common_cardinality"),
                                budget))
    lines.extend(record_rank(read_table(root / "rank_one_summary.csv"), budget))
    lines.extend(record_structure(read_table(root / "free_sets.csv")))
    lines.extend(record_overhang(read_table(root / "overhang_summary.csv"),
                                 root / "overhang_summary.csv", budget))
    lines.extend(record_figures(paths, root))
    lines.extend(record_findings(root, tables_named(tables, "2_measured"), budget))
    lines.extend(record_closing())
    record_path.parent.mkdir(parents=True, exist_ok=True)
    record_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return record_path


# writes one metrics table through d3, with the block that has no rows left empty
def save_table(root, name, decision_rows, objective_rows):
    path = root / "table_{}.csv".format(name)
    root.mkdir(parents=True, exist_ok=True)
    save_metrics_table({objective_block: objective_rows,
                        decision_block: decision_rows}, path)
    return path


# the name of the table one imprecision level's rows are written to
def level_table_name(prefix, eps):
    return "{}_eps_{}".format(prefix, repr(float(eps)))


# every per-seed decision-space row of the run, random search and both solvers
def all_decision_rows(runs, comparisons, settings):
    measured, solver_rows = [], []
    for problem_name in problem_names:
        problem = problem_registry[problem_name]
        delta = problem_delta(problem)
        for eps in epsilon_levels:
            params = problem_parameters(eps)
            for budget in budgets_for(eps, settings["budgets"]):
                found = comparisons[(problem_name, eps, budget)]
                measured.extend(decision_rows_by_seed(found, problem_name, eps,
                                                      budget))
                for comparison in found:
                    measured.extend(pair_rows_at_delta(comparison, problem_name,
                                                       eps, budget, zero_delta))
                measured.extend(noise_floor_rows(found, problem_name, eps, budget))
                for solver in population_solvers:
                    solver_rows.extend(solver_pair_rows(runs, problem, params,
                                                        solver, eps, budget, delta))
    return measured, solver_rows


# the delta sweep over every problem and level at the reported budget
def all_delta_sweep_rows(comparisons, settings):
    rows = []
    budget = settings["budgets"][0]
    for problem_name in problem_names:
        for eps in epsilon_levels:
            rows.extend(delta_sweep_rows(comparisons[(problem_name, eps, budget)],
                                         problem_registry[problem_name], eps,
                                         budget))
    return rows


# the field order of every raw csv this script writes
raw_fieldnames = {
    "free_sets.csv": ("problem", "phi", "eps", "column", "n_columns",
                      "effective_columns", "depends_on", "free_set",
                      "free_set_size", "constant_column"),
    "decision_metrics_by_seed.csv": ("problem", "solver", "phi_a", "phi_b",
                                     "status", "metric", "eps", "n_evals", "seed",
                                     "cardinality_a", "cardinality_b", "delta",
                                     "containment_violations", "value"),
    "objective_metrics_by_seed.csv": ("problem", "phi", "solver", "metric", "eps",
                                      "n_evals", "seed", "cardinality",
                                      "full_cardinality", "reference_size",
                                      "include_singular_segments", "value"),
    "overlap_conventions.csv": ("problem", "solver", "phi_a", "phi_b", "status",
                                "eps", "n_evals", "delta", "box_scale", "n_seeds",
                                "dice_median", "dice_q1", "dice_q3",
                                "jaccard_median", "jaccard_q1", "jaccard_q3"),
    "rank_one_by_generation.csv": ("problem", "solver", "phi", "eps", "n_evals",
                                   "seed", "generation", "n_candidates", "n_pop",
                                   "rank_1_of_candidates", "survivors_from_rank_1",
                                   "n_fronts"),
    "rank_one_summary.csv": ("problem", "solver", "phi", "eps", "n_evals",
                             "n_seeds", "pop_size", "n_generations",
                             "saturates_in_every_seed",
                             "first_saturated_generation", "median", "q1", "q3",
                             "iqr"),
    "overhang_by_seed.csv": ("measurement", "structure", "problem", "phi", "eps",
                             "column", "free_set_size", "constant_column",
                             "n_evals", "seed", "defined", "value",
                             "protected_index"),
    "overhang_summary.csv": ("measurement", "structure", "problem", "phi", "eps",
                             "column", "n_evals", "free_set_size",
                             "constant_column", "defined", "n_seeds", "median",
                             "q1", "q3", "iqr", "mean", "standard_deviation",
                             "standard_error"),
    "noise_floor_sweep.csv": ("problem", "phi", "metric", "eps", "n_evals", "seed",
                              "delta_box_fraction", "delta", "box_scale",
                              "cardinality_a", "cardinality_b", "value"),
    "delta_sweep.csv": ("problem", "phi_a", "phi_b", "status", "metric", "eps",
                        "n_evals", "seed", "delta_box_fraction", "delta",
                        "box_scale", "cardinality_a", "cardinality_b", "value"),
    "inherited_instrument_error.csv": ("problem", "phi_a", "phi_b", "status",
                                       "metric", "n_evals", "delta", "exact",
                                       "measured_median", "error",
                                       "relative_error"),
    "summary.csv": ("key", "value", "source"),
}


# writes one of the run's raw csv files, in the field order stated above
def write_raw_table(root, name, rows):
    return write_table(root / name, raw_fieldnames[name], rows)


# the measured pair tables, one per imprecision level, and the rows behind them
def write_measured(root, measured_by_seed):
    write_raw_table(root, "decision_metrics_by_seed.csv", measured_by_seed)
    write_raw_table(root, "overlap_conventions.csv",
                    overlap_convention_rows(measured_by_seed))
    tables = {}
    for eps in epsilon_levels:
        rows = [row for row in measured_by_seed if row["eps"] == float(eps)]
        name = level_table_name("2_measured", eps)
        tables[name] = save_table(root, name,
                                  block_admissible(decision_table_rows(rows)), [])
    return tables


# the solver tables, the objective-space metrics beside the solvers' own pairs
def write_solvers(root, objective_by_seed, solver_by_seed, points):
    write_raw_table(root, "objective_metrics_by_seed.csv", objective_by_seed)
    tables = {}
    for eps in epsilon_levels:
        decision = [row for row in solver_by_seed if row["eps"] == float(eps)]
        objective = [row for row in objective_by_seed if row["eps"] == float(eps)]
        name = level_table_name("3_solvers", eps)
        tables[name] = save_table(
            root, name, block_admissible(decision_table_rows(decision)),
            objective_table_rows(objective, points))
    return tables


# the free sets, the effective column counts and m-2, per seed and summarised
def write_structure(root, settings):
    free_rows = structure_rows(settings)
    write_raw_table(root, "free_sets.csv", free_rows)
    rows = overhang_rows(free_rows, settings)
    write_raw_table(root, "overhang_by_seed.csv", rows)
    write_raw_table(root, "overhang_summary.csv", overhang_summary_rows(rows))
    return free_rows


# the rank-1 series of every population configuration, per generation and summarised
def write_rank(root, rank_rows):
    write_raw_table(root, "rank_one_by_generation.csv", rank_rows)
    return write_raw_table(root, "rank_one_summary.csv",
                           rank_summary_rows(rank_rows))


# every artefact between the runs and the record, and the tables they are in
def write_artefacts(root, runs, comparisons, rank_rows, settings, tier0_root):
    announce("computing the decision-space metrics")
    measured_by_seed, solver_by_seed = all_decision_rows(runs, comparisons, settings)
    tables = write_measured(root, measured_by_seed)
    announce("computing the objective-space metrics")
    objective_by_seed, points, cardinalities = objective_values(runs, settings)
    tables.update(write_solvers(root, objective_by_seed, solver_by_seed, points))
    write_raw_table(root, "delta_sweep.csv",
                    all_delta_sweep_rows(comparisons, settings))
    announce("sweeping the noise floor")
    write_raw_table(root, "noise_floor_sweep.csv", floor_sweep_rows(runs, settings))
    write_raw_table(root, "inherited_instrument_error.csv",
                    inherited_error_rows(tier0_root))
    announce("measuring the free sets and the overhang")
    write_structure(root, settings)
    write_rank(root, rank_rows)
    return tables, points, cardinalities


# the whole run: the grid, the artefacts, the tables, the figures and the record
def run(output_root, record_path, settings, tier0_root):
    started = time.time()
    root = Path(output_root)
    runs, comparisons, rank_rows = execute_grid(settings)
    announce("saving raw results")
    save_raw(root, runs)
    tables, points, cardinalities = write_artefacts(root, runs, comparisons,
                                                    rank_rows, settings, tier0_root)
    announce("drawing figures")
    paths = all_figures(root, runs, settings)
    write_raw_table(root, "summary.csv",
                    summary_rows(settings, runs, tables, points, cardinalities,
                                 time.time() - started))
    announce("writing the record")
    write_record(Path(record_path), root, tables, paths, settings, tier0_root)
    return tables


# the tables of a run already on disk, by the names save_table gives them
def artefact_tables(root):
    return {name: root / "table_{}.csv".format(name)
            for prefix in ("2_measured", "3_solvers")
            for name in [level_table_name(prefix, eps) for eps in epsilon_levels]}


# the figures of a run already on disk, in the order the record lists them
def artefact_figures(root):
    return sorted((root / "figures").glob("*.png"))


# every configuration of a run already on disk, read back from its raw arrays
def artefact_runs(root, settings):
    return {(problem_name, solver, phi_name, eps, budget):
            load_raw_runs(raw_path(root, (problem_name, solver, phi_name, eps,
                                          budget)))
            for problem_name in problem_names
            for solver in solver_names
            for phi_name in phi_names
            for eps in epsilon_levels
            for budget in budgets_for(eps, settings["budgets"])}


# the figures redrawn from the raw arrays, without re-running anything
def rebuild_figures(output_root, settings):
    root = Path(output_root)
    return all_figures(root, artefact_runs(root, settings), settings)


# the noise-floor sweep recomputed from the raw arrays, without re-running anything
def rebuild_floor_sweep(output_root, settings):
    # the sweep needs only the per-phi decision sets random search returned, and
    # the raw arrays hold those, so it is the one artefact that can be added to a
    # finished run without spending the grid again.
    root = Path(output_root)
    return write_raw_table(root, "noise_floor_sweep.csv",
                           floor_sweep_rows(artefact_runs(root, settings),
                                            settings))


# the record rebuilt from the artefacts of a run, without re-running anything
def rebuild_record(output_root, record_path, settings, tier0_root):
    # the raw results and the tables are re-readable without re-running, so the
    # record they are read into is too. this is how a change to the record's prose
    # reaches the document without spending the grid again, and it is also the
    # check that every number in the record does come out of a file: nothing of
    # the run is in memory here.
    root = Path(output_root)
    return write_record(Path(record_path), root, artefact_tables(root),
                        artefact_figures(root), settings, tier0_root)


# the run parameters as the command line states them
def parse_arguments(argv):
    parser = argparse.ArgumentParser(description="e2, the tier 1 run")
    parser.add_argument("--output-root", default=str(repository_root / "results"
                                                     / "tier1"))
    parser.add_argument("--tier0-root", default=str(repository_root / "results"
                                                    / "tier0"))
    parser.add_argument("--record", default=str(repository_root / "docs"
                                                / "e2_tier1_results.md"))
    parser.add_argument("--seeds", default=",".join(str(seed) for seed in run_seeds))
    parser.add_argument("--overhang-seeds",
                        default=",".join(str(seed) for seed in overhang_seeds))
    parser.add_argument("--budgets", default="{},{}".format(
        gate_budget, gate_budget * convergence_multiple))
    parser.add_argument("--pop-size", type=int, default=gate_pop_size)
    parser.add_argument("--record-only", action="store_true",
                        help="rebuild the record from artefacts already written")
    parser.add_argument("--floor-only", action="store_true",
                        help="recompute the noise-floor sweep from the raw "
                             "arrays, then the record")
    parser.add_argument("--figures-only", action="store_true",
                        help="redraw the figures from the raw arrays, then the "
                             "record")
    return parser.parse_args(argv)


# the entry point: parse, run, and say where the record went
def main(argv=None):
    arguments = parse_arguments(argv)
    settings = run_settings(
        [int(seed) for seed in arguments.seeds.split(",")],
        [int(budget) for budget in arguments.budgets.split(",")],
        arguments.pop_size,
        [int(seed) for seed in arguments.overhang_seeds.split(",")])
    if arguments.floor_only:
        rebuild_floor_sweep(arguments.output_root, settings)
        rebuild_record(arguments.output_root, arguments.record, settings,
                       arguments.tier0_root)
    elif arguments.figures_only:
        rebuild_figures(arguments.output_root, settings)
        rebuild_record(arguments.output_root, arguments.record, settings,
                       arguments.tier0_root)
    elif arguments.record_only:
        rebuild_record(arguments.output_root, arguments.record, settings,
                       arguments.tier0_root)
    else:
        run(arguments.output_root, arguments.record, settings,
            arguments.tier0_root)
    announce("done, record at {}".format(arguments.record))


if __name__ == "__main__":
    main()
