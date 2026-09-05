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

    highest numbers in use: v-59, p-06, s-13, r-22, d-06, and x-02 for the
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
    current phase:      e, experiments. **e1 and e2 are both run**, tier 0 and
                        tier 1, and the phase a correction e2 waited on, a5-b, is
                        done. **phase d is built**, d1,
                        d2 and d3 all
                        done, and phase c is complete and tagged
                        phase-c-complete**, closed out in
                        docs/phase_c_summary.md. its gate does not pass: twelve of
                        ninety reverse measurements exceed the corrected
                        tolerance, every one of them nsga-ii, and the failure is
                        understood and is a finding rather than a defect
    current subpart:    e2, the tier 1 run, **run and awaiting review**.
                        experiments/run_tier1.py, tests/test_run_tier1.py,
                        docs/e2_tier1_results.md and results/tier1/. all three
                        solvers, all three phi, zdt1_interval and dtlz2_interval,
                        the five imprecision levels, five seeds, at budget 5000
                        with one convergence check per problem at 20000: 108
                        configurations, 540 runs, 4243 seconds, ten metrics
                        tables, 72 figures and the record generated so that no
                        number in it is typed. **there is no table 1 and the
                        record says so**, that table being exact and p1 only;
                        what replaces it is e1's instrument error read back out
                        of results/tier0/, the exact 0.394710 measured 0.555932
                        at budget 5000 and 0.504177 at 20000, a relative bias of
                        0.408 and 0.277, so every benchmark coverage here is an
                        upper bound on true sharing and a lower bound on how far
                        the orders differ. the headline pair at delta zero and
                        budget 5000 runs 0.846 to 0.545 on zdt1 across eps 0.05
                        to 0.50 with jaccard 0.087 to 0.133, and 0.898 to 0.684
                        on dtlz2 with jaccard 0.136 to 0.322. **the noise floor
                        is exactly zero on both benchmarks at every level and
                        every phi**, which is d-08's dimension argument measured
                        rather than argued, and the swept floor is a step and
                        never an informative intermediate value. m-2 at twenty
                        seeds is positive on zdt1 under all three phi and on
                        dtlz2 under examples 2.3 and 2.4 and exactly zero under
                        example 2.2; m-1 is not computed. e2 does not read any of
                        it, which is e3's
    a5-b:               done, its review evidenced by e2's prompt, which reads
                        the a5-b section of docs/a1_uncertainty_model.md and says
                        in terms that a5-b's width forms are not to be changed.
                        e1 is done on the same evidence, e2's prompt reading e1's
                        record and inheriting its instrument-error rows
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
    the suite:          1074 tests after e2's 45, of which twelve parameter sets of
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
                        tests/test_metrics_objective.py, tests/test_reporting.py,
                        tests/test_run_tier0.py, tests/test_run_tier1.py
                        experiments/run_tier0.py, experiments/run_tier1.py
                        docs/e1_tier0_run.md, docs/e2_tier1_results.md
                        results/tier0/ and results/tier1/, each holding its run's
                        raw arrays, its manifest, its tables and its figures
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
    a5-b tier 1 width drivers                **done**, its review evidenced by
                                            e2's prompt. each
                                            objective now drives its half-width
                                            with its own decision variable, zdt1
                                            r_1 on x_30 and r_2 on x_29, dtlz2
                                            r_1, r_2 and r_3 on x_12, x_11 and
                                            x_10, every form a1 part 4's unchanged.
                                            no two image columns coincide under any
                                            admissible phi, by a symbolic argument
                                            with one full-rank witness matrix; a5's
                                            shared width fails the same certificate
                                            at rank 3 and rank 4. a1 part 4's slice
                                            sweep was re-run and **both forms pass
                                            on all four conditions at every level**,
                                            on a harness that reproduces a1's own
                                            published tables exactly.
                                            docs/a1_uncertainty_model.md a5-b,
                                            CONTEXT.md section 10 a5, d-05
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
    e1  tier 0 run                          **run and awaiting review.**
                                            experiments/run_tier0.py,
                                            tests/test_run_tier0.py,
                                            docs/e1_tier0_run.md and
                                            results/tier0/. the whole grid at 5000
                                            and again at 20000, three tables, 18
                                            figures, and the record generated so
                                            that no number in it is typed
    e2  tier 1 run                          **run and awaiting review.**
                                            experiments/run_tier1.py,
                                            tests/test_run_tier1.py,
                                            docs/e2_tier1_results.md and
                                            results/tier1/. all three solvers,
                                            all three phi, both benchmarks, the
                                            five imprecision levels, at 5000 and
                                            with one convergence check per
                                            problem at 20000: 108 configurations,
                                            540 runs, ten tables, 72 figures and
                                            the record generated. no table 1,
                                            which is exact and p1 only, and e1's
                                            instrument error carried in its place;
                                            the noise floor is exactly zero at
                                            tier 1 dimensions and the swept floor
                                            says why; m-2 at twenty seeds and m-1
                                            not computed. e2 reads nothing, which
                                            is e3's
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
    g3  the latex memoria                   not started, waits on g1 and g2. the
                                            two email-today items are answered and
                                            are d-07: english, short and applied
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

d-05, 2026-09-04, proposed in plan-after-meeting, taken in the research chat,
    **implemented in a5-b** |
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

d-07, 2026-09-04, closed | **the memoria is in english, and it is short and
    applied.** it does not re-derive the framework, does not restate the theory of
    [1] beyond what a reader needs to follow the application, and does not carry
    the derivations at length: it cites the papers and shows what applying them
    produced, the problems, the measured results, the tables and the figures. the
    derivations stay in docs/b1_phi_efficient_sets.md and the other deliverables
    and are cited from the memoria rather than reproduced in it, which is the
    normal arrangement for an applied write-up and is what keeps the memoria short
    without losing anything. **the consequence, decided here rather than
    discovered in g3**: the containment result, v-56's exact linear relations and
    the rank-1 saturation cannot each carry a full section in a short applied
    document. the containment and v-56 become one compact section of structural
    observations in the body, not an appendix, because both are guards on how the
    claim may be phrased and a guard a reader meets after the claim has already
    been read is not a guard; the saturation stays where
    docs/plan_after_meeting.md section a1 put it, beside the nsga-ii coverage
    deficit, because it is a measurement about the transformation and not a
    structural fact about the orders | the two email-today items of
    docs/plan_after_meeting.md section h3, answered | g3, which can now be drafted
    and whose structure this fixes; g1, whose results document prioritises
    accordingly, the claim of plan section a1 being the spine and everything else
    compressed against it; CONTEXT.md section 10 g3; **it closes what d-06 left
    open and blocking**. no translation step is scheduled and no spanish
    terminology has to be fixed, which removes the risk plan section h3 raised,
    that one spanish word would be used for the half-width and the full width,
    which CONTEXT.md section 4 and section 10 a2 forbid in english for a reason
    that does not change with the language. **the length is settled as a shape and
    not as a page range**: no page count was given, and if one is wanted it is a
    second question and not this decision

d-08, 2026-09-04, closed in the research chat | **delta is zero, and delta zero
    is the headline value everywhere; a positive delta is reported only where two
    different samples are compared and it is structurally required**, which is the
    seed-to-seed noise floor and the population solvers' own pairs | the headline
    instrument filters one sample under the three phi, so the three sets are index
    sets over one array and two decision vectors are bitwise identical or they are
    different points, which makes delta zero exact rather than a limit; it removes
    the tuning risk instead of managing it, e1 having measured the reported
    coverage of X_lu in X_cw at 0.556, 0.625, 0.726, 0.931, 0.997 and 1.000 across
    box fractions 0 to 0.2, so any positive delta reports a choice; and a
    box-fraction delta means something different at thirty variables than at two,
    distances scaling with the square root of the dimension, so a fraction fixed on
    p1's 2-box would go vacuous on zdt1 without anyone noticing |
    CONTEXT.md sections 10 e2 and 10 g1; e2, which reports at delta zero; g1 and
    g3, whose tables carry it; e1's artefacts already carry both, its table 2
    having a delta column with a zero row and a positive row for every pair, so
    **nothing of e1 is re-run**

d-09, 2026-09-04, closed in the research chat | **the overlap reported is jaccard
    and is named jaccard, and it is computed alongside dice rather than by changing
    compute_overlap** | d2's compute_overlap is the two covered counts over the two
    cardinalities, which is dice; docs/meeting_2026_09_04.md section 4.3's 0.103177
    is the shared measure over the union, which is jaccard; both are correct, they
    are different functionals, and docs/plan_after_meeting.md section b1 conflated
    them by naming compute_overlap as the measured counterpart of the second. the
    exact values on p1's headline pair are 0.187054 and 0.103177, e1's
    exact_regions_p1.csv | CONTEXT.md sections 10 e2 and 10 g1; e2 and g1, whose
    tables lead with coverage, which is directional and is the same functional in
    both tables, and name the convention of any overlap they print; **d2 is not
    changed**, compute_overlap keeping its meaning and e1's artefacts keeping
    theirs. what remains open and is not this decision: e1's measured table carries
    dice only, so a measured jaccard on tier 0 needs one recomputation from e1's
    stored sets, which is e3's or g1's to do and is not a re-run of e1

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
    test in a4 and repeated in a5. **the trigger fired a second time in a5-b**,
    which changed both tier 1 width forms and therefore had to re-run the check
    rather than inherit it: both forms pass all four of a1 part 4's conditions at
    every level, on a slice that grids every driver, and the harness reproduces a1
    part 4's published tables exactly on a1's own slice, docs/a1_uncertainty_model.md
    a5-b sections 4 and 5. the risk stays open because it is about any future
    width form and not about these two.

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

r-22 | a slice fraction from a1 part 4's separation sweep is grid-resolution
    dependent: phi_lu's zdt1 fraction at eps = 0.10 runs 0.2441, 0.1435, 0.1392 and
    0.0769 at sides 32, 61, 64 and 128, a factor of three across the four.
    cost: a5-b's verdict is untouched, being about whether the three sets are
    distinct and not about how large any of them is, but a fraction quoted as a
    quantity would be quoting the grid rather than the problem, and no reader of
    the memoria could tell which.
    trigger: g1 or g3 quoting a slice fraction, and any later session reading the
    a5-b tables of docs/a1_uncertainty_model.md as sizes.
    mitigation: no slice fraction appears in the memoria as a quantity. it may
    appear only as a comparison at one stated resolution, with the side printed
    beside it and both arms of the comparison sharing that side; a5-b's own tables
    state theirs and its arm 1 is never comparable with its arm 3. e2's tables are
    unaffected, carrying no slice fraction at all.
    docs/a1_uncertainty_model.md, a5-b section 4.

r-17 | retired in c3-c, r-10 in a3, r-01 in a4, r-07 in a3-b, r-04 in b1, r-03 in
    plan-after-meeting and **r-20 in e2**, its mitigation taken in a5-b and the
    effective column count measured at e2's run. all seven are in
    docs/answered.md with the reasoning that retired them.

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

    **outcome, recorded 2026-09-04 from e1's artefacts and not waiting for e3.**
    the row above is unchanged, as registration requires; this is the line under
    it.
    **m-2 is confirmed.** the overhang is exactly zero at every pair where the
    free set is empty and non-zero where it is not, which is what the condition
    predicts, on both problems and all three phi.
    docs/e1_tier0_run.md section 6, results/tier0/registered_measurements.csv.
    **m-1 has failed as an instrument and is withdrawn.** it orders a sample by an
    image column and measures whether the smallest members survive the filter,
    which conflates being protected with being a genuinely good point: under
    example 2.2 the image columns are the real objectives, so a member extreme in
    one of them survives for ordinary reasons and not because anything shielded
    it. e1 measured a lift of 8.22 on p1 under example 2.2, where the prediction
    says at most 1.5 because the effect is absent there, and 1.65 to 2.27 on the
    columns where it is present, where the prediction says at least 3. those are
    the same non-discrimination seen from both sides and not two separate misses.
    **the mechanism stands and the instrument does not.** m-1 is not reinterpreted
    and its thresholds are not adjusted: fixing both before the run is exactly
    what made the failure visible, and that is the result.
    **the 1/8 measurement is inconclusive and is not confirming.** e1 measured a
    mean overhang of 0.163 with a standard error of 0.094 against a predicted
    0.125 on p1 under example 2.4. 0.125 lies inside that spread and so does zero,
    so the measurement separates the prediction from nothing at five seeds. it is
    re-registered at x-02 rather than read.

x-02 | **the 1/8 overhang constant, re-registered at a seed count that can decide
    it.** section f2 of docs/plan_after_meeting.md derives the expected overhang
    of the protected member on p1 under example 2.4 from the general form, as the
    mean distance from a uniform x_2 on [-1/2, 3/2] to the projection [0, 1], and
    that is 1/8. the constant is derived and not fitted.
    | unchanged from x-01: the same problem, the same phi, the same column, the
    same estimator. **what changes is the seed count and nothing else**, from five
    to twenty. the reason is arithmetic and was computed before the re-run: the
    per-seed overhang has a standard deviation near 0.16, so five seeds give a
    standard error near 0.072 and twenty give near 0.036, which halves it and puts
    1/8 outside the interval around zero. random search at budget 5000 is the
    cheapest thing in the project and this is the only measurement that needs the
    extra seeds, so they are spent here and nowhere else.
    | **the confirming measurement**: the mean overhang over twenty seeds lies
    within one standard error of 1/8, and zero does not.
    | **the refuting measurement**: the mean over twenty seeds is further from 1/8
    than its standard error, or the interval around it still contains zero. in the
    first case the mechanism as stated in section f2 is wrong and the response is
    to withdraw the generalisation and not to adjust the constant; in the second
    the measurement is inconclusive again and no seed count will fix it, which
    would itself retire the measurement.
    | registered 2026-09-04, after e1 and before the twenty-seed run. **m-1 is not
    carried into it**: it is withdrawn at x-01's outcome line above and is not
    re-registered in any form

## 8. session log

the last three entries only. **the whole log, unchanged and in order, is in
docs/session_log.md**, moved there in repo-clean because it is history and this
file holds current state.

one line per session, appended after review. never edited once written; a
correction is a new entry. the detail behind each line is in that session's
commit message and in its docs/ deliverable.

format:

    date | subpart | files | outcome | next

2026-09-05 | e2 | new experiments/run_tier1.py, tests/test_run_tier1.py and
    docs/e2_tier1_results.md; results/tier1/; PROGRESS.md; docs/session_log.md;
    docs/answered.md; FASES.md | **the tier 1 run.** all three solvers, all three
    phi, zdt1_interval and dtlz2_interval, the five imprecision levels of
    src/problems_tier1.py, five seeds, at budget 5000 with one convergence check
    per problem at 20000 at that module's own default level: 108 configurations,
    540 runs, 4243 seconds. ten metrics tables, one per level and kind, 72 figures
    and the record generated, so that every number in it is read back out of a
    file the run wrote.
    **there is no table 1 and the record says so rather than leaving it out**: it
    is exact and p1 only and the two benchmarks have no closed form. what stands
    in its place is e1's instrument error, read back out of results/tier0/ and not
    typed: the exact coverage of X_lu in X_cw is 0.394710 and the measurement
    gives 0.555932 at budget 5000 and 0.504177 at 20000, a relative bias of 0.408
    and 0.277. **the instrument overstates agreement**, so every measured coverage
    here is an upper bound on true sharing and a lower bound on how far the two
    orders differ, and the benchmark numbers understate the difference by a factor
    measured once on the calibration problem.
    **the headline pair on the benchmarks**, example 2.2 against example 2.4, at
    delta zero and budget 5000: on zdt1 the coverage of X_lu in X_cw runs 0.846,
    0.722, 0.660 and 0.545 across eps 0.05 to 0.50 and the reverse 0.088 to 0.160,
    with jaccard 0.087 to 0.133; on dtlz2 0.898 to 0.684 and 0.138 to 0.372, with
    jaccard 0.136 to 0.322. coverage leads and any overlap is named, d-09, and
    dice is printed beside jaccard because e1's artefacts use it.
    **the noise floor is exactly zero on both benchmarks, at every level, under
    every phi**, and that is a measurement and not an omission: two independent
    uniform samples share no point, and at thirty and at twelve variables a ball
    of one twentieth of the box diameter contains none of the other sample's
    points. the floor was swept to find where it stops being zero and it is a
    step and never an informative intermediate value: on zdt1 zero to a fifth of
    the box diameter and 0.438 to 0.896 at three tenths, on dtlz2 0.0026 to 0.0066
    at a tenth and 0.734 to 0.952 at a fifth. **so at tier 1 dimensions the floor
    of docs/plan_after_meeting.md section b1 cannot discriminate**, and the reason
    is the dimension and not the problems.
    **the delta sweep is flat**, which is the same fact from the other side: the
    headline coverage does not move at all from delta zero to a tenth of the box
    diameter on either problem, against p1 where the same range took it from 0.556
    to 0.997. d-08's dimension argument, measured rather than argued.
    **a5-b's correction checked at the run and not inherited**: the effective
    column count is 2m under every phi at every positive level on both problems,
    and at eps = 0 it is m under example 2.2 and m + 1 under the other two, which
    is what makes that level a baseline. no containment violation anywhere, r-11.
    **the rank-1 size against the population size, per configuration**, read
    through a pymoo callback that leaves the front bit-identical: nsga-ii
    saturates in every seed in all fifteen dtlz2 configurations and in twelve of
    fifteen on zdt1, mopso in twelve and in five. at eps = 0.10 nsga-ii first
    fills the slots at generation 2 to 4 on dtlz2 and 4 to 17 on zdt1, which is
    c3-d's ordering on a5-b's new forms.
    **m-2 at twenty seeds, x-02's count, computed and not read**: the median
    overhang is strictly positive on zdt1 under all three phi and on dtlz2 under
    examples 2.3 and 2.4, and exactly zero on dtlz2 under example 2.2. it is
    reported against two structures, x-01's registered one and section f3's own
    domination argument re-run on a5-b's forms, because a5-b moved which variable
    each half-width reads. **m-1 is not computed**, being withdrawn at x-01's
    outcome line. x-02's own p1 constant is not e2's and stays open.
    **r-20 retires**, its mitigation measured; **r-22 opens**, a1's slice
    fractions being grid-resolution dependent by a factor of three.
    45 tests added. the fast run is 555 passed and 519 deselected, and the full run
    is 1062 passed and 12 xfailed in 1544.19s, the twelve being c3's finding held
    in strict xfail | the research chat, on e2; then e3, with f1 and f2 beside it

2026-09-04 | a5-b | src/problems_tier1.py; tests/test_problems_tier1.py;
    docs/a1_uncertainty_model.md, appendix a5-b; CONTEXT.md sections 10 a5, 10 e2
    and 10 g1; FASES.md; PROGRESS.md | **the tier 1 width defect corrected, and
    e2 unblocked.** every objective of zdt1 and dtlz2 shared one width function,
    so under examples 2.3 and 2.4 the image carried duplicate columns and the
    transformed problem had three effective objectives where zdt1 has four and
    four where dtlz2 has six, with none of it under example 2.2. the redundancy
    was phi-dependent and the study's headline pair is exactly those two orders.
    each objective now has its own driver, zdt1 r_1 on x_30 and r_2 on x_29,
    dtlz2 r_1, r_2 and r_3 on x_12, x_11 and x_10, **with the functional form of
    every half-width unchanged**: the drivers were chosen so that a1 part 4's
    argument applies to each verbatim, x_29 and x_30 entering zdt1's g linearly
    with the same slope 9/29 and x_10, x_11 and x_12 entering dtlz2's g
    quadratically with the same interior optimum. no variable carrying a centre
    may drive a width, which excludes x_1 on zdt1 and x_1 and x_2 on dtlz2.
    **non-coincidence is checked as a property and not as a count.** the 2m image
    columns are linear combinations of the 2m base functions with pairwise
    distinct coefficient vectors, and that follows from [1]'s determinant
    condition alone, so it holds for every admissible phi and not only the three
    in the registry; coincidence would therefore require a linear dependence among
    the base functions, and one full-rank witness matrix at written-out points
    rules it out, at smallest-to-largest singular value ratios of 8.4e-03 and
    4.1e-03. **the certificate is shown to have power**: rebuilt on a5's shared
    width it returns rank 3 and rank 4, which are exactly the effective column
    counts the defect predicts.
    **a1 part 4's slice sweep was re-run and both forms pass**, on all four of
    a1's conditions at every level: three distinct sets, none the crisp set,
    phi_lu not collapsed onto phi_ls, none saturating. no form was adjusted at any
    point. the slice gained one axis per new driver, which the change forces since
    a1's slice pins x_29, x_10 and x_11, so a middle arm was run -- a5's shared
    width on the new slice -- to isolate the form change from the slice change.
    **the harness is a1's**: a1's script was a throwaway and is not in the
    repository, and at side 61 on a1's own slice it reproduces every fraction of
    both published tables exactly, which is what makes this a re-run. the
    correction's signature is visible in the middle arm: on one slice, giving each
    objective its own driver raises zdt1's phi_ls fraction from 0.0468 to 0.3745
    and its phi_cw from 0.0356 to 0.2844 while phi_lu barely moves, which is the
    duplicate column being removed and is as phi-dependent as the defect was.
    **two decisions from the research chat recorded and applied**, d-08 and d-09:
    delta zero is the headline value everywhere and a positive delta appears only
    where two different samples are compared; and the overlap reported is jaccard,
    named jaccard, computed alongside dice rather than by changing compute_overlap.
    **x-01's outcome recorded without waiting for e3**: m-2 confirmed, m-1
    withdrawn as an instrument for conflating protection with being a good point,
    and the 1/8 measurement inconclusive at five seeds and re-registered as x-02 at
    twenty. 12 tests added. the fast run is 515 passed and 514 deselected in
    265.56s and the full run is 1017 passed and 12 xfailed in 1376.97s | the
    research chat, on a5-b; then e2

2026-09-04 | e1 | new experiments/run_tier0.py, tests/test_run_tier0.py and
    docs/e1_tier0_run.md; new results/tier0/, holding 36 raw npz files with their
    manifest, twelve csv artefacts and eighteen figures; tests/conftest.py, which
    now puts experiments/ on the path; FASES.md, a1 corrected and an e1 entry
    added; CONTEXT.md section 10 g3; PROGRESS.md | **the calibration measured.**
    all three solvers, all three phi, p0 and p1, at seeds 11 to 15, at budget 5000
    with the whole grid repeated at 20000 as the convergence check: 36
    configurations, 180 runs, 5554 s of wall clock. three tables, all through d3's
    save_metrics_table. **the record is generated**: every number in it is read
    back out of a file the run wrote and the file and the key are named beside it,
    so the number-provenance rule of CONTEXT.md section 10 e1 holds by
    construction rather than by care, and --record-only rebuilds the record from
    the artefacts with nothing of the run in memory.
    **the instrument's error, which is what p1 exists to give.** on the pair
    nested in neither direction and at delta zero, the exact 0.394710 measures
    0.555932 at budget 5000 and 0.504177 at 20000; the exact 0.122571 measures
    0.221859 and 0.182152; the exact overlap 0.187054 measures 0.315349 and
    0.265889. every one moves toward its exact value when the budget is
    quadrupled, and the residual at 20000 is the count-for-measure bias and the
    recovered-for-derived overhang together. the containment shows in the
    measurement exactly: coverage of X_lu in X_ls and of X_cw in X_ls is 1.000000
    at both deltas and both budgets.
    **three things the plan and the schema did not meet on, decided here and
    written into the record.** d2's compute_overlap is the two covered counts over
    the two cardinalities and tends to twice the shared measure over the sum, not
    to the shared measure over the union: 0.187054 against 0.103177 on the
    headline pair, so table 1 carries d2's convention and exact_regions_p1.csv
    carries both under separate keys, and plan section b1's identification of the
    two is wrong. the noise floor is a row and not a column, labelled a check,
    d3's decision block having no column for it. and **the tolerance is not needed
    on the instrument that carries the result**: the three sets of one comparison
    are index sets over one array, so at delta zero the coverage is the exact
    shared count, and every pair is reported at delta zero as well as at one
    twentieth of the box diameter. the sweep says the second is far too generous
    at two variables, coverage of X_lu in X_cw running 0.556, 0.625, 0.726, 0.931,
    0.997, 1.000 across box fractions 0, 0.01, 0.02, 0.05, 0.1 and 0.2; it was
    fixed before the run and was not tuned after it.
    **no hypervolume is scored on p0**, one image column being constant under
    every phi, so no point can strictly dominate a row and every box has zero
    thickness; on p1 the point is derived once per phi across both budgets and
    every front was asserted to lie strictly inside it before being scored, and
    none was refused.
    **m-1 and m-2 computed and not read**, x-01 being e3's to read. two
    corrections recorded: FASES.md's a1 entry said the distinct-width variant was
    measured and discarded when a1-b measured and adopted it, and d-07 closes the
    two email-blocking items of plan section h3. 18 tests added. the full run is
    1001 passed and 12 xfailed in 739.10s | the research chat, on e1; then e3, and
    a5-b before e2
