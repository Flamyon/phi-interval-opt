# the two tier 0 analytic problems, evaluation only. no efficient set is derived
# here and none is assumed; what the phi-efficient sets are is b1's work.
# every problem is a Problem record and the four names on it are the calling
# convention a4, a5, c1 and c2 all share:
#   evaluate(x, params)  the interval bounds of every objective, as a tuple of
#                        (f_l, f_u) pairs, one pair per interval objective, each
#                        entry a numpy array over the population.
#   bounds()             the decision box, as (lower, upper) arrays.
#   n_vars               the number of decision variables.
#   n_obj                the number of interval objectives, m.
# n_obj is m and never 2m. the transformed real problem that theorem 3.1 of [1]
# licenses solving has 2m objectives, m interval objectives times two image
# coordinates each, and that doubling is done by src/phi_transforms.py and never
# here. confusing the two already cost this project one revision, so it is
# written down at the interface where the mistake would be made.
# x is an array of shape (population, n_vars); every returned array has the shape
# of the population, that is x.shape[:-1].
# [1] is papers/new_preference_order_relationships_paper.txt, costa,
# osuna-gomez and chalco-cano, fuzzy sets and systems 477 (2024) 108812.

from collections import namedtuple

import numpy as np

Problem = namedtuple("Problem", ("name", "n_vars", "n_obj", "evaluate", "bounds"))


# splits a population array into one array per decision variable
def decision_columns(x, n_vars):
    array = np.asarray(x, dtype=float)
    if array.ndim < 1 or array.shape[-1] != n_vars:
        raise ValueError(
            "x must have shape (population, {}), the last axis running over the "
            "decision variables; got shape {}".format(n_vars, array.shape)
        )
    return tuple(array[..., k] for k in range(n_vars))


# p0's dimensions. n = 1 and m = 2 are the paper's, not the project's:
# [1] lines 752-753 define F : R -> (C)^2 of one real variable.
p0_n_vars = 1
p0_n_obj = 2

# the published anchor point, and the whole of what [1] states about this F.
# lines 753-755, transcribed in docs/a0_framework.md c15: "Hence, f_1 and f_1-bar
# are not differentiable at x = 0, although x = 0 is a strict minimum for F
# considering the order relation <=_phi with phi given in Example 2.2." so the
# point is x = 0, the phi it is asserted under is phi_lu, example 2.2,
# lambda = (1, 0), beta = (0, 1), and the property is what the paper calls "a
# strict minimum". the paper does not name that property in the vocabulary of
# definition 3.1, whose three names are strong or strict optimal solution,
# optimal solution and weak optimal solution, and a0 found no sentence of [1]
# identifying the two. definition 3.1(1) is the plausible reading, being the one
# stated through the same relation <=_phi, but that is an inference and it is
# p-06 for b1, not something this comment asserts. the paper gives no proof.
# what the paper does not state, and what must therefore not be read off this
# constant: it says nothing about the efficient set of this F under phi_lu, and
# nothing at all about it under examples 2.3 or 2.4. this is an anchor point and
# not an efficient set. r-04 records the consequence for b1: the anchor cannot be
# reached by applying example 3.9 under phi_lu, because Lam_1^T f = -|x| and
# B_1^T f = |x| are both non-differentiable at 0, so that example's hypotheses
# fail exactly there.
p0_anchor = np.array([0.0])


# p0, the worked function [1] gives after example 3.9, as two interval objectives
def evaluate_p0(x, params=None):
    # [1] section 3.1, printed pages 10 and 11, lines 752-753, transcribed in
    # docs/a0_framework.md c15: F_1(x) = [-|x|, |x|] and F_2(x) = [0, x^2].
    # params is accepted and ignored. p0 has no imprecision parameter, its widths
    # being fixed by the paper; the argument is kept so that the calling
    # convention is one convention and not two.
    (x_1,) = decision_columns(x, p0_n_vars)
    first_lower = -np.abs(x_1)
    first_upper = np.abs(x_1)
    second_lower = np.zeros_like(x_1)
    second_upper = np.square(x_1)
    return ((first_lower, first_upper), (second_lower, second_upper))


# p0's decision box, holding the published anchor point in its interior
def bounds_p0():
    # [1] sets S = R, lines 752-753, so the box is the project's and not the
    # paper's. [-1, 1] is chosen because it contains negative values, which
    # CONTEXT.md section 10 a4 requires since the anchor sits at the origin, and
    # because the anchor is then the centre of the box and cannot lie on a face.
    return np.array([-1.0]), np.array([1.0])


# p1's dimensions, from docs/a1_uncertainty_model.md, section "p1, proposed"
p1_n_vars = 2
p1_n_obj = 2

# p1's decision box, docs/a1_uncertainty_model.md "p1, proposed" and unchanged by
# a1-b. it is not the unit box and the reason is example 3.9: condition (15) is
# unconstrained stationarity and carries no constraint multipliers, so b1 can
# apply it only at interior points. on [0, 1]^2 the efficient set would touch
# three faces. a1-b re-measured every phi's efficient set on this box and found
# all of them strictly interior.
p1_lower = np.array([-0.5, -0.5])
p1_upper = np.array([1.5, 1.5])

# p1's imprecision parameters. rho = 1/4 is a1-b's,
# docs/a1_uncertainty_model.md a1-b, "the modified p1, measured". delta was 1/10
# there and is 1/8 here; the change is a4-b's and its verification is
# docs/a4b_dominance_tolerance.md part 2.
# rho is fixed by interiority and not by taste. the stationary point of c - r in
# its width variable is at 1/(1 - rho); at rho = 1/2 that is 2, outside any
# reasonable box, and a1's grid check at rho = 1/2 returned a phi_lu efficient set
# running to the face. at rho = 1/4 it is 4/3, interior to [-0.5, 1.5]. rho must
# also stay below 1 for c - r to be convex at all.
# delta keeps the half-width strictly positive, over [0.1250, 0.6875] on the box,
# so no interval degenerates. it is 1/8 rather than a1-b's 1/10 because 1/10 is
# not a dyadic rational and was the only constant in p1 that is not: a4-b
# measured that on a dyadic sample f_u - f_l then differs from 2r at 3314 of 4225
# points and gives the width column 150 distinct values where it truly has 49,
# while at delta = 1/8 the same sample is exact, 4225 of 4225 bitwise and 49
# distinct values. delta enters every image coordinate as an additive constant,
# so no gradient, hessian, stationary point or interiority claim of a1-b moves
# and every phi's efficient index set is unchanged; a4-b part 2 verifies both in
# exact integer arithmetic. this buys exactness only where the sample is itself
# dyadic, so it does not remove the need for a project dominance rule.
p1_default_params = {"rho": 0.25, "delta": 0.125}

# the shape of p1, docs/a1_uncertainty_model.md a1-b, "the modified p1, measured".
# this is the modified design with distinct widths, not a1's identical-width
# version: r_1 is driven by x_2 and r_2 by x_1, so the two width columns of the
# transformed problem are different functions of x. under a1's identical widths
# they were the same function and one of the four transformed objectives
# contributed nothing to dominance.
# all ten distinct image coordinates, three phi times two objectives times two
# coordinates with phi_lu and phi_ls sharing their first, are degree-2
# polynomials with constant positive semidefinite hessians. they are therefore
# differentiable to every order and globally convex, and every one of their
# stationary points and stationary lines meets the interior of the box. that is
# what keeps example 3.9 available to b1 here, and it is verified coordinate by
# coordinate, by hessian eigenvalue and by a 20000-chord midpoint convexity test,
# in docs/a1_uncertainty_model.md a1-b, "Hessians, eigenvalues, convexity and
# stationary points".


# reads rho and delta out of params, falling back to the values a1-b verified
def p1_parameters(params):
    values = dict(p1_default_params)
    if params is not None:
        values.update(params)
    rho = float(values["rho"])
    delta = float(values["delta"])
    # a1's two standing conditions on the pair. rho >= 1 makes c - r non-convex,
    # which loses theorem 3.3 and example 3.9 together; delta <= 0 lets the
    # half-width vanish, which is the degenerate case of CONTEXT.md section 5
    # step 1. only rho = 1/4 with delta = 1/10 has been measured; any other
    # admissible pair passes these checks but carries none of a1-b's numbers.
    if not 0.0 < rho < 1.0:
        raise ValueError("rho must lie strictly in (0, 1); got {}".format(rho))
    if delta <= 0.0:
        raise ValueError("delta must be strictly positive; got {}".format(delta))
    return rho, delta


# p1, the modified two-variable design of a1-b, as two interval objectives
def evaluate_p1(x, params=None):
    # centres, a1-b: c_1 = x_1^2 + (x_2 - 1)^2 and c_2 = (x_1 - 1)^2 + (x_2 - 1)^2.
    # half-widths, a1-b: r_1 = rho x_2^2 + delta and r_2 = rho x_1^2 + delta.
    # objective 2 is objective 1 with the roles of x_1 and x_2 exchanged and the
    # centre shifted, which is what makes the two width columns distinct.
    x_1, x_2 = decision_columns(x, p1_n_vars)
    rho, delta = p1_parameters(params)
    centre_1 = np.square(x_1) + np.square(x_2 - 1.0)
    centre_2 = np.square(x_1 - 1.0) + np.square(x_2 - 1.0)
    half_width_1 = rho * np.square(x_2) + delta
    half_width_2 = rho * np.square(x_1) + delta
    return (
        (centre_1 - half_width_1, centre_1 + half_width_1),
        (centre_2 - half_width_2, centre_2 + half_width_2),
    )


# p1's decision box, the square a1-b measured every efficient set inside
def bounds_p1():
    return np.array(p1_lower), np.array(p1_upper)


p0 = Problem(name="p0", n_vars=p0_n_vars, n_obj=p0_n_obj, evaluate=evaluate_p0, bounds=bounds_p0)
p1 = Problem(name="p1", n_vars=p1_n_vars, n_obj=p1_n_obj, evaluate=evaluate_p1, bounds=bounds_p1)

# name to problem, so experiment code loops over problems rather than naming them,
# the same convention phi_registry uses in src/phi_transforms.py.
problem_registry = {"p0": p0, "p1": p1}
