# f2's problem and f2's answer, encoded. I-BK1 as [16] states it in appendix A,
# and the three phi-efficient sets docs/part2/f2_ibk1_derivation.md derives for
# it. this module derives nothing of its own: every formula below names the
# section of f2 it is copied from, and no condition is strengthened, weakened or
# extended on the way in. that is src/reference_fronts.py's discipline for p1,
# applied here to a problem the project did not construct.
#
# why one module and not two. on tier 0 the split is src/problems_tier0.py for
# the evaluation and src/reference_fronts.py for the derived sets, and it is
# there because b2 was a separate subpart with a weight simplex to sample and a
# rational map to push it through. here the problem and its derived sets arrive
# together from one paper-and-pencil session and each derived set is one pair of
# polynomial inequalities, so the second module would hold thirty lines. the
# calling convention is not restated: Problem and decision_columns are imported
# from src/problems_tier0.py, so a4, a5 and this module are one interface and not
# three, and the five names on the record, the meaning of representation, the
# no-round-trip rule and the reason n_obj is m and never 2m are all documented at
# the head of that module.
#
# no uncertainty is added and no width function is written. I-BK1's imprecision
# is in its published coefficients, docs/plan_after_meeting.md section a2, and
# that is the whole point of part 2: on p1 and on the tier 1 benchmarks the
# project chose the width, and here it chose nothing. the check that the choice
# was not smuggled back in is f2 section 0, which finds no objective of any of
# [16]'s five gate-passing candidates with proportional centre and half-width
# coefficient vectors, so the width-centre independence part1_closing section 6.1
# needs is the paper's and not a design of ours.
#
# the representation is "endpoints", and that is the paper's own form. [16] writes
# each objective as (+)_j [a_ij, b_ij] (.) h_ij(x) with (.) Moore's product,
# definition 2.1(iii) printed page 3; every h_ij of I-BK1 is a square and hence
# non-negative on the whole box, so (.) does not interchange the boundary
# functions anywhere, [16]'s own condition of printed page 27 and
# docs/part2/lit_review.md section 1.7, and
#     G_i(x) = [ sum_j a_ij h_ij(x),  sum_j b_ij h_ij(x) ].
# the two endpoint functions are therefore what the published coefficients
# compute and the centre and half-width are what would be derived from them. per
# d-02 this module returns the endpoints and builds no centre and no radius, and
# nothing downstream rebuilds one: phi is applied once to the declared
# representation through phi_registry[name].of_endpoints.
#
# what is deliberately not here. nothing of [16] beyond the problem statement is
# implemented: not the Newton method, not the gH-gradients, not definition 2.18's
# Pareto critical set and not proposition 2.1, which f2 section 4.3 shows is false
# as printed with this very problem as the counterexample, a-11. and **Table 1's
# x* is not a fixture**: f2 section 4.2 shows it lies outside all three derived
# sets and is not a Pareto optimal point of I-BK1 in [16]'s own definition 2.17,
# so it is encoded in tests/test_problems_native.py as a point that must be
# outside and nowhere as a point a front should contain. what f2 section 7 hands
# this module as the implementation check is the other checkpoint, equation (25)'s
# published curve, which must lie inside all three regions along its whole length.
#
# f1's criterion 3 is not discharged here by a1's diagnostic. CONTEXT.md section
# 10 f2 asks for the separation check on the union bounding box of the three
# efficient sets; docs/part2/lit_review.md section 7.2 reversed the order so that
# the derivation runs first, and f2 answered criterion 3 exactly from the closed
# forms, f2 section 3. r-09 is discharged for I-BK1 by derivation and no
# sample-based separation check is owed on this problem.
#
# [16] is papers/Newton Method for Multiobjective Optimization Problems of
# Interval-Valued Maps.pdf, and I-BK1 is its problem 1 of appendix A, printed
# page 27, transcribed in docs/part2/lit_review.md section 1.8 and re-read from
# the paper in f2 section 1.1.
# [1] is papers/new_preference_order_relationships_paper.txt, costa,
# osuna-gomez and chalco-cano, fuzzy sets and systems 477 (2024) 108812.

import numpy as np

from phi_transforms import phi_registry
from problems_tier0 import Problem, decision_columns
from random_search import phi_image
from reference_fronts import (farthest_point_indices, farthest_point_mode,
                              oversampling_factor)

# I-BK1's dimensions, [16] printed page 27: n = 2, m = 2, so the transformed real
# problem has 2m = 4 columns.
ibk1_n_vars = 2
ibk1_n_obj = 2

# the decision box, [16] printed page 27: lb^T = (-10, -10), ub^T = (10, 10).
ibk1_lower = np.array([-10.0, -10.0])
ibk1_upper = np.array([10.0, 10.0])

# the shift the second objective's basis functions carry, [16] printed page 27:
# both terms of G_2 are squares about 5. it is the problem's own constant and it
# is named because it is also the corner (5, 5) that every derived set is pinned
# at, f2 section 2.4.
ibk1_shift = 5.0

# the four coefficient intervals, [16] problem 1 of appendix A, printed page 27,
# transcribed in docs/part2/lit_review.md section 1.8 and re-read in f2 section
# 1.1:
#     G_1(x_1, x_2) := [0.1, 0.2] (.) x_1^2      (+)  [0.1, 0.3] (.) x_2^2
#     G_2(x_1, x_2) := [0.1, 0.3] (.) (x_1-5)^2  (+)  [0.1, 0.5] (.) (x_2-5)^2
# one tuple per objective, one interval per basis function, in the paper's order,
# and the printed decimals rather than f2's exact rationals: the coefficients are
# the paper's and the module states them as the paper prints them.
ibk1_coefficients = (((0.1, 0.2), (0.1, 0.3)), ((0.1, 0.3), (0.1, 0.5)))

# the representation, per d-02 and the module comment above
ibk1_representation = "endpoints"


# the two basis functions of one objective, both squares and both non-negative
def basis_functions(objective, x_1, x_2):
    # objective 1 is supported at the origin and objective 2 at (5, 5), [16]
    # printed page 27. the non-negativity is what makes the endpoint reading of
    # (.) the paper's own, section 1.7 of docs/part2/lit_review.md.
    if objective == 0:
        return np.square(x_1), np.square(x_2)
    return np.square(x_1 - ibk1_shift), np.square(x_2 - ibk1_shift)


# one objective's interval as its two endpoint functions, over the population
def objective_endpoints(objective, x_1, x_2):
    first, second = basis_functions(objective, x_1, x_2)
    (lower_1, upper_1), (lower_2, upper_2) = ibk1_coefficients[objective]
    return (lower_1 * first + lower_2 * second, upper_1 * first + upper_2 * second)


# I-BK1, problem 1 of [16] appendix A, as two interval objectives
def evaluate_ibk1(x, params=None):
    # params is accepted and ignored. I-BK1 has no imprecision parameter, its
    # coefficients being the paper's and fixed, and the argument is kept so that
    # the calling convention is one convention and not two; p0 does the same.
    x_1, x_2 = decision_columns(x, ibk1_n_vars)
    return tuple(objective_endpoints(objective, x_1, x_2)
                 for objective in range(ibk1_n_obj))


# I-BK1's decision box, the one [16] states, holding all three derived sets inside it
def bounds_ibk1():
    # f2 section 2.5: all three derived sets lie in [0, 5]^2, so every point of
    # every one of them is interior to this box with a margin of at least 5 on
    # every side. that margin is a property of the published problem and not,
    # as p1's was, of a choice the project made.
    return np.array(ibk1_lower), np.array(ibk1_upper)


ibk1 = Problem(name="ibk1", n_vars=ibk1_n_vars, n_obj=ibk1_n_obj,
               representation=ibk1_representation, evaluate=evaluate_ibk1,
               bounds=bounds_ibk1)

# name to problem, the convention src/problems_tier0.py and
# src/problems_tier1.py use, so experiment code loops rather than naming.
problem_registry = {"ibk1": ibk1}

# f2 section 2.4's three derived sets, as the wedges in nu they are. with
#     U := x_1 / (5 - x_1),  V := x_2 / (5 - x_2),  nu := V / U
# every derived set is the band of a closed interval of nu, and cleared of
# denominators the band [p/q, r/q] is
#     p x_1 (5 - x_2)  <=  q x_2 (5 - x_1)  <=  r x_1 (5 - x_2)
# on [0, 5]^2. the entries are (p, r, q) and they are integers, so membership is
# decided by exact integer-coefficient inequalities and carries no tolerance
# anywhere. f2 section 2.4 prints the three in exactly this cleared form, which
# is what covers the two corners (0, 0) and (5, 5) without a case split: both
# sides vanish there and every band holds.
#     phi_lu   nu in [2/3, 5/3]      phi_ls   nu in [1/2, 2]
#     phi_cw   nu in [3/4, 3/2]
derived_bands = {"lu": (2, 5, 3), "ls": (1, 4, 2), "cw": (3, 6, 4)}

# the two sampling modes, and the mode has no default for r-13's reason. the
# region is sampled through a parametrisation, (nu, x_1) below, and
# docs/part1/b2b_reference_density.md measured that the density a parametrisation
# puts on the front biases igd, which averages over reference points: two fronts
# differing only in where they place their points are ranked in opposite orders
# in 31 of 32 swapped-allocation pairs there. so the caller states the mode and
# its value belongs in every table beside the seed and the point count.
# parametrisation is the draw itself; farthest_point is b2-b's correction, the
# same draw at oversampling_factor times the size, subsampled by greedy
# farthest-point selection in objective space. the corrected mode's name is
# imported from src/reference_fronts.py rather than spelled again, so that a
# sampling_mode column reading "farthest_point" names the same correction in e1's
# tables and in f3's.
parametrisation_mode = "parametrisation"
sampling_modes = (parametrisation_mode, farthest_point_mode)

# the seed of the region draw, the project's date convention for a fixed sample
# seed, as src/reference_fronts.py's weight_sample_seed is.
region_sample_seed = 20260905


# raises unless f2 derived a region for this phi, which is all three of them
def require_phi(phi_name):
    if phi_name not in derived_bands:
        raise ValueError(
            "unknown phi {!r}; docs/part2/f2_ibk1_derivation.md section 2.4 "
            "derives a region for {} and this module encodes those and nothing "
            "else".format(phi_name, sorted(derived_bands)))


# raises unless the caller stated one of the two sampling modes
def require_sampling_mode(sampling_mode):
    if sampling_mode not in sampling_modes:
        raise ValueError(
            "sampling_mode must be stated as one of {}; got {!r}. the two modes "
            "give reference fronts of different density in objective space and "
            "igd is an average over reference points, r-13 and "
            "docs/part1/b2b_reference_density.md, so this module will not choose "
            "for the caller.".format(list(sampling_modes), sampling_mode))


# the two ends of one phi's band of nu, f2 section 2.4
def band_ends(phi_name):
    require_phi(phi_name)
    lower, upper, denominator = derived_bands[phi_name]
    return lower / float(denominator), upper / float(denominator)


# whether each point lies in one phi's derived set, by f2 section 2.4's inequalities
def in_region(phi_name, x):
    # the cleared form, so the comparison is between products of the point's own
    # coordinates and small integers and no division is taken. the box condition
    # is f2 section 2.4's [0, 5]^2 and it is part of the description and not a
    # clipping: f2 section 2.5 shows every point outside it is dominated by its
    # projection onto it under every phi.
    require_phi(phi_name)
    lower, upper, denominator = derived_bands[phi_name]
    x_1, x_2 = decision_columns(x, ibk1_n_vars)
    left = x_1 * (ibk1_shift - x_2)
    right = x_2 * (ibk1_shift - x_1)
    inside = ((0.0 <= x_1) & (x_1 <= ibk1_shift)
              & (0.0 <= x_2) & (x_2 <= ibk1_shift))
    return (inside & (lower * left <= denominator * right)
            & (denominator * right <= upper * left))


# nu at a stated point, the coordinate f2 section 2.4 states every set in
def nu_at(x):
    # undefined at the two corners, where both sides vanish, which is why
    # in_region uses the cleared form and this function is for reporting a stated
    # interior point against the bands and for nothing else.
    x_1, x_2 = decision_columns(x, ibk1_n_vars)
    return x_2 * (ibk1_shift - x_1) / (x_1 * (ibk1_shift - x_2))


# the curve of constant nu through (0, 0) and (5, 5), f2 section 2.4
def curve_x_2(nu, x_1):
    # x_2 = 5 c x_1 / (5 + (c - 1) x_1) for c > 0, the hyperbola f2 section 2.4
    # gives; c = 1 is the diagonal. the denominator is bounded below by
    # 5 + (min c - 1) * 5, which is 2.5 at the smallest band end any phi has,
    # so it does not vanish anywhere on [0, 5].
    return (ibk1_shift * nu * x_1) / (ibk1_shift + (nu - 1.0) * x_1)


# a draw of the parametrisation of one phi's wedge, as (nu, x_1)
def parametrisation_sample(phi_name, n_points, seed):
    # f2 section 2.4: the set is exactly {nu in the band} times {U in [0, inf]},
    # and U = x_1 / (5 - x_1) is an increasing bijection of [0, 5) onto [0, inf),
    # so sweeping nu across the band and x_1 along [0, 5] sweeps the whole wedge
    # and reaches both corners. the draw is uniform in those two coordinates and
    # that is a parametrisation like any other: its density in objective space is
    # its own and not the front's, which is what the mode above exists to correct.
    lower, upper = band_ends(phi_name)
    generator = np.random.default_rng(seed)
    return (generator.uniform(lower, upper, size=int(n_points)),
            generator.uniform(0.0, ibk1_shift, size=int(n_points)))


# the decision points of a parametrisation draw, one row per (nu, x_1) pair
def region_points(nu, x_1):
    return np.column_stack([np.asarray(x_1, dtype=float),
                            curve_x_2(np.asarray(nu, dtype=float),
                                      np.asarray(x_1, dtype=float))])


# the objective-space image the farthest-point selection is made in
def selection_image(phi_name, points):
    # the selection is in objective space and not in decision space because igd
    # is computed on the front and it is the front's density that biases it,
    # r-13. I-BK1 carries no imprecision parameter, so unlike p1 there is no
    # question of which parameters the image is taken at.
    return phi_image(ibk1, ibk1.evaluate(points, None), phi_registry[phi_name])


# one phi's derived set, sampled, with the parametrisation that produced each point
def efficient_set(phi_name, n_points, sampling_mode, seed=region_sample_seed):
    require_phi(phi_name)
    require_sampling_mode(sampling_mode)
    if int(n_points) < 1:
        raise ValueError("n_points must be at least 1; got {}".format(n_points))
    if sampling_mode == parametrisation_mode:
        nu, x_1 = parametrisation_sample(phi_name, int(n_points), seed)
        return region_points(nu, x_1), np.column_stack([nu, x_1])
    nu, x_1 = parametrisation_sample(phi_name, int(n_points) * oversampling_factor,
                                     seed)
    points = region_points(nu, x_1)
    kept = farthest_point_indices(selection_image(phi_name, points), int(n_points))
    return points[kept], np.column_stack([nu, x_1])[kept]


# the derived set pushed through phi, as the (k, 2m) array the solvers produce
def reference_front(phi_name, n_points, sampling_mode, seed=region_sample_seed):
    points, _ = efficient_set(phi_name, int(n_points), sampling_mode, seed)
    return selection_image(phi_name, points)
