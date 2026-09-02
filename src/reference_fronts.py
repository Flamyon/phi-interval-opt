# b2: the phi-efficient sets of p1 and the reference fronts they give. this module
# encodes docs/b1_phi_efficient_sets.md and derives nothing of its own: every
# formula below names the section of b1 it is copied from, and no condition is
# strengthened, weakened or extended on the way in.
#
# what is encoded, and what deliberately is not. b1 section 2.1 turns condition
# (15) of [1] into the diagonal linear system
#     d_1(w) x_1 = rho_1(w),   d_2(w) x_2 = rho_2(w)
# with all four forms linear in the four weights, and b1 section 2.2 solves it in
# closed form as the rational map w -> x(w). this module samples the weight
# simplex and pushes the sample through that map. it does not encode the
# algebraic description of the region that b1 section 2.4 gives: those
# inequalities are the derivation's output, not its content, and sampling inside
# them would restate b1's boundary instead of its derivation. the inequalities
# appear only in tests/test_reference_fronts.py, as the check that the sampled
# points land where b1 says they do.
#
# the weight index convention is b1 section 0's, taken from [1] lines 715-723, and
# inverting it inverts the problem: w_1 sits on Lambda_1^T f, w_2 on B_1^T f, w_3
# on Lambda_2^T f and w_4 on B_2^T f. that is also the column order of the
# transformed real problem, so the 2m columns a solver produces are
# (Lambda_1^T f, B_1^T f, Lambda_2^T f, B_2^T f) and reference_front returns
# exactly those, in that order. a transposition here would corrupt every igd in
# the project, so the order is asserted explicitly in the tests and not assumed.
#
# p1 only. b1 section 7.4 finds that p0 is a smoke test and not a fixture, so
# efficient_set and reference_front both raise for it rather than returning
# something that would pass for a front.
#
# the singular segments, and why the caller has to decide. b1 section 2.3 finds
# two singular weight rays for phi_ls and for phi_cw and none for phi_lu, and b1
# section 2.6 records the one thing the derivation does not close: on those rays
# the published conditions give weak optimality and no optimality verdict either
# way, while a4's grid says part of each segment is non-dominated. that gap is
# unresolved and this module does not resolve it. include_singular_segments has no
# default: the caller states which set it wants and the value it stated belongs in
# every table d1 and e1 write, next to the seed and the point count, because the
# two reference fronts are two different objects and a metric computed against one
# is not comparable with a metric computed against the other.
#
# the sampling mode, and why the caller has to state that one too. r-13: the
# weight sample is a dirichlet draw on the simplex and w -> x(w) is a rational
# map, so the density of the sample in objective space is the parametrisation's
# and not the front's, while igd is an average over reference points and so
# weights a densely sampled region of the front more heavily than a sparse one.
# the correction is to oversample through the same map by oversampling_factor and
# keep n_points of that draw by greedy farthest-point selection in objective
# space. it changes which of the sampled points survive and nothing else: every
# kept point is still x(w) at a weight this module recorded, and b1 section 2.4's
# inequalities are still nowhere in this file. sampling_mode has no default for
# the reason include_singular_segments has none, and for a measured reason as
# well: docs/b2b_reference_density.md builds fronts that differ only in where they
# place their points, one favouring the densely sampled part of the front and one
# the sparse part, and the two references rank them differently. under every phi
# and both settings of the flag the dirichlet reference asks for 25 points of 200
# more in the half it oversamples than the corrected one does, 31 of the 32
# swapped-allocation pairs under phi_ls and phi_cw are ranked in opposite orders,
# and under phi_lu a pair whose fill distances agree to 0.24 per cent is preferred
# one way by 22 per cent and the other by 3. so the mode is not a refinement, it
# decides comparisons, and its value belongs in every table beside the seed, the
# point count and the flag.
#
# [1] is papers/new_preference_order_relationships_paper.txt, costa,
# osuna-gomez and chalco-cano, fuzzy sets and systems 477 (2024) 108812.

from collections import namedtuple

import numpy as np

from phi_transforms import phi_registry
from problems_tier0 import p1_default_params

# the four linear forms of the diagonal system, b1 section 2.1. each field holds
# the coefficients of w_1, w_2, w_3, w_4 in that order.
StationaritySystem = namedtuple("StationaritySystem", ("d_1", "d_2", "rho_1", "rho_2"))


# packs one phi's four linear forms as arrays, so a weight sample is one matmul
def make_system(d_1, d_2, rho_1, rho_2):
    return StationaritySystem(d_1=np.array(d_1), d_2=np.array(d_2),
                              rho_1=np.array(rho_1), rho_2=np.array(rho_2))


# the system of b1 section 2.1, copied form for form, per phi.
#   phi_lu  d_1 = 2 w_1 + 2 w_2 + (3/2) w_3 + (5/2) w_4
#           d_2 = (3/2) w_1 + (5/2) w_2 + 2 w_3 + 2 w_4
#           rho_1 = 2 w_3 + 2 w_4,  rho_2 = 2 w_1 + 2 w_2 + 2 w_3 + 2 w_4
#   phi_ls  d_1 = 2 w_1 + (3/2) w_3 + w_4,  d_2 = (3/2) w_1 + w_2 + 2 w_3
#           rho_1 = 2 w_3,  rho_2 = 2 w_1 + 2 w_3
#   phi_cw  d_1 = 2 w_1 + 2 w_3 + (1/2) w_4,  d_2 = 2 w_1 + (1/2) w_2 + 2 w_3
#           rho_1 = 2 w_3,  rho_2 = 2 w_1 + 2 w_3
# the coefficients are the hessians and linear parts of b1 section 1.1, which are
# p1's at rho = 1/4 and are constant in x. they do not move with delta, b1 section
# 1.2, which is why derivation_parameters below fixes rho and leaves delta free.
stationarity_systems = {
    "lu": make_system((2.0, 2.0, 1.5, 2.5), (1.5, 2.5, 2.0, 2.0),
                      (0.0, 0.0, 2.0, 2.0), (2.0, 2.0, 2.0, 2.0)),
    "ls": make_system((2.0, 0.0, 1.5, 1.0), (1.5, 1.0, 2.0, 0.0),
                      (0.0, 0.0, 2.0, 0.0), (2.0, 0.0, 2.0, 0.0)),
    "cw": make_system((2.0, 0.0, 2.0, 0.5), (2.0, 0.5, 2.0, 0.0),
                      (0.0, 0.0, 2.0, 0.0), (2.0, 0.0, 2.0, 0.0)),
}

# the singular ray of b1 section 2.3 and the segment of b1 section 2.6 it leaves
# undecided, per phi. b1 section 2.3 finds two rays for phi_ls and phi_cw, all
# mass on w_2 alone or on w_4 alone, and none at all for phi_lu, no coefficient of
# whose d_1 and d_2 vanishes. the w_4 ray gives the solution line x_1 = 0, every
# point of which with x_2 in (0, 4/3] the regular weights already reach, so it
# adds nothing; the w_2 ray gives the line x_2 = 0, whose part with x_1 > 0 is
# exactly the closure of the derived set minus the derived set, b1 section 2.6.
# the second entry is the largest x_1 the derived region reaches, b1 section 2.4,
# and it is where b1 section 2.6 puts the end of the undecided segment.
singular_segments = {
    "lu": None,
    "ls": (np.array([0.0, 1.0, 0.0, 0.0]), 4.0 / 3.0),
    "cw": (np.array([0.0, 1.0, 0.0, 0.0]), 1.0),
}

# rho = 1/4 is baked into every coefficient of stationarity_systems through the
# hessians of b1 section 1.1, so the derivation is about that rho and no other.
derivation_rho = 0.25

# the weight sample is a dirichlet draw over the simplex, and the concentration is
# below one on purpose. b1 section 2.4 reaches every extreme value of every
# derived region, 4/5, 1 and 4/3, only at weights with zero components, so a
# sample of the open simplex alone approaches the extremes and never arrives.
# measured against a fine lattice of b1 section 2.4's regions at 4000 points, the
# worst gap in objective space is 0.034, 0.165 and 0.138 for phi_lu, phi_ls and
# phi_cw at concentration 0.3, against 0.274, 1.191 and 0.868 at concentration 1.
weight_concentration = 0.3
weight_sample_seed = 20260901

# the two sampling modes. dirichlet is the draw described just above, kept as it
# was and still the mode every measurement recorded before b2-b was made in;
# farthest_point is the r-13 correction, the same draw at oversampling_factor
# times the size, subsampled by farthest-point selection in objective space.
dirichlet_mode = "dirichlet"
farthest_point_mode = "farthest_point"
sampling_modes = (dirichlet_mode, farthest_point_mode)

# how much larger the draw the farthest-point selection chooses from is. it is
# measured and not chosen by taste, docs/b2b_reference_density.md section 3. at
# 1000 kept points the coefficient of variation of the nearest-neighbour distance
# within the front falls, for phi_lu, phi_ls and phi_cw, from 0.74, 1.13 and 1.42
# at factor 1, which is the dirichlet draw itself, to 0.15, 0.23 and 0.34 at
# factor 5, 0.12, 0.16 and 0.20 at factor 10, 0.12, 0.13 and 0.14 at factor 20 and
# 0.11, 0.11 and 0.12 at factor 40. the cost of the selection is linear in the
# factor, 0.56 s at factor 10 against 2.51 s at factor 40 for those 1000 points,
# and ten takes at least 94 per cent of the reduction factor 40 reaches at a
# quarter of its cost. the factor is a constant and not an argument because it is
# not a reporting parameter: unlike the mode and the flag it does not name a
# different object, it converges to the same evenly spaced front from below, and a
# table that carried it would invite comparing two fronts that differ only in how
# well the same selection was resolved.
oversampling_factor = 10


# raises unless the problem is the one b1 derived a fixture for, which is p1 alone
def require_p1(problem):
    if problem.name != "p1":
        raise ValueError(
            "no reference front exists for {}; b2 is for p1 only. "
            "docs/b1_phi_efficient_sets.md section 7.4 records why p0 is a smoke "
            "test and not a fixture: under phi_lu and phi_ls its optimal set is "
            "the whole decision box, so an igd against it measures nothing about "
            "finding an efficient set, and under phi_cw it is the single point "
            "x = 0, which is the published anchor and not a front. p0's own "
            "hypotheses fail as well, example 3.9's differentiability at x = 0 "
            "under all three phi and theorem 3.3's convexity under phi_lu and "
            "phi_ls. what p0 supports is the c3 gate's check that a solver finds "
            "x = 0.".format(problem.name)
        )


# raises unless phi is one of the three b1 derived the system for
def require_phi(phi_name):
    if phi_name not in stationarity_systems:
        raise ValueError(
            "unknown phi {!r}; docs/b1_phi_efficient_sets.md section 2.1 derives "
            "the system for {} only".format(phi_name, sorted(stationarity_systems))
        )


# raises unless the caller stated one of the two sampling modes
def require_sampling_mode(sampling_mode):
    if sampling_mode not in sampling_modes:
        raise ValueError(
            "sampling_mode must be stated as one of {}; got {!r}. the two modes "
            "give reference fronts of different density in objective space and "
            "igd is an average over reference points, r-13, so this module will "
            "not choose for the caller.".format(list(sampling_modes), sampling_mode)
        )


# p1's parameters for a reference front, fixing rho and leaving delta free
def derivation_parameters(params):
    values = dict(p1_default_params)
    if params is not None:
        values.update(params)
    if float(values["rho"]) != derivation_rho:
        raise ValueError(
            "the derived sets are p1's at rho = {}, docs/b1_phi_efficient_sets.md "
            "section 1.1, and every coefficient of the system is that rho's; got "
            "rho = {}. delta is free, b1 section 1.2, entering every image "
            "coordinate as an additive constant.".format(derivation_rho, values["rho"])
        )
    return values


# a weight sample of the simplex with every singular weight dropped, b1 section 2.3
def simplex_weights(phi_name, n_points, seed):
    if n_points < 1:
        return np.zeros((0, 4))
    system = stationarity_systems[phi_name]
    generator = np.random.default_rng(seed)
    kept = []
    total = 0
    while total < n_points:
        block = generator.dirichlet(np.full(4, weight_concentration), size=n_points)
        regular = np.logical_and(block @ system.d_1 > 0.0, block @ system.d_2 > 0.0)
        kept.append(block[regular])
        total += int(np.count_nonzero(regular))
    return np.concatenate(kept)[:n_points]


# the map w -> x(w) of b1 section 2.2, the unique solution of the diagonal system
def stationary_points(phi_name, weights):
    system = stationarity_systems[phi_name]
    w = np.asarray(weights, dtype=float)
    return np.column_stack([(w @ system.rho_1) / (w @ system.d_1),
                            (w @ system.rho_2) / (w @ system.d_2)])


# the objective-space image the farthest-point selection is made in, at the
# derivation's own parameters. the selection is in objective space and not in
# decision space because igd is computed on the front and it is the front's
# density that biases it, r-13. the parameters are not the caller's and need not
# be: rho is fixed at derivation_rho for every reference front, and delta enters
# every image coordinate as an additive constant, b1 section 1.2, so a different
# delta translates the whole image and leaves every distance inside it unchanged.
# the same rows are therefore selected at every delta the caller may pass.
def selection_image(problem, phi_name, points):
    return transformed_image(problem, points, phi_registry[phi_name],
                             derivation_parameters(None))


# greedy farthest-point selection: the point farthest from the ones already kept,
# repeatedly, in the euclidean distance of the space the image lives in. the first
# point is the one farthest from the image's centroid, which is on the boundary of
# the front and is a function of the draw alone, so the whole selection is
# deterministic and carries no second seed. the indices come back in the draw's own
# order, so the kept front is a subsequence of the oversample and not a reordering.
def farthest_point_indices(image, n_keep):
    centre = np.mean(image, axis=0)
    first = int(np.argmax(np.sum((image - centre) ** 2, axis=1)))
    chosen = [first]
    # the squared distance from each candidate to the nearest kept point, updated
    # against the one just kept rather than recomputed against all of them
    nearest = np.sum((image - image[first]) ** 2, axis=1)
    while len(chosen) < n_keep:
        index = int(np.argmax(nearest))
        chosen.append(index)
        nearest = np.minimum(nearest, np.sum((image - image[index]) ** 2, axis=1))
    return np.sort(np.array(chosen, dtype=int))


# the regular part of the sample, in the mode the caller stated. the dirichlet
# mode returns the draw itself; the farthest-point mode draws oversampling_factor
# times as many and keeps n_points of them, the weight that produced each kept
# point travelling with it so the caller still holds x(w) and its w.
def regular_sample(problem, phi_name, n_points, sampling_mode, seed):
    if n_points < 1:
        return np.zeros((0, 2)), np.zeros((0, 4))
    if sampling_mode == dirichlet_mode:
        weights = simplex_weights(phi_name, n_points, seed)
        return stationary_points(phi_name, weights), weights
    weights = simplex_weights(phi_name, n_points * oversampling_factor, seed)
    points = stationary_points(phi_name, weights)
    kept = farthest_point_indices(selection_image(problem, phi_name, points), n_points)
    return points[kept], weights[kept]


# how many of the requested points go on the singular segment, none unless asked
def singular_share(phi_name, n_points, include_singular_segments):
    if not isinstance(include_singular_segments, bool):
        raise ValueError(
            "include_singular_segments must be stated as True or False; got {!r}. "
            "docs/b1_phi_efficient_sets.md section 2.6 leaves the status of those "
            "points undecided, so this module will not choose for the caller."
            .format(include_singular_segments)
        )
    if not include_singular_segments or singular_segments[phi_name] is None:
        return 0
    # the region is two-dimensional and the segment one-dimensional, so matching
    # the linear density of an n-point area sample takes about sqrt(n) points.
    # they come out of n_points rather than on top of it, so the two settings
    # return the same count and a difference between them is content and not size.
    return min(n_points, int(np.ceil(np.sqrt(n_points))))


# the undecided segment of b1 section 2.6, sampled with its singular weight
def singular_segment_points(phi_name, n_points):
    segment = singular_segments[phi_name]
    if segment is None or n_points < 1:
        return np.zeros((0, 2)), np.zeros((0, 4))
    weight, x_1_end = segment
    points = np.column_stack([np.linspace(0.0, x_1_end, n_points), np.zeros(n_points)])
    return points, np.tile(weight, (n_points, 1))


# p1's phi-efficient set under one phi, sampled, with the weight that produced each point
def efficient_set(problem, phi_name, n_points, include_singular_segments,
                  sampling_mode, seed=weight_sample_seed):
    require_p1(problem)
    require_phi(phi_name)
    require_sampling_mode(sampling_mode)
    if int(n_points) < 1:
        raise ValueError("n_points must be at least 1; got {}".format(n_points))
    n_singular = singular_share(phi_name, int(n_points), include_singular_segments)
    # the segment is a linspace on a one-dimensional set, b1 section 2.6, so it is
    # already as evenly spaced as it can be and the mode does not touch it: the
    # correction is to the two-dimensional part, whose density is the weight
    # parametrisation's.
    points, weights = regular_sample(problem, phi_name, int(n_points) - n_singular,
                                     sampling_mode, seed)
    segment_points, segment_weights = singular_segment_points(phi_name, n_singular)
    return (np.concatenate([points, segment_points]),
            np.concatenate([weights, segment_weights]))


# the 2m columns of the transformed real problem, phi applied to each objective.
# the pairing convention of src/problems_tier0.py: the problem names the
# representation its intervals are computed in and the phi record is asked for
# that route by name, so no endpoint is ever rebuilt from a centre and a radius.
def transformed_image(problem, x, record, params):
    route = getattr(record, "of_" + problem.representation)
    columns = []
    for pair in problem.evaluate(x, params):
        first, second = route(*pair)
        columns.append(first)
        columns.append(second)
    return np.stack(columns, axis=-1)


# the efficient set pushed through phi, as the (k, 2m) array the solvers produce
def reference_front(problem, phi_name, n_points, include_singular_segments,
                    sampling_mode, params=None, seed=weight_sample_seed):
    require_p1(problem)
    values = derivation_parameters(params)
    points, _ = efficient_set(problem, phi_name, int(n_points),
                              include_singular_segments, sampling_mode, seed)
    return transformed_image(problem, points, phi_registry[phi_name], values)
