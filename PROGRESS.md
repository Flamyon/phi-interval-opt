# phi-interval-opt: progress

state, not specification. the specification is CONTEXT.md and this file never
repeats it. edited by the human only, from session record blocks reviewed in the
research chat.

project started 2026-08-30. nothing has been built.


## 1. where the project stands

    current phase:      a, formulation
    current subpart:    a2, awaiting review (a0, a0-b and a1 also awaiting review)
    blocked on:         nothing
    files on disk:      docs/a0_framework.md
                        docs/a1_uncertainty_model.md
                        papers/new_preference_order_relationships_paper.txt
                        papers/Presentacion_optimizacion_intervalar.txt
                        src/interval_math.py
                        tests/conftest.py
                        tests/test_interval_math.py
                        requirements.txt, versions pinned to the venv


## 2. subpart status

status is one of: not started, in progress, awaiting review, done, reopened.

phase a, formulation
    a0  verification pass over [1]          awaiting review
    a1  uncertainty model                   awaiting review
    a2  interval_math.py                    awaiting review
    a3  phi_transforms.py                   not started
    a4  problems_tier0.py                   not started
    a5  problems_tier1.py                   not started

phase b, ground truth
    b1  phi-efficient sets, derivation      not started
    b2  reference_fronts.py                 not started

phase c, solvers
    c1  random_search.py                    not started
    c2  runners.py                          not started
    c3  validation gate                     not started

phase d, analysis
    d1  metrics_objective.py                not started
    d2  metrics_decision.py                 not started
    d3  reporting.py                        not started

phase e, experiments
    e1  tier 0 run                          not started
    e2  tier 1 run                          not started
    e3  results synthesis                   not started

phase f, part 2
    f1  data and interval construction      not started
    f2  optimization under selected phi     not started
    f3  backtest                            not started
    f4  write-up                            not started


## 3. decisions

decisions taken in the research chat and closed. a decision is reopened only with a
reason recorded here as a new entry, never by editing the old one.

format:

    d-nn, date. one sentence stating the decision.
        why: the reason.
        source: the paper, example or file it rests on, or "project judgement".
        affects: the subparts it constrains.

none yet.


## 4. verified facts

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


## 5. questions the papers answer

reading tasks with an owner. no working assumption is attached to these, because
the source can settle them and guessing is what this project is avoiding.

format:

    p-nn | question | owner subpart | status | answer once found

p-01 | what letter and typeface does [1] use for the class of automorphisms and
    for the beta row vector, and what works are behind its own references [7],
    [9], [23], [26] and [31]? the extracted text drops both glyphs everywhere and
    ends before the bibliography | a0, then b1 | open, needs the pdf of [1] |

p-02 | does ishibuchi and tanaka 1990, [9] in the project's numbering, state the
    centre-width comparison in the same coefficients as example 2.4 of [1]? this
    is the provenance sentence in CONTEXT.md section 3, and a0 could not verify it
    because [1] attributes CW-convexity to its own unresolvable reference [31] |
    b1 | open, needs the paper itself and not literature/Center-Width
    Decomposition.md |

p-03 | does an interval-space analogue of proposition 5.1 appear in any source
    outside [1]? [1] itself does not state one, established in a0-b as v-26. the
    candidates are [1]'s own reference [9], the m = 1 predecessor of this
    framework, and its [26] and [31] | b1 | open, blocked on p-01, since [1]'s
    bibliography is not in the extracted text and those numbers cannot yet be
    resolved to works |

p-04 | does any construction in [7] or [8], the two interval evolutionary
    algorithm papers, drive the interval width from the decision vector rather
    than by a constant band? both extend crisp benchmarks into interval ones, and
    [8] is named in CONTEXT.md section 3 as the methodological template for doing
    so, so their construction is directly comparable to a1's | a5 | open, needs
    the two papers rather than their literature/ summaries |

p-05 | does stefanini, arana-jimenez and sorini 2025, [10] in the project's
    numbering, state the gh-difference exactly as
    a -gh b = [min{a_l - b_l, a_u - b_u}, max{a_l - b_l, a_u - b_u}], with the
    two-branch definition a = b + c or b = a + (-1) c, and in which numbered
    definition of its section 2? a2 implemented gh_difference from
    literature/gH-differentiability calculus for interval analysis.md section 2,
    because the paper is not in papers/. that is a summary and not a paper, so
    under the evidence rule of CONTEXT.md section 11 the formula is not yet
    established. the same paper is CONTEXT.md section 6's source for the
    midpoint-radius regularity criterion b1 needs, so one acquisition closes both
    | b1, and a2 on re-check | open, needs the paper itself |


## 6. questions only the supervisors can answer

each carries the working assumption the project proceeds on. none blocks work. if
an answer differs from the assumption, record it as a decision in section 3 and
list the subparts that have to change.

format:

    s-nn | question | working assumption | asked on | answer

s-01 | equation (16) of [1] is internally inconsistent in the w subscripts on the
    beta terms: the expanded line carries w_2i, the collected line carries
    w_2i-1. which is intended? | b1 does not cite (16). it expands (15) directly
    from the definitions of Lambda_i and B_i, which reproduces the expanded line.
    (16) is a convenience under a hypothesis (15) does not require | not yet asked
    |

s-02 | example 3.9 statements 1 and 2 read "w_i >= 0 not equal zero for all i".
    does that mean nonnegative and not all zero, or strictly positive? | the
    former, which is the reading CONTEXT.md section 6 already carries; the latter
    would make statement 3 redundant. any b1 result that turns on a zero weight in
    statements 1 or 2 carries the ambiguity explicitly | not yet asked |

s-03 | [1] defines an efficient solution for (12) as one for which no x != x-bar
    has h_i(x) <= h_i(x-bar) for all i, with no strictness required anywhere. that
    is strong efficiency, not the usual Pareto efficiency, and it does not match
    definition 3.1(2). which does theorem 3.1 mean? | the usual Pareto definition,
    which is what definition 3.1(2) and equation (6) give and what pymoo
    implements. the two differ only when two distinct decision vectors have the
    same image, so the choice is recorded in b2 rather than assumed away | not yet
    asked |

s-04 | should CONTEXT.md section 2 record that the conclusion of [1] does make a
    comparative statement about two phi, under the quasilinear-space criterion,
    see v-23? | no amendment. the project rule that part 1 may not rank phi is a
    project rule about what this study can measure, and it stands independently of
    what [1] says; the paper's criterion is structural, not empirical, and does not
    bear on the measurement design | not yet asked |

s-05 | CONTEXT.md section 9 excludes sections 4 and 5 of [1] as the fuzzy branch.
    that exclusion was written before anyone had read section 5, and section 5
    contains proposition 5.1, which relates the solution sets of the example 2.2
    and example 2.3 automorphisms, two of the three phi in the experiment, see
    v-24. does the exclusion stand? | the exclusion stands for implementation. the
    project formulates the interval problem, implements the three phi as
    committed, and takes nothing from sections 4 or 5 as a result it claims.
    proposition 5.1 is recorded as a prediction to be checked empirically, not as
    a result the project asserts, and no interval analogue is derived from it: [1]
    does not state one, v-26, and whether theorem 5.1 yields one is not the
    agent's call. if an empirical result contradicts the prediction, that is a
    finding about the interval case and not a refutation of [1] | not yet asked
    |

s-06 | the phi transforms are numerically unsafe at small width. computing the
    second image coordinate as f_u - f_l loses it entirely when the true width is
    constant or near zero: on the a1 part 1 diagnostic that turned four identical
    non-dominated sets of 16 into |lu|=16 and |ls|=|cw|=30, which reads as a phi
    effect and is rounding noise. CONTEXT.md section 10 a3 specifies make_phi as a
    function of (f_l, f_u), which forces the subtraction. should the interface
    carry (centre, half_width) instead? | a3 keeps the specified (f_l, f_u)
    signature for now, and a2 and a3 each carry a test that the constant-width
    case returns identical non-dominated sets under all three phi, so the artefact
    cannot reach a result unnoticed. changing a specified interface is not a1's
    call | not yet asked |

s-07 | the degeneracy check CONTEXT.md section 5 step 1 prescribes, and the a4 and
    a5 tests that implement it, run on a uniform sample of the box. that is not
    sufficient: zdt1 with half-width eps*x_n passes every width-versus-centre
    statistic and separates all three phi on a uniform sample, yet on the slice
    where the efficient set lives phi_cw returns the crisp efficient set exactly.
    should the check also run on that slice? | yes. a4 and a5 add a second
    assertion on the slice obtained by holding the non-conflicting variables at
    their crisp optima. a1's tier 1 forms were chosen against that stronger check
    | not yet asked |

s-08 | p1's phi-efficient set is a two-dimensional band, not the curve the a4 spec
    asked for, and a1 establishes that a curve and three distinct phi are not both
    available at two variables and two interval objectives. accept the band, or
    change p1's shape? | accept the band. it serves the stated purpose, giving
    spread and coverage two dimensions of structure rather than one, and it is
    tractable for b1, being a product of intervals whose x_2 bounds do not depend
    on x_1. CONTEXT.md section 10 a4 has been corrected to say so | not yet asked |

s-09 | tier 1 uses one absolute half-width for every objective, following slide
    19's "incertidumbre acotada +-eps en los objetivos". on zdt1 that is a large
    relative imprecision on f_1, which ranges over [0,1], and a small one on f_2,
    which ranges over roughly [0,10]. should the half-width be scaled per
    objective instead? | keep the common absolute width, as the closest reading of
    slide 19, and record the asymmetry in every tier 1 table. a per-objective
    scaling is a one-line change if the supervisors prefer it | not yet asked |


## 7. risks

format:

    r-nn | risk | what it would cost | what would trigger it | mitigation

r-01 | the source papers are not under version control: .gitignore line 1 is
    "*.txt", so git mv failed in a0 and the two files were moved with plain mv |
    the exact text a0 verified against is not recoverable from history, and a
    re-extraction could differ from it silently | any re-extraction of the pdf, or
    a fresh clone of the repository | un-ignore papers/ or commit the extracted
    text; decision for the research chat

r-02 | reference [9] of [1], the m = 1 predecessor, is where the order relations
    on C that equation (3) decomposes into are defined, and it is not among the
    five papers of CONTEXT.md section 3 | if b1 needs a property of those
    relations beyond what equation (3) states, it has no source in scope | b1
    needing a property of the componentwise relation on C | equation (3) states
    the relation fully in terms of phi_i and the order on R^2, so nothing is
    missing today; raise in the research chat if b1 needs more

r-03 | the pdf of [1] is not in the repository, and the extracted text is missing
    its reference list and two glyphs | provenance claims in CONTEXT.md section 3
    cannot be verified and [1]'s own citations cannot be resolved | already
    realised in a0 | obtain the pdf; p-01 and p-02

r-04 | b1's route to p0's published anchor is not the one CONTEXT.md previously
    assumed: example 3.9's hypotheses fail at x = 0 under phi_lu, because both
    image coordinates of the first objective are non-differentiable there | b1's
    check on its own procedure, "state whether the paper's published conclusion is
    recovered", may not close by the planned route | b1 starting p0 | CONTEXT.md
    section 6 corrected in a0; b1 uses example 3.8, which needs no
    differentiability, or definition 3.1 directly, or records that the conditions
    do not close and goes to the research chat

r-05 | example 2.1 shows the class permits different coefficients per objective,
    which none of the three implemented phi use | nothing for the committed
    experiment, but a reviewer may ask why the study fixes one 2x2 map across all
    objectives when the framework does not require it | memoria review | the
    answer is in docs/a0_framework.md c9 and in CONTEXT.md section 4: the three
    named examples carrying convexity notions are the committed variable

r-06 | if an interval analogue of proposition 5.1 holds, the phi_lu and phi_ls
    efficient sets are nested rather than merely different | it invalidates no
    measurement, but a result reported as "the sets differ" for that pair would be
    presenting a containment as a free empirical finding, and cross-evaluating
    phi_lu's set under phi_ls would lose nothing by construction, making the
    delta-coverage in that direction trivially complete | e1 producing the phi_lu
    against phi_ls decision-space metrics | report that pair as a check on the
    prediction of s-05 rather than as an independent finding, and state the
    containment as a prediction and not as a result the project claims. the phi_cw
    comparisons are unaffected: v-25 records that no statement of [1] relates
    example 2.4 to either of the other two

r-07 | computing a phi image coordinate as f_u - f_l is numerically unsafe when
    the width is constant or near zero. the cancellation error is of order machine
    epsilon times |f|, and under phi_ls and phi_cw that error becomes the whole
    content of the second coordinate | a degenerate construction would present as
    the three phi differing, which reads as a positive result, rather than as the
    three phi coinciding, which is the symptom CONTEXT.md section 5 step 1 tells
    the project to look for. a study could report arithmetic as a phi effect |
    already realised in the a1 diagnostic, where it gave |lu|=16 against
    |ls|=|cw|=30 on a construction whose exact answer is four identical sets of 16
    | a2 and a3 carry the constant-width test described in s-06; the tier 1 eps=0
    baseline sits exactly at the dangerous limit and is labelled degenerate already

r-08 | a construction can pass every width-versus-centre statistic on a uniform
    sample and still give phi_cw the crisp efficient set, because a uniform sample
    of a 30-dimensional box contains almost nothing near the efficient set | tier 1
    would measure nothing while appearing to measure something, and the failure
    would surface only at e3 when the phi comparison came out empty | already
    realised for zdt1 with half-width eps*x_n, measured in a1 part 2 | the width
    driver rule in a1 part 2, plus the slice check proposed as s-07. a1's
    recommended tier 1 forms were selected against it

r-09 | a1's width driver rule was derived from two benchmarks and one tier 0 design
    and has not been tested outside them | a tier 1 or portfolio problem built on
    it could still be degenerate in a way not yet seen | f1 constructing interval
    returns for part 2, which is a different kind of problem | treat the rule as a
    working rule and not a result, and run the full a1 diagnostic including the
    slice check on every new problem before it is used

r-10 | gh_difference in src/interval_math.py is the first piece of code in the
    project whose formula is cited to a literature/ summary and not to a paper,
    because [10] is not in papers/. v-35 records that [1] contains no
    gh-difference, so there is no second source in scope | if the summary's
    closed form or its branch condition differs from the paper's, every later use
    of gh_difference carries the error, and the project would have broken its own
    evidence rule without noticing | already realised in a2; the comment above the
    function says so in the code itself | obtain [10] and close p-05. nothing in
    the committed experiment calls gh_difference yet: the three phi and the tier 0
    and tier 1 objectives need only add, scalar_multiply, centre, half_width and
    width, all of which are cited to [1] as v-34 and v-35


## 8. session log

one block per session, appended after review. never edited by the coding agent, and
never edited after it is written; a correction is a new entry.

format:

    date | subpart | files produced | outcome | next

2026-08-31 | a0 | docs/a0_framework.md. papers/ and docs/ created; the two source
    texts moved into papers/ with plain mv, since *.txt is gitignored and git mv
    refused. CONTEXT.md corrected in three places, sections 4, 6 and 11, each
    shown as a before and after block in the session reply. PROGRESS.md sections
    1, 2, 4, 5, 6, 7 and 8 updated. |
    outcome: of the 15 claims checked, 12 confirmed, 1 refuted, 1 partially
    confirmed, 1 split. refuted: c9, sections 2 and 3 do contain a further named
    example of phi, example 2.1, with explicit coefficients. partially confirmed:
    c14, the differentiability hypothesis of example 3.9 is confirmed verbatim but
    the printed weight condition admits two readings and the paper does not settle
    it. split: c15, the worked function, its stated conclusion and the phi it is
    stated under are all confirmed, but CONTEXT.md's account of what it
    demonstrates is refuted, since example 3.9's hypotheses fail at that point.
    23 verified facts recorded. 8 ambiguity or text-corruption items recorded and
    none resolved; three of them became s-01 to s-03. |
    next: a1, the uncertainty model decision, or a2, interval_math.py. a0 and a1
    are parallelizable and a2 is parallel with both. a0 unblocks a3 and b1.

2026-08-31 | a0-b | docs/a0_framework.md, section "a0-b addendum" appended, plus
    a correction to a0's own page citation for the conclusion passage and an
    extension of its page table. .gitignore given the exception !papers/*.txt and
    both source papers committed, commit cd30981, since a0 had verified against
    them while they were untracked; no other ignore rule changed. PROGRESS.md
    sections 1, 4, 5, 6, 7 and 8 updated. CONTEXT.md not changed. |
    outcome: proposition 5.1 exists and is transcribed. it is a statement about
    the two fuzzy problems, running from the example 2.2 automorphism to the
    example 2.3 one, so the phi_ls solution set contains the phi_lu one; stated
    for the optimal solution concept only, with no convexity or differentiability
    hypothesis and no converse. example 2.4 appears in no such statement. no
    interval-space analogue is stated anywhere in sections 2 or 3: established by
    exhaustive search, not derived, and the session stopped there as instructed.
    theorem 5.1 is where the fuzzy and interval formulations are related, and its
    interval side is a family indexed by alpha rather than one problem. the
    conclusion's "better option" claim is confirmed conditional, on m = 1 and on
    the quasilinear-space criterion. c16 to c19 refute nothing in CONTEXT.md.
    6 verified facts added, 1 corrected, 2 ambiguities recorded as a-9 and a-10,
    p-03, s-05 and r-06 raised. |
    next: s-05 goes to the supervisors before b1 or e3 uses anything from section
    5. otherwise unchanged from a0: a1 or a2, and a0 still unblocks a3 and b1.

2026-08-31 | a1 | docs/a1_uncertainty_model.md. CONTEXT.md section 10 a4 corrected
    in one place, shown as a before and after block in the session reply.
    PROGRESS.md sections 1, 2, 4, 5, 6, 7 and 8 updated. no src/, no tests, nothing
    committed. the diagnostic ran from a throwaway script in the session scratchpad
    under /tmp, numpy only. |
    outcome: the degeneracy hypothesis of CONTEXT.md section 5 step 1 is confirmed
    in exact arithmetic on both benchmarks, and its "function of the centre alone"
    clause is confirmed separately by a proportional-imprecision control. the first
    run appeared to refute it and did not: computing the width as f_u - f_l turns
    the constant-width case into what looks like a phi effect, recorded as r-07 and
    s-06. imprecision in the coefficients is rejected, because it makes the
    half-width an exact linear function of the centre on any monomial objective and
    phi_cw then returns the crisp set exactly. imprecision in the objective with a
    decision-driven half-width is recommended, subject to a width driver rule the
    session had to derive, since a construction can pass the uniform-sample check
    and still be degenerate on the efficient set, r-08 and s-07. p1 is proposed
    with its six image coordinates written out, all convex and differentiable, on a
    box chosen so the efficient set is interior and example 3.9 is applicable; its
    efficient set is a two-dimensional band and not the curve a4 asked for, which
    is why CONTEXT.md was corrected, s-08. tier 1 forms and a five-level eps sweep
    are fixed for both benchmarks. 4 verified facts, 1 p-row, 4 s-rows, 3 r-rows,
    6 unsettled items. |
    next: a1 is reviewed in the research chat before a4, a5 or b1's p1 branch, per
    CONTEXT.md section 10. a2 is unblocked now and is parallel with that review.

2026-08-31 | a2 | src/interval_math.py, tests/conftest.py,
    tests/test_interval_math.py, requirements.txt with every version pinned to the
    venv. branch a2-interval-math, commit on that branch and not on main. the a0,
    a0-b and a1 edits to CONTEXT.md, PROGRESS.md and docs/ were already uncommitted
    on main when the session opened and were left uncommitted, so the a2 commit
    carries only a2's own four files. PROGRESS.md sections 1, 2, 4, 5, 7 and 8
    updated. CONTEXT.md not changed: nothing read this session refutes it. |
    outcome: the six functions build and 16 tests pass. add and scalar_multiply are
    cited to [1] section 2 page 2 lines 101-106, recorded as v-34; the sign rule is
    printed there as a two-case brace and the negative-scalar endpoint swap is part
    of the definition. centre, half_width and width are cited to examples 2.4 and
    2.3, which is the only place [1] defines them, recorded as v-35. the same
    search established that [1] contains no gh-difference at all, so gh_difference
    had to be cited to literature/gH-differentiability calculus for interval
    analysis.md section 2 rather than to [10] itself, which is not in papers/. that
    is a summary and not a paper, so under the evidence rule it is not established:
    raised as p-05 and r-10, and the comment above the function says so in the
    code. gh_difference is implemented with np.minimum and np.maximum on the two
    endpoint differences, so both branches are resolved entry by entry and one
    array may hold entries of either; a test asserts the defining property
    a = b + c or b = a + (-1) c holds entrywise on a 500-entry random array where
    both branches occur. one item for the research chat: s-06's working assumption
    says a2 and a3 each carry a constant-width test on the non-dominated sets under
    all three phi, and a2 cannot, since it has no phi and CONTEXT.md section 10 a2
    forbids one. a2 carries instead the arithmetic half of that check, that a
    constant-width construction at centres of order 1000 returns a width constant
    to better than 1e-12 and exactly twice the half-width; the non-dominated half
    of the check falls entirely to a3. |
    pytest output, literal:

        ============================= test session starts ==============================
        platform linux -- Python 3.12.3, pytest-9.1.1, pluggy-1.6.0 -- /home/flamyon/quant/imus/phi-interval-opt/.venv/bin/python
        cachedir: .pytest_cache
        rootdir: /home/flamyon/quant/imus/phi-interval-opt
        collecting ... collected 16 items

        tests/test_interval_math.py::test_add_sums_endpoints PASSED              [  6%]
        tests/test_interval_math.py::test_scalar_multiply_negative_swaps_endpoints PASSED [ 12%]
        tests/test_interval_math.py::test_scalar_multiply_positive_keeps_endpoints PASSED [ 18%]
        tests/test_interval_math.py::test_scalar_multiply_zero_gives_degenerate_interval PASSED [ 25%]
        tests/test_interval_math.py::test_scalar_multiply_mixed_sign_array_is_elementwise PASSED [ 31%]
        tests/test_interval_math.py::test_centre_half_width_and_width_on_known_intervals PASSED [ 37%]
        tests/test_interval_math.py::test_width_is_twice_half_width_on_a_random_array PASSED [ 43%]
        tests/test_interval_math.py::test_gh_difference_first_branch PASSED      [ 50%]
        tests/test_interval_math.py::test_gh_difference_second_branch PASSED     [ 56%]
        tests/test_interval_math.py::test_gh_difference_mixed_branches_in_one_array PASSED [ 62%]
        tests/test_interval_math.py::test_gh_difference_satisfies_its_definition_entrywise PASSED [ 68%]
        tests/test_interval_math.py::test_degenerate_interval_is_handled PASSED  [ 75%]
        tests/test_interval_math.py::test_gh_difference_of_an_interval_with_itself_is_zero PASSED [ 81%]
        tests/test_interval_math.py::test_every_function_preserves_shape PASSED  [ 87%]
        tests/test_interval_math.py::test_no_function_mutates_its_inputs PASSED  [ 93%]
        tests/test_interval_math.py::test_constant_width_construction_is_constant_up_to_rounding PASSED [100%]

        ============================== 16 passed in 0.21s ==============================

    next: a3, phi_transforms.py, which a0 unblocked and which a2 now supplies the
    arithmetic for. p-05 goes with the other paper-acquisition items; it does not
    block a3, a4 or a5, none of which call gh_difference.
