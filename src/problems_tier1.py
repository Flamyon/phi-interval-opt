# the two tier 1 benchmarks, zdt1 and dtlz2, as interval problems. evaluation
# only. no efficient set is derived here and none is assumed; what the
# phi-efficient sets are is b1's and b2's work.
# the calling convention is a4's and is not restated: this module imports Problem
# and decision_columns from src/problems_tier0.py so that a4 and a5 are one
# interface and not two. the five names on a Problem record, the meaning of
# representation, the no-round-trip rule and the reason n_obj is m and never 2m
# are all documented at the head of that module.
# both problems declare "centre_radius" and neither builds an endpoint anywhere.
# that is CONTEXT.md section 10 a5, and it follows from the construction itself:
# docs/a1_uncertainty_model.md part 4, "the form", writes
#     F_i(x) = [ f_i(x) - r_i(x),  f_i(x) + r_i(x) ]
# so the centre f_i and the half-width r_i are the two functions actually given
# and the endpoint pair is derived from them, never the other way round. phi is
# applied to (f_i, r_i) once, through phi_registry[name].of_centre_radius.
# the published objectives are untouched at every level of imprecision: the
# centres are the f_i of [2] and [3] exactly, so the crisp benchmark is not a
# limit that is approached but the exact eps = 0 member of the family.
#
# sources for the crisp objectives, both read in this session.
# [2] e. zitzler, k. deb and l. thiele, "comparison of multiobjective
#     evolutionary algorithms: empirical results", evolutionary computation
#     8(2) (2000) 173-195, papers/zitzler_deb_thiele_2000_comparison.pdf.
#     zdt1 is its test function T_1, section 4, definition 4, equation (7),
#     printed page 177. note that the formulas of that paper are set in bitmap
#     math fonts and are dropped by text extraction; they were read from the
#     rendered page.
# [3] k. deb, l. thiele, m. laumanns and e. zitzler, "scalable multi-objective
#     optimization test problems", congress on evolutionary computation (cec)
#     2002, ieee, papers/deb_thiele_laumanns_zitzler_2002_scalable.pdf.
#     dtlz2 is its section vii.b, equation (9), pdf page 4.
# [1] papers/new_preference_order_relationships_paper.txt, costa, osuna-gomez
#     and chalco-cano, fuzzy sets and systems 477 (2024) 108812, for the three
#     phi whose second image coordinate the crisp limit is a statement about.
#
# a naming collision worth stating once, because it is the kind of thing that
# produces a silent index error. [2] writes m for the number of decision
# variables and [3] writes M for the number of objectives. this project writes
# n_vars for the first and n_obj, m, for the second, per a4. so [2]'s "m = 30"
# is n_vars = 30 here and its m - 1 = 29 is n_vars - 1, while [3]'s M = 3 is
# n_obj = 3.

import numpy as np

from problems_tier0 import Problem, decision_columns

# the imprecision levels of docs/a1_uncertainty_model.md part 4, "the levels to
# sweep": the crisp baseline plus four positive levels. the four were placed from
# a1's slice sweeps, 0.05 and 0.10 where phi_lu's efficient set is still tight
# and 0.25 and 0.50 where it has opened up, which is the spread CONTEXT.md
# section 10 e3 reports as the level at which the difference appears or vanishes.
epsilon_levels = (0.0, 0.05, 0.10, 0.25, 0.50)

# eps = 0 is a degenerate baseline and is labelled one here so that no table can
# quietly count it as a data point. at eps = 0 every half-width is zero, so the
# second image coordinate of examples 2.3 and 2.4 of [1] is identically zero,
# half of the 2m transformed objectives are constant, and the three phi coincide
# with each other and with the crisp order. docs/a1_uncertainty_model.md part 1
# is the general version of that statement and CONTEXT.md section 10 a5 records
# it. it is the crisp benchmark, and it is not a point in the sensitivity study.
crisp_level = 0.0

# the level used when a caller names none. it is a member of epsilon_levels and
# nothing more: no level is distinguished by a1, which sweeps all five, so every
# experiment names its own eps and this only keeps evaluate(x, None) meaningful.
default_params = {"eps": 0.10}


# reads the imprecision level out of params, falling back to default_params
def imprecision_level(params):
    values = dict(default_params)
    if params is not None:
        values.update(params)
    eps = float(values["eps"])
    # eps < 0 would make r_i negative and F_i not an interval. eps = 0 is
    # admitted and is the crisp baseline above, so the bound is not strict.
    if eps < 0.0:
        raise ValueError("eps must be non-negative; got {}".format(eps))
    return eps


# zdt1's dimensions. n_vars is [2]'s m = 30 and n_obj is m, the two interval
# objectives; the transformed real problem has 2m = 4 objectives and that
# doubling belongs to src/phi_transforms.py.
zdt1_n_vars = 30
zdt1_n_obj = 2

# zdt1's representation, per the head of this module: the centre and half-width
# pair, which is the form docs/a1_uncertainty_model.md part 4 constructs it in.
zdt1_representation = "centre_radius"


# zdt1's centres and half-widths, [2] equation (7) with a1 part 4's half-width
def evaluate_zdt1(x, params=None):
    # centres, [2] definition 4, equation (7), page 177, with f_2 assembled by
    # [2] equation (6) on the same page, f_2(x) = g(x_2,...,x_m) h(f_1, g):
    #     f_1(x_1)          = x_1
    #     g(x_2,...,x_m)    = 1 + 9 . (sum_{i=2}^{m} x_i) / (m - 1)
    #     h(f_1, g)         = 1 - sqrt(f_1 / g)
    # with m = 30 and x_i in [0, 1]. g >= 1 on the box, so f_1 / g is defined
    # everywhere and its square root is real, x_1 being non-negative.
    columns = decision_columns(x, zdt1_n_vars)
    eps = imprecision_level(params)
    # f_1 is x_1 itself. it is copied because decision_columns hands back views
    # into the caller's array, and a returned array that aliases an argument
    # would break the convention that evaluation never writes into its input.
    centre_1 = np.copy(columns[0])
    g = 1.0 + 9.0 * np.sum(np.stack(columns[1:], axis=-1), axis=-1) / (zdt1_n_vars - 1)
    centre_2 = g * (1.0 - np.sqrt(centre_1 / g))
    half_width = zdt1_half_width(columns[-1], eps)
    return ((centre_1, half_width), (centre_2, half_width))


# zdt1's half-width, quadratic in the last decision variable
def zdt1_half_width(x_n, eps):
    # docs/a1_uncertainty_model.md part 4, "the form":
    #     r_1(x) = r_2(x) = eps * ( (x_n - 1/2)^2 + 1/20 )
    # one function of x_n = x_30 for both objectives, and the same array is
    # returned for both, the two half-widths being one function and not two.
    # why quadratic here and linear in dtlz2, which is a1 part 4's reason and not
    # an inconsistency. [2]'s g is linear in x_n with slope 9/(n_vars - 1) and
    # its optimum in x_n sits on the face x_n = 0, so a half-width linear in x_n
    # is either aligned with g, which makes phi_cw reproduce the crisp order, or
    # opposed to it, which hands every phi the whole slice. a1 part 4 measured
    # the linear form and prints its table: phi_lu and phi_ls identical at every
    # level, phi_cw the crisp order at every level, and all of them saturating at
    # the whole slice above eps = 0.2. a quadratic half-width has its optimum at
    # the interior point x_n = 1/2, different from g's, and the trade-off then
    # resolves in the interior.
    # the + 1/20 keeps the half-width strictly positive at x_n = 1/2, so no
    # interval degenerates there. unlike p1's delta it is not a dyadic rational
    # and does not need to be: a4-b's dyadic argument is about the endpoint round
    # trip, and this module performs none.
    # at eps = 0 this is 0.0 times a finite non-negative number, which is exactly
    # 0.0 in ieee arithmetic. the crisp half-width is a product and never a
    # difference, so it is exactly zero and not a cancellation residue.
    return eps * (np.square(x_n - 0.5) + 0.05)


# zdt1's decision box, the unit cube of [2] equation (7)
def bounds_zdt1():
    # [2] definition 4, equation (7), page 177: "where m = 30, and x_i in [0,1]".
    return np.zeros(zdt1_n_vars), np.ones(zdt1_n_vars)


# dtlz2's dimensions. n_obj is [3]'s M = 3 and n_vars is [3]'s n = M + k - 1
# with k = |x_M| = 10, the value [3] section vii.b states for this problem;
# [3] section vii.a states n = M + k - 1. the transformed real problem has
# 2m = 6 objectives and that doubling belongs to src/phi_transforms.py.
dtlz2_n_vars = 12
dtlz2_n_obj = 3

# dtlz2's representation, the same centre and half-width pair as zdt1's
dtlz2_representation = "centre_radius"


# dtlz2's centres and half-widths, [3] equation (9) with a1 part 4's half-width
def evaluate_dtlz2(x, params=None):
    # centres, [3] section vii.b, equation (9), pdf page 4, written out at M = 3,
    # where the product of cosines has one factor and x_{M-1} is x_2:
    #     f_1(x) = (1 + g(x_M)) cos(x_1 pi/2) cos(x_2 pi/2)
    #     f_2(x) = (1 + g(x_M)) cos(x_1 pi/2) sin(x_2 pi/2)
    #     f_3(x) = (1 + g(x_M)) sin(x_1 pi/2)
    #     g(x_M) = sum_{x_i in x_M} (x_i - 0.5)^2,  0 <= x_i <= 1
    # the sine of the last objective is a sine of x_1 and not of x_2, and the
    # sine of f_2 is a sine of x_2 and not of x_1. that is what the paper prints,
    # f_M carrying sin(x_1 pi/2) and f_2 carrying sin(x_{M-1} pi/2), and it is
    # checked by the sphere identity at non-uniform x in the tests, since a
    # decision vector with x_1 = x_2 satisfies the identity under either reading.
    columns = decision_columns(x, dtlz2_n_vars)
    eps = imprecision_level(params)
    # x_M is the tail x_{M}, ..., x_n, that is x_3 to x_12, which is k = 10
    # variables, [3] section vii.b.
    tail = np.stack(columns[dtlz2_n_obj - 1:], axis=-1)
    scale = 1.0 + np.sum(np.square(tail - 0.5), axis=-1)
    angle_1, angle_2 = columns[0] * (0.5 * np.pi), columns[1] * (0.5 * np.pi)
    centre_1 = scale * np.cos(angle_1) * np.cos(angle_2)
    centre_2 = scale * np.cos(angle_1) * np.sin(angle_2)
    centre_3 = scale * np.sin(angle_1)
    half_width = dtlz2_half_width(columns[-1], eps)
    return ((centre_1, half_width), (centre_2, half_width), (centre_3, half_width))


# dtlz2's half-width, linear in the last decision variable
def dtlz2_half_width(x_n, eps):
    # docs/a1_uncertainty_model.md part 4, "the form":
    #     r_1(x) = r_2(x) = r_3(x) = eps * x_n
    # one function of x_n = x_12 for all three objectives, and the same array is
    # returned for all three.
    # why linear here and quadratic in zdt1, which is a1 part 4's reason. [3]'s
    # g is already quadratic in x_n with an interior optimum at x_n = 1/2, so a
    # half-width linear in x_n, whose optimum is at 0, already differs from it
    # and the trade-off is bounded. no extra curvature is needed and none is
    # added: a half-width of the form (x_n - 1/2)^2 would put the width's optimum
    # exactly on g's and reintroduce the alignment that makes phi_cw reproduce
    # the crisp order, which is the failure a1 part 4 measured on zdt1.
    # x_n >= 0 on the box, so this is non-negative, and at eps = 0 it is exactly
    # 0.0, a product and never a difference, as in zdt1_half_width.
    return eps * x_n


# dtlz2's decision box, the unit cube of [3] equation (9)
def bounds_dtlz2():
    # [3] section vii.b, equation (9): "0 <= x_i <= 1, for i = 1, 2, ..., n".
    return np.zeros(dtlz2_n_vars), np.ones(dtlz2_n_vars)


zdt1_interval = Problem(
    name="zdt1_interval", n_vars=zdt1_n_vars, n_obj=zdt1_n_obj,
    representation=zdt1_representation, evaluate=evaluate_zdt1, bounds=bounds_zdt1)
dtlz2_interval = Problem(
    name="dtlz2_interval", n_vars=dtlz2_n_vars, n_obj=dtlz2_n_obj,
    representation=dtlz2_representation, evaluate=evaluate_dtlz2, bounds=bounds_dtlz2)

# name to problem, the same convention src/problems_tier0.py and
# src/phi_transforms.py use, so experiment code loops rather than naming.
problem_registry = {"zdt1_interval": zdt1_interval, "dtlz2_interval": dtlz2_interval}
