# the three named automorphisms of [1], built through one constructor over coefficients.
# each phi takes the two arrays of one interval objective over a population and
# returns the two image coordinates as two arrays of the same shape.
# there are two evaluation routes and they are the same phi. an interval can be
# carried as its endpoint pair (f_l, f_u) or as its centre and half-width (c, r),
# and the two are related by the linear map (f_l, f_u) = M (c, r) with
# M = [[1, -1], [1, 1]], since f_l = c - r and f_u = c + r. composing [1]'s phi
# with M gives the same map read in the other coordinates, so which route is used
# changes the arithmetic and never the order. see make_phi_of_centre_radius for
# the composite and for why admissibility is still tested on lam and beta.
# a problem returns the representation in which its intervals are actually
# computed and phi is applied once to that; endpoints are never built from a
# centre and a radius and then differenced back. see src/problems_tier0.py.
# [1] is papers/new_preference_order_relationships_paper.txt, costa, osuna-gomez
# and chalco-cano, fuzzy sets and systems 477 (2024) 108812.

from collections import namedtuple

import numpy as np

# one phi, its coefficients, and both of its evaluation routes.
# the registry holds these records and not bare functions, and that is the point:
# a record is not callable, so phi(f_l, f_u) raises at once instead of quietly
# evaluating the wrong route. the caller has to name of_endpoints or
# of_centre_radius, and a problem names its own route in Problem.representation,
# so the two cannot be crossed by accident. a4-b measured what crossing them
# costs: the endpoint route shatters a width column's 46 true values into 210.
Phi = namedtuple("Phi", ("name", "lam", "beta", "of_endpoints", "of_centre_radius"))


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


# builds the same phi of the same coefficient pair, applied to (centre, half_width)
def make_phi_of_centre_radius(lam, beta):
    # f_l = c - r and f_u = c + r, so (f_l, f_u) = M (c, r) with
    # M = [[1, -1], [1, 1]] and det M = 2. composing the phi of [1] section 2,
    # page 3, lines 170-172 with M gives, entry by entry,
    #   first  = lam_1 (c - r) + lam_2 (c + r)  = (lam_1 + lam_2) c + (lam_2 - lam_1) r
    #   second = beta_1 (c - r) + beta_2 (c + r) = (beta_1 + beta_2) c + (beta_2 - beta_1) r
    # and det of that composite is 2 (lam_1 beta_2 - lam_2 beta_1) = 2 det phi,
    # so it vanishes exactly when the paper's condition fails and never otherwise.
    # this is therefore the same automorphism evaluated in different coordinates
    # and not a second family: [1]'s definition on endpoint pairs is untouched.
    # admissibility is tested where the paper states it, on lam and beta, by
    # calling make_phi and discarding the endpoint route it returns. the check
    # lives in exactly one place and runs on the paper's coefficients.
    make_phi(lam, beta)
    lam_1, lam_2 = float(lam[0]), float(lam[1])
    beta_1, beta_2 = float(beta[0]), float(beta[1])
    first_c, first_r = lam_1 + lam_2, lam_2 - lam_1
    second_c, second_r = beta_1 + beta_2, beta_2 - beta_1

    # the phi of these coefficients, applied to one interval objective over a population
    def phi(c, r):
        first = first_c * np.asarray(c) + first_r * np.asarray(r)
        second = second_c * np.asarray(c) + second_r * np.asarray(r)
        return first, second

    return phi


# builds one named phi with both of its routes, checking admissibility once
def make_phi_pair(name, lam, beta):
    # make_phi raises here if the pair is inadmissible, and
    # make_phi_of_centre_radius is then handed coefficients already accepted, so
    # the condition of [1] page 3 line 172 is tested once per phi and not twice.
    of_endpoints = make_phi(lam, beta)
    of_centre_radius = make_phi_of_centre_radius(lam, beta)
    return Phi(name=name, lam=tuple(float(v) for v in lam),
               beta=tuple(float(v) for v in beta),
               of_endpoints=of_endpoints, of_centre_radius=of_centre_radius)


# name to phi record, so experiment code loops over phi rather than naming them.
# the order lu, ls, cw is the order of examples 2.2, 2.3 and 2.4 in [1] and is
# the order every table and every loop in the project uses.
# example 2.2 of [1], page 5, lines 332-336: lambda = (1, 0), beta = (0, 1).
#     on endpoints it gives (f_l, f_u), the identity.
#     on (c, r) it gives (c - r, c + r), which is M itself.
# example 2.3 of [1], page 6, lines 342-346: lambda = (1, 0), beta = (-1, 1).
#     on endpoints it gives (f_l, f_u - f_l).
#     on (c, r) it gives (c - r, 2r), so the width is read and never subtracted.
# example 2.4 of [1], page 6, lines 348-353: lambda = (1/2, 1/2),
# beta = (-1/2, 1/2).
#     on endpoints it gives ((f_l + f_u) / 2, (f_u - f_l) / 2).
#     on (c, r) it gives (c, r) exactly, the identity, its composite matrix being
#     the identity with determinant 1 = 2 * (1/2).
# note the second coordinate of example 2.3 is the full width and that of example
# 2.4 is the half-width; they are two different orders and never one word.
phi_registry = {
    "lu": make_phi_pair("lu", (1.0, 0.0), (0.0, 1.0)),
    "ls": make_phi_pair("ls", (1.0, 0.0), (-1.0, 1.0)),
    "cw": make_phi_pair("cw", (0.5, 0.5), (-0.5, 0.5)),
}

# the endpoint route of each named phi, kept under the names a2 and a3 introduced.
# the paired centre-radius route of each is phi_registry[name].of_centre_radius.
phi_lu = phi_registry["lu"].of_endpoints
phi_ls = phi_registry["ls"].of_endpoints
phi_cw = phi_registry["cw"].of_endpoints
