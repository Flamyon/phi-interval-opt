# phi-interval-opt: verified facts

moved out of PROGRESS.md in session a1-b, unchanged. this file is the project's
record of claims checked against a source. numbering continues here and numbers
are never reused. the rows are in the order they stood in PROGRESS.md, which is
not strictly numeric: v-29 was appended after v-33 by a0-b and stays there.

highest number in use: v-41.

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
