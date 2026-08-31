# tests for src/problems_tier0.py, subpart a4

import numpy as np
import pytest

from interval_math import centre, half_width, width
from phi_transforms import phi_registry
from problems_tier0 import p0, p0_anchor, p1, problem_registry

# a1-b's grid for p1, docs/a1_uncertainty_model.md a1-b: 61 x 61 on the box,
# 3721 points, and the 0.1 margin it widens the efficient region by.
grid_side = 61
slice_margin = 0.1
# a1's centre-bin count for the width-versus-centre statistic,
# docs/a1_uncertainty_model.md part 1, "seed = 20260831, sample = 5000 uniform
# points, 20 centre-bins".
centre_bins = 20


# a uniform random population inside a problem's decision box
def random_population(problem, size=500, seed=20260831):
    generator = np.random.default_rng(seed)
    lower, upper = problem.bounds()
    return generator.uniform(lower, upper, size=(size, problem.n_vars))


# a regular grid over a box, one array of points with the decision variables last
def grid_points(lower, upper, n_side=grid_side):
    axes = [np.linspace(lower[k], upper[k], n_side) for k in range(len(lower))]
    mesh = np.meshgrid(*axes, indexing="ij")
    return np.stack([axis.ravel() for axis in mesh], axis=-1)


# the 2m columns of the transformed real problem, phi applied to each objective
def phi_image(problem, x, phi, params=None):
    columns = []
    for f_l, f_u in problem.evaluate(x, params):
        first, second = phi(f_l, f_u)
        columns.append(first)
        columns.append(second)
    return np.stack(columns, axis=-1)


# the m columns of the underlying crisp problem, the interval centres
def crisp_image(problem, x, params=None):
    return np.stack([centre(f_l, f_u) for f_l, f_u in problem.evaluate(x, params)], axis=-1)


# the non-dominated index set of a population of objective rows, usual pareto relation.
# local to this test file on purpose, as in tests/test_phi_transforms.py: c1 and
# d2 own the real one and a second implementation under src/ would be two
# implementations of the same thing.
# the rows are rounded first, and that is r-07 and not a convenience. the second
# image coordinate of phi_ls and phi_cw is a subtraction of the two endpoints,
# and (c + r) - (c - r) is not exactly 2r in doubles once delta = 1/10 has made r
# inexact, so two points sharing a width by construction can differ in it by an
# ulp. left alone that noise makes dominated points survive: on the box grid it
# added 9 points to phi_ls and 17 to phi_cw, all of them at x_1 < 0 and all
# strictly dominated in every coordinate by the point above them at x_1 = 0.
# nine decimals is far below the smallest real gap on these grids, which is a
# multiple of 1/3600, and far above the noise. with it the box grid reproduces
# a1-b's published counts exactly: 31 crisp, 460 lu, 1505 ls, 961 cw.
def non_dominated_indices(image, decimals=9):
    rows = np.round(image, decimals)
    keep = np.ones(rows.shape[0], dtype=bool)
    for i in range(rows.shape[0]):
        not_worse = np.all(rows <= rows[i], axis=1)
        strictly_better = np.any(rows < rows[i], axis=1)
        keep[i] = not np.any(not_worse & strictly_better)
    return frozenset(np.flatnonzero(keep).tolist())


# the crisp and the three phi non-dominated sets of one problem over one point set
def efficient_sets(problem, x, params=None):
    sets = {"crisp": non_dominated_indices(crisp_image(problem, x, params))}
    for name, phi in phi_registry.items():
        sets[name] = non_dominated_indices(phi_image(problem, x, phi, params))
    return sets


# a1's within-centre-bin width spread, as a fraction of the width span.
# correlation is deliberately not used: a1 part 1 found it unreliable, its
# zero-variance guard firing at one epsilon and not at another, and recorded the
# span and this statistic as the two that behaved in every run.
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


# a1-b's 61 x 61 grid over p1's whole decision box
@pytest.fixture(scope="module")
def p1_box_grid():
    lower, upper = p1.bounds()
    return grid_points(lower, upper)


# the crisp and three phi non-dominated sets on that box grid
@pytest.fixture(scope="module")
def p1_box_sets(p1_box_grid):
    return efficient_sets(p1, p1_box_grid)


# a1-b's re-grid: the union bounding box of the three phi efficient sets on the
# box, widened by the margin, re-gridded at the same resolution
@pytest.fixture(scope="module")
def p1_slice_grid(p1_box_grid, p1_box_sets):
    union = sorted(p1_box_sets["lu"] | p1_box_sets["ls"] | p1_box_sets["cw"])
    points = p1_box_grid[np.array(union)]
    lower = np.min(points, axis=0) - slice_margin
    upper = np.max(points, axis=0) + slice_margin
    return grid_points(lower, upper)


# the crisp and three phi non-dominated sets on the re-grid, which is what r-08 asks for
@pytest.fixture(scope="module")
def p1_slice_sets(p1_slice_grid):
    return efficient_sets(p1, p1_slice_grid)


# evaluate returns m pairs of arrays shaped like the population, m and not 2m
@pytest.mark.parametrize("problem", [p0, p1], ids=["p0", "p1"])
def test_evaluate_returns_one_pair_per_interval_objective(problem):
    x = random_population(problem, size=37)
    pairs = problem.evaluate(x, None)
    # the count is m, the number of interval objectives. 2m is the number of
    # columns the transformed problem has after phi, and phi is not applied here.
    assert len(pairs) == problem.n_obj
    assert problem.n_obj == 2
    for f_l, f_u in pairs:
        assert f_l.shape == (37,)
        assert f_u.shape == (37,)


# both problems return legitimate intervals everywhere in their box
@pytest.mark.parametrize("problem", [p0, p1], ids=["p0", "p1"])
def test_lower_endpoint_never_exceeds_upper_endpoint(problem):
    x = random_population(problem, size=2000)
    for f_l, f_u in problem.evaluate(x, None):
        assert np.all(f_l <= f_u)


# the registry holds both problems under the names the rest of the project uses
def test_problem_registry_holds_both_problems():
    assert problem_registry == {"p0": p0, "p1": p1}
    assert (p0.n_vars, p0.n_obj) == (1, 2)
    assert (p1.n_vars, p1.n_obj) == (2, 2)


# p0 reproduces [1]'s worked function at the anchor and at two hand-checked points
def test_p0_reproduces_the_published_function():
    # [1] lines 752-753: F_1(x) = [-|x|, |x|], F_2(x) = [0, x^2]. hand-checked:
    #   x =  0     F_1 = [ 0.0, 0.0 ]   F_2 = [0, 0.00]
    #   x =  2     F_1 = [-2.0, 2.0 ]   F_2 = [0, 4.00]
    #   x = -0.5   F_1 = [-0.5, 0.5 ]   F_2 = [0, 0.25]
    # every value here is an exact double, so the comparison is exact.
    x = np.array([[0.0], [2.0], [-0.5]])
    (first_lower, first_upper), (second_lower, second_upper) = p0.evaluate(x, None)
    assert np.array_equal(first_lower, np.array([0.0, -2.0, -0.5]))
    assert np.array_equal(first_upper, np.array([0.0, 2.0, 0.5]))
    assert np.array_equal(second_lower, np.array([0.0, 0.0, 0.0]))
    assert np.array_equal(second_upper, np.array([0.0, 4.0, 0.25]))


# p0's params argument is accepted and ignored, since p0 has no imprecision level
def test_p0_ignores_params():
    x = random_population(p0, size=50)
    without = p0.evaluate(x, None)
    with_params = p0.evaluate(x, {"rho": 0.5, "delta": 0.2})
    for (a_l, a_u), (b_l, b_u) in zip(without, with_params):
        assert np.array_equal(a_l, b_l)
        assert np.array_equal(a_u, b_u)


# p0's box holds the published anchor point strictly inside, not on a face
def test_p0_bounds_contain_the_anchor_in_the_interior():
    lower, upper = p0.bounds()
    assert np.all(lower < p0_anchor)
    assert np.all(p0_anchor < upper)
    # example 3.9's condition (15) is unconstrained stationarity, so b1 needs the
    # anchor interior with room around it, not merely feasible. r-04 records that
    # the hypotheses fail there anyway, which is a separate matter from the box.
    assert np.min(np.minimum(p0_anchor - lower, upper - p0_anchor)) >= 1.0
    # the box carries negative values, which CONTEXT.md section 10 a4 requires.
    assert np.all(lower < 0.0)


# p1's centres and half-widths match hand-computed values at three points
def test_p1_centres_and_half_widths_at_three_points():
    # a1-b: c_1 = x_1^2 + (x_2-1)^2, c_2 = (x_1-1)^2 + (x_2-1)^2,
    # r_1 = x_2^2/4 + 1/10, r_2 = x_1^2/4 + 1/10. hand-computed:
    #   x = ( 0.0, 0.0)   c = (1.0, 2.0)   r = (0.1000, 0.1000)
    #   x = ( 1.0, 1.0)   c = (1.0, 0.0)   r = (0.3500, 0.3500)
    #   x = (-0.5, 1.5)   c = (0.5, 2.5)   r = (0.6625, 0.1625)
    # the third point is the corner where a1-b measures the largest half-width on
    # the box, 0.6625, and the pair (0.6625, 0.1625) is the design's asymmetry:
    # r_1 is driven by x_2 and r_2 by x_1, so they differ at the same point.
    x = np.array([[0.0, 0.0], [1.0, 1.0], [-0.5, 1.5]])
    (f1_l, f1_u), (f2_l, f2_u) = p1.evaluate(x, None)
    assert centre(f1_l, f1_u) == pytest.approx([1.0, 1.0, 0.5])
    assert centre(f2_l, f2_u) == pytest.approx([2.0, 0.0, 2.5])
    assert half_width(f1_l, f1_u) == pytest.approx([0.1, 0.35, 0.6625])
    assert half_width(f2_l, f2_u) == pytest.approx([0.1, 0.35, 0.1625])


# p1's half-width stays strictly positive on the box, over a1-b's measured range
def test_p1_half_width_is_strictly_positive_on_the_box(p1_box_grid):
    # a1-b, "phi-separation on the box": half-width range [0.1000, 0.6625]. a
    # width that reached zero would put the second image coordinate of phi_ls and
    # phi_cw into the cancellation regime of r-07.
    for f_l, f_u in p1.evaluate(p1_box_grid, None):
        radii = half_width(f_l, f_u)
        assert np.min(radii) == pytest.approx(0.1)
        assert np.max(radii) == pytest.approx(0.6625)
        assert np.all(radii > 0.0)


# p1's width varies within a centre bin, which is step 1's independence condition
def test_p1_width_varies_within_a_centre_bin(p1_box_grid):
    # a1-b measures 0.966 of the span for both objectives on the box. the
    # assertion is a floor well under that, so the test states the property and
    # not the number.
    for f_l, f_u in p1.evaluate(p1_box_grid, None):
        fraction = within_bin_width_spread(centre(f_l, f_u), width(f_l, f_u))
        assert fraction >= 0.9


# the same independence check near the efficient region, which is the s-07 slice
def test_p1_width_varies_within_a_centre_bin_near_the_efficient_region(p1_slice_grid):
    # a1-b measures 0.987 and 0.895 of the span here, the two objectives no longer
    # agreeing because the modified design is not symmetric in x_1 and x_2.
    for f_l, f_u in p1.evaluate(p1_slice_grid, None):
        fraction = within_bin_width_spread(centre(f_l, f_u), width(f_l, f_u))
        assert fraction >= 0.85


# the r-08 check: the three phi separate on and near the efficient region
def test_the_three_phi_give_distinct_sets_near_the_efficient_region(p1_slice_grid, p1_slice_sets):
    # why the slice and not a uniform sample of the box. a1 part 2 built zdt1 with
    # half-width eps*x_n, which passes every width-versus-centre statistic and
    # separates all three phi on a uniform sample, |phi_cw| = 86 against
    # |crisp| = 24. on the slice where the efficient set actually lives, phi_cw
    # returned the crisp efficient set exactly. a uniform sample of a large box
    # contains almost nothing near the efficient set, so separation measured on
    # one is not evidence of separation at all. that is r-08, and the procedure
    # here is a1-b's answer to it: grid the box, take the non-dominated set under
    # each phi, take the union bounding box with a margin, re-grid there.
    # sizes and containment fractions are asserted, never exact counts, so the
    # test does not break when the grid resolution changes.
    total = p1_slice_grid.shape[0]
    crisp, lu, ls, cw = (p1_slice_sets[k] for k in ("crisp", "lu", "ls", "cw"))
    assert len({lu, ls, cw}) == 3
    for name in ("lu", "ls", "cw"):
        assert p1_slice_sets[name] != crisp
        assert 0.02 < len(p1_slice_sets[name]) / total < 0.95
    # a1-b's slice fractions are 0.195, 0.671 and 0.430, so the ordering
    # |crisp| < |lu| < |cw| < |ls| holds with a wide gap at every step.
    assert len(crisp) < len(lu) < len(cw) < len(ls)
    # phi_lu strictly inside phi_ls, the direction r-06 predicts and a1-b measures
    # at containment 1.000 on both the box and the slice.
    assert lu < ls
    assert containment(lu, ls) == 1.0
    # phi_cw nested with phi_lu in neither direction, a1-b measuring 0.420 and
    # 0.190 on the slice. strict inequalities only, no numbers.
    assert 0.0 < containment(lu, cw) < 1.0
    assert 0.0 < containment(cw, lu) < 1.0
