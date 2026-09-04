# tests for e2, experiments/run_tier1.py.
#
# what is worth testing in an experiment script, and what is not. the numbers the
# run returns are the result and cannot be asserted in advance; what can be
# asserted is that the instrument computing them is the one it says it is. so
# these tests check five things and nothing else:
#
#   the free sets. the run decides which columns m-2 is computed on by measuring
#   which decision variables each image column moves with, and
#   docs/plan_after_meeting.md section f3 states those sets for the a5 forms by
#   hand. a5-b moved which variable each half-width reads, so the sets are
#   restated here for the forms src/problems_tier1.py now carries and the
#   measurement must agree with them, or the registered prediction is being read
#   on the wrong columns.
#
#   the effective column counts. a5-b's whole point is that no two image columns
#   coincide as functions at any positive imprecision level, r-20, and that at
#   eps = 0 they do, every half-width being zero there. the run measures both and
#   this file asserts what the measurement must return.
#
#   the two overlap conventions. jaccard is computed from dice by an identity,
#   d-09, and the identity is checked against jaccard counted directly from two
#   index sets rather than against itself.
#
#   the shortcut. the script builds random search's fronts out of the one filtered
#   sample rather than calling run_random_search a second time, so that one seed
#   costs one filter pass. that is only sound if the two agree exactly, and this
#   file asserts they do, front and decision vectors, bitwise.
#
#   the callback. the rank-1 series is read out of the algorithm's state through a
#   pymoo Callback, and an instrument that perturbed the run would be measuring
#   something else. the front is asserted bit-identical to src/runners.py's own at
#   the same seed, which is the check docs/c3_validation.md section 5.1 made of
#   the same instrument.
#
# and one end-to-end run at a small budget, marked slow, which asserts that every
# artefact is written and that a second run from the same seeds reproduces every
# one of them byte for byte, which is the whole of "re-runnable to the same
# numbers from the same seeds".

import numpy as np
import pytest

import run_tier1 as e2
from problems_tier1 import crisp_level, dtlz2_interval, zdt1_interval
from random_search import filter_one_sample_under_every_phi, run_random_search
from reporting import decision_block, read_metrics_table
from runners import run_solver

# every decision variable of a problem except the ones stated
def all_but(n_vars, excluded):
    return [index for index in range(n_vars) if index not in excluded]


# the variables each image column of a5-b's forms depends on, read by hand.
# zdt1's half-widths read x_30 and x_29, which are indices 29 and 28, and dtlz2's
# read x_12, x_11 and x_10, which are 11, 10 and 9. the centre columns are read
# off [2] equation (7) and [3] equation (9): zdt1's f_1 is x_1 alone and its f_2
# moves with every variable; dtlz2's three centres all carry g, and the third
# omits x_2, which is index 1. the free set is the complement of each entry.
zdt1_dependence = {
    "lu": {0: [0, 29], 1: [0, 29], 2: all_but(30, []), 3: all_but(30, [])},
    "ls": {0: [0, 29], 1: [29], 2: all_but(30, []), 3: [28]},
    "cw": {0: [0], 1: [29], 2: all_but(30, []), 3: [28]},
}
dtlz2_dependence = {
    "lu": {0: all_but(12, []), 1: all_but(12, []), 2: all_but(12, []),
           3: all_but(12, []), 4: all_but(12, [1]), 5: all_but(12, [1])},
    "ls": {0: all_but(12, []), 1: [11], 2: all_but(12, []), 3: [10],
           4: all_but(12, [1]), 5: [9]},
    "cw": {0: all_but(12, []), 1: [11], 2: all_but(12, []), 3: [10],
           4: all_but(12, [1]), 5: [9]},
}
stated_dependence = {"zdt1_interval": zdt1_dependence,
                     "dtlz2_interval": dtlz2_dependence}


# the imprecision levels at which no half-width is identically zero
positive_levels = tuple(level for level in e2.epsilon_levels if level > 0.0)


@pytest.mark.parametrize("problem", (zdt1_interval, dtlz2_interval))
@pytest.mark.parametrize("phi_name", ("lu", "ls", "cw"))
def test_the_measured_free_sets_are_a5b_s_forms_read_by_hand(problem, phi_name):
    depends, constant = e2.column_dependence(
        problem, e2.problem_parameters(e2.convergence_eps), phi_name,
        e2.dependence_points, e2.dependence_seed)
    assert not np.any(constant)
    for column, stated in stated_dependence[problem.name][phi_name].items():
        measured = [index for index in range(problem.n_vars)
                    if depends[column, index]]
        assert measured == stated


@pytest.mark.parametrize("problem", (zdt1_interval, dtlz2_interval))
@pytest.mark.parametrize("phi_name", ("lu", "ls", "cw"))
@pytest.mark.parametrize("eps", positive_levels)
def test_no_two_image_columns_coincide_at_any_positive_level(problem, phi_name,
                                                             eps):
    # a5-b, and the property it was written to buy: the transformed problem has
    # 2m effective objectives under every phi, so the headline pair is not a
    # comparison between problems of different dimension. r-20.
    assert e2.effective_columns(problem, e2.problem_parameters(eps), phi_name,
                                e2.dependence_points,
                                e2.dependence_seed) == 2 * problem.n_obj


@pytest.mark.parametrize("problem", (zdt1_interval, dtlz2_interval))
def test_the_columns_do_coincide_at_the_crisp_level_and_the_count_says_so(problem):
    # eps = 0 is the crisp baseline and is labelled one, src/problems_tier1.py:
    # every half-width is zero, so examples 2.3 and 2.4 carry m copies of the zero
    # column and example 2.2 carries each centre twice. the counts differ between
    # the two, which is what makes the level a baseline and not a data point.
    counts = {name: e2.effective_columns(problem,
                                         e2.problem_parameters(crisp_level),
                                         name, e2.dependence_points,
                                         e2.dependence_seed)
              for name in e2.phi_names}
    assert counts["lu"] == problem.n_obj
    assert counts["ls"] == counts["cw"] == problem.n_obj + 1
    assert all(count < 2 * problem.n_obj for count in counts.values())


def test_jaccard_is_dice_over_two_minus_dice_and_agrees_with_a_direct_count():
    # d-09. the identity is checked against jaccard counted from two index sets
    # over one sample, which is what delta zero makes the two conventions on the
    # instrument the study's result is computed with.
    sample = filter_one_sample_under_every_phi(
        zdt1_interval, e2.problem_parameters(e2.convergence_eps), 300, 11)
    first = set(sample.indices["lu"].tolist())
    second = set(sample.indices["cw"].tolist())
    vectors = sample.decision_vectors
    dice = e2.compute_overlap(vectors[sample.indices["lu"]],
                              vectors[sample.indices["cw"]], e2.zero_delta)
    direct = len(first & second) / len(first | second)
    assert e2.jaccard_from_dice(dice) == pytest.approx(direct, abs=1e-12)
    assert e2.jaccard_from_dice(1.0) == pytest.approx(1.0)
    assert e2.jaccard_from_dice(0.0) == 0.0


def test_the_fronts_built_from_one_sample_are_run_random_search_s_own():
    # the shortcut the script takes, asserted bitwise. the sample is a pure
    # function of the box, the budget and the seed, so filtering it once under
    # every phi must give exactly what running random search under each phi gives.
    params = e2.problem_parameters(e2.convergence_eps)
    comparisons, results = e2.random_search_runs(zdt1_interval, params, 300, (11,),
                                                 0.1)
    for phi_name in e2.phi_names:
        direct = run_random_search(zdt1_interval, phi_name, params, 300, (11,))[0]
        built = results[phi_name][0]
        assert np.array_equal(built.front, direct.front)
        assert np.array_equal(built.decision_vectors, direct.decision_vectors)
        assert built.n_evals == direct.n_evals == 300
    assert comparisons[0].seed == 11


def test_delta_is_a_stated_fraction_of_the_box_diameter():
    assert e2.box_diameter(zdt1_interval) == pytest.approx(np.sqrt(30.0))
    assert e2.box_diameter(dtlz2_interval) == pytest.approx(np.sqrt(12.0))
    assert e2.problem_delta(zdt1_interval) == pytest.approx(
        e2.delta_box_fraction * e2.box_diameter(zdt1_interval))


def test_the_distance_to_a_projection_is_zero_inside_it_and_the_gap_outside():
    assert e2.interval_distance([0.5], [(0.0, 1.0)]) == 0.0
    assert e2.interval_distance([-0.25], [(0.0, 1.0)]) == pytest.approx(0.25)
    assert e2.interval_distance([1.5], [(0.0, 1.0)]) == pytest.approx(0.5)
    assert e2.interval_distance([], []) == 0.0


def test_the_two_overhang_structures_pin_what_the_two_arguments_pin():
    # x-01 registered {x_2 = ... = x_29 = 0} and {x_3 = ... = x_11 = 1/2}; a5-b's
    # drivers take one variable out of the first and two out of the second, and
    # both are per-variable projections of the unit box everywhere else.
    zdt1 = e2.efficient_projections("zdt1_interval", e2.registered_structure)
    assert zdt1[0] == (0.0, 1.0) and zdt1[29] == (0.0, 1.0)
    assert all(interval == (0.0, 0.0) for interval in zdt1[1:29])
    moved = e2.efficient_projections("zdt1_interval", e2.a5b_structure)
    assert moved[28] == (0.0, 1.0)
    assert all(interval == (0.0, 0.0) for interval in moved[1:28])
    dtlz2 = e2.efficient_projections("dtlz2_interval", e2.registered_structure)
    assert all(interval == (0.5, 0.5) for interval in dtlz2[2:11])
    later = e2.efficient_projections("dtlz2_interval", e2.a5b_structure)
    assert all(interval == (0.5, 0.5) for interval in later[2:9])
    assert later[9] == later[10] == later[11] == (0.0, 1.0)


def test_the_convergence_check_is_one_level_and_the_sweep_is_every_level():
    budgets = (5000, 20000)
    assert e2.budgets_for(e2.convergence_eps, budgets) == budgets
    for eps in e2.epsilon_levels:
        if eps != e2.convergence_eps:
            assert e2.budgets_for(eps, budgets) == (5000,)


def test_the_figure_panels_never_plot_a_first_coordinate_against_a_second():
    for n_cols in (4, 6):
        pairs = e2.figure_col_pairs(n_cols)
        assert pairs
        for first, second in pairs:
            assert first % 2 == second % 2
            assert 0 <= first < n_cols and 0 <= second < n_cols


def test_a_measured_table_survives_d3_and_reads_back_as_it_was_written(tmp_path):
    params = e2.problem_parameters(e2.convergence_eps)
    comparisons, _ = e2.random_search_runs(zdt1_interval, params, 300, (11, 12),
                                           0.1)
    rows = e2.decision_rows_by_seed(comparisons, "zdt1_interval",
                                    e2.convergence_eps, 300)
    path = e2.save_table(tmp_path, "2_measured_test",
                         e2.block_admissible(e2.decision_table_rows(rows)), [])
    written = read_metrics_table(path)[decision_block]
    assert written
    assert all(row["metric"] != "overlap_jaccard" for row in written)
    assert all(row["n_seeds"] == 2 and row["n_evals"] == 300 for row in written)
    finding = [row for row in written
               if (row["phi_a"], row["phi_b"]) == ("lu", "cw")]
    assert finding and all(row["status"] == "finding" for row in finding)


@pytest.mark.slow
@pytest.mark.parametrize("solver", ("nsga2", "mopso"))
def test_the_rank_callback_does_not_perturb_the_run(solver):
    # the instrument reads state and writes nothing back, so the front must come
    # back bit-identical to the one src/runners.py returns at the same seed.
    # docs/c3_validation.md section 5.1 made the same check of the same callback.
    params = e2.problem_parameters(e2.convergence_eps)
    settings = e2.run_settings((11, 12), (200,), 20, (11,))
    watched, recorders = e2.population_runs(zdt1_interval, "cw", params, solver,
                                            200, settings)
    plain = run_solver(zdt1_interval, "cw", params,
                       {"nsga2": e2.make_nsga2, "mopso": e2.make_mopso}[solver],
                       10, 20, (11, 12))
    assert len(recorders) == 2
    for first, second in zip(watched, plain):
        assert np.array_equal(first.front, second.front)
    for recorder in recorders:
        assert recorder.rows
        assert all(row["n_pop"] == 20 for row in recorder.rows)
        assert all(row["rank_1_of_candidates"] >= 1 for row in recorder.rows)


# the files a run writes that must be identical between two runs of one seed list
def stable_artefacts(root):
    # summary.csv is excluded because it carries the wall clock, and the record is
    # compared separately for the same reason. everything else is the run.
    return sorted(path for path in root.rglob("*.csv") if path.name != "summary.csv")


# the record with the one line that cannot be reproduced removed
def record_without_the_clock(path):
    return [line for line in path.read_text(encoding="utf-8").splitlines()
            if "wall_seconds" not in line]


# a small run of the whole script into a stated directory
def small_run(root):
    e2.main(["--output-root", str(root), "--record", str(root / "record.md"),
             "--seeds", "11,12,13", "--overhang-seeds", "11,12,13,14",
             "--budgets", "200,400", "--pop-size", "20"])
    return root


@pytest.mark.slow
def test_a_run_writes_every_artefact_and_repeats_itself_byte_for_byte(tmp_path):
    # "re-runnable to the same numbers from the same seeds", asserted rather than
    # claimed. the budget is small because what is under test is the pipeline and
    # not the numbers; every seeded stream in it is the one the real run uses.
    first = small_run(tmp_path / "first")
    second = small_run(tmp_path / "second")
    for name in e2.raw_fieldnames:
        assert (first / name).is_file(), name
    for eps in e2.epsilon_levels:
        for prefix in ("2_measured", "3_solvers"):
            name = "table_{}.csv".format(e2.level_table_name(prefix, eps))
            assert (first / name).is_file(), name
    assert (first / "raw" / "manifest.csv").is_file()
    assert len(list((first / "raw").glob("*.npz"))) == 108
    assert len(list((first / "figures").glob("*.png"))) == 72
    assert record_without_the_clock(first / "record.md") == record_without_the_clock(
        second / "record.md")
    for path in stable_artefacts(first):
        other = second / path.relative_to(first)
        assert path.read_bytes() == other.read_bytes(), path.name


@pytest.mark.slow
def test_the_raw_arrays_read_back_as_the_runs_that_were_written(tmp_path):
    # the raw results are re-readable without re-running, which is what makes a
    # later session able to recompute a metric without a solver.
    root = small_run(tmp_path / "run")
    key = ("dtlz2_interval", "nsga2", "cw", e2.convergence_eps, 400)
    results = e2.load_raw_runs(e2.raw_path(root, key))
    assert [result.seed for result in results] == [11, 12, 13]
    assert all(result.n_evals == 400 for result in results)
    assert all(result.front.shape[1] == 2 * 3 for result in results)
    assert all(result.front.shape[0] == result.decision_vectors.shape[0]
               for result in results)


@pytest.mark.slow
def test_the_record_rebuilds_from_the_artefacts_alone(tmp_path):
    # the record is the run's numbers read back out of the run's files, so it must
    # be reproducible from those files with nothing of the run in memory. this is
    # also what lets the record's prose be corrected without spending the grid
    # again.
    root = small_run(tmp_path / "run")
    first = (root / "record.md").read_text(encoding="utf-8")
    e2.main(["--output-root", str(root), "--record", str(root / "again.md"),
             "--budgets", "200,400", "--record-only"])
    assert (root / "again.md").read_text(encoding="utf-8") == first
