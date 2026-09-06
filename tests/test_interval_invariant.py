# f6's regression check, and it is the check that proves no result moves.
#
# f6 did two things to evaluation: src/interval_math.py gained the interval
# product of [16] section 2.1 item (iii), printed page 4, and
# src/problems_native.py's objective_endpoints now goes through it instead of
# computing (sum_j a_ij h_ij, sum_j b_ij h_ij) in fixed order. every other
# problem of the project was left untouched, having no interval coefficient
# multiplying anything at all, docs/part2/f5_boundary_interchange.md section 2
# per problem. this file asserts both halves of that sentence rather than
# stating them.
#
# what is asserted, and where the content of each assertion is.
#   the bitwise comparison has content on exactly one problem. I-BK1 is the only
#   place in the project where an interval coefficient multiplies a function of
#   x, so it is the only place with two readings to compare, and the fixed-order
#   reading is written out below as src/problems_native.py computed it before f6
#   and compared against the module bitwise on a dense grid of the whole box. the
#   two agree because every h_ij of I-BK1 is a square, and that reason is itself
#   asserted on the same grid rather than quoted.
#   the invariant carries the rest. every problem of every registry is evaluated
#   on a dense sample of its own box and every interval it returns must satisfy
#   f_l <= f_u, which is r >= 0 in centre and half-width coordinates. that is the
#   guard of src/problems_tier0.py doing its work, and it is what a future
#   problem breaking the non-negativity assumption would fail here.
#   the loop is over the three registries and not over a list of five names, so a
#   problem a later session adds is covered without this file being edited, and
#   the five the project has today are asserted present so that a registry
#   emptied by accident cannot make the loop vacuous.
#
# the check against the source rather than against the project is not here and is
# not duplicated here: [16]'s printed G(x*) at Table 1's x* is
# tests/test_problems_native.py, test_printed_objective_row_reproduces, which
# reads ibk1.evaluate and therefore now runs through the product.
#
# no tolerance appears in this file. the comparisons are np.array_equal on
# doubles and the invariant is a comparison of doubles, both exact.

import numpy as np
import pytest

import problems_native
import problems_tier0
import problems_tier1
from problems_native import basis_functions, ibk1_coefficients
from problems_tier1 import epsilon_levels

# the five problems the project carries today, in the order tier 0, tier 1, native
project_problems = ("p0", "p1", "zdt1_interval", "dtlz2_interval", "ibk1")

# the dense samples. a grid where the dimension allows one and a uniform draw
# above it, and the draw carries both corners of the box so that the faces are
# evaluated and not only the interior.
grid_side_by_dimension = {1: 20001, 2: 201}
draw_size = 20000
draw_seed = 20260906

# I-BK1's box gridded for the bitwise comparison, 201 x 201 = 40401 points of
# [-10, 10]^2. the grid runs over the whole published box and not over the
# [0, 5]^2 the derived sets live in, since what is being compared is the
# evaluation and not the derivation.
ibk1_grid_side = 201


# every problem of the project, from the registries and not from a list of names
def all_problems():
    registries = (problems_tier0.problem_registry, problems_tier1.problem_registry,
                  problems_native.problem_registry)
    return [problem for registry in registries
            for _, problem in sorted(registry.items())]


# the parameter sets one problem must hold the invariant at
def parameter_cases(problem):
    # tier 1 carries the imprecision level and is checked at every level of a1's
    # sweep, the crisp baseline included, since eps = 0 is where every half-width
    # is exactly zero and r >= 0 holds with no margin. every other problem takes
    # its own defaults through params = None, which is the calling convention.
    if problem.name in problems_tier1.problem_registry:
        return [{"eps": level} for level in epsilon_levels]
    return [None]


# a dense sample of one problem's box, a grid in low dimension and a draw above it
def dense_sample(problem):
    lower, upper = problem.bounds()
    side = grid_side_by_dimension.get(problem.n_vars)
    if side is not None:
        return grid_points(lower, upper, side)
    generator = np.random.default_rng(draw_seed)
    drawn = generator.uniform(lower, upper, size=(draw_size, problem.n_vars))
    return np.concatenate([drawn, lower[None, :], upper[None, :]], axis=0)


# a regular grid over a box, one array of points with the decision variables last
def grid_points(lower, upper, n_side):
    axes = [np.linspace(lower[k], upper[k], n_side) for k in range(len(lower))]
    mesh = np.meshgrid(*axes, indexing="ij")
    return np.stack([axis.ravel() for axis in mesh], axis=-1)


# I-BK1's endpoints as src/problems_native.py computed them before f6
def fixed_order_endpoints(objective, x_1, x_2):
    # the expression f5 section 1.1 read at problems_native.py lines 115 to 118,
    # kept here and nowhere else in the project: (sum_j a_ij h_ij, sum_j b_ij
    # h_ij), the two endpoints in fixed order and no minimum or maximum taken.
    first, second = basis_functions(objective, x_1, x_2)
    (lower_1, upper_1), (lower_2, upper_2) = ibk1_coefficients[objective]
    return (lower_1 * first + lower_2 * second, upper_1 * first + upper_2 * second)


# whether the interval one pair denotes is well ordered, entry by entry
def denotes_a_well_ordered_interval(problem, pair):
    # written out here rather than imported from src/problems_tier0.py, so that
    # the loop below is not the guard checked against itself: the guard runs
    # inside every evaluate call and this is a second, independent reading of the
    # same invariant in the same coordinates.
    if problem.representation == "endpoints":
        return np.less_equal(pair[0], pair[1])
    return np.greater_equal(pair[1], 0.0)


# the registries hold the five problems the project has, so the loop is not vacuous
def test_every_project_problem_is_in_a_registry():
    assert set(project_problems) <= {problem.name for problem in all_problems()}


# every problem returns well ordered intervals at every point of a dense sample
@pytest.mark.parametrize("problem", all_problems(),
                         ids=[problem.name for problem in all_problems()])
def test_the_invariant_holds_on_a_dense_sample_of_every_box(problem):
    # this is also why the guard can be on always and refuse rather than warn: no
    # problem of the project can trip it. f5 section 2 established that per
    # problem, by construction on four of them and on a 200000-point draw for
    # I-BK1; here it is one loop over the registries, on grids where the
    # dimension allows a grid, so that a problem added later is measured and not
    # argued about.
    points = dense_sample(problem)
    assert len(points) >= draw_size
    for params in parameter_cases(problem):
        for objective, pair in enumerate(problem.evaluate(points, params)):
            assert np.all(denotes_a_well_ordered_interval(problem, pair)), (
                problem.name, objective)


# the product and the fixed-order reading agree bitwise everywhere on I-BK1's box
def test_the_product_agrees_with_the_fixed_order_reading_on_ibk1():
    # the whole of "no result of f2 or f3 moves". the module's objective_endpoints
    # now takes minima and maxima over the corner products and the pre-f6
    # expression above takes neither, and on this problem they are the same
    # double at every one of 40401 grid points, so every number f3 measured is
    # the number it would measure today.
    points = grid_points(*problems_native.ibk1.bounds(), ibk1_grid_side)
    x_1, x_2 = points[:, 0], points[:, 1]
    for objective in range(problems_native.ibk1_n_obj):
        product = problems_native.objective_endpoints(objective, x_1, x_2)
        fixed_order = fixed_order_endpoints(objective, x_1, x_2)
        assert np.array_equal(product[0], fixed_order[0]), objective
        assert np.array_equal(product[1], fixed_order[1]), objective


# and they agree because every basis function of I-BK1 is non-negative on the box
def test_every_basis_function_of_ibk1_is_non_negative_on_its_box():
    # the reason the two readings coincide, asserted rather than quoted: where a
    # basis function is non-negative the smallest corner product is a_ij h_ij and
    # the largest is b_ij h_ij, which is exactly the fixed-order pair. it is a
    # statement about I-BK1 and about the assumption under which the comparison
    # above can pass, so a change to these basis functions fails here first and
    # there second, which is the order a later session wants to read them in.
    points = grid_points(*problems_native.ibk1.bounds(), ibk1_grid_side)
    x_1, x_2 = points[:, 0], points[:, 1]
    for objective in range(problems_native.ibk1_n_obj):
        for values in basis_functions(objective, x_1, x_2):
            assert np.all(values >= 0.0), objective


# the coefficient intervals I-BK1 multiplies by are themselves well ordered
def test_ibk1_s_coefficient_intervals_are_well_ordered():
    # the transcription check the product makes newly relevant: an interchanged
    # coefficient pair would give an interchanged interval at every point where
    # its basis function is positive, and the guard would then fire on the
    # published problem itself.
    point = np.array([1.0]), np.array([2.0])
    for objective, coefficients in enumerate(ibk1_coefficients):
        assert len(coefficients) == len(basis_functions(objective, *point))
        for lower, upper in coefficients:
            assert lower <= upper, objective
