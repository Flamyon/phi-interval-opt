# phi-interval-opt: progress

state, not specification. the specification is CONTEXT.md and this file never
repeats it. edited by the human only, from session record blocks reviewed in the
research chat.

this file holds current state and open items only. everything settled lives
elsewhere:

    docs/verified.md    every verified fact, v-01 to v-46
    docs/answered.md    answered questions and retired risks
    git log             session-by-session detail, one commit per subpart

    highest numbers in use: v-47, p-06, s-11, r-11, d-02.
    numbering continues across those files and numbers are never reused.

project started 2026-08-30.

## 1. where the project stands

    current phase:      b, ground truth
    current subpart:    b1, awaiting review. phase a is complete: a0, a0-b, a1,
                        a1-b, a2, a3, a3-b, a4, a4-b, a5 and a-close are all done
                        and docs/phase_a_summary.md is the close-out document
    blocked on:         nothing
    files on disk:      docs/a0_framework.md, docs/a1_uncertainty_model.md,
                        docs/a4b_dominance_tolerance.md,
                        docs/a_close_containment.md, docs/phase_a_summary.md,
                        docs/b1_phi_efficient_sets.md,
                        docs/verified.md, docs/answered.md
                        papers/new_preference_order_relationships_paper.txt
                        papers/Presentacion_optimizacion_intervalar.txt
                        papers/zitzler_deb_thiele_2000_comparison.pdf
                        papers/deb_thiele_laumanns_zitzler_2002_scalable.pdf
                        src/interval_math.py, src/phi_transforms.py,
                        src/problems_tier0.py, src/problems_tier1.py
                        tests/conftest.py, tests/test_interval_math.py,
                        tests/test_phi_transforms.py, tests/test_problems_tier0.py,
                        tests/test_problems_tier1.py
                        requirements.txt, versions pinned to the venv

## 2. subpart status

status is one of: not started, in progress, awaiting review, done, reopened.

phase a, formulation. complete, tagged phase-a-complete.
    a0  verification pass over [1]          done
    a1  uncertainty model                   done
    a2  interval_math.py                    done
    a3  phi_transforms.py                   done
    a4  problems_tier0.py                   done
    a5  problems_tier1.py                   done

phase b, ground truth
    b1  phi-efficient sets, derivation      awaiting review
    b2  reference_fronts.py                 not started, and is the next subpart

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

decisions taken in the research chat and closed. a decision is reopened only with
a reason recorded here as a new entry, never by editing the old one.

format:

    d-nn, date. one sentence stating the decision.
        why: the reason.
        source: the paper, example or file it rests on, or "project judgement".
        affects: the subparts it constrains.
        status: closed, or proposed and awaiting the research chat.

d-01, 2026-08-31. p1's default delta becomes 1/8, replacing a1-b's 1/10.
    why: 1/10 was p1's only non-dyadic constant. at 1/8 the endpoint route is
    exact on a dyadic sample, 4225 of 4225 points bitwise and the width column
    carrying its true 49 distinct values against 150 at 1/10.
    source: docs/a4b_dominance_tolerance.md part 2, which verifies in exact
    integer arithmetic that delta enters every image coordinate as an additive
    constant, that no gradient or hessian moves, and that all three efficient
    index sets are identical.
    affects: a4, done; b1 and b2 inherit the new constant; a1-b's tables were
    measured at 1/10 and their efficient sets are unchanged by this.
    status: closed.

d-02, 2026-08-31, taken in the research chat and built in a3-b. every phi image is
    computed from the representation the problem declares, and one untoleranced
    dominance relation is used everywhere.
    why: it is the only option measured that needs no tolerance parameter, is
    stable over twelve decades of magnitude, and reaches inside pymoo rather than
    patching its output. the framing that made it cheap is that it is an
    evaluation-order change and not an interface change: (f_l, f_u) = M (c, r)
    with M = [[1, -1], [1, 1]] and det M = 2, so composing with phi gives the same
    phi in other coordinates and the composite determinant is 2 det phi, leaving
    admissibility exactly where [1] states it, on lam and beta.
    source: docs/a4b_dominance_tolerance.md for the measurements; the composite
    was re-derived and checked in a3-b before being implemented, on 2000 random
    rational coefficient sets, and is in CONTEXT.md section 4.
    affects: a3 gained make_phi_of_centre_radius and a paired registry, make_phi
    itself unchanged; a4 gained Problem.representation, p0 declaring "endpoints"
    and p1 "centre_radius"; a5 builds tier 1 in centre and half-width form from
    the start; c1, c2, d2 and b2 compare with no tolerance. the a4 test's rounding
    step is gone and the same grids return a1-b's counts without it.
    status: closed.

## 4. verified facts

moved to docs/verified.md in session a1-b. the number is kept in place so that
every existing reference to "PROGRESS.md section 4", in the session log, in the
s-rows and in the commit history, still resolves to something.

## 5. questions the papers answer

reading tasks with an owner. no working assumption, because the source can settle
them and guessing is what this project is avoiding.

format: p-nn | question | owner subpart | status

p-01 | what letter and typeface does [1] use for the automorphism class and the
    beta row vector, and what works are its [7], [9], [23], [26] and [31]? | a0,
    then b1 | open, needs the pdf of [1]

p-02 | does ishibuchi and tanaka 1990, [9], state the centre-width comparison in
    the same coefficients as example 2.4 of [1]? | b1 | open, needs the paper and
    not literature/Center-Width Decomposition.md

p-04 | does any construction in [7] or [8] drive the interval width from the
    decision vector rather than by a constant band? | e3 | open, needs the two
    papers themselves, which are not in papers/. the owner moves from a5 to e3 in
    a-close, which is the date the row was missing: [7] and [8] are comparison
    references, CONTEXT.md section 3, and the first place the project has to say
    anything about them is e3's synthesis, where the memoria answers the direct-
    interval objection. a5 ran without them and nothing between here and e3 waits
    on them: tier 1's widths are a1 part 4's and are cited there. if they are not
    obtained by e3, e3 records that the comparison is made against the literature
    summaries in literature/ and not against the papers, which is a weaker
    citation and has to be visible as one

p-05 | under which numbered definition does [10] state the gh-difference, and
    under which theorem number the midpoint-radius regularity criterion? | b1,
    then b2 | open and now realised. b1 needed the criterion and had to cite it as
    "theorem 34" from literature/gH-differentiability calculus for interval
    analysis.md with the number unverified, [10] not being in papers/. the outcome
    of the check is not in doubt for p1, every function involved being a
    polynomial with a strictly positive radius, and b1 does not rest on the
    number; the paper is still wanted so the memoria can cite it properly

p-06 | does [1] anywhere identify the "strict minimum" it asserts at x = 0 for the
    worked function after example 3.9 with one of definition 3.1's three named
    concepts? | b1 | open. the paper's words are "a strict minimum", which is not
    one of the three names, and a0 found no sentence joining them. definition
    3.1(1) is the plausible reading, being the only one stated through the same
    relation, but a4-b demoted it from a claim to an inference in both
    CONTEXT.md section 10 a4 and p0's comment

## 6. questions only the supervisors can answer

each carries the working assumption the project proceeds on. none blocks work. if
an answer differs from the assumption, record it as a decision in section 3 and
list the subparts that have to change.

format: s-nn | question / assumption / status / discussed in

s-01 | (16) of [1] is inconsistent in the w subscripts on the beta terms: the
    expanded line carries w_2i, the collected line w_2i-1. which is intended?
    assumption: b1 does not cite (16), it expands (15) from the definitions.
    status: not yet asked. b1 has run and the assumption held: (15) was expanded
    from the definitions of Lambda_i and B_i and (16) is cited nowhere, so the row
    now costs nothing until the memoria wants to print (16).
    discussed in: docs/a0_framework.md c14.

s-02 | example 3.9's "w_i >= 0 not equal zero for all i": nonnegative and not all
    zero, or strictly positive?
    assumption: the former, the latter making statement 3 redundant.
    status: not yet asked, and now carrying a witness rather than only the
    redundancy argument. b1 found a point of p1, x = (4/3, 1) under phi_lu, that
    example 3.8 statement 3 certifies as an optimal and hence weak optimal
    solution and at which (15) holds for w = (0, 0, 1, 0) and for no strictly
    positive w, so the strict reading makes example 3.9 statement 1 false there.
    no b1 result depends on the answer: every optimality conclusion is drawn from
    example 3.8, whose weight condition is unambiguous, and the strict reading
    would cost only the necessity direction.
    discussed in: docs/a0_framework.md c14 and a-2, docs/b1_phi_efficient_sets.md
    section 6.

s-03 | [1]'s efficient solution for (12) requires no strictness, which is strong
    efficiency and not definition 3.1(2). which does theorem 3.1 mean?
    assumption: the usual pareto definition, as in definition 3.1(2) and pymoo.
    status: not yet asked; the two differ only when two decision vectors share an
    image, so the choice is recorded in b2 rather than assumed away.
    discussed in: docs/a0_framework.md.

s-04 | should CONTEXT.md section 2 record that [1]'s conclusion does compare two
    phi, under the quasilinear-space criterion?
    assumption: no amendment; the rule that part 1 may not rank phi is about what
    this study can measure, and [1]'s criterion is structural, not empirical.
    status: not yet asked, wording only.
    discussed in: docs/verified.md v-23.

s-05 | CONTEXT.md section 9 excludes sections 4 and 5 of [1], but section 5 holds
    proposition 5.1, which relates two of the three phi. does the exclusion stand?
    assumption: it stands for implementation; proposition 5.1 is a prediction to
    be checked, never a result the project asserts, and no analogue is derived.
    status: not yet asked, wanted before b1 or e3 touches section 5.
    discussed in: docs/a0_framework.md, a0-b addendum, and v-24 and v-26.

s-06 | computing the second image coordinate as f_u - f_l loses it at constant or
    near-zero width. should make_phi carry (centre, half_width) instead?
    assumption: both, which is what a3-b built. make_phi keeps the specified
    (f_l, f_u) signature and is unchanged; make_phi_of_centre_radius is the same
    phi in the other coordinates, and a problem declares which route applies to it.
    status: the row is narrower than a4-b framed it and is no longer blocking. the
    mathematics is unchanged: the composite is phi o M with det 2 det phi, so [1]'s
    definition on endpoint pairs and its admissibility condition both stand as
    written, and no order, efficient set or result depends on the route. what is
    left to ask is a presentation question for the memoria, whether the supervisors
    want the centre-radius form given as the working form of phi or kept as an
    implementation note.
    discussed in: docs/a4b_dominance_tolerance.md part 3, CONTEXT.md section 4,
    and v-41 and v-42.

s-07 | the step 1 degeneracy check runs on a uniform sample of the box, which
    zdt1 with half-width eps*x_n passes while phi_cw reproduces the crisp
    efficient set. should the check also run on the slice where that set lives?
    assumption: yes, and a1's tier 1 forms were chosen against the stronger check.
    status: not yet asked; a4 has built it, re-gridding the union bounding box of
    the three efficient sets and asserting separation there, and a5 repeats it.
    discussed in: docs/a1_uncertainty_model.md part 2 and a1-b.

s-08 | p1's phi-efficient set is a two-dimensional band and not a curve, and a1
    establishes that a curve and three distinct phi are not both available at two
    variables and two interval objectives. accept the band, or change p1's shape?
    assumption: accept the band. it gives spread and coverage two dimensions of
    structure, and b1 needs no axis bounds for it: every image coordinate is a
    quadratic with a constant hessian, so the closed form is the
    weight-parameterized stationarity map x(w) = -(sum_k w_k H_k)^-1 (sum_k w_k
    b_k) over the weight simplex, which b2 samples and pushes points through.
    status: answered as assumed, and b1 delivered what a4 predicted. the map is
    an explicit rational function of the weight vector for all three phi and the
    band has a closed-form boundary, two conic arcs for phi_lu, one for phi_ls and
    none for phi_cw, whose set is the unit square. the row can retire on the
    supervisors' acknowledgement.
    discussed in: docs/a1_uncertainty_model.md part 3 and a1-b section 3,
    docs/b1_phi_efficient_sets.md sections 2.2 and 2.4.

s-09 | tier 1 uses one absolute half-width for every objective, which on zdt1 is
    large relative to f_1 and small relative to f_2. scale it per objective?
    assumption: keep the common absolute width as the closest reading of slide 19
    and record the asymmetry in every tier 1 table.
    status: not yet asked, a one-line change in a5 if the answer differs.
    discussed in: docs/a1_uncertainty_model.md part 4.

s-10 | CONTEXT.md section 10 c2 justifies double seeding by pymoo's independent
    generator, but v-38 measures the opposite: minimize(seed=s) alone is
    bit-reproducible. keep the double seeding?
    assumption: keep it, since c1's own uniform sampling does need a seeded global
    state, so the instruction is right though its stated reason is inverted.
    status: not yet asked; CONTEXT.md was not edited, the section 11 licence being
    to correct against a paper, and a project diagnostic is not a paper.
    discussed in: docs/verified.md v-38.

s-11 | three questions about docs/a_close_containment.md, widened in a-close-b
    from the phi_lu case alone to the criterion both containments follow from.
    first, is the criterion correct? if phi_B = M phi_A with M entrywise
    non-negative and invertible then phi_A-dominance implies phi_B-dominance, so
    ND_B is contained in ND_A; non-negativity keeps every inequality and
    invertibility keeps the strict one. second, are both containments correct?
    M is [[1, 0], [1, 1]] from phi_ls to phi_lu and [[1, 1/2], [0, 1/2]] from
    phi_ls to phi_cw, both non-negative, so ND_lu and ND_cw both sit inside
    ND_ls, and no map into phi_ls or between phi_lu and phi_cw is non-negative.
    third, is any of it published? the phi_lu case is the interval-space analogue
    of proposition 5.1 of [1], which a0-b found nowhere in sections 2 or 3, the
    paper stating it for the fuzzy problems only; [1] cites its own [26] for
    LS-convexity and LS-Pareto so [26] is where it would sit, with [9] and [31]
    the other candidates. the phi_cw case and the criterion have no candidate
    location: v-25 records that [1] relates example 2.4's solution set to
    nothing, and the criterion is about the class and not about a pair of named
    examples.
    assumption: the project does not build on any of it. b1 derives from [1]'s
    own results and does not shorten a derivation with it, no test asserts the
    phi_cw containment, and d2 and e3 report the phi_ls pairs as checks on r-06
    and never as independent findings. it is recorded, not used.
    status: not yet asked. two consequences do not wait on it because they hold
    whichever way it is answered: CONTEXT.md section 10 c3 has the gate report the
    violation count as numerical noise, and a5's separation report prints the same
    two counts on its noise line. the e3 instruction added in a-close-b does
    depend on it and says so in place.
    discussed in: docs/a_close_containment.md, and v-24, v-25, v-26, v-46 and
    v-47.


## 7. risks

format: r-nn | risk / cost / trigger / mitigation

r-02 | [9] of [1], where the order relations on C that (3) decomposes are defined,
    is not among the five papers in scope.
    cost: b1 has no source for a property of those relations beyond (3).
    trigger: b1 needing such a property.
    mitigation: (3) states the relation fully in terms of phi_i and the order on
    R^2, so nothing is missing today; research chat if b1 needs more.

r-03 | the pdf of [1] is not in the repository and the extracted text lacks its
    reference list and two glyphs.
    cost: section 3's provenance claims and [1]'s own citations cannot be resolved.
    trigger: already realised in a0.
    mitigation: obtain the pdf; p-01 and p-02.

r-04 | example 3.9's hypotheses fail at p0's anchor x = 0, and b1 found the
    failure wider than this row stated: the differentiability hypothesis fails
    under all three phi, p0's first half-width being |x|, and theorem 3.3 refuses
    phi-convexity under phi_lu and phi_ls as well.
    cost: realised. p0's efficient set is not reachable from the optimality
    conditions under any phi, and under phi_cw they hold and are vacuous, the
    first image coordinate being identically zero.
    trigger: fired in b1.
    mitigation: the one this row named worked for the anchor. example 3.8
    statement 3 makes x = 0 an optimal solution under all three phi, so the
    published conclusion is recovered and the procedure is validated before p1.
    the sets come from definition 3.1 applied directly. the consequence is that
    p0 is a smoke test and not a b2 fixture, docs/b1_phi_efficient_sets.md
    section 7.4, and the row retires with that reasoning.

r-05 | example 2.1 shows the class permits different coefficients per objective,
    which none of the three implemented phi use.
    cost: nothing for the experiment; a reviewer may ask why one 2x2 map is fixed
    across all objectives when the framework does not require it.
    trigger: memoria review.
    mitigation: the answer is in docs/a0_framework.md c9 and CONTEXT.md section 4.

r-06 | corrected in a-close-b, the conditional removed and the phi_cw clause
    withdrawn. as raised in a0-b this read "if an interval analogue of
    proposition 5.1 holds, the phi_lu and phi_ls efficient sets are nested rather
    than merely different", and closed "the phi_cw comparisons are unaffected,
    v-25". the first half is no longer conditional and the second half is false.
    both ND_lu and ND_cw are contained in ND_ls, exactly, for every problem, so
    two of the three pairs are nested and only phi_lu against phi_cw is not.
    cost: "the sets differ" would present a containment as a free finding on two
    pairs and not one, and one direction of delta-coverage and of overlap is
    trivially complete on both. the phi_ls against phi_cw pair is the one the
    old wording would have let through unlabelled.
    trigger: e1 or e2 producing the decision-space metrics for either phi_ls
    pair, which is r-11's trigger as well.
    mitigation: report both phi_ls pairs as checks on the containment with it
    named, never as independent findings, and take the sensitivity signal from
    phi_lu against phi_cw, which is nested in neither direction. CONTEXT.md
    section 10 e3 now states this and states that it stands on s-11.

r-08 | a construction can pass every width-versus-centre statistic on a uniform
    sample and still give phi_cw the crisp efficient set, a uniform sample of a
    large box containing almost nothing near that set.
    cost: tier 1 would measure nothing while appearing to measure something, and
    the failure would surface only at e3.
    trigger: already realised for zdt1 with half-width eps*x_n, a1 part 2.
    mitigation: a1's width driver rule plus the slice check of s-07, built as a
    test in a4 and repeated in a5.

r-09 | a1's width driver rule was derived from two benchmarks and one tier 0
    design and has not been tested outside them.
    cost: a tier 1 or portfolio problem built on it could still be degenerate in a
    way not yet seen.
    trigger: f1 constructing interval returns, a different kind of problem.
    mitigation: treat it as a working rule and not a result, and run the full a1
    diagnostic including the slice check on every new problem before use.

r-11 | the phi_lu inside phi_ls nesting is a theorem in real arithmetic and
    fails by rounding in doubles, c + r and (c - r) + 2r not being the same
    double. a5 measured one violation, dtlz2 at eps = 0.50, one point of 1565,
    where the centre (1 + g) cos(x_1 pi/2) is 6.1e-17 against a half-width of 0.5.
    cost: d2's delta-coverage and any cross-evaluation of phi_lu against phi_ls
    will show a handful of points on the wrong side of a containment that is
    exact, and a table reporting them as a finding would be reporting arithmetic.
    trigger: e1 or e2 producing the phi_lu against phi_ls decision-space metrics,
    which is r-06's trigger as well.
    mitigation: v-46 states the exact result and the measured size of the
    artefact, and a5's test asserts the containment as a band and not as an
    equality; d2 reports the pair as a check on r-06 with the artefact named.
    this is not r-07: no endpoint is built and no round trip is performed, the
    cancellation is inside phi's own first coordinate c - r, and no representation
    a problem can declare removes it.

r-10 | retired in a3, r-01 in a4 and r-07 in a3-b. all three are in
    docs/answered.md with the reasoning that retired them.

## 8. session log

one line per session, appended after review. never edited once written; a
correction is a new entry. the detail behind each line is in that session's
commit message and in its docs/ deliverable.

format:

    date | subpart | files | outcome | next

2026-08-31 | a0 | docs/a0_framework.md | 15 claims checked against [1]: 12
    confirmed, 1 refuted, 1 partial, 1 split. 23 verified facts. CONTEXT.md
    corrected in sections 4, 6 and 11 | a1 or a2; a0 unblocks a3 and b1
2026-08-31 | a0-b | docs/a0_framework.md addendum; papers/ committed | proposition
    5.1 transcribed; no interval-space analogue anywhere in [1]. 6 facts added,
    1 corrected | s-05 to the supervisors before b1 or e3 uses section 5
2026-08-31 | a1 | docs/a1_uncertainty_model.md | degeneracy hypothesis confirmed
    in exact arithmetic; coefficient imprecision rejected; p1 proposed; CONTEXT.md
    section 10 a4 corrected | a1 reviewed before a4, a5 or b1's p1 branch
2026-08-31 | a2 | src/interval_math.py, tests/conftest.py,
    tests/test_interval_math.py, requirements.txt | six functions, 16 tests pass.
    gh_difference cited to a literature/ summary, raised as p-05 and r-10 | a3
2026-08-31 | a2, addendum after review | none | pymoo 0.6.2 and numpy 2.5.2
    confirmed compatible, v-36 to v-38. s-06 split between a2 and a3 recorded.
    s-10 raised | a3
2026-08-31 | a3 | src/phi_transforms.py, tests/test_phi_transforms.py,
    src/interval_math.py comment only | three phi built through make_phi, 29 tests
    pass. gh_difference re-cited to a primary source, v-39. r-10 retired | a4
2026-08-31 | a1-b | docs/a1_uncertainty_model.md section "a1-b, distinct widths",
    docs/verified.md, docs/answered.md, PROGRESS.md, CONTEXT.md | modified p1 keeps
    convexity, interiority and phi-separation and loses the product-of-intervals
    efficient set for phi_lu and phi_ls. PROGRESS.md restructured | research chat
    decides p1's widths; then a4
2026-08-31 | a4 | src/problems_tier0.py, tests/test_problems_tier0.py,
    PROGRESS.md, docs/answered.md, docs/verified.md, CONTEXT.md | p0 and p1 built,
    p1 in a1-b's distinct-width form, 13 tests pass and 42 in the suite. the r-08
    slice check is a test. s-08 re-answered on the stationarity map, r-01 retired,
    v-42 added, CONTEXT.md sections 11 and 12 amended | b1, or a5
2026-08-31 | a4-b | docs/a4b_dominance_tolerance.md, src/problems_tier0.py,
    tests/test_problems_tier0.py, PROGRESS.md, CONTEXT.md | the endpoint route's
    error measured at eps|c| and shown to shatter the width column's structural
    ties; an eleven-decade clean tolerance band found; delta changed to 1/8 as
    d-01 after exact verification; the (centre, half_width) route recommended as
    d-02, open. pymoo's epsilon argument shown to be a no-op | the research chat
    takes or rejects d-02; then a5
2026-08-31 | a3-b | src/phi_transforms.py, src/problems_tier0.py, their tests,
    CONTEXT.md, PROGRESS.md, docs/answered.md, docs/verified.md | the composite
    re-derived and checked before implementing; both routes built from one
    coefficient pair and one admissibility check; p1 now primary in centre and
    half-width and p0 in endpoints; the a4 rounding step deleted and a1-b's counts
    reproduced without it. 55 tests pass. d-02 closed, r-07 retired, s-06 narrowed
    to a presentation question, v-43 added | a5, which builds tier 1 in centre and
    half-width form
2026-08-31 | a5 | src/problems_tier1.py, tests/test_problems_tier1.py,
    papers/ two benchmark pdfs, docs/verified.md, docs/answered.md, PROGRESS.md |
    zdt1 and dtlz2 built in centre and half-width form from a1 part 4's widths,
    both declaring centre_radius and forming no endpoint, the crisp half-width
    exactly zero. the crisp objectives taken from [2] equation (7) and [3]
    equation (9), read in this session, v-44 and v-45. the separation sample is
    constructed from each benchmark's published crisp Pareto set rather than
    sampled, per r-08, and neither benchmark saturates: the three phi are
    distinct at all four levels with the non-dominated fraction between 0.03 and
    0.93. the phi_lu inside phi_ls nesting was found to fail by one point of 1565
    through rounding, v-46 and r-11. 22 tests, 115 in the suite. the a4-b against
    a3-b magnitude-sweep discrepancy recorded beside r-07 and not investigated |
    b1, which now has both tiers to derive against
2026-08-31 | a-close | docs/a_close_containment.md, docs/phase_a_summary.md,
    CONTEXT.md, PROGRESS.md, docs/answered.md | phase a closed. the phi_lu inside
    phi_ls containment verified three ways, symbolically through the project's own
    phi routes, by exhaustive rational case analysis covering both strictness
    branches, and on p0, p1, zdt1 and dtlz2 with an exact filter returning zero
    violations where doubles return the one v-46 records. p-03 closed by the proof
    and s-11 raised, two questions: is it correct, and is it published, [26] being
    where it would sit. the project does not build on it. CONTEXT.md section 10 c3
    gains the violation count as a numerical-noise measure, which holds either
    way. p-04 re-owned to e3 with the date it was missing. one observation
    recorded and not developed: the same map argument appears to put phi_cw's set
    inside phi_ls's too, which bears on r-06 and is for the research chat. 115
    tests pass | b1
2026-09-01 | a-close-b | tests/test_problems_tier1.py, docs/a_close_containment.md,
    docs/verified.md, CONTEXT.md, PROGRESS.md | a5's |ls&cw| shortfall on dtlz2
    run down and found to be arithmetic, not bookkeeping: the helper builds index
    sets over one array and reproduces exactly under a second implementation, 8 of
    8 cases, and all 39 points at eps = 0.50 are phi_ls-dominated in doubles and
    none in exact arithmetic. every number the helper prints was recomputed
    exactly; only the phi_ls and phi_lu columns move, the crisp set and |cw| being
    bit-identical. v-47. the report gains cw<ls, ls<cw and a noise line, which is
    the one thing that was wrong, a containment printed as a raw intersection with
    no noise count beside it; no computation and no assertion was wrong. the
    result generalised: phi_B = M phi_A with M non-negative and invertible gives
    ND_B inside ND_A, verified with both hypotheses removed in turn, and both
    containments follow from it, so ND_lu and ND_cw both sit inside ND_ls.
    CONTEXT.md section 10 e3 now takes the sensitivity signal from phi_lu against
    phi_cw. s-11 widened to three questions, r-06 corrected, its phi_cw clause
    withdrawn. 115 tests pass | b1
2026-09-01 | b1 | docs/b1_phi_efficient_sets.md, PROGRESS.md | the phi-efficient
    sets derived. condition (15) confirmed to be stationarity of the weighted sum
    before use, from [1] lines 715-723. p1: all ten image coordinates convex with
    constant psd hessians so theorem 3.3 gives phi-convexity globally under all
    three phi, regularity trivial by [10]'s midpoint-radius criterion, cited to
    the literature/ summary with the number unverified, p-05. (15) is a diagonal
    linear system and x(w) comes out as an explicit rational map for each phi,
    verified exactly on 3000 random weights per phi with the gradient identically
    zero. the singular weights characterised: none for phi_lu, and for phi_ls and
    phi_cw exactly the two rays putting all mass on one width coordinate, each
    giving a consistent system with a line of solutions and never an inconsistent
    one. the sets in closed form, two conic arcs bounding phi_lu, one bounding
    phi_ls, and phi_cw's set exactly the unit square; all three strictly interior
    to the box. optimality taken from example 3.8 statement 3 rather than example
    3.9 statement 3, uniqueness of a strictly convex minimiser covering zero
    weights too, with example 3.9 statement 1 closing the set from the other
    side. against a4's grid: 0 of 20000 derived points dominated under any phi,
    phi_cw exact at every resolution, and the phi_lu and phi_ls residue shown to
    be the finite grid, the excess distance fixed at 2.6 spacings while the
    absolute distance halves with the spacing and 0 of 289, 0 of 1418 and 0 of
    961 in-region points falling under a 24-fold local refinement. both
    containments reproduced from the closed forms independently of
    docs/a_close_containment.md. p0: hypotheses fail wider than r-04 stated, the
    anchor still recovered under all three phi by example 3.8, the sets only from
    definition 3.1 directly, and p0 recorded as a smoke test and not a fixture.
    s-02 gains a witness against the strict reading, s-08 answered, r-04 realised
    and mitigated. one thing does not close and was not patched: on the two
    singular segments the published conditions give weak optimality and no
    optimality verdict | b2, which encodes the map and the regions
