# phi-interval-opt: progress

state, not specification. the specification is CONTEXT.md and this file never
repeats it. edited by the human only, from session record blocks reviewed in the
research chat.

this file holds current state and open items only. everything settled lives
elsewhere:

    docs/verified.md    every verified fact, v-01 to v-41
    docs/answered.md    answered questions and retired risks
    git log             session-by-session detail, one commit per subpart

    highest numbers in use: v-41, p-05, s-10, r-10.
    numbering continues across those files and numbers are never reused.

project started 2026-08-30.

## 1. where the project stands

    current phase:      a, formulation
    current subpart:    a1-b, awaiting review (a0, a0-b, a1, a2 and a3 also
                        awaiting review)
    blocked on:         nothing
    files on disk:      docs/a0_framework.md
                        docs/a1_uncertainty_model.md
                        papers/new_preference_order_relationships_paper.txt
                        papers/Presentacion_optimizacion_intervalar.txt
                        src/interval_math.py
                        tests/conftest.py
                        src/phi_transforms.py
                        tests/test_interval_math.py
                        tests/test_phi_transforms.py
                        docs/verified.md
                        docs/answered.md
                        requirements.txt, versions pinned to the venv

## 2. subpart status

status is one of: not started, in progress, awaiting review, done, reopened.

phase a, formulation
    a0  verification pass over [1]          awaiting review
    a1  uncertainty model                   awaiting review
    a2  interval_math.py                    awaiting review
    a3  phi_transforms.py                   awaiting review
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

moved to docs/verified.md in session a1-b. the number is kept in place so that
every existing reference to "PROGRESS.md section 4", in the session log, in the
s-rows and in the commit history, still resolves to something.


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

p-05 | under which numbered definition does stefanini, arana-jimenez and sorini
    2025, [10] in the project's numbering, state the gh-difference, and does it
    print the collected closed form directly? narrowed in a3: the content is no
    longer open. v-39 establishes the two-branch definition, with its branch test
    on the interval length, from the presentation, slide 5 equation (2), which is
    a primary source in papers/, and gh_difference is now cited to it. what is
    still missing is only the definition number in [10] itself, wanted so the
    memoria can cite the journal article rather than a slide, and because
    CONTEXT.md section 6 also needs [10] for the midpoint-radius regularity
    criterion b1 uses. that second need is unchanged and is the reason to obtain
    the paper | b1 | narrowed, content settled by v-39, numbering still needs the
    paper itself |

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
    signature for now, and the constant-width check is carried in two halves, so
    the artefact cannot reach a result unnoticed. changing a specified interface
    is not a1's call.
    split recorded in a2, which found it could not carry the whole check: a2 has
    no phi and CONTEXT.md section 10 a2 forbids one, so a non-dominated set cannot
    be formed there. a2 carries the arithmetic half, that a constant-width
    construction returns a width constant to better than 1e-12 at centres of order
    1000 and exactly twice the half-width, in
    tests/test_interval_math.py::test_constant_width_construction_is_constant_up_to_rounding.
    a3 carries the whole of the non-domination half, that the constant-width case
    returns identical non-dominated sets under all three phi. the original wording
    of this row asked a2 for the non-domination half as well.
    both halves are now built. a3's is
    tests/test_phi_transforms.py::test_constant_width_collapses_the_three_phi_to_one_order,
    which applies each of the three phi to f -> [f - eps, f + eps], takes the
    non-dominated index set of each 2m-column image, and asserts the three are
    identical and equal to the crisp one. it gets a1's exact-arithmetic case by
    construction and not by tolerance: the crisp values are multiples of 2^-10
    below 2 and eps is 2^-6, so every endpoint, difference and half-sum involved
    is an exact double. its non-domination filter is local to that test file,
    since c1 and d2 own the real one. v-41 records that both a1 findings, the
    collapse and the rounding artefact, reproduce against the built phi
    | not yet asked |

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

s-10 | CONTEXT.md section 10 c2 says "set the seed both through numpy.random.seed
    and through minimize, because pymoo 0.6.2 builds its own generator
    independently". v-38 confirms the mechanism and measures the opposite
    consequence: because the generator is independent, the global seed does
    nothing for a pymoo run, and minimize(seed=s) alone is bit-reproducible for
    both nsga2 and mopso_cd. the sentence's reason does not support its
    instruction. should c2 keep the double seeding? | keep it. it costs one line,
    it is harmless, and c1's own uniform sampling and any numpy-level randomness
    the runners add do need a seeded global state, so the instruction is right
    even though its stated reason is inverted. a2 did not edit CONTEXT.md for
    this: the licence in section 11 is to correct against a paper that refutes,
    and a project diagnostic is not a paper | not yet asked |

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
    | a2 and a3 carry the constant-width test described in s-06, a2 the
    arithmetic half and a3 the non-domination half; the tier 1 eps=0 baseline sits
    exactly at the dangerous limit and is labelled degenerate already

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
