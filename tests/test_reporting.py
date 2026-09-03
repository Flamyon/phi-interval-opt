# tests for src/reporting.py, subpart d3.
# the module writes artefacts, so most of what is checked here is what it refuses
# to write. the first group is the required fields, one test per field per block,
# because a table missing any one of them is a table that cannot be interpreted in
# october and the whole point of the module is that the refusal happens now; the
# second is the round trip, which is what makes a written table evidence rather
# than a picture of one, together with the byte reproducibility that lets two runs
# be compared by their files; the third is the summary across seeds against a hand
# computed answer at an odd and an even seed count; and the fourth is the figures,
# checked for being written and non-empty and never for their pixels, plus the one
# piece of arithmetic the figures carry, b1 section 2.4's region boundary, checked
# against b1's own inequalities from the other side exactly as
# tests/test_reference_fronts.py checks b2's sampled points.

import numpy as np
import pytest
from matplotlib.figure import Figure

from metrics_decision import check_status, finding_status
from metrics_objective import nadir_margin_rule, nadir_rule
from reference_fronts import dirichlet_mode, farthest_point_mode
from reporting import (PlottedFront, PlottedSet, block_fields, blocks,
                       decision_block, decision_fields, draw_regions,
                       objective_block, objective_fields, plot_decision_sets,
                       plot_fronts, read_metrics_table, region_boundary,
                       save_metrics_table, summarize_across_seeds)

# b1 section 2.4's extreme values, as exact doubles, as test_reference_fronts.py
# writes them
four_thirds = 4.0 / 3.0
# the residual tolerance the region-boundary check reads membership at. it is
# tests/test_reference_fronts.py's own number and it is a floating-point residual
# of an exact identity, not a tolerance on an order: no comparison in this file
# ranks two rows.
residual_bound = 1e-12


# a complete objective-space row, with any field overridden by the caller
def objective_row(**overrides):
    row = {"problem": "p1", "phi": "lu", "solver": "nsga2", "metric": "hypervolume",
           "cardinality": 100, "n_evals": 5000, "reference_size": 1000,
           "sampling_mode": farthest_point_mode, "include_singular_segments": False,
           "hv_reference_rule": nadir_margin_rule,
           "hv_reference_point": (2.0, 2.5, 3.0, 1.25)}
    row.update(summarize_across_seeds([1.0, 2.0, 3.0, 4.0]))
    row.update(overrides)
    return row


# a complete decision-space row, with any field overridden by the caller
def decision_row(**overrides):
    row = {"problem": "p1", "phi_a": "lu", "phi_b": "cw", "status": finding_status,
           "metric": "overlap", "n_evals": 5000, "cardinality_a": 586,
           "cardinality_b": 612, "delta": 0.1, "box_scale": 2.0,
           "containment_violations": None,
           "note": "nested in neither direction, so both directions are measured"}
    row.update(summarize_across_seeds([0.25, 0.5, 0.75]))
    row.update(overrides)
    return row


# the two-block mapping save_metrics_table takes, from rows of each block
def table(objective_rows=(), decision_rows=()):
    return {objective_block: list(objective_rows),
            decision_block: list(decision_rows)}


# a table with one row in each block, which is the shape most tests write
def one_row_table():
    return table([objective_row()], [decision_row()])


# an objective-space row missing one required field is refused, naming that field
@pytest.mark.parametrize("field", objective_fields)
def test_a_missing_objective_field_is_refused_naming_it(field, tmp_path):
    row = objective_row()
    del row[field]
    path = tmp_path / "metrics.csv"
    with pytest.raises(ValueError, match=repr(field)):
        save_metrics_table(table([row]), path)
    # the whole table is checked before the file is opened, so a refusal leaves
    # nothing on disk that a reader could take for a table
    assert not path.exists()


# a decision-space row missing one required field is refused, naming that field
@pytest.mark.parametrize("field", decision_fields)
def test_a_missing_decision_field_is_refused_naming_it(field, tmp_path):
    row = decision_row()
    del row[field]
    path = tmp_path / "metrics.csv"
    with pytest.raises(ValueError, match=repr(field)):
        save_metrics_table(table([], [row]), path)
    assert not path.exists()


# a required field present but empty is refused too, an empty cell being a number
# with nothing saying what it is
@pytest.mark.parametrize("field", ("n_seeds", "n_evals", "cardinality", "median"))
def test_a_required_field_stated_as_none_is_refused(field, tmp_path):
    with pytest.raises(ValueError, match=repr(field)):
        save_metrics_table(table([objective_row(**{field: None})]),
                           tmp_path / "metrics.csv")


# a required field left blank is refused for the same reason, an empty cell being
# indistinguishable from a missing one once the file is read
def test_a_required_field_left_blank_is_refused(tmp_path):
    with pytest.raises(ValueError, match="'note'"):
        save_metrics_table(table([], [decision_row(note="  ")]),
                           tmp_path / "metrics.csv")


# containment_violations is the one field that may be absent, and its absence says
# there is no containment on the pair rather than that the count came out zero
def test_containment_violations_may_be_none_and_reads_back_as_none(tmp_path):
    path = tmp_path / "metrics.csv"
    save_metrics_table(table([], [decision_row(containment_violations=None),
                                  decision_row(phi_b="ls", status=check_status,
                                               containment_violations=1)]), path)
    read_back = read_metrics_table(path)[decision_block]
    assert read_back[0]["containment_violations"] is None
    assert read_back[1]["containment_violations"] == 1


# a field the block has no column for is refused, since it would not reach the file
def test_a_field_outside_the_block_is_refused(tmp_path):
    with pytest.raises(ValueError, match="hv_reference_point"):
        save_metrics_table(table([], [decision_row(hv_reference_point=(1.0, 1.0))]),
                           tmp_path / "metrics.csv")


# a block missing from the results is refused, an empty block being a statement
def test_a_missing_block_is_refused(tmp_path):
    with pytest.raises(ValueError, match=decision_block):
        save_metrics_table({objective_block: [objective_row()]},
                           tmp_path / "metrics.csv")


# a decision-space metric cannot be written under the objective block's restriction
def test_a_decision_metric_in_the_objective_block_is_refused(tmp_path):
    with pytest.raises(ValueError, match="metric"):
        save_metrics_table(table([objective_row(metric="overlap")]),
                           tmp_path / "metrics.csv")


# an objective-space metric cannot be written into the block read as comparable
def test_an_objective_metric_in_the_decision_block_is_refused(tmp_path):
    with pytest.raises(ValueError, match="metric"):
        save_metrics_table(table([], [decision_row(metric="hypervolume")]),
                           tmp_path / "metrics.csv")


# the reporting parameters are the ones the producing modules state and no others
@pytest.mark.parametrize("field, value", (("sampling_mode", "uniform"),
                                          ("hv_reference_rule", "front_nadir"),
                                          ("include_singular_segments", "yes")))
def test_an_unstated_reporting_parameter_is_refused(field, value, tmp_path):
    with pytest.raises(ValueError, match=field):
        save_metrics_table(table([objective_row(**{field: value})]),
                           tmp_path / "metrics.csv")


# the value read back is the value written. the hypervolume reference point is
# written as its 2m doubles and read back as a tuple of them, so it is compared by
# value and not by the container it was handed in
def same_value(read_value, written_value):
    if isinstance(written_value, (tuple, list, np.ndarray)):
        return tuple(np.ravel(read_value)) == tuple(np.ravel(written_value))
    return read_value == written_value


# a written table reads back with every required column present and the values written
def test_a_written_table_round_trips(tmp_path):
    path = tmp_path / "metrics.csv"
    written = table([objective_row(),
                     objective_row(phi="cw", metric="igd",
                                   sampling_mode=dirichlet_mode,
                                   include_singular_segments=True,
                                   hv_reference_rule=nadir_rule)],
                    [decision_row(),
                     decision_row(phi_b="ls", status=check_status,
                                  metric="coverage_a_in_b",
                                  containment_violations=1,
                                  note="check on r-06")])
    save_metrics_table(written, path)
    read_back = read_metrics_table(path)
    for block_name in blocks:
        assert len(read_back[block_name]) == len(written[block_name])
        for read_row, written_row in zip(read_back[block_name], written[block_name]):
            assert sorted(read_row) == sorted(block_fields[block_name])
            for field in block_fields[block_name]:
                assert same_value(read_row[field], written_row[field])


# the same results written twice give the same bytes, so two runs compare by file
def test_the_same_results_give_the_same_bytes(tmp_path):
    first, second = tmp_path / "one.csv", tmp_path / "two.csv"
    save_metrics_table(one_row_table(), first)
    save_metrics_table(one_row_table(), second)
    assert first.read_bytes() == second.read_bytes()
    assert len(first.read_bytes()) > 0


# the restriction is in the file and not only in a caption, once per block
def test_the_file_carries_each_block_restriction(tmp_path):
    path = tmp_path / "metrics.csv"
    save_metrics_table(one_row_table(), path)
    text = path.read_text()
    assert "never rank one phi against another" in text
    assert "comparable across phi" in text
    assert "block,{}".format(objective_block) in text
    assert "block,{}".format(decision_block) in text


# the median and the interquartile range of an even number of seeds, by hand.
# four values 1, 2, 3, 4 give a median of 2.5 and, on numpy's linear quartiles,
# q1 = 1.75 and q3 = 3.25, so the range is 1.5
def test_median_and_interquartile_range_on_an_even_seed_count():
    summary = summarize_across_seeds([4.0, 1.0, 3.0, 2.0])
    assert summary == {"n_seeds": 4, "median": 2.5, "q1": 1.75, "q3": 3.25,
                       "iqr": 1.5}


# and of an odd number: five values 1 to 5 give 3, with q1 = 2 and q3 = 4
def test_median_and_interquartile_range_on_an_odd_seed_count():
    summary = summarize_across_seeds([5.0, 4.0, 3.0, 2.0, 1.0])
    assert summary == {"n_seeds": 5, "median": 3.0, "q1": 2.0, "q3": 4.0,
                       "iqr": 2.0}


# the summary is what the row carries, so the seed count cannot be lost from it
def test_the_summary_is_what_the_table_carries(tmp_path):
    path = tmp_path / "metrics.csv"
    row = objective_row(**summarize_across_seeds([4.0, 1.0, 3.0, 2.0]))
    save_metrics_table(table([row]), path)
    read_back = read_metrics_table(path)[objective_block][0]
    assert (read_back["n_seeds"], read_back["median"], read_back["iqr"]) == (4, 2.5,
                                                                            1.5)


# a summary of no values is refused rather than returned as a median of nothing
def test_a_summary_of_no_seeds_is_refused():
    with pytest.raises(ValueError, match="at least one entry"):
        summarize_across_seeds([])


# a check row and a finding row go into one block only with the status column on both
def test_a_check_and_a_finding_row_need_the_status_column(tmp_path):
    path = tmp_path / "metrics.csv"
    check_row = decision_row(phi_b="ls", status=check_status,
                             containment_violations=1, note="check on r-06")
    finding_row = decision_row(status=finding_status)
    without_status = dict(check_row)
    del without_status["status"]
    with pytest.raises(ValueError, match="'status'"):
        save_metrics_table(table([], [without_status, finding_row]), path)
    assert not path.exists()
    save_metrics_table(table([], [check_row, finding_row]), path)
    statuses = [row["status"] for row in read_metrics_table(path)[decision_block]]
    assert statuses == [check_status, finding_status]


# a status outside d2's two labels is refused, the labels not being re-declared here
def test_a_status_outside_d2s_labels_is_refused(tmp_path):
    with pytest.raises(ValueError, match="status"):
        save_metrics_table(table([], [decision_row(status="ok")]),
                           tmp_path / "metrics.csv")


# two fronts and two column pairs, at sizes small enough to keep the file fast
def plotted_fronts():
    generator = np.random.default_rng(3)
    return [PlottedFront("nsga-ii", 5, 5000, generator.random((30, 4))),
            PlottedFront("random search", 5, 5000, generator.random((70, 4)) + 0.1)]


# two decision sets on p1, one per phi, drawn over their derived regions
def plotted_sets():
    generator = np.random.default_rng(4)
    return [PlottedSet("random search, phi_lu", "p1", "lu", 5, 5000,
                       generator.random((40, 2))),
            PlottedSet("random search, phi_cw", "p1", "cw", 5, 5000,
                       generator.random((40, 2)))]


# plot_fronts writes a non-empty figure to the path it was given
def test_plot_fronts_writes_a_non_empty_figure(tmp_path):
    path = tmp_path / "fronts.png"
    assert plot_fronts(plotted_fronts(), [(0, 1), (2, 3)], "p1 under phi_lu",
                       path) == path
    assert path.exists() and path.stat().st_size > 0


# plot_decision_sets writes a non-empty figure to the path it was given
def test_plot_decision_sets_writes_a_non_empty_figure(tmp_path):
    path = tmp_path / "sets.png"
    assert plot_decision_sets(plotted_sets(), "p1 recovered sets", path) == path
    assert path.exists() and path.stat().st_size > 0


# the column pairs are the caller's and the module chooses none of its own
def test_plot_fronts_refuses_an_empty_or_out_of_range_projection(tmp_path):
    with pytest.raises(ValueError, match="at least one pair"):
        plot_fronts(plotted_fronts(), [], "no pairs", tmp_path / "a.png")
    with pytest.raises(ValueError, match="outside"):
        plot_fronts(plotted_fronts(), [(0, 9)], "wrong column", tmp_path / "b.png")


# an overlay is of fronts in one image space, so two column counts are refused
def test_plot_fronts_refuses_two_image_spaces(tmp_path):
    fronts = plotted_fronts() + [PlottedFront("wider", 5, 5000, np.zeros((4, 6)))]
    with pytest.raises(ValueError, match="columns between them"):
        plot_fronts(fronts, [(0, 1)], "two spaces", tmp_path / "c.png")


# the derived region is drawn once per phi present, and only where the problem is p1
def test_the_region_is_drawn_once_per_phi_and_only_for_p1():
    axis = Figure().subplots()
    draw_regions(axis, plotted_sets() + [plotted_sets()[0]])
    assert len(axis.lines) == 2
    other = Figure().subplots()
    draw_regions(other, [PlottedSet("dtlz2 under phi_lu", "dtlz2", "lu", 5, 5000,
                                    np.zeros((3, 2)))])
    assert len(other.lines) == 0


# the residual of b1 section 2.4's phi_ls inequality, 7 x_1 x_2 - 4 x_1 + 12 x_2 - 16
def ls_form(x_1, x_2):
    return 7.0 * x_1 * x_2 - 4.0 * x_1 + 12.0 * x_2 - 16.0


# the residual of b1 section 2.4's other bound on X_lu, 4 x_1 - x_1 x_2 - 20 x_2 + 16
def lu_lower_form(x_1, x_2):
    return 4.0 * x_1 - x_1 * x_2 - 20.0 * x_2 + 16.0


# the drawn boundary lies on b1 section 2.4's closed form for its own phi.
# the inequalities are written here and not in the module, so a passing test means
# the drawn curve is where the derivation puts it and not that one file agrees
# with itself, which is what tests/test_reference_fronts.py does for b2's points
@pytest.mark.parametrize("phi_name", ("lu", "ls", "cw"))
def test_the_drawn_boundary_lies_on_b1s_closed_form(phi_name):
    x_1, x_2 = region_boundary(phi_name)
    if phi_name == "cw":
        residuals = [-x_1, -x_2, x_1 - 1.0, x_2 - 1.0]
    elif phi_name == "ls":
        residuals = [-x_1, -x_2, x_1 - four_thirds, x_2 - four_thirds,
                     ls_form(x_1, x_2)]
    else:
        residuals = [-x_1, lu_lower_form(x_1, x_2), ls_form(x_1, x_2)]
    assert max(float(np.max(residual)) for residual in residuals) <= residual_bound


# and it touches the extremes b1 section 2.4 states, which a curve drawn over the
# wrong interval would not
def test_the_drawn_boundary_reaches_b1s_extremes():
    lu_x_1, lu_x_2 = region_boundary("lu")
    assert (float(np.max(lu_x_1)), float(np.min(lu_x_2)), float(np.max(lu_x_2))) == (
        four_thirds, 0.8, four_thirds)
    ls_x_1, ls_x_2 = region_boundary("ls")
    assert (float(np.max(ls_x_1)), float(np.max(ls_x_2))) == (four_thirds, four_thirds)


# no region is drawn for a phi b1 derived none for
def test_an_unknown_phi_has_no_drawn_region():
    with pytest.raises(ValueError, match="section 2.4"):
        region_boundary("golden")


# a file whose rows are under no block is refused rather than read as a table
def test_a_table_without_a_block_is_refused(tmp_path):
    path = tmp_path / "loose.csv"
    path.write_text("problem,phi\np1,lu\n")
    with pytest.raises(ValueError, match="opens with a block"):
        read_metrics_table(path)
