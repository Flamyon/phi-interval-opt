# tests for src/interval_math.py, subpart a2

import numpy as np

from interval_math import add, centre, gh_difference, half_width, scalar_multiply, width


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
