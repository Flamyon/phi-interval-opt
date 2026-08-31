# the three named automorphisms of [1], built through one constructor over coefficients.
# each phi takes the two endpoint arrays of one interval objective over a population
# and returns the two image coordinates as two arrays of the same shape.
# [1] is papers/new_preference_order_relationships_paper.txt, costa, osuna-gomez
# and chalco-cano, fuzzy sets and systems 477 (2024) 108812.

import numpy as np


# builds the phi of one coefficient pair, rejecting a pair the paper does not admit
def make_phi(lam, beta):
    # [1] section 2, page 3, lines 170-172, the unnumbered display and the line
    # under it: phi_i(x_2i-1, x_2i) = (lambda_2i-1 x_2i-1 + lambda_2i x_2i,
    # beta_2i-1 x_2i-1 + beta_2i x_2i), where the four coefficients are "real
    # numbers (that can be chosen according to a decision)" subject to the single
    # condition "lambda_2i-1 beta_2i != lambda_2i beta_2i-1".
    # x_2i-1 is the lower endpoint f_l and x_2i is the upper endpoint f_u.
    lam_1, lam_2 = float(lam[0]), float(lam[1])
    beta_1, beta_2 = float(beta[0]), float(beta[1])
    # the condition is an exact inequality in the paper, so it is tested exactly
    # and not against a tolerance.
    determinant = lam_1 * beta_2 - lam_2 * beta_1
    if determinant == 0.0:
        raise ValueError(
            "inadmissible coefficients lam = ({}, {}), beta = ({}, {}): "
            "lam_1 beta_2 - lam_2 beta_1 = {}, but [1] section 2, page 3, line 172 "
            "requires lambda_2i-1 beta_2i != lambda_2i beta_2i-1, so this pair is "
            "not an automorphism of r^2".format(lam_1, lam_2, beta_1, beta_2, determinant)
        )

    # the phi of these coefficients, applied to one interval objective over a population
    def phi(f_l, f_u):
        first = lam_1 * np.asarray(f_l) + lam_2 * np.asarray(f_u)
        second = beta_1 * np.asarray(f_l) + beta_2 * np.asarray(f_u)
        return first, second

    return phi


# example 2.2 of [1], page 5, lines 332-336: lambda = (1, 0), beta = (0, 1), giving (f_l, f_u)
phi_lu = make_phi((1.0, 0.0), (0.0, 1.0))

# example 2.3 of [1], page 6, lines 342-346: lambda = (1, 0), beta = (-1, 1), giving (f_l, f_u - f_l)
phi_ls = make_phi((1.0, 0.0), (-1.0, 1.0))

# example 2.4 of [1], page 6, lines 348-353: lambda = (1/2, 1/2), beta = (-1/2, 1/2),
# giving ((f_l + f_u) / 2, (f_u - f_l) / 2), the centre and the half-width.
# note the second coordinate here is half the second coordinate of phi_ls above.
phi_cw = make_phi((0.5, 0.5), (-0.5, 0.5))

# name to function, so experiment code loops over phi rather than naming them.
# the order lu, ls, cw is the order of examples 2.2, 2.3 and 2.4 in [1] and is
# the order every table and every loop in the project uses.
phi_registry = {"lu": phi_lu, "ls": phi_ls, "cw": phi_cw}
