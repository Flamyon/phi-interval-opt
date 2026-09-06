# interval arithmetic on numpy arrays of endpoints.
# an interval objective over a whole population is carried as two arrays of the
# same shape, a_l and a_u, with a_l <= a_u entrywise. every function below
# returns new arrays and never writes into its arguments.
# [1] is papers/new_preference_order_relationships_paper.txt, costa,
# osuna-gomez and chalco-cano, fuzzy sets and systems 477 (2024) 108812.
# [16] is papers/Newton Method for Multiobjective Optimization Problems of
# Interval-Valued Maps.pdf, mondal, ghosh and kim, and it is the only source in
# the corpus that prints the interval product; f6 added multiply and
# multiply_by_real from it. [9] is papers/9-Multiobjective programming in
# optimization of the interval objective function .pdf, ishibuchi and tanaka,
# european journal of operational research 48 (1990) 219-225.

import numpy as np


# sum of two intervals, endpoint by endpoint
def add(a_l, a_u, b_l, b_u):
    # [1] section 2, page 2, line 105:
    # [a_l, a_u] + [b_l, b_u] = [a_l + b_l, a_u + b_u]
    return np.add(a_l, b_l), np.add(a_u, b_u)


# product of a real scalar and an interval, swapping the endpoints when the scalar is negative
def scalar_multiply(lam, a_l, a_u):
    # [1] section 2, page 2, lines 103-106, the braced display beside the sum:
    # lam . [a_l, a_u] = [lam a_l, lam a_u] if lam >= 0, and
    # lam . [a_l, a_u] = [lam a_u, lam a_l] if lam < 0.
    # the branch is selected entrywise with np.where, so a lam array whose
    # entries differ in sign stays correct entry by entry.
    non_negative = np.greater_equal(lam, 0.0)
    lower = np.where(non_negative, np.multiply(lam, a_l), np.multiply(lam, a_u))
    upper = np.where(non_negative, np.multiply(lam, a_u), np.multiply(lam, a_l))
    return lower, upper


# the interval product, its source and its cross-check, kept above the two
# functions that implement it because it is one citation for both.
# the operation is item (iii) of the display of moore's four operations in [16]
# section 2.1, printed page 4, which stands between "which are defined as
# follows" and definition 2.1 and which [16] attributes to moore, its reference
# [28]. the locator is corrected here against the paper, re-read this session,
# and only the locator: the project has cited this operation as "definition
# 2.1(iii) of [16] printed page 3" since f2, and the display is unnumbered,
# precedes definition 2.1, which is the gh-difference, and is on printed page 4.
# the content is what it always was.
# cross-check, per the evidence rule. [9] definition 2.1, equation (2.5), printed
# page 220, defines the operation on two closed intervals, for * in {+, -, ., /},
# as the set of all s * t with s in the first and t in the second, and prints no
# closed form for the product, that paper using only the sum and the real
# multiple, its equations (2.6) to (2.9); the four corner products below are that
# set for the product, its endpoints being attained at corners because s t is
# monotone in each factor separately. [1] states no product at all: [1] section 2,
# page 2, lines 100-134 equips the interval space with addition and multiplication
# by a real scalar and with nothing else. so [16] is the only source in the corpus
# that prints the operation, and neither of the other two contradicts it.


# product of two intervals, the minimum and the maximum over the four endpoint products
def multiply(a_l, a_u, b_l, b_u):
    # [16] section 2.1 item (iii), printed page 4, with s := [s_l, s_u] and
    # t := [t_l, t_u]:
    #   s (.) t := [min{s_l t_l, s_l t_u, s_u t_l, s_u t_u},
    #               max{s_l t_l, s_l t_u, s_u t_l, s_u t_u}]
    # np.minimum and np.maximum choose entrywise, so one array may hold entries
    # of every sign case at once and a sign change inside b is resolved entry by
    # entry and never by a scalar branch. that is gh_difference's discipline.
    first = np.multiply(a_l, b_l)
    second = np.multiply(a_l, b_u)
    third = np.multiply(a_u, b_l)
    fourth = np.multiply(a_u, b_u)
    lower = np.minimum(np.minimum(first, second), np.minimum(third, fourth))
    upper = np.maximum(np.maximum(first, second), np.maximum(third, fourth))
    return lower, upper


# product of an interval and an array of real values, the degenerate case of multiply
def multiply_by_real(a_l, a_u, h):
    # [16]'s (iii) at t = [h, h]: the four corner products collapse to two, h a_l
    # and h a_u, and the product is the minimum and the maximum of those. this is
    # the operation an objective (+)_j [a_j, b_j] (.) h_j(x) of [16] appendix A
    # needs, and it is a separate name because writing multiply(a_l, a_u, h, h)
    # at every call site would read as two independent factors where there is one.
    # how this relates to scalar_multiply, and why both exist. scalar_multiply is
    # the same map by the route [1] prints, the sign branch of [1] section 2,
    # page 2, lines 103-106, and [9] equation (2.8) printed page 220 prints that
    # same branch; this one is the route [16] prints. they agree entry by entry
    # wherever both apply, and not approximately: where h >= 0, h a_l <= h a_u, so
    # the minimum is h a_l, which is the endpoint the branch selects, and where
    # h < 0 the inequality reverses and both give h a_u. the one thing that can
    # differ is the sign of a zero, np.minimum(-0.0, 0.0) being +0.0 where the
    # branch keeps -0.0, and -0.0 == 0.0, so no comparison, no order and no
    # arithmetic in the project can see it. both exist because each is the
    # operation its own source prints, and this module encodes what a source
    # prints rather than one form chosen from several.
    return multiply(a_l, a_u, h, h)


# centre of an interval, the first image coordinate of example 2.4 of [1]
def centre(a_l, a_u):
    # [1] example 2.4, page 6, lines 348-353: the first coordinate of phi_i is
    # (1/2) x_2i-1 + (1/2) x_2i = (x_2i-1 + x_2i) / 2
    return 0.5 * np.add(a_l, a_u)


# half-width of an interval, the second image coordinate of example 2.4 of [1]
def half_width(a_l, a_u):
    # [1] example 2.4, page 6, lines 348-353: the second coordinate of phi_i is
    # (-1/2) x_2i-1 + (1/2) x_2i = (x_2i - x_2i-1) / 2.
    # this carries the factor of one half and width below does not; they are the
    # second coordinates of two different orders and are never interchanged.
    return 0.5 * np.subtract(a_u, a_l)


# full width of an interval, the second image coordinate of example 2.3 of [1]
def width(a_l, a_u):
    # [1] example 2.3, page 6, lines 342-346: the second coordinate of phi_i is
    # -1 x_2i-1 + 1 x_2i = x_2i - x_2i-1, with no factor of one half.
    # kept a separate name from half_width because example 2.3 and example 2.4
    # are different orders and one word for both would hide the factor of two.
    return np.subtract(a_u, a_l)


# gh-difference of two intervals, defined for every pair and covering both branches
def gh_difference(a_l, a_u, b_l, b_u):
    # primary source: papers/Presentacion_optimizacion_intervalar.txt, slide 5 of
    # 23, equation (2), lines 109-117, which prints the definition as
    #   a -gh b = c  iff  (a) a = b + c      if mu(b) <= mu(a)
    #                     (b) b = a + (-1) c if mu(b) >  mu(a),
    # where mu is the length of the interval, mu(a) = a_u - a_l. the slide
    # attributes it to markov 1974 and stefanini 2008.
    # the closed form below is those two branches collected, not a further
    # assumption: on branch (a) solving a = b + c gives c = [a_l - b_l,
    # a_u - b_u], whose width mu(a) - mu(b) is non-negative there, so its lower
    # endpoint is the smaller of the two differences; on branch (b) solving
    # b = a + (-1) c gives c = [a_u - b_u, a_l - b_l], and there mu(b) > mu(a)
    # makes that ordering the correct one. hence
    #   a -gh b = [min{a_l - b_l, a_u - b_u}, max{a_l - b_l, a_u - b_u}].
    # secondary source, agreeing with the above and stating the closed form
    # directly: literature/gH-differentiability calculus for interval analysis.md
    # section 2, quoting stefanini, arana-jimenez and sorini 2025, information
    # sciences 691, 121601, section 2. that paper is not in papers/, so what is
    # still unverified is its own definition number, not the content; see p-05.
    # mu(b) <= mu(a) is the same test as half_width(b) <= half_width(a).
    # np.minimum and np.maximum choose entrywise, so a single array may hold
    # entries falling in either branch.
    lower_difference = np.subtract(a_l, b_l)
    upper_difference = np.subtract(a_u, b_u)
    lower = np.minimum(lower_difference, upper_difference)
    upper = np.maximum(lower_difference, upper_difference)
    return lower, upper
