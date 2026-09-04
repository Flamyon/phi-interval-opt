# tests for e1, experiments/run_tier0.py.
#
# what is worth testing in an experiment script, and what is not. the numbers the
# run returns are the result and cannot be asserted in advance; what can be
# asserted is that the instrument computing them is the one it says it is. so
# these tests check three things and nothing else:
#
#   the closed forms. the exact table is the calibration's known answer, and this
#   file checks the areas this script integrates against the values
#   docs/meeting_2026_09_04.md section 4.3 published from an independent adaptive
#   quadrature and an 8000 by 8000 grid count, and against a grid count taken here
#   from the region inequalities directly rather than from the antiderivatives.
#   two routes to one number, and the derivation is not checked against itself.
#
#   the free sets. the run decides which columns m-1 and m-2 are computed on by
#   measuring which decision variables each image column moves with, and
#   docs/plan_after_meeting.md section f2 states what those sets are for p1 by
#   hand. the measurement must agree with the derivation, or the registered
#   prediction is being read on the wrong columns.
#
#   the shortcut. the script builds random search's fronts out of the one filtered
#   sample rather than calling run_random_search a second time, so that one seed
#   costs one filter pass. that is only sound if the two agree exactly, and this
#   file asserts they do, front and decision vectors, bitwise.
#
# and one end-to-end run at a small budget, marked slow, which asserts that every
# artefact is written and that a second run from the same seeds reproduces every
# one of them byte for byte, which is the whole of "re-runnable to the same
# numbers from the same seeds".

import numpy as np
import pytest

import run_tier0 as e1
from problems_tier0 import p0, p1
from random_search import run_random_search
from reporting import decision_block, read_metrics_table

# the values docs/meeting_2026_09_04.md section 4.3 publishes for the areas of
# b1 section 2.4's three regions, at the precision it prints them.
published_areas = {"lu": 0.310533, "ls": 1.513401, "cw": 1.0}

# the pair statistics the same section publishes, as (share of the first in the
# second, share of the second in the first, shared fraction of the union).
published_pairs = {("lu", "ls"): (1.0, 0.205189, 0.205189),
                   ("lu", "cw"): (0.394710, 0.122571, 0.103177),
                   ("ls", "cw"): (0.660763, 1.0, 0.660763)}

# the free sets docs/plan_after_meeting.md sections f2 and f3 state for p1 by
# hand, as column index to the decision variables the column does not depend on.
# under example 2.2 every column moves with both variables; under examples 2.3 and
# 2.4 the two width columns move with one each.
stated_free_sets = {"lu": {0: [], 1: [], 2: [], 3: []},
                    "ls": {0: [], 1: [0], 2: [], 3: [1]},
                    "cw": {0: [], 1: [0], 2: [], 3: [1]}}


# whether a point satisfies b1 section 2.4's inequalities for one region
def in_region(phi_name, x_1, x_2):
    upper = 7.0 * x_1 * x_2 - 4.0 * x_1 + 12.0 * x_2 - 16.0 <= 0.0
    if phi_name == "cw":
        return (0.0 <= x_1) & (x_1 <= 1.0) & (0.0 <= x_2) & (x_2 <= 1.0)
    if phi_name == "ls":
        return ((0.0 <= x_1) & (x_1 <= 4.0 / 3.0) & (0.0 <= x_2)
                & (x_2 <= 4.0 / 3.0) & upper)
    lower = 4.0 * x_1 - x_1 * x_2 - 20.0 * x_2 + 16.0 <= 0.0
    return (x_1 >= 0.0) & lower & upper


# the area of one region counted on a grid of the decision box
def grid_area(phi_name, resolution=2000):
    lower, upper = p1.bounds()
    step = (upper - lower) / resolution
    x_1 = lower[0] + step[0] * (np.arange(resolution) + 0.5)
    x_2 = lower[1] + step[1] * (np.arange(resolution) + 0.5)
    grid_1, grid_2 = np.meshgrid(x_1, x_2, indexing="ij")
    return float(np.count_nonzero(in_region(phi_name, grid_1, grid_2))
                 * step[0] * step[1])


def test_the_derived_areas_are_the_ones_the_meeting_document_published():
    areas = e1.derived_areas()
    for name, published in published_areas.items():
        assert round(areas[name], 6) == published


def test_the_intersection_of_x_lu_and_x_cw_is_the_published_closed_form():
    # b1 section 2.4 and docs/meeting_2026_09_04.md section 4.3: 64 ln(21/20) - 3.
    # the script integrates the arc rather than evaluating this expression, so the
    # two are two routes to one number.
    assert e1.lu_cw_intersection_area() == pytest.approx(
        64.0 * np.log(21.0 / 20.0) - 3.0, abs=1e-12)


def test_the_areas_agree_with_a_grid_count_of_the_region_inequalities():
    # the inequalities are transcribed here and the antiderivatives are in the
    # script, so a disagreement is a disagreement between two readings of b1
    # section 2.4 and not a file agreeing with itself.
    areas = e1.derived_areas()
    for name in ("lu", "ls", "cw"):
        assert grid_area(name) == pytest.approx(areas[name], abs=2e-3)


def test_the_exact_pair_statistics_reproduce_the_published_table():
    areas = e1.derived_areas()
    intersections = e1.derived_intersections(areas)
    for pair, published in published_pairs.items():
        statistics = e1.exact_pair_statistics(areas[pair[0]], areas[pair[1]],
                                              intersections[pair])
        assert round(statistics["coverage_a_in_b"], 6) == published[0]
        assert round(statistics["coverage_b_in_a"], 6) == published[1]
        assert round(statistics["overlap_union_share"], 6) == published[2]


def test_the_two_overlap_conventions_are_different_quantities():
    # the reason table 1 carries d2's convention and exact_regions_p1.csv carries
    # both: compute_overlap is the two covered counts over the two cardinalities
    # and not the shared measure over the union, and on the headline pair the two
    # differ in the first decimal.
    areas = e1.derived_areas()
    statistics = e1.exact_pair_statistics(areas["lu"], areas["cw"],
                                          e1.lu_cw_intersection_area())
    assert statistics["overlap_d2_convention"] > statistics["overlap_union_share"]
    assert round(statistics["overlap_union_share"], 6) == 0.103177
    assert round(statistics["overlap_d2_convention"], 6) == 0.187054


@pytest.mark.parametrize("phi_name", ("lu", "ls", "cw"))
def test_the_measured_free_sets_are_the_ones_the_plan_derived_for_p1(phi_name):
    depends, constant = e1.column_dependence(p1, e1.problem_parameters(p1),
                                             phi_name, e1.dependence_points,
                                             e1.dependence_seed)
    assert not np.any(constant)
    for column, free in stated_free_sets[phi_name].items():
        measured = [index for index in range(p1.n_vars) if not depends[column, index]]
        assert measured == free


@pytest.mark.parametrize("phi_name", ("lu", "ls", "cw"))
def test_p0_carries_one_constant_image_column_under_every_phi(phi_name):
    # p0's first objective is [-|x|, |x|], so its centre is identically zero, and
    # its second is [0, x^2], so that objective's lower endpoint is. one column of
    # the image is therefore constant under every phi, which is why no
    # hypervolume is scored on p0 and why the protected-minimiser mechanism has no
    # strict minimiser to work with there.
    _, constant = e1.column_dependence(p0, None, phi_name, e1.dependence_points,
                                       e1.dependence_seed)
    assert int(np.count_nonzero(constant)) == 1


def test_the_fronts_built_from_one_sample_are_run_random_search_s_own():
    # the shortcut the script takes, asserted bitwise. the sample is a pure
    # function of the box, the budget and the seed, so filtering it once under
    # every phi must give exactly what running random search under each phi gives.
    params = e1.problem_parameters(p1)
    comparisons, results = e1.random_search_runs(p1, params, 400, (11,), 0.1)
    for phi_name in e1.phi_names:
        direct = run_random_search(p1, phi_name, params, 400, (11,))[0]
        built = results[phi_name][0]
        assert np.array_equal(built.front, direct.front)
        assert np.array_equal(built.decision_vectors, direct.decision_vectors)
        assert built.n_evals == direct.n_evals == 400


def test_delta_is_a_stated_fraction_of_the_box_diameter():
    assert e1.box_diameter(p0) == pytest.approx(2.0)
    assert e1.box_diameter(p1) == pytest.approx(2.0 * np.sqrt(2.0))
    assert e1.problem_delta(p1) == pytest.approx(e1.delta_box_fraction
                                                 * e1.box_diameter(p1))


def test_the_distance_to_a_projection_is_zero_inside_it_and_the_gap_outside():
    assert e1.interval_distance([0.5], [(0.0, 1.0)]) == 0.0
    assert e1.interval_distance([-0.25], [(0.0, 1.0)]) == pytest.approx(0.25)
    assert e1.interval_distance([1.5], [(0.0, 1.0)]) == pytest.approx(0.5)
    assert e1.interval_distance([], []) == 0.0


def test_the_exact_table_survives_d3_and_reads_back_as_it_was_written(tmp_path):
    path = e1.save_table(tmp_path, "1_exact_p1", e1.exact_table_rows(p1), [])
    rows = read_metrics_table(path)[decision_block]
    assert len(rows) == 9
    finding = [row for row in rows
               if (row["phi_a"], row["phi_b"], row["metric"])
               == ("lu", "cw", "coverage_a_in_b")]
    assert round(finding[0]["median"], 6) == 0.394710
    assert finding[0]["status"] == "finding"
    assert all(row["n_seeds"] == 0 and row["n_evals"] == 0 for row in rows)


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
    e1.main(["--output-root", str(root), "--record", str(root / "record.md"),
             "--seeds", "11,12,13", "--budgets", "200,400", "--pop-size", "20",
             "--reference-points", "60"])
    return root


@pytest.mark.slow
def test_a_run_writes_every_artefact_and_repeats_itself_byte_for_byte(tmp_path):
    # "re-runnable to the same numbers from the same seeds", asserted rather than
    # claimed. the budget is small because what is under test is the pipeline and
    # not the numbers; every seeded stream in it is the one the real run uses.
    first = small_run(tmp_path / "first")
    second = small_run(tmp_path / "second")
    expected = ("table_1_exact_p1.csv", "table_2_measured.csv",
                "table_3_solvers.csv", "exact_regions_p1.csv", "free_sets.csv",
                "decision_metrics_by_seed.csv", "objective_metrics_by_seed.csv",
                "registered_measurements.csv",
                "registered_measurements_summary.csv", "delta_sweep.csv",
                "instrument_error_p1.csv", "summary.csv")
    for name in expected:
        assert (first / name).is_file()
    assert (first / "raw" / "manifest.csv").is_file()
    assert len(list((first / "raw").glob("*.npz"))) == 36
    assert len(list((first / "figures").glob("*.png"))) == 18
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
    key = ("p1", "nsga2", "cw", 400)
    results = e1.load_raw_runs(e1.raw_path(root, key))
    assert [result.seed for result in results] == [11, 12, 13]
    assert all(result.n_evals == 400 for result in results)
    assert all(result.front.shape[1] == 2 * 2 for result in results)
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
    e1.main(["--output-root", str(root), "--record", str(root / "again.md"),
             "--budgets", "200,400", "--record-only"])
    assert (root / "again.md").read_text(encoding="utf-8") == first
