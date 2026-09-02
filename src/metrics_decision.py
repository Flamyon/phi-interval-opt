# d2: the metrics that are comparable across phi, and the instrument the study's
# headline result is computed with.
#
# why these and not the objective-space ones. each phi maps the same interval
# problem into a different image space on a different scale, so hypervolume, igd
# and spread compare volumes measured in different spaces and cannot rank phi
# against each other; CONTEXT.md section 5 step 5 admits them for comparing
# solvers under a fixed phi and forbids them for comparing phi. the decision
# space is the same space for every phi, and it is where the answer to part 1's
# research question lives. that is why d2 is on the minimum presentable path of
# CONTEXT.md section 8 and d1 is not.
#
# every function here takes two (k, n_vars) arrays of decision vectors, never a
# front and never an index set, and the two arrays are the recovered sets in
# full: CONTEXT.md section 10 d1 restricts the common-cardinality truncation of
# r-16 to the objective-space metrics, because truncating a set-geometry measure
# in the decision space discards real coverage. what r-16 does require here is
# that the cardinality is printed beside every number, which is why the pairwise
# record below carries n_a and n_b and the comparison record carries the sizes.
#
# delta has no default, for the reason include_singular_segments has none in
# src/reference_fronts.py, s-12. it is a reporting parameter: two coverages at two
# delta are two different quantities and neither is comparable with the other, so
# the caller states it and its value belongs in every table that carries the
# metric, next to the scale of the decision box. p1's box is [-0.5, 1.5]^2, so a
# delta of 0.1 is a twentieth of the side; the number means nothing without that.
#
# no tolerance anywhere, d-02 and CONTEXT.md section 5. cross_evaluate filters
# through src/random_search.py's non_dominated_indices, which is the project's one
# dominance relation, and phi is applied through that module's phi_image, which
# takes the route the problem's declared representation names. neither is
# reimplemented here and no comparison in this module rounds, snaps or admits an
# epsilon. delta is a distance in the decision space and touches no order.
#
# the cost, r-15. non_dominated_indices is O(N^2 m) with (block x N x 2m) boolean
# temporaries, and r-15's mitigation rules out pymoo's NonDominatedSorting as a
# substitute, that being a decision against CONTEXT.md section 5 and not this
# session's to take. so cross_evaluate filters the whole of set_a once per call
# rather than once per pair of points, and one call is one filter. at the sizes e1
# will use this is not a constraint: on p1 at budget 5000 a random-search front is
# 586 to 2256 rows, docs/c3_validation.md section 5.3, and v-57 measures the
# filter at 66 s for n = 25000, which is quadratic, so a 2256-row call is well
# under a second and the six calls of one compare_phi_on_one_sample are seconds.
# the sets that would cost are unfiltered samples, and nothing here takes one.
#
# [1] is papers/new_preference_order_relationships_paper.txt, costa,
# osuna-gomez and chalco-cano, fuzzy sets and systems 477 (2024) 108812.

from collections import namedtuple

import numpy as np

from phi_transforms import phi_registry
from random_search import (filter_one_sample_under_every_phi, non_dominated_indices,
                           phi_image, require_phi)

# the two directed distances and the symmetric one. they are returned together and
# read apart: a_to_b is the largest distance from a point of set_a to the nearest
# point of set_b, so with set_b the reference it asks whether what was found is
# correct, and b_to_a asks whether what exists was found. the two answer different
# questions and a table that prints only the symmetric one has thrown the
# distinction away. docs/c3_validation.md section 1 is why that matters here: the
# forward direction carries a floor no budget removes, and the gate asserts the
# reverse direction alone and reports the forward one.
Hausdorff = namedtuple("Hausdorff", ("a_to_b", "b_to_a", "symmetric"))

# one pair of phi, its metrics over one sample, and the label that says how the
# pair may be read. status is the label; see pair_status for what the two values
# mean and why the field is not optional.
PhiPair = namedtuple(
    "PhiPair",
    ("phi_a", "phi_b", "status", "containment", "containment_violations", "note",
     "n_a", "n_b", "hausdorff", "coverage_a_in_b", "coverage_b_in_a", "overlap",
     "cross_a_under_b", "cross_b_under_a"),
)

# one call of compare_phi_on_one_sample: the sample the three sets were filtered
# out of, their sizes, and one PhiPair per pair. the sample is carried and not
# discarded for src/random_search.py's own reason, that three index sets over an
# array the caller no longer holds is not the isolation the comparison rests on.
PhiComparison = namedtuple(
    "PhiComparison",
    ("problem", "seed", "n_evals", "delta", "sample", "sizes", "pairs"),
)

# the three pairs, in the lu, ls, cw order of examples 2.2, 2.3 and 2.4 of [1],
# which is the order every table and every loop in the project uses.
phi_pairs = (("lu", "ls"), ("lu", "cw"), ("ls", "cw"))

# the two labels a pair can carry. they are not interchangeable and the difference
# is the whole of r-06: on a pair labelled a check one direction of coverage and
# of overlap is fixed by a containment before any code runs, so a difference
# measured there is in part a theorem. only the pair labelled a finding carries
# the sensitivity signal.
check_status = "check"
finding_status = "finding"

# the containment of docs/a_close_containment.md, as (inner, outer) per pair.
# corollaries 1 and 2: ND_lu and ND_cw both sit inside ND_ls, exactly and for
# every problem, from the criterion that phi_B = M phi_A with M entrywise
# non-negative and invertible makes phi_A-dominance imply phi_B-dominance. phi_lu
# and phi_cw are nested in neither direction, which is why that pair is the one
# CONTEXT.md section 10 e3 takes its headline number from.
containments = {("lu", "ls"): ("lu", "ls"), ("ls", "cw"): ("cw", "ls")}


# raises unless the array is a (k, n_vars) array of decision vectors with k >= 1
def require_decision_set(points, name):
    array = np.asarray(points, dtype=float)
    if array.ndim != 2:
        raise ValueError(
            "{} must have shape (k, n_vars), one decision vector per row; got "
            "shape {}. these metrics live in the decision space, CONTEXT.md "
            "section 5 step 5, and a (k, 2m) front is not a decision set"
            .format(name, array.shape))
    if array.shape[0] < 1:
        raise ValueError(
            "{} must hold at least one decision vector; got {} rows. a hausdorff "
            "distance to an empty set is not defined and is not returned as zero"
            .format(name, array.shape[0]))
    return array


# raises unless the two sets are decision sets over the same decision space
def require_decision_sets(set_a, set_b):
    array_a = require_decision_set(set_a, "set_a")
    array_b = require_decision_set(set_b, "set_b")
    if array_a.shape[1] != array_b.shape[1]:
        raise ValueError(
            "set_a has {} decision variables and set_b has {}; the decision space "
            "is the one space every phi shares, so two sets measured against each "
            "other are two sets in it".format(array_a.shape[1], array_b.shape[1]))
    return array_a, array_b


# raises unless delta was stated as a finite distance in the decision space
def require_delta(delta):
    value = float(delta)
    if not np.isfinite(value) or value < 0.0:
        raise ValueError(
            "delta must be a finite distance and at least zero; got {!r}. it has "
            "no default because it is a reporting parameter, s-12: its value "
            "belongs in every table that carries the metric, beside the scale of "
            "the decision box".format(delta))
    return value


# the distance from every point of set_a to the nearest point of set_b
def nearest_distances(array_a, array_b, block=256):
    # blocked for memory and not for meaning, as src/random_search.py's filter is:
    # the minimum is over the whole of set_b either way. the difference is formed
    # before it is squared rather than through an expansion of the squared norm,
    # so no cancellation is committed on points that are close together, which is
    # the whole population of a coverage measurement.
    out = np.empty(len(array_a))
    for start in range(0, len(array_a), block):
        chunk = array_a[start:start + block]
        gaps = chunk[:, None, :] - array_b[None, :, :]
        out[start:start + block] = np.sqrt(np.min(np.sum(np.square(gaps), axis=2),
                                                  axis=1))
    return out


# the two directed hausdorff distances between two decision sets, and the symmetric one
def compute_hausdorff(set_a, set_b):
    array_a, array_b = require_decision_sets(set_a, set_b)
    a_to_b = float(np.max(nearest_distances(array_a, array_b)))
    b_to_a = float(np.max(nearest_distances(array_b, array_a)))
    return Hausdorff(a_to_b=a_to_b, b_to_a=b_to_a, symmetric=max(a_to_b, b_to_a))


# the fraction of set_a lying within delta of some point of set_b
def compute_coverage(set_a, set_b, delta):
    # asymmetric, and reported one direction per call: the fraction of set_a that
    # a decision maker holding set_b already has to within delta is not the
    # fraction of set_b that a holder of set_a has. CONTEXT.md section 10 d2 says
    # both ways, so both ways is two calls and never one number.
    array_a, array_b = require_decision_sets(set_a, set_b)
    distance = require_delta(delta)
    return float(np.count_nonzero(nearest_distances(array_a, array_b) <= distance)
                 / len(array_a))


# the delta-neighbourhood intersection of two decision sets over their union
def compute_overlap(set_a, set_b, delta):
    # a point of set_a lies in set_a's own delta-neighbourhood always, so it lies
    # in the intersection of the two neighbourhoods exactly when it is within
    # delta of set_b, and the same the other way. the intersection is therefore
    # the two covered counts and the union is the two cardinalities. symmetric,
    # one at identical sets, zero at sets further apart than delta, and equal to
    # 2 |A| / (|A| + |B|) when A is contained in B, which is the number the two
    # check pairs of phi_pairs are pinned to at delta = 0 and not a measurement.
    array_a, array_b = require_decision_sets(set_a, set_b)
    distance = require_delta(delta)
    covered = (np.count_nonzero(nearest_distances(array_a, array_b) <= distance)
               + np.count_nonzero(nearest_distances(array_b, array_a) <= distance))
    return float(covered / (len(array_a) + len(array_b)))


# the fraction of set_a that survives non-dominated filtering under a second phi
def cross_evaluate(set_a, phi_name, problem, params):
    # what a decision maker committed to phi_name would keep of a set recovered
    # under another order, CONTEXT.md section 5 step 5. it needs no common scale
    # between the two image spaces, which is why it is comparable across phi.
    # the filter is the project's one dominance relation and phi is applied
    # through the route the problem's representation names; neither is
    # reimplemented, and the whole set goes through the filter once. it is
    # non-dominance within set_a under phi_name and not membership of the whole
    # sample's front, so it is not recoverable by intersecting index sets.
    require_phi(phi_name)
    array = require_decision_set(set_a, "set_a")
    if array.shape[1] != problem.n_vars:
        raise ValueError(
            "set_a has {} decision variables and {} has {}"
            .format(array.shape[1], problem.name, problem.n_vars))
    image = phi_image(problem, problem.evaluate(array, params), phi_registry[phi_name])
    return float(len(non_dominated_indices(image)) / len(array))


# the label a pair of phi may be read under, check or finding
def pair_status(phi_a, phi_b):
    # r-06 and CONTEXT.md section 10 e3. on the two pairs involving phi_ls a
    # containment fixes one direction of coverage and of overlap before anything
    # runs, so what is measured there is in part a theorem and is reported as a
    # check on the containment with it named. the phi_lu against phi_cw pair is
    # nested in neither direction and is the only one carrying the signal.
    return check_status if (phi_a, phi_b) in containments else finding_status


# what a table must print beside the pair, naming the containment and the artefact
def pair_note(phi_a, phi_b):
    if (phi_a, phi_b) not in containments:
        return ("nested in neither direction, so both directions are measured; "
                "this is the pair CONTEXT.md section 10 e3 takes the headline "
                "number from")
    inner, outer = containments[(phi_a, phi_b)]
    return ("check on r-06 and not a finding: ND_{} sits inside ND_{} exactly and "
            "for every problem, docs/a_close_containment.md, so coverage of {} in "
            "{} and one direction of the overlap are fixed before this runs. the "
            "containment is exact in real arithmetic and fails by rounding in "
            "doubles, one point of 1565 measured, r-11, so a nonzero violation "
            "count is arithmetic and never a result about phi. it stands on s-11; "
            "if the supervisors refute the criterion this pair is reported like "
            "the other and no result moves".format(inner, outer, inner, outer))


# how many members of the contained set are missing from the containing one
def containment_violations(sample, phi_a, phi_b):
    # the r-11 artefact, counted rather than described, and it is a count of
    # rounding. it is None where no containment applies, so a table cannot print
    # a zero for the phi_lu against phi_cw pair and read it as agreement.
    if (phi_a, phi_b) not in containments:
        return None
    inner, outer = containments[(phi_a, phi_b)]
    return int(len(set(sample.indices[inner].tolist())
                   - set(sample.indices[outer].tolist())))


# every pairwise decision-space metric of two phi over one filtered sample
def measure_one_pair(sample, problem, params, phi_a, phi_b, delta):
    set_a = sample.decision_vectors[sample.indices[phi_a]]
    set_b = sample.decision_vectors[sample.indices[phi_b]]
    return PhiPair(
        phi_a=phi_a, phi_b=phi_b,
        status=pair_status(phi_a, phi_b),
        containment=containments.get((phi_a, phi_b)),
        containment_violations=containment_violations(sample, phi_a, phi_b),
        note=pair_note(phi_a, phi_b),
        n_a=len(set_a), n_b=len(set_b),
        hausdorff=compute_hausdorff(set_a, set_b),
        coverage_a_in_b=compute_coverage(set_a, set_b, delta),
        coverage_b_in_a=compute_coverage(set_b, set_a, delta),
        overlap=compute_overlap(set_a, set_b, delta),
        cross_a_under_b=cross_evaluate(set_a, phi_b, problem, params),
        cross_b_under_a=cross_evaluate(set_b, phi_a, problem, params))


# the pairwise decision-space metrics of all three phi over one random-search sample
def compare_phi_on_one_sample(problem, params, n_evals, seed, delta):
    # this and not the solver runs, and the reason is c1's isolation. the sample
    # is a pure function of the box, the budget and the seed, so the three sets
    # below differ only through the order; in nsga-ii and mopso phi drives the
    # search as well as the ordering, and c3-f measured the consequence, that at
    # matched cardinality nsga-ii's coverage of the derived region is
    # phi-conditional and random search's is not,
    # docs/c3_validation.md section 5.5. a difference measured on nsga-ii output
    # is therefore confounded with nsga-ii's own behaviour under each order and is
    # not evidence about the order. CONTEXT.md section 10 e3, c-close's amendment.
    require_delta(delta)
    sample = filter_one_sample_under_every_phi(problem, params, n_evals, seed)
    sizes = {name: int(len(indices)) for name, indices in sample.indices.items()}
    pairs = tuple(measure_one_pair(sample, problem, params, phi_a, phi_b, delta)
                  for phi_a, phi_b in phi_pairs)
    return PhiComparison(problem=problem.name, seed=seed, n_evals=int(n_evals),
                         delta=float(delta), sample=sample, sizes=sizes, pairs=pairs)
