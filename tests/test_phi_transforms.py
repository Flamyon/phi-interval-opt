# tests for src/phi_transforms.py, subpart a3

import numpy as np
import pytest

from interval_math import centre, half_width, width
from phi_transforms import make_phi, phi_cw, phi_ls, phi_lu, phi_registry

# the coefficient pairs of the three named examples, as [1] prints them.
# lu is example 2.2, page 5, lines 332-336; ls is example 2.3, page 6, lines
# 342-346; cw is example 2.4, page 6, lines 348-353.
named_coefficients = {
    "lu": ((1.0, 0.0), (0.0, 1.0)),
    "ls": ((1.0, 0.0), (-1.0, 1.0)),
    "cw": ((0.5, 0.5), (-0.5, 0.5)),
}


# a random population of one interval objective, lower endpoints and widths both random
def random_interval(size=400, seed=20260831):
    generator = np.random.default_rng(seed)
    f_l = generator.uniform(-10.0, 10.0, size=size)
    f_u = f_l + generator.uniform(0.0, 5.0, size=size)
    return f_l, f_u


# recovers (f_l, f_u) from the two image coordinates by inverting the coefficient matrix
def invert_phi(lam, beta, first, second):
    inverse = np.linalg.inv(np.array([[lam[0], lam[1]], [beta[0], beta[1]]]))
    f_l = inverse[0, 0] * first + inverse[0, 1] * second
    f_u = inverse[1, 0] * first + inverse[1, 1] * second
    return f_l, f_u


# the non-dominated index set of a population of objective rows, usual pareto relation.
# local to this test file on purpose: c1 and d2 own the real one, and a second
# implementation under src/ would be two implementations of the same thing.
def non_dominated_indices(rows):
    keep = np.ones(rows.shape[0], dtype=bool)
    for i in range(rows.shape[0]):
        not_worse = np.all(rows <= rows[i], axis=1)
        strictly_better = np.any(rows < rows[i], axis=1)
        keep[i] = not np.any(not_worse & strictly_better)
    return frozenset(np.flatnonzero(keep).tolist())


# phi_lu is the identity, which is what makes example 2.2 the identity automorphism
def test_phi_lu_is_the_identity():
    f_l, f_u = random_interval()
    first, second = phi_lu(f_l, f_u)
    assert np.array_equal(first, f_l)
    assert np.array_equal(second, f_u)


# phi_cw returns exactly the centre and the half-width of interval_math
def test_phi_cw_is_centre_and_half_width():
    f_l, f_u = random_interval()
    first, second = phi_cw(f_l, f_u)
    assert np.array_equal(first, centre(f_l, f_u))
    assert np.array_equal(second, half_width(f_l, f_u))


# phi_ls returns the lower endpoint and exactly the full width of interval_math
def test_phi_ls_is_lower_endpoint_and_full_width():
    f_l, f_u = random_interval()
    first, second = phi_ls(f_l, f_u)
    assert np.array_equal(first, f_l)
    assert np.array_equal(second, width(f_l, f_u))


# the factor of two that separates example 2.3 from example 2.4
def test_phi_ls_second_coordinate_is_twice_phi_cw_second_coordinate():
    f_l, f_u = random_interval()
    _, second_ls = phi_ls(f_l, f_u)
    _, second_cw = phi_cw(f_l, f_u)
    assert np.array_equal(second_ls, 2.0 * second_cw)
    assert not np.array_equal(second_ls, second_cw)


# a pair singular through a zero column is rejected
def test_make_phi_rejects_a_pair_singular_through_a_zero():
    with pytest.raises(ValueError) as raised:
        make_phi((1.0, 0.0), (2.0, 0.0))
    assert "inadmissible" in str(raised.value)
    assert "1.0" in str(raised.value) and "2.0" in str(raised.value)


# a pair singular only through proportionality, with no zero anywhere, is rejected too
def test_make_phi_rejects_a_pair_singular_through_proportionality():
    with pytest.raises(ValueError) as raised:
        make_phi((2.0, 4.0), (1.0, 2.0))
    assert "inadmissible" in str(raised.value)


# an admissible pair that is not one of the three named examples still constructs and inverts.
# this one is the first component of example 2.1 of [1], page 4, lines 234-262,
# lambda = (0, 1) and beta = (1/2, 1/2). it is a named example of the paper and it
# is deliberately not in phi_registry: it carries no convexity notion.
def test_make_phi_accepts_an_admissible_pair_outside_the_registry():
    lam, beta = (0.0, 1.0), (0.5, 0.5)
    phi = make_phi(lam, beta)
    f_l, f_u = random_interval()
    first, second = phi(f_l, f_u)
    recovered_l, recovered_u = invert_phi(lam, beta, first, second)
    assert np.allclose(recovered_l, f_l)
    assert np.allclose(recovered_u, f_u)
    assert phi not in phi_registry.values()


# the registry holds exactly the three named examples, in the order of [1]
def test_registry_holds_the_three_named_examples_in_order():
    assert list(phi_registry) == ["lu", "ls", "cw"]
    assert phi_registry["lu"] is phi_lu
    assert phi_registry["ls"] is phi_ls
    assert phi_registry["cw"] is phi_cw


# every phi in the registry is invertible, recovering (f_l, f_u) from its image
def test_every_registry_phi_is_invertible():
    f_l, f_u = random_interval()
    for name, phi in phi_registry.items():
        lam, beta = named_coefficients[name]
        first, second = phi(f_l, f_u)
        recovered_l, recovered_u = invert_phi(lam, beta, first, second)
        assert np.allclose(recovered_l, f_l), name
        assert np.allclose(recovered_u, f_u), name


# every instance in the registry comes out of make_phi on the paper's coefficients
def test_every_registry_phi_matches_make_phi_on_the_papers_coefficients():
    f_l, f_u = random_interval()
    for name, phi in phi_registry.items():
        lam, beta = named_coefficients[name]
        rebuilt_first, rebuilt_second = make_phi(lam, beta)(f_l, f_u)
        first, second = phi(f_l, f_u)
        assert np.array_equal(first, rebuilt_first), name
        assert np.array_equal(second, rebuilt_second), name


# every phi returns arrays of the shape of its inputs
def test_every_phi_preserves_shape():
    f_l, f_u = random_interval(size=37)
    for name, phi in phi_registry.items():
        for array in phi(f_l, f_u):
            assert isinstance(array, np.ndarray), name
            assert array.shape == f_l.shape, name


# no phi writes into its arguments
def test_no_phi_mutates_its_inputs():
    f_l, f_u = random_interval()
    before_l, before_u = f_l.copy(), f_u.copy()
    for phi in phi_registry.values():
        phi(f_l, f_u)
    assert np.array_equal(before_l, f_l)
    assert np.array_equal(before_u, f_u)


# a constant-width sample laid out as the 2m real objectives of [1] under one phi
def constant_width_image(phi, crisp, epsilon):
    columns = []
    for objective in range(crisp.shape[1]):
        f_l = crisp[:, objective] - epsilon
        f_u = crisp[:, objective] + epsilon
        first, second = phi(f_l, f_u)
        columns.extend([first, second])
    return np.column_stack(columns)


# the s-06 check: a constant width collapses all three phi to one order.
# a1 established this in exact arithmetic, v-30, and also established that in
# plain double precision the same construction can break it: computing the width
# as f_u - f_l on a generic sample can make the three sets differ through
# rounding alone, r-07. that failure is sample-dependent, not universal, which is
# exactly why it is dangerous and why this test does not rely on a tolerance.
# this test asserts the exact-arithmetic result, the one a1 established as true,
# and it gets exactness by construction rather than by tolerance: the crisp
# values are multiples of 2^-10 below 2 and epsilon is 2^-6, so f - eps, f + eps,
# their difference and their half-sum are all exact doubles and every phi image
# coordinate is computed with no rounding at all.
def test_constant_width_collapses_the_three_phi_to_one_order():
    generator = np.random.default_rng(20260831)
    crisp = generator.integers(0, 1024, size=(200, 2)) / 1024.0
    epsilon = 1.0 / 64.0
    index_sets = {}
    for name, phi in phi_registry.items():
        image = constant_width_image(phi, crisp, epsilon)
        index_sets[name] = non_dominated_indices(image)
    assert index_sets["lu"] == index_sets["ls"] == index_sets["cw"]
    assert index_sets["lu"] == non_dominated_indices(crisp)
    assert 0 < len(index_sets["lu"]) < crisp.shape[0]
