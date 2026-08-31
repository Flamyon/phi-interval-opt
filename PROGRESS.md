# phi-interval-opt: progress

state, not specification. the specification is CONTEXT.md and this file never
repeats it. edited by the human only, from session record blocks reviewed in the
research chat.

this file holds current state and open items only. everything settled lives
elsewhere:

    docs/verified.md    every verified fact, v-01 to v-42
    docs/answered.md    answered questions and retired risks
    git log             session-by-session detail, one commit per subpart

    highest numbers in use: v-42, p-05, s-10, r-10.
    numbering continues across those files and numbers are never reused.

project started 2026-08-30.

## 1. where the project stands

    current phase:      a, formulation
    current subpart:    a4, awaiting review (a0, a0-b, a1, a1-b, a2 and a3 also
                        awaiting review)
    blocked on:         nothing
    files on disk:      docs/a0_framework.md, docs/a1_uncertainty_model.md,
                        docs/verified.md, docs/answered.md
                        papers/new_preference_order_relationships_paper.txt
                        papers/Presentacion_optimizacion_intervalar.txt
                        src/interval_math.py, src/phi_transforms.py,
                        src/problems_tier0.py
                        tests/conftest.py, tests/test_interval_math.py,
                        tests/test_phi_transforms.py, tests/test_problems_tier0.py
                        requirements.txt, versions pinned to the venv

## 2. subpart status

status is one of: not started, in progress, awaiting review, done, reopened.

phase a, formulation
    a0  verification pass over [1]          awaiting review
    a1  uncertainty model                   awaiting review
    a2  interval_math.py                    awaiting review
    a3  phi_transforms.py                   awaiting review
    a4  problems_tier0.py                   awaiting review
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

decisions taken in the research chat and closed. a decision is reopened only with
a reason recorded here as a new entry, never by editing the old one.

format:

    d-nn, date. one sentence stating the decision.
        why: the reason.
        source: the paper, example or file it rests on, or "project judgement".
        affects: the subparts it constrains.

none yet.

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

p-03 | does an interval-space analogue of proposition 5.1 appear outside [1],
    whose own [9], [26] and [31] are the candidates? | b1 | open, blocked on p-01

p-04 | does any construction in [7] or [8] drive the interval width from the
    decision vector rather than by a constant band? | a5 | open, needs the two
    papers themselves

p-05 | under which numbered definition does [10] state the gh-difference? | b1 |
    narrowed in a3, content settled by v-39; the paper is still wanted for the
    number and for the midpoint-radius criterion CONTEXT.md section 6 gives b1

## 6. questions only the supervisors can answer

each carries the working assumption the project proceeds on. none blocks work. if
an answer differs from the assumption, record it as a decision in section 3 and
list the subparts that have to change.

format: s-nn | question / assumption / status / discussed in

s-01 | (16) of [1] is inconsistent in the w subscripts on the beta terms: the
    expanded line carries w_2i, the collected line w_2i-1. which is intended?
    assumption: b1 does not cite (16), it expands (15) from the definitions.
    status: not yet asked, costs nothing until b1 runs.
    discussed in: docs/a0_framework.md c14.

s-02 | example 3.9's "w_i >= 0 not equal zero for all i": nonnegative and not all
    zero, or strictly positive?
    assumption: the former, the latter making statement 3 redundant.
    status: not yet asked, and any b1 result turning on a zero weight carries the
    ambiguity explicitly.
    discussed in: docs/a0_framework.md c14 and a-2.

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
    assumption: a3 keeps the specified (f_l, f_u) signature, since changing a
    specified interface is not the agent's call.
    status: not yet asked; both halves of the guard are built and passing, the
    arithmetic half in a2 as v-42 and the non-domination half in a3 as v-41, and
    a4 met the artefact again and rounds before every non-domination filter.
    discussed in: docs/a1_uncertainty_model.md part 1, and v-41 and v-42.

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
    status: re-answered in a4. the old answer rested on the set being a product of
    intervals whose x_2 bounds do not depend on x_1; a1-b removed that premise for
    phi_lu and phi_ls, and it was the wrong criterion anyway. b1 is expected to
    produce the map, not a bounding box.
    discussed in: docs/a1_uncertainty_model.md part 3 and a1-b section 3.

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

r-04 | example 3.9's hypotheses fail at p0's anchor x = 0 under phi_lu, both image
    coordinates of the first objective being non-differentiable there.
    cost: b1's "is the published conclusion recovered" check may not close by the
    planned route.
    trigger: b1 starting p0.
    mitigation: example 3.8, or definition 3.1 directly, or the research chat;
    a4 carries the same warning at src/problems_tier0.py's p0_anchor.

r-05 | example 2.1 shows the class permits different coefficients per objective,
    which none of the three implemented phi use.
    cost: nothing for the experiment; a reviewer may ask why one 2x2 map is fixed
    across all objectives when the framework does not require it.
    trigger: memoria review.
    mitigation: the answer is in docs/a0_framework.md c9 and CONTEXT.md section 4.

r-06 | if an interval analogue of proposition 5.1 holds, the phi_lu and phi_ls
    efficient sets are nested rather than merely different.
    cost: "the sets differ" would present a containment as a free finding, and one
    direction of delta-coverage would be trivially complete.
    trigger: e1 producing the phi_lu against phi_ls decision-space metrics.
    mitigation: report that pair as a check on s-05's prediction, not as an
    independent finding; the phi_cw comparisons are unaffected, v-25.

r-07 | computing an image coordinate as f_u - f_l is unsafe at constant or near
    zero width, the cancellation being the whole second coordinate of phi_ls and
    phi_cw.
    cost: a degenerate construction presents as the three phi differing, which
    reads as a positive result, so arithmetic could be reported as a phi effect.
    trigger: already realised, in the a1 diagnostic and again in a4, where ulp
    noise in (c + r) - (c - r) kept 9 dominated points in ls and 17 in cw.
    mitigation: the a2 and a3 halves of s-06, v-42 and v-41; a4 rounds before
    every non-domination filter; the eps=0 tier 1 baseline is labelled degenerate.

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

r-10 | retired in a3, and r-01 in a4. both are in docs/answered.md with the
    reasoning that retired them.

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
