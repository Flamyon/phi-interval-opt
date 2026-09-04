# tests for src/problems_tier1.py, subpart a5

import numpy as np
import pytest

from phi_transforms import phi_registry
from problems_tier1 import (crisp_level, dtlz2_interval, dtlz2_width_drivers,
                            epsilon_levels, problem_registry, zdt1_interval,
                            zdt1_width_drivers)

# the positive levels of docs/a1_uncertainty_model.md part 4. eps = 0 is the
# degenerate baseline and is tested separately, since under it the three phi
# coincide with the crisp order by construction.
positive_levels = tuple(e for e in epsilon_levels if e > 0.0)
# a1's centre-bin count for the width-versus-centre statistic,
# docs/a1_uncertainty_model.md part 1, "20 centre-bins".
centre_bins = 20
# the constructed separation samples, sized in this file's own exploration. the
# grids are small because the non-dominated relation below is quadratic in the
# sample size and is run at four levels on both problems.
zdt1_side = 32
dtlz2_side = 12
# the jitter put into the decision variables that do not drive the width. it is
# small on purpose: it must move the sample off the crisp Pareto set without
# moving it out of the region the set lives in.
zdt1_jitter = 0.01
dtlz2_jitter = 0.02
sample_seed = 20260831
# a5-b's slice sweep, the re-run of docs/a1_uncertainty_model.md part 4. 61 points
# per free axis is a1's own resolution, recovered in a5-b by reproducing every
# published fraction of a1's two tables exactly at that side and at no other; the
# slice grids fewer axes there, so the two sides differ and the point counts are
# comparable rather than equal.
a1_slice_side = 61
sweep_slice_side = {"zdt1_interval": 15, "dtlz2_interval": 8}
# the margin the independence certificate's smallest singular value must clear,
# relative to its largest. it is not a tolerance on a comparison, d-02: nothing
# here compares two objective rows. it is the distance from the rank verdict to
# machine precision, and the measured ratios are 8.4e-03 for zdt1 and 4.1e-03 for
# dtlz2, thirteen orders above it.
certificate_margin = 1e-6


# the non-dominated index set of a population of objective rows, usual pareto relation.
# local to this test file on purpose, for the reason tests/test_problems_tier0.py
# gives: c1 and d2 own the real one and a second implementation under src/ would
# be two implementations of the same thing. no tolerance and no rounding, which
# is CONTEXT.md section 5's rule and costs nothing here, both problems returning
# the representation their intervals are computed in.
def non_dominated_indices(image):
    keep = np.ones(image.shape[0], dtype=bool)
    for i in range(image.shape[0]):
        not_worse = np.all(image <= image[i], axis=1)
        strictly_better = np.any(image < image[i], axis=1)
        keep[i] = not np.any(not_worse & strictly_better)
    return frozenset(np.flatnonzero(keep).tolist())


# the route of one phi record that matches a problem's declared representation
def route_for(problem, record):
    return getattr(record, "of_" + problem.representation)


# the 2m columns of the transformed real problem, phi applied to each objective
def phi_image(problem, x, record, params):
    route = route_for(problem, record)
    columns = []
    for pair in problem.evaluate(x, params):
        first, second = route(*pair)
        columns.append(first)
        columns.append(second)
    return np.stack(columns, axis=-1)


# the m columns of the underlying crisp problem, the interval centres
def crisp_image(problem, x, params):
    route = route_for(problem, phi_registry["cw"])
    return np.stack([route(*pair)[0] for pair in problem.evaluate(x, params)], axis=-1)


# the m centre arrays and the m half-width arrays of a problem, under its own route
def centres_and_half_widths(problem, x, params):
    route = route_for(problem, phi_registry["cw"])
    pairs = [route(*pair) for pair in problem.evaluate(x, params)]
    return [c for c, _ in pairs], [r for _, r in pairs]


# the crisp and the three phi non-dominated sets of one problem over one sample
def efficient_sets(problem, x, params):
    sets = {"crisp": non_dominated_indices(crisp_image(problem, x, params))}
    for name, record in phi_registry.items():
        sets[name] = non_dominated_indices(phi_image(problem, x, record, params))
    return sets


# a1's within-centre-bin width spread, as a fraction of the width span.
# correlation is deliberately not used: a1 part 1 found it unreliable, its
# zero-variance guard firing at one epsilon and not at another, and recorded
# this statistic as one of the two that behaved in every run.
def within_bin_width_spread(centres, widths, n_bins=centre_bins):
    edges = np.linspace(np.min(centres), np.max(centres), n_bins + 1)
    bin_of = np.clip(np.digitize(centres, edges[1:-1]), 0, n_bins - 1)
    spreads = [
        np.max(widths[bin_of == b]) - np.min(widths[bin_of == b])
        for b in range(n_bins)
        if np.count_nonzero(bin_of == b) > 1
    ]
    return float(np.median(spreads) / (np.max(widths) - np.min(widths)))


# the fraction of set a that lies in set b
def containment(a, b):
    return len(a & b) / len(a)


# a uniform random population inside a problem's decision box
def random_population(problem, size=2000, seed=sample_seed):
    generator = np.random.default_rng(seed)
    lower, upper = problem.bounds()
    return generator.uniform(lower, upper, size=(size, problem.n_vars))


# why the separation samples below are constructed and not sampled, and what
# they miss. this is r-08 in tier 1 form and the reasoning is a1's.
# a 30-dimensional box cannot be gridded and a uniform sample of one contains
# essentially nothing near the efficient region: the crisp Pareto set of zdt1 is
# the face x_2 = ... = x_30 = 0, which a uniform sample never approaches, and a
# uniform draw has g near 1 + 9/2 rather than near 1. a1 part 2 measured what
# that costs. it built zdt1 with the half-width eps*x_n, found every
# width-versus-centre statistic healthy and all three phi separating on a uniform
# sample, and then found phi_cw returning exactly the crisp efficient set on the
# slice where the efficient set actually lives. separation measured on a uniform
# sample of a large box is therefore not evidence of separation.
# so each sample is built from the published crisp Pareto set, which both papers
# state in closed form, perturbed along the variable that drives the half-width
# and jittered in the rest:
#   zdt1, [2] definition 4 equation (7) page 177, "the Pareto-optimal front is
#     formed with g(x) = 1", which on x in [0,1]^30 means x_2 = ... = x_30 = 0
#     with x_1 free. x_1 and the width driver x_30 are gridded over [0, 1] and
#     x_2 ... x_29 carry a small uniform jitter.
#   dtlz2, [3] section vii.b equation (9), "the Pareto-optimal solutions
#     corresponds to x_i* = 0.5 (x_i* in x_M)", that is x_3 = ... = x_12 = 0.5
#     with x_1 and x_2 free. x_1, x_2 and the width driver x_12 are gridded over
#     [0, 1] and x_3 ... x_11 carry a small jitter about 0.5.
# what this misses, stated so no result is read past it. it is a low-dimensional
# slice through one region, so every fraction below is a fraction of this sample
# and never of the box, and a phi whose efficient set lay mostly elsewhere would
# be invisible here. it varies one tail variable broadly, the width driver, so a
# difference between the phi driven by some other tail variable would be missed.
# and it says nothing about where the phi-efficient sets are: that is b1's
# derivation and b2's reference fronts, and nothing here is compared against one.


# zdt1's separation sample, built from the crisp Pareto set of [2]
def build_zdt1_sample():
    generator = np.random.default_rng(sample_seed)
    axis = np.linspace(0.0, 1.0, zdt1_side)
    first, driver = np.meshgrid(axis, axis, indexing="ij")
    x = np.zeros((zdt1_side * zdt1_side, zdt1_interval.n_vars))
    x[:, 0] = first.ravel()
    x[:, -1] = driver.ravel()
    x[:, 1:-1] = generator.uniform(0.0, zdt1_jitter, size=(x.shape[0], x.shape[1] - 2))
    return x


# dtlz2's separation sample, built from the crisp Pareto set of [3]
def build_dtlz2_sample():
    generator = np.random.default_rng(sample_seed)
    axis = np.linspace(0.0, 1.0, dtlz2_side)
    first, second, driver = np.meshgrid(axis, axis, axis, indexing="ij")
    x = np.full((dtlz2_side ** 3, dtlz2_interval.n_vars), 0.5)
    x[:, 0], x[:, 1] = first.ravel(), second.ravel()
    x[:, -1] = driver.ravel()
    x[:, 2:-1] = 0.5 + generator.uniform(
        -dtlz2_jitter, dtlz2_jitter, size=(x.shape[0], x.shape[1] - 3))
    return x


sample_builders = {"zdt1_interval": build_zdt1_sample, "dtlz2_interval": build_dtlz2_sample}
# the samples and their efficient sets, built once for the whole module. the
# non-dominated relation is quadratic in the sample size and is wanted at four
# levels on both problems.
sample_cache = {}
sets_cache = {}


# the constructed separation sample of one problem, built once
def sample_of(name):
    if name not in sample_cache:
        sample_cache[name] = sample_builders[name]()
    return sample_cache[name]


# the crisp and three phi non-dominated sets on that sample at one level, built once
def sets_of(name, eps):
    if (name, eps) not in sets_cache:
        problem = problem_registry[name]
        sets_cache[(name, eps)] = efficient_sets(problem, sample_of(name), {"eps": eps})
    return sets_cache[(name, eps)]


# one line of the separation report: sizes, fractions, intersections, containments
# and the two noise counts. a-close-b added cw<ls and ls<cw to the containment
# line and the noise line beneath it, for the reason recorded above the overlap
# test: |ls&cw| was printed here from a5 onward with no containment beside it, so
# a shortfall that is entirely double-precision read as a structural fact. these
# are the numbers that fill the e1 and e2 tables and they carry their own noise
# measure now.
def separation_report(name, eps, sets, total):
    order = ("crisp", "lu", "ls", "cw")
    sizes = " ".join("{} {}".format(k, len(sets[k])) for k in order)
    fractions = " ".join("{} {:.4f}".format(k, len(sets[k]) / total) for k in order)
    pairs = (("lu", "ls"), ("lu", "cw"), ("ls", "cw"))
    meets = " ".join("|{}&{}| {}".format(a, b, len(sets[a] & sets[b])) for a, b in pairs)
    conts = " ".join(
        "{}<{} {:.3f}".format(a, b, containment(sets[a], sets[b]))
        for a, b in (("lu", "ls"), ("ls", "lu"), ("lu", "cw"), ("cw", "lu"),
                     ("crisp", "cw"), ("cw", "ls"), ("ls", "cw"))
    )
    # both containments below are exact in real arithmetic, so every point
    # counted here is a rounding artefact and not a property of the orders. this
    # is the count CONTEXT.md section 10 c3 has the validation gate report.
    noise = " ".join("|{}\\{}| {}".format(a, b, len(sets[a] - sets[b]))
                     for a, b in (("lu", "ls"), ("cw", "ls")))
    return "\n".join(("{} eps={} total={}".format(name, eps, total),
                      "  sizes       " + sizes,
                      "  fractions   " + fractions,
                      "  meets       " + meets,
                      "  containment " + conts,
                      "  noise       " + noise))


# evaluate returns m pairs of arrays shaped like the population, m and not 2m
@pytest.mark.parametrize("problem", [zdt1_interval, dtlz2_interval],
                         ids=["zdt1", "dtlz2"])
def test_evaluate_returns_one_pair_per_interval_objective(problem):
    x = random_population(problem, size=37)
    pairs = problem.evaluate(x, None)
    # the count is m, the number of interval objectives. 2m, four for zdt1 and
    # six for dtlz2, is the number of columns the transformed problem has after
    # phi, and phi is not applied here.
    assert len(pairs) == problem.n_obj
    assert problem.n_obj == (2 if problem.name == "zdt1_interval" else 3)
    for first, second in pairs:
        assert first.shape == (37,)
        assert second.shape == (37,)


# both problems declare the centre and half-width form and are paired with its route
@pytest.mark.parametrize("problem", [zdt1_interval, dtlz2_interval],
                         ids=["zdt1", "dtlz2"])
def test_representation_is_declared_and_has_a_matching_route(problem):
    # CONTEXT.md section 10 a5: tier 1 is built in centre and half-width form
    # from the start and never forms an endpoint, so the declaration is
    # centre_radius and the caller's getattr pairing must find a route.
    assert problem.representation == "centre_radius"
    for record in phi_registry.values():
        assert callable(route_for(problem, record))


# every half-width is non-negative at every level, so every F_i is an interval
@pytest.mark.parametrize("problem", [zdt1_interval, dtlz2_interval],
                         ids=["zdt1", "dtlz2"])
@pytest.mark.parametrize("eps", epsilon_levels)
def test_every_half_width_is_non_negative(problem, eps):
    # r >= 0 is checked as it is computed and is never turned into f_l <= f_u,
    # which would require building the endpoints this module refuses to build.
    x = random_population(problem)
    for _, radii in problem.evaluate(x, {"eps": eps}):
        assert np.all(radii >= 0.0)


# at eps = 0 the half-width is exactly zero, not a cancellation residue
@pytest.mark.parametrize("problem", [zdt1_interval, dtlz2_interval],
                         ids=["zdt1", "dtlz2"])
def test_the_crisp_half_width_is_exactly_zero(problem):
    # both half-widths are eps times a finite non-negative function of x_n, so
    # at eps = 0 they are exactly 0.0 in ieee arithmetic. array_equal and not
    # approx: the point of a5's centre-radius declaration is that this is exact.
    # the consequence, and what CONTEXT.md section 10 a5 asks for: the second
    # image coordinate of example 2.3 of [1], the full width 2r, and of example
    # 2.4, the half-width r, are then identically zero as well.
    x = random_population(problem)
    zero = np.zeros(x.shape[0])
    for _, radii in problem.evaluate(x, {"eps": crisp_level}):
        assert np.array_equal(radii, zero)
    for name in ("ls", "cw"):
        image = phi_image(problem, x, phi_registry[name], {"eps": crisp_level})
        assert np.array_equal(image[:, 1::2], np.zeros_like(image[:, 1::2])), name


# the centres do not depend on the imprecision level, at any level
@pytest.mark.parametrize("problem", [zdt1_interval, dtlz2_interval],
                         ids=["zdt1", "dtlz2"])
def test_the_centres_are_the_published_objectives_at_every_level(problem):
    # docs/a1_uncertainty_model.md part 4, "the crisp limit": the centres are the
    # published f_i at every eps, so the crisp problem is not a limit that is
    # approached but the exact eps = 0 member of the family. bitwise equality,
    # since eps enters no centre expression.
    x = random_population(problem)
    reference = crisp_image(problem, x, {"eps": crisp_level})
    for eps in positive_levels:
        assert np.array_equal(crisp_image(problem, x, {"eps": eps}), reference), eps


# evaluate writes into nothing and returns no view of its argument
@pytest.mark.parametrize("problem", [zdt1_interval, dtlz2_interval],
                         ids=["zdt1", "dtlz2"])
def test_evaluate_does_not_mutate_or_alias_its_argument(problem):
    x = random_population(problem, size=64)
    original = np.copy(x)
    pairs = problem.evaluate(x, {"eps": 0.25})
    assert np.array_equal(x, original)
    # zdt1's first centre is x_1 itself, so this is the one place an alias could
    # be handed back; it is copied for exactly that reason.
    for first, second in pairs:
        assert not np.shares_memory(first, x)
        assert not np.shares_memory(second, x)


# the registry holds both problems under the names the rest of the project uses
def test_problem_registry_holds_both_problems():
    assert problem_registry == {"zdt1_interval": zdt1_interval,
                                "dtlz2_interval": dtlz2_interval}
    assert (zdt1_interval.n_vars, zdt1_interval.n_obj) == (30, 2)
    assert (dtlz2_interval.n_vars, dtlz2_interval.n_obj) == (12, 3)


# both decision boxes are the unit cube the papers state
@pytest.mark.parametrize("problem", [zdt1_interval, dtlz2_interval],
                         ids=["zdt1", "dtlz2"])
def test_bounds_are_the_published_unit_cube(problem):
    # [2] definition 4 equation (7) page 177, "x_i in [0,1]", and [3] section
    # vii.b equation (9), "0 <= x_i <= 1, for i = 1, 2, ..., n".
    lower, upper = problem.bounds()
    assert np.array_equal(lower, np.zeros(problem.n_vars))
    assert np.array_equal(upper, np.ones(problem.n_vars))


# a negative imprecision level is refused, since it would make r negative
def test_a_negative_level_is_refused():
    with pytest.raises(ValueError):
        zdt1_interval.evaluate(random_population(zdt1_interval, size=4), {"eps": -0.01})


# a1 part 4's sweep is the crisp baseline and four positive levels
def test_the_sweep_is_the_crisp_baseline_and_four_positive_levels():
    # docs/a1_uncertainty_model.md part 4, "the levels to sweep":
    # eps in {0, 0.05, 0.10, 0.25, 0.50}.
    assert epsilon_levels == (0.0, 0.05, 0.10, 0.25, 0.50)
    assert crisp_level == 0.0
    assert len(positive_levels) == 4


# zdt1's centres reproduce the published values of [2] at four hand-checked points
def test_zdt1_reproduces_the_published_values():
    # [2] definition 4, equation (7), page 177, with f_2 = g h from equation (6):
    #     f_1 = x_1,  g = 1 + 9 (sum_{i=2}^{30} x_i)/29,  h = 1 - sqrt(f_1/g)
    # hand-computed, the first three on the Pareto set g = 1 and the fourth off it:
    #   x_1 = 0.00, tail 0      g = 1  f_1 = 0.00  f_2 = 1 - 0     = 1.0
    #   x_1 = 0.25, tail 0      g = 1  f_1 = 0.25  f_2 = 1 - 0.5   = 0.5
    #   x_1 = 1.00, tail 0      g = 1  f_1 = 1.00  f_2 = 1 - 1     = 0.0
    #   x_1 = 1.00, tail 1/3    g = 1 + 9 (29/3)/29 = 4, f_2 = 4 (1 - 1/2) = 2.0
    # the fourth is the one that would survive a wrong divisor or a tail that
    # starts at the wrong index: 29 terms of 1/3 give g = 4 exactly only if the
    # sum runs over x_2 ... x_30 and is divided by 29.
    x = np.zeros((4, zdt1_interval.n_vars))
    x[:, 0] = [0.0, 0.25, 1.0, 1.0]
    x[3, 1:] = 1.0 / 3.0
    (centre_1, _), (centre_2, _) = zdt1_interval.evaluate(x, {"eps": crisp_level})
    assert centre_1 == pytest.approx([0.0, 0.25, 1.0, 1.0])
    assert centre_2 == pytest.approx([1.0, 0.5, 0.0, 2.0])


# zdt1's half-width is a1 part 4's quadratic, now once per objective on its driver
def test_zdt1_half_width_matches_a1_part_4():
    # docs/a1_uncertainty_model.md part 4 with a5-b's drivers:
    # r_i = eps ((x_{driver(i)} - 1/2)^2 + 1/20), driver(1) = 30, driver(2) = 29.
    # **the form is a1 part 4's unchanged**; what a5-b moved is which variable
    # each objective reads, so the hand-computed values are a1's own:
    #   driver = 0.0   0.5 (0.25 + 0.05) = 0.150
    #   driver = 0.5   0.5 (0.00 + 0.05) = 0.025, the strictly positive minimum
    #   driver = 1.0   0.5 (0.25 + 0.05) = 0.150
    # the minimum is interior, at the driver's 1/2, which is the whole reason the
    # form is quadratic here: [2]'s g is linear in each of x_29 and x_30 with its
    # optimum on the face 0, and a1 part 4 measured the linear half-width
    # collapsing phi_lu onto phi_ls and phi_cw onto the crisp order.
    # this test asserted r_1 == r_2 until a5-b, which was the defect and not a
    # property: it is now asserted that the two are driven apart.
    x = np.zeros((3, zdt1_interval.n_vars))
    x[:, zdt1_width_drivers[0]] = [0.0, 0.5, 1.0]
    x[:, zdt1_width_drivers[1]] = [0.5, 1.0, 0.0]
    (_, radius_1), (_, radius_2) = zdt1_interval.evaluate(x, {"eps": 0.5})
    assert radius_1 == pytest.approx([0.15, 0.025, 0.15])
    assert radius_2 == pytest.approx([0.025, 0.15, 0.15])
    assert not np.array_equal(radius_1, radius_2)
    assert np.all(radius_1 > 0.0) and np.all(radius_2 > 0.0)


# dtlz2's centres reproduce the published values of [3] at non-uniform points
def test_dtlz2_reproduces_the_published_values_at_non_uniform_points():
    # [3] section vii.b, equation (9), at M = 3:
    #   f_1 = (1+g) cos(x_1 pi/2) cos(x_2 pi/2)
    #   f_2 = (1+g) cos(x_1 pi/2) sin(x_2 pi/2)
    #   f_3 = (1+g) sin(x_1 pi/2)
    # hand-computed with the tail at 0.5, so g = 0 and 1 + g = 1:
    #   (x_1, x_2) = (0, 0)      (1, 0, 0)
    #   (x_1, x_2) = (1, 0)      (0, 0, 1)
    #   (x_1, x_2) = (0, 1)      (0, 1, 0)
    #   (x_1, x_2) = (1/3, 2/3)  (cos30 cos60, cos30 sin60, sin30)
    #                          = (sqrt(3)/4, 3/4, 1/2)
    # the fourth point is the one that catches a swapped sine index. under the
    # wrong reading, f_2 carrying sin(x_1 pi/2) and f_3 carrying sin(x_2 pi/2),
    # it would give (sqrt(3)/4, sqrt(3)/4, sqrt(3)/2), and it would still satisfy
    # the sphere identity, which is why a uniform x_1 = x_2 cannot be relied on.
    x = np.full((4, dtlz2_interval.n_vars), 0.5)
    x[:, 0] = [0.0, 1.0, 0.0, 1.0 / 3.0]
    x[:, 1] = [0.0, 0.0, 1.0, 2.0 / 3.0]
    pairs = dtlz2_interval.evaluate(x, {"eps": crisp_level})
    centres = [centre for centre, _ in pairs]
    root_three_quarter = np.sqrt(3.0) / 4.0
    assert centres[0] == pytest.approx([1.0, 0.0, 0.0, root_three_quarter], abs=1e-15)
    assert centres[1] == pytest.approx([0.0, 0.0, 1.0, 0.75], abs=1e-15)
    assert centres[2] == pytest.approx([0.0, 1.0, 0.0, 0.5], abs=1e-15)


# dtlz2's sphere identity holds at non-uniform decision vectors
def test_dtlz2_sphere_identity_at_non_uniform_vectors():
    # [3] section vii.b: "the Pareto-optimal solutions corresponds to
    # x_i* = 0.5 (x_i* in x_M) and all objective function values must satisfy
    # the sum_{m=1}^{M} (f_m*)^2 = 1". off that set the same algebra gives
    # sum f_m^2 = (1 + g)^2, cos^2 + sin^2 = 1 twice over.
    # the sample is uniform in x_1 and x_2 and therefore non-uniform: a vector
    # with x_1 = x_2 satisfies the identity under a swapped sine index too, so a
    # uniform one would hide exactly the error this checks for.
    x = random_population(dtlz2_interval, size=500)
    assert np.all(x[:, 0] != x[:, 1])
    tail = x[:, dtlz2_interval.n_obj - 1:]
    scale = 1.0 + np.sum(np.square(tail - 0.5), axis=-1)
    for eps in epsilon_levels:
        centres = crisp_image(dtlz2_interval, x, {"eps": eps})
        assert np.sum(np.square(centres), axis=-1) == pytest.approx(np.square(scale))
    # and on the published Pareto set itself, where the sum is 1.
    on_set = np.full((200, dtlz2_interval.n_vars), 0.5)
    on_set[:, 0] = np.linspace(0.0, 1.0, 200)
    on_set[:, 1] = np.linspace(1.0, 0.0, 200)
    centres = crisp_image(dtlz2_interval, on_set, {"eps": crisp_level})
    assert np.sum(np.square(centres), axis=-1) == pytest.approx(np.ones(200))


# dtlz2's half-width is a1 part 4's linear form, now once per objective
def test_dtlz2_half_width_matches_a1_part_4():
    # docs/a1_uncertainty_model.md part 4 with a5-b's drivers: r_i = eps
    # x_{driver(i)}, driver(1) = 12, driver(2) = 11, driver(3) = 10. linear and
    # not quadratic because [3]'s g is already quadratic in each of x_10, x_11
    # and x_12 with an interior optimum at 1/2, so a half-width whose optimum is
    # at 0 already differs from it; the quadratic form would put the two optima
    # together and give back the crisp order under phi_cw.
    # this test asserted r_1 == r_2 == r_3 until a5-b, which was the defect.
    x = np.full((3, dtlz2_interval.n_vars), 0.5)
    x[:, dtlz2_width_drivers[0]] = [0.0, 0.5, 1.0]
    x[:, dtlz2_width_drivers[1]] = [1.0, 0.0, 0.5]
    x[:, dtlz2_width_drivers[2]] = [0.5, 1.0, 0.0]
    radii = [radius for _, radius in dtlz2_interval.evaluate(x, {"eps": 0.25})]
    assert radii[0] == pytest.approx([0.0, 0.125, 0.25])
    assert radii[1] == pytest.approx([0.25, 0.0, 0.125])
    assert radii[2] == pytest.approx([0.125, 0.25, 0.0])
    for first in range(len(radii)):
        for second in range(first + 1, len(radii)):
            assert not np.array_equal(radii[first], radii[second]), (first, second)


# the width varies within a centre bin, which is CONTEXT.md section 5 step 1's condition
@pytest.mark.parametrize("problem", [zdt1_interval, dtlz2_interval],
                         ids=["zdt1", "dtlz2"])
@pytest.mark.parametrize("eps", positive_levels)
def test_the_width_varies_within_a_centre_bin(problem, eps):
    # step 1's necessary condition, checked as an assertion and not assumed: if
    # the width were constant or a function of the centre alone, the image in the
    # (centre, width) plane would be a curve, every injective phi would map it to
    # another monotone curve and the three orders would coincide.
    # the statistic is a1's within-bin spread as a fraction of the width span and
    # not a correlation, for the reason a1 part 1 records. it is measured on a
    # uniform sample of the box, which is where a1 measured it; the separation
    # test below is the one that may not use a uniform sample.
    # the statistic is invariant in eps, both the spread and the span scaling
    # with it, so the level only has to be positive for the span to be non-zero.
    x = random_population(problem, size=5000)
    centres, radii = centres_and_half_widths(problem, x, {"eps": eps})
    for objective, (centre, radius) in enumerate(zip(centres, radii)):
        assert within_bin_width_spread(centre, 2.0 * radius) >= 0.9, objective


# the same condition on the constructed separation sample, where it matters most
@pytest.mark.parametrize("name", sorted(problem_registry), ids=sorted(problem_registry))
def test_the_width_varies_within_a_centre_bin_on_the_constructed_sample(name):
    # a1 part 2's failure was a problem passing this on a uniform sample and
    # collapsing on the slice, so the statistic is repeated where the separation
    # claim is actually made. the width driver is gridded independently of the
    # variables that move the centres, so the spread is the full span here.
    problem = problem_registry[name]
    centres, radii = centres_and_half_widths(problem, sample_of(name), {"eps": 0.10})
    for objective, (centre, radius) in enumerate(zip(centres, radii)):
        assert within_bin_width_spread(centre, 2.0 * radius) >= 0.9, objective


# at eps = 0 the three phi and the crisp order give the same set, which is the degeneracy
@pytest.mark.parametrize("name", sorted(problem_registry), ids=sorted(problem_registry))
def test_the_crisp_level_collapses_the_three_phi_onto_the_crisp_order(name):
    # CONTEXT.md section 10 a5 and docs/a1_uncertainty_model.md part 4: at eps = 0
    # half of the transformed objectives are constant and the three phi coincide
    # with each other and with the crisp order. phi_lu's image is then (c, c) in
    # each objective, a duplicated column, and phi_ls's and phi_cw's are (c, 0).
    # this is asserted so that the baseline is labelled by a test and not only by
    # a comment: it is the degenerate member of the family and not a data point.
    sets = sets_of(name, crisp_level)
    assert sets["lu"] == sets["crisp"]
    assert sets["ls"] == sets["crisp"]
    assert sets["cw"] == sets["crisp"]


# the separation test: the three phi give three different sets on a sample that
# is not saturated, at every positive level of a1 part 4's sweep
# the separation report is a large-sample diagnostic, so it is marked slow. the
# slice check s-07 and r-08 rest on is the constructed-sample width test above,
# which is cheap and stays in the fast run.
@pytest.mark.slow
@pytest.mark.parametrize("name", sorted(problem_registry), ids=sorted(problem_registry))
@pytest.mark.parametrize("eps", positive_levels)
def test_the_three_phi_separate_on_the_constructed_sample(name, eps, capsys):
    sets = sets_of(name, eps)
    total = sample_of(name).shape[0]
    with capsys.disabled():
        print(separation_report(name, eps, sets, total))
    crisp, lu, ls, cw = (sets[k] for k in ("crisp", "lu", "ls", "cw"))
    # the three orders give three different sets, and none of them is the crisp
    # order. this is what the sensitivity study needs to exist at all.
    assert len({lu, ls, cw}) == 3
    for phi_set in (lu, ls, cw):
        assert phi_set != crisp
    # the saturation guard, and the reason it is a fraction and not a size. with
    # 2m = 4 and 2m = 6 real objectives almost any sample can come out mutually
    # incomparable, and then all three phi return the whole sample, agree with
    # each other for a reason that has nothing to do with the orders, and the
    # separation statistic measures nothing. that outcome fails here.
    for key in ("lu", "ls", "cw"):
        assert 0.02 < len(sets[key]) / total < 0.95, key
    # the crisp order on m columns is far from saturated on the same sample,
    # which is the sharper form of the same guard.
    assert len(crisp) / total < 0.25
    assert len(crisp) < min(len(lu), len(ls), len(cw))


# phi_lu's efficient set inside phi_ls's, the direction r-06 predicts and a1-b
# measured at containment 1.000 on tier 0. in exact arithmetic that containment
# is a theorem and not an observation, and so is the same containment for phi_cw:
# docs/a_close_containment.md states the criterion once, that phi_B = M phi_A
# with M entrywise non-negative and invertible makes phi_A-dominance imply
# phi_B-dominance and so puts ND_B inside ND_A, and both follow from it, M being
# [[1, 0], [1, 1]] from phi_ls to phi_lu and [[1, 1/2], [0, 1/2]] from phi_ls to
# phi_cw. phi_ls's non-dominated set is therefore the largest of the three and
# contains the other two. the project does not build on that; it is s-11 to the
# supervisors and this comment records why the numbers below look as they do.
# in doubles neither containment is exact, and the two fail by different amounts
# for a reason worth stating. phi_cw's route is (c, r) with coefficients 1 and 0,
# so it commits no arithmetic at all, while phi_ls's and phi_lu's shared first
# coordinate is computed as c - r and rounds. so every rounded tie in c - r is a
# chance for a phi_cw point to leave the phi_ls set, and the phi_lu set, which is
# built on the same rounded column, mostly moves with it. measured here, and
# printed on the report's noise line: |cw \ ls| is 7, 13, 28 and 39 on dtlz2 and
# 0 at every level on zdt1, while |lu \ ls| is 0 everywhere except the single
# point of v-46. a-close-b checked all 39 of the eps = 0.50 points directly:
# every one is dominated under phi_ls in doubles by a named point and none of
# them is dominated exactly, and the same 39 are non-dominated under phi_cw
# exactly. they sit at x_1 = 1, where the first centre is (1 + g) cos(pi/2) =
# 6.1e-17 against a half-width of 0.5, so c - r absorbs differences of order
# 1e-18 that phi_cw's untouched centre column keeps. it is a cancellation inside
# phi's own first coordinate and not a round trip, and no representation choice
# open to a5 removes it, the centre being what [3] prints.
# only the phi_lu band is asserted, at 0.99 against the 0.9994 measured, and no
# assertion is added for phi_cw: the containments are awaiting s-11 and a test
# that asserted one would be building on it. the numbers are reported instead.
# the pairwise structure of the same three sets, split off to keep the two tests
# short; both read the same cached sets and neither recomputes anything
@pytest.mark.parametrize("name", sorted(problem_registry), ids=sorted(problem_registry))
@pytest.mark.parametrize("eps", positive_levels)
def test_the_separation_sets_overlap_without_coinciding(name, eps):
    sets = sets_of(name, eps)
    crisp, lu, ls, cw = (sets[k] for k in ("crisp", "lu", "ls", "cw"))
    # every pair overlaps and no pair coincides, so each pairwise intersection is
    # non-empty and strictly smaller than the union.
    for first, second in ((lu, ls), (lu, cw), (ls, cw)):
        assert 0 < len(first & second) < len(first | second)
    # phi_lu inside phi_ls, the direction stated above.
    assert len(lu) < len(ls)
    assert containment(lu, ls) >= 0.99
    # phi_cw nested with phi_lu in neither direction. strict inequalities only.
    assert 0.0 < containment(lu, cw) < 1.0
    assert 0.0 < containment(cw, lu) < 1.0
    # the crisp set inside phi_cw's. phi_cw's image columns are the crisp columns
    # plus the m width columns, and adding a column can only lose a dominating
    # point unless it ties on every crisp column, which no pair in this sample
    # does. it is asserted rather than assumed for that reason.
    assert containment(crisp, cw) == 1.0


# phi_lu's efficient set grows with the level and phi_cw's does not move
@pytest.mark.parametrize("name", sorted(problem_registry), ids=sorted(problem_registry))
def test_phi_lu_is_the_sensitive_order_and_phi_cw_is_the_stable_one(name):
    # docs/a1_uncertainty_model.md part 4: "phi_lu is the sensitive one", its
    # efficient set growing from 11% to 51% of the zdt1 slice and from 11% to 85%
    # of the dtlz2 slice as eps runs over the sweep, while phi_cw is stable.
    # the ordering is asserted, never the fractions.
    sizes = [len(sets_of(name, eps)["lu"]) for eps in positive_levels]
    assert sizes == sorted(sizes) and sizes[0] < sizes[-1]
    # phi_cw's stability is exact and not merely observed: its image is
    # (c_i, r_i) with r_i = eps w_i(x_n), so raising eps scales the m width
    # columns by one positive constant, and dominance is invariant under that.
    # so the set is literally the same at every positive level.
    reference = sets_of(name, positive_levels[0])["cw"]
    for eps in positive_levels[1:]:
        assert sets_of(name, eps)["cw"] == reference, eps


# a5-b, and the reason the check below is symbolic and not a sample.
#
# what has to be proved. no two of the 2m image columns of a problem coincide as
# functions, under any of the three phi. that is the property a5 as built did not
# have: with one width function per problem, r_1 and r_2 were the same function,
# so under example 2.3 the columns 2r_1 and 2r_2 were one column written twice
# and under example 2.4 r_1 and r_2 were. the transformed problem then had three
# effective objectives where it appeared to have four, and four where it appeared
# to have six, and the count depended on which phi was applied.
#
# why a sample cannot prove it. finding two columns that differ at some sampled
# points shows they differ there and says nothing about the rest of the box; and
# a sample that found no difference would not prove coincidence either. what is
# wanted is a statement about the functions, so the argument is about the
# functions.
#
# the argument, in two steps.
#
# first, symbolically. src/phi_transforms.py's centre-radius route applies to
# each objective i the matrix
#     [ lam_1 + lam_2   lam_2 - lam_1  ]
#     [ beta_1 + beta_2 beta_2 - beta_1 ]
# to the pair (c_i, r_i), and its determinant is 2 (lam_1 beta_2 - lam_2 beta_1),
# twice [1]'s own, so it is non-zero exactly when the pair is admissible. so each
# image column is a fixed linear combination of the 2m base functions
# c_1, ..., c_m, r_1, ..., r_m, with a known coefficient vector. two columns of
# different objectives have disjoint support, and their coefficient vectors are
# distinct because an invertible matrix has no zero row; the two columns of one
# objective have the two rows of that matrix as their coefficient vectors, and
# those are distinct because an invertible matrix has no repeated row. **so the
# 2m coefficient vectors are pairwise distinct for every admissible phi**, which
# is a statement about [1]'s admissibility condition and not about these two
# problems.
#
# second, the one thing that is not symbolic. if two columns with distinct
# coefficient vectors were equal as functions, their difference would be a
# non-zero linear combination of c_1, ..., c_m, r_1, ..., r_m vanishing
# identically, that is a linear dependence among the base functions. so the whole
# question reduces to: **are the 2m base functions linearly independent?** under
# a5 as built they were not, r_1 - r_2 being identically zero, and that single
# dependence is the entire defect. the certificate below settles the question the
# way linear independence is settled: a matrix of the 2m functions evaluated at
# stated points, of full rank. a full-rank matrix proves independence outright,
# and it is a witness and not a sample -- one such matrix suffices and no number
# of extra points would strengthen it.
#
# the points are written out below rather than drawn, so the certificate is the
# same object on every run and can be checked by hand.


# the 2m base functions c_1..c_m, r_1..r_m of one problem at stated points
def base_function_values(problem, x, eps):
    pairs = problem.evaluate(x, {"eps": eps})
    return np.stack([centre for centre, _ in pairs] + [radius for _, radius in pairs],
                    axis=-1)


# zdt1's witness points: eight decision vectors, written out and not drawn
def zdt1_witness_points():
    # the four coordinates that matter are x_1, which is c_1; any tail variable
    # that is not a driver, here x_2, which moves g and therefore c_2 alone; and
    # the two drivers x_30 and x_29. everything else is zero, so the vectors sit
    # on and near [2]'s crisp Pareto set where the efficient set lives.
    x = np.zeros((8, zdt1_interval.n_vars))
    x[:, 0] = [0.0, 0.25, 0.5, 0.75, 1.0, 0.125, 0.375, 0.625]
    x[:, 1] = [0.0, 0.0, 0.25, 0.5, 0.75, 1.0, 0.5, 0.25]
    x[:, zdt1_width_drivers[1]] = [0.0, 0.25, 0.5, 0.75, 1.0, 0.5, 0.0, 1.0]
    x[:, zdt1_width_drivers[0]] = [1.0, 0.0, 0.75, 0.25, 0.5, 0.125, 1.0, 0.0]
    return x


# dtlz2's witness points: twelve decision vectors, written out and not drawn
def dtlz2_witness_points():
    # x_1 and x_2 are [3]'s two angles and move the three centres; x_3 is a tail
    # variable that is not a driver and moves 1 + g; x_12, x_11 and x_10 are the
    # three drivers. the rest sit at 0.5, which is [3]'s own Pareto value for the
    # tail.
    x = np.full((12, dtlz2_interval.n_vars), 0.5)
    x[:, 0] = np.linspace(0.0, 1.0, 12)
    x[:, 1] = np.linspace(1.0, 0.0, 12)
    x[:, 2] = np.linspace(0.0, 0.5, 12)
    x[:, dtlz2_width_drivers[2]] = np.tile([0.0, 0.25, 0.75, 1.0], 3)
    x[:, dtlz2_width_drivers[1]] = np.tile([1.0, 0.5, 0.0, 0.25], 3)
    x[:, dtlz2_width_drivers[0]] = np.tile([0.25, 1.0, 0.5, 0.0], 3)
    return x


witness_points = {"zdt1_interval": zdt1_witness_points,
                  "dtlz2_interval": dtlz2_witness_points}


# the rank of a value matrix and how far that verdict sits from machine precision
def independence_certificate(values):
    singular = np.linalg.svd(values, compute_uv=False)
    return int(np.linalg.matrix_rank(values)), float(singular[-1] / singular[0])


# the 2m base functions are linearly independent, which is a5-b's whole point
@pytest.mark.parametrize("name", sorted(problem_registry), ids=sorted(problem_registry))
@pytest.mark.parametrize("eps", positive_levels)
def test_the_base_functions_are_linearly_independent(name, eps):
    # the second step of the argument above. full rank proves independence, and
    # with the coefficient vectors pairwise distinct for every admissible phi it
    # proves that no two image columns coincide, under any phi and not only the
    # three in the registry.
    problem = problem_registry[name]
    values = base_function_values(problem, witness_points[name](), eps)
    rank, ratio = independence_certificate(values)
    assert rank == 2 * problem.n_obj
    assert ratio > certificate_margin, ratio


# the certificate fails on a5's shared width function, which is why it is here
@pytest.mark.parametrize("name", sorted(problem_registry), ids=sorted(problem_registry))
def test_the_certificate_rejects_the_shared_width_a5_b_replaced(name):
    # CONTEXT.md section 11: a test that guards a branch must demonstrate the
    # branch was entered. a certificate that passed whatever it was handed would
    # be no certificate, so a5's own construction is rebuilt here, one width
    # function repeated across the objectives, and it must fail. the rank it
    # returns is the effective column count docs/plan_after_meeting.md section b4
    # states: three where zdt1 appears to have four and four where dtlz2 appears
    # to have six.
    problem = problem_registry[name]
    values = base_function_values(problem, witness_points[name](), 0.10)
    shared = np.copy(values)
    for objective in range(1, problem.n_obj):
        shared[:, problem.n_obj + objective] = shared[:, problem.n_obj]
    rank, _ = independence_certificate(shared)
    assert rank == 2 * problem.n_obj - (problem.n_obj - 1)
    assert rank < 2 * problem.n_obj


# every objective's half-width is driven by its own decision variable
@pytest.mark.parametrize("name", sorted(problem_registry), ids=sorted(problem_registry))
def test_each_objective_has_its_own_width_driver(name):
    # a5-b. moving one driver moves that objective's half-width and no other's,
    # and moves no centre at all except through g, which is what makes the m
    # width columns m different functions. the drivers are distinct indices and
    # none of them is x_1 or, on dtlz2, x_2: those carry the centres.
    problem = problem_registry[name]
    drivers = {"zdt1_interval": zdt1_width_drivers,
               "dtlz2_interval": dtlz2_width_drivers}[name]
    assert len(set(drivers)) == problem.n_obj
    assert all(driver >= problem.n_obj for driver in drivers)
    base = witness_points[name]()
    radii = [radius for _, radius in problem.evaluate(base, {"eps": 0.25})]
    for moved, driver in enumerate(drivers):
        x = np.copy(base)
        # 0.5 is the driver value at which zdt1's quadratic half-width is
        # stationary, so the move is made from it to a value that is not, which
        # is where a difference has to appear if the driver is read at all.
        x[:, driver] = 0.9
        after = [radius for _, radius in problem.evaluate(x, {"eps": 0.25})]
        assert not np.array_equal(after[moved], radii[moved]), moved
        for other in range(problem.n_obj):
            if other != moved:
                assert np.array_equal(after[other], radii[other]), (moved, other)


# a5-b's slice sweep, the re-run of docs/a1_uncertainty_model.md part 4.
#
# what a1 part 4's slice was and why it has to change. a1 fixed the whole tail and
# gridded two axes: for zdt1 x_1 and x_30 with x_2 ... x_29 = 0, which is [2]'s
# crisp Pareto set with the width driver freed; for dtlz2 x_1 and x_12 with
# x_2 = 0.5 and x_3 ... x_11 = 0.5, which is [3]'s. a5-b gives the second and
# third objectives their own drivers, and a1's slice pins every one of them: x_29
# at 0 on zdt1 and x_10, x_11 at 0.5 on dtlz2. run on a1's slice the new forms
# would have constant half-widths on all but the first objective, so the slice
# gains one axis per new driver. **that is forced by the change and is not a
# choice about it**: a slice that froze the new drivers would measure the old
# problem.
#
# so three arms are reported, and the middle one is what makes the comparison a
# comparison. arm 1 is a1's own slice with a5's shared width, which reproduces
# a1's published table exactly at side 61 and is the check that this harness is
# a1's procedure and not a new one. arm 2 is a5's shared width on the new slice
# and arm 3 is a5-b's drivers on the same slice, so the two differ in the width
# form alone and the added axes cancel between them.
#
# the fractions move with the grid resolution -- a5-b measured phi_lu's zdt1
# fraction at 0.2441, 0.1435 and 0.0769 for sides 32, 61 and 128 at one eps -- so
# arm 1's numbers are comparable with a1's and arms 2 and 3 with each other, and
# never arm 1 with arm 3.


# a1 part 4's own slice, the crisp Pareto set with the single width driver freed
def a1_slice(name, side):
    axis = np.linspace(0.0, 1.0, side)
    first, driver = np.meshgrid(axis, axis, indexing="ij")
    problem = problem_registry[name]
    fill = 0.0 if name == "zdt1_interval" else 0.5
    x = np.full((side * side, problem.n_vars), fill)
    x[:, 0] = first.ravel()
    x[:, -1] = driver.ravel()
    return x


# the same slice with one axis per width driver, which a5-b's forms require
def sweep_slice(name, side):
    problem = problem_registry[name]
    drivers = {"zdt1_interval": zdt1_width_drivers,
               "dtlz2_interval": dtlz2_width_drivers}[name]
    axes = np.meshgrid(*[np.linspace(0.0, 1.0, side)] * (1 + len(drivers)),
                       indexing="ij")
    fill = 0.0 if name == "zdt1_interval" else 0.5
    x = np.full((side ** (1 + len(drivers)), problem.n_vars), fill)
    x[:, 0] = axes[0].ravel()
    for driver, values in zip(drivers, axes[1:]):
        x[:, driver] = values.ravel()
    return x


# the shared-width image of a problem, a5 as built, for the sweep's middle arm
def shared_width_image(problem, x, record, eps):
    # a5's construction rebuilt from a5-b's: every objective takes the first
    # objective's half-width, which is what one width function per problem meant.
    # nothing in src/ is changed to produce it and it exists only here.
    pairs = problem.evaluate(x, {"eps": eps})
    shared = tuple((centre, pairs[0][1]) for centre, _ in pairs)
    columns = []
    for pair in shared:
        first, second = record.of_centre_radius(*pair)
        columns.extend((first, second))
    return np.stack(columns, axis=-1)


# the crisp and three phi non-dominated sets on a stated slice, either width form
def slice_sets(problem, x, eps, shared=False):
    pairs = problem.evaluate(x, {"eps": eps})
    sets = {}
    for name, record in phi_registry.items():
        image = (shared_width_image(problem, x, record, eps) if shared
                 else phi_image(problem, x, record, {"eps": eps}))
        sets[name] = non_dominated_indices(image)
    crisp = np.stack([centre for centre, _ in pairs], axis=-1)
    sets["crisp"] = non_dominated_indices(crisp)
    return sets


# one row of a1 part 4's slice table: the three fractions, the two flags, the extents
def sweep_row(x, sets, drivers, total):
    fractions = " ".join("{} {:.4f}".format(k, len(sets[k]) / total)
                         for k in ("lu", "ls", "cw"))
    flags = "lu==ls {} cw==crisp {}".format(sets["lu"] == sets["ls"],
                                            sets["cw"] == sets["crisp"])
    extents = " ".join(
        "{} x_{} [{:.2f},{:.2f}]".format(k, driver + 1,
                                         np.min(x[sorted(sets[k]), driver]),
                                         np.max(x[sorted(sets[k]), driver]))
        for k in ("lu", "cw") for driver in drivers[:1])
    return "  {}  {}  {}".format(fractions, flags, extents)


# a5-b's forms separate the three phi on the slice where the efficient set lives
@pytest.mark.slow
@pytest.mark.parametrize("name", sorted(problem_registry), ids=sorted(problem_registry))
def test_the_new_width_forms_pass_a1_part_4_s_slice_sweep(name, capsys):
    # this is the check r-08 and s-07 exist for, and it is the risk a5-b actually
    # carries: a1 measured a zdt1 width that passed every uniform-sample statistic
    # and still handed phi_cw the crisp efficient set on the slice where the
    # solutions live. so the new forms are checked on and near the efficient
    # region and not on a uniform draw of the box.
    # the verdict, per problem and per phi, is the four conditions below, and they
    # are a1 part 4's own: three distinct sets, none of them the crisp set,
    # phi_lu not collapsed onto phi_ls, and none of them the whole slice. the
    # rejected linear form of a1 part 4 failed the middle two at every level.
    problem = problem_registry[name]
    drivers = {"zdt1_interval": zdt1_width_drivers,
               "dtlz2_interval": dtlz2_width_drivers}[name]
    x = sweep_slice(name, sweep_slice_side[name])
    lines = ["{} sweep slice, {} points, {} axes".format(name, len(x), 1 + len(drivers))]
    for eps in positive_levels:
        shared = slice_sets(problem, x, eps, shared=True)
        distinct = slice_sets(problem, x, eps, shared=False)
        lines.append("  eps {}".format(eps))
        lines.append("    a5 shared  " + sweep_row(x, shared, drivers, len(x)))
        lines.append("    a5-b own   " + sweep_row(x, distinct, drivers, len(x)))
        for key in ("lu", "ls", "cw"):
            assert distinct[key] != distinct["crisp"], (eps, key)
            assert 0.0 < len(distinct[key]) / len(x) < 1.0, (eps, key)
        assert len({distinct["lu"], distinct["ls"], distinct["cw"]}) == 3, eps
        assert distinct["lu"] != distinct["ls"], eps
    with capsys.disabled():
        print("\n".join(lines))


# the harness reproduces a1 part 4's published table on a1's own slice
@pytest.mark.slow
@pytest.mark.parametrize("name", sorted(problem_registry), ids=sorted(problem_registry))
def test_the_sweep_harness_reproduces_a1_part_4(name, capsys):
    # arm 1, and it is what makes the re-run a re-run. a1's script was a throwaway
    # and is not in the repository, so the only evidence that this harness is a1's
    # procedure is that it returns a1's numbers: with a5's shared width, on a1's
    # two-axis slice, at side 61, every fraction of both published tables comes
    # back to the four decimals a1 printed. the levels below are a1's own, which
    # for zdt1 include 1.00 and for dtlz2 begin at 0.02, and are not this
    # project's sweep.
    problem = problem_registry[name]
    published = {
        "zdt1_interval": {0.05: (0.1105, 0.5281, 0.5082), 0.10: (0.1435, 0.5284, 0.5082),
                          0.25: (0.3701, 0.5286, 0.5082), 0.50: (0.4700, 0.5286, 0.5082),
                          1.00: (0.5133, 0.5286, 0.5082)},
        "dtlz2_interval": {0.02: (0.1121, 0.5560, 0.5082), 0.05: (0.1814, 0.5907, 0.5082),
                           0.10: (0.2706, 0.6353, 0.5082), 0.25: (0.4964, 0.7482, 0.5082),
                           0.50: (0.8517, 0.9258, 0.5082)},
    }[name]
    x = a1_slice(name, a1_slice_side)
    lines = ["{} a1's slice, {} points, side {}".format(name, len(x), a1_slice_side)]
    for eps, expected in published.items():
        sets = slice_sets(problem, x, eps, shared=True)
        measured = tuple(round(len(sets[k]) / len(x), 4) for k in ("lu", "ls", "cw"))
        lines.append("    eps {:<5} measured {} published {}".format(eps, measured,
                                                                    expected))
        assert measured == expected, (eps, measured, expected)
    with capsys.disabled():
        print("\n".join(lines))
