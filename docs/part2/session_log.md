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

