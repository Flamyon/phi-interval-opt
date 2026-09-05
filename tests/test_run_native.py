# tests for f3, experiments/run_native.py.
#
# what is worth testing in an experiment script, and what is not. the numbers the
# run returns are the result and cannot be asserted in advance; what can be
# asserted is that the instrument computing them is the one it says it is. so
# these tests check four things and nothing else:
#
#   the closed forms. table 1 is the calibration's known answer and it is
#   integrated here from the bands of nu through an antiderivative. this file
#   checks it against the values docs/part2/f2_ibk1_derivation.md section 3.1
#   published, and against a grid count taken from f2 section 2.4's region
#   inequalities directly through src/problems_native.py. two routes to one
#   number, and the derivation is not checked against itself.
#
#   the free sets. the run decides whether m-2 is computed at all by measuring
#   which decision variables each image column moves with, and f2 section 1.2
#   states from the forms that every one of the twelve moves with both. the
#   measurement must agree with the derivation, or the registered condition of
#   PROGRESS.md x-01 is being read on the wrong columns.
#
#   the dominance test. section 6 of the record is a measurement made in [16]'s
#   own relation against [16]'s own printed row, and f2 section 4.2 supplies a
#   worked witness with a stated margin. the test asserts the script's relation
#   reproduces that margin and rejects the printed point itself.
#
#   the shortcut. the script builds random search's fronts out of the one
#   filtered sample rather than calling run_random_search a second time, so that
#   one seed costs one filter pass. that is only sound if the two agree exactly,
#   and this file asserts they do, front and decision vectors, bitwise.
#
# and one end-to-end run at a small budget, marked slow, which asserts that every
# artefact is written and that a second run from the same seeds reproduces every
# one of them byte for byte, which is the whole of "re-runnable to the same
# numbers from the same seeds".

import numpy as np
import pytest

import run_native as f3
from problems_native import ibk1, ibk1_shift, in_region
from random_search import run_random_search
from reporting import decision_block, read_metrics_table

# the areas docs/part2/f2_ibk1_derivation.md section 3.1 publishes for the three
# derived regions, at the precision it prints them. f2 gives them as closed forms
# in logarithms and this script integrates the band, so the two are two routes.
published_areas = {"lu": 3.790332, "ls": 5.685282, "cw": 2.875612}

# the overlap fractions the same section publishes, which are the shared measure
# over the union, that is jaccard, one per pair in phi_pairs order.
published_union_shares = {("lu", "ls"): 0.666692, ("lu", "cw"): 0.758670,
                          ("ls", "cw"): 0.505799}

# f2 section 4.2's dominator of [16]'s Table 1 point and the tightest of its four
# margins as that section prints it. the point was found there by exhaustive
# search and is used here as the fixture the script's own relation is read
# against.
f2_dominator = (2.897500, 2.397500)
f2_tightest_margin = 0.273966

# the number of image columns of I-BK1, three phi times 2m, and how many of them
# f2 section 1.2 says have a non-empty free set. the second number is zero and
# the test asserts it rather than the run reporting it.
n_image_columns = 3 * 2 * ibk1.n_obj
free_columns_expected = 0

# the grid the region inequalities are counted on. the boundaries are hyperbolas,
# so a midpoint count converges from a curved boundary and its own accuracy is
# the scale the comparison is made at; it is stated here and is not a tolerance
# on the derivation.
grid_resolution = 1000
grid_accuracy = 2e-3


# the area of one derived region, counted on a grid of the quadrant
def grid_area(phi_name, resolution=grid_resolution):
    step = ibk1_shift / resolution
    side = np.linspace(0.0, ibk1_shift, resolution, endpoint=False) + step / 2.0
    grid_1, grid_2 = np.meshgrid(side, side, indexing="ij")
    grid = np.column_stack([grid_1.ravel(), grid_2.ravel()])
    return float(np.count_nonzero(in_region(phi_name, grid)) * step * step)


# the derived areas are the ones f2 section 3.1 published
def test_the_derived_areas_are_the_ones_f2_published():
    areas = f3.derived_areas()
    for name, published in published_areas.items():
        assert round(areas[name], 6) == published


# the antiderivative route agrees with a count of f2's own inequalities
def test_the_areas_agree_with_a_grid_count_of_the_region_inequalities():
    # the inequalities live in src/problems_native.py and the antiderivative in
    # the script, so a disagreement is a disagreement between two readings of f2
    # section 2.4 and not a file agreeing with itself.
    areas = f3.derived_areas()
    for name in f3.phi_names:
        assert grid_area(name) == pytest.approx(areas[name], abs=grid_accuracy)


# the intersections come out of the bands and carry f2's nesting
def test_the_intersections_are_the_contained_regions():
    # the script intersects the two bands and measures the result, so the nesting
    # f2 section 3.1 states is derived here and not assumed. where one band
    # contains the other the intersection must be the contained region's own
    # measure, to the last bit and not approximately.
    areas = f3.derived_areas()
    intersections = f3.derived_intersections()
    for (phi_a, phi_b), shared in intersections.items():
        assert shared == min(areas[phi_a], areas[phi_b])


# the exact pair statistics reproduce the overlap fractions f2 published
def test_the_exact_pair_statistics_reproduce_f2_section_3_1():
    areas = f3.derived_areas()
    intersections = f3.derived_intersections()
    for pair, published in published_union_shares.items():
        statistics = f3.exact_pair_statistics(areas[pair[0]], areas[pair[1]],
                                              intersections[pair])
        assert round(statistics["overlap_union_share"], 6) == published
        # every pair nests, so one direction of every coverage is exactly one
        assert 1.0 in (statistics["coverage_a_in_b"], statistics["coverage_b_in_a"])


# the two overlap conventions are two different quantities, d-09
def test_the_two_overlap_conventions_are_different_quantities():
    areas = f3.derived_areas()
    statistics = f3.exact_pair_statistics(areas["lu"], areas["cw"],
                                          f3.derived_intersections()[("lu", "cw")])
    assert statistics["overlap_d2_convention"] > statistics["overlap_union_share"]
    assert f3.jaccard_from_dice(statistics["overlap_d2_convention"]) == \
        pytest.approx(statistics["overlap_union_share"])


# jaccard from dice is the identity e2 states and not a second definition
def test_jaccard_from_dice_is_the_identity():
    # with a and b contained one in the other, dice is 2|A| / (|A| + |B|) and
    # jaccard is |A| / |B|, and the identity must carry that case exactly.
    assert f3.jaccard_from_dice(1.0) == pytest.approx(1.0)
    assert f3.jaccard_from_dice(0.0) == 0.0
    assert f3.jaccard_from_dice(2.0 * 1.0 / (1.0 + 3.0)) == pytest.approx(1.0 / 3.0)


# no image column of I-BK1 is a function of a strict subset of the variables
@pytest.mark.parametrize("phi_name", ("lu", "ls", "cw"))
def test_no_image_column_has_a_free_set(phi_name):
    # f2 section 1.2: every one of the twelve image coordinates is a diagonal
    # quadratic in both variables with strictly positive coefficients, because
    # [16] put a non-degenerate interval on both terms of both objectives. the
    # measurement must agree, or x-01's condition is being read on the wrong
    # columns. and no column is constant, so nothing is excluded for want of a
    # strict minimiser either.
    depends, constant = f3.column_dependence(phi_name, f3.dependence_points,
                                             f3.dependence_seed)
    assert not np.any(constant)
    assert bool(np.all(depends))


# the run's own free-set table says the condition applies nowhere
def test_the_free_set_table_records_the_condition_as_absent():
    rows = f3.free_set_rows()
    assert len(rows) == n_image_columns
    assert len(f3.columns_with_a_free_set(rows)) == free_columns_expected
    assert all(row["free_set"] == "" for row in rows)
    assert all(row["depends_on"] == "0 1" for row in rows)


# the dominance test is [16]'s own relation against [16]'s own printed row
def test_the_dominance_test_reproduces_f2_s_witness():
    # f2 section 4.2's dominator must count and its tightest margin must be the
    # one printed there; the printed point itself must not count, no point being
    # strictly better than itself in any coordinate.
    points = np.array([f2_dominator, f3.printed_x_star])
    mask = f3.dominator_mask(points)
    assert mask.tolist() == [True, False]
    margin, best = f3.widest_dominator(points, mask)
    assert round(margin, 6) == f2_tightest_margin
    assert best.tolist() == list(f2_dominator)


# a set holding no dominator returns no margin rather than a zero
def test_a_set_with_no_dominator_carries_no_margin():
    points = np.array([f3.printed_x_star])
    margin, best = f3.widest_dominator(points, f3.dominator_mask(points))
    assert margin is None
    assert best is None


# the fronts built from one sample are what run_random_search returns
def test_the_fronts_built_from_one_sample_are_run_random_search_s_own():
    # the shortcut the script takes, asserted bitwise. the sample is a pure
    # function of the box, the budget and the seed, so filtering it once under
    # every phi must give exactly what running random search under each phi gives.
    _, results = f3.random_search_runs(400, (11,), f3.problem_delta())
    for phi_name in f3.phi_names:
        direct = run_random_search(ibk1, phi_name, None, 400, (11,))[0]
        built = results[phi_name][0]
        assert np.array_equal(built.front, direct.front)
        assert np.array_equal(built.decision_vectors, direct.decision_vectors)
        assert built.n_evals == direct.n_evals == 400


# delta is a stated fraction of the box diameter and never an absolute number
def test_delta_is_a_stated_fraction_of_the_box_diameter():
    assert f3.box_diameter() == pytest.approx(20.0 * np.sqrt(2.0))
    assert f3.problem_delta() == pytest.approx(f3.delta_box_fraction
                                               * f3.box_diameter())


# table 1 survives d3 and reads back as it was written
def test_the_exact_table_survives_d3_and_reads_back_as_it_was_written(tmp_path):
    path = f3.save_table(tmp_path, "1_exact_ibk1", f3.exact_table_rows(), [])
    rows = read_metrics_table(path)[decision_block]
    assert len(rows) == 9
    finding = [row for row in rows
               if (row["phi_a"], row["phi_b"], row["metric"])
               == ("lu", "cw", "coverage_a_in_b")]
    assert round(finding[0]["median"], 6) == published_union_shares[("lu", "cw")]
    assert finding[0]["status"] == "finding"
    assert all(row["n_seeds"] == 0 and row["n_evals"] == 0 for row in rows)
    # the note on the finding row says the pair nests on this problem too, so a
    # reader of the artefact alone cannot take it for a measured difference. the
    # two check rows carry the containment note and not this one, the criterion
    # predicting those two before anything runs.
    assert "nests as well" in finding[0]["note"]
    checks = [row for row in rows if row["status"] == "check"]
    assert checks and all("nests as well" not in row["note"] for row in checks)


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
    f3.main(["--output-root", str(root), "--record", str(root / "record.md"),
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
    expected = ("table_1_exact_ibk1.csv", "table_2_measured.csv",
                "table_3_solvers.csv", "exact_regions_ibk1.csv", "free_sets.csv",
                "decision_metrics_by_seed.csv", "objective_metrics_by_seed.csv",
                "overlap_conventions.csv", "delta_sweep.csv",
                "dominators_by_seed.csv", "dominators_summary.csv",
                "instrument_error_ibk1.csv", "raw_manifest.csv", "summary.csv")
    for name in expected:
        assert (first / name).is_file()
    assert len(list((first / "raw").glob("*.npz"))) == 18
    assert len(list((first / "figures").glob("*.png"))) == 24
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
    results = f3.load_raw_runs(f3.raw_path(root, ("nsga2", "cw", 400)))
    assert [result.seed for result in results] == [11, 12, 13]
    assert all(result.n_evals == 400 for result in results)
    assert all(result.front.shape[1] == 2 * ibk1.n_obj for result in results)
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
    f3.main(["--output-root", str(root), "--record", str(root / "again.md"),
             "--budgets", "200,400", "--record-only"])
    assert (root / "again.md").read_text(encoding="utf-8") == first
