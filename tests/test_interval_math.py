# tests for src/interval_math.py, subpart a2

import numpy as np

from interval_math import (add, centre, gh_difference, half_width, multiply,
                           multiply_by_real, scalar_multiply, width)


# a fixed pair of interval populations, entry 1 degenerate on purpose
def sample_pair():
    a_l = np.array([-2.0, 0.0, 1.0, 3.0])
    a_u = np.array([-1.0, 0.0, 4.0, 3.5])
    b_l = np.array([0.5, -1.0, 2.0, -3.0])
    b_u = np.array([2.5, 1.0, 2.5, 1.0])
    return a_l, a_u, b_l, b_u


# calls every function of the module once on the given pair, returning the results
def call_every_function(a_l, a_u, b_l, b_u):
    return [
        add(a_l, a_u, b_l, b_u),
        scalar_multiply(-1.5, a_l, a_u),
        multiply(a_l, a_u, b_l, b_u),
        multiply_by_real(a_l, a_u, b_l),
        (centre(a_l, a_u),),
        (half_width(a_l, a_u),),
        (width(a_l, a_u),),
        gh_difference(a_l, a_u, b_l, b_u),
    ]


# add sums the lower bounds and the upper bounds separately
def test_add_sums_endpoints():
    a_l, a_u, b_l, b_u = sample_pair()
    lower, upper = add(a_l, a_u, b_l, b_u)
    assert np.array_equal(lower, a_l + b_l)
    assert np.array_equal(upper, a_u + b_u)
    assert np.all(lower <= upper)


# a negative scalar swaps the endpoints
def test_scalar_multiply_negative_swaps_endpoints():
    a_l = np.array([1.0, -3.0, 0.0])
    a_u = np.array([4.0, -1.0, 0.0])
    lower, upper = scalar_multiply(-2.0, a_l, a_u)
    assert np.array_equal(lower, -2.0 * a_u)
    assert np.array_equal(upper, -2.0 * a_l)
    assert np.all(lower <= upper)


# a positive scalar leaves the endpoints in place
def test_scalar_multiply_positive_keeps_endpoints():
    a_l = np.array([1.0, -3.0, 0.0])
    a_u = np.array([4.0, -1.0, 0.0])
    lower, upper = scalar_multiply(3.0, a_l, a_u)
    assert np.array_equal(lower, 3.0 * a_l)
    assert np.array_equal(upper, 3.0 * a_u)
    assert np.all(lower <= upper)


# a zero scalar collapses every interval to the degenerate interval at zero
def test_scalar_multiply_zero_gives_degenerate_interval():
    a_l = np.array([1.0, -3.0, 0.0])
    a_u = np.array([4.0, -1.0, 0.0])
    lower, upper = scalar_multiply(0.0, a_l, a_u)
    assert np.array_equal(lower, np.zeros(3))
    assert np.array_equal(upper, np.zeros(3))
    assert np.array_equal(width(lower, upper), np.zeros(3))


# a lam array with entries of both signs is branch-correct entry by entry
def test_scalar_multiply_mixed_sign_array_is_elementwise():
    a_l = np.array([1.0, 1.0, 1.0])
    a_u = np.array([4.0, 4.0, 4.0])
    lam = np.array([2.0, -2.0, 0.0])
    lower, upper = scalar_multiply(lam, a_l, a_u)
    assert np.array_equal(lower, np.array([2.0, -8.0, 0.0]))
    assert np.array_equal(upper, np.array([8.0, -2.0, 0.0]))


# the four sign cases of one factor against a fixed interval, hand-checked
def test_multiply_covers_every_sign_combination():
    # one column per case, hand-computed from the four corner products of [16]
    # section 2.1 item (iii), printed page 4:
    #   [1, 2] (.) [3, 4]     both positive          [3, 8]
    #   [1, 2] (.) [-4, -3]   second negative        [-8, -3]
    #   [-2, -1] (.) [3, 4]   first negative         [-8, -3]
    #   [-2, -1] (.) [-4, -3] both negative          [3, 8]
    #   [-2, 3] (.) [-4, 5]   both span zero         [-12, 15]
    #   [-2, 3] (.) [0, 0]    a degenerate zero      [0, 0]
    a_l = np.array([1.0, 1.0, -2.0, -2.0, -2.0, -2.0])
    a_u = np.array([2.0, 2.0, -1.0, -1.0, 3.0, 3.0])
    b_l = np.array([3.0, -4.0, 3.0, -4.0, -4.0, 0.0])
    b_u = np.array([4.0, -3.0, 4.0, -3.0, 5.0, 0.0])
    lower, upper = multiply(a_l, a_u, b_l, b_u)
    assert np.array_equal(lower, np.array([3.0, -8.0, -8.0, 3.0, -12.0, 0.0]))
    assert np.array_equal(upper, np.array([8.0, -3.0, -3.0, 8.0, 15.0, 0.0]))
    assert np.all(lower <= upper)


# the product of two intervals is the set of products of their members
def test_multiply_is_the_set_of_products_of_the_members():
    # [9] definition 2.1, equation (2.5), printed page 220, defines the operation
    # as that set, and the closed form is checked against it here rather than
    # against itself: every product of a point of the first interval and a point
    # of the second lies inside the returned interval, and both endpoints are
    # attained by some such pair.
    generator = np.random.default_rng(20260906)
    a_l = generator.uniform(-5.0, 5.0, size=200)
    a_u = a_l + generator.uniform(0.0, 4.0, size=200)
    b_l = generator.uniform(-5.0, 5.0, size=200)
    b_u = b_l + generator.uniform(0.0, 4.0, size=200)
    lower, upper = multiply(a_l, a_u, b_l, b_u)
    steps = np.linspace(0.0, 1.0, 51)
    inside_a = a_l[:, None] + steps[None, :] * (a_u - a_l)[:, None]
    inside_b = b_l[:, None] + steps[None, :] * (b_u - b_l)[:, None]
    products = inside_a[:, :, None] * inside_b[:, None, :]
    assert np.all(products >= lower[:, None, None])
    assert np.all(products <= upper[:, None, None])
    assert np.array_equal(np.min(products, axis=(1, 2)), lower)
    assert np.array_equal(np.max(products, axis=(1, 2)), upper)


# one array whose entries fall in different sign cases is resolved entry by entry
def test_multiply_by_real_is_elementwise_across_a_sign_change():
    # the coefficient interval is one interval and h is an array with entries of
    # both signs and an exact zero, so a scalar branch on the sign of h would be
    # wrong at four of the seven entries and right at three.
    h = np.array([-2.0, -1.0, -0.5, 0.0, 0.5, 1.0, 2.0])
    lower, upper = multiply_by_real(2.0, 3.0, h)
    assert np.array_equal(lower, np.array([-6.0, -3.0, -1.5, 0.0, 1.0, 2.0, 4.0]))
    assert np.array_equal(upper, np.array([-4.0, -2.0, -1.0, 0.0, 1.5, 3.0, 6.0]))
    assert np.all(lower <= upper)


# an interval spanning zero times a value of exactly zero is the degenerate zero interval
def test_multiply_by_real_at_exactly_zero_is_the_zero_interval():
    a_l, a_u = np.array([-2.0, 0.0, 1.0]), np.array([3.0, 0.0, 4.0])
    lower, upper = multiply_by_real(a_l, a_u, np.zeros(3))
    assert np.array_equal(lower, np.zeros(3))
    assert np.array_equal(upper, np.zeros(3))
    assert np.array_equal(width(lower, upper), np.zeros(3))


# multiply_by_real and scalar_multiply are the same map by two sources' routes
def test_multiply_by_real_agrees_with_scalar_multiply():
    # [16]'s (iii) at a degenerate second factor against [1]'s printed sign
    # branch, on an array carrying both signs and a zero. they agree entry by
    # entry, which is what the comment on multiply_by_real claims; the sign of a
    # zero is not asserted, np.minimum(-0.0, 0.0) being +0.0 and -0.0 == 0.0.
    generator = np.random.default_rng(20260906)
    a_l = generator.uniform(-6.0, 6.0, size=500)
    a_u = a_l + generator.uniform(0.0, 3.0, size=500)
    h = np.concatenate([generator.uniform(-4.0, 4.0, size=498), [0.0, 0.0]])
    by_moore = multiply_by_real(a_l, a_u, h)
    by_branch = scalar_multiply(h, a_l, a_u)
    assert np.array_equal(by_moore[0], by_branch[0])
    assert np.array_equal(by_moore[1], by_branch[1])
    assert (h < 0.0).any() and (h > 0.0).any() and (h == 0.0).any()


# f5's own diagnostic, as a test: the product does not interchange the boundary functions
def test_the_product_is_well_ordered_across_i_vu2_s_sign_change():
    # docs/part2/f5_boundary_interchange.md section 1.2, block C, reproduced as an
    # assertion. the form is I-VU2's G_1, problem 2 of [16] appendix A printed
    # page 28, [1, 1.5] (.) x_1 (+) [1, 1.5] (.) x_2 at x_2 = 0, evaluated at
    # f5's seven points of [-4, 4]^2. the fixed-order reading returns lower >
    # upper at the three points with x_1 < 0 and the product returns f5's printed
    # moore rows, which are well ordered at all seven.
    x_1 = np.array([-2.0, -1.0, -0.5, 0.0, 0.5, 1.0, 2.0])
    x_2 = np.zeros_like(x_1)
    first = multiply_by_real(1.0, 1.5, x_1)
    second = multiply_by_real(1.0, 1.5, x_2)
    lower, upper = add(first[0], first[1], second[0], second[1])
    assert np.array_equal(lower, np.array([-3.0, -1.5, -0.75, 0.0, 0.5, 1.0, 2.0]))
    assert np.array_equal(upper, np.array([-2.0, -1.0, -0.5, 0.0, 0.75, 1.5, 3.0]))
    assert np.all(lower <= upper)
    fixed_order_lower = 1.0 * x_1 + 1.0 * x_2
    fixed_order_upper = 1.5 * x_1 + 1.5 * x_2
    assert np.count_nonzero(fixed_order_lower > fixed_order_upper) == 3


# centre, half_width and width on intervals whose values are known by hand
def test_centre_half_width_and_width_on_known_intervals():
    a_l = np.array([2.0, -3.0, 5.0])
    a_u = np.array([6.0, 1.0, 5.0])
    assert np.array_equal(centre(a_l, a_u), np.array([4.0, -1.0, 5.0]))
    assert np.array_equal(half_width(a_l, a_u), np.array([2.0, 2.0, 0.0]))
    assert np.array_equal(width(a_l, a_u), np.array([4.0, 4.0, 0.0]))


# width is exactly twice half_width, the factor that separates example 2.3 from example 2.4
def test_width_is_twice_half_width_on_a_random_array():
    generator = np.random.default_rng(20260831)
    a_l = generator.uniform(-10.0, 10.0, size=500)
    a_u = a_l + generator.uniform(0.0, 5.0, size=500)
    assert np.array_equal(width(a_l, a_u), 2.0 * half_width(a_l, a_u))
    assert not np.array_equal(width(a_l, a_u), half_width(a_l, a_u))


# the first branch of the gh-difference, where a is the wider interval and a = b + c
def test_gh_difference_first_branch():
    a_l, a_u = np.array([1.0]), np.array([5.0])
    b_l, b_u = np.array([0.0]), np.array([1.0])
    lower, upper = gh_difference(a_l, a_u, b_l, b_u)
    assert np.array_equal(lower, np.array([1.0]))
    assert np.array_equal(upper, np.array([4.0]))
    recovered_l, recovered_u = add(b_l, b_u, lower, upper)
    assert np.array_equal(recovered_l, a_l)
    assert np.array_equal(recovered_u, a_u)


# the second branch of the gh-difference, where b is the wider interval and b = a + (-1) c
def test_gh_difference_second_branch():
    a_l, a_u = np.array([1.0]), np.array([2.0])
    b_l, b_u = np.array([0.0]), np.array([4.0])
    lower, upper = gh_difference(a_l, a_u, b_l, b_u)
    assert np.array_equal(lower, np.array([-2.0]))
    assert np.array_equal(upper, np.array([1.0]))
    negated_l, negated_u = scalar_multiply(-1.0, lower, upper)
    recovered_l, recovered_u = add(a_l, a_u, negated_l, negated_u)
    assert np.array_equal(recovered_l, b_l)
    assert np.array_equal(recovered_u, b_u)


# one array holding entries of both branches is resolved entry by entry
def test_gh_difference_mixed_branches_in_one_array():
    a_l = np.array([1.0, 1.0, 2.0, -4.0])
    a_u = np.array([5.0, 2.0, 2.0, 0.0])
    b_l = np.array([0.0, 0.0, 1.0, -1.0])
    b_u = np.array([1.0, 4.0, 3.0, 1.0])
    lower, upper = gh_difference(a_l, a_u, b_l, b_u)
    assert np.array_equal(lower, np.array([1.0, -2.0, -1.0, -3.0]))
    assert np.array_equal(upper, np.array([4.0, 1.0, 1.0, -1.0]))
    first_branch = half_width(a_l, a_u) >= half_width(b_l, b_u)
    assert first_branch.any() and not first_branch.all()


# the defining property of the gh-difference holds entrywise on a mixed random array
def test_gh_difference_satisfies_its_definition_entrywise():
    generator = np.random.default_rng(20260831)
    a_l = generator.uniform(-10.0, 10.0, size=500)
    a_u = a_l + generator.uniform(0.0, 6.0, size=500)
    b_l = generator.uniform(-10.0, 10.0, size=500)
    b_u = b_l + generator.uniform(0.0, 6.0, size=500)
    lower, upper = gh_difference(a_l, a_u, b_l, b_u)
    first_branch = half_width(a_l, a_u) >= half_width(b_l, b_u)
    assert first_branch.any() and not first_branch.all()
    forward_l, forward_u = add(b_l, b_u, lower, upper)
    negated_l, negated_u = scalar_multiply(-1.0, lower, upper)
    backward_l, backward_u = add(a_l, a_u, negated_l, negated_u)
    assert np.allclose(np.where(first_branch, forward_l, backward_l),
                       np.where(first_branch, a_l, b_l))
    assert np.allclose(np.where(first_branch, forward_u, backward_u),
                       np.where(first_branch, a_u, b_u))


# a degenerate interval has zero width and a well defined gh-difference
def test_degenerate_interval_is_handled():
    a_l = np.array([3.0, -1.0, 0.0])
    a_u = np.array([3.0, -1.0, 0.0])
    b_l = np.array([1.0, -4.0, -2.0])
    b_u = np.array([1.0, 2.0, -2.0])
    assert np.array_equal(width(a_l, a_u), np.zeros(3))
    assert np.array_equal(half_width(a_l, a_u), np.zeros(3))
    assert np.array_equal(centre(a_l, a_u), a_l)
    lower, upper = gh_difference(a_l, a_u, b_l, b_u)
    assert np.array_equal(lower, np.array([2.0, -3.0, 2.0]))
    assert np.array_equal(upper, np.array([2.0, 3.0, 2.0]))
    assert np.all(lower <= upper)


# the gh-difference of an interval with itself is the degenerate interval at zero
def test_gh_difference_of_an_interval_with_itself_is_zero():
    a_l, a_u, _, _ = sample_pair()
    lower, upper = gh_difference(a_l, a_u, a_l, a_u)
    assert np.array_equal(lower, np.zeros(4))
    assert np.array_equal(upper, np.zeros(4))


# every function returns arrays of the shape of its inputs
def test_every_function_preserves_shape():
    a_l, a_u, b_l, b_u = sample_pair()
    for result in call_every_function(a_l, a_u, b_l, b_u):
        for array in result:
            assert isinstance(array, np.ndarray)
            assert array.shape == a_l.shape


# no function writes into its arguments
def test_no_function_mutates_its_inputs():
    a_l, a_u, b_l, b_u = sample_pair()
    before = [a_l.copy(), a_u.copy(), b_l.copy(), b_u.copy()]
    call_every_function(a_l, a_u, b_l, b_u)
    for original, argument in zip(before, [a_l, a_u, b_l, b_u]):
        assert np.array_equal(original, argument)


# a constant-width construction stays constant in width up to rounding, the r-07 case
def test_constant_width_construction_is_constant_up_to_rounding():
    generator = np.random.default_rng(20260831)
    centres = generator.uniform(-1000.0, 1000.0, size=500)
    epsilon = 0.05
    a_l = centres - epsilon
    a_u = centres + epsilon
    widths = width(a_l, a_u)
    assert np.allclose(widths, 2.0 * epsilon)
    assert np.max(np.abs(widths - 2.0 * epsilon)) < 1e-12
    assert np.array_equal(widths, 2.0 * half_width(a_l, a_u))
