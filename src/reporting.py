# d3: the tables and the figures e1, e2 and e3 produce, and the point at which a
# restriction that holds in the code has to still hold in the artefact.
#
# what this module is for. d1's three metrics are valid for comparing solvers
# under one fixed phi and are never a ranking of phi, CONTEXT.md section 5 step 5,
# and d2's are the ones the decision space makes comparable across phi. those two
# statements are written into src/metrics_objective.py and src/metrics_decision.py
# and a reader of a csv has neither file in front of them. so the separation is
# written into the file itself, as two blocks with different columns and a stated
# restriction above each, and not into a caption that travels separately and gets
# lost. a reader holding only the csv must not be able to make a comparison the
# metrics do not support.
#
# what it refuses, and why refusing is the job. a row is a mapping and not a
# record, so a field can be missing, and save_metrics_table refuses the whole
# table naming the field rather than writing a cell that is silently empty. the
# fields it insists on are the ones without which a number cannot be read later:
# the seed count and the budget, because a metric is a metric at a budget and
# over a set of seeds; the cardinality, because all three objective-space metrics
# move with it by more than the differences e1 is trying to detect, r-16; the
# reference size, the sampling mode and include_singular_segments, because two
# reference fronts built at two settings are two different objects and an igd
# against one is not comparable with an igd against the other, r-12 and r-13 and
# s-12; the hypervolume reference point and the rule that produced it, because the
# same front against two points is two numbers and moocore clips at the point
# rather than refusing, so an unrecorded point is not a measurement; delta and the
# scale of the decision box, because a coverage at one delta is not a coverage at
# another and neither means anything without the side of the box beside it; and
# the status of a phi pair, because on the two pairs involving phi_ls one
# direction of coverage and of overlap is fixed by a containment before any solver
# runs, r-06 and r-11, and a difference measured there is in part a theorem.
# catching a missing field at write time costs one exception; catching it at
# reading time in october costs the run that produced the table.
#
# no metric is computed here. every value in a row was produced by d1 or d2 and
# this module renders it. the one arithmetic it does is the summary across seeds,
# summarize_across_seeds, which is a median and an interquartile range of values
# it was handed and is required by CONTEXT.md section 10 d3 in every row: a single
# number over several seeds hides whether the seeds agreed, and one run per
# configuration gives no variance at all, CONTEXT.md section 10 c2.
#
# the labels are not re-declared. check and finding come from
# src/metrics_decision.py, the reference-point rules from
# src/metrics_objective.py and the sampling modes from src/reference_fronts.py, so
# a table cannot state a mode or a rule that the module producing the number does
# not have, and renaming one of them there breaks the table rather than silently
# writing the old name.
#
# the figures. every one carries the budget, the seed count and the cardinality of
# each series inside the figure, in the legend entry, and never in the filename: a
# file gets renamed, moved and pasted into a document, and the numbers that say
# what it is have to travel inside the image. the plotted records below are what
# makes that possible, each series arriving with those three values rather than
# with an array alone.
#
# plot_decision_sets draws b1's closed-form region behind the recovered sets where
# the problem is p1, which is the one figure this project can produce that shows
# the derived answer and what each solver found in one picture. the three regions
# are docs/b1_phi_efficient_sets.md section 2.4, transcribed here as the two
# curves and the two boxes that bound them, the same closed forms
# tests/test_reference_fronts.py checks b2's sampled points against. they are
# drawn and nothing is computed from them: src/reference_fronts.py encodes b1's
# map w -> x(w) and deliberately not its region, that being the derivation's
# output rather than its content, and this module does not change that.
#
# plot_convergence is not here. it would need a per-generation record of the
# front or of an indicator, and src/runners.py records no such thing: a
# SearchResult carries the seed, the budget, the final front and the matching
# decision vectors, and pymoo's history is not requested from minimize. adding
# that recording is a change to c2 and is not this session's, so this module does
# not carry a convergence figure and does not carry a stub that would look like
# one.
#
# no tolerance anywhere, d-02 and CONTEXT.md section 5. nothing here compares two
# objective rows or two decision vectors; the module formats, refuses and draws.
# a value is written with repr, which round-trips a double exactly, so a table
# read back holds the numbers that were written and two runs on the same input
# give the same bytes.

import csv
from collections import namedtuple

import numpy as np
from matplotlib.figure import Figure

from metrics_decision import check_status, finding_status, require_decision_set
from metrics_objective import reference_point_rules, require_front
from reference_fronts import sampling_modes

# the two blocks, named in the file and in the mapping save_metrics_table takes.
# both are written even where one is empty: a table showing one block alone
# invites being read as the whole comparison, and an empty block is a statement
# while a missing one is an omission.
objective_block = "objective_space"
decision_block = "decision_space"
blocks = (objective_block, decision_block)

# the columns of the objective-space block, which are also its required fields and
# the order they are written in. every one of them is named in the module comment
# above with the reason a number is unreadable without it.
objective_fields = ("problem", "phi", "solver", "metric", "n_seeds", "n_evals",
                    "cardinality", "reference_size", "sampling_mode",
                    "include_singular_segments", "hv_reference_rule",
                    "hv_reference_point", "median", "q1", "q3", "iqr")

# the columns of the decision-space block. phi_a, phi_b and status travel
# together: the pair is what the row is about and the status is how it may be
# read, so the column is in the block's fields and a row cannot be written into
# this block without it.
decision_fields = ("problem", "phi_a", "phi_b", "status", "metric", "n_seeds",
                   "n_evals", "cardinality_a", "cardinality_b", "delta",
                   "box_scale", "containment_violations", "note", "median", "q1",
                   "q3", "iqr")

block_fields = {objective_block: objective_fields, decision_block: decision_fields}

# the metrics each block may carry, d1's three and d2's eight. the restriction the
# block header states is about these and no others, so a hypervolume in the
# decision block, which a reader would take as comparable across phi, is refused
# rather than written under a line saying that it is.
objective_metrics = ("hypervolume", "igd", "spread")
decision_metrics = ("hausdorff_a_to_b", "hausdorff_b_to_a", "hausdorff_symmetric",
                    "coverage_a_in_b", "coverage_b_in_a", "overlap",
                    "cross_a_under_b", "cross_b_under_a")
block_metrics = {objective_block: objective_metrics, decision_block: decision_metrics}

# the one field whose value may be absent, and its absence says something. d2
# returns None for the phi_lu against phi_cw pair, which no containment covers, so
# an empty cell there is the absence of a containment and a zero would be a count
# of rounding on a pair that has none.
optional_value_fields = ("containment_violations",)

# how each column is read back, so that a table round-trips to the values written
# and not to their strings. everything unlisted is text.
integer_fields = ("n_seeds", "n_evals", "cardinality", "cardinality_a",
                  "cardinality_b", "reference_size", "containment_violations")
float_fields = ("median", "q1", "q3", "iqr", "delta", "box_scale")
boolean_fields = ("include_singular_segments",)
point_fields = ("hv_reference_point",)

# the restriction above each block, written into the artefact. the first block's
# is the whole reason the two are separate.
block_notes = {
    objective_block: (
        "hypervolume, igd and spread are computed on the (k, 2m) rows of one",
        "phi's image. each phi maps the same problem into a different space on a",
        "different scale, CONTEXT.md section 5 step 5, so these compare solvers",
        "under one fixed phi and never rank one phi against another; a ratio",
        "taken across two phi here is a ratio of volumes in two different spaces",
        "and means nothing. all three move with the cardinality, r-16, which is",
        "why every row states the one it was computed at.",
    ),
    decision_block: (
        "hausdorff, coverage, overlap and cross evaluation are computed on the",
        "recovered sets in the decision space, which is the one space every phi",
        "shares, so these are the metrics comparable across phi and this is the",
        "block a phi comparison is read from. a row whose status is check has one",
        "direction fixed by a containment before any solver ran, r-06 and r-11,",
        "so a difference there is in part a theorem; only a row whose status is",
        "finding carries the sensitivity signal.",
    ),
}

# the preamble both blocks share, above them in the file
table_notes = (
    "metrics table, written by src/reporting.py, subpart d3. two blocks with",
    "different columns, and the split is the content and not the layout.",
    "every value is a median with its interquartile range over the seed count in",
    "the same row, and every row states the evaluation budget and the",
    "cardinality it was computed at. no cell is one run.",
)

# the problem b1 derived a closed-form region for, and the only one whose region a
# figure draws. docs/b1_phi_efficient_sets.md section 7.4 is why p0 has none.
region_problem = "p1"

# the derived regions are drawn in one grey with a line style per phi, so that a
# region never takes a colour from the series drawn over it and a reader cannot
# match the wrong boundary to a set by colour.
region_colour = "0.35"
region_styles = {"lu": "-", "ls": "--", "cw": ":"}

# b1 section 2.4's extreme values, as exact doubles
four_fifths = 4.0 / 5.0
four_thirds = 4.0 / 3.0

# how many points the two curved boundaries are drawn with. a drawing resolution
# and not a reporting parameter: it converges to the same curve and names no
# different object, so it is a constant here for the reason
# src/reference_fronts.py's oversampling_factor is one there.
boundary_resolution = 200


# the median and the interquartile range of one metric over the seeds it was run at
def summarize_across_seeds(values):
    # returned as the row's own fields rather than as a record, so that a caller
    # merges it into the row and cannot carry the median without the seed count
    # that produced it. numpy's linear quartiles, so four seeds giving 1, 2, 3, 4
    # give q1 = 1.75, median = 2.5 and q3 = 3.25.
    array = np.asarray(values, dtype=float)
    if array.ndim != 1 or array.size < 1:
        raise ValueError(
            "values must be one metric's value at each seed, one dimension and at "
            "least one entry; got shape {}. CONTEXT.md section 10 d3 asks for a "
            "median with an interquartile range and never a single number"
            .format(array.shape))
    q1, median, q3 = np.percentile(array, (25.0, 50.0, 75.0))
    return {"n_seeds": int(array.size), "median": float(median), "q1": float(q1),
            "q3": float(q3), "iqr": float(q3 - q1)}


# one cell, formatted so that identical inputs give identical bytes
def format_value(field, value):
    # repr on a double is the shortest text that reads back as the same double, so
    # a table round-trips exactly and two runs agree byte for byte. bool is tested
    # before int because it is one.
    if value is None:
        return ""
    if isinstance(value, (bool, np.bool_)):
        return str(bool(value))
    if isinstance(value, (int, np.integer)):
        return str(int(value))
    if isinstance(value, (float, np.floating)):
        return repr(float(value))
    if isinstance(value, (list, tuple, np.ndarray)):
        return " ".join(repr(float(entry))
                        for entry in np.asarray(value, dtype=float).ravel())
    text = str(value)
    if "\n" in text or "\r" in text:
        raise ValueError(
            "the value of {!r} carries a line break; the table is read back a "
            "line at a time and a wrapped cell would not survive it".format(field))
    return text


# one cell, read back as the value that was written
def parse_value(field, text):
    if text == "":
        return None
    if field in integer_fields:
        return int(text)
    if field in float_fields:
        return float(text)
    if field in boolean_fields:
        if text not in ("True", "False"):
            raise ValueError(
                "{} reads {!r} and it is a flag stated as True or False, s-12"
                .format(field, text))
        return text == "True"
    if field in point_fields:
        return tuple(float(entry) for entry in text.split(" "))
    return text


# raises unless the results name both blocks, nothing else, and hold a row between them
def require_blocks(results):
    missing = [name for name in blocks if name not in results]
    if missing:
        raise ValueError(
            "results must name every block, {}; it is missing {}. an empty block "
            "is written as an empty block, since a table showing one of the two "
            "alone reads as the whole comparison".format(list(blocks), missing))
    unknown = [name for name in results if name not in blocks]
    if unknown:
        raise ValueError(
            "results names {} and the blocks are {}; the two differ in what may "
            "be compared across phi and a third would say nothing about that"
            .format(unknown, list(blocks)))
    if not any(len(results[name]) for name in blocks):
        raise ValueError("results holds no rows in either block; there is no table")


# whether a value would reach the file as an empty cell
def is_empty(value):
    # None and blank text are the same thing once written, a cell with nothing in
    # it under a column that says what the number beside it means.
    return value is None or (isinstance(value, str) and not value.strip())


# raises unless a row carries exactly its block's fields, naming the field it lacks
def require_row_fields(row, block_name, index):
    fields = block_fields[block_name]
    for field in fields:
        if field not in row:
            raise ValueError(
                "row {} of the {} block lacks the required field {!r}. every "
                "field of that block is required, CONTEXT.md section 10 d3: a "
                "table that cannot be interpreted later is refused at write time "
                "and not discovered at reading time".format(index, block_name, field))
        if is_empty(row[field]) and field not in optional_value_fields:
            raise ValueError(
                "row {} of the {} block leaves {!r} empty, and only {} may be "
                "absent; an empty cell under any other column is a number with "
                "nothing saying what it is".format(index, block_name, field,
                                                   list(optional_value_fields)))
    unknown = [field for field in row if field not in fields]
    if unknown:
        raise ValueError(
            "row {} of the {} block carries {}, which that block has no column "
            "for; the value would not reach the file at all"
            .format(index, block_name, sorted(unknown)))


# raises unless a stated value is one the module that produced the number has
def require_choice(value, allowed, field, block_name, index):
    if value not in allowed:
        raise ValueError(
            "row {} of the {} block states {} = {!r} and it must be one of {}; "
            "the names come from the modules that produce the numbers and are "
            "not re-declared here".format(index, block_name, field, value,
                                          list(allowed)))


# raises unless the row's stated parameters are the ones its metric was produced under
def require_row_values(row, block_name, index):
    require_choice(row["metric"], block_metrics[block_name], "metric", block_name,
                   index)
    if block_name == objective_block:
        require_choice(row["sampling_mode"], sampling_modes, "sampling_mode",
                       block_name, index)
        require_choice(row["hv_reference_rule"], reference_point_rules,
                       "hv_reference_rule", block_name, index)
        if not isinstance(row["include_singular_segments"], (bool, np.bool_)):
            raise ValueError(
                "row {} of the {} block states include_singular_segments as {!r} "
                "and it is True or False; the two settings are two different "
                "reference fronts, r-12 and s-12"
                .format(index, block_name, row["include_singular_segments"]))
    else:
        require_choice(row["status"], (check_status, finding_status), "status",
                       block_name, index)


# writes the preamble and one block's restriction as comment lines
def write_notes(handle, lines):
    for line in lines:
        handle.write("# {}\n".format(line))


# writes one block: its name, its restriction, its header and its rows
def write_block(handle, writer, block_name, rows):
    handle.write("\n")
    writer.writerow(["block", block_name])
    write_notes(handle, block_notes[block_name])
    fields = block_fields[block_name]
    writer.writerow(list(fields))
    for row in rows:
        writer.writerow([format_value(field, row[field]) for field in fields])


# writes the objective-space and decision-space metrics as one csv, in two blocks
def save_metrics_table(results, path):
    # the whole table is checked before anything is written, so a refusal leaves
    # no half-written file to be read as a table.
    require_blocks(results)
    for block_name in blocks:
        for index, row in enumerate(results[block_name]):
            require_row_fields(row, block_name, index)
            require_row_values(row, block_name, index)
    with open(path, "w", newline="", encoding="utf-8") as handle:
        write_notes(handle, table_notes)
        writer = csv.writer(handle, lineterminator="\n")
        for block_name in blocks:
            write_block(handle, writer, block_name, results[block_name])
    return path


# the rows of a written table, comments and blank lines dropped
def table_records(path):
    with open(path, newline="", encoding="utf-8") as handle:
        lines = [line for line in handle
                 if line.strip() and not line.startswith("#")]
    return [record for record in csv.reader(lines) if record]


# one written record, read back as the row that was written
def parse_row(record, block_name, index):
    fields = block_fields[block_name]
    if len(record) != len(fields):
        raise ValueError(
            "row {} of the {} block holds {} cells and the block has {} columns"
            .format(index, block_name, len(record), len(fields)))
    return {field: parse_value(field, text) for field, text in zip(fields, record)}


# reads a table back as the mapping save_metrics_table was given
def read_metrics_table(path):
    results = {name: [] for name in blocks}
    block_name = None
    for record in table_records(path):
        if record[0] == "block":
            block_name = record[1]
            if block_name not in blocks:
                raise ValueError("the file names a block {!r} and the blocks are "
                                 "{}".format(block_name, list(blocks)))
        elif block_name is None:
            raise ValueError(
                "the file opens with {!r} and a table opens with a block; every "
                "row belongs to one of the two and a row outside them has no "
                "restriction over it".format(record[0]))
        elif tuple(record) != block_fields[block_name]:
            results[block_name].append(
                parse_row(record, block_name, len(results[block_name])))
    return results


# one series of a figure, carrying a front and the three values that say what it is
PlottedFront = namedtuple("PlottedFront", ("label", "n_seeds", "n_evals", "rows"))

# one series of a decision-space figure. the problem and the phi are on the record
# because the region drawn behind the points is that phi's and exists for p1 alone.
PlottedSet = namedtuple(
    "PlottedSet", ("label", "problem_name", "phi_name", "n_seeds", "n_evals",
                   "points"))


# the legend entry of one series: what it is, at what budget, over how many seeds
def series_label(item, cardinality):
    # in the figure and never in the filename, CONTEXT.md section 10 d3: a file is
    # renamed and pasted into a document and the numbers that say what it is have
    # to travel inside the image.
    return "{}  budget {}, {} seeds, k = {}".format(
        item.label, int(item.n_evals), int(item.n_seeds), int(cardinality))


# the name of one column of the 2m image, in the order src/reference_fronts.py returns
def column_name(index):
    return ("Lambda_{}^T f" if index % 2 == 0 else "B_{}^T f").format(index // 2 + 1)


# raises unless every plotted front is a (k, 2m) array over one image space
def require_plotted_fronts(fronts):
    if len(fronts) < 1:
        raise ValueError("fronts must hold at least one front to plot")
    widths = set()
    for item in fronts:
        widths.add(require_front(item.rows, item.label).shape[1])
    if len(widths) != 1:
        raise ValueError(
            "the fronts have {} columns between them; an overlay is of fronts in "
            "one phi's image and two image spaces do not share axes"
            .format(sorted(widths)))
    return widths.pop()


# raises unless the column pairs are usable pairs of the fronts' 2m columns
def require_col_pairs(col_pairs, n_cols):
    pairs = [tuple(int(index) for index in pair) for pair in col_pairs]
    if not pairs:
        raise ValueError(
            "col_pairs must name at least one pair of columns; the projection is "
            "an argument and this module does not choose it, CONTEXT.md section "
            "10 d3")
    for pair in pairs:
        if len(pair) != 2 or pair[0] == pair[1]:
            raise ValueError(
                "{} is not a pair of two distinct columns".format(pair))
        if any(not 0 <= index < n_cols for index in pair):
            raise ValueError(
                "{} names a column outside the {} the fronts have"
                .format(pair, n_cols))
    return pairs


# overlays fronts, one 2d panel per stated column pair
def plot_fronts(fronts, col_pairs, title, path):
    n_cols = require_plotted_fronts(fronts)
    pairs = require_col_pairs(col_pairs, n_cols)
    figure = Figure(figsize=(4.6 * len(pairs), 4.4), layout="constrained")
    axes = figure.subplots(1, len(pairs), squeeze=False)[0]
    for axis, (first, second) in zip(axes, pairs):
        for item in fronts:
            rows = np.asarray(item.rows, dtype=float)
            axis.scatter(rows[:, first], rows[:, second], s=12,
                         label=series_label(item, len(rows)))
        axis.set_xlabel(column_name(first))
        axis.set_ylabel(column_name(second))
    axes[0].legend(loc="best", fontsize="small")
    figure.suptitle(title)
    figure.savefig(path)
    return path


# raises unless every plotted set is a (k, n_vars) decision set with n_vars at least two
def require_plotted_sets(sets):
    if len(sets) < 1:
        raise ValueError("sets must hold at least one decision set to plot")
    for item in sets:
        if require_decision_set(item.points, item.label).shape[1] < 2:
            raise ValueError(
                "{} has one decision variable; this figure is the plane the "
                "derived regions live in".format(item.label))


# the curve x_1 = (16 - 12 x_2) / (7 x_2 - 4), b1 section 2.4
def upper_boundary(x_2):
    # the upper boundary of X_lu and of X_ls alike, b1 section 2.4: the same curve
    # bounds both, running from (4/3, 1) to (0, 4/3).
    return (16.0 - 12.0 * x_2) / (7.0 * x_2 - 4.0)


# the curve x_1 = (20 x_2 - 16) / (4 - x_2), b1 section 2.4
def lower_boundary(x_2):
    # the other boundary of X_lu, running from (0, 4/5) to (4/3, 1).
    return (20.0 * x_2 - 16.0) / (4.0 - x_2)


# b1 section 2.4's closed-form region boundary for one phi, as (x_1, x_2)
def region_boundary(phi_name):
    # transcribed from docs/b1_phi_efficient_sets.md section 2.4 and drawn only:
    # X_lu is bounded by the two curves above, X_ls is [0, 4/3]^2 cut by the same
    # upper curve and X_cw is the unit square. these are the closures; the open
    # segment x_2 = 0 that b1 excludes from X_ls and X_cw is the undecided
    # singular segment of b1 section 2.6, s-12, and is not drawn separately.
    upper = np.linspace(1.0, four_thirds, boundary_resolution)
    if phi_name == "cw":
        return (np.array([0.0, 1.0, 1.0, 0.0, 0.0]),
                np.array([0.0, 0.0, 1.0, 1.0, 0.0]))
    if phi_name == "ls":
        return (np.concatenate([[0.0, four_thirds], upper_boundary(upper), [0.0]]),
                np.concatenate([[0.0, 0.0], upper, [0.0]]))
    if phi_name == "lu":
        lower = np.linspace(four_fifths, 1.0, boundary_resolution)
        return (np.concatenate([lower_boundary(lower), upper_boundary(upper), [0.0]]),
                np.concatenate([lower, upper, [four_fifths]]))
    raise ValueError(
        "docs/b1_phi_efficient_sets.md section 2.4 derives a region for lu, ls "
        "and cw; got {!r}".format(phi_name))


# draws the derived regions of the phi present, behind everything else
def draw_regions(axis, sets):
    drawn = set()
    for item in sets:
        key = (item.problem_name, item.phi_name)
        if item.problem_name != region_problem or key in drawn:
            continue
        drawn.add(key)
        x_1, x_2 = region_boundary(item.phi_name)
        axis.plot(x_1, x_2, color=region_colour,
                  linestyle=region_styles[item.phi_name], linewidth=1.3, zorder=1,
                  label="derived X_{}, b1 section 2.4".format(item.phi_name))


# the recovered sets in decision space, with b1's derived region behind them
def plot_decision_sets(sets, title, path):
    require_plotted_sets(sets)
    figure = Figure(figsize=(6.4, 5.8), layout="constrained")
    axis = figure.subplots()
    draw_regions(axis, sets)
    for item in sets:
        points = np.asarray(item.points, dtype=float)
        axis.scatter(points[:, 0], points[:, 1], s=12, zorder=2,
                     label=series_label(item, len(points)))
    axis.set_xlabel("x_1")
    axis.set_ylabel("x_2")
    axis.legend(loc="best", fontsize="small")
    figure.suptitle(title)
    figure.savefig(path)
    return path
