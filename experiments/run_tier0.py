# e1: the tier 0 run. all three solvers, all three phi, p0 and p1, over the seed
# list, at the gate budget, with one convergence check per problem at four times
# it. it writes the raw results, the three tables, the figures and the record.
# it interprets nothing; e3 does that, CONTEXT.md section 10 e3.
#
# what makes this script the calibration and not just a run. p1 is the only
# problem in the project whose phi-efficient sets are known exactly,
# docs/b1_phi_efficient_sets.md section 2.4, so it is the only place where the
# measurement can be checked against a known answer. table 1 below is that known
# answer computed from the closed forms, table 2 is the same quantity measured on
# recovered sets, and the difference between p1's row of each is the instrument's
# error, measured once, here. docs/plan_after_meeting.md sections a1 and b3.
#
# the number-provenance rule, CONTEXT.md section 10 e1, is why the record is
# generated. every number in docs/e1_tier0_run.md is read back out of a file this
# script wrote, and the record names the file and the key beside it. nothing is
# typed into the record, so re-running the script regenerates the record's numbers
# from the same seeds rather than leaving them to agree with the run on the day
# they were copied.
#
# what is run, and why the pair numbers come from one solver only. the pair
# statistics of table 2 are computed on random search alone, through
# src/metrics_decision.py's compare_phi_on_one_sample, which draws one uniform
# sample of the box, evaluates it once and filters it under each phi in turn, so
# the three sets differ only through the order. in nsga-ii and mopso phi drives
# the search as well as the ordering, so a difference between two of their runs
# is a difference of orders and of trajectories at once; they are run under every
# phi and reported in their own table as a question about how solvers behave
# under each order, and they are never the source of a pair number.
# docs/plan_after_meeting.md section b1, CONTEXT.md section 10 e3.
#
# the three tables, all written through src/reporting.py's save_metrics_table.
#   table_1_exact_p1.csv    the closed-form pair statistics of p1, from the
#                           lebesgue measures of b1 section 2.4's regions. no
#                           seed, no budget and no solver enter it.
#   table_2_measured.csv    the measured pair statistics, every problem and both
#                           budgets, on random search output, with the same-phi
#                           seed-to-seed noise floor beside them.
#   table_3_solvers.csv     the objective-space metrics per solver under a fixed
#                           phi, and the pair statistics of nsga-ii's and mopso's
#                           own output, which are about the solvers.
#
# three points where the fixed schema of d3 and the plan's table did not meet,
# recorded here and in the record rather than solved by widening d3, which is
# another subpart's file:
#   the noise floor is a row and not a column. plan section b3 gives table 2 two
#     noise-floor columns; d3's decision block has no column for them and adding
#     one is a change to d3. so a noise-floor row carries phi_a equal to phi_b,
#     and it is labelled a check, because the block note reserves the finding
#     label for the row that carries the sensitivity signal and a same-phi row
#     carries none by construction. its note says what it is.
#   the solver is a note and not a column, for the same reason and with no cost:
#     table 2 is random search throughout, so the column would be constant.
#   d2's compute_overlap is not the shared fraction of the union. it is the two
#     covered counts over the two cardinalities, which for uniformly sampled sets
#     tends to 2|A and B| / (|A| + |B|) and not to |A and B| / |A or B|. the two
#     differ: on p1 under example 2.2 against example 2.4 the first is 0.187 and
#     the second is 0.103. so table 1's overlap column is computed in d2's own
#     convention, which is what makes p1's two rows comparable, and the union
#     share that docs/meeting_2026_09_04.md section 4.3 reports is written beside
#     it in exact_regions_p1.csv under its own key. neither number is dropped and
#     the record names both.
#
# the hypervolume reference point, and the assertion CONTEXT.md section 10 e1
# puts here. moocore clips at the reference point instead of refusing, v-59, so a
# front row beyond the point contributes nothing and the number still comes back
# looking like a hypervolume. one point is therefore derived per problem and phi
# from every row that will be scored against it, across both budgets, all three
# solvers and all five seeds, together with the reference front where one exists,
# by the margin rule; every front is asserted to lie strictly inside it before it
# is scored, and a front that is not is refused rather than scored. pooling
# across budgets is what makes the convergence check a comparison of two
# hypervolumes and not of two different measurements.
# where a pooled column has zero range the margin is zero, the point cannot
# strictly dominate anything and every row's box has zero thickness, so the
# configuration is not scored and the reason is recorded. p0's image carries such
# a column under every phi: its first objective's lower endpoint is identically
# zero under examples 2.3 and 2.4 and its centre is identically zero under
# example 2.2.
#
# the free sets, and the two registered measurements. m-1 and m-2 of
# docs/plan_after_meeting.md section f4 and PROGRESS.md x-01 are computed here
# from artefacts this run already produces. which columns they are computed on is
# decided by the free set F_k of each image column, and the free sets are
# measured rather than asserted: each decision variable is resampled in turn and
# a column that does not move is a column that does not depend on it. a column
# that is constant is flagged and left out of the statistics, because the
# mechanism's hypothesis is a member that minimises the column strictly and a
# constant column has none.
#
# the raw results are written before any metric is computed, so a metric can be
# recomputed without re-running a solver, and the manifest names every array.
#
# no number is typed into this file that is not a run parameter or a constant of
# a derivation cited beside it. the closed-form regions are transcribed from
# docs/b1_phi_efficient_sets.md section 2.4 and their measures are integrated
# here in closed form; tests/test_run_tier0.py checks the results against the
# values docs/meeting_2026_09_04.md section 4.3 published from an independent
# quadrature and an 8000 by 8000 grid.

import argparse
import csv
import sys
import time
from pathlib import Path

import numpy as np

repository_root = Path(__file__).resolve().parent.parent
source_directory = repository_root / "src"
if str(source_directory) not in sys.path:
    sys.path.insert(0, str(source_directory))

from metrics_decision import (check_status, compare_phi_on_one_sample,
                              compute_coverage, compute_hausdorff, compute_overlap,
                              cross_evaluate, pair_note, pair_status, phi_pairs)
from metrics_objective import (compute_hv, compute_igd, compute_spread,
                               derive_reference_point, igd_reference,
                               nadir_margin_rule)
from phi_transforms import phi_registry
from problems_tier0 import p1_default_params, problem_registry
from random_search import SearchResult, phi_image
from reference_fronts import farthest_point_mode, weight_sample_seed
from reporting import (PlottedFront, PlottedSet, decision_block, format_value,
                       objective_block, plot_decision_sets, plot_fronts,
                       read_metrics_table, save_metrics_table,
                       summarize_across_seeds)
from runners import run_mopso, run_nsga2

# the three phi in the lu, ls, cw order of examples 2.2, 2.3 and 2.4 of [1],
# which is the order every table and every loop in the project uses.
phi_names = ("lu", "ls", "cw")

# the three solvers of slide 17. random search is the control and is in the grid
# on the same terms as the other two, CONTEXT.md section 10 c1.
solver_names = ("random_search", "nsga2", "mopso")

# the two tier 0 problems. p0 is the published anchor's problem and p1 is the
# fixture, docs/b1_phi_efficient_sets.md section 7.4.
problem_names = ("p0", "p1")

# the seed list, the population and the gate budget, all three the ones
# tests/test_validation.py ran the gate at. a run at a budget the gate did not
# pass would be a run behind an untested gate.
run_seeds = (11, 12, 13, 14, 15)
gate_pop_size = 100
gate_n_gen = 50
gate_budget = gate_pop_size * gate_n_gen

# the convergence check, one per problem: the whole grid re-measured at four
# times the budget, which is the multiple c3 reported its budget trend at. the
# check is the comparison of the two, and it is a comparison and not a second
# experiment because every configuration is repeated exactly, including the
# hypervolume reference point.
convergence_multiple = 4

# delta, stated as a fraction of the box diameter and never as an absolute
# number, docs/plan_after_meeting.md section b1: a fixed absolute delta means
# different things in a 2-box and in a 30-box. one twentieth is the scale
# src/metrics_decision.py takes as its own worked example on p1's box. it is
# fixed before the run and is not tuned afterwards.
delta_box_fraction = 0.05

# the fractions the coverage and overlap statistics are also computed at, so that
# their movement with delta is a measured artefact rather than a caveat. plan
# section b2 lists the appearance of a tolerance as one of the five things lost
# between the exact number and the measured one.
delta_sweep_fractions = (0.0, 0.01, 0.02, delta_box_fraction, 0.10, 0.20)

# zero is in that list and it is not a limiting case here. the three sets of one
# random-search comparison are three index sets over one array, so two decision
# vectors are the same point bitwise or they are two points, and no tolerance is
# needed to decide it: at delta zero the coverage is exactly the shared count over
# the count, which is the measured counterpart of the exact statement with the
# tolerance removed rather than made small. a positive delta is needed only where
# two different samples are compared, which is the noise floor and the population
# solvers' own pairs, and there it is needed absolutely, two independent uniform
# samples sharing no point at all.
zero_delta = 0.0

# the igd reference front. the size is the one tests/test_runners.py and the gate
# use; the mode is b2-b's correction, r-13, because igd averages over reference
# points and the dirichlet draw's density in objective space is the
# parametrisation's; the seed is src/reference_fronts.py's own. both settings of
# the singular flag are computed, since s-12 leaves the status of those points
# undecided and the two settings are two different reference objects.
reference_points = 1000
reference_sampling_mode = farthest_point_mode
reference_seed = weight_sample_seed
singular_settings = (False, True)

# the hypervolume reference point rule. the margin rule and not the strict nadir,
# CONTEXT.md section 10 e1: the strict nadir puts the point on the extremes of the
# rows it is derived from, and a row on an extreme is then clipped.
hv_rule = nadir_margin_rule

# how the free sets are measured: one resampling of each decision variable over a
# sample of this size at this seed. it is a structural property and not a
# reporting parameter, so it takes a fixed seed and is not summarised over seeds.
dependence_points = 512
dependence_seed = 20260905

# m-1's tail, PROGRESS.md x-01: the fraction of the thirty smallest under a column
# that survive the filter, against the chance rate.
tail_rank_count = 30

# the projections of the derived phi-efficient sets onto each decision variable,
# per problem and phi, as closed intervals. p1's are read off the regions of
# docs/b1_phi_efficient_sets.md section 2.4: X_lu spans x_1 in [0, 4/3] and x_2 in
# [4/5, 4/3], X_ls spans [0, 4/3] in both, X_cw spans [0, 1] in both. p0's are
# section 7.4's: the optimal set is the whole decision box under examples 2.2 and
# 2.3 and the single point x = 0 under example 2.4. m-2 measures a distance to
# these and to nothing else.
four_fifths = 4.0 / 5.0
four_thirds = 4.0 / 3.0
efficient_projections = {
    ("p0", "lu"): ((-1.0, 1.0),),
    ("p0", "ls"): ((-1.0, 1.0),),
    ("p0", "cw"): ((0.0, 0.0),),
    ("p1", "lu"): ((0.0, four_thirds), (four_fifths, four_thirds)),
    ("p1", "ls"): ((0.0, four_thirds), (0.0, four_thirds)),
    ("p1", "cw"): ((0.0, 1.0), (0.0, 1.0)),
}

# the column pairs the objective-space figures project onto. the 2m columns come
# in the order (Lambda_1^T f, B_1^T f, Lambda_2^T f, B_2^T f), so (0, 2) is the
# two first image coordinates against each other and (1, 3) the two second ones,
# which keeps each panel within one image coordinate of the transform and never
# plots a first coordinate against a second.
figure_col_pairs = ((0, 2), (1, 3))

# the two registered measurements, named as PROGRESS.md x-01 names them
tail_lift_name = "m-1_tail_survival_lift"
overhang_name = "m-2_overhang"


# the run parameters of one invocation, so that no function reads a global budget
def run_settings(seeds, budgets, pop_size, n_reference_points):
    return {"seeds": tuple(int(seed) for seed in seeds),
            "budgets": tuple(int(budget) for budget in budgets),
            "pop_size": int(pop_size),
            "reference_points": int(n_reference_points)}


# the parameters one problem is evaluated at, p1's being a1-b's and d-01's
def problem_parameters(problem):
    return dict(p1_default_params) if problem.name == "p1" else None


# the euclidean diameter of a problem's decision box, the scale delta is stated in
def box_diameter(problem):
    lower, upper = problem.bounds()
    return float(np.sqrt(np.sum(np.square(np.asarray(upper) - np.asarray(lower)))))


# the absolute delta of one problem, the stated fraction of its box diameter
def problem_delta(problem, fraction=delta_box_fraction):
    return float(fraction) * box_diameter(problem)


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
    print("[e1] {}".format(message), flush=True)


# the antiderivative of the lower arc of b1 section 2.4, read in u = 4 - x_2
def lower_arc_antiderivative(u):
    # the lower boundary of X_lu is x_1 = (20 x_2 - 16) / (4 - x_2), and
    # 64 ln(4 - x_2) - 20 (4 - x_2) differentiates to minus it, so the integral of
    # the arc from a to b is this function at 4 - a minus this function at 4 - b.
    return 64.0 * np.log(u) - 20.0 * u


# the integral of b1 section 2.4's lower arc over an interval of x_2
def lower_arc_area(x_2_from, x_2_to):
    return float(lower_arc_antiderivative(4.0 - x_2_from)
                 - lower_arc_antiderivative(4.0 - x_2_to))


# the antiderivative of the upper arc of b1 section 2.4, read in u = 7 x_2 - 4
def upper_arc_antiderivative(u):
    # the upper boundary of X_lu and of X_ls is x_1 = (16 - 12 x_2) / (7 x_2 - 4),
    # whose antiderivative in x_2 is (64 ln u - 12 u) / 49 with u = 7 x_2 - 4.
    return (64.0 * np.log(u) - 12.0 * u) / 49.0


# the integral of b1 section 2.4's upper arc over an interval of x_2
def upper_arc_area(x_2_from, x_2_to):
    return float(upper_arc_antiderivative(7.0 * x_2_to - 4.0)
                 - upper_arc_antiderivative(7.0 * x_2_from - 4.0))


# the lebesgue measure of each of b1 section 2.4's three derived regions
def derived_areas():
    # X_lu is bounded below by the lower arc on x_2 in [4/5, 1] and above by the
    # upper arc on [1, 4/3]; X_ls is the rectangle [0, 4/3] x [0, 1] together with
    # the same upper arc over [1, 4/3]; X_cw is the unit square. the segments b1
    # excludes are one-dimensional and carry no measure.
    area_lu = lower_arc_area(four_fifths, 1.0) + upper_arc_area(1.0, four_thirds)
    area_ls = four_thirds + upper_arc_area(1.0, four_thirds)
    return {"lu": area_lu, "ls": area_ls, "cw": 1.0}


# the lebesgue measure of the intersection of X_lu and X_cw
def lu_cw_intersection_area():
    # intersecting X_lu with [0, 1]^2 keeps x_2 in [4/5, 1], where the binding
    # boundary is the lower arc, and caps x_1 at 1, which binds from x_2 = 20/21
    # since the arc reaches 1 there. b1 section 2.4 and
    # docs/meeting_2026_09_04.md section 4.3 give the closed form 64 ln(21/20) - 3.
    crossing = 20.0 / 21.0
    return lower_arc_area(four_fifths, crossing) + (1.0 - crossing)


# the pairwise intersection measures of the three derived regions
def derived_intersections(areas):
    # ND_lu and ND_cw both sit inside ND_ls exactly and for every problem,
    # docs/a_close_containment.md, and b1 section 2.4's regions carry the
    # containment: X_lu and X_cw are subsets of X_ls, so those two intersections
    # are the contained region itself and only the lu against cw pair is free in
    # both directions.
    return {("lu", "ls"): areas["lu"], ("lu", "cw"): lu_cw_intersection_area(),
            ("ls", "cw"): areas["cw"]}


# the exact pair statistics of one pair of derived regions
def exact_pair_statistics(area_a, area_b, shared):
    # coverage is the share of one region lying in the other, which is the
    # quantity d2's compute_coverage tends to at delta zero on a uniform sample.
    # two overlap conventions are returned because they are two different
    # quantities: d2's compute_overlap is the second, and the shared fraction of
    # the union is the first, which is what docs/meeting_2026_09_04.md
    # section 4.3 reports.
    return {"coverage_a_in_b": shared / area_a, "coverage_b_in_a": shared / area_b,
            "overlap_union_share": shared / (area_a + area_b - shared),
            "overlap_d2_convention": 2.0 * shared / (area_a + area_b)}


# every exact quantity of p1's derived regions, as one long-format table
def exact_region_rows():
    areas = derived_areas()
    intersections = derived_intersections(areas)
    rows = [{"quantity": "area", "phi_a": name, "phi_b": "", "value": areas[name]}
            for name in phi_names]
    for phi_a, phi_b in phi_pairs:
        shared = intersections[(phi_a, phi_b)]
        rows.append({"quantity": "intersection_area", "phi_a": phi_a,
                     "phi_b": phi_b, "value": shared})
        statistics = exact_pair_statistics(areas[phi_a], areas[phi_b], shared)
        for name in sorted(statistics):
            rows.append({"quantity": name, "phi_a": phi_a, "phi_b": phi_b,
                         "value": statistics[name]})
    return rows


# the note the exact table's rows carry, saying what the row is and is not
def exact_note(phi_a, phi_b):
    return ("exact lebesgue measure of b1 section 2.4's derived regions; no seed, "
            "no budget, no solver and no tolerance enter it, so the seed count, "
            "the budget and the two cardinalities are written as zero. overlap is "
            "d2's convention, twice the shared measure over the sum of the two, so "
            "that this row and p1's row of table 2 are the same quantity; the "
            "shared fraction of the union is in exact_regions_p1.csv. "
            + pair_note(phi_a, phi_b))


# table 1, the exact pair statistics of p1, in d3's decision block
def exact_table_rows(problem):
    areas = derived_areas()
    intersections = derived_intersections(areas)
    rows = []
    for phi_a, phi_b in phi_pairs:
        statistics = exact_pair_statistics(areas[phi_a], areas[phi_b],
                                           intersections[(phi_a, phi_b)])
        for metric in ("coverage_a_in_b", "coverage_b_in_a"):
            rows.append(exact_table_row(problem, phi_a, phi_b, metric,
                                        statistics[metric]))
        rows.append(exact_table_row(problem, phi_a, phi_b, "overlap",
                                    statistics["overlap_d2_convention"]))
    return rows


# one row of table 1, with the fields a measured row would carry set to zero
def exact_table_row(problem, phi_a, phi_b, metric, value):
    return {"problem": problem.name, "phi_a": phi_a, "phi_b": phi_b,
            "status": pair_status(phi_a, phi_b), "metric": metric, "n_seeds": 0,
            "n_evals": 0, "cardinality_a": 0, "cardinality_b": 0, "delta": 0.0,
            "box_scale": box_diameter(problem), "containment_violations": None,
            "note": exact_note(phi_a, phi_b), "median": value, "q1": value,
            "q3": value, "iqr": 0.0}


# the fronts of one filtered sample, one per phi, from a single evaluation
def sample_fronts(problem, params, sample):
    # the isolation of src/random_search.py's filter_one_sample_under_every_phi is
    # carried through to the fronts: the problem is evaluated once and each phi's
    # front is that evaluation's image at that phi's index set, so the three
    # fronts of one seed differ only through the order. this is the same object
    # run_random_search would return at the same seed, the sample being a pure
    # function of the box, the budget and the seed, and it is built here so that
    # one seed costs one filter pass rather than two.
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


# nsga-ii's and mopso's runs on one problem under one phi at one budget
def solver_runs(problem, phi_name, params, budget, seeds, pop_size):
    # the budget is spent in evaluations and the generation count follows from it,
    # so both solvers spend exactly the stated budget, src/runners.py.
    n_gen = int(budget) // int(pop_size)
    return {"nsga2": run_nsga2(problem, phi_name, params, n_gen, pop_size, seeds),
            "mopso": run_mopso(problem, phi_name, params, n_gen, pop_size, seeds)}


# every run of the grid, with the random-search comparisons the pair table reads
def execute_grid(settings):
    runs, comparisons = {}, {}
    for problem_name in problem_names:
        problem = problem_registry[problem_name]
        params = problem_parameters(problem)
        delta = problem_delta(problem)
        for budget in settings["budgets"]:
            announce("running {} at budget {}".format(problem_name, budget))
            found, results = random_search_runs(problem, params, budget,
                                                settings["seeds"], delta)
            comparisons[(problem_name, budget)] = found
            for name in phi_names:
                runs[(problem_name, "random_search", name, budget)] = results[name]
                for solver, found_runs in solver_runs(
                        problem, name, params, budget, settings["seeds"],
                        settings["pop_size"]).items():
                    runs[(problem_name, solver, name, budget)] = found_runs
    return runs, comparisons


# the file one configuration's raw arrays are written to
def raw_path(root, key):
    problem_name, solver, phi_name, budget = key
    return root / "raw" / "{}_{}_{}_{}.npz".format(problem_name, solver, phi_name,
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
        problem_name, solver, phi_name, budget = key
        for result in runs[key]:
            rows.append({"problem": problem_name, "solver": solver, "phi": phi_name,
                         "n_evals": result.n_evals, "seed": result.seed,
                         "cardinality": int(len(result.front)),
                         "n_columns": int(result.front.shape[1]),
                         "file": path.relative_to(root).as_posix()})
    write_table(root / "raw" / "manifest.csv",
                ("problem", "solver", "phi", "n_evals", "seed", "cardinality",
                 "n_columns", "file"), rows)
    return rows


# the 2m image columns of one problem under one phi, at a stated sample
def image_columns(problem, params, phi_name, x):
    return phi_image(problem, problem.evaluate(x, params), phi_registry[phi_name])


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


# the free set of every image column of every problem and phi, as table rows
def free_set_rows(settings):
    rows = []
    for problem_name in problem_names:
        problem = problem_registry[problem_name]
        params = problem_parameters(problem)
        for phi_name in phi_names:
            depends, constant = column_dependence(problem, params, phi_name,
                                                  dependence_points, dependence_seed)
            for column in range(depends.shape[0]):
                free = [str(index) for index in range(problem.n_vars)
                        if not depends[column, index]]
                rows.append({"problem": problem_name, "phi": phi_name,
                             "column": column, "depends_on": " ".join(
                                 str(index) for index in range(problem.n_vars)
                                 if depends[column, index]),
                             "free_set": " ".join(free),
                             "free_set_size": len(free),
                             "constant_column": bool(constant[column])})
    return rows


# a flag as a boolean, whether it arrives as one or as the text a csv holds
def as_bool(value):
    return value == "True" if isinstance(value, str) else bool(value)


# the free set of one column, read back out of the free-set rows
def free_set_of(rows, problem_name, phi_name, column):
    for row in rows:
        if (row["problem"], row["phi"], int(row["column"])) == (problem_name,
                                                               phi_name, column):
            return ([int(index) for index in row["free_set"].split()],
                    as_bool(row["constant_column"]))
    raise KeyError("no free set recorded for {} {} column {}"
                   .format(problem_name, phi_name, column))


# m-1 for one column of one filtered sample: the tail's survival against chance
def tail_survival_lift(sample, phi_name, column, columns, n_evals):
    # x-01's measurement, unchanged: the sample is ordered ascending by the
    # column, s_30 is the fraction of the thirty smallest that survive the filter
    # under that phi, the chance rate is the front's size over the budget, and the
    # lift is their ratio.
    keep = set(int(index) for index in sample.indices[phi_name].tolist())
    order = np.argsort(columns[:, column], kind="stable")[:tail_rank_count]
    survived = sum(1 for index in order.tolist() if index in keep)
    chance = len(sample.indices[phi_name]) / float(n_evals)
    return float(survived / len(order)) / chance, float(survived / len(order)), chance


# the distance from a point to a box, zero inside it
def interval_distance(values, intervals):
    gaps = [max(low - value, 0.0, value - high)
            for value, (low, high) in zip(values, intervals)]
    return float(np.sqrt(np.sum(np.square(gaps)))) if gaps else 0.0


# m-2 for one column: how far the protected member lies outside the derived set
def column_overhang(sample, problem_name, phi_name, column, columns, free):
    # x-01's measurement: the argmin of the column in that seed's sample is the
    # protected member, and the overhang is the distance from its free
    # coordinates to the projection of the known efficient structure onto them.
    # where the free set is empty the distance is over no coordinates and is zero
    # by construction, which is the case the prediction calls absent.
    protected = int(np.argmin(columns[:, column]))
    point = sample.decision_vectors[protected]
    intervals = [efficient_projections[(problem_name, phi_name)][index]
                 for index in free]
    return interval_distance([point[index] for index in free], intervals), protected


# both registered measurements over one problem, phi and budget, per seed
def registered_rows_for(comparisons, problem, params, phi_name, free_rows, budget):
    rows = []
    for comparison in comparisons:
        sample = comparison.sample
        columns = image_columns(problem, params, phi_name, sample.decision_vectors)
        for column in range(columns.shape[1]):
            free, constant = free_set_of(free_rows, problem.name, phi_name, column)
            rows.extend(registered_rows_for_column(sample, comparison, problem,
                                                   phi_name, column, columns, free,
                                                   constant, budget))
    return rows


# the two measurements of one column at one seed, with what is not defined marked
def registered_rows_for_column(sample, comparison, problem, phi_name, column,
                               columns, free, constant, budget):
    shared = {"problem": problem.name, "phi": phi_name, "column": column,
              "free_set_size": len(free), "constant_column": constant,
              "n_evals": int(budget), "seed": int(comparison.seed)}
    if constant:
        return [dict(shared, measurement=name, value=None,
                     defined=False) for name in (tail_lift_name, overhang_name)]
    lift, tail_share, chance = tail_survival_lift(sample, phi_name, column, columns,
                                                 budget)
    overhang, protected = column_overhang(sample, problem.name, phi_name, column,
                                          columns, free)
    return [dict(shared, measurement=tail_lift_name, value=lift, defined=True,
                 tail_share=tail_share, chance_rate=chance, protected_index=protected),
            dict(shared, measurement=overhang_name, value=overhang, defined=True,
                 tail_share=tail_share, chance_rate=chance, protected_index=protected)]


# every per-seed value of m-1 and m-2, over both budgets and every problem and phi
def registered_measurement_rows(comparisons, free_rows, settings):
    rows = []
    for problem_name in problem_names:
        problem = problem_registry[problem_name]
        params = problem_parameters(problem)
        for budget in settings["budgets"]:
            for phi_name in phi_names:
                rows.extend(registered_rows_for(comparisons[(problem_name, budget)],
                                                problem, params, phi_name, free_rows,
                                                budget))
    return [dict({"tail_share": None, "chance_rate": None, "protected_index": None},
                 **row) for row in rows]


# the median and interquartile range of each registered measurement over the seeds
def registered_summary_rows(rows):
    summary = []
    keys = sorted({(row["problem"], row["phi"], row["column"], row["n_evals"],
                    row["measurement"]) for row in rows})
    for problem_name, phi_name, column, budget, measurement in keys:
        values = [row["value"] for row in rows
                  if (row["problem"], row["phi"], row["column"], row["n_evals"],
                      row["measurement"]) == (problem_name, phi_name, column,
                                              budget, measurement) and row["defined"]]
        first = next(row for row in rows
                     if (row["problem"], row["phi"], row["column"]) == (
                         problem_name, phi_name, column))
        entry = {"problem": problem_name, "phi": phi_name, "column": column,
                 "n_evals": budget, "measurement": measurement,
                 "free_set_size": first["free_set_size"],
                 "constant_column": first["constant_column"],
                 "defined": bool(values)}
        entry.update(summarize_across_seeds(values) if values else
                     {"n_seeds": 0, "median": None, "q1": None, "q3": None,
                      "iqr": None})
        # the mean and the spread of the mean as well as the median, because
        # x-01's refuting measurement is stated on the mean over seeds: on p1
        # under example 2.4 it is predicted to equal 1/8 to within the seed
        # spread, and a median cannot be read against that constant.
        entry.update(mean_and_spread(values))
        summary.append(entry)
    return summary


# the mean over seeds and the standard error the prediction is read against
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
            "cross_a_under_b": pair.cross_a_under_b,
            "cross_b_under_a": pair.cross_b_under_a}


# every per-seed decision-space value of the random-search pair comparisons
def decision_rows_by_seed(comparisons, problem_name, budget):
    rows = []
    for comparison in comparisons:
        for pair in comparison.pairs:
            for metric, value in pair_values(pair).items():
                rows.append({"problem": problem_name, "solver": "random_search",
                             "phi_a": pair.phi_a, "phi_b": pair.phi_b,
                             "status": pair.status, "metric": metric,
                             "n_evals": int(budget), "seed": int(comparison.seed),
                             "cardinality_a": pair.n_a, "cardinality_b": pair.n_b,
                             "delta": comparison.delta,
                             "containment_violations": pair.containment_violations,
                             "value": value})
    return rows


# the three delta-dependent pair statistics of one comparison at a stated delta
def pair_rows_at_delta(comparison, problem_name, budget, delta):
    # the same statistics compare_phi_on_one_sample returns, recomputed at a second
    # delta from the sets it already filtered. the metrics that do not move with
    # delta, the three hausdorff distances and the two cross evaluations, are not
    # repeated: they are one number per pair and they are already in the rows the
    # comparison produced.
    rows = []
    vectors = comparison.sample.decision_vectors
    for phi_a, phi_b in phi_pairs:
        set_a = vectors[comparison.sample.indices[phi_a]]
        set_b = vectors[comparison.sample.indices[phi_b]]
        values = {"coverage_a_in_b": compute_coverage(set_a, set_b, delta),
                  "coverage_b_in_a": compute_coverage(set_b, set_a, delta),
                  "overlap": compute_overlap(set_a, set_b, delta)}
        rows.extend({"problem": problem_name, "solver": "random_search",
                     "phi_a": phi_a, "phi_b": phi_b,
                     "status": pair_status(phi_a, phi_b), "metric": metric,
                     "n_evals": int(budget), "seed": int(comparison.seed),
                     "cardinality_a": len(set_a), "cardinality_b": len(set_b),
                     "delta": float(delta),
                     "containment_violations": None, "value": value}
                    for metric, value in values.items())
    return rows


# the same coverage statistic between two seeds of one phi, the instrument's floor
def noise_floor_rows(comparisons, problem_name, budget):
    # docs/plan_after_meeting.md section b1: a cross-phi number that does not
    # exceed the seed-to-seed disagreement of the same phi is not evidence of
    # anything. each seed is paired with the next one cyclically, so there is one
    # value per seed and the summary over them is a summary over the seed count
    # the row states.
    rows = []
    for phi_name in phi_names:
        sets = [comparison.sample.decision_vectors[comparison.sample.indices[phi_name]]
                for comparison in comparisons]
        for index, comparison in enumerate(comparisons):
            other = (index + 1) % len(comparisons)
            rows.extend(noise_floor_values(sets[index], sets[other], phi_name,
                                           problem_name, budget, comparison))
    return rows


# the three pair statistics between two same-phi seeds, as per-seed rows
def noise_floor_values(set_a, set_b, phi_name, problem_name, budget, comparison):
    delta = comparison.delta
    values = {"coverage_a_in_b": compute_coverage(set_a, set_b, delta),
              "coverage_b_in_a": compute_coverage(set_b, set_a, delta),
              "overlap": compute_overlap(set_a, set_b, delta)}
    return [{"problem": problem_name, "solver": "random_search_noise_floor",
             "phi_a": phi_name, "phi_b": phi_name, "status": check_status,
             "metric": metric, "n_evals": int(budget), "seed": int(comparison.seed),
             "cardinality_a": len(set_a), "cardinality_b": len(set_b),
             "delta": delta, "containment_violations": None, "value": value}
            for metric, value in values.items()]


# the pair statistics of one population solver's own output, per seed
def solver_pair_rows(runs, problem, params, solver, budget, delta):
    rows = []
    for phi_a, phi_b in phi_pairs:
        runs_a = runs[(problem.name, solver, phi_a, budget)]
        runs_b = runs[(problem.name, solver, phi_b, budget)]
        for result_a, result_b in zip(runs_a, runs_b):
            values = solver_pair_values(result_a, result_b, phi_a, phi_b, problem,
                                        params, delta)
            rows.extend({"problem": problem.name, "solver": solver, "phi_a": phi_a,
                         "phi_b": phi_b, "status": pair_status(phi_a, phi_b),
                         "metric": metric, "n_evals": int(budget),
                         "seed": int(result_a.seed),
                         "cardinality_a": len(result_a.decision_vectors),
                         "cardinality_b": len(result_b.decision_vectors),
                         "delta": delta, "containment_violations": None,
                         "value": value} for metric, value in values.items())
    return rows


# the eight metrics between two decision sets a solver returned under two phi
def solver_pair_values(result_a, result_b, phi_a, phi_b, problem, params, delta):
    set_a, set_b = result_a.decision_vectors, result_b.decision_vectors
    hausdorff = compute_hausdorff(set_a, set_b)
    return {"hausdorff_a_to_b": hausdorff.a_to_b,
            "hausdorff_b_to_a": hausdorff.b_to_a,
            "hausdorff_symmetric": hausdorff.symmetric,
            "coverage_a_in_b": compute_coverage(set_a, set_b, delta),
            "coverage_b_in_a": compute_coverage(set_b, set_a, delta),
            "overlap": compute_overlap(set_a, set_b, delta),
            "cross_a_under_b": cross_evaluate(set_a, phi_b, problem, params),
            "cross_b_under_a": cross_evaluate(set_b, phi_a, problem, params)}


# the note a measured pair row carries, naming the solver, the delta and the pair
def measured_note(phi_a, phi_b, solver, delta, fraction, containment_note):
    scale = ("delta is zero, so the row is the shared count over the count, with "
             "no tolerance in it at all; the three sets are index sets over one "
             "array, so two vectors are the same point bitwise or they are two "
             "points" if delta == zero_delta else
             "delta is {} of the box diameter, the box_scale column"
             .format(repr(float(fraction))))
    return ("{}; {}; containment_violations is the largest count over the seeds; {}"
            .format(solver_note(solver), scale, containment_note))


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


# the key a decision-space table row is summarised over its seeds by
def decision_group_key(row):
    return (row["problem"], row["solver"], row["phi_a"], row["phi_b"],
            row["metric"], row["n_evals"], row["delta"])


# the decision-block rows of a table, one per group, summarised over the seeds
def decision_table_rows(by_seed, fraction=delta_box_fraction):
    rows = []
    for key in sorted({decision_group_key(row) for row in by_seed}):
        group = [row for row in by_seed if decision_group_key(row) == key]
        problem_name, solver, phi_a, phi_b, metric, budget, delta = key
        row = {"problem": problem_name, "phi_a": phi_a, "phi_b": phi_b,
               "status": group[0]["status"], "metric": metric,
               "n_evals": budget,
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
        rows.append(row)
    return rows


# the largest containment violation count over a group's seeds, absent where none
def violation_count(group):
    counts = [item["containment_violations"] for item in group
              if item["containment_violations"] is not None]
    return int(max(counts)) if counts else None


# the coverage and overlap statistics at a range of delta, as raw rows
def delta_sweep_rows(comparisons, problem, budget):
    # delta is a reporting parameter and the numbers move with it,
    # docs/plan_after_meeting.md section b2, so its movement is measured here
    # rather than left as a caveat. it is computed at the reported budget only.
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
                                               phi_a, phi_b, budget))
    return rows


# the three delta-dependent statistics of one pair at one delta
def delta_sweep_values(set_a, set_b, delta, fraction, comparison, problem, phi_a,
                       phi_b, budget):
    values = {"coverage_a_in_b": compute_coverage(set_a, set_b, delta),
              "coverage_b_in_a": compute_coverage(set_b, set_a, delta),
              "overlap": compute_overlap(set_a, set_b, delta)}
    return [{"problem": problem.name, "phi_a": phi_a, "phi_b": phi_b,
             "status": pair_status(phi_a, phi_b), "metric": metric,
             "n_evals": int(budget), "seed": int(comparison.seed),
             "delta_box_fraction": fraction, "delta": delta,
             "box_scale": box_diameter(problem), "cardinality_a": len(set_a),
             "cardinality_b": len(set_b), "value": value}
            for metric, value in values.items()]


# every reference front of one problem and phi, one per setting of the singular flag
def reference_fronts_for(problem, phi_name, params, n_points):
    # a reference front exists for p1 alone, docs/b1_phi_efficient_sets.md
    # section 7.4: under examples 2.2 and 2.3 p0's optimal set is the whole
    # decision box and under example 2.4 it is one point, so an igd against it
    # measures nothing about finding an efficient set.
    if problem.name != "p1":
        return {}
    return {flag: igd_reference(problem, phi_name, n_points, flag,
                                reference_sampling_mode, params, reference_seed)
            for flag in singular_settings}


# every row that will be scored under one problem and phi, at every budget
def scored_rows(runs, problem_name, phi_name, settings):
    return [result.front
            for solver in solver_names
            for budget in settings["budgets"]
            for result in runs[(problem_name, solver, phi_name, budget)]]


# the one hypervolume reference point of a problem and phi, or why there is none
def hypervolume_point(rows, references):
    # derived from every row it will be scored against, across both budgets, all
    # three solvers and all five seeds, together with the reference fronts where
    # they exist, so that one point serves the whole comparison and the two
    # budgets are two hypervolumes of one measurement. where a pooled column has
    # zero range the margin rule adds nothing to the nadir there, no point can
    # strictly dominate the rows and every box has zero thickness, so no
    # hypervolume is scored and the reason is returned instead.
    pooled = np.concatenate(list(rows) + [reference.front
                                          for reference in references], axis=0)
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
def objective_rows_by_seed(results, problem_name, phi_name, solver, budget, point,
                           scorable, references):
    rows = []
    for result in results:
        shared = {"problem": problem_name, "phi": phi_name, "solver": solver,
                  "n_evals": int(budget), "seed": int(result.seed),
                  "cardinality": int(len(result.front))}
        rows.append(dict(shared, metric="spread", reference_size=0,
                         include_singular_segments=False,
                         value=compute_spread(result.front)))
        if scorable:
            require_dominating_point(point.point, result.front,
                                     "{} {} {} at budget {} seed {}".format(
                                         problem_name, phi_name, solver, budget,
                                         result.seed))
            rows.append(dict(shared, metric="hypervolume", reference_size=0,
                             include_singular_segments=False,
                             value=compute_hv(result.front, point.point)))
        for flag, reference in references.items():
            rows.append(dict(shared, metric="igd",
                             reference_size=len(reference.front),
                             include_singular_segments=flag,
                             value=compute_igd(result.front, reference.front)))
    return rows


# every per-seed objective-space value, with the points the hypervolumes used
def objective_values(runs, settings):
    rows, points = [], {}
    for problem_name in problem_names:
        problem = problem_registry[problem_name]
        params = problem_parameters(problem)
        for phi_name in phi_names:
            references = reference_fronts_for(problem, phi_name, params,
                                              settings["reference_points"])
            point, scorable, reason = hypervolume_point(
                scored_rows(runs, problem_name, phi_name, settings),
                list(references.values()))
            points[(problem_name, phi_name)] = (point, scorable, reason)
            for solver in solver_names:
                for budget in settings["budgets"]:
                    rows.extend(objective_rows_by_seed(
                        runs[(problem_name, solver, phi_name, budget)], problem_name,
                        phi_name, solver, budget, point, scorable, references))
    return rows, points


# the key an objective-space table row is summarised over its seeds by
def objective_group_key(row):
    return (row["problem"], row["phi"], row["solver"], row["metric"],
            row["n_evals"], row["reference_size"], row["include_singular_segments"])


# the objective-block rows of the solver table, summarised over the seeds
def objective_table_rows(by_seed, points):
    rows = []
    for key in sorted({objective_group_key(row) for row in by_seed}, key=repr):
        group = [row for row in by_seed if objective_group_key(row) == key]
        problem_name, phi_name, solver, metric, budget, size, flag = key
        point = points[(problem_name, phi_name)][0]
        row = {"problem": problem_name, "phi": phi_name, "solver": solver,
               "metric": metric, "n_evals": budget,
               "cardinality": int(np.median([item["cardinality"]
                                             for item in group])),
               "reference_size": size, "sampling_mode": reference_sampling_mode,
               "include_singular_segments": flag, "hv_reference_rule": hv_rule,
               "hv_reference_point": point.point}
        row.update(summarize_across_seeds([item["value"] for item in group]))
        rows.append(row)
    return rows


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


# the three solvers' fronts in one phi's image, one figure per problem and phi
def front_figures(root, runs, budget):
    paths = []
    for problem_name in problem_names:
        for phi_name in phi_names:
            fronts = [pooled_front(runs, (problem_name, solver, phi_name, budget),
                                   solver) for solver in solver_names]
            path = figure_root(root) / "fronts_{}_{}_{}.png".format(
                problem_name, phi_name, budget)
            plot_fronts(fronts, figure_col_pairs,
                        "{} under phi_{}, the three solvers".format(problem_name,
                                                                    phi_name),
                        path)
            paths.append(path)
    return paths


# one solver's decision sets under the three phi, at one seed, largest first
def single_seed_sets(runs, problem_name, solver, budget, seed_index=0):
    # one seed and not the five pooled, and the three ordered by decreasing size.
    # both are about what the figure shows rather than about what was measured:
    # five seeds of random search put twenty thousand points on the plane and bury
    # b1's derived boundaries under them, and drawing the sets in the registry's
    # order hides X_lu entirely, ND_lu sitting inside ND_ls. the legend carries the
    # seed count and the cardinality of each series, so nothing is concealed by
    # either choice, and every number is in the tables and not in the figure.
    sets = []
    for phi_name in phi_names:
        result = runs[(problem_name, solver, phi_name, budget)][seed_index]
        sets.append(PlottedSet(
            label="phi_{}".format(phi_name), problem_name=problem_name,
            phi_name=phi_name, n_seeds=1, n_evals=result.n_evals,
            points=result.decision_vectors))
    return sorted(sets, key=lambda item: -len(item.points))


# the recovered decision sets over b1's derived regions, one figure per solver
def decision_figures(root, runs, budgets):
    # p1 only: the figure is the plane the derived regions live in, and p0 has one
    # decision variable, so src/reporting.py refuses it and is right to.
    paths = []
    for budget in budgets:
        for solver in solver_names:
            path = figure_root(root) / "decision_sets_p1_{}_{}.png".format(solver,
                                                                          budget)
            plot_decision_sets(single_seed_sets(runs, "p1", solver, budget),
                               "p1, {}, the three phi over b1's derived regions"
                               .format(solver), path)
            paths.append(path)
    return paths


# every figure of the run, each one carrying its own budget and seed count
def all_figures(root, runs, settings):
    paths = []
    for budget in settings["budgets"]:
        paths.extend(front_figures(root, runs, budget))
    paths.extend(decision_figures(root, runs, settings["budgets"]))
    return paths


# one key of the summary file, with the file a reader should check it against
def summary_row(key, value, source):
    return {"key": key, "value": value, "source": source}


# the run parameters, one key each, as the record reads them back
def summary_parameters(settings):
    return [summary_row("seeds", " ".join(str(seed) for seed in settings["seeds"]),
                        "run parameter"),
            summary_row("n_seeds", len(settings["seeds"]), "run parameter"),
            summary_row("budgets", " ".join(str(budget)
                                            for budget in settings["budgets"]),
                        "run parameter"),
            summary_row("pop_size", settings["pop_size"], "run parameter"),
            summary_row("delta_box_fraction", delta_box_fraction, "run parameter"),
            summary_row("reference_points", settings["reference_points"],
                        "run parameter"),
            summary_row("reference_sampling_mode", reference_sampling_mode,
                        "run parameter"),
            summary_row("reference_seed", reference_seed, "run parameter"),
            summary_row("hv_reference_rule", hv_rule, "run parameter"),
            summary_row("dependence_points", dependence_points, "run parameter"),
            summary_row("dependence_seed", dependence_seed, "run parameter"),
            summary_row("tail_rank_count", tail_rank_count, "run parameter")]


# each problem's box scale and the absolute delta the fraction gives on it
def summary_scales():
    rows = []
    for problem_name in problem_names:
        problem = problem_registry[problem_name]
        rows.append(summary_row("box_scale_{}".format(problem_name),
                                box_diameter(problem), "the problem's bounds"))
        rows.append(summary_row("delta_{}".format(problem_name),
                                problem_delta(problem), "run parameter"))
    return rows


# the tables written and whether each problem and phi was scored a hypervolume
def summary_artefacts(tables, points):
    rows = [summary_row("table_{}".format(name), path.name, "written here")
            for name, path in sorted(tables.items())]
    for key in sorted(points):
        _, scorable, reason = points[key]
        rows.append(summary_row("hypervolume_scored_{}_{}".format(*key), scorable,
                                reason or "the point dominates every scored row"))
    return rows


# the run parameters and counts, as the keys the record reads its prose from
def summary_rows(settings, runs, tables, points, elapsed):
    counts = [summary_row("n_configurations", len(runs), "the run grid"),
              summary_row("n_runs", sum(len(value) for value in runs.values()),
                          "the run grid"),
              summary_row("wall_seconds", elapsed, "the run grid")]
    return (summary_parameters(settings) + counts + summary_scales()
            + summary_artefacts(tables, points))


# the gap between p1's exact pair statistic and the measured one, per pair and metric
def instrument_error_rows(exact_rows, measured_rows, budget):
    # the calibration's whole point, docs/plan_after_meeting.md section b3: p1's
    # row of table 1 and p1's row of table 2 are the same quantity derived and
    # measured, so their difference is the instrument's error, and p1 is the only
    # problem where it can be computed at all.
    rows = []
    for exact in exact_rows:
        for measured in find_rows(measured_rows, exact["phi_a"], exact["phi_b"],
                                  exact["metric"], budget):
            rows.append({"problem": exact["problem"], "phi_a": exact["phi_a"],
                         "phi_b": exact["phi_b"], "status": exact["status"],
                         "metric": exact["metric"], "n_evals": budget,
                         "delta": measured["delta"],
                         "box_scale": measured["box_scale"],
                         "exact": exact["median"],
                         "measured_median": measured["median"],
                         "measured_q1": measured["q1"],
                         "measured_q3": measured["q3"],
                         "error": measured["median"] - exact["median"]})
    return rows


# p1's measured rows of one pair and metric at one budget, one per delta
def find_rows(rows, phi_a, phi_b, metric, budget):
    return [row for row in rows
            if (row["problem"], row["phi_a"], row["phi_b"], row["metric"],
                row["n_evals"]) == ("p1", phi_a, phi_b, metric, budget)]


# one cell of a record table, every number at six decimals, everything else as it is
def record_cell(value):
    # a value read back out of a csv arrives as text, and a value read back
    # through d3's own reader arrives as a double; both are rendered the same way
    # here so that one table does not print six decimals and the next seventeen.
    # the full-precision value is in the file the section names.
    if isinstance(value, bool):
        return str(value)
    if isinstance(value, str) and looks_numeric(value):
        return "{:.6f}".format(float(value))
    if isinstance(value, float):
        return "{:.6f}".format(value)
    return "" if value is None else str(value)


# whether a cell's text is a decimal number rather than a name or an integer
def looks_numeric(text):
    if not any(mark in text for mark in (".", "e-", "e+")):
        return False
    try:
        float(text)
    except ValueError:
        return False
    return True


# a markdown table of stated columns over stated rows
def markdown_table(fields, rows):
    lines = ["| " + " | ".join(fields) + " |",
             "| " + " | ".join("---" for _ in fields) + " |"]
    for row in rows:
        lines.append("| " + " | ".join(record_cell(row[field]) for field in fields)
                     + " |")
    return lines


# the rows of a written table's decision block, filtered to a stated budget
def decision_rows_at(path, budget=None):
    rows = read_metrics_table(path)[decision_block]
    return [row for row in rows if budget is None or row["n_evals"] == budget]


# the record's opening: what was run, read back out of summary.csv
def record_opening(summary, tables):
    lines = ["# e1: the tier 0 run", "",
             "generated by experiments/run_tier0.py. every number below is read "
             "back out of a file that script wrote, and the file and the key are "
             "named beside it; nothing here is typed. re-running the script from "
             "the same seeds regenerates this document with the same numbers.", "",
             "## 1. what was run", "",
             "from results/tier0/summary.csv, one key per row:", ""]
    lines.extend(markdown_table(("key", "value", "source"), summary))
    lines.extend(["", "the run grid is every solver of slide 17 under every phi of "
                  "[1] on both tier 0 problems at every budget above, at each seed. "
                  "the second budget is the convergence check, one per problem: the "
                  "whole grid repeated at four times the first, with the "
                  "hypervolume reference point derived once across both so that the "
                  "two are two measurements of one quantity and not two "
                  "measurements.", ""])
    lines.extend(["the tables written, all through src/reporting.py's "
                  "save_metrics_table:", ""])
    lines.extend(["- results/tier0/{}".format(path.name)
                  for path in sorted(tables.values(), key=lambda item: item.name)])
    return lines + [""]


# the record's exact table, table 1 of plan section b3
def record_exact(path, exact_path):
    lines = ["## 2. table 1, exact, p1 only", "",
             "the closed-form pair statistics of docs/b1_phi_efficient_sets.md "
             "section 2.4's derived regions, integrated in closed form by this "
             "script. no seed, no budget, no solver and no tolerance enter them. "
             "source: results/tier0/{}, decision block; every measure and both "
             "overlap conventions are in results/tier0/{}.".format(path.name,
                                                                   exact_path.name),
             ""]
    rows = decision_rows_at(path)
    lines.extend(markdown_table(("phi_a", "phi_b", "status", "metric", "median"),
                                rows))
    lines.extend(["", "the overlap column is d2's convention, twice the shared "
                  "measure over the sum of the two measures, which is what "
                  "src/metrics_decision.py's compute_overlap tends to on uniformly "
                  "sampled sets. the shared fraction of the union that "
                  "docs/meeting_2026_09_04.md section 4.3 reports is a different "
                  "quantity and is in results/tier0/{} under the key "
                  "overlap_union_share.".format(exact_path.name), ""])
    return lines


# the record's measured table, table 2 of plan section b3, and its noise floor
def record_measured(path, budgets):
    lines = ["## 3. table 2, measured, every problem and both budgets", "",
             "measured on random search's one filtered sample, through "
             "src/metrics_decision.py's compare_phi_on_one_sample: one uniform "
             "sample of the box, evaluated once, filtered under each phi in turn, "
             "so the three sets differ only through the order. source: "
             "results/tier0/{}, decision block; the per-seed values behind every "
             "median are in results/tier0/decision_metrics_by_seed.csv."
             .format(path.name), "",
             "every pair appears at two values of delta and the delta column "
             "separates them. at delta zero the number is the shared count over "
             "the count, with no tolerance in it: the three sets of one comparison "
             "are index sets over one array, so two decision vectors are the same "
             "point bitwise or they are two points, and that row is the measured "
             "counterpart of table 1 with the tolerance removed rather than made "
             "small. the second value is one twentieth of the box diameter, and it "
             "is the value at which the row can be read against the noise floor "
             "below, which is identically zero at delta zero because two "
             "independent uniform samples share no point.", ""]
    for budget in budgets:
        lines.extend(["### budget {}".format(budget), ""])
        lines.extend(record_measured_budget(path, budget))
        lines.append("")
    lines.extend(record_noise_floor(path))
    lines.extend(record_cross_evaluation(path, budgets[0]))
    return lines + [""]


# the cross-phi rows of table 2 at one budget, both deltas together
def record_measured_budget(path, budget):
    rows = [row for row in decision_rows_at(path, budget)
            if row["metric"] in ("coverage_a_in_b", "coverage_b_in_a", "overlap")
            and row["phi_a"] != row["phi_b"]]
    return markdown_table(("problem", "phi_a", "phi_b", "status", "metric",
                           "cardinality_a", "cardinality_b", "median", "q1", "q3",
                           "delta", "box_scale"), rows)


# the same-phi seed-to-seed rows of table 2, and what they are for
def record_noise_floor(path):
    lines = ["### the noise floor", "",
             "one phi against itself at two seeds, so no order difference can "
             "appear in it; a cross-phi number that does not exceed it is not "
             "evidence of anything, docs/plan_after_meeting.md section b1. it is a "
             "row and not a column because d3's decision block has no column for it "
             "and widening d3 is another subpart's file.", ""]
    floor = [row for row in decision_rows_at(path)
             if row["phi_a"] == row["phi_b"] and row["metric"] in
             ("coverage_a_in_b", "coverage_b_in_a", "overlap")]
    return lines + markdown_table(("problem", "phi_a", "metric", "n_evals",
                                   "cardinality_a", "cardinality_b", "median", "q1",
                                   "q3"), floor)


# the cross evaluation and the symmetric hausdorff, at the reported budget
def record_cross_evaluation(path, budget):
    # the third comparable metric of CONTEXT.md section 5 step 5: what a decision
    # maker committed to one order would keep of the set recovered under another.
    # it needs no common scale between the two image spaces and no tolerance, and
    # it is in no other section, so it is here rather than only in the file.
    lines = ["", "### cross evaluation and distance, at budget {}".format(budget),
             "", "cross_a_under_b is the fraction of the set recovered under phi_a "
             "that survives non-dominated filtering under phi_b, which is what a "
             "decision maker committed to phi_b would keep of phi_a's answer. the "
             "hausdorff distance is symmetric and is in the decision space. "
             "neither moves with delta.", ""]
    rows = [row for row in decision_rows_at(path, budget)
            if row["metric"] in ("cross_a_under_b", "cross_b_under_a",
                                 "hausdorff_symmetric")
            and row["phi_a"] != row["phi_b"]]
    return lines + markdown_table(("problem", "phi_a", "phi_b", "status", "metric",
                                   "cardinality_a", "cardinality_b", "median", "q1",
                                   "q3"), rows)


# the record's instrument-error section, the calibration's own number
def record_instrument_error(rows, path, budget):
    lines = ["## 4. the instrument's error, measured once, on p1", "",
             "p1 is in both tables, and the difference between its two rows is what "
             "the calibration buys: the gap between the quantity derived and the "
             "same quantity measured on recovered sets at budget {}. every other "
             "row of table 2 is read subject to it. source: results/tier0/{}."
             .format(budget, path.name), ""]
    lines.extend(markdown_table(("phi_a", "phi_b", "status", "metric", "delta",
                                 "exact", "measured_median", "measured_q1",
                                 "measured_q3", "error"), rows))
    lines.extend(["", "the error is the measured median minus the exact value, and "
                  "it is given at both values of delta. the delta zero rows carry "
                  "three of the five things docs/plan_after_meeting.md section b2 "
                  "lists as lost between the exact statement and the measured one: "
                  "measure becomes count, derived becomes recovered, and there is "
                  "no truth to be outside of on any other problem. the positive "
                  "delta rows carry the fourth as well, the tolerance, and the "
                  "fifth, dimension, does not bite at two variables and will on "
                  "tier 1. e1 measures the gap and does not interpret it.", ""])
    return lines


# the record's solver table, the objective-space metrics and the solver pairs
def record_solvers(path, points):
    lines = ["## 5. table 3, the solvers", "",
             "the objective-space metrics are valid for comparing solvers under one "
             "fixed phi and are never a ranking of phi, CONTEXT.md section 5 step "
             "5. the decision block of the same file holds the pair statistics of "
             "nsga-ii's and mopso's own output, where phi drives the search as well "
             "as the ordering, so those rows are a question about the solvers and "
             "never a pair number of the study. source: results/tier0/{}; the "
             "per-seed values are in results/tier0/objective_metrics_by_seed.csv "
             "and results/tier0/decision_metrics_by_seed.csv.".format(path.name),
             "", "the hypervolume reference point, one per problem and phi, derived "
             "by the {} rule from every row scored against it across both budgets, "
             "all three solvers and every seed, together with the reference fronts "
             "where they exist:".format(hv_rule), ""]
    lines.extend(markdown_table(("key", "value", "source"), points))
    return lines + [""]


# the objective-space block of the solver table, at one budget
def record_objective_metrics(path, budget):
    lines = ["", "the objective-space metrics at budget {}; the same rows at the "
             "convergence budget are in the same file. every row is a median with "
             "its interquartile range over the seeds, at the cardinality stated "
             "beside it, and a ratio taken across two phi here is a ratio of "
             "volumes in two different spaces and means nothing."
             .format(budget), ""]
    rows = [row for row in read_metrics_table(path)[objective_block]
            if row["n_evals"] == budget]
    return lines + markdown_table(
        ("problem", "phi", "solver", "metric", "cardinality", "reference_size",
         "include_singular_segments", "median", "q1", "q3"), rows)


# the record's registered measurements, m-1 and m-2 of x-01
def record_registered(rows, path, budget):
    lines = ["## 6. the two registered measurements", "",
             "m-1, the tail-survival lift, and m-2, the overhang, both registered "
             "in PROGRESS.md x-01 before this run and computed here from artefacts "
             "the run already produced. which columns they are computed on is "
             "decided by the free sets, which are measured and not asserted: "
             "results/tier0/free_sets.csv. the registered budget is {}; the same "
             "measurements at the convergence budget are in the same file. source: "
             "results/tier0/{}, with the per-seed values in "
             "results/tier0/registered_measurements.csv.".format(budget, path.name),
             ""]
    lines.extend(markdown_table(("problem", "phi", "column", "measurement",
                                 "free_set_size", "constant_column", "defined",
                                 "n_seeds", "median", "iqr", "mean",
                                 "standard_error"),
                                [row for row in rows
                                 if int(row["n_evals"]) == budget]))
    lines.extend(["", "x-01 reads them as follows and e1 does not read them: m-1 is "
                  "predicted at or above 3 where the condition says present and at "
                  "or below 1.5, taken as the largest over all columns, where it "
                  "says absent; m-2 is predicted strictly positive where present "
                  "and exactly zero where absent, and on p1 under example 2.4 its "
                  "mean over seeds is predicted to equal one eighth to within the "
                  "seed spread. a column that is constant has no member minimising "
                  "it strictly, so the mechanism's hypothesis is unavailable there "
                  "and neither measurement is defined; those rows are marked and "
                  "not filled with a zero.", ""])
    return lines


# the record's free sets, which decide what m-1 and m-2 are computed on
def record_free_sets(rows):
    lines = ["## 7. the free sets", "",
             "measured by resampling each decision variable in turn: a column that "
             "does not move does not depend on that variable, and its free set is "
             "what is left. source: results/tier0/free_sets.csv. the column order is "
             "the 2m order every module assumes, (Lambda_1^T f, B_1^T f, "
             "Lambda_2^T f, B_2^T f).", ""]
    lines.extend(markdown_table(("problem", "phi", "column", "depends_on",
                                 "free_set", "free_set_size", "constant_column"),
                                rows))
    return lines + [""]


# the record's delta sweep, delta being a reporting parameter and not a constant
def record_delta_sweep(rows, budget):
    lines = ["## 8. how the measured numbers move with delta", "",
             "delta is a reporting parameter, stated as a fraction of the box "
             "diameter and not as an absolute number, and the numbers move with it: "
             "docs/plan_after_meeting.md section b2 lists the appearance of a "
             "tolerance as one of the five things lost between the exact statement "
             "and the measured one. the median over the seeds at budget {}, on the "
             "pair that is nested in neither direction. source: "
             "results/tier0/delta_sweep.csv.".format(budget), ""]
    lines.extend(markdown_table(("problem", "phi_a", "phi_b", "metric",
                                 "delta_box_fraction", "delta", "median"), rows))
    return lines + [""]


# the record's figure list, every figure carrying its own budget and seed count
def record_figures(paths, root):
    lines = ["## 9. the figures", "",
             "every figure is drawn through src/reporting.py and carries the "
             "budget, the seed count and the cardinality of each series inside the "
             "image and never in the filename. the decision-space figures exist for "
             "p1 alone: they are the plane b1's derived regions live in, drawn "
             "behind the recovered sets, and p0 has one decision variable. the "
             "decision-space figures are drawn at the first seed of the list and "
             "with the three sets in decreasing order of size, because five seeds "
             "pooled bury the derived boundaries and the registry's order hides "
             "X_lu under X_ls; both are drawing choices and the legend states the "
             "seed count and the cardinality of every series. the paths are "
             "relative to the run's output root, results/tier0.", ""]
    # sorted, and not in the order they were drawn, so that the list a run writes
    # and the list a rebuild reads off the directory are one list.
    lines.extend("- {}".format(path.relative_to(root).as_posix())
                 for path in sorted(paths))
    return lines + [""]


# the overlap convention and the noise floor's label, decided in this session
def record_closing_conventions():
    return [
        "## 10. what this run settled that the plan did not", "",
        "*d2's overlap is not the shared fraction of the union.* "
        "compute_overlap is the two covered counts over the two cardinalities, "
        "which on uniformly sampled sets tends to twice the shared measure over the "
        "sum of the two measures and not to the shared measure over the union. "
        "docs/plan_after_meeting.md section b1 names compute_overlap as the "
        "measured counterpart of the 0.103177 of docs/meeting_2026_09_04.md section "
        "4.3, and those are two different quantities. table 1 therefore carries the "
        "exact value in d2's own convention, so that p1's two rows are comparable, "
        "and results/tier0/exact_regions_p1.csv carries both under separate keys. "
        "the coverage columns are unaffected: coverage is the same functional in "
        "both tables.", "",
        "*the noise floor is a row and not a column,* and it is labelled a check. "
        "plan section b3 gives table 2 two noise-floor columns and d3's decision "
        "block has none; widening d3 is another subpart's file. a same-phi row "
        "carries no order difference by construction, so labelling it a finding "
        "would be worse than labelling it a check, and its note says which kind of "
        "check it is.", ""]


# the hypervolume point and the two deltas, decided in this session
def record_closing_instruments():
    return [
        "*the hypervolume reference point is derived once per problem and phi "
        "across both budgets,* so that the convergence check compares two "
        "hypervolumes of one measurement rather than two numbers against two "
        "points. where a pooled image column is constant no point can strictly "
        "dominate any row and every box has zero thickness, so no hypervolume is "
        "scored there and the reason is recorded in summary.csv; p0 carries such a "
        "column under every phi. every front that is scored is asserted to lie "
        "strictly inside the point first, and a front that does not is refused "
        "rather than scored, CONTEXT.md section 10 e1 and v-59.", "",
        "*the tolerance is not needed on the instrument that carries the result, "
        "and every pair is therefore reported at delta zero as well.* plan section "
        "b2 lists the appearance of a tolerance as one of the five things lost "
        "between the exact number and the measured one, on the ground that the "
        "measured one needs delta to decide when two decision vectors are the same "
        "point. on random search's one filtered sample they are the same point "
        "bitwise or they are two points, the three sets being index sets over one "
        "array, so at delta zero the coverage is exactly the shared count over the "
        "count and that loss does not occur. it does occur wherever two different "
        "samples are compared, which is the noise floor and the population "
        "solvers' own pairs, and there delta zero returns zero by construction. so "
        "table 2 carries both, the delta column separates them, and the "
        "instrument's error is given at both.", "",
        "*delta was fixed before the run at one twentieth of the box diameter* and "
        "was not tuned afterwards; the sweep in section 8 is what the numbers do at "
        "other values, emitted so that the movement is a measured artefact rather "
        "than a caveat.", ""]


# what this session settled that the plan did not, and what e1 refuses to do
def record_closing():
    return record_closing_conventions() + record_closing_instruments() + [
        "## 11. what e1 does not do", "",
        "e1 does not interpret. it does not read the registered measurements "
        "against their thresholds, does not say whether the instrument's error is "
        "small, does not compare solvers and does not select anything. that is e3, "
        "CONTEXT.md section 10 e3, and the tables and the record above are its "
        "input.", ""]


# writes the record, reading every number back out of the files just written
def write_record(record_path, root, tables, paths, budget):
    summary = read_table(root / "summary.csv")
    lines = record_opening(summary, tables)
    lines.extend(record_exact(tables["1_exact_p1"], root / "exact_regions_p1.csv"))
    lines.extend(record_measured(tables["2_measured"],
                                 sorted({row["n_evals"] for row in
                                         decision_rows_at(tables["2_measured"])})))
    lines.extend(record_instrument_error(read_table(root / "instrument_error_p1.csv"),
                                         root / "instrument_error_p1.csv", budget))
    lines.extend(record_solvers(tables["3_solvers"],
                                [row for row in summary
                                 if row["key"].startswith("hypervolume_scored")]))
    lines.extend(record_objective_metrics(tables["3_solvers"], budget))
    registered = root / "registered_measurements_summary.csv"
    lines.extend(record_registered(read_table(registered), registered, budget))
    lines.extend(record_free_sets(read_table(root / "free_sets.csv")))
    lines.extend(record_delta_sweep(delta_sweep_summary(root, budget), budget))
    lines.extend(record_figures(paths, root))
    lines.extend(record_closing())
    record_path.parent.mkdir(parents=True, exist_ok=True)
    record_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return record_path


# the delta sweep's median over seeds, on the pair free in both directions
def delta_sweep_summary(root, budget):
    rows = [row for row in read_table(root / "delta_sweep.csv")
            if int(row["n_evals"]) == budget and (row["phi_a"], row["phi_b"])
            == ("lu", "cw")]
    summary = []
    for key in sorted({(row["problem"], row["metric"], row["delta_box_fraction"],
                        row["delta"]) for row in rows}):
        values = [float(row["value"]) for row in rows
                  if (row["problem"], row["metric"], row["delta_box_fraction"],
                      row["delta"]) == key]
        summary.append({"problem": key[0], "phi_a": "lu", "phi_b": "cw",
                        "metric": key[1], "delta_box_fraction": float(key[2]),
                        "delta": float(key[3]),
                        "median": float(np.median(values))})
    return summary


# writes one metrics table through d3, with the block that has no rows left empty
def save_table(root, name, decision_rows, objective_rows):
    path = root / "table_{}.csv".format(name)
    root.mkdir(parents=True, exist_ok=True)
    save_metrics_table({objective_block: objective_rows,
                        decision_block: decision_rows}, path)
    return path


# every per-seed decision-space row of the run, random search and both solvers
def all_decision_rows(runs, comparisons, settings):
    measured, solver_rows = [], []
    for problem_name in problem_names:
        problem = problem_registry[problem_name]
        params = problem_parameters(problem)
        delta = problem_delta(problem)
        for budget in settings["budgets"]:
            found = comparisons[(problem_name, budget)]
            measured.extend(decision_rows_by_seed(found, problem_name, budget))
            for comparison in found:
                measured.extend(pair_rows_at_delta(comparison, problem_name, budget,
                                                   zero_delta))
            measured.extend(noise_floor_rows(found, problem_name, budget))
            for solver in ("nsga2", "mopso"):
                solver_rows.extend(solver_pair_rows(runs, problem, params, solver,
                                                    budget, delta))
    return measured, solver_rows


# the delta sweep over every problem at the reported budget
def all_delta_sweep_rows(comparisons, budget):
    rows = []
    for problem_name in problem_names:
        rows.extend(delta_sweep_rows(comparisons[(problem_name, budget)],
                                     problem_registry[problem_name], budget))
    return rows


# the field order of every raw csv this script writes
raw_fieldnames = {
    "exact_regions_p1.csv": ("quantity", "phi_a", "phi_b", "value"),
    "free_sets.csv": ("problem", "phi", "column", "depends_on", "free_set",
                      "free_set_size", "constant_column"),
    "decision_metrics_by_seed.csv": ("problem", "solver", "phi_a", "phi_b", "status",
                                     "metric", "n_evals", "seed", "cardinality_a",
                                     "cardinality_b", "delta",
                                     "containment_violations", "value"),
    "objective_metrics_by_seed.csv": ("problem", "phi", "solver", "metric",
                                      "n_evals", "seed", "cardinality",
                                      "reference_size", "include_singular_segments",
                                      "value"),
    "registered_measurements.csv": ("measurement", "problem", "phi", "column",
                                    "free_set_size", "constant_column", "n_evals",
                                    "seed", "defined", "value", "tail_share",
                                    "chance_rate", "protected_index"),
    "registered_measurements_summary.csv": ("measurement", "problem", "phi",
                                            "column", "n_evals", "free_set_size",
                                            "constant_column", "defined", "n_seeds",
                                            "median", "q1", "q3", "iqr", "mean",
                                            "standard_deviation", "standard_error"),
    "delta_sweep.csv": ("problem", "phi_a", "phi_b", "status", "metric", "n_evals",
                        "seed", "delta_box_fraction", "delta", "box_scale",
                        "cardinality_a", "cardinality_b", "value"),
    "instrument_error_p1.csv": ("problem", "phi_a", "phi_b", "status", "metric",
                                "n_evals", "delta", "box_scale", "exact",
                                "measured_median", "measured_q1", "measured_q3",
                                "error"),
    "summary.csv": ("key", "value", "source"),
}


# writes one of the run's raw csv files, in the field order stated above
def write_raw_table(root, name, rows):
    return write_table(root / name, raw_fieldnames[name], rows)


# the exact regions of p1, table 1, and the raw file the union share lives in
def write_exact(root):
    write_raw_table(root, "exact_regions_p1.csv", exact_region_rows())
    return save_table(root, "1_exact_p1",
                      exact_table_rows(problem_registry["p1"]), [])


# the measured pair table and the per-seed rows behind it, table 2
def write_measured(root, measured_by_seed):
    write_raw_table(root, "decision_metrics_by_seed.csv", measured_by_seed)
    return save_table(root, "2_measured", decision_table_rows(measured_by_seed), [])


# the solver table, the objective-space metrics beside the solvers' own pairs
def write_solvers(root, objective_by_seed, solver_by_seed, points):
    write_raw_table(root, "objective_metrics_by_seed.csv", objective_by_seed)
    return save_table(root, "3_solvers", decision_table_rows(solver_by_seed),
                      objective_table_rows(objective_by_seed, points))


# every artefact between the runs and the record, and the tables they are in
def write_artefacts(root, runs, comparisons, settings):
    announce("computing the exact regions and the decision-space metrics")
    tables = {"1_exact_p1": write_exact(root)}
    measured_by_seed, solver_by_seed = all_decision_rows(runs, comparisons, settings)
    tables["2_measured"] = write_measured(root, measured_by_seed)
    announce("computing the objective-space metrics")
    objective_by_seed, points = objective_values(runs, settings)
    tables["3_solvers"] = write_solvers(root, objective_by_seed, solver_by_seed,
                                        points)
    write_raw_table(root, "delta_sweep.csv",
                    all_delta_sweep_rows(comparisons, settings["budgets"][0]))
    write_instrument_error(root, tables, settings["budgets"][0])
    write_registered(root, comparisons, settings)
    return tables, points


# the instrument's error, p1's exact row against p1's measured row
def write_instrument_error(root, tables, budget):
    return write_raw_table(
        root, "instrument_error_p1.csv",
        instrument_error_rows(decision_rows_at(tables["1_exact_p1"]),
                              decision_rows_at(tables["2_measured"]), budget))


# the free sets and the two registered measurements, per seed and summarised
def write_registered(root, comparisons, settings):
    free_rows = free_set_rows(settings)
    write_raw_table(root, "free_sets.csv", free_rows)
    rows = registered_measurement_rows(comparisons, free_rows, settings)
    write_raw_table(root, "registered_measurements.csv", rows)
    return write_raw_table(root, "registered_measurements_summary.csv",
                           registered_summary_rows(rows))


# the whole run: the grid, the artefacts, the tables, the figures and the record
def run(output_root, record_path, settings):
    started = time.time()
    root = Path(output_root)
    runs, comparisons = execute_grid(settings)
    announce("saving raw results")
    save_raw(root, runs)
    tables, points = write_artefacts(root, runs, comparisons, settings)
    announce("drawing figures")
    paths = all_figures(root, runs, settings)
    write_raw_table(root, "summary.csv",
                    summary_rows(settings, runs, tables, points,
                                 time.time() - started))
    announce("writing the record")
    write_record(Path(record_path), root, tables, paths, settings["budgets"][0])
    return tables


# the tables of a run already on disk, by the names save_table gives them
def artefact_tables(root):
    return {name: root / "table_{}.csv".format(name)
            for name in ("1_exact_p1", "2_measured", "3_solvers")}


# the figures of a run already on disk, in the order the record lists them
def artefact_figures(root):
    return sorted((root / "figures").glob("*.png"))


# every configuration of a run already on disk, read back from its raw arrays
def artefact_runs(root, settings):
    return {(problem_name, solver, phi_name, budget):
            load_raw_runs(raw_path(root, (problem_name, solver, phi_name, budget)))
            for problem_name in problem_names
            for solver in solver_names
            for phi_name in phi_names
            for budget in settings["budgets"]}


# the figures redrawn from the raw arrays, without re-running anything
def rebuild_figures(output_root, settings):
    root = Path(output_root)
    return all_figures(root, artefact_runs(root, settings), settings)


# the record rebuilt from the artefacts of a run, without re-running anything
def rebuild_record(output_root, record_path, budget):
    # the raw results and the tables are re-readable without re-running, so the
    # record they are read into is too. this is how a change to the record's prose
    # reaches the document without spending the grid again, and it is also the
    # check that every number in the record does come out of a file: nothing of
    # the run is in memory here.
    root = Path(output_root)
    return write_record(Path(record_path), root, artefact_tables(root),
                        artefact_figures(root), budget)


# the run parameters as the command line states them
def parse_arguments(argv):
    parser = argparse.ArgumentParser(description="e1, the tier 0 run")
    parser.add_argument("--output-root", default=str(repository_root / "results"
                                                     / "tier0"))
    parser.add_argument("--record", default=str(repository_root / "docs"
                                                / "e1_tier0_run.md"))
    parser.add_argument("--seeds", default=",".join(str(seed) for seed in run_seeds))
    parser.add_argument("--budgets", default="{},{}".format(
        gate_budget, gate_budget * convergence_multiple))
    parser.add_argument("--pop-size", type=int, default=gate_pop_size)
    parser.add_argument("--reference-points", type=int, default=reference_points)
    parser.add_argument("--record-only", action="store_true",
                        help="rebuild the record from artefacts already written")
    parser.add_argument("--figures-only", action="store_true",
                        help="redraw the figures from the raw arrays, then the "
                             "record")
    return parser.parse_args(argv)


# the entry point: parse, run, and say where the record went
def main(argv=None):
    arguments = parse_arguments(argv)
    settings = run_settings([int(seed) for seed in arguments.seeds.split(",")],
                            [int(budget) for budget in arguments.budgets.split(",")],
                            arguments.pop_size, arguments.reference_points)
    if arguments.figures_only:
        rebuild_figures(arguments.output_root, settings)
        rebuild_record(arguments.output_root, arguments.record,
                       settings["budgets"][0])
    elif arguments.record_only:
        rebuild_record(arguments.output_root, arguments.record,
                       settings["budgets"][0])
    else:
        run(arguments.output_root, arguments.record, settings)
    announce("done, record at {}".format(arguments.record))


if __name__ == "__main__":
    main()
