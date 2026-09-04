# phi-interval-opt: progress

state, not specification. the specification is CONTEXT.md and this file never
repeats it. edited by the human only, from session record blocks reviewed in the
research chat.

this file holds current state and open items only. everything settled lives
elsewhere:

    docs/verified.md    every verified fact, v-01 to v-57
    docs/answered.md    answered questions and retired risks
    docs/session_log.md the whole session log, moved out of section 8 in
                        repo-clean. this file keeps the last three entries
    docs/supervisor_questions.md
                        the full text of every open s-row. section 6 is the index
    git log             session-by-session detail, one commit per subpart

    highest numbers in use: v-59, p-06, s-13, r-21, d-06, and x-02 for the
    registered predictions of section 9, which is new.
    numbering continues across those files and numbers are never reused.

project started 2026-08-30.

## 1. where the project stands

    the meeting:        the supervisors' meeting of 2026-09-04 happened.
                        **its decisions are in docs/meeting_2026_09_04.md and the
                        plan they produced is docs/plan_after_meeting.md**, which
                        is the document to read before the next session. five
                        things changed: part 1 is accepted as a controlled test on
                        adapted problems and nothing is retracted; phase e proceeds
                        as specified; more phi may be searched for subject to the
                        framework's conditions; **part 2 is no longer the portfolio
                        application but the interval-native problems of [16]**, with
                        the portfolio recorded as future work; and **the corpus is
                        open**, every paper being in papers/ and every previous
                        paper-level exclusion lifted. four artefacts are due on
                        25 september: a paper-like results document, a latex
                        memoria, the code repository and a short presentation with
                        no implementation detail
    current phase:      d, analysis. **phase c is complete and tagged
                        phase-c-complete**, closed out in
                        docs/phase_c_summary.md. its gate does not pass: twelve of
                        ninety reverse measurements exceed the corrected
                        tolerance, every one of them nsga-ii, and the failure is
                        understood and is a finding rather than a defect
    current subpart:    d3, reporting.py, **built and awaiting review**. the
                        tables and the figures e1, e2 and e3 produce, and the
                        point at which a restriction holding in the code has to
                        still hold in the artefact. the objective-space and the
                        decision-space metrics go into two blocks with different
                        columns, each under the restriction it is read subject to,
                        written in the file and not in a caption, so a reader
                        holding the csv alone cannot make a comparison the metrics
                        do not support. **a row lacking a required field is
                        refused and the field is named**: the seed count, the
                        budget, the cardinality and a median with an interquartile
                        range on every row; the reference size, the sampling mode,
                        include_singular_segments and the hypervolume reference
                        point with the rule that produced it on an objective row,
                        r-12, r-13 and s-12; delta, the scale of the decision box
                        and the pair's status on a decision row, r-06 and r-11.
                        no metric is computed there and the labels are not
                        re-declared, check and finding coming from d2, the
                        reference-point rules from d1 and the sampling modes from
                        b2. every figure carries the budget, the seed count and
                        the cardinality of each series inside the figure and never
                        in a filename, and plot_decision_sets draws b1 section
                        2.4's closed-form region behind the recovered sets where
                        the problem is p1. **plot_convergence is not built**:
                        src/runners.py records no per-generation history, a
                        SearchResult carrying the final front alone, and adding
                        the recording is a change to c2 and was not this
                        session's. **d1 moves to done**, its review evidenced by
                        this session's prompt, which reads d1 as amended, asks d3
                        to render what d1 and d2 produce and asks for d1's two
                        pymoo findings to be recorded where e1 and e3 will need
                        them; b2-b and d2 moved to done in d1 on d1's prompt,
                        which reads b2-b's correction as the reference d1 must use
                        and d2's shape as settled. next is e1.
                        c3-f is done, its review evidenced by c-close's prompt,
                        which accepts its decomposition and asks for the close-out.
                        c3-c is
                        done, its review evidenced by c3-d's prompt, which accepts
                        its corrections and asks one diagnostic question about
                        section 5; c3-d is done, its review evidenced by c3-e's
                        prompt; c3-e ran and **never committed**, its session
                        ending before it wrote, and its measurements are recorded
                        for the first time in docs/c3_validation.md sections 5.2
                        to 5.4 by c3-f, which also carries its own review of them
                        in its prompt. c1 is done, its
                        review evidenced by c2's prompt; c2 is done, its review evidenced by c2-b's
                        prompt, which reverses one of its choices; c2-b is
                        done, its review evidenced by c3's prompt, which quotes
                        its findings into CONTEXT.md sections 10 c2, 10 d1 and 11;
                        c3 is done, corrected in c3-b, its review evidenced by
                        c3-b's prompt, which reverses its forward assertion; and
                        c3-b is done, its review evidenced by c3-c's prompt, which
                        corrects three things c3-b left: the missing proposition
                        behind the forward floor, the sampled quality measure, and
                        the tolerance; and c3-c is done, its review evidenced by
                        c3-d's prompt. b1 and b2 are done and
                        phase b is complete and, since d2-b, tagged
                        phase-b-complete at b2's commit, its close-out
                        docs/phase_b_summary.md. phase a is complete: a0, a0-b,
                        a1, a1-b, a2, a3, a3-b, a4, a4-b, a5 and a-close are all
                        done and docs/phase_a_summary.md is the close-out
                        document
    blocked on:         nothing, and that is a decision and not an absence. the
                        gate fails in twelve of ninety, all nsga-ii, three seeds
                        under phi_ls and three under phi_cw and none under phi_lu,
                        docs/c3_validation.md sections 3 and 4. what those twelve
                        say is r-19: nsga-ii's decision-space coverage of a
                        full-dimensional efficient set is worse than uniform
                        random sampling at equal cardinality. no solver returns a
                        point that beats the derivation anywhere, ninety of
                        ninety, so the derivation, b2's encoding and all three
                        solvers agree about where the efficient set is and two of
                        the three cover it to within the derivation's own
                        resolution. phase e starts carrying the six items of
                        docs/c3_validation.md section 10
    phase d depends on: **no open row blocked d2**, the only phase d subpart on the
                        minimum path, and it is built. what it carries rather than
                        waits on, every row of it in src/metrics_decision.py:
                        s-12 and r-12, include_singular_segments has no default
                        and its value goes in every table beside the seed and the
                        point count, the two settings being two different
                        reference objects; r-11 and r-06, the phi_lu inside phi_ls
                        containment is exact in real arithmetic and fails by
                        rounding in doubles, one point of 1565 measured, so d2
                        reports that pair as a check with the artefact named and
                        never as a finding; s-11, which is what makes that pair a
                        check rather than a finding, and if the supervisors refute
                        the criterion the instruction is removed and all three
                        pairs are reported alike; r-16, cardinality is printed
                        beside every metric; and r-15, whose trigger names d2
                        filtering large sets repeatedly and whose mitigation
                        rules out the one speed-up available, pymoo's
                        NonDominatedSorting, as a decision against CONTEXT.md
                        section 5. **d1's two prerequisites were met before it
                        was built**: r-13's mitigation is b2-b, and d1 computes
                        igd against that reference and nothing else, and r-12's
                        trigger, d1 computing igd, has fired with
                        include_singular_segments stated on every reference d1
                        builds. both values travel on the record igd_reference
                        returns rather than on the call site. r-19 bears on how e3
                        reads a spread statistic, not on whether d2 can be
                        written
    the suite:          995 tests after d3's 66, of which twelve parameter sets of
                        test_the_derived_set_is_reached_by_the_solver at nsga-ii
                        fail on purpose and are marked xfail(strict=True) in
                        repo-clean-b, pinned to nsga-ii under phi_ls at seeds 11,
                        13 and 14 and under phi_cw at 12, 13 and 14, both flag
                        settings. **the assertion is unchanged and still runs on
                        all ninety**: strict means a thirteenth failure is a
                        plain failure and an unexpected pass is an error, which
                        is what records that the finding has not moved. this is
                        not what c3-c refused, which was exempting nsga-ii from
                        the assertion or marking the six configurations
                        non-strict xfail. docs/c3_validation.md sections 4.1
                        and 5
    files on disk:      docs/a0_framework.md, docs/a1_uncertainty_model.md,
                        docs/a4b_dominance_tolerance.md,
                        docs/a_close_containment.md, docs/phase_a_summary.md,
                        docs/b1_phi_efficient_sets.md,
                        docs/verified.md, docs/answered.md,
                        docs/phase_c_summary.md, docs/supervisor_questions.md,
                        docs/session_log.md, docs/phase_b_summary.md,
                        docs/project_narrative.md,
                        docs/b2b_reference_density.md
                        papers/new_preference_order_relationships_paper.txt
                        papers/Presentacion_optimizacion_intervalar.txt
                        papers/zitzler_deb_thiele_2000_comparison.pdf
                        papers/deb_thiele_laumanns_zitzler_2002_scalable.pdf
                        src/interval_math.py, src/phi_transforms.py,
                        src/problems_tier0.py, src/problems_tier1.py,
                        src/reference_fronts.py, src/random_search.py,
                        src/runners.py, src/metrics_decision.py,
                        src/metrics_objective.py, src/reporting.py
                        docs/c3_validation.md
                        tests/conftest.py, tests/test_interval_math.py,
                        tests/test_phi_transforms.py, tests/test_problems_tier0.py,
                        tests/test_problems_tier1.py, tests/test_reference_fronts.py,
                        tests/test_random_search.py, tests/test_runners.py,
                        tests/test_validation.py, tests/test_metrics_decision.py,
                        tests/test_metrics_objective.py, tests/test_reporting.py
                        requirements.txt, versions pinned to the venv
                        pytest.ini, holding the slow marker and nothing else.
                        repo-clean widened the marker from "runs a solver" to
                        cover a large-sample diagnostic as well and marked four
                        such tests, docs/session_log.md

## 2. subpart status

status is one of: not started, in progress, awaiting review, done, reopened.

phase a, formulation. complete, tagged phase-a-complete.
    a0  verification pass over [1]          done
    a1  uncertainty model                   done
    a2  interval_math.py                    done
    a3  phi_transforms.py                   done
    a4  problems_tier0.py                   done
    a5  problems_tier1.py                   done, corrected in a5-b
    a5-b tier 1 width drivers                **new, not started**. a5 shares one
                                            width function across a problem's
                                            objectives, so under examples 2.3 and
                                            2.4 the image carries duplicate columns
                                            and the transformed problem has three
                                            effective objectives where zdt1 has four
                                            and four where dtlz2 has six, while
                                            under example 2.2 it has all of them.
                                            the duplication is phi-dependent, so the
                                            headline comparison on tier 1 confounds
                                            the order with the transformed
                                            dimension. a5-b gives each objective its
                                            own driver as p1 has and re-runs a1 part
                                            4's slice sweep on the new forms.
                                            CONTEXT.md section 10 a5,
                                            docs/plan_after_meeting.md section b4.
                                            **precedes e2**

phase b, ground truth. complete, tagged phase-b-complete in d2-b, the tag naming
b2's commit; its close-out document is docs/phase_b_summary.md, written after the
fact in repo-clean-b. b2-b came after the tag and during phase d, r-13's
mitigation being a prerequisite for d1 and for nothing else.
    b1  phi-efficient sets, derivation      done
    b1-b the closed form along the path      **new, not started, optional**. the
         phi_t from example 2.4 to 2.2       one-parameter family
                                            [[1, -(1-t)], [1, 1]] in centre and
                                            half-width coordinates has determinant
                                            1 + (1-t)^2 > 0, so it is admissible by
                                            [1]'s own condition at every t; on p1
                                            every member has convex image
                                            coordinates and constant diagonal
                                            hessians, so b1's route closes with t
                                            carried as a symbol and the overlap with
                                            X_cw becomes a function of t rather than
                                            three numbers. one session, no runs, and
                                            it strengthens the calibration rather
                                            than the exploration.
                                            docs/plan_after_meeting.md section c3.
                                            **first optional session, taken only if
                                            two scheduled sessions finish early**
    b2  reference_fronts.py                 done
    b2-b the reference front's density       done

phase c, solvers
    c1  random_search.py                    done
    c2  runners.py                          done, corrected in c2-b
    c2-b archive and cardinality             done
    c3  validation gate                     done, corrected in c3-b
    c3-b the gate's assertions, restated     done, corrected in c3-c
    c3-c the three corrections               done, gate fails and is asserted
    c3-d the saturation diagnostic           done, no code changed
    c3-e the pullback diagnostic             done, no code changed, never committed
    c3-f the frame, the control, the closed   done, no code changed
         forms
    c-close phase c close-out                done, no code changed

phase c is complete, tagged phase-c-complete. its close-out document is
docs/phase_c_summary.md and the accumulated supervisor questions are
docs/supervisor_questions.md.

phase d, analysis
    d1  metrics_objective.py                done, off the minimum path
    d2  metrics_decision.py                 done
    d3  reporting.py                        awaiting review, off the minimum path

CONTEXT.md section 8's minimum presentable path is a0, a1, a2, a3, a4, b1, b2,
c1, c2, c3, d2, e1: tier 0 only, with the decision-space metrics and the
correctness gate. **d2 is the only phase d subpart on it.** d1 and d3 were built
as the calendar allowed and are not prerequisites for e1. **d1 is built**, so
r-12's and r-13's triggers have both fired rather than gone quiet: it computes igd
against b2-b's corrected reference and states include_singular_segments on every
reference it builds, both values travelling on the record igd_reference returns.
r-16's trigger fired with them and its mitigation is code and no longer a
recommendation. **d3 is built**, so the recording those three mitigations require
is enforced where the numbers leave the process: a table whose row omits the mode,
the flag, the reference size, the reference point with its rule, the cardinality,
the budget, the seed count, delta, the box scale or a phi pair's status is refused
with the field named, and nothing is written.

phase e, experiments
    e1  tier 0 run                          not started. **next session**
    e2  tier 1 run                          not started, waits on a5-b and on e1
    e3  results synthesis                   not started. its subject is unchanged
                                            except that it no longer selects a phi
                                            to carry into part 2, part 2 now running
                                            all three

phase f, part 2. **every subpart rewritten on 2026-09-04, identifiers kept and
subjects changed**, CONTEXT.md section 10 f1 to f4 and docs/plan_after_meeting.md
section a2. what they were: f1 yfinance and 30 s&p 500 assets, f2 portfolio
optimization under the selected phi, f3 an out-of-sample backtest against
markowitz, equal-weight and risk parity, f4 the answer to "which phi is better".
the portfolio application is future work, where slide 21 of the supervisors'
presentation places it.
    f1  reading pass over [16], with the      not started. document only. **runs in
        gate                                  parallel with e1 and e2** and gates f2
    f2  problems_native.py                    not started, waits on f1 passing an
                                              example
    f3  the native run, plus its derivation   not started, waits on f2 and on e2
    f4  part 2 write-up                       not started, waits on f3, or on f1
                                              alone in the fallback form

phase g, the write-up. **new on 2026-09-04.** three of the four artefacts due on
25 september; the fourth is the repository itself.
    g1  the results document                not started, waits on e1 and e3
    g2  the figure set                      not started, can start on e1's output
    g3  the latex memoria                   not started, waits on g1 and g2, and on
                                            the two email-today items of
                                            docs/plan_after_meeting.md section h3
    g4  the presentation                    not started, waits on g3's frozen claim
                                            sentence and g2's figures

## 3. decisions

decisions taken in the research chat and closed. a decision is reopened only with
a reason recorded here as a new entry, never by editing the old one. one line per
field; the reasoning each rests on is in the source named.

format: d-nn, date, status | decision | source | affects

d-01, 2026-08-31, closed | p1's default delta becomes 1/8, replacing a1-b's 1/10
    | docs/a4b_dominance_tolerance.md part 2, which verifies in exact integer
    arithmetic that delta is an additive constant on every image coordinate and
    that all three efficient index sets are identical | a4, done; b1 and b2
    inherit the constant; a1-b's tables were measured at 1/10 and are unchanged
    by it

d-02, 2026-08-31, closed | every phi image is computed from the representation
    the problem declares, and one untoleranced dominance relation is used
    everywhere | docs/a4b_dominance_tolerance.md for the measurements, the
    composite re-derived and checked in a3-b on 2000 random rational coefficient
    sets, and CONTEXT.md section 4 | a3, which gained make_phi_of_centre_radius
    and a paired registry; a4, which gained Problem.representation; a5, built in
    centre and half-width form; b2, c1, c2 and d2, which compare with no
    tolerance

d-03, 2026-09-01, proposed in c2, reversed in c2-b before it was taken, and
    awaiting the research chat in the c2-b form | mopso_cd's archive truncation
    is drawn from the algorithm's own seeded generator, at pymoo's default
    archive_size of 200 | project diagnostic, v-48 and v-51, with the pymoo 0.6.2
    source read in c2 and c2-b; the candidate rejected is archive_size =
    pop_size * n_gen, sized so the truncation is never reached, rejected for
    changing mopso's leader pool and for costing roughly quadratically in the
    budget, docs/session_log.md c2-b, its cost at v-57 | c2, rebuilt this way in
    c2-b; c3, e1 and e2, which no
    longer pay the resize's cost; r-14 and r-15; and if it is taken, CONTEXT.md
    section 10 c2 needs a clause for the one override, which only the research
    chat can write

d-04, 2026-09-04, taken at the supervisors' meeting | **part 2's subject changes
    from the portfolio application to the interval-native test problems of [16],
    and the corpus is open**: every paper is in papers/ and the paper-level
    exclusions of CONTEXT.md section 9 are lifted | the meeting of 2026-09-04,
    decisions 4 and 5, docs/meeting_2026_09_04.md;
    docs/plan_after_meeting.md sections a2 and e | CONTEXT.md sections 2, 3, 4, 6,
    8, 9, 10 e3, 10 f1 to f4, 11 and 12; f1 to f4, rewritten in place; e3, which no
    longer selects a phi; r-03, which retires; s-05, which is moot; p-01, p-02,
    p-04, p-05 and p-06, which become answerable

d-05, 2026-09-04, proposed in this session and awaiting the research chat |
    **a5's shared width function is replaced by one driver per objective**, zdt1
    r_1 on x_30 and r_2 on x_29, dtlz2 r_1, r_2 and r_3 on x_12, x_11 and x_10,
    each keeping the functional form a1 part 4 argued for | the duplication is
    phi-dependent, so the transformed problem has four effective objectives under
    example 2.2 and three under example 2.4 on zdt1, and six against four on dtlz2,
    which confounds the study's headline pair with the transformed dimension;
    a1-b measured the analogous correction on p1, where phi_cw's efficient set was
    bit-identical either way while phi_ls moved from 1271 to 1505 grid points;
    docs/plan_after_meeting.md section b4 | a5, corrected in a5-b; a1 part 4, whose
    slice sweep is re-run on the new forms per r-08 and s-07; e2, which does not
    start before a5-b. **nothing already built is re-run**: e2 has not started, b1
    does not cover tier 1 and c3's gate is tier 0 only. it does not answer s-09

d-06, 2026-09-04, closed at the meeting | **the deliverable format is four
    artefacts**: a paper-like results document, a latex memoria, the code
    repository, and a short presentation with no implementation detail | the
    meeting of 2026-09-04 | phase g, new; CONTEXT.md sections 8 and 10 g1 to g4;
    the number-provenance rule now binding e1, e2, f3 and phase g, CONTEXT.md
    section 10 e1. **still unstated and blocking g3**: the memoria's expected
    length and its language, docs/plan_after_meeting.md section h3

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
    then b1 | **open and now answerable**: the pdf of [1] is in papers/ since
    2026-09-04 and it carries its reference list. it stops being a wait and becomes
    a reading task, and resolving [1]'s own [9], [26] and [31] is what would settle
    the third part of s-11

p-02 | does ishibuchi and tanaka 1990, [9], state the centre-width comparison in
    the same coefficients as example 2.4 of [1]? | b1 | **open, and substantively
    answered from the paper, which is in papers/ since 2026-09-04**: definition
    3.4, equations (3.11) and (3.12), a_c <= b_c and a_w <= b_w for minimisation,
    with a_w the half-width by the paper's own equation (4.6), a_R = a_L + 2 a_w.
    docs/plan_after_meeting.md section c2. **the row stays open** because that
    reading was made while surveying papers/ and not in a session that recorded
    printed page numbers, which the evidence rule requires; the session that does
    so closes it, and it should also record definitions 3.1, 3.2, 3.3 and equation
    (4.1), which are three further order relations the project has never looked at

p-04 | does any construction in [7] or [8] drive the interval width from the
    decision vector rather than by a constant band? | e3 | **open and now
    answerable**: both pdfs are in papers/ since 2026-09-04, and [13] is a third
    source of the same kind. the paragraph below was written when they were absent
    and its contingency no longer applies. the owner moves from a5 to e3 in
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
    then b2 | **open and now answerable**: [10]'s pdf is in papers/ since
    2026-09-04. this is the one unverified number in b1's derivation and it can be
    closed by a reading session before the memoria cites it. what follows is the
    row as it stood. b1 needed the criterion and had to cite it as
    "theorem 34" from literature/gH-differentiability calculus for interval
    analysis.md with the number unverified, [10] not being in papers/. the outcome
    of the check is not in doubt for p1, every function involved being a
    polynomial with a strictly positive radius, and b1 does not rest on the
    number; the paper is still wanted so the memoria can cite it properly

p-06 | does [1] anywhere identify the "strict minimum" it asserts at x = 0 for the
    worked function after example 3.9 with one of definition 3.1's three named
    concepts? | b1 | **open and now answerable** with [1]'s pdf, in papers/ since
    2026-09-04, and wanted before the memoria prints p0's status. the paper's words are "a strict minimum", which is not
    one of the three names, and a0 found no sentence joining them. definition
    3.1(1) is the plausible reading, being the only one stated through the same
    relation, but a4-b demoted it from a claim to an inference in both
    CONTEXT.md section 10 a4 and p0's comment

## 6. questions only the supervisors can answer

each carries the working assumption the project proceeds on. none blocks work.
**nine are open after the meeting of 2026-09-04.** none of the nine was asked at
that meeting, which spent its time on direction rather than on readings; they are
still worth asking and docs/supervisor_questions.md is still the version to send.
if an answer differs from the assumption, record it as a decision in section 3 and
list the subparts that have to change.

what the meeting settled: **s-08 is answered as assumed** and retires, decision 1
accepting part 1's results as they stand and the two-dimensional band being what
b1 derived and what the meeting document presented; **s-05 is moot**, the
paper-level exclusions of CONTEXT.md section 9 having been lifted, so proposition
5.1 may be read and cited like any other published result, the retained working
rule being only that the project does not assert an interval analogue of a fuzzy
proposition without deriving it. both are in docs/answered.md with the reasoning.
**s-11 gains a project-side reading task rather than an answer**: its third part,
whether the criterion is published, is no longer unanswerable inside the project
now that [1]'s pdf and its reference list are in papers/, and section c2 of
docs/plan_after_meeting.md has already found that ishibuchi and tanaka's
proposition 4.1 agrees with the criterion on a case the criterion decides.
**s-09 is untouched by decision d-05**: distinct width drivers and per-objective
scaling are independent choices.

**docs/supervisor_questions.md is the version the supervisors read** and holds
the full text of every row: the question, the working assumption, what depends on
the answer and where it is written up. this section is the index into it and
nothing else. s-13 is closed and is in docs/answered.md.

format: s-nn | question | working assumption | where the full text is

s-01 | which w subscripts (16) of [1] intends, the expanded line's w_2i or the
    collected line's w_2i-1 | the project does not cite (16); b1 expands (15)
    from the definitions of Lambda_i and B_i | docs/supervisor_questions.md
    s-01, docs/a0_framework.md c14

s-02 | example 3.9's "w_i >= 0 not equal zero for all i", nonnegative and not all
    zero or strictly positive | the former, the strict reading making statement 3
    redundant and making statement 1 false at a witness b1 found |
    docs/supervisor_questions.md s-02, docs/b1_phi_efficient_sets.md section 6

s-03 | which efficiency theorem 3.1 means, [1]'s no-strictness form being strong
    efficiency and not definition 3.1(2) | the usual pareto definition, as in
    definition 3.1(2) and pymoo | docs/supervisor_questions.md s-03,
    docs/a0_framework.md

s-04 | should CONTEXT.md section 2 record that [1]'s conclusion does compare two
    phi, under the quasilinear-space criterion | no amendment; the rule that part
    1 may not rank phi is about what this study can measure and [1]'s criterion
    is structural | docs/supervisor_questions.md s-04, docs/verified.md v-23


s-06 | should make_phi carry (centre, half_width), the second image coordinate
    being lost at constant or near-zero width if computed as f_u - f_l | both,
    which is what a3-b built, and what is left is the presentation question for
    the memoria | docs/supervisor_questions.md s-06,
    docs/a4b_dominance_tolerance.md part 3

s-07 | should the step 1 degeneracy check run on the slice where the efficient
    set lives as well as on the box | yes, and a1's tier 1 forms were chosen
    against the stronger check, which a4 built as a test and a5 repeats |
    docs/supervisor_questions.md s-07, docs/a1_uncertainty_model.md part 2


s-09 | one absolute half-width for every tier 1 objective, or one scaled per
    objective | keep the common absolute width as the closest reading of slide 19
    and record the asymmetry in every tier 1 table | docs/supervisor_questions.md
    s-09, docs/a1_uncertainty_model.md part 4

s-10 | keep the double seeding, CONTEXT.md section 10 c2 justifying it by a pymoo
    generator that v-38 measures the opposite way | keep it, since c1's own
    uniform sampling does need a seeded global state, so the instruction is right
    though its stated reason is inverted | docs/supervisor_questions.md s-10,
    docs/verified.md v-38 and v-48

s-11 | is the entrywise-non-negative containment criterion correct, are both
    containments correct, and is any of it published | the project does not build
    on any of it: b1 derives from [1]'s own results, no test asserts the phi_cw
    containment, and d2 and e3 report the phi_ls pairs as checks on r-06 |
    docs/supervisor_questions.md s-11, docs/a_close_containment.md

s-12 | are the points of the singular weight segments optimal solutions for
    (1MIOP_phi), the published conditions giving weak optimality and no verdict
    either way | b2 does not choose and does not patch:
    include_singular_segments has no default and the value goes in every table |
    docs/supervisor_questions.md s-12, docs/b1_phi_efficient_sets.md section 2.6

## 7. risks

open risks only, in the four fields CONTEXT.md section 11 requires and nothing
beyond them. the measurements, the diagnoses and the rejected candidates each row
accumulated are in the deliverable named in its mitigation.

format: r-nn | risk / cost / trigger / mitigation

r-02 | [9] of [1], where the order relations on C that (3) decomposes are
    defined, is not among the five papers in scope.
    cost: b1 has no source for a property of those relations beyond (3).
    trigger: b1 needing such a property.
    mitigation: (3) states the relation fully in terms of phi_i and the order on
    R^2, so nothing is missing today; research chat if b1 needs more.

r-05 | example 2.1 shows the class permits different coefficients per objective,
    which none of the three implemented phi use.
    cost: nothing for the experiment; a reviewer may ask why one 2x2 map is fixed
    across all objectives when the framework does not require it.
    trigger: memoria review.
    mitigation: the answer is in docs/a0_framework.md c9 and CONTEXT.md section 4.

r-06 | both ND_lu and ND_cw are contained in ND_ls, exactly and for every
    problem, so two of the three phi pairs are nested and only phi_lu against
    phi_cw is not.
    cost: "the sets differ" would present a containment as a free finding on two
    pairs, one direction of delta-coverage and of overlap being trivially
    complete on both.
    trigger: e1 or e2 producing the decision-space metrics for either phi_ls
    pair, which is r-11's trigger as well.
    mitigation: report both phi_ls pairs as checks on the containment with it
    named and take the sensitivity signal from phi_lu against phi_cw; CONTEXT.md
    section 10 e3 states this and states that it stands on s-11;
    docs/a_close_containment.md.

r-08 | a construction can pass every width-versus-centre statistic on a uniform
    sample and still give phi_cw the crisp efficient set.
    cost: tier 1 would measure nothing while appearing to measure something, and
    the failure would surface only at e3.
    trigger: already realised for zdt1 with half-width eps*x_n,
    docs/a1_uncertainty_model.md part 2.
    mitigation: a1's width driver rule plus the slice check of s-07, built as a
    test in a4 and repeated in a5.

r-09 | a1's width driver rule was derived from two benchmarks and one tier 0
    design and has not been tested outside them.
    cost: a tier 1 or portfolio problem built on it could still be degenerate in
    a way not yet seen.
    trigger: **f2 building an interval-native problem from [16]**, a different
    kind of problem, and a5-b's new width drivers. the trigger read "f1
    constructing interval returns" while part 2 was the portfolio application.
    mitigation: treat it as a working rule and not a result, and run the full a1
    diagnostic including the slice check on every new problem before use. f1's
    criterion 3 records it per example and f2 discharges it as an assertion.

r-11 | the phi_lu inside phi_ls nesting is a theorem in real arithmetic and fails
    by rounding in doubles, one point of 1565 measured on dtlz2 at eps = 0.50.
    cost: d2's delta-coverage and any cross-evaluation of phi_lu against phi_ls
    will show a handful of points on the wrong side of an exact containment, and
    a table reporting them as a finding would be reporting arithmetic.
    trigger: e1 or e2 producing the phi_lu against phi_ls decision-space metrics,
    which is r-06's trigger as well.
    mitigation: v-46 states the exact result and the measured size of the
    artefact, a5's test asserts the containment as a band and not as an equality,
    and d2 reports the pair as a check on r-06 with the artefact named. d3 refuses
    a decision-space row that omits the pair's status, so a check cannot reach a
    table looking like a finding, and it writes d2's absent violation count as an
    empty cell, so the pair no containment covers cannot show a zero there.

r-12 | the reference front with the singular segments and the one without are two
    different objects, so igd against one is not comparable with igd against the
    other, and s-12 says the published conditions do not decide which is right.
    cost: measured and small rather than negligible, the igd of a fixed test
    front moving by -0.63 to +5.36 per cent at 1000 reference points and by
    -0.11 to +1.35 at 20000, so the choice can flip a comparison already inside a
    few per cent.
    trigger: d1 computing igd and e1 tabling it, under phi_ls or phi_cw; phi_lu
    has no singular ray at all, b1 section 2.3, so the flag is a no-op there.
    mitigation: include_singular_segments has no default, the value is recorded
    in every table beside the seed and the point count, and where two solvers
    land within a few per cent e1 reports the metric both ways. d1 carries it on
    the record igd_reference returns, so it travels with the front and not with
    the call site, and d3 refuses an objective-space row that omits it.

r-13 | b2's reference front is sampled through b1's weight map, so its density in
    objective space is the parametrisation's and not the front's, and igd is an
    average over reference points.
    cost: measured in b2-b and decision-relevant rather than cosmetic. the
    nearest-neighbour spacing of a 1000-point front has a coefficient of variation
    of 0.74, 1.13 and 1.42 under phi_lu, phi_ls and phi_cw against 0.12, 0.16 and
    0.20 after the correction; the igd of one fixed test front differs by 5.07 to
    30.41 per cent between the two references and still by 5.07, 12.73 and 26.20
    at 20000 reference points, so unlike r-12's the gap does not close with
    density; and two fronts of equal fill distance can be ranked in opposite
    orders, the dirichlet reference asking for 25 points of 200 more in the half
    it oversamples under every phi and both flag settings.
    trigger: d1 computing igd.
    mitigation: built in b2-b and no longer a plan. sampling_mode has no default
    and its farthest-point setting oversamples by ten through the same map and
    subsamples by farthest-point selection in objective space, which changes which
    points are kept and not the derivation; d1, built, computes igd against that
    mode and records it in every table beside the seed, the point count and the
    singular flag, CONTEXT.md section 10 d1, on the record igd_reference returns,
    and d3 refuses an objective-space row that omits the mode.
    tests/test_metrics_objective.py reproduces the ranking flip at reduced size,
    so d1 fails loudly if the reason for the correction ever stops holding. c3, d2 and the dominance checks state the
    dirichlet mode and are unaffected, measuring a hausdorff distance, two counts
    and a relation. docs/b2b_reference_density.md.

r-14 | pymoo 0.6.2 reaches a generator no seeding call controls: any algorithm
    holding an archive truncates it with RandomTruncation, which passes no
    random_state and draws from np.random.default_rng(None), v-48.
    cost: a run that is not bit-reproducible while appearing to be seeded,
    realised on mopso_cd at its default archive size, five runs of one seed
    giving five different fronts.
    trigger: any use of a pymoo algorithm with a bounded archive; mopso_cd today,
    a future d1 indicator or a phase f solver that carries one tomorrow.
    mitigation: d-03 in its c2-b form; tests/test_runners.py asserts bitwise
    reproducibility for both solvers on every problem and phi and separately
    counts the truncation calls on the one case that overflows at test size, and
    reproducibility is asserted for any new solver rather than assumed.

r-15 | a sweep's cost is set by mopso's archive and by the project's dominance
    filter, which is O(N^2 m) with (block x N x 2m) boolean temporaries; the
    archive half is fixed in c2-b by d-03 and the filter half stands.
    cost: measured, v-57. at budget 5000 per run, nsga-ii 0.33 to 0.50 s, mopso
    1.13 to 3.21 s and random search 1.69 to 2.06 s; the filter alone takes 66 s
    at n = 25000 and 381 s at n = 50000, and time and not memory is the
    constraint.
    trigger: e1 or e2 departing from the research chat's plan of a full sweep at
    budget 5000 with one budget-20000 convergence check per problem, about 11
    minutes for e1 and about an hour for e2; and d1 or d2 filtering large sets
    repeatedly.
    mitigation: the budget and the seed count are stated in that plan rather than
    discovered while a sweep runs; the one reduction available for the filter
    half, using pymoo's NonDominatedSorting where speed matters, is a decision
    against CONTEXT.md section 5 and is not taken here.

r-16 | every objective-space metric moves with the number of rows a solver
    returns, and the three solvers return very different numbers: 100 for
    nsga-ii, at most 200 for mopso and 32 to 2220 for random search.
    cost: measured in c2-b and larger than the differences e1 would be trying to
    detect. on one fixed front, igd improves by a factor of 6.5 from k = 25 to
    the full 610 rows and by 2.7 from k = 100, and hypervolume by 10.3 per cent,
    on cardinality alone.
    trigger: d1 computing hypervolume, igd or spread for more than one solver,
    and e1 or e3 tabling them side by side.
    mitigation: built in d1 and no longer a recommendation.
    truncate_to_common_cardinality is the one implementation, a uniform random
    subsample at a stated seed returning a subsequence of its input, and
    common_cardinality takes the smallest front over the whole comparison and not
    per phi; the truncation is for the objective-space metrics only, d2's being
    set-geometry measures computed on the full recovered sets. the second rule,
    cardinality printed beside every metric, is kept as well and not instead, and
    d3 enforces it in the artefact: a row without a cardinality is not written.

r-18 | no monotone trend in budget is a property either population method has
    under phi_ls or phi_cw: v-54's mechanism protects the offending points, a
    larger budget electing a new smallest-|x_1| member at an x_2 that is no
    better placed.
    cost: measured, and the numbers are unchanged from c3-b's. four times the
    budget lowers the outside fraction under phi_lu by about two points for both
    population methods and does not lower it under phi_ls or phi_cw.
    trigger: any statement in e1 or the memoria that more budget buys a better
    front, and r-15's one budget-20000 run per problem, which must be read as a
    check and never as a trend.
    mitigation: c3-c removed the assertion for all three solvers rather than
    restricting it to phi_lu, where the mechanism is absent, and
    docs/c3_validation.md section 6 reports the trend as a number on both
    measures for all three solvers. what remains open under the number is what a
    capped-front method's budget response should be reported as at all.

r-19 | nsga-ii's decision-space coverage of a full-dimensional efficient set is
    worse than uniform random sampling at equal cardinality under phi_ls and
    phi_cw and not under phi_lu; half of that is the comparator, X_lu's shape
    making a uniform draw 40 per cent worse there for its area, and half is
    nsga-ii's own and has no mechanism after five named exclusions.
    cost: measured, and it is a cost to the comparison and not to the pipeline.
    twelve of the gate's ninety reverse measurements fail, by 0.005 to 0.039 in a
    box of side 2, the suite is red in twelve tests by decision, and four times
    the budget removes none of it.
    trigger: e3 reading any spread statistic, d1's compute_spread included; e1
    reporting a decision-space coverage or hausdorff number for nsga-ii without
    the cardinality-matched uniform draw beside it; and e1 or e2 reporting any
    population-method front without the rank-1 size against the population size.
    mitigation: partial and stated. e1 and e3 report nsga-ii's coverage against a
    uniform draw of its own cardinality and e2 and e3 report the rank-1 size
    against the population size, both now required by CONTEXT.md sections 10 e2
    and 10 e3; whether a decision-space diversity operator belongs in the
    comparison at all is a change to c2 and is out of scope for a gate. the
    measurements, the five exclusions and the control are docs/c3_validation.md
    sections 3, 4 and 5.

r-20 | a5's shared width function makes the transformed problem's effective
    column count phi-dependent: zdt1 has four under example 2.2 and three under
    examples 2.3 and 2.4, dtlz2 six against four.
    cost: the study's headline pair on tier 1, example 2.2 against example 2.4,
    then compares problems of different transformed dimension, and the measured
    difference confounds the order with the dimension. no caption separates them
    afterwards. p1 does not have the defect, a1-b having removed it, so the
    calibration and the benchmarks are not built on the same terms.
    trigger: e2 producing any tier 1 pair number, and g1 or g3 reporting one.
    mitigation: d-05, a5-b, which gives each objective its own driver before e2
    runs. if d-05 is not taken, every tier 1 table carries the effective column
    count per phi and the memoria states the confound in writing.
    docs/plan_after_meeting.md section b4.

r-21 | f1's gate may pass no example of [16], the paper not having been read and
    its examples not having been chosen for this purpose.
    cost: known in advance rather than discovered. the claim loses its third
    clause and becomes a two-stage claim; the answer to [7]'s objection reverts
    from a result to an argument; the presentation loses one slide and its
    strongest closing sentence.
    trigger: f1's verdict table.
    mitigation: the fallback is written before the reading and not after it,
    docs/plan_after_meeting.md section d2: part 2 becomes the reading result, what
    the twenty problems are, why each does or does not serve, and what a study
    using them would need. f4 has a form for that case and f2 and f3 do not run.

r-17 | retired in c3-c, r-10 in a3, r-01 in a4, r-07 in a3-b, r-04 in b1 and
    **r-03 in this session**, the pdf of [1] having arrived in papers/. all six
    are in docs/answered.md with the reasoning that retired them.

## 9. registered predictions

new section, opened 2026-09-04. a prediction is registered **before** the run that
could confirm it, with both of its measurements fixed at registration, so that
neither is available afterwards as an explanation of whatever the run returned. a
row is never edited after registration; an outcome is a new line under it and a
correction is a new row.

format: x-nn | the prediction | the condition | the confirming measurement | the
refuting measurement | status

x-01 | **the protected-minimiser effect.** for any finite candidate set S, the
    member minimising an image column g_k strictly over S is dominated by no
    member of S, since domination requires being no worse in every column. where
    g_k is a function of a strict subset T_k of the decision variables, that
    member's coordinates outside T_k are unconstrained by its protection, so it
    lies outside the phi-efficient set with a probability bounded away from zero
    at every budget.
    | the effect appears at a pair (problem, phi) **exactly when** some column has
    a non-empty free set F_k and the phi-efficient set's projection onto F_k is a
    proper subset of the box's, of positive co-measure. **not** that the
    minimiser be interior: dtlz2's width is minimised at x_n = 0, on a face. the
    general form reproduces v-54's two measured constants on p1 under example 2.4
    exactly, probability 1/2 and expected overhang 1/8, which is the check that
    the generalisation is the right one. derived analytically from the a5 forms:
    **present on p1 under examples 2.3 and 2.4 and absent under example 2.2;
    present on zdt1 under all three, the draft's "not under phi_lu" being refuted
    there because zdt1's own f_1 = x_1 is separable and the shared half-width
    depends on x_30 alone, so free sets are non-empty under every phi; present on
    dtlz2 under examples 2.3 and 2.4 and absent under example 2.2, whose only
    free-set column omits x_2, a variable the efficient set does not constrain**;
    and present on any interval-native problem satisfying the same condition,
    which f1 records per example under its criterion 4.
    docs/plan_after_meeting.md sections f2 and f3.
    | **m-1, the tail-survival lift.** per problem, phi and column k with F_k
    non-empty: random search's uniform box sample at budget 5000 at each of the
    five seeds, filtered under phi, ordered ascending by g_k; s_30 is the fraction
    of the thirty smallest that survive, c = |front| / 5000 is the chance rate,
    L = s_30 / c, reported per seed with median and interquartile range.
    predicted L >= 3 where the condition says present; L <= 1.5, taken as the
    maximum over all columns, where it says absent.
    | **m-2, the overhang.** per seed, the argmin of g_k, with the distance from
    its F_k-coordinates to b1 section 2.4's closed form for p1, to
    {x_2 = ... = x_29 = 0} for zdt1 and to {x_3 = ... = x_11 = 1/2} for dtlz2.
    predicted median strictly positive where present and exactly zero where
    absent, and **on p1 under example 2.4 the mean over seeds equals 1/8 to within
    the seed spread**. 1/8 is derived and not fitted, so a measured mean that is
    not 1/8 within the seed spread refutes the mechanism as stated, and the
    response is to withdraw the generalisation and not to adjust the constant.
    | registered 2026-09-04, before e1 and e2. **what is not evidence either way,
    written down so it cannot be offered later**: that the efficient sets differ
    more under one phi than another; that nsga-ii covers X_cw worse than X_lu;
    that the outside fraction is higher under examples 2.3 and 2.4. all three are
    already established, all three have other explanations on record, and none of
    them is m-1 or m-2

## 8. session log

the last three entries only. **the whole log, unchanged and in order, is in
docs/session_log.md**, moved there in repo-clean because it is history and this
file holds current state.

one line per session, appended after review. never edited once written; a
correction is a new entry. the detail behind each line is in that session's
commit message and in its docs/ deliverable.

format:

    date | subpart | files | outcome | next

2026-09-02 | b2-b | src/reference_fronts.py; tests/test_reference_fronts.py and
    the four call sites in tests/test_validation.py, tests/test_runners.py,
    tests/test_random_search.py and tests/test_metrics_decision.py; new
    docs/b2b_reference_density.md; CONTEXT.md section 10 d1; PROGRESS.md | r-13's
    mitigation, built before d1 rather than deferred with it. **sampling_mode has
    no default**, for the reason include_singular_segments has none: dirichlet is
    the draw as b2 built it and farthest_point is the same draw at ten times the
    size subsampled to n_points by greedy farthest-point selection in objective
    space, and the two are two reference objects. the selection is in objective
    space because that is where igd averages; it is made at the derivation's own
    parameters, delta translating the image and moving no distance in it, so the
    caller's delta does not move which rows are kept; the singular segment is a
    linspace on a one-dimensional set and is not selected. **the derivation is
    untouched**: every kept point is still x(w) at a drawn w, the kept front is a
    subsequence of the oversample and a test walks it through, and b1 section 2.4's
    inequalities are still nowhere in src/. the factor ten is measured and not
    chosen, the coefficient of variation of the nearest-neighbour spacing of a
    1000-point front falling from 0.74, 1.13 and 1.42 at factor 1 to 0.12, 0.16 and
    0.20 at ten and 0.11, 0.11 and 0.12 at forty, ten taking at least 94 per cent
    of the available reduction at a quarter of forty's cost. **the bias is
    decision-relevant and r-13 is not retired**: on one fixed random-search front
    igd differs by 5.07 to 30.41 per cent between the two references and still by
    5.07, 12.73 and 26.20 at 20000 reference points, where r-12's flag difference
    on the same front falls from 4.30 to 0.55; the allocation minimising igd puts
    25 points of 200 more in the oversampled half under the dirichlet reference
    than under the corrected one, under every phi and both flags; 31 of 32 mirror
    pairs under phi_ls and phi_cw are ranked in opposite orders by the two
    references, with the density-free fill distance agreeing with the corrected
    one; and one pair of equal fill distance, 0.080595 against 0.080788 under
    phi_lu, is preferred one way by 22 per cent and the other by 3. everything was
    measured under both settings of the flag, r-12. 55 tests added, the mode
    parametrised into every b2 test that can afford it, the mode's own two being
    the subsequence check and the nearest-neighbour spread comparison, which is
    asserted as a comparison and never against a number; the 20000-point extreme
    test stays in the dirichlet mode, the selection costing 189 s at that size, and
    a companion test asserts the same convergence for the other mode at 200 and
    2000. the four call sites outside b2 state dirichlet explicitly with the reason
    at each, so docs/c3_validation.md's numbers are unchanged. the fast run is 370
    passed and 507 deselected in 166.42s and the full run is 865 passed and 12
    xfailed in 1268.75s | the research chat, on b2-b; then d1 if it is built, or
    e1

2026-09-03 | d1 | new src/metrics_objective.py and tests/test_metrics_objective.py;
    CONTEXT.md section 10 b2 and section 10 d1; docs/verified.md; PROGRESS.md |
    the three objective-space metrics and the truncation that makes them
    comparable across solvers. **they never rank phi**: each phi maps the same
    problem into a different space on a different scale, so the restriction is in
    the module head and in CONTEXT.md section 10 d1, and the metrics comparable
    across phi remain d2's. **pymoo's indicators where pymoo has one, not
    reimplemented**: compute_hv is pymoo.indicators.hv.HV and compute_igd is
    pymoo.indicators.igd.IGD, both left unnormalised so the reference this module
    is handed is the one the indicator is given. what they do that their names
    would not say is measured and reported rather than worked around, v-59:
    moocore's hypervolume clips at the reference point rather than refusing, the
    rows (0, 1) and (3, 0.5) against (2, 2) giving 2.0, so a row beyond the point
    is discarded silently; pymoo's igd averages over the reference points and not
    over the front, 0.0 against 7.0710678118654755 on the transposed call, which
    is the direction r-13 is about. **pymoo has no indicator for the spread this
    project means**: its SpacingIndicator is a spread of nearest-neighbour
    cityblock distances normalised by n, 0.649519052838329 where the same
    quantity normalised by n - 1 is 0.75, and no paper in scope defines it, so
    compute_spread is M_3^* of [2] definition 6 equation (19), printed page 181,
    read from the rendered page as a5 read zdt1, v-58: the euclidean norm of the
    per-column ranges, larger being wider. its limitation is asserted and not
    hidden, that it reads the extremes of each column and nothing between them,
    and whether d1 should also carry [2]'s distribution metric M_2^*, which needs
    a neighbourhood parameter the fixed signature has no room for, is left to the
    research chat. **every reference is an argument and none is built inside a
    metric**: derive_reference_point takes the rule by name,
    reference_front_nadir or reference_front_nadir_plus_range_tenth, and returns
    the rule beside the point; igd_reference returns the front with the mode, the
    flag, the seed and the size on the record, r-13 and s-12; and no parameter of
    any of the six entry points has a default, asserted by inspect over all of
    them and not by reading. **r-16 is code and no longer a recommendation**:
    truncate_to_common_cardinality is the one uniform random subsample at a
    stated seed, bitwise reproducible and a subsequence of its input, and
    common_cardinality takes the smallest front over the whole comparison and not
    per phi. **b2-b's headline is a regression test at reduced size**: 400
    reference points against 2000 and a 60-point mirror pair allocated 45 against
    15 in place of 200 and 150 against 50. the fill distance against an
    independent covering draw and the corrected reference both prefer the
    sparse-favouring front under phi_ls, 0.345423 against 0.462182, and under
    phi_cw, 0.212935 against 0.280172, while the drawn reference prefers the
    other; under phi_lu the oversampled half is also the half the front needs
    more points in and all three agree, which is section 6.3's 31 of 32 and its
    16 of 16, reproduced. v-52's cardinality effect is reproduced the same way,
    igd 0.1101, 0.0735, 0.0534 and 0.0306 and hypervolume 4.3008, 4.5243, 4.6390
    and 4.7228 at 25, 50, 100 and 290 rows of one fixed random-search front.
    **CONTEXT.md section 10 b2's signature line was wrong on both entry points**,
    missing include_singular_segments and sampling_mode on efficient_set and on
    reference_front, and is corrected with a note that neither has a default.
    b2-b and d2 move to done, their review evidenced by this session's prompt,
    which reads b2-b's correction as the reference d1 must use and d2's shape as
    settled. 52 tests added, all in the fast run. the fast run is 422 passed and
    507 deselected in 129.68s and the full run is 917 passed and 12 xfailed in
    922.89s | the research chat, on d1; then d3 or e1

2026-09-04 | plan-after-meeting | new docs/plan_after_meeting.md; CONTEXT.md
    sections 2, 3, 4, 6, 8, 9, 10 a5, 10 e1, 10 e3, 10 f1 to f4, 10 g1 to g4, 11
    and 12; PROGRESS.md; docs/answered.md | **planning only, no code, no
    experiment, no new module**, and nothing was implemented: no phi was added to
    the registry, a5's width functions were not changed and the newton method was
    not touched. the session after the supervisors' meeting of 2026-09-04.
    **the single claim, defended**: the choice of order relation is not a
    modelling detail, and moving between two of the framework's own named orders
    replaces most of the optimal set, calibrated exactly on p1 at 10.3 per cent of
    the union shared, reproduced on standard benchmarks and persisting on problems
    that are interval-valued at source. every other finding got a disposition and
    none is left floating.
    **the arc is the plan's spine**: read the framework, build a controlled
    problem answerable exactly, validate the measurement against that known
    answer, extend it to standard benchmarks, apply it to problems interval-valued
    at source. p1 is the calibration and not a toy, being the only place the
    measurement can be checked at all; the interval-native problems are the ending
    and not a fallback.
    **a defect not raised at the meeting**: a5 shares one width function across a
    problem's objectives, so the transformed problem's effective column count is
    **phi-dependent**, four against three on zdt1 and six against four on dtlz2,
    which confounds the study's headline pair with the transformed dimension.
    r-20, d-05, a5-b, and it precedes e2. **nothing already built is re-run.**
    **the phi search got a stopping condition** in the framework's own terms: the
    containment criterion, which in centre and half-width coordinates says any phi
    with four non-negative coefficients is a refinement of example 2.4 and carries
    nothing new, so a new order must carry a sign change. applied to [9], now in
    papers/: definitions 3.1 and 3.3 are example 2.2, definition 3.4 is example
    2.4 with a_w the half-width, equation (4.1)'s order is **excluded as a check**
    with M = [[1, 0], [1/2, 1/2]] against example 2.2, which [9]'s own proposition
    4.1 independently confirms, and definition 3.2's width-seeking order is
    **admitted** and nested with none of the three. the recommendation is neither:
    it is b1-b, the closed form along the path from example 2.4 to example 2.2 on
    p1, one session and no runs, which strengthens the calibration where a fourth
    phi would extend the exploration.
    **the prediction was corrected before it was registered**, x-01. the draft was
    already proved by b1 section 2.4 and by v-54, and two facts in it were wrong:
    delta is 1/8 since d-01, and the condition is a strict subset with a unique
    minimiser and not an interior one. the general form reproduces v-54's 1/2 and
    1/8 exactly, and analytically from the a5 forms it is **refuted for zdt1**,
    whose separable f_1 = x_1 gives example 2.2 a free-set column too, and
    **confirmed for dtlz2**, whose only free-set column under example 2.2 omits a
    variable the efficient set does not constrain. m-1 and m-2 are fixed now.
    **scope**: eleven CONTEXT.md scope statements superseded with before and after
    blocks, the four paper-level exclusions of section 9 lifted, the evidence rule
    restated and strengthened rather than relaxed. r-03 retires, s-05 is moot,
    s-08 is answered, and p-01, p-02, p-04, p-05 and p-06 all become answerable
    because [1], [7], [8], [9] and [10] are now on disk.
    **the calendar**: e1 next, f1 beside it, a5-b, e2, f2, e3, f3, then g1, g2, g3
    and g4, with delivery on 25 september and a cut order that drops stages from
    the end and never from the middle. two email-today items, the memoria's length
    and its language, both blocking g3. no test was run and none was changed; the
    suite is unchanged at 995 | the research chat, on this plan; then e1

2026-09-03 | d3 | new src/reporting.py and tests/test_reporting.py; CONTEXT.md
    sections 10 e1 and 10 e3; PROGRESS.md | the last instrument before the
    experiments, and the point at which a restriction that holds in the code has
    to still hold in the artefact. **the two blocks are the content and not the
    layout**: the objective-space metrics and the decision-space ones are written
    with different columns and each under the restriction it is read subject to,
    in the file itself and not in a caption, because a reader holding the csv
    alone has neither module in front of them. the objective block says that these
    compare solvers under one fixed phi and never rank phi and that all three move
    with the cardinality; the decision block says that these are the ones the
    decision space makes comparable across phi and that a row whose status is
    check has one direction fixed by a containment before any solver ran. **a row
    lacking a required field is refused with the field named and nothing is
    written**, which is one test per field per block, sixteen and seventeen of
    them: the seed count, the budget, the cardinality and a median with an
    interquartile range everywhere; the reference size, the sampling mode,
    include_singular_segments and the hypervolume reference point with the rule
    that produced it on an objective row, r-12, r-13 and s-12; delta, the scale of
    the decision box, the pair's status and d2's note and violation count on a
    decision row, r-06 and r-11. a blank cell is refused as a missing one, a field
    the block has no column for is refused because the value would not reach the
    file at all, and a metric is refused in the wrong block, so a hypervolume
    cannot be written under a line saying the numbers below it are comparable
    across phi. **the labels are not re-declared**: check and finding are imported
    from d2, the two reference-point rules from d1 and the two sampling modes from
    b2, so a table cannot state a name the module producing the number does not
    have. **the artefact is evidence and not a picture of one**: values are
    written with repr, which is the shortest text that reads back as the same
    double, read_metrics_table reads a table back to the values that were written
    and the same results written twice give the same bytes.
    containment_violations is the one field that may be empty, and its emptiness
    is d2's None, the pair no containment covers, so a zero cannot be read there
    as agreement. **every figure carries the budget, the seed count and the
    cardinality of each series inside the figure**, in the legend entry and never
    in a filename; plot_fronts takes its column pairs as an argument and chooses
    none of its own; plot_decision_sets draws b1 section 2.4's closed-form region
    behind the recovered sets where the problem is p1, in one grey with a line
    style per phi so that a region never takes a series colour, and the three
    boundaries are transcribed from b1 and checked in the tests against b1's own
    inequalities from the other side, as tests/test_reference_fronts.py checks
    b2's sampled points. no metric is computed in the module and no pixel is
    asserted in its tests. **plot_convergence is not built and nothing was added
    to c2**: src/runners.py returns a SearchResult of the seed, the budget, the
    final front and its decision vectors, pymoo's history is not requested from
    minimize, and adding the recording is a change to c2 and was not this
    session's; the module carries no stub that would look like one. **d1's two
    pymoo findings are filed where they will be needed**, both with before and
    after blocks in the session reply: CONTEXT.md section 10 e1 now requires e1 to
    assert that the hypervolume reference point dominates every front it scores
    and to fail rather than let moocore clip, v-59's rows (0, 1) and (3, 0.5)
    against the point (2, 2) giving 2.0, which is the first row's box alone; and
    CONTEXT.md section 10 e3 now requires e3 to state that the igd it reports is
    pymoo's coverage direction, the average over the reference points, and not
    [2]'s M_1^*, definition 6 equation (17), the average over the front, v-59's
    0.0 against the transposed call's 7.0710678118654755. **d1 moves to done**,
    its review evidenced by this session's prompt, which reads d1 as amended, asks
    d3 to render what d1 and d2 produce and asks for those two findings to be
    recorded. 66 tests added, all in the fast run. the fast run is 488 passed and
    507 deselected in 105.85s and the full run is 983 passed and 12 xfailed in
    586.75s | the research chat, on d3; then e1
