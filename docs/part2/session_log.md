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
