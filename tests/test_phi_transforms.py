# tests for src/phi_transforms.py, subpart a3

import numpy as np
import pytest

from interval_math import centre, half_width, width
from phi_transforms import (make_phi, make_phi_of_centre_radius, make_phi_pair,
                            phi_cw, phi_ls, phi_lu, phi_registry)

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
    assert phi not in [record.of_endpoints for record in phi_registry.values()]


# the registry holds exactly the three named examples, in the order of [1]
def test_registry_holds_the_three_named_examples_in_order():
    assert list(phi_registry) == ["lu", "ls", "cw"]
    assert phi_registry["lu"].of_endpoints is phi_lu
    assert phi_registry["ls"].of_endpoints is phi_ls
    assert phi_registry["cw"].of_endpoints is phi_cw
    for name, record in phi_registry.items():
        assert record.name == name
        assert (record.lam, record.beta) == named_coefficients[name]


# every phi in the registry is invertible, recovering (f_l, f_u) from its image
def test_every_registry_phi_is_invertible():
    f_l, f_u = random_interval()
    for name, record in phi_registry.items():
        lam, beta = named_coefficients[name]
        first, second = record.of_endpoints(f_l, f_u)
        recovered_l, recovered_u = invert_phi(lam, beta, first, second)
        assert np.allclose(recovered_l, f_l), name
        assert np.allclose(recovered_u, f_u), name


# every instance in the registry comes out of make_phi on the paper's coefficients
def test_every_registry_phi_matches_make_phi_on_the_papers_coefficients():
    f_l, f_u = random_interval()
    for name, record in phi_registry.items():
        lam, beta = named_coefficients[name]
        rebuilt_first, rebuilt_second = make_phi(lam, beta)(f_l, f_u)
        first, second = record.of_endpoints(f_l, f_u)
        assert np.array_equal(first, rebuilt_first), name
        assert np.array_equal(second, rebuilt_second), name


# every phi returns arrays of the shape of its inputs
def test_every_phi_preserves_shape():
    f_l, f_u = random_interval(size=37)
    for name, record in phi_registry.items():
        for array in record.of_endpoints(f_l, f_u):
            assert isinstance(array, np.ndarray), name
            assert array.shape == f_l.shape, name


# no phi writes into its arguments
def test_no_phi_mutates_its_inputs():
    f_l, f_u = random_interval()
    before_l, before_u = f_l.copy(), f_u.copy()
    for record in phi_registry.values():
        record.of_endpoints(f_l, f_u)
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
    for name, record in phi_registry.items():
        image = constant_width_image(record.of_endpoints, crisp, epsilon)
        index_sets[name] = non_dominated_indices(image)
    assert index_sets["lu"] == index_sets["ls"] == index_sets["cw"]
    assert index_sets["lu"] == non_dominated_indices(crisp)
    assert 0 < len(index_sets["lu"]) < crisp.shape[0]


# a random (centre, half_width) population, both drawn independently
def random_centre_radius(size=400, seed=20260901):
    generator = np.random.default_rng(seed)
    return generator.uniform(-10.0, 10.0, size=size), generator.uniform(0.0, 5.0, size=size)


# a (centre, half_width) population on a dyadic grid, so every value is exact in binary
def dyadic_centre_radius(size=400, seed=20260901):
    # multiples of 2^-6 with magnitudes below 2^7, so c, r, c - r and c + r are
    # all exact doubles and every product by the registry's coefficients, which
    # are 0, +-1/2 and +-1, is exact too.
    generator = np.random.default_rng(seed)
    c = generator.integers(-8192, 8193, size=size) / 64.0
    r = generator.integers(0, 8193, size=size) / 64.0
    return c, r


# the composite is phi composed with the endpoint map, which is what makes it the same phi
def test_the_centre_radius_route_is_phi_composed_with_the_endpoint_map():
    # f_l = c - r and f_u = c + r, so applying the endpoint route to (c - r, c + r)
    # must give what the centre-radius route gives on (c, r), for any admissible
    # coefficients and not only for the three named ones. the pair below is
    # example 2.1 of [1], page 4, lines 234-262, which is deliberately not in the
    # registry.
    c, r = random_centre_radius()
    for lam, beta in list(named_coefficients.values()) + [((0.0, 1.0), (0.5, 0.5))]:
        composed = make_phi(lam, beta)(c - r, c + r)
        direct = make_phi_of_centre_radius(lam, beta)(c, r)
        assert np.allclose(direct[0], composed[0])
        assert np.allclose(direct[1], composed[1])


# the composite determinant is twice the paper's, so the two agree on admissibility
def test_the_composite_determinant_is_twice_the_paper_determinant():
    # [1] page 3, line 172 requires lam_1 beta_2 != lam_2 beta_1. the composite
    # with M = [[1, -1], [1, 1]] has matrix
    #   [[lam_1 + lam_2, lam_2 - lam_1], [beta_1 + beta_2, beta_2 - beta_1]]
    # whose determinant works out to 2 (lam_1 beta_2 - lam_2 beta_1), det M being
    # 2. so the composite is singular exactly when the paper's condition fails,
    # and testing admissibility on lam and beta is testing it for both routes.
    generator = np.random.default_rng(20260901)
    for _ in range(200):
        lam_1, lam_2, beta_1, beta_2 = generator.integers(-8, 9, size=4) / 4.0
        paper = lam_1 * beta_2 - lam_2 * beta_1
        composite = (lam_1 + lam_2) * (beta_2 - beta_1) - (lam_2 - lam_1) * (beta_1 + beta_2)
        assert composite == pytest.approx(2.0 * paper)
        assert (composite == 0.0) == (paper == 0.0)


# the two routes agree on a random sample, for every phi in the registry
def test_the_two_routes_agree_on_a_random_sample():
    c, r = random_centre_radius()
    for name, record in phi_registry.items():
        endpoint = record.of_endpoints(c - r, c + r)
        exact = record.of_centre_radius(c, r)
        assert np.allclose(exact[0], endpoint[0]), name
        assert np.allclose(exact[1], endpoint[1]), name


# the two routes agree bitwise on a dyadic sample, for every phi in the registry
def test_the_two_routes_agree_bitwise_on_a_dyadic_sample():
    # on a dyadic sample there is no rounding to disagree about, so agreement is
    # exact rather than close. this is the case a4-b part 2 identified: where the
    # arithmetic is exact the two routes are the same doubles, and where it is not
    # they are not, which is the whole reason the route is declared per problem.
    c, r = dyadic_centre_radius()
    for name, record in phi_registry.items():
        endpoint = record.of_endpoints(c - r, c + r)
        exact = record.of_centre_radius(c, r)
        assert np.array_equal(exact[0], endpoint[0]), name
        assert np.array_equal(exact[1], endpoint[1]), name


# phi_cw's centre-radius route returns the centre and the half-width untouched
def test_phi_cw_of_centre_radius_is_the_identity():
    # example 2.4 has lam = (1/2, 1/2) and beta = (-1/2, 1/2), so its composite is
    # ((1/2 + 1/2) c + (1/2 - 1/2) r, (-1/2 + 1/2) c + (1/2 + 1/2) r) = (c, r),
    # the identity, with determinant 1 = 2 * (1/2). so on this route the centre
    # and the half-width are not computed at all, they are passed through.
    c, r = random_centre_radius()
    first, second = phi_registry["cw"].of_centre_radius(c, r)
    assert np.array_equal(first, c)
    assert np.array_equal(second, r)


# phi_ls's centre-radius route reads the full width without ever subtracting
def test_phi_ls_of_centre_radius_returns_twice_the_half_width():
    # example 2.3 has lam = (1, 0) and beta = (-1, 1), so its composite second
    # coordinate is (beta_1 + beta_2) c + (beta_2 - beta_1) r = 0 c + 2 r.
    c, r = random_centre_radius()
    first, second = phi_registry["ls"].of_centre_radius(c, r)
    assert np.array_equal(first, c - r)
    assert np.array_equal(second, 2.0 * r)


# both constructors reject an inadmissible pair, on the paper's lam and beta
def test_both_routes_reject_an_inadmissible_pair():
    for build in (make_phi, make_phi_of_centre_radius):
        with pytest.raises(ValueError, match="inadmissible coefficients"):
            build((1.0, 2.0), (2.0, 4.0))
    with pytest.raises(ValueError, match="inadmissible coefficients"):
        make_phi_pair("bad", (1.0, 2.0), (2.0, 4.0))


# the registry is not callable, so a route cannot be used by mistake for the other
def test_a_registry_entry_is_not_callable():
    # the record has to be asked for a named route. this is the guard the module
    # comment describes: crossing the two routes is what a4-b measured the cost of.
    f_l, f_u = random_interval()
    for name, record in phi_registry.items():
        with pytest.raises(TypeError):
            record(f_l, f_u)
        assert callable(record.of_endpoints) and callable(record.of_centre_radius)
