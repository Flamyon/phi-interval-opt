# phi-interval-opt: verified facts

moved out of PROGRESS.md in session a1-b, unchanged. this file is the project's
record of claims checked against a source. numbering continues here and numbers
are never reused. the rows are in the order they stood in PROGRESS.md, which is
not strictly numeric: v-29 was appended after v-33 by a0-b and stays there.

highest number in use: v-56.

claims read from a paper in this project, with their location. a claim moves here
only once it has been checked against the source, and once here it may be relied on
without re-checking. anything not on this list is not established.

format:

    v-nn | claim | paper | location | verified in | date

line numbers are lines of papers/new_preference_order_relationships_paper.txt.
pages are the printed journal pages. every row below was checked against the
paper in a0; the transcriptions are in docs/a0_framework.md.

v-01 | the class of admissible automorphisms acts componentwise on endpoint pairs,
    each component the map phi_i(x_2i-1, x_2i) = (lambda_2i-1 x_2i-1 + lambda_2i
    x_2i, beta_2i-1 x_2i-1 + beta_2i x_2i) | [1] | section 2, unnumbered display,
    page 3, lines 163-171 | a0 | 2026-08-31

v-02 | admissibility is exactly lambda_2i-1 beta_2i != lambda_2i beta_2i-1 for
    every i; no further condition on the coefficients appears anywhere in sections
    2 or 3 | [1] | section 2, page 3, lines 171-172, restated page 6, lines
    398-399 | a0 | 2026-08-31

v-03 | the coefficients are real numbers "that can be chosen according to a
    decision", and the semantics of the problem are "implicitly expressed by the
    values ... which can be chosen by a decision maker" | [1] | section 2, page 3,
    line 171; section 3, page 6, lines 397-401 | a0 | 2026-08-31

v-04 | the preference order is defined through the injective phi-bar from the
    m-tuples of intervals into R^2m; for this class the order on R^2m is
    componentwise and the relation decomposes objective by objective | [1] |
    definition 2.1, page 2, lines 123-134; eq (2), page 3, lines 175-176; eq (3),
    page 3, lines 179-184 | a0 | 2026-08-31

v-05 | m interval objectives give 2m real objectives: phi-bar o F maps S into
    R^2m and the transformed problem is (13), min (phi-bar o F)(x) | [1] | eq (12)
    line 511, composition display lines 517-532, eq (13) line 537, page 8 | a0 |
    2026-08-31

v-06 | example 2.2 has lambda = (1, 0), beta = (0, 1), gives (f_l, f_u), and its
    phi-convexity coincides with LU-convexity | [1] | example 2.2, page 5, lines
    332-336 | a0 | 2026-08-31

v-07 | example 2.3 has lambda = (1, 0), beta = (-1, 1), gives (f_l, f_u - f_l),
    the full width with no factor of one half, and its phi-convexity coincides
    with LS-convexity | [1] | example 2.3, page 6, lines 342-346 | a0 | 2026-08-31

v-08 | example 2.4 has lambda = (1/2, 1/2), beta = (-1/2, 1/2), gives
    ((f_l + f_u)/2, (f_u - f_l)/2), centre and half-width, and its phi-convexity
    coincides with CW-convexity | [1] | example 2.4, page 6, lines 348-353 | a0 |
    2026-08-31

v-09 | definition 3.1 gives three solution concepts for the minimisation problem,
    strong or strict optimal through the relation of eq (3), optimal through eq
    (6), weak optimal through eq (7), with the implication chain strong or strict
    => optimal => weak optimal | [1] | definition 3.1, page 6, lines 371-374;
    implication display, page 6, line 394 | a0 | 2026-08-31

v-10 | theorem 3.1: x-bar is an optimal (weakly optimal) solution for 1MIOP_phi if
    and only if it is an efficient (weakly efficient) solution for min (phi-bar o
    F)(x). its only hypotheses are phi in the class, S in R^n and F
    multi-interval-valued: no convexity, no differentiability, no constraint
    qualification | [1] | theorem 3.1, page 8, lines 545-546 | a0 | 2026-08-31

v-11 | theorem 3.2: x-bar is an optimal (weak optimal) solution for 2MIOP_phi if
    and only if it is an efficient (weakly efficient) solution for MOP_(-phi),
    with -phi and MOP_(-phi) defined inside the proof | [1] | theorem 3.2, page 9,
    lines 584-586; -phi and MOP_(-phi), lines 588-595 | a0 | 2026-08-31

v-12 | theorem 3.3: F is phi-convex if and only if Lambda_i^T f and B_i^T f are
    convex for all i, where Lambda_i^T f = lambda_2i-1 f_l + lambda_2i f_u and
    B_i^T f = beta_2i-1 f_l + beta_2i f_u | [1] | theorem 3.3, page 9, lines
    638-641; the two coordinates, lines 647 and 656 | a0 | 2026-08-31

v-13 | remark 2.2 is the pointwise form of theorem 3.3: F is phi-convex at x* if
    and only if those same two combinations are convex at x*. this is the form
    examples 3.4 to 3.7 need, since they assume phi-convexity at x-bar and not
    globally | [1] | remark 2.2, page 5, lines 319-327 | a0 | 2026-08-31

v-14 | example 3.8 has four numbered statements. the standing condition on the
    weights of (14) is w in R^2m, w_i >= 0 for all i, and the 2m weights summing
    to one. statement 2 strengthens it to w_i > 0 for all i; statement 3
    strengthens the solution to unique rather than the weights; statement 4 is the
    converse under S convex and F phi-convex and returns weights that may have
    zero components | [1] | example 3.8, page 10, lines 682-706 | a0 | 2026-08-31

v-15 | example 3.9 requires Lambda_i^T f and B_i^T f to be differentiable for all
    i, and requires nothing of f_l and f_u. note that this is not a usable
    weakening: each phi_i is invertible, so the two pairs are differentiable
    together for every admissible phi | [1] | example 3.9 hypotheses, page 10,
    lines 709-711 | a0 | 2026-08-31

v-16 | example 3.9 has three numbered statements, not four. 1 and 2 are the
    necessary and sufficient pair for weak optimal solutions; 3 is sufficient
    only, for optimal solutions, under w_i > 0 for all i. no necessary condition
    for optimal solutions is given there | [1] | example 3.9, page 10, lines
    712-730 | a0 | 2026-08-31

v-17 | condition (15) is the vanishing at x-bar of the gradient of the single
    real-valued function sum over i of (w_2i-1 Lambda_i^T f + w_2i B_i^T f), which
    is exactly the objective of the scalar problem (14) of example 3.8 | [1] | eq
    (15), page 10, lines 715-723 | a0 | 2026-08-31

v-18 | the worked function [1] gives after example 3.9 is F : R -> (C)^2 with
    F_1(x) = [-|x|, |x|] and F_2(x) = [0, x^2]; so n = 1, m = 2, S = R | [1] |
    page 11, lines 752-753 | a0 | 2026-08-31

v-19 | the paper's only stated conclusion about that function is that x = 0 is a
    strict minimum for F under the order relation of the phi of example 2.2. no
    proof is given, and nothing is said about its efficient set under any phi |
    [1] | page 11, lines 753-755 | a0 | 2026-08-31

v-20 | for that function the paper states only that the aggregate sum over i of
    (Lambda_i^T f + B_i^T f) equals x^2, is differentiable and convex, and has
    vanishing gradient at 0, "which is a version of condition (15)". the
    individual image coordinates Lambda_1^T f = -|x| and B_1^T f = |x| are not
    differentiable at 0, so example 3.9's own hypotheses fail there | [1] | page
    11, lines 756-769 | a0 | 2026-08-31

v-21 | example 2.1 is a further named example of a phi in section 2, with m = 4
    and fully explicit coefficients per component: lambda = (0, 1) beta =
    (1/2, 1/2); lambda = (-1, 1) beta = (0, -1); lambda = (-1/2, 1/2) beta =
    (0, -1); lambda = (-1, 0) beta = (0, -1). it is the only place in [1] where
    one phi carries different coefficients in different components, and the only
    place in sections 2 and 3 with negative coefficients. it carries no convexity
    notion and no optimality condition | [1] | example 2.1, page 4, lines 234-262
    | a0 | 2026-08-31

v-22 | the examples of section 3 introduce no phi of their own. 3.1 and 3.4 use
    example 2.2; 3.2 and 3.7 use example 2.3; 3.3, 3.5 and 3.6 use example 2.4;
    3.8 and 3.9 hold for arbitrary phi in the class | [1] | pages 6, 7 and 10,
    lines 406, 415, 420, 430-431, 448-449, 464-465, 486-487, 682, 709 | a0 |
    2026-08-31

v-23 | the conclusion of [1] gives a further explicit automorphism, unnumbered and
    not an example: phi(x_1, x_2) = (-x_1, x_2), that is lambda = (-1, 0),
    beta = (0, 1), which it says coincides with the inclusion order; and it states
    that this order "would be a better option than" the order of example 2.2 for a
    decision maker wanting an ordered quasilinear interval space | [1] | section
    6, page 20, lines 1510-1515 | a0 | 2026-08-31
    corrected in a0-b: a0 cited this as page 19. the page 19 footer is at line
    1505 and the passage begins at line 1509, so it is page 20. the line numbers
    were right. see also v-29, which adds the m = 1 restriction a0 did not record.

v-24 | proposition 5.1: for the fuzzy problems, if x-bar is an optimal solution
    for (1MFIOP_phi) with phi the automorphism of example 2.2, then x-bar is also
    an optimal solution for (1MFIOP_psi) with psi the automorphism of example 2.3.
    so the solution set under example 2.2 is contained in the solution set under
    example 2.3: the LS set is the larger one and contains the LU one. hypotheses
    are only that both problems share S and F-tilde and that x-bar is optimal
    under example 2.2. no convexity, no differentiability, no constraint
    qualification, no structure on S. it is stated for the optimal solution
    concept of definition 5.1(2) only, not for strong or strict and not for weak,
    and no converse is stated | [1] | proposition 5.1, page 19, lines 1481-1487;
    remark 5.1, lines 1489-1494; proof deferred to appendix A, page 22, lines
    1664-1685 | a0-b | 2026-08-31

v-25 | example 2.4, this project's phi_cw, appears in no statement of [1]
    relating its solution set to that of any other automorphism. proposition 5.1
    and remark 5.1 name only examples 2.2 and 2.3 | [1] | established by
    exhaustive search of the whole file; method recorded in docs/a0_framework.md
    c17 | a0-b | 2026-08-31

v-26 | sections 2 and 3 of [1] contain no stated relation between the solution
    sets of two different automorphisms, and no interval-space analogue of
    proposition 5.1. every result there fixes one phi: examples 3.1 to 3.3 relate
    one phi to a formulation in the literature, examples 3.4 to 3.7 give a
    condition under one phi, theorems 3.1 to 3.3 concern one phi, and examples 3.8
    and 3.9 hold for an arbitrary but fixed phi | [1] | sections 2 and 3, lines
    99-771; search method recorded in docs/a0_framework.md c17 | a0-b | 2026-08-31

v-27 | theorem 5.1 is where [1] states the relationship between the fuzzy and the
    interval formulations: for phi in the class, x-bar is a (local) strong or
    strict, optimal, or weak optimal solution for the fuzzy problem (23) if and
    only if it is one for the interval problem (25), min [F-tilde]_alpha(x), for
    all alpha in [0, 1]. its only hypothesis is phi in the class. the interval
    side is a family indexed by alpha, not a single interval problem, and the
    theorem covers all three solution concepts where proposition 5.1 covers one |
    [1] | theorem 5.1, page 16, lines 1207-1223 | a0-b | 2026-08-31

v-28 | the fuzzy order is the interval order applied at every alpha-level:
    definition 4.1 and equation (18) define the fuzzy preference relation by
    requiring the relation of equation (3) to hold on the alpha-cuts for all alpha
    in [0, 1], and proposition 4.1 derives its partial-order property directly
    from proposition 2.2 | [1] | definition 4.1, page 12, lines 851-862; eq (18),
    lines 865-872; proposition 4.1, lines 875-878 | a0-b | 2026-08-31

v-30 | a constant half-width collapses phi_lu, phi_ls and phi_cw to one order and
    to the crisp order. on zdt1 (n=30, m=2) and dtlz2 (n=12, m=3) at eps in
    {0.05, 0.5}, over 5000 uniform points, all four non-dominated index sets are
    identical, not merely equal in size. this is CONTEXT.md section 5 step 1's
    constant-width clause, confirmed | project diagnostic, not a paper |
    docs/a1_uncertainty_model.md part 1, exact arithmetic, seed 20260831 | a1 |
    2026-08-31

v-31 | a half-width that is an exact function of the centre collapses all three
    phi to the crisp order too, even when the width is far from constant.
    proportional imprecision f -> [f(1-eps), f(1+eps)] on zdt1 at eps in
    {0.10, 0.25} gives width spans of 0.84 and 2.19, correlation +1.0000, and all
    four index sets identical. this is step 1's "function of the centre alone"
    clause, confirmed | project diagnostic | docs/a1_uncertainty_model.md part 2
    (c) | a1 | 2026-08-31

v-32 | multiplicative coefficient imprecision makes the half-width an exact linear
    function of the centre for any objective that is a monomial in the imprecise
    coefficient. on zdt1 with f1 = c1*x1, c1 in [1-d, 1+d], objective 1 gives
    correlation +1.0000 and phi_cw returns the crisp non-dominated set exactly, at
    d = 0.10 and d = 0.25 | project diagnostic | docs/a1_uncertainty_model.md part
    2 (b) | a1 | 2026-08-31

v-33 | all six image coordinates of a problem are convex under all three phi if
    and only if (centre - half_width) is convex and half_width is convex, since
    centre + half_width and centre are non-negative combinations of those two.
    this is the design rule p1 is built to | derived from [1] theorem 3.3 and the
    coefficients of examples 2.2, 2.3 and 2.4, verified in a0 as v-06 to v-08 and
    v-12 | docs/a1_uncertainty_model.md part 3 | a1 | 2026-08-31

v-29 | the conclusion's "better option" claim about the inclusion-order
    automorphism is conditional and not general. it is stated for the case m = 1
    and under the antecedent "if one of the objectives of a decision making is to
    model an interval optimization problem aiming to use properties of an ordered
    quasilinear interval space". the criterion is axiom (q.11) of definition 2.1
    in [1]'s reference [23], which the order of example 2.2 fails, with the
    counterexample alpha = 1, beta = -1, x = [-1, 1], and which the inclusion
    order satisfies. it is structural, not empirical, and compares no solution
    sets. this refines v-23 | [1] | conclusion, page 20, lines 1503 and 1509-1516
    | a0-b | 2026-08-31

v-34 | the interval arithmetic of [1] is: [a_l, a_u] + [b_l, b_u] = [a_l + b_l,
    a_u + b_u], and lam . [a_l, a_u] = [lam a_l, lam a_u] if lam >= 0 and
    [lam a_u, lam a_l] if lam < 0. the sign rule is printed as a two-case brace,
    so the endpoint swap is part of the definition and not a convention this
    project added. [1] attributes both operations to its own reference [21] | [1]
    | section 2, page 2, lines 101-106 | a2 | 2026-08-31

v-35 | [1] never defines a centre, a midpoint, a width, a radius or a
    gh-difference, and never uses those words. the only place those quantities
    appear is as image coordinates of examples 2.3 and 2.4. so centre, half_width
    and width have their definitions in [1] only through those two examples, and
    the gh-difference has no source in [1] at all | [1] | established by
    exhaustive search of the whole file for hukuhara, gh, midpoint, center,
    centre, width and radius, case-insensitive, zero hits | a2 | 2026-08-31

v-36 | pymoo 0.6.2 runs correctly under numpy 2.5.2. nsga2 and mopso_cd both
    complete on a 3-variable, 4-objective problem with bounds off the unit box,
    both are bit-identical across two runs at the same seed and differ across
    seeds, and the hv and igd indicators d1 needs return finite values. zero
    warnings of any kind were raised. the only numpy-2.0-removed alias anywhere in
    the installed package is np.NaN inside a comment in vendor/vendor_cmaes.py,
    which is single-objective and not used by c2. so the c2 pin needs no numpy
    ceiling and the mopso_cd and seeding assumptions stand | project diagnostic,
    not a paper | throwaway script in the session scratchpad, nsga2 and mopso_cd
    at pop_size 40 for 15 generations, seeds 1 and 2 | a2 | 2026-08-31

v-37 | in pymoo 0.6.2 the class in pymoo.algorithms.moo.mopso_cd is named
    MOPSO_CD with the underscore, not MOPSOCD; the latter raises ImportError |
    project diagnostic | .venv pymoo 0.6.2, import checked | a2 | 2026-08-31

v-38 | pymoo 0.6.2 seeds only its own generator: core/algorithm.py line 126 is
    self.random_state = np.random.default_rng(self.seed), and there is not one
    call to global np.random.rand, random, randint, choice, permutation, normal,
    uniform, shuffle or seed anywhere under pymoo/core, pymoo/operators or
    pymoo/algorithms. measured consequence: minimize(seed=s) alone is
    bit-reproducible for both nsga2 and mopso_cd across deliberately different
    global numpy states. numpy.random.seed therefore does nothing for a pymoo run
    in this build | project diagnostic | pymoo 0.6.2 source plus a throwaway
    reproducibility script, both algorithms, minimize seed 7 under global seeds
    111 and 222 | a2 | 2026-08-31

v-39 | the gh-difference has a primary source in papers/ after all. slide 5 of
    23 of the presentation prints, as its equation (2), a -gh b = c iff (a)
    a = b + c if mu(b) <= mu(a), (b) b = a + (-1) c if mu(b) > mu(a), where mu is
    the length of the interval, mu(a) = a_u - a_l, and attributes it to markov
    1974 and stefanini 2008. the branch test is on the length and not on the
    half-width, which is the same test. the collected closed form
    [min{a_l - b_l, a_u - b_u}, max{a_l - b_l, a_u - b_u}] follows from those two
    branches by solving each for c, and is not a further assumption: this is
    derived in the comment above gh_difference and not taken from anywhere |
    papers/Presentacion_optimizacion_intervalar.txt | slide 5 of 23, equation (2),
    lines 109-117, page marker at line 119 | a3 | 2026-08-31

v-40 | the same slide, equation (1), lines 104-107, prints the interval
    arithmetic independently of [1]: a + b = [a_l + b_l, a_u + b_u] and
    lam a = [lam a_l, lam a_u] if lam >= 0, [lam a_u, lam a_l] if lam < 0, naming
    it standard interval arithmetic. this is a second primary source agreeing
    with v-34, so add and scalar_multiply are now attested twice |
    papers/Presentacion_optimizacion_intervalar.txt | slide 5 of 23, equation (1),
    lines 101-107 | a3 | 2026-08-31

v-41 | the constant-width collapse of v-30 reproduces exactly under the three phi
    as implemented in src/phi_transforms.py, and so does the rounding artefact of
    r-07. on 200 points in two objectives at eps = 1/64: on a dyadic grid, where
    the endpoint subtraction is exact, all three non-dominated index sets are
    identical and equal to the crisp one, 7 points; on generic doubles in [0, 1]
    the same construction gives |lu| = 8 against |ls| = |cw| = 9, differing
    through rounding alone; on generic doubles in [0, 1000] the three agree again.
    so the artefact is sample-dependent and not universal, which is what makes it
    dangerous | project diagnostic, not a paper | throwaway script in the session
    scratchpad; the exact case is asserted in
    tests/test_phi_transforms.py::test_constant_width_collapses_the_three_phi_to_one_order
    | a3 | 2026-08-31

v-42 | the arithmetic half of the s-06 guard, built in a2 and recorded here so
    that s-06's history sits with the a2 and a3 records rather than in
    PROGRESS.md. a constant-width construction f -> [f - eps, f + eps] at 500
    centres drawn uniformly from [-1000, 1000] with eps = 0.05 returns a width
    constant to better than 1e-12 and exactly twice the half-width, so the
    endpoint subtraction of r-07 is safe at that scale and the collapse of v-30
    cannot be blamed on it there. the non-domination half of the same guard is
    v-41 | project diagnostic, not a paper | asserted in
    tests/test_interval_math.py::test_constant_width_construction_is_constant_up_to_rounding
    | a2 | 2026-08-31

v-43 | an interval's endpoint pair and its centre-half-width pair are related by
    the linear map (f_l, f_u) = M (c, r) with M = [[1, -1], [1, 1]] and det M = 2,
    and composing the phi of [1] with M gives first = (lam_1 + lam_2) c +
    (lam_2 - lam_1) r and second = (beta_1 + beta_2) c + (beta_2 - beta_1) r,
    whose determinant is 2 (lam_1 beta_2 - lam_2 beta_1) = 2 det phi. so the
    composite is singular exactly when the paper's admissibility condition fails,
    the centre-radius route is the same automorphism in other coordinates rather
    than a second family, and [1]'s definition on endpoint pairs stands unchanged.
    checked entry by entry in exact rational arithmetic on 2000 random coefficient
    sets before it was implemented, with no mismatch and no determinant
    disagreement | derivation from [1] section 2, page 3, lines 170-172, checked
    in this project | the composite is stated in CONTEXT.md section 4; the check
    is asserted in
    tests/test_phi_transforms.py::test_the_centre_radius_route_is_phi_composed_with_the_endpoint_map
    and ::test_the_composite_determinant_is_twice_the_paper_determinant
    | a3-b | 2026-08-31

v-44 | zdt1 is test function T_1 of [2]: f_1(x_1) = x_1, g(x_2,...,x_m) =
    1 + 9 . (sum_{i=2}^{m} x_i) / (m - 1), h(f_1, g) = 1 - sqrt(f_1 / g), with
    f_2 = g h from the scheme of equation (6) on the same page, m = 30 variables,
    x_i in [0, 1], and the Pareto-optimal front formed with g(x) = 1. note that
    [2] writes m for the number of decision variables, which is this project's
    n_vars, and not for the number of objectives | [2] zitzler, deb and thiele,
    evolutionary computation 8(2) (2000) 173-195,
    papers/zitzler_deb_thiele_2000_comparison.pdf | section 4, definition 4,
    equation (7), printed page 177, read from the rendered page: the paper's
    formulas are set in bitmap math fonts and text extraction drops them | a5 |
    2026-08-31

v-45 | dtlz2 is test problem DTLZ2 of [3]: f_1 = (1 + g(x_M)) cos(x_1 pi/2) ...
    cos(x_M-1 pi/2), f_2 = (1 + g(x_M)) cos(x_1 pi/2) ... sin(x_M-1 pi/2), down to
    f_M = (1 + g(x_M)) sin(x_1 pi/2), with g(x_M) = sum_{x_i in x_M} (x_i - 0.5)^2
    and 0 <= x_i <= 1 for i = 1, ..., n. the paper states k = |x_M| = 10 for this
    problem and n = M + k - 1, so M = 3 gives n = 12 and x_M = x_3 ... x_12. the
    Pareto-optimal solutions are x_i* = 0.5 for x_i in x_M, and there the
    objective values satisfy sum_{m=1}^{M} (f_m*)^2 = 1. the sine of the last
    objective is a sine of x_1 and the sine of f_2 is a sine of x_M-1 | [3] deb,
    thiele, laumanns and zitzler, congress on evolutionary computation 2002, ieee,
    papers/deb_thiele_laumanns_zitzler_2002_scalable.pdf | section vii.b,
    equation (9), pdf page 4 | a5 | 2026-08-31

v-46 | the nesting of the phi_lu and phi_ls efficient sets is exact in real
    arithmetic and not in doubles. phi_ls's image is (c - r, 2r) and phi_lu's is
    (c - r, c + r) with c + r = (c - r) + 2r, so anything dominated under phi_ls
    is dominated under phi_lu by the same point and the non-dominated sets nest
    the other way, phi_lu inside phi_ls. measured on a5's constructed samples the
    containment is 1.000 at all four levels on zdt1 and at eps = 0.05, 0.10 and
    0.25 on dtlz2, and 0.999361 on dtlz2 at eps = 0.50, one point of 1565. that
    point sits at x_1 = 1, where dtlz2's first centre is (1 + g) cos(pi/2) =
    6.1e-17 against a half-width of 0.5, so c - r absorbs a difference between two
    points that c + r keeps. it is a cancellation inside phi's own first
    coordinate, not the round trip of r-07, and no representation a problem can
    declare removes it | project diagnostic, not a paper | asserted as a band in
    tests/test_problems_tier1.py::test_the_separation_sets_overlap_without_coinciding
    | a5 | 2026-08-31

v-47 | a5's separation report shows |ls&cw| falling short of |cw| on dtlz2 by 7,
    13, 28 and 39 points at the four levels and not at all on zdt1. the helper is
    not at fault: tests/test_problems_tier1.py builds all four sets as frozensets
    of row indices over one sample array, so |ls&cw| is an index-set intersection,
    and recomputing every set with a second implementation, an explicit pair loop
    with no broadcasting, reproduces all eight cases exactly, 0 mismatches. the
    shortfall is the c - r cancellation. all 39 points at eps = 0.50 are dominated
    under phi_ls in doubles by a named point and none of them is dominated under
    phi_ls, or under phi_cw, in exact rational arithmetic; recomputed exactly,
    |cw \ ls| and |lu \ ls| are 0 in all eight cases. the asymmetry between the
    two counts has a cause: phi_cw's centre-radius route is (c, r) with
    coefficients 1 and 0 and commits no arithmetic, while phi_ls's and phi_lu's
    shared first coordinate is computed as c - r and rounds, so every rounded tie
    in c - r can drop a phi_cw point out of the phi_ls set while phi_lu, built on
    the same rounded column, moves with it. the affected points sit at x_1 = 1,
    where dtlz2's first centre is (1 + g) cos(pi/2) = 6.1e-17 against a half-width
    of up to 0.5; zdt1 has no such face and shows none. the crisp column and |cw|
    are bit-identical in exact and double arithmetic in all eight cases, 144 and
    32, and 947 and 483 | project diagnostic, not a paper |
    docs/a_close_containment.md section 3.4; the two counts are printed on the
    noise line of tests/test_problems_tier1.py's separation report | a-close-b |
    2026-09-01

v-48 | pymoo 0.6.2 does construct a generator that no seeding call reaches, which
    refines v-38 rather than contradicting it: v-38's search was for calls to the
    global numpy state and there are none, while this is a fresh generator seeded
    from the operating system. core/algorithm.py line 249, inside advance, is
    self.archive = self.archive.add(infills) for any algorithm holding an archive,
    and Archive.add truncates with self.truncation once the non-dominated set
    passes max_size, util/archive.py lines 86 and 87 inside add, which begins at
    line 77. the default truncation is
    RandomTruncation, util/archive.py lines 16 to 19, whose __call__ is decorated
    with default_random_state and is called with no random_state, so it draws from
    np.random.default_rng(None). measured consequence for mopso_cd, whose archive
    is a MultiObjectiveArchive with max_size = archive_size, default 200: on p1
    under phi_ls at pop_size 40 and n_gen 20, five runs at seed 7 with both
    numpy.random.seed(7) and minimize(seed=7) gave five different fronts of 179,
    178, 184, 194 and 189 rows. the runs diverge at generation 17 with the
    algorithm's own seeded generator in an identical state at that point, which is
    what rules out the seeded stream as the cause. nsga-ii is unaffected, holding
    no archive. setting archive_size to the whole evaluation budget removes it, the
    archive then holding at most one entry per evaluation and never overflowing:
    bit-reproducible over p0, p1, zdt1 and dtlz2 under all three phi, which is what
    c2 did; c2-b replaced it with a seeded truncation at pymoo's own archive size,
    v-51 and d-03, the finding about the generator being unchanged | project
    diagnostic, not a paper | pymoo 0.6.2
    source, plus scratchpad scripts and tests/test_runners.py::
    test_the_same_seed_gives_the_same_front | c2 | 2026-09-01

v-49 | under pymoo's ("n_gen", n) termination the two solvers do not spend the
    same budget: at pop_size 20 and n_gen 3, 5 and 10, nsga-ii's evaluator reports
    60, 100 and 200 evaluations and mopso_cd's reports 80, 120 and 220, one
    population more, its initial swarm being evaluated outside the generation
    count. under MaximumFunctionCallTermination(pop_size * n_gen) both report 60,
    100 and 200 exactly. so budget parity, CONTEXT.md section 5 step 4, needs the
    termination stated in evaluations, which is what src/runners.py does; the
    count is asserted against the problem's own evaluation calls in
    tests/test_runners.py | project diagnostic, not a paper | pymoo 0.6.2,
    scratchpad script and tests/test_runners.py::test_the_budget_is_pop_size_times_n_gen
    | c2 | 2026-09-01

v-50 | pymoo's non-domination and the project's agree exactly on solver output.
    random_search.non_dominated_indices is the identity on the front returned by
    both nsga-ii and mopso_cd, on p0, p1, zdt1 and dtlz2 under all three phi, 24
    cases, with no row differing in any of them. this is what CONTEXT.md section 5
    predicts structurally, pymoo comparing raw doubles and its NonDominatedSorting
    epsilon argument being a translation, and it is now measured on output rather
    than argued from the source. src/runners.py therefore returns pymoo's front
    unfiltered: re-filtering it would hide a future disagreement instead of
    reporting one | project diagnostic, not a paper |
    tests/test_runners.py::test_the_project_filter_is_the_identity_on_the_pymoo_front
    | c2 | 2026-09-01

v-51 | the unseeded truncation of v-48 can be fixed without resizing the archive
    and without reimplementing any of mopso. pymoo's Algorithm accepts an archive
    object at construction, core/algorithm.py line 34 taking archive: Archive |
    None = None and line 58 storing it, and MOPSO_CD passes **kwargs through to it,
    so one can be handed in; it does not survive, _setup overwriting it at line 77
    with MultiObjectiveArchive(max_size=self.archive_size) and _update_archive
    building another at lines 216 to 219 on every generation. the only surviving
    place is the archive _update_archive installs, so src/runners.py's
    SeededArchiveMopso overrides that one method by delegation and reinstalls
    pymoo's own archive with a truncation that draws from the algorithm's seeded
    generator. measured: bit-identical over five runs at one seed on p0, p1, zdt1
    and dtlz2 under all three phi, at pymoo's default archive_size of 200, with the
    project's filter still the identity on every front. the truncation is reached
    at 800 evaluations on p1 under phi_ls and at 400 on none of the four problems,
    so the test that exercises it is separate from the reproducibility grid. cost
    on p1 under phi_lu at pop_size 100, seconds at budgets 500, 1000, 2000, 4000
    and 20000: 0.09, 0.30, 0.82, 2.05 and 11.71 seeded at archive 200, against
    0.08, 0.32, 1.18, 6.61 and 187.78 for c2's resize and 0.08, 0.32, 0.82, 1.91
    and 10.35 for pymoo's unseeded default | project diagnostic, not a paper |
    pymoo 0.6.2 source, scratchpad scripts, and tests/test_runners.py::
    test_the_archive_truncation_is_seeded_and_is_reached | c2-b | 2026-09-01

v-52 | objective-space metrics move with front cardinality by more than the
    differences a solver comparison would be reporting. one fixed front, random
    search on p1 under phi_lu at budget 5000 and seed 11, 610 rows, measured
    against b2's 1000-point reference front with include_singular_segments False
    and subsampled uniformly at random, ten draws per size and the mean over them:
    igd 0.1303, 0.0851, 0.0551, 0.0357, 0.0221 and 0.0201 at 25, 50, 100, 200, 500
    and 610 rows, and hypervolume against the fixed reference point (1.5892, 2.334,
    1.174, 1.3731) 4.6845, 4.9176, 5.0433, 5.1084, 5.1595 and 5.1665 over the same
    sizes. the points are the same points and the search is the same search, so
    the factor of 6.5 in igd between k = 25 and the full front, and of 2.7 between
    k = 100 and it, is cardinality and nothing else. igd's spread over the ten
    draws is 0.1013 to 0.2260 at k = 25 and 0.0217 to 0.0223 at k = 500 | project
    diagnostic, not a paper | scratchpad script over src/random_search.py,
    src/reference_fronts.py and pymoo's IGD and HV indicators | c2-b | 2026-09-01

v-53 | the forward recovery distance on p1 carries a floor that is a property of
    filtering a finite sample and not of any solver, under phi_ls and phi_cw and
    not under phi_lu. the mechanism is structural: p1's image columns are
    (c_1 - r_1, c_1 + r_1, c_2 - r_2, c_2 + r_2) under phi_lu,
    (c_1 - r_1, 2 r_1, c_2 - r_2, 2 r_2) under phi_ls and (c_1, r_1, c_2, r_2)
    under phi_cw, so phi_ls and phi_cw each carry two columns depending on one
    decision variable alone, r_1 = rho x_2^2 + delta and r_2 = rho x_1^2 + delta,
    and phi_lu carries none. in any finite candidate set the point of smallest
    |x_1| is then the strict minimiser of the r_2 column, so no other candidate is
    no worse in every column and none can dominate it, whatever its x_2; it enters
    every front the ordinary pareto filter returns. its x_2 ranges over the whole
    box [-1/2, 3/2] while b1 section 2.4 puts X_cw's x_2 in [0, 1] and X_ls's in
    [0, 4/3], so the forward hausdorff distance is bounded below by that overhang,
    up to 1/2 under phi_cw, and a larger sample supplies a new such pair rather
    than removing the old one. measured on the gate's own uniform draws at budget
    5000: under phi_ls and phi_cw both extreme points are non-dominated at all
    five gate seeds, under phi_lu both are dominated at all five, and over 40
    independent draws of 2000 points the phi_lu extreme points are dominated in 24
    and 40 of 40 while the phi_ls and phi_cw ones are dominated in 0 of 40. the
    two overhangs the mechanism predicts are the two largest forward distances c3
    reported for random search under phi_cw: the smallest-|x_1| point of seed 11
    is (0.00026, 1.41550) at distance 0.4155 from X_cw and of seed 12 is
    (-0.00000, -0.36913) at 0.3691, which are c3's section 5.1 worst points
    exactly, and c3's largest measured forward distance, 0.5000154 at mopso under
    phi_ls at seed 11, is the box overhang 1/2 to within the reference sample's
    own resolution. this is a property of the design and not a defect: it is why
    c3's forward assertion could not pass, why c3 found the budget removed none of
    random search's forward failures, and why every later reader of e1's tables
    must read a forward distance as reported and never as a quality measure |
    project diagnostic, not a paper | c3's sections 3, 5.1, 5.2 and 5.4, and
    tests/test_validation.py::test_one_image_column_is_a_function_of_one_variable_under_ls_and_cw
    and ::test_the_protected_extreme_can_lie_outside_the_derived_region, the
    latter renamed in c3-c and the third test this row cited,
    ::test_the_extreme_points_of_a_finite_sample_survive_the_filter, replaced
    there by ::test_the_strict_minimiser_of_a_width_column_is_never_dominated,
    which asserts the same thing about an arbitrary finite set instead of about
    one sampler's draws. **the claim stands and its explanation is superseded by
    v-54**, which proves what this row observed and adds the corollary that the
    whole low-|x_1| tail is shielded, not only its first member | c3-b |
    2026-09-01

v-54 | the protected extreme. let S be any finite set of decision vectors in p1's
    box, of at least two elements. if x* in S has |x*_1| strictly smaller than
    every other member's |x_1|, then under phi_ls and under phi_cw no member of S
    dominates x*, whatever x*_2 is; and the same holds for the member of strictly
    smallest |x_2|. proof: under phi_cw the fourth image column is r_2 and under
    phi_ls it is 2 r_2, so in both cases it is a (rho x_1^2 + delta) with a > 0, a
    strictly increasing function of |x_1| and of nothing else; the hypothesis
    makes x* its strict minimiser over S; domination requires being no worse in
    every column and therefore no worse in that one, which contradicts
    strictness. the second column is a (rho x_2^2 + delta) and gives the |x_2|
    statement. under phi_lu the four columns are c_1 -+ r_1 and c_2 -+ r_2 and
    every one of them moves with both variables, d(c_1 - r_1)/dx_1 = 2 x_1 and
    d(c_1 - r_1)/dx_2 = 2 (x_2 - 1) - 2 rho x_2, so the hypothesis is
    unavailable there. corollary, and it is the corollary that matters: ordering S
    by |x_1| ascending, the j-th member can be dominated only by one of the j - 1
    below it, so the whole low-|x_1| tail is shielded and not only its first
    member. consequences: the protected member's other coordinate is unconstrained
    by the hypothesis, so for a uniform draw it lies outside X_cw's x_2 range with
    probability exactly 1/2 and its expected overhang is exactly 1/8 at every
    budget; and a larger budget elects a new member of smaller |x_1| rather than
    removing the old one, so no monotone trend in budget is a property either
    population method has under phi_ls or phi_cw. measured: over 2000 adversarial
    finite sets with two members planted at the worst place the box allows, the
    two extremes are dominated 0 times under phi_ls and phi_cw and 1066 and 1939
    times under phi_lu; over the five gate draws of 5000 points the thirty
    smallest |x_1| survive the filter at rate 0.73 and 0.60 under phi_ls and
    phi_cw against 0.44 and 0.31 for the sample at large, while the thirty
    smallest |x_2| survive at 0.79 and 0.69 under those two phi and are dominated
    in all 150 cases under phi_lu; and over 200 uniform draws at n = 1000, 5000, 20000 and 80000 the
    median smallest |x_1| falls as 7.45e-04, 1.41e-04, 4.21e-05, 1.00e-05 while
    the mean overhang of the elected point's x_2 does not move, 0.1226, 0.1404,
    0.1334, 0.1261. this supersedes v-53's account of the same phenomenon by
    proving it rather than observing it, and it is what removes c3-b's budget
    trend assertion | project diagnostic, not a paper | docs/c3_validation.md
    section 1, and tests/test_validation.py::test_the_strict_minimiser_of_a_width_column_is_never_dominated,
    ::test_one_image_column_is_a_function_of_one_variable_under_ls_and_cw,
    ::test_the_whole_low_width_tail_is_shielded_and_not_only_its_first_member,
    ::test_the_low_width_tail_is_not_shielded_under_lu and
    ::test_a_larger_budget_re_elects_the_protected_extreme | c3-c | 2026-09-01

v-55 | the reverse recovery direction is bounded by one fill distance and not by
    a sum of two. write R for a derived region of b1 section 2.4 and S for a
    recovered set. the reverse hausdorff is sup over p in the reference set of
    dist(p, S); every reference point lies in R, so that supremum is at most
    sup over y in R of dist(y, S), the fill distance of S with respect to R, and
    the reference sample enters only through being a subset of R. its own
    resolution therefore plays no part in this direction, and for any two subsets
    A and B of R the two-sided bound is max(fill(A), fill(B)) and never
    fill(A) + fill(B). the bound requires nothing of S: S need not lie in R, and
    p1's protected extremes do not. measured on 300 random pairs of subsets of
    each region at sizes 1000 and 100: the bound held 300 of 300 in both
    directions under all three phi and its reverse slack reached 0.0000, so it is
    attained and not merely valid, while the sum stands at 0.189, 0.293 and 0.238
    against maxima of 0.143, 0.219 and 0.177 for phi_lu, phi_ls and phi_cw. this
    is what removes h_reference from the c3 gate tolerance and retires r-17 |
    project diagnostic, not a paper | docs/c3_validation.md section 2.1, and
    tests/test_validation.py::test_the_reverse_distance_is_bounded_by_the_solver_fill_distance
    | c3-c | 2026-09-01

v-56 | the three phi images of p1 are constant linear images of one another, and
    exactly two of the three pairs are similarities. writing g_lu, g_ls and g_cw
    for the four image columns of b1 section 1.1, g_lu = A g_cw and
    g_ls = B g_cw for every x, with A = [[1,-1,0,0],[1,1,0,0],[0,0,1,-1],[0,0,1,1]]
    and B = [[1,-1,0,0],[0,2,0,0],[0,0,1,-1],[0,0,0,2]], because each phi is a
    constant linear map of the endpoint pair. A^T A = 2 I, so A is sqrt(2) times
    an orthogonal matrix: the phi_lu image is a rotation and a uniform scaling of
    the phi_cw image, the singular values of J_lu are exactly sqrt(2) times those
    of J_cw at every point, and the two maps' singular-value ratios are identical
    pointwise. B is not a similarity: B^T B is block diagonal with two copies of
    [[1,-1],[-1,5]], whose eigenvalues are 3 +- sqrt 5, so B's singular values are
    sqrt(3 + sqrt 5) = 2.288246 and sqrt(3 - sqrt 5) = 0.874032, each twice, and
    its condition number is exactly (1 + sqrt 5)^2 / 4 = 2.618034, the golden
    ratio squared. the map from the phi_ls image to the phi_lu image, A B^-1, has
    singular values exactly phi and 1/phi and the same condition number. checked
    on 500 random points of the box and on all three region samples: the two
    identities hold to 0.000e+00 and the pointwise equality of the raw ratios to
    7.1e-15. this is a fact about examples 2.2, 2.3 and 2.4 of [1] and not about
    p1, since A and B do not contain the problem. **reported and not asserted: the
    session that measured it added nothing to the suite, so no test guards this
    row yet** | project diagnostic, not a paper | docs/c3_validation.md section
    5.5, "where phi_ls sits" | c3-f | 2026-09-02
