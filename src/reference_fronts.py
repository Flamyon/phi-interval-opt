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
                  seed=weight_sample_seed):
    require_p1(problem)
    require_phi(phi_name)
    if int(n_points) < 1:
        raise ValueError("n_points must be at least 1; got {}".format(n_points))
    n_singular = singular_share(phi_name, int(n_points), include_singular_segments)
    weights = simplex_weights(phi_name, int(n_points) - n_singular, seed)
    points = stationary_points(phi_name, weights)
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
                    params=None, seed=weight_sample_seed):
    require_p1(problem)
    values = derivation_parameters(params)
    points, _ = efficient_set(problem, phi_name, int(n_points),
                              include_singular_segments, seed)
    return transformed_image(problem, points, phi_registry[phi_name], values)
