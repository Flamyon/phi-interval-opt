# phi-interval-opt: part 2 session log

part 2's session log, created in session lit-review on 2026-09-05 with that
session as its first entry. **part 1's log is docs/part1/session_log.md and is
closed at its docs-clean entry**; part 2's entries go here and not there, per
docs/part2/README.md.

same conventions as part 1's log. one line per session, appended after review,
**never edited once written**: a correction is a new entry. the detail behind each
line is in that session's commit message and in its docs/part2/ deliverable.

format:

    date | subpart | files | outcome | next

2026-09-05 | f1, as session lit-review | docs/part2/lit_review.md, new;
    docs/part2/README.md; docs/part2/session_log.md, new; PROGRESS.md sections 5
    and 7; docs/answered.md; CONTEXT.md section 10 f1 | **reading pass over six
    papers, no code, no run, no phi added to the registry.** [16]'s twenty
    appendix-A problems transcribed with n, m, the 2m column count, box,
    objectives and a per-criterion verdict against the gate of
    docs/part1/part1_closing.md section 7.2. **no example passes the gate and none
    fails it for want of trying**: criterion 3 cannot be answered by reading and
    not determinable is not a pass. **criterion 5 passes on nineteen of twenty** —
    the problems are ⊕_j [a_ij,b_ij] ⊙ h_ij(x), coefficient imprecision, the
    paper's own and credited to Mondal and Ghosh 2025 — and only I-CH fails it, as
    f(x) ± 1, which is also the constant-width degeneracy of part1_closing section
    6.1 occurring in a published problem. **five problems pass every criterion a
    reading can settle**, I-BK1, I-SD, I-IKK1, I-VFM1 and I-MHHM2; four close b1's
    route cheaply and I-SD closes it by a diagonal-but-not-constant Hessian route
    the plan did not anticipate. **I-BK1 is recommended**: it is p1's shape term
    for term and the only problem in the appendix with published checkpoints, a
    point in Table 1 and a closed-form curve at equation (25), both re-derived by
    hand this session and both exact. **I-IKK1 is recommended second and for a
    different weakness**: three of its six columns are single-variable functions,
    making it a third registered test of part1_closing section 3.4's
    protected-minimiser condition, and it is the one candidate outside the
    half-width alignment regime. [16]'s own order relation is definition 2.2 =
    example 2.2 of [1] = phi_lu, so its published points are phi_lu points and are
    directly usable; its definition 2.17 is [1] definition 3.1(1) exactly and its
    definition 2.16 is none of [1]'s three, sitting strictly between 3.1(2) and
    3.1(3). **[9] holds six order relations and not the four-and-a-fifth the plan
    expected**, the sixth being ⩽*_LC at equations (4.15)-(4.16) printed page 223,
    whose containment inside phi_lu and phi_cw the criterion predicts and **[9]'s
    own proposition 4.2 proves — a second independent confirmation of the
    containment criterion, on the minimisation side and on the project's own two
    registry members**. ⩽_cw of definition 3.2 is admissible and nested with none
    of the three, so it would be a finding; **it was not added to the registry**.
    **p-02 closed**, a_w is the half-width by [9]'s equation (2.4), its proof of
    proposition 4.1 and its example 1, three times over. **p-05 closed in both
    halves**: [10]'s theorem 34, printed page 13, is exactly what b1 cited from the
    summary, and its proposition 32, printed page 12, is the sufficient condition
    b1 actually used and is wider than a1's strict-positivity rule; the
    gH-difference has **no numbered definition in [10]** and the memoria must cite
    it by page or use [16] definition 2.1. **b1's derivation now has no unverified
    number.** [7], [8] and [13]'s objection transcribed from all three with printed
    pages, and the three shown not to lie in 𝔄_m for three different reasons —
    population dependence, an "or incomparable" disjunct in the aggregation, and a
    reference interval built from both intervals — with [8]'s per-objective
    relation being phi_lu itself. **[8] and [13] independently report the
    selection-pressure loss part1_closing section 4.3 measured, about their own
    direct methods.** [12] confirmed a duplicate of [7] by identical extracted text
    and distinct md5. [14] and [15] recorded as the future-work citation and not
    read. **ten ambiguities reported and none resolved**, including [16]'s Table 3
    row for I-TR1, which is computed from three runs and not the stated 100, and
    its invalid printed argument that x⋆ is Pareto optimal, which proposition 2.1
    supplies independently. **c5 is reachable and stays marked unsupported** until
    criterion 3 is answered. part 2's substantive arm priced at three sessions, two
    of them paper-and-pencil | f2, the derivation on I-BK1, **after the human takes
    the decision lit_review section 7.2 asks for**: whether the derivation comes
    before the separation check and answers criterion 3 exactly, reversing the
    order docs/plan_after_meeting.md section d1 anticipated

2026-09-05 | f2, the derivation on I-BK1 | docs/part2/f2_ibk1_derivation.md, new;
    PROGRESS.md sections 2, 6 and 7; docs/answered.md | **paper and pencil with
    exact rational symbolic verification, no module, no run, nothing from [16]
    implemented.** b1's method applied to a problem the project did not construct.
    the ordering decision lit_review section 7.2 asked for **was taken**: the
    derivation comes before the separation check and answers criterion 3 exactly
    rather than by sample, reversing docs/plan_after_meeting.md section d1. **the
    cheap check first**: under coefficient imprecision the centre and half-width are
    two combinations of the same h_ij with coefficients (a+b)/2 and (b-a)/2, and
    they are proportional exactly when every coefficient interval of that objective
    has the same relative half-width, which is part1_closing section 6.1's
    degeneracy; **no objective of any of the five candidates is proportional**,
    thirteen objectives checked in exact rationals, so the width-centre
    independence comes from the published coefficients and not from any choice of
    ours. **the derivation closes under all three phi with no reservation**, which
    p1 did under one of three: every one of the twelve image coordinates is a
    strictly positive diagonal quadratic, so theorem 3.3 gives phi-convexity with no
    semidefinite row, **there is no singular weight direction at all** and b1's two
    singular rays do not recur, every derived set is strictly interior to
    [-10,10]^2 with margin 5, and the sandwich collapses so that optimal = weak
    optimal = X_phi exactly under all three. [10] proposition 32 is **load-bearing
    and not a formality**: I-BK1's radii vanish at (0,0) and (5,5), which are the
    two corners every derived set is pinned at, and a strict-positivity rule would
    have left a hole there. the sets are wedges: with U = x_1/(5-x_1),
    V = x_2/(5-x_2) and nu = V/U, **X_lu is nu in [2/3,5/3], X_ls is [1/2,2] and
    X_cw is [3/4,3/2]**, each a region between two hyperbolas through (0,0) and
    (5,5), given as pairs of polynomial inequalities, verified in both directions in
    exact rationals. **criterion 3 passes and I-BK1 passes the gate**: X_cw strictly
    inside X_lu strictly inside X_ls, areas 2.8756, 3.7903, 5.6853 in closed form,
    overlap fractions 0.7587, 0.6667 and 0.5058, and every crisp comparator is a
    one-dimensional curve of constant nu. **two of the three relations are predicted
    by the containment criterion and are checks; X_cw inside X_lu is not predicted
    and is a finding**, and it differs in kind from p1, where phi_lu and phi_cw
    crossed. **the external checks split.** equation (25)'s published curve is
    exactly nu = 162/169 constant, **inside all three derived sets along its whole
    length**, with eight of Table 2's eleven rows on it and two more at its
    corners; that is the first external
    check the project has ever had and it passes. **Table 1's x* is outside all
    three**, nu = 0.1109, and the failure is located in the paper, not in the
    derivation: **x* is not a Pareto optimal point of I-BK1 in [16]'s own definition
    2.17**, shown by an explicit dominator y = (2.8975, 2.3975) whose four endpoint
    values are all strictly below the paper's printed G(x*), tightest margin 0.2740
    against a printed rounding of 1e-6. the mechanism is identified: the interval
    directional derivative's Minkowski sum overestimates, so **[16]'s Pareto
    critical set is nu in (1/9, 10), area 16.07, 4.24 times X_lu and containing all
    three derived sets**, and x* is the algorithm's output at tolerance just outside
    it. **a-11: [16]'s proposition 2.1 and lemma 2.4(ii) are false as printed**,
    with x = (5/2, 5/6) a Pareto critical point of I-BK1 that is dominated in all
    four coordinates and every hypothesis verified; lemma 2.4 is attributed to [27],
    not on disk, so the session does not say where the proof fails. **lit_review's
    a-4 is resolved in the negative**: the printed argument is invalid and the
    conclusion is false, and the rescue through proposition 2.1 does not survive.
    **a-12: Table 2's alpha = 0.8 row carries the alpha = 0.9 row's second
    coordinate**, (25) giving 4.235294 against the printed 4.628566, with the row's
    objective values computed from the printed value. **s-02 gains a second witness
    and a structural one**: every weight reaching a boundary ray of any derived set
    has two zero components, so reading two makes example 3.9 statement 1 false
    along a whole curve. r-09 discharged for I-BK1 by derivation rather than
    diagnostic, r-21 retired, s-12 recorded as p1's alone. **clause c5 stays marked
    unsupported**: the gate is passed but c5 is about measured behaviour under the
    project's instrument and that is f3's | f3, the reference set and the exact
    statistics, **after the research chat rules on a-11**, which is the one finding
    this session raises that bears on whether [16]'s published points may be used at
    all


2026-09-05 | f3, the module and the native run | src/problems_native.py, new;
    experiments/run_native.py, new; tests/test_problems_native.py, new;
    tests/test_run_native.py, new; docs/part2/f3_native_run.md, new and generated;
    results/part2/, new; CONTEXT.md section 12; PROGRESS.md sections 1 and 2 |
    **the application stage: the instrument calibrated on p1 and extended to two
    benchmarks, applied to a problem that is interval-valued at source and that
    the project did not construct.** two files because the second is meaningless
    without the first. **src/problems_native.py holds I-BK1 as [16] states it**,
    coefficients cited to printed page 27, representation declared "endpoints"
    because every h_ij is a square and Moore's product does not interchange the
    boundary functions there, so the published coefficients compute the endpoints
    and nothing rebuilds them from a centre and a radius, d-02. **no uncertainty
    was added and no width function was written.** it also encodes f2 section
    2.4's three wedges as pairs of integer-coefficient inequalities cleared of
    denominators, so membership carries no tolerance and the two corners need no
    case split, and samples them through the (nu, x_1) parametrisation with b2-b's
    farthest-point correction, the mode stated by the caller with no default per
    r-13. **experiments/run_native.py is the run**: all three solvers, all three
    phi, five seeds, budget 5000 with the convergence check at 20000, 18
    configurations, 90 runs, 24 figures, 1714 s, every number in the record read
    back out of a file the run wrote. **table 1 exists and that is the point**:
    the areas 2.8756, 3.7903 and 5.6853 reproduce f2 section 3.1 to six decimals
    by a second route, an antiderivative in the band against a grid count of the
    inequalities, and the pairwise coverages are 1.0 and 0.666692 on (lu, ls),
    0.758670 and 1.0 on (lu, cw), 0.505799 and 1.0 on (ls, cw). **the instrument's
    error, measured a second time and on a problem of a different origin**: at
    delta zero and budget 5000 the relative error is +0.251677 on cov(ls in lu),
    +0.074414 on cov(lu in cw), +0.482801 on cov(ls in cw) and +0.137192,
    +0.003818 and +0.275886 on the three dice overlaps; six of the nine rows
    measure above the exact value, two land exactly on it and one measures below.
    **every magnitude is inside the +0.810049 e1 measured on p1**, so the stopping
    rule the brief states was not triggered and nothing was adjusted to fit.
    **the two rows that land exactly on the exact value are the two containments**,
    ND_lu inside ND_ls and ND_cw inside ND_ls, and the recovered sets carry both
    with a containment violation count of zero, so r-11's rounding artefact does
    not occur on I-BK1 at all. **the one row that measures below, -0.088235, is
    cov(cw in lu)**, the direction no containment covers: f2's nesting X_cw inside
    X_lu is about the derived regions and the finite non-dominated sets of a
    sample need not nest for that pair. **the headline convention does not apply
    here and the record says so plainly**: all three pairs nest on I-BK1, so one
    direction of every pair is fixed before anything runs and no row of this run
    is a measured difference between two orders; two of the three are the
    criterion's checks and X_cw inside X_lu is f2's finding about the problem.
    **the counterexample reproduces independently and by a different route**: run
    without being told any of it, every solver under every phi at every seed
    returns points dominating [16]'s Table 1 x* in the paper's own definition 2.2,
    medians of 5 to 15 points at budget 5000 and 4 to 40 at 20000, widest margin
    0.269627 against f2's algebraic 0.273966. reported as a measurement; the claim
    about the paper stays f2's. **x-01's condition is structurally absent**: none
    of the twelve image columns has a non-empty free set and none is constant,
    which is what f2 section 1.2 predicts from the forms, so m-2 is not computed
    and I-BK1 is the first problem in the project where the effect is absent under
    every phi. igd exists here where it did not at tier 1, the derived sets
    supplying a reference, and include_singular_segments is False everywhere as a
    no-op, I-BK1 having no singular weight direction. objective metrics at the
    common cardinality 100, r-16, so this block and e1's full-cardinality one may
    not be placed side by side. **c5 is not declared supported**: the run reports
    the evidence and f4 states the claim | f4, part 2's write-up, which is where
    c5 is judged and where a-11 has to be disposed of

2026-09-05 | f4, part 2's write-up | docs/part2/part2_closing.md, new;
    PROGRESS.md sections 1 and 2; docs/part2/session_log.md | **no experiment, no
    module, no run, no new claim and no new number except the one judgement the
    brief asks for.** part 2's canonical record, modelled on
    docs/part1/part1_closing.md and written so that g1 opens nothing else for part
    2's results; every part 2 figure read out of an f2 or f3 artefact with the file
    named, every part 1 figure quoted from part1_closing with the tier 0 or tier 1
    file that document names. **clause c5 is judged, and narrower than the draft**:
    supported in the form that on a problem published by a third party and
    interval-valued in its own coefficients the three orders give three distinct
    phi-efficient sets with the difference exact -- bands [3/4,3/2] inside [2/3,5/3]
    inside [1/2,2], areas 2.875612, 3.790332 and 5.685282, 0.494201 of the largest
    outside the smallest -- reproduced by the project's own instrument with a
    relative error of -0.088235 to +0.482801 at budget 5000, every magnitude inside
    p1's +0.810049; **not** supported in part 1's own terms, because all three sets
    nest and part 1's headline quantity, how much of each of two non-nested sets
    lies outside the other, has no counterpart on I-BK1; and not supported as a
    statement about interval-native problems in general. **the second calibration
    point is delivered and its result is that the magnitude does not transfer**: by
    the identity measured jaccard over exact jaccard the factor is 1.2517, 1.0067
    and 1.4828 on the three pairs against p1's 1.81, so 1.81 is a property of p1's
    geometry, which is what part1_closing section 7.3 said a second point would
    decide; **the sign does transfer**, six of nine rows above the exact value, one
    below and that one the direction no containment covers, two exactly on it.
    **the hausdorff weakness is not removed** -- exact_regions_ibk1.csv carries no
    hausdorff either -- and the geometry question is untouched, as lit_review 7.2
    said in advance it would be. **two conventions stated once.** delta: I-BK1 is
    the convention's third distinct failure, its box being [-10,10]^2 while the
    derived sets live in [0,5]^2, so the standard 0.05 box fraction is a fifth of
    the sets' own diameter and saturates every cross-phi statistic and the noise
    floor alike at 1.000000; with p1's tuning failure and tier 1's dimension
    failure that makes **delta zero the only readable value in the project, for
    three different reasons**. budget: **the response is not one-directional on
    I-BK1**, five of nine rows moving toward the exact value, two away and two
    exact at both budgets, so part1_closing section 3.2's uniform-budget leg does
    not survive and what survives is the sign measured directly against a known
    answer plus the magnitude being inside p1's. **the counterexample is written as
    a correction to a published result**, in that order: the transcription
    confirmed against [16]'s own printed G(x*) and its printed gH-gradients, then
    y = (2.8975, 2.3975) with the four inequalities and the tightest margin
    0.273966 against a printed rounding five orders of magnitude smaller, then the
    independent reproduction -- 18 of 18 configurations, 5 of 5 seeds each, medians
    5 to 15 at budget 5000 and 4 to 40 at 20000, widest margin 0.269627 -- then the
    mechanism, the Minkowski sum's overestimate making [16]'s Pareto critical set
    nu in (1/9,10), 4.24 times X_lu, with x* at tolerance just outside it, and the
    limits last. **a-11 is disposed of**: the memoria cites neither proposition 2.1
    nor lemma 2.4(ii), does not use Table 1's x* as a fixture, uses equation (25)'s
    curve which passes, records a-4 as resolved in the negative and a-12 beside it,
    and **where the proof fails is not claimed**, lemma 2.4 being attributed to a
    reference not on disk. **the nesting is recorded as an observation with a
    mechanism and not as a result**: the wedge structure in nu explains why the
    disagreement on I-BK1 is one-dimensional and does not force the nesting, which
    is the ordering of six ratios of published coefficients, and one problem of each
    kind cannot establish that adapted problems cross and native ones nest.
    **I-IKK1 is named as the problem that would decide it** -- interval-native with
    p1's single-variable width structure, so it separates "adapted against native"
    from "these coefficients against those", and a third registered test of x-01 on
    three columns at once -- at two sessions and with no published checkpoint.
    x-01's structural absence on I-BK1 recorded, 0 of 12 columns with a free set.
    the fallback of docs/plan_after_meeting.md section d2 recorded as **not
    needed**, its text being lit_review sections 1.8, 1.9 and 6 and owed to the
    memoria anyway. **phase f is complete** | g1, the results document, whose two
    inputs now both exist; and, before it, the research chat's disposition of a-11
    and a-12 toward the authors, which this document records and does not decide

2026-09-06 | f5, boundary-function interchange and the last problem's shortlist |
    docs/part2/f5_boundary_interchange.md, new; docs/part2/session_log.md |
    **audit, reading and diagnostics. no problem added to src/, no derivation, no
    fix to evaluation semantics, and nothing committed but the document and this
    line.** **the headline is the audit and it is a defect, not a wrong result: the
    project implements the fixed-order endpoint reading and not definition
    2.1(iii) of [16].** src/interval_math.py has no interval-product primitive at
    all -- its six callables are add, scalar_multiply, centre, half_width, width
    and gh_difference -- and objective_endpoints in src/problems_native.py computes
    (sum a_j h_j, sum b_j h_j) in fixed order. **tested rather than read**: I-VU2's
    G_1 pushed through the module's own arithmetic returns lower > upper at every
    point with x_1 < 0, and phi_ls and phi_cw carry it forward as **negative
    widths**, 3 of 7 sampled points, because **nothing in src/ asserts f_l <= f_u**.
    **correct on everything ever run and silently wrong in general**; the fix is
    its own session and r-23 is proposed, its cheaper half being the missing guard
    rather than the missing primitive. **no problem already run can trigger it**,
    per problem with the reason: p0 has no product, p1 and both tier 1 benchmarks
    have half-widths non-negative by construction, and I-BK1's four h_ij are
    squares -- 200000 points per box, f_l <= f_u everywhere. **the substantive
    result is a check lit_review did not run**: part1_closing section 6.1's
    degeneracy is decidable exactly from the printed coefficients, since r_i is an
    affine function of c_i iff rho_j = (b_j-a_j)/(a_j+b_j) is constant across the
    non-constant terms, and **eight of the twenty appendix-A problems have at least
    one objective that fails it**, five of them on every objective -- I-CH
    (constant width, part1_closing 6.1 verbatim in a published problem), I-FON,
    I-Hil1, I-TR1 and I-Comet. **any objective that is one coefficient on one
    function is degenerate**, which disposes of I-AP1 and I-AP4, lit_review's two
    "not determinable" rows, on a ground it did not have: two of three objectives
    each are phi-blind. **five of the twenty interchange** -- I-VU2, I-CH, I-Hil1,
    I-Viennet, I-Comet -- and I-KW2's and I-PNR's sign-changing factors carry
    degenerate coefficients and interchange nothing, correcting lit_review 1.9's
    prose without moving its verdicts; I-Viennet's ⊖gH kink is **not** reached,
    correcting lit_review 1.8. **the crossing meets the answer, and the
    phi-dependence is a mechanism**: under phi_cw and phi_ls the second image
    column is the half-width sum w|h|, minimised exactly on the locus, so the order
    pulls the efficient set onto it -- 12/161, 205/400 and 780/780 of sampled
    crossing points survive on I-CH, I-Viennet and I-Comet against 0, 4 and 0 under
    phi_lu. **on I-VU2 it is exact, not a grid statement**: the origin, where both
    crossing loci meet, is efficient under all three phi because three of the four
    columns attain their global minimum there. **that is p0's obstruction on a
    published problem** -- G_1's lower boundary function 1.25(x1+x2) -
    0.25(|x1|+|x2|) + 1 is concave so theorem 3.3 fails for phi_lu and phi_ls
    globally, example 3.9's differentiability fails on the loci under all three by
    a0 c14's invertibility argument, and the kink sits at the answer -- reached
    from Moore's product rather than written into the problem, and on two lines
    rather than one point. **four candidates, no pick, by instruction**: I-SD for
    novelty (first n > 2 and first non-polynomial derivation, closing by the
    diagonal-but-not-constant route, risking the two ends of its efficient set on
    faces and a 3-D set in a 4-D box), I-IKK1 for decision value (settles
    part2_closing section 4, third x-01 test, no checkpoint), I-VU2 for the
    crossing -- **the only appendix-A problem that interchanges and is not
    disqualified otherwise, so the sign-changing slot and the expected-failure slot
    collapse onto one problem**, with G_2 phi-blind at r = c/5 as its cost -- and
    I-MHHM2 as the floor. **s-14 proposed**, whether example 3.9 statements 2 and
    3's phi-convexity is theorem 3.3's global form as printed or remark 2.2's
    pointwise one, which decides whether a crossing costs phi_lu and phi_ls their
    sufficiency on the whole box or only on the locus. **and a sixth gate criterion
    proposed**, the 6.1 check of section 3.2, which the gate of part1_closing 7.2
    currently has nothing that would have caught | the research chat's choice of
    the last problem, with this comparison in front of it; and, separately, the
    session that fixes evaluation semantics and adds the well-ordering guard

2026-09-06 | f6, the interval product and the interval invariant | src/interval_math.py;
    src/problems_native.py; src/problems_tier0.py; tests/test_interval_math.py;
    tests/test_problems_tier0.py; tests/test_interval_invariant.py, new;
    CONTEXT.md sections 10 a2, 10 a4 and 12; PROGRESS.md sections 1 and 7;
    docs/answered.md; docs/part2/f5_boundary_interchange.md;
    docs/part2/session_log.md | **code and tests, no new problem, no derivation
    and no measured number changed**, which is asserted and not stated. the two
    halves of r-23 are built. **the product**: src/interval_math.py gains
    multiply and multiply_by_real, the minimum and the maximum over the four
    endpoint products, elementwise over numpy arrays so a sign change inside one
    array is resolved entry by entry, and objective_endpoints in
    src/problems_native.py calls it instead of computing (sum a_j h_j, sum b_j
    h_j) in fixed order. **one locator corrected against the paper and only the
    locator**: ⊙ is item (iii) of the unnumbered operations display of [16]
    **section 2.1, printed page 4**, not "definition 2.1(iii), printed page 3",
    definition 2.1 on that page being the gH-difference; the content is
    unchanged. cross-checked, per the evidence rule: **[9] defines the operation
    as the set of products of the members**, its definition 2.1 equation (2.5)
    printed page 220, and prints no closed form, and **[1] states no product at
    all**, so [16] is the corpus's only printed source and neither of the other
    two contradicts it. **the guard**: f_l <= f_u, which is r >= 0 in centre and
    half-width coordinates, checked at the one interface every problem shares --
    Problem wraps every evaluate it is given -- so tier 0, tier 1, the native
    problems and any problem a later session adds are covered by construction. it
    **raises** and does not assert, an assert being removed by python -O, and it
    **runs always**: measured on f3's own configuration, 0.361 ms of a 0.711 s
    nsga-ii run at the gate budget, 0.05 per cent, and 0.003 ms of the 0.818 ms
    20000-row random search call. **nothing moved, asserted rather than read**:
    the product and the fixed-order reading agree bitwise at all 40401 points of a
    201 x 201 grid of I-BK1's whole box, the non-negativity of every h_ij that
    makes them agree is asserted on the same grid, the invariant holds on a dense
    sample of every box of every problem of every registry, and [16]'s printed
    G(x*) still reproduces at the printed precision through the new path.
    **f5's own diagnostic is a test now**, I-VU2's G_1 across its sign change well
    ordered at all seven of f5's points where the fixed-order reading returned
    three reversed, and the guard fires on a constructed ill-ordered problem in
    both representations with a message naming the objective and the point. **613
    pass fast against 592 before f6, and the full run is 1123 passed and 12
    xfailed**, the twenty-one new tests being six on the product, six on the
    guard and nine in tests/test_interval_invariant.py; no existing test is
    changed, newly skipped or newly xfailed | g1, the results document, and the
    research chat's choice of the last problem; **s-14 and the proposed sixth
    gate criterion are untouched by this session** and stay where f5 left them

2026-09-06 | f7, I-VU2 derived and the boundary of the transformation approach |
    docs/part2/f7_ivu2_derivation.md, new; PROGRESS.md sections 1 and 6;
    docs/answered.md; docs/part2/session_log.md | **paper and pencil with exact
    rational verification. no module, no run, no problem added to src/, no test
    changed and nothing from [16] implemented.** **s-14 is answered from the
    printed text and answered against the weakening**: [1] definition 2.2 printed
    page 5 defines both "φ-convex" (8), global on S, and "φ-convex at x*" (9);
    examples 3.4 to 3.7 printed pages 7 and 8 use the pointwise form four times
    with "continuously differentiable **at x̄**" beside it; example 3.9 printed
    page 10 uses the unqualified form in statements 2 and 3 **and in its
    differentiability preamble**, which f5 did not ask about and which matters
    more here. so b1's reading is the printed one. **and the answer changes
    nothing on I-VU2**: under the pointwise reading F is phi_lu- and
    phi_ls-convex at exactly one point, the origin, which is the one point where
    the differentiability fails independently, so example 3.9's statements 2 and
    3 are unavailable at every point of the box under phi_lu and phi_ls under
    either reading. **the derivation closes under phi_lu and does not close under
    phi_ls or phi_cw, and the reason is not the crossing**: a singular weight ray,
    w ∝ (1,3,0,0) under phi_ls and (1,5,0,0) under phi_cw, on which the scalarised
    objective is constant on the quadrant holding the whole answer, so (15) holds
    everywhere on it and example 3.8 statement 4 cannot pin the optimal set below
    it — b1 section 2.3's phenomenon on a published problem, two-dimensional
    rather than one-dimensional, and s-12 recurring. **the order that keeps
    theorem 3.3 is the one that does not close and the order that loses it is the
    one that does**, which corrects f5 section 4.1's reading of where the damage
    falls. **the crossing's own failure is exhibited and not asserted**: the
    candidate set (15) produces on the open quadrants is the open segment
    {(t, t/2) : −4 < t < 0}, the origin is its limit point and is not in it, and
    at the origin the first expression of (15) is undefined under all three phi
    because each ∇Λ_i^T f and ∇B_i^T f is required separately. **the origin is a
    strong optimal solution under all three phi by definition 3.1(1) printed page
    6**, proved from one column of objective 2 per phi and the positive
    definiteness of U = x_1²+2x_2², with no differentiability and no convexity,
    and certified a second time by example 3.8 statement 3 at w = (0,0,w_3,w_4);
    (15) cannot produce it and example 3.8 can, which is the boundary in one
    sentence. **the interiority reading costs an arc here** where it cost nothing
    on p1 and I-BK1, the answer containing the face piece {(−4,s) : −4 ⩽ s ⩽ −2}.
    **criterion 3 fails exactly**: all three phi-efficient sets equal the L-shaped
    curve E = {(t,t/2)} ∪ {(−4,s)} and equal the crisp centre problem's, because
    the interchange makes r_1 = (1−c_1)/5 on the third quadrant — part1_closing
    6.1's degeneracy with **negative** slope, created by the crossing — while G_2
    is phi-blind at r_2 = (c_2+1)/5, so both objectives are degenerate where the
    answer is. **that corrects f5 section 3.5's "G_1 is not degenerate", which is
    true of the box and false where it matters, and does not reverse f5's
    choice.** the containment corollaries hold as checks and the un-predicted
    (lu, cw) pair is an equality, the project's third distinct answer on that pair
    after p1's crossing and I-BK1's strict nesting. **no external check exists**:
    [16] prints for I-VU2 only Table 3's iteration statistics, printed page 23,
    and Figure 3(a), printed page 24, and no solution point, so none is claimed;
    what is checked is that E lies inside [16]'s own Pareto critical set of
    definition 2.18 printed page 7, computed in closed form as the cone
    2/9 ⩽ x_2/x_1 ⩽ 9/8 and agreeing with an 8000-direction scan at 70 points,
    and that Table 3's minimum iteration count of 0 over 100 random starts is
    consistent with that cone being one ninth of the box while E has measure zero.
    **I-VU2 is not a second counterexample to [16] proposition 2.1 or lemma
    2.4(ii)**, both of whose hypotheses it fails independently; only a-11's
    mechanism recurs. x-01 is structurally absent, all twelve columns depending on
    both variables | g1, the results document; the research chat's disposition of
    s-14, of f5's proposed sixth gate criterion, and of whether s-12 gains I-VU2
    as a second instance
2026-09-06 | f8, part 2 closed on a second pass, I-VU2 folded in |
    docs/part2/part2_closing.md, extended by four sections with nothing in it
    rewritten; PROGRESS.md sections 1 and 2; docs/verified.md, v-60 and v-61;
    docs/part2/session_log.md | **no run, no module, no derivation, no new number
    and no new claim.** every figure in the added sections is read out of an f5,
    f6 or f7 artefact with its section named, and the four sections are
    **appended** rather than inserted so that every locator another document
    already cites still points where it pointed. **the decision, recorded with its
    reason and not as an omission: I-VU2 is not run.** f7 establishes by
    derivation that its three phi-efficient sets are equal to each other and to
    the crisp centre problem's, because the boundary interchange creates
    part1_closing section 6.1's degeneracy on the quadrant holding the whole
    answer while G_2 is phi-blind before the interchange is considered at all, so
    **a run would measure the crisp problem three times**: no pair, no coverage,
    no overlap, nothing to compare, and nothing to calibrate either, the sets
    being derived rather than estimated. part2_closing section 10.7.
    **I-VU2 is written throughout as the boundary of the transformation approach
    and not as a fourth comparison**, section 10: the derivation closes under
    example 2.2 and not under 2.3 or 2.4, and the obstruction is a **singular
    weight ray** on which the scalarised objective is constant across the quadrant
    holding the answer — b1 section 2.3's phenomenon one dimension up, s-12
    recurring — so **the order that keeps theorem 3.3 is the one that fails to
    close**; the crossing's own failure is separate, additional and exhibited,
    (15)'s candidate set being the open segment whose limit point the origin is
    and is not in, and at the origin (15) cannot be written at all because no
    gradient of an individual image coordinate exists; and **the origin is
    nevertheless a strong optimal solution under all three phi by definition
    3.1(1)**, which is the section's strongest sentence and is written to be
    lifted — a point whose optimality is provable while the machinery that
    generates candidates provably does not apply there. **s-14 is settled and
    settles against the weakening**, [1] definition 2.2 printed page 5 with
    example 3.9's differentiability preamble printed page 10, and it
    **retroactively confirms b1's reading rather than changing it**. **the two
    corrections are stated as the current reading and not as history**: f5 section
    4.1 expected the crossing to be the obstruction and it is not, and f5's "G_1
    is not degenerate" is true of the box and false on the quadrant where the
    answer lives, so criterion 3 fails on I-VU2 **exactly**; both are corrections
    to a reading and not to a measurement, and no number moves. **what part 2 is,
    written out in section 11**: the twenty-problem corpus read and screened
    twice, **two problems derived and one run** — I-BK1 derived, run and the
    second calibration point; I-VU2 derived and deliberately not run — plus f6's
    code work, which changed no number, plus the correction to [16], which stands
    unchanged. **there is no third problem**: the two-asset portfolio problem of
    [16] section 6 printed page 26 was **not examined**, lit_review section 5.2
    naming it for the memoria's future-work paragraph only and the meeting of
    2026-09-04 having moved the portfolio out of scope, and that is recorded with
    its reason rather than left to a count. **clause c5 is re-judged in section 12
    on the full evidence and does not move**: I-VU2 adds no comparison and no
    measured number, so the magnitude arm is **untouched, neither strengthened nor
    weakened**, and no third calibration point exists; what it does add is **the
    first published interval-native problem on which the three orders coincide**,
    so the wider plural form of the clause is not merely unsupported but known not
    to hold as a universal, and that limit is now printed beside the clause with
    the regime test that decides it — part1_closing section 6.1's condition, read
    **on the region where the efficient set lives and not on the box**, which is
    the one refinement I-VU2 forces on f5's screen. **f6 is recorded as a
    precondition of f7 and not an improvement to it**, section 10.8: I-VU2 is the
    first problem the project has touched that exercises the guard, **2071 of 4000
    sampled points ill ordered under the pre-f6 fixed-order reading against 0
    under Moore's product**, and the 2071 are exactly the half of the box that
    holds the entire answer. **two v-rows registered from f6's cross-check**,
    docs/verified.md: **v-60**, ⊙ is item (iii) of the unnumbered operations
    display of [16] section 2.1, **printed page 4**, and not "definition 2.1(iii),
    printed page 3", which points at the gH-difference — the memoria cites this
    operation, so the locator must be right; and **v-61**, the verified negative
    that [16] is the corpus's only printed closed form for the product, [9]'s
    definition 2.1 equation (2.5) printed page 220 giving the set of products with
    no closed form and using only the sum and the real multiple, and [1] equipping
    the space with ⊞ and ⊡ alone, which is why the project ran this long without
    an interval product. **no external check on I-VU2 is claimed and none exists.**
    **part 2 is closed and no further test problem is in scope** | phase g: the
    figures, the presentation, the memoria and, if time allows, the paper — g2,
    g4, g3 and g1. I-IKK1 stays as future work, part2_closing section 7.2; and the
    research chat still holds the disposition of a-11 and a-12 toward the authors,
    of s-14's residue, of f5's proposed sixth gate criterion, and of whether s-12's
    row gains I-VU2 as a second instance
