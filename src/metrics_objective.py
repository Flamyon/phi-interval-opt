# d1: the three objective-space metrics, and the truncation that makes them
# comparable across solvers.
#
# what they are for, and what they are not for. hypervolume, igd and spread are
# computed on the (k, 2m) fronts the solvers return, and those fronts live in the
# image of one phi. each phi maps the same interval problem into a different
# space on a different scale, CONTEXT.md section 5 step 5, so a hypervolume under
# phi_lu and a hypervolume under phi_cw are volumes of regions in two different
# spaces and their ratio means nothing. these three compare solvers under one
# fixed phi and never rank phi against each other, and every table that carries
# one carries that restriction in writing. the metrics that are comparable across
# phi are d2's, in the decision space, which is the one space every phi shares.
#
# which pymoo indicator each of the three uses, and where.
#     compute_hv    pymoo.indicators.hv.HV, which is pymoo 0.6.2's Hypervolume
#         and delegates to moocore's hypervolume. it is constructed here with
#         ref_point alone and zero_to_one left at its default False, so
#         pymoo's normalization is the identity and the reference point this
#         module is handed is the reference point moocore is given.
#     compute_igd   pymoo.indicators.igd.IGD, which delegates to moocore's igd
#         with norm_by_dist left at its default False.
#     compute_spread   no pymoo indicator. see below.
#
# what pymoo does that differs from the definition, reported and not worked
# around. moocore's hypervolume clips at the reference point rather than
# refusing: a front row lying beyond the reference point in some column
# contributes nothing there instead of raising, measured in v-59, the
# rows (0, 1) and (3, 0.5) against the reference point (2, 2) giving 2.0, which
# is (0, 1)'s box alone. so a reference point that does not dominate the whole
# front silently discards part of it, which is one more reason the point is an
# argument and is recorded. pymoo's igd is the average over the reference points
# of the distance to the nearest front point, the formula
# docs/b2b_reference_density.md section 1 states, and not the average over the
# front points: measured in v-59, one reference point at the origin against the
# front (0, 0) and (10, 10) gives 0 and the transposed call gives
# 7.0710678118654755, which is sqrt(200) / 2. note that it is therefore not [2]'s M_1^*, equation (17) on
# printed page 181, which averages over the front and is the other direction.
#
# spread, and why it is not a pymoo indicator. pymoo 0.6.2 ships
# indicators/spacing.py, whose SpacingIndicator is a spread of the
# nearest-neighbour distances in the cityblock metric normalised by the number of
# points; that quantity is defined in none of the papers this project has read,
# and CONTEXT.md section 11's evidence rule admits a definition only from a paper
# read here and recorded with its location. so compute_spread is [2]'s M_3^*,
# definition 6 equation (19) on printed page 181, read from the rendered page as
# a5 read equation (7), v-58:
#     M_3^*(Y') = sqrt( sum over i = 1 to n of max{ |p'_i - q'_i| : p', q' in Y' } )
# the maximum over pairs of the ith coordinate difference is that column's range,
# so this is the euclidean norm of the vector of per-column ranges, and [2] page
# 181 says what it is for: "the maximum extent in each dimension to estimate the
# range to which the front spreads out. in the case of two objectives, this
# equals the distance of the two outer solutions". larger is wider. the
# limitation is the same sentence read carefully and it is not hidden here: M_3^*
# reads the extremes of each column and nothing between them, so a front that
# clusters in the interior scores exactly as one that fills it, which
# tests/test_metrics_objective.py asserts rather than leaves to be discovered.
# [2]'s own distribution metric is M_2^*, equation (18), and it takes a
# neighbourhood parameter sigma^*; adding one would change the signature
# CONTEXT.md section 10 d1 fixes, so it is not taken here and the choice is the
# research chat's.
#
# every reference is an argument and none is built inside. igd's reference front
# comes from src/reference_fronts.py with include_singular_segments stated, s-12,
# and sampling_mode stated, r-13, and it is the farthest-point mode d1 uses:
# docs/b2b_reference_density.md section 6 builds two fronts of equal fill
# distance and the two references rank them in opposite orders, so the mode is
# not a refinement of a number but a decision about a comparison. igd_reference
# below returns those values beside the front so a table cannot print the metric
# without them.
#
# the hypervolume reference point is in 2m dimensions, is fixed per phi and is an
# argument for the same reason: the same front against two reference points is
# two numbers, so a hypervolume whose point is unrecorded is not a measurement.
# derive_reference_point takes the rule by name and returns it with the point, so
# what a table carries is the rule and not 2m numbers from nowhere.
#
# the cardinality rule, r-16. all three metrics move with the number of rows the
# front carries, measured in c2-b on one fixed front subsampled uniformly at
# random, v-52: igd 0.1303 at 25 rows against 0.0201 at all 610, and hypervolume
# 4.6845 against 5.1665, on the same points from the same search. the three
# solvers return very different sizes, nsga-ii exactly its population, mopso at
# most its archive and random search whatever is non-dominated, so a metric
# compared across solvers is computed at a common cardinality, reached by
# truncate_to_common_cardinality at a stated seed. uniform and not
# crowding-distance based: a crowding selection is a spread rule and would be
# reported beside spread. the common size is common_cardinality over every front
# in the comparison and not per phi, ND_lu being contained in ND_ls,
# docs/a_close_containment.md, so the smallest front is systematically phi_lu's
# and truncating each phi to its own smallest would put a phi-dependent selection
# inside the one comparison the study exists to make. the rule is for these three
# metrics only: d2's hausdorff, coverage and overlap are set-geometry measures in
# the decision space and are computed on the full recovered sets.
#
# no tolerance anywhere, d-02 and CONTEXT.md section 5. nothing here compares two
# objective rows: these are distances, volumes and ranges, and the dominance
# relation is src/random_search.py's alone. the truncation draws indices and
# copies rows and rounds nothing.
#
# [1] is papers/new_preference_order_relationships_paper.txt, costa,
# osuna-gomez and chalco-cano, fuzzy sets and systems 477 (2024) 108812.
# [2] is papers/zitzler_deb_thiele_2000_comparison.pdf, zitzler, deb and thiele,
# evolutionary computation 8(2) (2000) 173-195.

from collections import namedtuple

import numpy as np
from pymoo.indicators.hv import HV
from pymoo.indicators.igd import IGD

# imported as a module and not by name: compute_igd's second parameter is called
# reference_front, the name CONTEXT.md section 10 d1 gives it, and a from-import
# of src/reference_fronts.py's function of that name would be shadowed inside it.
import reference_fronts

# a hypervolume reference point with the rule that produced it and the number of
# rows it was derived from. the point alone is 2m numbers a table cannot check;
# the rule is what makes it reproducible, so the two travel together.
ReferencePoint = namedtuple("ReferencePoint", ("rule", "point", "n_rows"))

# an igd reference front with every value a table has to print beside it. the
# front is the (k, 2m) array; the other five fields are what say which object it
# is, r-12, r-13 and s-12.
IgdReference = namedtuple(
    "IgdReference",
    ("phi_name", "n_points", "include_singular_segments", "sampling_mode", "seed",
     "front"),
)

# the two rules a hypervolume reference point may be derived by. both are read
# off the rows they are given, which is the reference front where one exists, and
# both name what they do: the nadir is the componentwise maximum of those rows
# exactly, and the second adds a tenth of each column's range to it. the tenth is
# in the rule's name and not in a table's footnote, so a table carrying the rule
# carries the constant. the strict nadir gives the extreme rows zero thickness in
# the column they are extreme in, and the margin rule is the one to use where
# that matters; neither is a default and the caller states which.
nadir_rule = "reference_front_nadir"
nadir_margin_rule = "reference_front_nadir_plus_range_tenth"
reference_point_rules = (nadir_rule, nadir_margin_rule)

# the fraction of each column's range the margin rule adds, named by the rule
nadir_margin_fraction = 0.1


# raises unless rows is a (k, 2m) array of objective rows with k >= 1
def require_front(rows, name):
    array = np.asarray(rows, dtype=float)
    if array.ndim != 2:
        raise ValueError(
            "{} must have shape (k, 2m), one objective row per row; got shape "
            "{}. these metrics live in the phi image space, CONTEXT.md section 5 "
            "step 5, and a (k, n_vars) decision set is not a front"
            .format(name, array.shape))
    if array.shape[0] < 1:
        raise ValueError(
            "{} must hold at least one objective row; got {} rows. none of these "
            "metrics is defined on an empty front and none is returned as zero"
            .format(name, array.shape[0]))
    return array


# raises unless two fronts have the same 2m columns, so they share an image space
def require_matching_columns(array_a, array_b, name_a, name_b):
    if array_a.shape[1] != array_b.shape[1]:
        raise ValueError(
            "{} has {} columns and {} has {}; both are 2m columns of one phi's "
            "image and a metric between two image spaces is not defined"
            .format(name_a, array_a.shape[1], name_b, array_b.shape[1]))


# the volume dominated by the front and bounded by the reference point
def compute_hv(front, reference_point):
    # pymoo.indicators.hv.HV, with zero_to_one left False so the point passes
    # through unnormalised. the point is an argument and never derived here: the
    # same front against a different point is a different number, and moocore
    # clips rather than refusing, so a point that fails to dominate a row drops
    # that row's contribution silently. derive_reference_point states a rule.
    array = require_front(front, "front")
    point = np.asarray(reference_point, dtype=float)
    if point.ndim != 1 or point.size != array.shape[1]:
        raise ValueError(
            "reference_point must be one point in the front's {} image "
            "dimensions; got shape {}. it is in 2m dimensions and fixed per phi, "
            "CONTEXT.md section 10 d1".format(array.shape[1], point.shape))
    return float(HV(ref_point=point)(array))


# the mean over the reference front of the distance to the nearest front point
def compute_igd(front, reference_front):
    # pymoo.indicators.igd.IGD, the average over the reference points and not
    # over the front, docs/b2b_reference_density.md section 1. the reference is
    # an argument and is built by igd_reference or by the caller stating both
    # reporting parameters; nothing is constructed inside.
    array = require_front(front, "front")
    reference = require_front(reference_front, "reference_front")
    require_matching_columns(array, reference, "front", "reference_front")
    return float(IGD(reference)(array))


# the extent of the front, [2] definition 6 equation (19), printed page 181
def compute_spread(front):
    # M_3^* of [2]: the maximum over pairs of the ith coordinate difference is
    # column i's range, and the metric is the euclidean norm of those ranges.
    # larger is wider. it reads the extremes of every column and nothing between
    # them, so it measures the extent of the front and not the evenness of it.
    array = require_front(front, "front")
    ranges = np.max(array, axis=0) - np.min(array, axis=0)
    return float(np.sqrt(np.sum(np.square(ranges))))


# a hypervolume reference point derived from stated rows by a stated rule
def derive_reference_point(rows, rule):
    array = require_front(rows, "rows")
    if rule not in reference_point_rules:
        raise ValueError(
            "rule must be stated as one of {}; got {!r}. the rule is an argument "
            "so that a table carries it, CONTEXT.md section 10 d1: a hypervolume "
            "whose reference point came from nowhere is not a measurement"
            .format(list(reference_point_rules), rule))
    nadir = np.max(array, axis=0)
    if rule == nadir_rule:
        point = nadir
    else:
        point = nadir + nadir_margin_fraction * (nadir - np.min(array, axis=0))
    return ReferencePoint(rule=rule, point=point, n_rows=len(array))


# the igd reference front, with the four values a table has to print beside it
def igd_reference(problem, phi_name, n_points, include_singular_segments,
                  sampling_mode, params, seed):
    # a thin call of src/reference_fronts.py that constructs nothing of its own.
    # none of the five arguments has a default. the mode and the flag have none
    # there either, r-13 and s-12; the seed and params have none here because
    # they are reporting parameters too, the seed naming which draw this is and
    # params naming the image the front lives in, delta entering every image
    # coordinate as an additive constant, b1 section 1.2. a reference built at
    # one delta and a solver front produced at another are two different images.
    front = reference_fronts.reference_front(problem, phi_name, int(n_points),
                                             include_singular_segments,
                                             sampling_mode, params, seed)
    return IgdReference(phi_name=phi_name, n_points=int(n_points),
                        include_singular_segments=include_singular_segments,
                        sampling_mode=sampling_mode, seed=seed, front=front)


# the smallest front in a comparison, which is the cardinality every front is cut to
def common_cardinality(fronts):
    # r-16, and it is taken over every front the comparison holds, across phi and
    # not per phi: the smallest is systematically phi_lu's, ND_lu sitting inside
    # ND_ls, so a per-phi minimum would put a phi-dependent selection inside the
    # comparison. CONTEXT.md section 10 d1.
    sizes = [len(require_front(front, "front")) for front in fronts]
    if not sizes:
        raise ValueError(
            "fronts must hold at least one front; a common cardinality is taken "
            "over the fronts of one comparison, r-16")
    return int(min(sizes))


# a uniform random subsample of a front to a stated cardinality at a stated seed
def truncate_to_common_cardinality(front, n_keep, seed):
    # the one implementation, so that every caller truncates the same way. the
    # selection is uniform and not by crowding distance: a crowding selection is
    # a spread rule and would be reported beside spread, r-16. the kept rows come
    # back in the front's own order, so the result is a subsequence of its input
    # and not a reordering of it, and the draw is np.random.default_rng at the
    # stated seed, so it is bitwise reproducible.
    array = require_front(front, "front")
    target = int(n_keep)
    if target < 1:
        raise ValueError("n_keep must be at least 1; got {}".format(n_keep))
    if target > len(array):
        raise ValueError(
            "n_keep is {} and the front has {} rows; the truncation is to the "
            "smallest front in the comparison and never upward, r-16"
            .format(target, len(array)))
    generator = np.random.default_rng(seed)
    kept = np.sort(generator.choice(len(array), size=target, replace=False))
    return array[kept]
