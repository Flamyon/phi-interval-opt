# tests for src/problems_tier1.py, subpart a5

import numpy as np
import pytest

from phi_transforms import phi_registry
from problems_tier1 import (crisp_level, dtlz2_interval, epsilon_levels,
                            problem_registry, zdt1_interval)

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


# zdt1's half-width is a1 part 4's quadratic in x_n, at three hand-checked points
def test_zdt1_half_width_matches_a1_part_4():
    # docs/a1_uncertainty_model.md part 4: r = eps ((x_n - 1/2)^2 + 1/20), one
    # function for both objectives. hand-computed at eps = 0.5:
    #   x_n = 0.0   0.5 (0.25 + 0.05) = 0.150
    #   x_n = 0.5   0.5 (0.00 + 0.05) = 0.025, the strictly positive minimum
    #   x_n = 1.0   0.5 (0.25 + 0.05) = 0.150
    # the minimum is interior, at x_n = 1/2, which is the whole reason the form
    # is quadratic here: [2]'s g is linear in x_n with its optimum on the face
    # x_n = 0, and a1 part 4 measured the linear half-width collapsing phi_lu
    # onto phi_ls and phi_cw onto the crisp order.
    x = np.zeros((3, zdt1_interval.n_vars))
    x[:, -1] = [0.0, 0.5, 1.0]
    (_, radius_1), (_, radius_2) = zdt1_interval.evaluate(x, {"eps": 0.5})
    assert radius_1 == pytest.approx([0.15, 0.025, 0.15])
    assert np.array_equal(radius_1, radius_2)
    assert np.all(radius_1 > 0.0)


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


# dtlz2's half-width is a1 part 4's linear function of x_n
def test_dtlz2_half_width_matches_a1_part_4():
    # docs/a1_uncertainty_model.md part 4: r = eps x_n, one function for all
    # three objectives. linear and not quadratic because [3]'s g is already
    # quadratic in x_n with an interior optimum at x_n = 1/2, so a half-width
    # whose optimum is at 0 already differs from it; the quadratic form would put
    # the two optima together and give back the crisp order under phi_cw.
    x = np.full((3, dtlz2_interval.n_vars), 0.5)
    x[:, -1] = [0.0, 0.5, 1.0]
    radii = [radius for _, radius in dtlz2_interval.evaluate(x, {"eps": 0.25})]
    assert radii[0] == pytest.approx([0.0, 0.125, 0.25])
    for radius in radii[1:]:
        assert np.array_equal(radius, radii[0])


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
