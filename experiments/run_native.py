# f3: the native run. all three solvers, all three phi, I-BK1, over the seed list,
# at the gate budget, with one convergence check at four times it. it writes the
# raw results, the tables, the figures and the record. it interprets nothing.
#
# what this run is, in the arc's terms. e1 calibrated the instrument on p1, the
# one problem the project built whose phi-efficient sets are known exactly, and
# measured what the instrument costs. e2 extended it to two standard benchmarks
# where no exact answer exists. f3 applies it to a problem that is interval-valued
# at source and that the project did not construct: I-BK1, problem 1 of appendix A
# of [16], whose imprecision is in its published coefficients.
# docs/plan_after_meeting.md sections a1 and a2.
#
# **there is a table 1 here, and that is the point of the session.** on tier 1
# there was none, zdt1 and dtlz2 having no closed-form phi-efficient set. I-BK1
# has one under all three phi, docs/part2/f2_ibk1_derivation.md section 2.4, so
# the exact pair statistics exist and the same quantities can be measured beside
# them. that makes this the **second calibration point** the project has and the
# first on a problem nobody adapted, which is what
# docs/part1/part1_closing.md section 7.3 asks for.
#
# what f3 answers and what it does not. clause c5 of
# docs/part1/part1_closing.md section 7.1 is marked unsupported and stays marked
# unsupported here: this script reports whether the measured comparison
# reproduces what f2 derived and at what error, and the claim is the write-up's.
# **no clause is declared supported by a script.**
#
# the three phi pairs, and why the headline convention does not apply here.
# docs/part1/part1_closing.md section 3.1 takes its headline from phi_lu against
# phi_cw because on p1 that pair is nested in neither direction. **on I-BK1 all
# three pairs nest**: f2 section 3.1 finds X_cw strictly inside X_lu strictly
# inside X_ls, exactly and from the closed forms. two of the three containments
# are predicted by docs/part1/a_close_containment.md and are checks, and
# src/metrics_decision.py labels them so; the third, X_cw inside X_lu, is not
# predicted and is f2 section 3.2's finding **about I-BK1** rather than a measured
# difference between the two orders. so the pair d2 labels a finding carries a
# derived nesting here and not a crossing, the record says so in those words, and
# **no nested pair is presented as a measured difference**.
#
# delta is zero and that is the headline, d-08. the pair statistics are computed
# on random search's one filtered sample through src/metrics_decision.py's
# compare_phi_on_one_sample, so the three sets are index sets over one array: two
# decision vectors are bitwise identical or they are different points. a positive
# delta is reported only where two different samples are compared and it is
# structurally required, which is the same-phi seed-to-seed noise floor and the
# population solvers' own pairs.
#
# coverage leads and any overlap is named, d-09. d2's compute_overlap is dice,
# twice the shared count over the two cardinalities; jaccard is the shared count
# over the union, and the two are different functionals. jaccard is computed
# **from** dice by the identity jaccard = dice / (2 - dice) and d2 is not changed,
# exactly as e2 does it.
#
# the counterexample, measured and not asserted. f2 section 4.2 establishes by
# algebra that [16]'s Table 1 point x* is dominated in all four endpoint values,
# and therefore is not a Pareto optimal point of I-BK1 in [16]'s own definition
# 2.17. this script asks a different question with the same subject: run without
# being told any of it, do the solvers return points that dominate x* in [16]'s
# own relation, how many and by how much. that is a second route to the same
# conclusion from a different direction. **it is reported as a measurement and
# never as a claim about the paper**; the claim is f2's and its argument is there.
#
# x-01, and the answer is a negative. the protected-minimiser condition of
# docs/part1/part1_closing.md section 3.4 applies at a pair (problem, phi) exactly
# when some image column has a non-empty free set. f2 section 1.2 finds all twelve
# of I-BK1's image coordinates to be diagonal quadratics in **both** variables
# with strictly positive coefficients, because [16] put a non-degenerate interval
# on both terms of both objectives, so every free set is empty and the condition
# applies nowhere. this script measures the free sets rather than asserting them,
# by resampling each decision variable in turn, and computes m-2 only where the
# condition applies. **m-1 is withdrawn as an instrument at x-01's outcome line
# and is not computed, not revived and not re-thresholded.**
#
# the objective-space metrics are computed at the common cardinality of the
# comparison, r-16 and CONTEXT.md section 10 d1, as e2 does and unlike e1, which
# reported at full cardinality and needed the caption of
# docs/part1/part1_closing.md section 3.5 to travel with its block. the
# decision-space metrics are on the full untruncated sets, which is where
# CONTEXT.md section 10 d1 puts the restriction. **the two objective blocks of
# e1 and f3 are not comparable with each other and may not be placed side by
# side**, e1's being at full cardinality.
#
# igd exists here and it did not on tier 1. src/problems_native.py encodes f2's
# derived sets, so there is a reference object to average over, and the flag
# include_singular_segments is False on every row because **I-BK1 has no singular
# weight direction at all**, f2 section 2.3: b1's two singular rays on p1 came
# from width coordinates that were functions of one variable each, and no image
# coordinate of I-BK1 is. s-12 does not arise on this problem and the flag is a
# no-op rather than a choice.
#
# the raw results are written before any metric is computed, so a metric can be
# recomputed without re-running a solver, and the manifest names every array.
#
# the number-provenance rule, CONTEXT.md section 10 e1. every number in
# docs/part2/f3_native_run.md is read back out of a file this script wrote and
# the record names the file and the key beside it. nothing is typed into the
# record. no number is typed into this file that is not a run parameter or a
# constant of [16] or of f2 cited beside it.
#
# [16] is papers/Newton Method for Multiobjective Optimization Problems of
# Interval-Valued Maps.pdf. [1] is
# papers/new_preference_order_relationships_paper.txt.

import argparse
import csv
import math
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
from metrics_objective import (common_cardinality, compute_hv, compute_igd,
                               compute_spread, derive_reference_point,
                               nadir_margin_rule, truncate_to_common_cardinality)
from phi_transforms import phi_registry
from problems_native import (band_ends, efficient_set, farthest_point_mode, ibk1,
                             ibk1_shift, reference_front, region_sample_seed)
from random_search import SearchResult, phi_image
from reporting import (PlottedFront, PlottedSet, decision_block, format_value,
                       objective_block, plot_decision_sets, plot_fronts,
                       read_metrics_table, save_metrics_table,
                       summarize_across_seeds)
from run_tier0 import markdown_table
from runners import run_mopso, run_nsga2

# the three phi in the lu, ls, cw order of examples 2.2, 2.3 and 2.4 of [1],
# which is the order every table and every loop in the project uses.
phi_names = ("lu", "ls", "cw")

# the three solvers of slide 17. random search is the control and is in the grid
# on the same terms as the other two, CONTEXT.md section 10 c1.
solver_names = ("random_search", "nsga2", "mopso")

# the one problem of this run, src/problems_native.py's
problem_name = ibk1.name

# the seed list, the population and the gate budget, all three e1's and e2's. the
# brief for this session fixes them so that the three runs are comparable at all.
run_seeds = (11, 12, 13, 14, 15)
gate_pop_size = 100
gate_n_gen = 50
gate_budget = gate_pop_size * gate_n_gen

# the convergence check: the whole grid re-measured at four times the budget. it
# is a comparison and not a second experiment, every configuration being repeated
# exactly, including the hypervolume reference point and the truncation.
convergence_multiple = 4

# delta, stated as a fraction of the box diameter and never as an absolute
# number, docs/plan_after_meeting.md section b1. one twentieth, e1's and e2's.
delta_box_fraction = 0.05

# the fractions the coverage and overlap statistics are also computed at, so that
# their movement with delta is a measured artefact rather than a caveat
delta_sweep_fractions = (0.0, 0.01, 0.02, delta_box_fraction, 0.10, 0.20)

# zero is in that list and it is not a limiting case, d-08. the three sets of one
# random-search comparison are index sets over one array, so two decision vectors
# are the same point bitwise or they are two points and no tolerance decides it.
zero_delta = 0.0

# the igd reference front. the size and the seed are src/problems_native.py's own
# and the mode is b2-b's correction, r-13, because igd averages over reference
# points and a parametrisation's density in objective space is its own.
reference_points = 1000
reference_sampling_mode = farthest_point_mode
reference_seed = region_sample_seed

# I-BK1 has no singular weight direction under any phi, f2 section 2.3, so the
# flag d3 requires on every objective-space row is False everywhere and is a
# no-op rather than a choice. s-12 is p1's row and does not arise here.
no_singular_setting = False

# the hypervolume reference point rule. the margin rule and not the strict nadir,
# CONTEXT.md section 10 e1, moocore clipping at the point instead of refusing.
hv_rule = nadir_margin_rule

# the seed of the common-cardinality truncation, r-16. a run parameter, and one
# seed for the whole run so that every front is cut the same way.
truncation_seed = 20260906

# how the free sets are measured: one resampling of each decision variable over a
# sample of this size at this seed. a structural property and not a reporting
# parameter, so it takes a fixed seed and is not summarised over seeds.
dependence_points = 512
dependence_seed = 20260905

# [16] Table 1, printed page 20, last row, k = 12, transcribed in
# docs/part2/lit_review.md section 1.6 and re-read in f2 section 4.2: the point
# algorithm 1 returns on I-BK1 and the objective row printed beside it, in the
# column order (G_1 lower, G_1 upper, G_2 lower, G_2 upper). the printed row and
# not a recomputation is what the dominance measurement below is made against,
# because a statement about the paper has to be checkable against the paper.
printed_x_star = (3.914930, 1.428474)
printed_g_star = (1.736722, 3.677497, 1.393317, 6.731112)

# the column pairs the objective-space figures project onto. the 2m columns come
# in the order (Lambda_1^T f, B_1^T f, Lambda_2^T f, B_2^T f), so (0, 2) is the
# two first image coordinates against each other and (1, 3) the two second ones.
figure_col_pairs = ((0, 2), (1, 3))

# how many points of each derived set the decision-space figure draws behind the
# recovered ones. a drawing resolution and not a reporting parameter.
region_figure_points = 2000

# the registered measurement this run computes, and the one it does not. m-2 is
# PROGRESS.md x-01's overhang; m-1 is withdrawn at x-01's outcome line.
overhang_name = "m-2_overhang"


# the run parameters of one invocation, so that no function reads a global budget
def run_settings(seeds, budgets, pop_size, n_reference_points):
    return {"seeds": tuple(int(seed) for seed in seeds),
            "budgets": tuple(int(budget) for budget in budgets),
            "pop_size": int(pop_size),
            "reference_points": int(n_reference_points)}


# the euclidean diameter of I-BK1's decision box, the scale delta is stated in
def box_diameter():
    lower, upper = ibk1.bounds()
    return float(np.sqrt(np.sum(np.square(np.asarray(upper) - np.asarray(lower)))))


# the absolute delta of this run, the stated fraction of the box diameter
def problem_delta(fraction=delta_box_fraction):
    return float(fraction) * box_diameter()


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
    print("[f3] {}".format(message), flush=True)


# the antiderivative f2 section 3.1 integrates the wedge with
def wedge_antiderivative(c):
    # f2 section 3.1: parameterising the wedge by (U, nu) and integrating the
    # jacobian 25 U / ((1 + U)^2 (1 + nu U)^2) over U in [0, inf] gives
    # |X_phi| = 25 [ I(L) - I(R) ] with I(c) = c ln c / (c - 1)^2 + 1 / (1 - c).
    # no band end of any of the three phi is 1, where I is singular, the six ends
    # being 1/2, 2/3, 3/4, 3/2, 5/3 and 2.
    return c * math.log(c) / (c - 1.0) ** 2 + 1.0 / (1.0 - c)


# the lebesgue measure of the wedge of one band of nu, f2 section 3.1
def band_measure(lower, upper):
    # the 25 is the square of the problem's own shift, the corner (5, 5) both
    # boundary curves of every wedge run to, f2 section 2.4.
    return ibk1_shift ** 2 * (wedge_antiderivative(lower)
                              - wedge_antiderivative(upper))


# the lebesgue measure of each of f2 section 2.4's three derived regions
def derived_areas():
    return {name: band_measure(*band_ends(name)) for name in phi_names}


# the measure of the intersection of two derived regions, from their bands
def derived_intersection(phi_a, phi_b):
    # every derived set is the wedge of an interval of nu and nothing else, f2
    # section 2.4, so the intersection of two of them is the wedge of the
    # intersected interval. the nesting f2 section 3.1 reports is therefore
    # derived here rather than assumed: where one band contains the other this
    # returns the contained one's own measure.
    lower_a, upper_a = band_ends(phi_a)
    lower_b, upper_b = band_ends(phi_b)
    return band_measure(max(lower_a, lower_b), min(upper_a, upper_b))


# the pairwise intersection measures of the three derived regions
def derived_intersections():
    return {(phi_a, phi_b): derived_intersection(phi_a, phi_b)
            for phi_a, phi_b in phi_pairs}


# the exact pair statistics of one pair of derived regions
def exact_pair_statistics(area_a, area_b, shared):
    # coverage is the share of one region lying in the other, which is the
    # quantity d2's compute_coverage tends to at delta zero on a uniform sample.
    # both overlap conventions are returned because they are two different
    # functionals, d-09: dice is d2's own and is what makes the exact and the
    # measured row the same quantity, and jaccard is the shared fraction of the
    # union, which is the convention f2 section 3.1 reports.
    dice = 2.0 * shared / (area_a + area_b)
    return {"coverage_a_in_b": shared / area_a, "coverage_b_in_a": shared / area_b,
            "overlap_d2_convention": dice, "overlap_union_share": jaccard_from_dice(dice)}


# every exact quantity of f2's derived regions, as one long-format table
def exact_region_rows():
    areas = derived_areas()
    intersections = derived_intersections()
    rows = [{"quantity": "band_lower", "phi_a": name, "phi_b": "",
             "value": band_ends(name)[0]} for name in phi_names]
    rows.extend({"quantity": "band_upper", "phi_a": name, "phi_b": "",
                 "value": band_ends(name)[1]} for name in phi_names)
    rows.extend({"quantity": "area", "phi_a": name, "phi_b": "",
                 "value": areas[name]} for name in phi_names)
    for phi_a, phi_b in phi_pairs:
        shared = intersections[(phi_a, phi_b)]
        rows.append({"quantity": "intersection_area", "phi_a": phi_a,
                     "phi_b": phi_b, "value": shared})
        statistics = exact_pair_statistics(areas[phi_a], areas[phi_b], shared)
        rows.extend({"quantity": name, "phi_a": phi_a, "phi_b": phi_b,
                     "value": statistics[name]} for name in sorted(statistics))
    return rows


# the pair note, with I-BK1's own geometry added where f2 settled it
def native_pair_note(phi_a, phi_b):
    # f2 section 3.1 finds X_cw strictly inside X_lu strictly inside X_ls, so on
    # this problem the pair d2 labels a finding is nested too. that is a result
    # about I-BK1 derived before this run and not a difference this run measured,
    # and the note says so on the row rather than leaving it to the record.
    if pair_status(phi_a, phi_b) == check_status:
        return pair_note(phi_a, phi_b)
    return (pair_note(phi_a, phi_b) + ". **on I-BK1 this pair nests as well**: f2 "
            "section 3.1 derives X_cw strictly inside X_lu from the closed forms, "
            "which docs/part1/a_close_containment.md's criterion does not predict "
            "in either direction and which f2 section 3.2 records as a finding "
            "about this problem. so the headline convention of "
            "docs/part1/part1_closing.md section 3.1 does not apply here, there "
            "being no non-nested pair at all, and this row is not a measured "
            "difference between two orders")


# the note the exact table's rows carry, saying what the row is and is not
def exact_note(phi_a, phi_b):
    return ("exact lebesgue measure of f2 section 2.4's derived regions, "
            "integrated in closed form from their bands of nu; no seed, no "
            "budget, no solver and no tolerance enter it, so the seed count, the "
            "budget and the two cardinalities are written as zero. overlap is "
            "d2's convention, twice the shared measure over the sum of the two, "
            "so that this row and the measured row are the same quantity; the "
            "jaccard value is in exact_regions_ibk1.csv. "
            + native_pair_note(phi_a, phi_b))


# table 1, the exact pair statistics of I-BK1, in d3's decision block
def exact_table_rows():
    areas = derived_areas()
    intersections = derived_intersections()
    rows = []
    for phi_a, phi_b in phi_pairs:
        statistics = exact_pair_statistics(areas[phi_a], areas[phi_b],
                                           intersections[(phi_a, phi_b)])
        for metric in ("coverage_a_in_b", "coverage_b_in_a"):
            rows.append(exact_table_row(phi_a, phi_b, metric, statistics[metric]))
        rows.append(exact_table_row(phi_a, phi_b, "overlap",
                                    statistics["overlap_d2_convention"]))
    return rows


# one row of table 1, with the fields a measured row would carry set to zero
def exact_table_row(phi_a, phi_b, metric, value):
    return {"problem": problem_name, "phi_a": phi_a, "phi_b": phi_b,
            "status": pair_status(phi_a, phi_b), "metric": metric, "n_seeds": 0,
            "n_evals": 0, "cardinality_a": 0, "cardinality_b": 0, "delta": 0.0,
            "box_scale": box_diameter(), "containment_violations": None,
            "note": exact_note(phi_a, phi_b), "median": value, "q1": value,
            "q3": value, "iqr": 0.0}


# the fronts of one filtered sample, one per phi, from a single evaluation
def sample_fronts(sample):
    # the isolation of src/random_search.py's filter_one_sample_under_every_phi is
    # carried through to the fronts: the problem is evaluated once and each phi's
    # front is that evaluation's image at that phi's index set, so the three
    # fronts of one seed differ only through the order. this is the same object
    # run_random_search would return at the same seed and it is built here so that
    # one seed costs one filter pass rather than two.
    pairs = ibk1.evaluate(sample.decision_vectors, None)
    fronts = {}
    for name in phi_names:
        keep = sample.indices[name]
        image = phi_image(ibk1, pairs, phi_registry[name])
        fronts[name] = (image[keep], sample.decision_vectors[keep])
    return fronts


# random search at one budget, as one comparison per seed and three results
def random_search_runs(budget, seeds, delta):
    comparisons, results = [], {name: [] for name in phi_names}
    for seed in seeds:
        comparison = compare_phi_on_one_sample(ibk1, None, budget, seed, delta)
        comparisons.append(comparison)
        for name, (front, vectors) in sample_fronts(comparison.sample).items():
            results[name].append(SearchResult(seed=seed, n_evals=int(budget),
                                              front=front, decision_vectors=vectors))
    return comparisons, results


# nsga-ii's and mopso's runs under one phi at one budget
def solver_runs(phi_name, budget, seeds, pop_size):
    # the budget is spent in evaluations and the generation count follows from it,
    # so both solvers spend exactly the stated budget, src/runners.py.
    n_gen = int(budget) // int(pop_size)
    return {"nsga2": run_nsga2(ibk1, phi_name, None, n_gen, pop_size, seeds),
            "mopso": run_mopso(ibk1, phi_name, None, n_gen, pop_size, seeds)}


# every run of the grid, with the random-search comparisons the pair table reads
def execute_grid(settings):
    runs, comparisons = {}, {}
    delta = problem_delta()
    for budget in settings["budgets"]:
        announce("running {} at budget {}".format(problem_name, budget))
        found, results = random_search_runs(budget, settings["seeds"], delta)
        comparisons[budget] = found
        for name in phi_names:
            runs[("random_search", name, budget)] = results[name]
            for solver, found_runs in solver_runs(name, budget, settings["seeds"],
                                                  settings["pop_size"]).items():
                runs[(solver, name, budget)] = found_runs
    return runs, comparisons


# the file one configuration's raw arrays are written to
def raw_path(root, key):
    solver, phi_name, budget = key
    return Path(root) / "raw" / "{}_{}_{}_{}.npz".format(problem_name, solver,
                                                         phi_name, budget)


# one configuration's runs, written as one compressed archive
def save_raw_runs(root, key, results):
    path = raw_path(root, key)
    path.parent.mkdir(parents=True, exist_ok=True)
    arrays = {}
    for index, result in enumerate(results):
        arrays["seed_{}".format(index)] = np.array([result.seed, result.n_evals])
        arrays["front_{}".format(index)] = result.front
        arrays["vectors_{}".format(index)] = result.decision_vectors
    np.savez_compressed(path, **arrays)
    return path


# one configuration's runs, read back out of the archive save_raw_runs wrote
def load_raw_runs(path):
    with np.load(path) as archive:
        count = sum(1 for name in archive.files if name.startswith("seed_"))
        return [SearchResult(seed=int(archive["seed_{}".format(index)][0]),
                             n_evals=int(archive["seed_{}".format(index)][1]),
                             front=archive["front_{}".format(index)],
                             decision_vectors=archive["vectors_{}".format(index)])
                for index in range(count)]


# every configuration's raw arrays, written before any metric is computed
def save_raw(root, runs):
    rows = []
    for key in sorted(runs):
        path = save_raw_runs(root, key, runs[key])
        rows.append({"problem": problem_name, "solver": key[0], "phi": key[1],
                     "n_evals": key[2], "n_runs": len(runs[key]),
                     "file": path.name})
    return write_table(Path(root) / "raw_manifest.csv",
                       ("problem", "solver", "phi", "n_evals", "n_runs", "file"),
                       rows)


# the 2m image columns of I-BK1 under one phi, at a stated sample
def image_columns(phi_name, x):
    return phi_image(ibk1, ibk1.evaluate(x, None), phi_registry[phi_name])


# which decision variables each image column depends on, measured by resampling
def column_dependence(phi_name, n_points, seed):
    # a structural property measured rather than asserted, e1's method unchanged.
    # one variable at a time is redrawn uniformly over its own range and a column
    # that does not move at any of the sample's points does not depend on that
    # variable. the free set F_k of docs/plan_after_meeting.md section f2 is the
    # complement of what this returns, and a constant column is reported
    # separately, the mechanism needing a member that minimises the column
    # strictly and a constant column having none.
    lower, upper = ibk1.bounds()
    generator = np.random.default_rng(seed)
    x = generator.uniform(lower, upper, size=(int(n_points), ibk1.n_vars))
    base = image_columns(phi_name, x)
    depends = np.zeros((base.shape[1], ibk1.n_vars), dtype=bool)
    for variable in range(ibk1.n_vars):
        moved = np.array(x, copy=True)
        moved[:, variable] = generator.uniform(lower[variable], upper[variable],
                                               size=int(n_points))
        depends[:, variable] = np.any(image_columns(phi_name, moved) != base, axis=0)
    return depends, np.all(base == base[0], axis=0)


# the free set of every image column of every phi, as table rows
def free_set_rows():
    rows = []
    for phi_name in phi_names:
        depends, constant = column_dependence(phi_name, dependence_points,
                                              dependence_seed)
        for column in range(depends.shape[0]):
            free = [str(index) for index in range(ibk1.n_vars)
                    if not depends[column, index]]
            rows.append({"problem": problem_name, "phi": phi_name,
                         "column": column, "depends_on": " ".join(
                             str(index) for index in range(ibk1.n_vars)
                             if depends[column, index]),
                         "free_set": " ".join(free), "free_set_size": len(free),
                         "constant_column": bool(constant[column])})
    return rows


# how many columns of the whole run have a non-empty free set, which decides m-2
def columns_with_a_free_set(rows):
    # PROGRESS.md x-01: the protected-minimiser condition applies at a pair
    # (problem, phi) exactly when some image column has a non-empty free set and
    # the efficient set's projection onto it is a proper subset of the box's. the
    # first half is measured here; where it is empty the condition applies
    # nowhere and m-2 is not computed rather than computed as zero, a zero
    # overhang over no coordinates being a value the estimator returns by
    # construction and not a measurement.
    return [row for row in rows if int(row["free_set_size"]) > 0]


# the four endpoint values of I-BK1 at each row of a decision set
def endpoint_values(x):
    # [16]'s own order relation is its definition 2.2, printed page 4,
    # componentwise <= on the endpoint pair of each objective, and
    # docs/part2/lit_review.md section 1.4 locates it as example 2.2 of [1], which
    # is phi_lu. so the relation the measurement below uses is the problem's own
    # representation read directly, and it does not depend on which phi the
    # solver was run under.
    return np.column_stack([value for pair in ibk1.evaluate(x, None)
                            for value in pair])


# which rows of a decision set beat the paper's printed row in all four values
def dominator_mask(x):
    # [16] definition 2.17, printed page 7: x* is a Pareto optimal point when no
    # other feasible x has G_i(x) <= G_i(x*) for all i. a row strictly below the
    # printed row in every one of the four endpoint values is a witness against
    # that and against definition 2.16's weak form as well, so the strict test is
    # the one made here and no reading of the non-strict case is needed.
    return np.all(endpoint_values(x) < np.asarray(printed_g_star), axis=1)


# the widest-margin dominator of a decision set, and how far it beats the row
def widest_dominator(x, mask):
    # the margin of one row is the smallest of its four gaps below the printed
    # row, so a positive margin is a domination in all four; the widest is the
    # largest of those, which is the statistic f2 section 4.2 reports for its own
    # dominator. absent where the set holds none.
    if not bool(np.any(mask)):
        return None, None
    margins = np.min(np.asarray(printed_g_star) - endpoint_values(x[mask]), axis=1)
    best = int(np.argmax(margins))
    return float(margins[best]), np.asarray(x[mask])[best]


# the domination count of one run against [16]'s printed row, as one row
def dominator_row(result, solver, phi_name, budget):
    mask = dominator_mask(result.decision_vectors)
    margin, point = widest_dominator(result.decision_vectors, mask)
    count = int(np.count_nonzero(mask))
    return {"problem": problem_name, "solver": solver, "phi": phi_name,
            "n_evals": int(budget), "seed": int(result.seed),
            "cardinality": int(len(result.decision_vectors)),
            "n_dominating": count,
            "share_dominating": count / float(len(result.decision_vectors)),
            "widest_margin": margin,
            "widest_x_1": None if point is None else float(point[0]),
            "widest_x_2": None if point is None else float(point[1])}


# every run's domination count against the printed row, per seed
def dominator_rows(runs, settings):
    return [dominator_row(result, solver, phi_name, budget)
            for solver in solver_names
            for phi_name in phi_names
            for budget in settings["budgets"]
            for result in runs[(solver, phi_name, budget)]]


# the domination counts summarised over the seeds of one configuration
def dominator_summary_rows(rows):
    summary = []
    keys = sorted({(row["solver"], row["phi"], row["n_evals"]) for row in rows})
    for solver, phi_name, budget in keys:
        group = [row for row in rows if (row["solver"], row["phi"],
                                         row["n_evals"]) == (solver, phi_name,
                                                             budget)]
        margins = [row["widest_margin"] for row in group
                   if row["widest_margin"] is not None]
        entry = {"problem": problem_name, "solver": solver, "phi": phi_name,
                 "n_evals": budget, "n_seeds": len(group),
                 "seeds_with_a_dominator": sum(1 for row in group
                                               if row["n_dominating"] > 0),
                 "cardinality": int(np.median([row["cardinality"]
                                               for row in group])),
                 "widest_margin_over_seeds": max(margins) if margins else None}
        entry.update(summarize_across_seeds([row["n_dominating"] for row in group]))
        summary.append(entry)
    return summary


# the eight decision-space metrics of one pair, plus the jaccard convention
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
def decision_row(solver, phi_a, phi_b, metric, budget, seed, n_a, n_b, delta,
                 violations, value):
    return {"problem": problem_name, "solver": solver, "phi_a": phi_a,
            "phi_b": phi_b, "status": pair_status(phi_a, phi_b), "metric": metric,
            "n_evals": int(budget), "seed": int(seed), "cardinality_a": int(n_a),
            "cardinality_b": int(n_b), "delta": float(delta),
            "containment_violations": violations, "value": value}


# every per-seed decision-space value of the random-search pair comparisons
def decision_rows_by_seed(comparisons, budget):
    return [decision_row("random_search", pair.phi_a, pair.phi_b, metric, budget,
                         comparison.seed, pair.n_a, pair.n_b, comparison.delta,
                         pair.containment_violations, value)
            for comparison in comparisons
            for pair in comparison.pairs
            for metric, value in pair_values(pair).items()]


# the four statistics that move with delta, between two decision sets
def delta_values(set_a, set_b, delta):
    dice = compute_overlap(set_a, set_b, delta)
    return {"coverage_a_in_b": compute_coverage(set_a, set_b, delta),
            "coverage_b_in_a": compute_coverage(set_b, set_a, delta),
            "overlap": dice, "overlap_jaccard": jaccard_from_dice(dice)}


# the delta-dependent pair statistics of one comparison at a stated delta
def pair_rows_at_delta(comparison, budget, delta):
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
        rows.extend(decision_row("random_search", phi_a, phi_b, metric, budget,
                                 comparison.seed, len(set_a), len(set_b), delta,
                                 None, value)
                    for metric, value in delta_values(set_a, set_b, delta).items())
    return rows


# the same coverage statistic between two seeds of one phi, the instrument's floor
def noise_floor_rows(comparisons, budget):
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
            rows.extend(noise_floor_values(sets[index], sets[other], phi_name,
                                           budget, comparison))
    return rows


# the pair statistics between two same-phi seeds, as per-seed rows
def noise_floor_values(set_a, set_b, phi_name, budget, comparison):
    delta = comparison.delta
    return [dict(decision_row("random_search_noise_floor", phi_name, phi_name,
                              metric, budget, comparison.seed, len(set_a),
                              len(set_b), delta, None, value),
                 status=check_status)
            for metric, value in delta_values(set_a, set_b, delta).items()]


# the pair statistics of one population solver's own output, per seed
def solver_pair_rows(runs, solver, budget, delta):
    rows = []
    for phi_a, phi_b in phi_pairs:
        runs_a = runs[(solver, phi_a, budget)]
        runs_b = runs[(solver, phi_b, budget)]
        for result_a, result_b in zip(runs_a, runs_b):
            values = solver_pair_values(result_a, result_b, phi_a, phi_b, delta)
            rows.extend(decision_row(solver, phi_a, phi_b, metric, budget,
                                     result_a.seed, len(result_a.decision_vectors),
                                     len(result_b.decision_vectors), delta, None,
                                     value) for metric, value in values.items())
    return rows


# the metrics between two decision sets one solver returned under two phi
def solver_pair_values(result_a, result_b, phi_a, phi_b, delta):
    set_a, set_b = result_a.decision_vectors, result_b.decision_vectors
    hausdorff = compute_hausdorff(set_a, set_b)
    values = {"hausdorff_a_to_b": hausdorff.a_to_b,
              "hausdorff_b_to_a": hausdorff.b_to_a,
              "hausdorff_symmetric": hausdorff.symmetric,
              "cross_a_under_b": cross_evaluate(set_a, phi_b, ibk1, None),
              "cross_b_under_a": cross_evaluate(set_b, phi_a, ibk1, None)}
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
    return (row["solver"], row["phi_a"], row["phi_b"], row["metric"],
            row["n_evals"], row["delta"])


# the decision-block rows of a table, one per group, summarised over the seeds
def decision_table_rows(by_seed, fraction=delta_box_fraction):
    rows = []
    for key in sorted({decision_group_key(row) for row in by_seed}):
        group = [row for row in by_seed if decision_group_key(row) == key]
        rows.append(decision_table_row(key, group, fraction))
    return rows


# one summarised decision-block row of a group of per-seed rows
def decision_table_row(key, group, fraction):
    solver, phi_a, phi_b, metric, budget, delta = key
    row = {"problem": problem_name, "phi_a": phi_a, "phi_b": phi_b,
           "status": group[0]["status"], "metric": metric, "n_evals": budget,
           "cardinality_a": int(np.median([item["cardinality_a"]
                                           for item in group])),
           "cardinality_b": int(np.median([item["cardinality_b"]
                                           for item in group])),
           "delta": delta, "box_scale": box_diameter(),
           "containment_violations": violation_count(group),
           "note": measured_note(phi_a, phi_b, solver, delta, fraction,
                                 native_pair_note(phi_a, phi_b))}
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


# the key one pair's two overlap conventions are grouped by
def overlap_key(row):
    return (row["solver"], row["phi_a"], row["phi_b"], row["n_evals"], row["delta"])


# the status the rows of one group already carry, which is not pair_status
def group_status(by_seed, key):
    # the noise floor is one phi against itself and d2's pair_status has no verdict
    # for that, so the label is put on the row where the row is built and is read
    # back here rather than recomputed. recomputing it would print the floor as a
    # finding, which is exactly what its own note says it is not.
    return next(row["status"] for row in by_seed if overlap_key(row) == key)


# the two overlap conventions of one pair side by side
def overlap_convention_rows(by_seed):
    rows = []
    keys = sorted({overlap_key(row) for row in by_seed
                   if row["metric"] == "overlap"})
    for key in keys:
        dice = [row["value"] for row in by_seed
                if overlap_key(row) == key and row["metric"] == "overlap"]
        jaccard = [row["value"] for row in by_seed
                   if overlap_key(row) == key and row["metric"] == "overlap_jaccard"]
        rows.append(overlap_convention_row(key, dice, jaccard,
                                           group_status(by_seed, key)))
    return rows


# one row of the overlap file, dice and jaccard of the same pair and the same seeds
def overlap_convention_row(key, dice, jaccard, status):
    solver, phi_a, phi_b, budget, delta = key
    dice_summary = summarize_across_seeds(dice)
    jaccard_summary = summarize_across_seeds(jaccard)
    return {"problem": problem_name, "solver": solver, "phi_a": phi_a,
            "phi_b": phi_b, "status": status,
            "n_evals": budget, "delta": delta, "box_scale": box_diameter(),
            "n_seeds": dice_summary["n_seeds"],
            "dice_median": dice_summary["median"], "dice_q1": dice_summary["q1"],
            "dice_q3": dice_summary["q3"],
            "jaccard_median": jaccard_summary["median"],
            "jaccard_q1": jaccard_summary["q1"],
            "jaccard_q3": jaccard_summary["q3"]}


# the coverage and overlap statistics at a range of delta, as raw rows
def delta_sweep_rows(comparisons, budget):
    # delta is a reporting parameter and the numbers move with it,
    # docs/plan_after_meeting.md section b2, so its movement is measured here
    # rather than left as a caveat. it is computed at the reported budget only.
    rows = []
    diameter = box_diameter()
    for comparison in comparisons:
        for fraction in delta_sweep_fractions:
            for row in pair_rows_at_delta(comparison, budget, fraction * diameter):
                rows.append(dict(row, delta_box_fraction=fraction,
                                 box_scale=diameter))
    return rows


# the igd reference front of one phi, f2's derived set pushed through it
def reference_fronts_for(phi_name, n_points):
    # one reference per phi and not two: p1 needed both settings of
    # include_singular_segments because b1 left the status of those points
    # undecided, s-12, and I-BK1 has no singular weight direction at all, f2
    # section 2.3, so there is one derived set and one reference object.
    return reference_front(phi_name, int(n_points), reference_sampling_mode,
                           reference_seed)


# every configuration key of the run, at every budget
def cell_keys(settings):
    return [(solver, phi_name, budget) for solver in solver_names
            for phi_name in phi_names for budget in settings["budgets"]]


# the cardinality every front of the comparison is cut to, r-16
def comparison_cardinality(runs, settings):
    # taken over every front of the comparison, across solvers, phi, seeds and
    # both budgets and not per phi: the smallest is systematically phi_lu's, so a
    # per-phi minimum would put a phi-dependent selection inside the comparison.
    # CONTEXT.md section 10 d1. pooling the budgets as well is what makes the
    # convergence check a comparison of two numbers of one measurement.
    return common_cardinality([result.front for key in cell_keys(settings)
                               for result in runs[key]])


# one run's front cut to the comparison's cardinality at the stated seed
def truncated_front(result, n_keep):
    return truncate_to_common_cardinality(result.front, n_keep, truncation_seed)


# the truncated fronts of one phi, pooled over solvers, seeds and both budgets
def pooled_truncated(runs, phi_name, settings, n_keep):
    return [truncated_front(result, n_keep)
            for solver in solver_names
            for budget in settings["budgets"]
            for result in runs[(solver, phi_name, budget)]]


# the one hypervolume reference point of a phi, or why there is none
def hypervolume_point(rows, reference):
    # derived from every row it will be scored against, across both budgets, all
    # three solvers and all five seeds, together with the reference front, so that
    # one point serves the whole comparison and the two budgets are two
    # hypervolumes of one measurement. where a pooled column has zero range the
    # margin rule adds no thickness there, no point can strictly dominate the rows
    # and every box has zero volume, so nothing is scored and the reason is
    # returned instead.
    pooled = np.concatenate(list(rows) + [reference], axis=0)
    point = derive_reference_point(pooled, hv_rule)
    ranges = np.max(pooled, axis=0) - np.min(pooled, axis=0)
    if np.all(ranges > 0.0):
        return point, True, ""
    degenerate = [int(index) for index in np.flatnonzero(ranges <= 0.0)]
    return point, False, (
        "no hypervolume is scored: image columns {} are constant over every row, "
        "so the margin rule adds no thickness there, the point cannot strictly "
        "dominate any row and every row's box has zero volume".format(degenerate))


# raises unless the reference point strictly dominates every row it will score
def require_dominating_point(point, front, label):
    # CONTEXT.md section 10 e1, v-59: moocore clips at the reference point instead
    # of refusing, so a row beyond the point contributes nothing and the number
    # still comes back looking like a hypervolume. a front the point does not
    # dominate is refused here rather than scored.
    if not bool(np.all(np.asarray(front, dtype=float) < np.asarray(point))):
        raise ValueError(
            "the hypervolume reference point {} does not dominate every row of "
            "{}; moocore would clip the rows beyond it and return a number, so "
            "this front is refused and not scored"
            .format(np.asarray(point).tolist(), label))


# the objective-space values of one configuration, per seed and per metric
def objective_rows_by_seed(results, key, point, scorable, reference, n_keep):
    solver, phi_name, budget = key
    rows = []
    for result in results:
        front = truncated_front(result, n_keep)
        shared = {"problem": problem_name, "phi": phi_name, "solver": solver,
                  "n_evals": int(budget), "seed": int(result.seed),
                  "cardinality": int(len(front)),
                  "full_cardinality": int(len(result.front)),
                  "reference_size": len(reference),
                  "include_singular_segments": no_singular_setting}
        rows.append(dict(shared, metric="spread", value=compute_spread(front)))
        rows.append(dict(shared, metric="igd",
                         value=compute_igd(front, reference)))
        if scorable:
            require_dominating_point(point.point, front,
                                     "{} {} at budget {} seed {}".format(
                                         solver, phi_name, budget, result.seed))
            rows.append(dict(shared, metric="hypervolume",
                             value=compute_hv(front, point.point)))
    return rows


# every per-seed objective-space value, with the points the hypervolumes used
def objective_values(runs, settings):
    rows, points = [], {}
    n_keep = comparison_cardinality(runs, settings)
    for phi_name in phi_names:
        reference = reference_fronts_for(phi_name, settings["reference_points"])
        point, scorable, reason = hypervolume_point(
            pooled_truncated(runs, phi_name, settings, n_keep), reference)
        points[phi_name] = (point, scorable, reason)
        for solver in solver_names:
            for budget in settings["budgets"]:
                rows.extend(objective_rows_by_seed(
                    runs[(solver, phi_name, budget)], (solver, phi_name, budget),
                    point, scorable, reference, n_keep))
    return rows, points, n_keep


# the key an objective-space table row is summarised over its seeds by
def objective_group_key(row):
    return (row["phi"], row["solver"], row["metric"], row["n_evals"],
            row["reference_size"])


# the objective-block rows of the solver table, summarised over the seeds
def objective_table_rows(by_seed, points):
    rows = []
    for key in sorted({objective_group_key(row) for row in by_seed}, key=repr):
        group = [row for row in by_seed if objective_group_key(row) == key]
        phi_name, solver, metric, budget, size = key
        row = {"problem": problem_name, "phi": phi_name, "solver": solver,
               "metric": metric, "n_evals": budget,
               "cardinality": int(np.median([item["cardinality"]
                                             for item in group])),
               "reference_size": size, "sampling_mode": reference_sampling_mode,
               "include_singular_segments": no_singular_setting,
               "hv_reference_rule": hv_rule,
               "hv_reference_point": points[phi_name][0].point}
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


# the three solvers' fronts in one phi's image, one figure per phi
def front_figures(root, runs, budget):
    paths = []
    for phi_name in phi_names:
        fronts = [pooled_front(runs, (solver, phi_name, budget), solver)
                  for solver in solver_names]
        path = figure_root(root) / "fronts_{}_{}_{}.png".format(problem_name,
                                                               phi_name, budget)
        plot_fronts(fronts, figure_col_pairs,
                    "{} under phi_{}, the three solvers".format(problem_name,
                                                                phi_name), path)
        paths.append(path)
    return paths


# f2's derived set of one phi, sampled, as the series drawn behind the recovered ones
def derived_series(phi_name, budget):
    # src/reporting.py draws a closed-form boundary for p1 alone, that being b1's
    # region and d3's own transcription of it. I-BK1's regions are f2's and are
    # encoded in src/problems_native.py, so they enter the figure as a plotted
    # series rather than through a change to d3, and they are put first so that
    # the recovered sets are drawn over them.
    points, _ = efficient_set(phi_name, region_figure_points,
                              reference_sampling_mode, reference_seed)
    return PlottedSet(label="derived X_{}, f2 section 2.4".format(phi_name),
                      problem_name=problem_name, phi_name=phi_name, n_seeds=0,
                      n_evals=int(budget), points=points)


# one solver's decision sets under the three phi at one seed, over the derived sets
def single_seed_sets(runs, solver, budget, phi_name, seed_index=0):
    # one phi per figure and not the three together, which is where this differs
    # from e1's. on p1 the three derived regions could be drawn as three
    # boundaries behind one set of points; here every derived set is a filled
    # wedge and three of them nested overlay into one shape, so each phi gets its
    # own panel with its own derived set behind it.
    result = runs[(solver, phi_name, budget)][seed_index]
    return [derived_series(phi_name, budget),
            PlottedSet(label="phi_{}, {}".format(phi_name, solver),
                       problem_name=problem_name, phi_name=phi_name, n_seeds=1,
                       n_evals=result.n_evals, points=result.decision_vectors)]


# the recovered decision sets over f2's derived sets, one figure per solver and phi
def decision_figures(root, runs, budgets):
    paths = []
    for budget in budgets:
        for solver in solver_names:
            for phi_name in phi_names:
                path = figure_root(root) / "decision_sets_{}_{}_{}_{}.png".format(
                    problem_name, solver, phi_name, budget)
                plot_decision_sets(
                    single_seed_sets(runs, solver, budget, phi_name),
                    "{}, {}, phi_{} over f2's derived set".format(
                        problem_name, solver, phi_name), path)
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
    return [summary_row("problem", problem_name, "run parameter"),
            summary_row("seeds", " ".join(str(seed) for seed in settings["seeds"]),
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
            summary_row("truncation_seed", truncation_seed, "run parameter"),
            summary_row("dependence_points", dependence_points, "run parameter"),
            summary_row("dependence_seed", dependence_seed, "run parameter")]


# the box scale, the absolute delta it gives and the printed point measured against
def summary_scales(n_keep):
    return [summary_row("box_scale", box_diameter(), "the problem's bounds"),
            summary_row("delta", problem_delta(), "run parameter"),
            summary_row("common_cardinality", n_keep,
                        "the smallest front of the comparison, r-16"),
            summary_row("printed_x_star",
                        " ".join(repr(value) for value in printed_x_star),
                        "[16] Table 1, printed page 20"),
            summary_row("printed_g_star",
                        " ".join(repr(value) for value in printed_g_star),
                        "[16] Table 1, printed page 20")]


# the tables written and whether each phi was scored a hypervolume
def summary_artefacts(tables, points):
    rows = [summary_row("table_{}".format(name), path.name, "written here")
            for name, path in sorted(tables.items())]
    for phi_name in sorted(points):
        _, scorable, reason = points[phi_name]
        rows.append(summary_row("hypervolume_scored_{}".format(phi_name), scorable,
                                reason or "the point dominates every scored row"))
    return rows


# the run parameters and counts, as the keys the record reads its prose from
def summary_rows(settings, runs, tables, points, n_keep, elapsed):
    counts = [summary_row("n_configurations", len(runs), "the run grid"),
              summary_row("n_runs", sum(len(value) for value in runs.values()),
                          "the run grid"),
              summary_row("wall_seconds", elapsed, "the run grid")]
    return (summary_parameters(settings) + counts + summary_scales(n_keep)
            + summary_artefacts(tables, points))


# the gap between the exact pair statistic and the measured one, per pair and metric
def instrument_error_rows(exact_rows, measured_rows, budget):
    # the calibration, docs/plan_after_meeting.md section b3, on a second problem.
    # the exact row and the measured row are the same quantity derived and
    # measured, so their difference is the instrument's error; p1 was the only
    # place it could be computed until I-BK1's derivation closed.
    rows = []
    for exact in exact_rows:
        for measured in find_rows(measured_rows, exact["phi_a"], exact["phi_b"],
                                  exact["metric"], budget):
            rows.append(error_row(exact, measured, budget))
    return rows


# one instrument-error row, the exact value against the measured one
def error_row(exact, measured, budget):
    # both the absolute and the relative gap, because
    # docs/part1/part1_closing.md section 3.2 states p1's error in the relative
    # form and a second measurement of the same bias has to be read against it.
    return {"problem": problem_name, "phi_a": exact["phi_a"],
            "phi_b": exact["phi_b"], "status": exact["status"],
            "metric": exact["metric"], "n_evals": budget,
            "delta": measured["delta"], "box_scale": measured["box_scale"],
            "exact": exact["median"], "measured_median": measured["median"],
            "measured_q1": measured["q1"], "measured_q3": measured["q3"],
            "error": measured["median"] - exact["median"],
            "relative_error": measured["median"] / exact["median"] - 1.0}


# which way the instrument's error runs on this problem, counted from the file
def error_direction_note(rows):
    # on p1 every row of e1's calibration ran the same way and the instrument was
    # measured to overstate agreement. here the direction is not uniform, so the
    # counts are taken from the file rather than asserted and the rows that run
    # the other way are named.
    zero = [row for row in rows if float(row["delta"]) == zero_delta]
    below = [row for row in zero if float(row["error"]) < 0.0]
    above = [row for row in zero if float(row["error"]) > 0.0]
    lines = ["", "**the direction of the error, counted from the file.** at delta "
             "zero {} of the {} rows measure above the exact value and {} below "
             "it; the rest land exactly on it.".format(len(above), len(zero),
                                                       len(below)), ""]
    return lines + ([] if not below else error_direction_below(below))


# what the rows measuring below the exact value are, and what they are not
def error_direction_below(below):
    named = ", ".join("{} against {} on {}".format(row["phi_a"], row["phi_b"],
                                                   row["metric"])
                      for row in below)
    return ["the rows landing exactly on the exact value are the ones a "
            "containment fixes: docs/part1/a_close_containment.md puts ND_lu and "
            "ND_cw inside ND_ls for every problem, and the recovered sets carry "
            "both with a containment violation count of zero in table 2, so those "
            "coverages are one in the derivation and one in the measurement "
            "alike. **what measures below is {}**, and it is the one direction no "
            "containment covers: f2 section 3.1's nesting of X_cw inside X_lu is a "
            "statement about the derived regions and not about the finite "
            "non-dominated sets of a sample, which need not nest for that pair. "
            "that is a gap between two different objects and not a disagreement "
            "with the derivation.".format(named), ""]


# the measured rows of one pair and metric at one budget, one per delta
def find_rows(rows, phi_a, phi_b, metric, budget):
    return [row for row in rows
            if (row["phi_a"], row["phi_b"], row["metric"],
                row["n_evals"]) == (phi_a, phi_b, metric, budget)]


# the rows of a written table's decision block, filtered to a stated budget
def decision_rows_at(path, budget=None):
    rows = read_metrics_table(path)[decision_block]
    return [row for row in rows if budget is None or row["n_evals"] == budget]


# the record's opening: what was run, read back out of summary.csv
def record_opening(summary, tables):
    lines = ["# f3: the native run, on I-BK1", "",
             "generated by experiments/run_native.py. every number below is read "
             "back out of a file that script wrote, and the file and the key are "
             "named beside it; nothing here is typed. re-running the script from "
             "the same seeds regenerates this document with the same numbers.", "",
             "the problem is I-BK1, problem 1 of appendix A of [16], printed page "
             "27, encoded in src/problems_native.py. **its imprecision is in its "
             "published coefficients**: no uncertainty was added, no width "
             "function was written and the project chose nothing about it. its "
             "phi-efficient sets are docs/part2/f2_ibk1_derivation.md section "
             "2.4's, derived there and encoded here.", "",
             "## 1. what was run", "",
             "from results/part2/summary.csv, one key per row:", ""]
    lines.extend(markdown_table(("key", "value", "source"), summary))
    lines.extend(["", "the run grid is every solver of slide 17 under every phi of "
                  "[1] on I-BK1 at every budget above, at each seed. the second "
                  "budget is the convergence check: the whole grid repeated at "
                  "four times the first, with the hypervolume reference point and "
                  "the truncation cardinality derived once across both so that the "
                  "two are two measurements of one quantity.", ""])
    lines.extend(["the tables written, all through src/reporting.py's "
                  "save_metrics_table:", ""])
    lines.extend(["- results/part2/{}".format(path.name)
                  for path in sorted(tables.values(), key=lambda item: item.name)])
    return lines + [""]


# the record's exact table, table 1, the second calibration row the project has
def record_exact(path, exact_path):
    lines = ["## 2. table 1, exact", "",
             "the closed-form pair statistics of docs/part2/f2_ibk1_derivation.md "
             "section 2.4's derived regions, integrated in closed form by this "
             "script from their bands of nu. no seed, no budget, no solver and no "
             "tolerance enter them. **this is the project's second calibration "
             "row and the first on a problem nobody adapted**, "
             "docs/part1/part1_closing.md section 7.3. source: results/part2/{}, "
             "decision block; the areas, the intersections, the bands and both "
             "overlap conventions are in results/part2/{}."
             .format(path.name, exact_path.name), ""]
    lines.extend(markdown_table(("phi_a", "phi_b", "status", "metric", "median"),
                                decision_rows_at(path)))
    lines.extend(["", "the overlap column is d2's convention, twice the shared "
                  "measure over the sum of the two, which is what "
                  "src/metrics_decision.py's compute_overlap tends to on uniformly "
                  "sampled sets and is what makes this row and the measured row "
                  "the same quantity. the shared fraction of the union, jaccard, "
                  "is a different functional and is in results/part2/{} under the "
                  "key overlap_union_share.".format(exact_path.name), ""])
    return lines


# the areas and the bands the exact table is computed from
def record_regions(rows, exact_path):
    lines = ["### the three regions", "",
             "each derived set is the wedge of a closed interval of "
             "nu = x_2 (5 - x_1) / (x_1 (5 - x_2)) over [0, 5]^2, f2 section 2.4, "
             "and its lebesgue measure is 25 [ I(L) - I(R) ] with "
             "I(c) = c ln c / (c - 1)^2 + 1 / (1 - c), f2 section 3.1. source: "
             "results/part2/{}.".format(exact_path.name), ""]
    wanted = ("band_lower", "band_upper", "area")
    values = {(row["quantity"], row["phi_a"]): row["value"] for row in rows}
    table = [{"phi": name, "band_lower": values[("band_lower", name)],
              "band_upper": values[("band_upper", name)],
              "area": values[("area", name)]} for name in phi_names
             if all((quantity, name) in values for quantity in wanted)]
    lines.extend(markdown_table(("phi", "band_lower", "band_upper", "area"), table))
    lines.extend(["", "the intersections and the jaccard values of the three "
                  "pairs, from the same file:", ""])
    pairs = [row for row in rows if row["quantity"] in ("intersection_area",
                                                        "overlap_union_share")]
    return lines + markdown_table(("quantity", "phi_a", "phi_b", "value"),
                                  pairs) + [""]


# the record's measured table, table 2, and its noise floor
def record_measured(path, budgets):
    lines = ["## 3. table 2, measured, at both budgets", "",
             "measured on random search's one filtered sample, through "
             "src/metrics_decision.py's compare_phi_on_one_sample: one uniform "
             "sample of the box, evaluated once, filtered under each phi in turn, "
             "so the three sets differ only through the order. the sets are the "
             "full recovered ones and are not truncated, CONTEXT.md section 10 d1. "
             "source: results/part2/{}, decision block; the per-seed values behind "
             "every median are in results/part2/decision_metrics_by_seed.csv and "
             "the jaccard value of every pair is in "
             "results/part2/overlap_conventions.csv.".format(path.name), "",
             "every pair appears at two values of delta and the delta column "
             "separates them. **at delta zero the number is the shared count over "
             "the count, with no tolerance in it**: the three sets of one "
             "comparison are index sets over one array, so two decision vectors "
             "are the same point bitwise or they are two points, and that row is "
             "the measured counterpart of table 1 with the tolerance removed "
             "rather than made small. the second value is one twentieth of the box "
             "diameter and is the value at which the row can be read against the "
             "noise floor below.", ""]
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
    return markdown_table(("phi_a", "phi_b", "status", "metric", "cardinality_a",
                           "cardinality_b", "median", "q1", "q3", "delta",
                           "containment_violations"), rows)


# the same-phi seed-to-seed rows of table 2, and what they are for
def record_noise_floor(path):
    lines = ["### the noise floor", "",
             "one phi against itself at two seeds, so no order difference can "
             "appear in it; a cross-phi number that does not exceed it is not "
             "evidence of anything, docs/plan_after_meeting.md section b1. it is "
             "computed at the positive delta only, two independent uniform samples "
             "sharing no point at all and the floor at delta zero being zero by "
             "construction.", "",
             "**the scale matters more here than on p1 and the floor is where it "
             "shows.** [16]'s box is much larger than the part of it the derived "
             "sets occupy, f2 section 2.5 putting all three inside the positive "
             "quadrant the two objectives are supported on, so a delta stated as "
             "a fraction of the box diameter is a larger fraction of the sets on "
             "I-BK1 than the same fraction was on p1. the delta sweep of section "
             "9 is what says at which fractions the statistic still separates "
             "anything, and the delta zero rows are the ones that carry the "
             "comparison with table 1.", ""]
    floor = [row for row in decision_rows_at(path)
             if row["phi_a"] == row["phi_b"] and row["metric"] in
             ("coverage_a_in_b", "coverage_b_in_a", "overlap")]
    return lines + markdown_table(("phi_a", "metric", "n_evals", "cardinality_a",
                                   "cardinality_b", "median", "q1", "q3"), floor)


# the cross evaluation and the symmetric hausdorff, at the reported budget
def record_cross_evaluation(path, budget):
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
    return lines + markdown_table(("phi_a", "phi_b", "status", "metric",
                                   "cardinality_a", "cardinality_b", "median",
                                   "q1", "q3"), rows)


# the record's instrument-error section, the second measurement of the same bias
def record_instrument_error(rows, path, budget):
    lines = ["## 4. the instrument's error, measured a second time", "",
             "I-BK1 is in both tables and the difference between its two rows is "
             "the gap between the quantity derived and the same quantity measured "
             "on recovered sets at budget {}. **this is the number that matters "
             "most in this run**: docs/part1/part1_closing.md section 3.2 records "
             "the same gap on p1, a problem the project built, and this is the "
             "same gap on a problem of a different origin. every other row of "
             "table 2 is read subject to it. source: results/part2/{}."
             .format(budget, path.name), ""]
    lines.extend(markdown_table(("phi_a", "phi_b", "status", "metric", "delta",
                                 "exact", "measured_median", "measured_q1",
                                 "measured_q3", "error", "relative_error"), rows))
    lines.extend(error_direction_note(rows))
    lines.extend(["", "the error is the measured median minus the exact value and "
                  "the relative error is that gap over the exact value, which is "
                  "the form part1_closing section 3.2 states p1's in. the delta "
                  "zero rows carry three of the five things "
                  "docs/plan_after_meeting.md section b2 lists as lost between the "
                  "exact statement and the measured one: measure becomes count, "
                  "derived becomes recovered, and the sets are what a finite "
                  "budget found. the positive delta rows carry the fourth as well, "
                  "the tolerance. **this script measures the gap and does not "
                  "interpret it**, and it does not compare it with p1's: that "
                  "comparison is the write-up's and it belongs beside "
                  "results/tier0/instrument_error_p1.csv, which this script does "
                  "not read.", ""])
    return lines


# the three phi pairs, and the convention that does not apply on this problem
def record_pairs(exact_rows):
    lines = ["## 5. the three phi pairs, and which is which", "",
             "**on I-BK1 there is no non-nested pair at all.** f2 section 3.1 "
             "derives X_cw strictly inside X_lu strictly inside X_ls from the "
             "closed forms, exactly and without a sample, and the coverages of "
             "table 1 carry it: one direction of every one of the three pairs is "
             "exactly one.", "",
             "docs/part1/a_close_containment.md predicts two of the three from the "
             "criterion that phi_B = M phi_A with M entrywise non-negative and "
             "invertible makes phi_A-dominance imply phi_B-dominance, and "
             "src/metrics_decision.py labels those two a check. the third is not "
             "predicted in either direction and on p1 the two orders genuinely "
             "crossed; **here it nests, and that is f2 section 3.2's finding about "
             "I-BK1 rather than a difference this run measured**.", ""]
    lines.extend(markdown_table(("phi_a", "phi_b", "status", "metric", "exact"),
                                pair_coverage_table(exact_rows)))
    return lines + record_pairs_consequence()


# the coverages of table 1, one row per pair and direction, for the pairs section
def pair_coverage_table(exact_rows):
    return [{"phi_a": row["phi_a"], "phi_b": row["phi_b"],
             "status": row["status"], "metric": row["metric"],
             "exact": row["median"]} for row in exact_rows
            if row["metric"] in ("coverage_a_in_b", "coverage_b_in_a")]


# what the nesting costs the headline convention, said in the record's own words
def record_pairs_consequence():
    return ["", "**the consequence for the headline.** "
            "docs/part1/part1_closing.md section 3.1 takes the study's headline "
            "pair to be phi_lu against phi_cw because on p1 it is the only pair "
            "nested in neither direction, so it is the only one where nothing is "
            "fixed before a solver runs. that convention does not apply on "
            "I-BK1: every pair is nested, so on this problem one direction of "
            "every pair is fixed before anything runs, and **no pair of this run "
            "may be presented as a measured difference between two orders**. "
            "what the run measures here is the instrument, section 4, and not a "
            "separation.", "",
            "what does separate on I-BK1 is the size of the three sets, and that "
            "is exact: the areas are in section 2 and the reverse coverages, the "
            "share of the larger set of a pair lying outside the smaller, are "
            "one minus the coverages in the table above. those are derived "
            "quantities and carry no instrument error at all.", ""]


# the counterexample, measured on the solvers' own output
def record_dominators(rows, path, budget, point, printed_row):
    lines = ["## 6. [16]'s Table 1 point, measured against the solvers' output", "",
             "docs/part2/f2_ibk1_derivation.md section 4.2 establishes by algebra "
             "that x* = ({}), the point [16]'s algorithm 1 returns on I-BK1 at "
             "Table 1 printed page 20, is dominated in all four endpoint values "
             "and is therefore not a Pareto optimal point of I-BK1 in [16]'s own "
             "definition 2.17. **that claim is f2's and is not made here.** what "
             "is measured here is a different question with the same subject: run "
             "without being told any of it, do the solvers return points that beat "
             "the paper's printed row, which is ({}). both are read back out of "
             "results/part2/summary.csv, where this run wrote them from the "
             "paper.".format(point, printed_row), "",
             "the relation is [16]'s own, its definition 2.2 printed page 4, "
             "componentwise on the endpoint pair of each objective, so it does not "
             "depend on which phi the solver was run under; a row counts when all "
             "four of its endpoint values are strictly below the printed row, "
             "which is a witness against definition 2.16's weak form as well. the "
             "margin of a row is the smallest of its four gaps and the widest "
             "margin is the largest of those over the set. source: "
             "results/part2/{}, with the per-seed counts in "
             "results/part2/dominators_by_seed.csv.".format(path.name), ""]
    lines.extend(markdown_table(("solver", "phi", "n_evals", "cardinality",
                                 "n_seeds", "seeds_with_a_dominator", "median",
                                 "q1", "q3", "widest_margin_over_seeds"),
                                [row for row in rows
                                 if int(row["n_evals"]) == budget]))
    return lines + record_dominators_reading()


# how the domination table is to be read, and what it is not
def record_dominators_reading():
    return ["", "the median column is the number of returned points beating the "
            "printed row, over the seeds, at the cardinality beside it. the rows "
            "at the convergence budget are in the same file. **this is a "
            "measurement about what the solvers found and not a claim about the "
            "paper**; f2 section 4.3 identifies the mechanism and records it as "
            "ambiguity a-11.", ""]


# the free sets, and why the registered overhang is not computed on this problem
def record_free_sets(rows):
    lines = ["## 7. x-01's condition, and why it is absent here", "",
             "the protected-minimiser condition of "
             "docs/part1/part1_closing.md section 3.4 applies at a pair (problem, "
             "phi) exactly when some image column has a non-empty free set, that "
             "is when some column is a function of a strict subset of the decision "
             "variables. this run measures the free sets rather than asserting "
             "them, by redrawing each decision variable in turn over a sample and "
             "asking which columns move. source: results/part2/free_sets.csv.", ""]
    lines.extend(markdown_table(("phi", "column", "depends_on", "free_set",
                                 "free_set_size", "constant_column"), rows))
    return lines + record_free_sets_verdict(rows)


# what the free-set table decides about m-2, and what the absence itself says
def record_free_sets_verdict(rows):
    with_free = [row for row in rows if int(row["free_set_size"]) > 0]
    return ["", "**{} of the {} image columns has a non-empty free set.** that is "
            "what f2 section 1.2 predicts from the forms: every one of the twelve "
            "image coordinates of I-BK1 is a diagonal quadratic in both variables "
            "with strictly positive coefficients, because [16] put a "
            "non-degenerate interval on both terms of both objectives, so no "
            "column can be minimised without constraining both coordinates."
            .format(len(with_free), len(rows)), "",
            "**so m-2, x-01's overhang, is not computed on this problem and the "
            "absence is the result.** the estimator is the distance from the free "
            "coordinates of a column's minimiser to the derived set's projection "
            "onto them; over no coordinates it returns zero by construction, "
            "which is a property of the estimator and not a measurement, so it is "
            "not written. **I-BK1 is the first problem in the project where the "
            "effect is structurally absent under every phi**: on p1 it is absent "
            "under example 2.2 and present under the other two, on zdt1 present "
            "under all three and on dtlz2 absent under example 2.2 alone. m-1 is "
            "withdrawn as an instrument at x-01's outcome line and is not "
            "computed, not revived and not re-thresholded.", ""]


# the record's solver table, the objective-space metrics and the solver pairs
def record_solvers(path, points, n_keep):
    lines = ["## 8. table 3, the solvers", "",
             "the objective-space metrics are valid for comparing solvers under "
             "one fixed phi and are never a ranking of phi, CONTEXT.md section 5 "
             "step 5. they are computed at the common cardinality of the whole "
             "comparison, {} rows, r-16 and CONTEXT.md section 10 d1, taken across "
             "solvers, phi, seeds and both budgets. **e1's tier 0 objective block "
             "is at full cardinality and this one is truncated, so the two are not "
             "comparable and may not be placed side by side**, "
             "docs/part1/part1_closing.md section 3.5. the decision block of the "
             "same file holds the pair statistics of nsga-ii's and mopso's own "
             "output, where phi drives the search as well as the ordering, so "
             "those rows are a question about the solvers and never a pair number "
             "of the study. source: results/part2/{}; the per-seed values are in "
             "results/part2/objective_metrics_by_seed.csv and "
             "results/part2/decision_metrics_by_seed.csv.".format(n_keep,
                                                                 path.name),
             "", "igd is against f2's derived set of the same phi, sampled at the "
             "stated size in the {} mode, r-13. include_singular_segments is False "
             "on every row and is a no-op and not a choice: **I-BK1 has no "
             "singular weight direction under any phi**, f2 section 2.3, so s-12 "
             "does not arise on this problem and there is one derived set rather "
             "than two.".format(reference_sampling_mode), "",
             "the hypervolume reference point, one per phi, derived by the {} rule "
             "from every row scored against it across both budgets, all three "
             "solvers and every seed, together with the reference front:"
             .format(hv_rule), ""]
    lines.extend(markdown_table(("key", "value", "source"), points))
    return lines + [""]


# the objective-space block of the solver table, at one budget
def record_objective_metrics(path, budget):
    lines = ["", "the objective-space metrics at budget {}; the same rows at the "
             "convergence budget are in the same file. every row is a median with "
             "its interquartile range over the seeds, at the cardinality stated "
             "beside it, and a ratio taken across two phi here is a ratio of "
             "volumes in two different spaces and means nothing.".format(budget),
             ""]
    rows = [row for row in read_metrics_table(path)[objective_block]
            if row["n_evals"] == budget]
    return lines + markdown_table(("phi", "solver", "metric", "cardinality",
                                   "reference_size", "median", "q1", "q3"), rows)


# the population solvers' own pair rows, and what they may be read as
def record_solver_pairs(path, budget):
    lines = ["", "the population solvers' own pairs at budget {}, at one twentieth "
             "of the box diameter. in nsga-ii and mopso phi drives the search as "
             "well as the ordering, so a difference between two of their runs is a "
             "difference of orders and of trajectories at once and these rows are "
             "never a pair number of the study.".format(budget), ""]
    rows = [row for row in decision_rows_at(path, budget)
            if row["metric"] in ("coverage_a_in_b", "coverage_b_in_a", "overlap")]
    return lines + markdown_table(("phi_a", "phi_b", "status", "metric",
                                   "cardinality_a", "cardinality_b", "median",
                                   "q1", "q3", "delta"), rows) + [""]


# the delta sweep, so that the reporting parameter's effect is a measured artefact
def record_delta_sweep(rows, budget):
    lines = ["## 9. the delta sweep", "",
             "delta is a reporting parameter and the numbers move with it, "
             "docs/plan_after_meeting.md section b2, so its movement is measured "
             "here rather than left as a caveat. the coverage and overlap "
             "statistics of the three pairs at budget {}, over six fractions of "
             "the box diameter. source: results/part2/delta_sweep.csv."
             .format(budget), ""]
    wanted = [row for row in rows if row["metric"] == "coverage_a_in_b"]
    return lines + markdown_table(("phi_a", "phi_b", "metric",
                                   "delta_box_fraction", "delta", "median", "q1",
                                   "q3"), wanted) + [""]


# the delta sweep summarised over the seeds, one row per pair, metric and fraction
def delta_sweep_summary(root, budget):
    rows = [row for row in read_table(root / "delta_sweep.csv")
            if int(row["n_evals"]) == budget]
    summary = []
    keys = sorted({(row["phi_a"], row["phi_b"], row["metric"],
                    row["delta_box_fraction"], row["delta"]) for row in rows})
    for phi_a, phi_b, metric, fraction, delta in keys:
        values = [float(row["value"]) for row in rows
                  if (row["phi_a"], row["phi_b"], row["metric"],
                      row["delta_box_fraction"], row["delta"]) == (
                          phi_a, phi_b, metric, fraction, delta)]
        entry = {"phi_a": phi_a, "phi_b": phi_b, "metric": metric,
                 "delta_box_fraction": float(fraction), "delta": float(delta)}
        entry.update(summarize_across_seeds(values))
        summary.append(entry)
    return summary


# the figures, named with what each one shows
def record_figures(paths, root):
    lines = ["## 10. the figures", "",
             "written to results/part2/figures/ by src/reporting.py. the "
             "decision-space figures draw f2's derived set of that phi behind the "
             "recovered points, one phi per panel: src/reporting.py draws a "
             "closed-form boundary for p1 alone, that being b1's region and d3's "
             "own transcription of it, so I-BK1's derived sets enter as a plotted "
             "series rather than through a change to another subpart's module. "
             "the paths are relative to the run's output root, results/part2.",
             ""]
    # sorted, and not in the order they were drawn, so that the list a run writes
    # and the list a rebuild reads off the directory are one list.
    lines.extend("- {}".format(Path(path).relative_to(root).as_posix())
                 for path in sorted(paths))
    return lines + [""]


# what this run answers, and the clause it does not close
def record_closing():
    return ["## 11. what this run answers and what it does not", "",
            "**clause c5 of docs/part1/part1_closing.md section 7.1 stays marked "
            "unsupported and this document does not move it.** c5 is the claim "
            "that the behaviour persists on problems interval-valued at source, "
            "and it is about measured behaviour under the project's own "
            "instrument. what this run supplies is the measurement: a second "
            "calibration row, section 2, the same quantities measured beside it, "
            "section 3, and the gap between them, section 4. **whether that "
            "evidence supports c5 is a judgement and it is the write-up's, f4's, "
            "not a script's.**", "",
            "three things this run establishes that are not about c5.", "",
            "**the pair convention does not transfer.** on I-BK1 all three pairs "
            "nest, section 5, so the headline pair of "
            "docs/part1/part1_closing.md section 3.1 has no counterpart here and "
            "no row of this run is a measured difference between two orders. that "
            "is a second geometry beside p1's and not a confirmation of it.", "",
            "**the paper's own Table 1 point is beaten by the solvers**, section "
            "6, independently of f2's algebra and by a different route. reported "
            "as a measurement; the claim about the paper is "
            "docs/part2/f2_ibk1_derivation.md section 4.2's and its mechanism is "
            "section 4.3's, recorded as ambiguity a-11.", "",
            "**the protected-minimiser condition is structurally absent**, section "
            "7, on every column and under every phi, which is the first problem in "
            "the project where that happens. it is a fact about I-BK1's "
            "coefficients and not about any phi.", "",
            "this document is generated and re-running the script must reproduce "
            "it exactly, so nothing interpretive that a later session might want "
            "to edit belongs in it. the reading is f4's."]


# the whole record, assembled from the files this run wrote and from nothing else
def write_record(record_path, root, tables, paths, budget):
    summary = read_table(root / "summary.csv")
    n_keep = summary_value(summary, "common_cardinality")
    lines = record_opening(summary, tables)
    lines.extend(record_exact(tables["1_exact_ibk1"],
                              root / "exact_regions_ibk1.csv"))
    lines.extend(record_regions(read_table(root / "exact_regions_ibk1.csv"),
                                root / "exact_regions_ibk1.csv"))
    lines.extend(record_measured(tables["2_measured"], sorted_budgets(summary)))
    lines.extend(record_instrument_error(
        read_table(root / "instrument_error_ibk1.csv"),
        root / "instrument_error_ibk1.csv", budget))
    lines.extend(record_pairs(decision_rows_at(tables["1_exact_ibk1"])))
    lines.extend(record_dominators(read_table(root / "dominators_summary.csv"),
                                   root / "dominators_summary.csv", budget,
                                   as_tuple(summary_value(summary,
                                                          "printed_x_star")),
                                   as_tuple(summary_value(summary,
                                                          "printed_g_star"))))
    lines.extend(record_free_sets(read_table(root / "free_sets.csv")))
    lines.extend(record_solvers(tables["3_solvers"], hypervolume_summary(summary),
                                n_keep))
    lines.extend(record_objective_metrics(tables["3_solvers"], budget))
    lines.extend(record_solver_pairs(tables["3_solvers"], budget))
    lines.extend(record_delta_sweep(delta_sweep_summary(root, budget), budget))
    lines.extend(record_figures(paths, root))
    lines.extend(record_closing())
    record_path.parent.mkdir(parents=True, exist_ok=True)
    record_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return record_path


# one key of summary.csv, so that the record reads a value and never a global
def summary_value(summary, key):
    return next(row["value"] for row in summary if row["key"] == key)


# a space-joined summary value written back as the tuple it came from
def as_tuple(value):
    return ", ".join(value.split())


# the budgets of the run, read back out of summary.csv rather than from a global
def sorted_budgets(summary):
    return [int(budget) for budget in summary_value(summary, "budgets").split()]


# the hypervolume rows of summary.csv, which say what was scored and what was not
def hypervolume_summary(summary):
    return [row for row in summary if row["key"].startswith("hypervolume_scored")]


# the field order of every raw csv this script writes
raw_fieldnames = {
    "raw_manifest.csv": ("problem", "solver", "phi", "n_evals", "n_runs", "file"),
    "exact_regions_ibk1.csv": ("quantity", "phi_a", "phi_b", "value"),
    "decision_metrics_by_seed.csv": ("problem", "solver", "phi_a", "phi_b",
                                     "status", "metric", "n_evals", "seed",
                                     "cardinality_a", "cardinality_b", "delta",
                                     "containment_violations", "value"),
    "objective_metrics_by_seed.csv": ("problem", "phi", "solver", "metric",
                                      "n_evals", "seed", "cardinality",
                                      "full_cardinality", "reference_size",
                                      "include_singular_segments", "value"),
    "overlap_conventions.csv": ("problem", "solver", "phi_a", "phi_b", "status",
                                "n_evals", "delta", "box_scale", "n_seeds",
                                "dice_median", "dice_q1", "dice_q3",
                                "jaccard_median", "jaccard_q1", "jaccard_q3"),
    "delta_sweep.csv": ("problem", "solver", "phi_a", "phi_b", "status", "metric",
                        "n_evals", "seed", "delta_box_fraction", "delta",
                        "box_scale", "cardinality_a", "cardinality_b",
                        "containment_violations", "value"),
    "free_sets.csv": ("problem", "phi", "column", "depends_on", "free_set",
                      "free_set_size", "constant_column"),
    "dominators_by_seed.csv": ("problem", "solver", "phi", "n_evals", "seed",
                               "cardinality", "n_dominating", "share_dominating",
                               "widest_margin", "widest_x_1", "widest_x_2"),
    "dominators_summary.csv": ("problem", "solver", "phi", "n_evals", "n_seeds",
                               "seeds_with_a_dominator", "cardinality", "median",
                               "q1", "q3", "iqr", "widest_margin_over_seeds"),
    "instrument_error_ibk1.csv": ("problem", "phi_a", "phi_b", "status", "metric",
                                  "n_evals", "delta", "box_scale", "exact",
                                  "measured_median", "measured_q1", "measured_q3",
                                  "error", "relative_error"),
    "summary.csv": ("key", "value", "source"),
}


# writes one of the run's raw csv files, in the field order stated above
def write_raw_table(root, name, rows):
    return write_table(Path(root) / name, raw_fieldnames[name], rows)


# a metrics table through d3, with both blocks and the names save_table gives them
def save_table(root, name, decision_rows, objective_rows):
    path = Path(root) / "table_{}.csv".format(name)
    save_metrics_table({decision_block: decision_rows,
                        objective_block: objective_rows}, path)
    return path


# the exact regions, table 1, and the raw file the bands and jaccards live in
def write_exact(root):
    write_raw_table(root, "exact_regions_ibk1.csv", exact_region_rows())
    return save_table(root, "1_exact_ibk1", exact_table_rows(), [])


# every per-seed decision-space row, random search's pairs and the solvers' own
def all_decision_rows(runs, comparisons, settings):
    measured, solver_rows = [], []
    delta = problem_delta()
    for budget in settings["budgets"]:
        found = comparisons[budget]
        measured.extend(decision_rows_by_seed(found, budget))
        for comparison in found:
            measured.extend(pair_rows_at_delta(comparison, budget, zero_delta))
        measured.extend(noise_floor_rows(found, budget))
        for solver in ("nsga2", "mopso"):
            solver_rows.extend(solver_pair_rows(runs, solver, budget, delta))
    return measured, solver_rows


# the measured pair table and the per-seed rows behind it, table 2
def write_measured(root, measured_by_seed):
    write_raw_table(root, "decision_metrics_by_seed.csv", measured_by_seed)
    write_raw_table(root, "overlap_conventions.csv",
                    overlap_convention_rows(measured_by_seed))
    return save_table(root, "2_measured",
                      decision_table_rows(block_admissible(measured_by_seed)), [])


# the solver table, the objective-space metrics beside the solvers' own pairs
def write_solvers(root, objective_by_seed, solver_by_seed, points):
    write_raw_table(root, "objective_metrics_by_seed.csv", objective_by_seed)
    return save_table(root, "3_solvers",
                      decision_table_rows(block_admissible(solver_by_seed)),
                      objective_table_rows(objective_by_seed, points))


# the instrument's error, the exact row against the measured one
def write_instrument_error(root, tables, budget):
    return write_raw_table(
        root, "instrument_error_ibk1.csv",
        instrument_error_rows(decision_rows_at(tables["1_exact_ibk1"]),
                              decision_rows_at(tables["2_measured"]), budget))


# the free sets, measured and not asserted, and the m-2 decision they carry
def write_free_sets(root):
    rows = free_set_rows()
    write_raw_table(root, "free_sets.csv", rows)
    return rows


# the domination counts against [16]'s printed row, per seed and summarised
def write_dominators(root, runs, settings):
    rows = dominator_rows(runs, settings)
    write_raw_table(root, "dominators_by_seed.csv", rows)
    return write_raw_table(root, "dominators_summary.csv",
                           dominator_summary_rows(rows))


# every artefact between the runs and the record, and the tables they are in
def write_artefacts(root, runs, comparisons, settings):
    announce("computing the exact regions and the decision-space metrics")
    tables = {"1_exact_ibk1": write_exact(root)}
    measured_by_seed, solver_by_seed = all_decision_rows(runs, comparisons, settings)
    tables["2_measured"] = write_measured(root, measured_by_seed)
    announce("computing the objective-space metrics")
    objective_by_seed, points, n_keep = objective_values(runs, settings)
    tables["3_solvers"] = write_solvers(root, objective_by_seed, solver_by_seed,
                                        points)
    write_raw_table(root, "delta_sweep.csv",
                    delta_sweep_rows(comparisons[settings["budgets"][0]],
                                     settings["budgets"][0]))
    write_instrument_error(root, tables, settings["budgets"][0])
    announce("measuring the free sets and the domination counts")
    write_free_sets(root)
    write_dominators(root, runs, settings)
    return tables, points, n_keep


# the whole run: the grid, the artefacts, the tables, the figures and the record
def run(output_root, record_path, settings):
    started = time.time()
    root = Path(output_root)
    runs, comparisons = execute_grid(settings)
    announce("saving raw results")
    save_raw(root, runs)
    tables, points, n_keep = write_artefacts(root, runs, comparisons, settings)
    announce("drawing figures")
    paths = all_figures(root, runs, settings)
    write_raw_table(root, "summary.csv",
                    summary_rows(settings, runs, tables, points, n_keep,
                                 time.time() - started))
    announce("writing the record")
    write_record(Path(record_path), root, tables, paths, settings["budgets"][0])
    return tables


# the tables of a run already on disk, by the names save_table gives them
def artefact_tables(root):
    return {name: root / "table_{}.csv".format(name)
            for name in ("1_exact_ibk1", "2_measured", "3_solvers")}


# the figures of a run already on disk, in the order the record lists them
def artefact_figures(root):
    return sorted((root / "figures").glob("*.png"))


# every configuration of a run already on disk, read back from its raw arrays
def artefact_runs(root, settings):
    return {(solver, phi_name, budget):
            load_raw_runs(raw_path(root, (solver, phi_name, budget)))
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
    parser = argparse.ArgumentParser(description="f3, the native run on I-BK1")
    parser.add_argument("--output-root", default=str(repository_root / "results"
                                                     / "part2"))
    parser.add_argument("--record", default=str(repository_root / "docs" / "part2"
                                                / "f3_native_run.md"))
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
