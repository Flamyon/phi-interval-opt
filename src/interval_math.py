# interval arithmetic on numpy arrays of endpoints.
# an interval objective over a whole population is carried as two arrays of the
# same shape, a_l and a_u, with a_l <= a_u entrywise. every function below
# returns new arrays and never writes into its arguments.
# [1] is papers/new_preference_order_relationships_paper.txt, costa,
# osuna-gomez and chalco-cano, fuzzy sets and systems 477 (2024) 108812.

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
    # source read in this project: literature/gH-differentiability calculus for
    # interval analysis.md section 2, "what is the gh-difference?", which quotes
    # stefanini, arana-jimenez and sorini 2025, information sciences 691,
    # 121601, section 2. the primary paper is not in papers/, so this citation
    # is to the summary and not to the paper itself.
    # definition as quoted there:
    #   a -gh b = c  iff  (a) a = b + c  or  (b) b = a + (-1) c,
    # with the closed form that covers both branches
    #   a -gh b = [min{a_l - b_l, a_u - b_u}, max{a_l - b_l, a_u - b_u}].
    # branch (a) is the one taken where half_width(a) >= half_width(b) and
    # branch (b) where it is smaller. np.minimum and np.maximum choose entrywise,
    # so a single array may hold entries falling in either branch.
    lower_difference = np.subtract(a_l, b_l)
    upper_difference = np.subtract(a_u, b_u)
    lower = np.minimum(lower_difference, upper_difference)
    upper = np.maximum(lower_difference, upper_difference)
    return lower, upper
