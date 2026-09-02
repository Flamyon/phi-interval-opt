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

    highest numbers in use: v-57, p-06, s-13, r-19, d-03.
    numbering continues across those files and numbers are never reused.

project started 2026-08-30.

## 1. where the project stands

    current phase:      d, analysis. **phase c is complete and tagged
                        phase-c-complete**, closed out in
                        docs/phase_c_summary.md. its gate does not pass: twelve of
                        ninety reverse measurements exceed the corrected
                        tolerance, every one of them nsga-ii, and the failure is
                        understood and is a finding rather than a defect
    current subpart:    d2, metrics_decision.py, **built and awaiting review**. it
                        is the only phase d subpart on CONTEXT.md section 8's
                        minimum presentable path; d1 and d3 are off it and are not
                        prerequisites for e1. nothing open blocked it, section 6
                        and section 7 below and docs/phase_c_summary.md section 5,
                        and the six rows it had to carry rather than wait on it
                        carries: the delta with no default, the two phi_ls pairs
                        labelled checks with the containment and r-11's rounding
                        artefact named, the cardinality beside every metric, and
                        one filter call per cross evaluation. next is e1.
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
                        section 5. **d1, if it is built, does have two
                        prerequisites**: r-13, whose mitigation is a b2-b before
                        d1 and is not needed at all if d1 is cut, and r-12, whose
                        trigger is d1 computing igd. r-19 bears on how e3 reads a
                        spread statistic, not on whether d2 can be written
    the suite:          822 tests after d2's 28, of which twelve parameter sets of
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
                        docs/project_narrative.md
                        papers/new_preference_order_relationships_paper.txt
                        papers/Presentacion_optimizacion_intervalar.txt
                        papers/zitzler_deb_thiele_2000_comparison.pdf
                        papers/deb_thiele_laumanns_zitzler_2002_scalable.pdf
                        src/interval_math.py, src/phi_transforms.py,
                        src/problems_tier0.py, src/problems_tier1.py,
                        src/reference_fronts.py, src/random_search.py,
                        src/runners.py, src/metrics_decision.py
                        docs/c3_validation.md
                        tests/conftest.py, tests/test_interval_math.py,
                        tests/test_phi_transforms.py, tests/test_problems_tier0.py,
                        tests/test_problems_tier1.py, tests/test_reference_fronts.py,
                        tests/test_random_search.py, tests/test_runners.py,
                        tests/test_validation.py, tests/test_metrics_decision.py
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
    a5  problems_tier1.py                   done

phase b, ground truth. complete, tagged phase-b-complete in d2-b, the tag naming
b2's commit; its close-out document is docs/phase_b_summary.md, written after the
fact in repo-clean-b.
    b1  phi-efficient sets, derivation      done
    b2  reference_fronts.py                 done

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
    d1  metrics_objective.py                not started, off the minimum path
    d2  metrics_decision.py                 awaiting review
    d3  reporting.py                        not started, off the minimum path

CONTEXT.md section 8's minimum presentable path is a0, a1, a2, a3, a4, b1, b2,
c1, c2, c3, d2, e1: tier 0 only, with the decision-space metrics and the
correctness gate. **d2 is the only phase d subpart on it.** d1 and d3 are built if
the calendar allows and are not prerequisites for e1. that is also where two open
risks go quiet: r-13 says its mitigation is "to be done in a b2-b before d1, and
not at all if d1 is cut", and r-12's trigger is d1 computing igd.

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

each carries the working assumption the project proceeds on. none blocks work.
all twelve are open and none has been asked yet. if an answer differs from the
assumption, record it as a decision in section 3 and list the subparts that have
to change.

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

s-05 | does CONTEXT.md section 9's exclusion of section 5 of [1] stand, given
    that it holds proposition 5.1 | it stands for implementation; proposition 5.1
    is a prediction to be checked and never a result the project asserts |
    docs/supervisor_questions.md s-05, docs/a0_framework.md a0-b addendum

s-06 | should make_phi carry (centre, half_width), the second image coordinate
    being lost at constant or near-zero width if computed as f_u - f_l | both,
    which is what a3-b built, and what is left is the presentation question for
    the memoria | docs/supervisor_questions.md s-06,
    docs/a4b_dominance_tolerance.md part 3

s-07 | should the step 1 degeneracy check run on the slice where the efficient
    set lives as well as on the box | yes, and a1's tier 1 forms were chosen
    against the stronger check, which a4 built as a test and a5 repeats |
    docs/supervisor_questions.md s-07, docs/a1_uncertainty_model.md part 2

s-08 | accept p1's two-dimensional efficient band, or change p1's shape | accept
    the band; it gives spread and coverage two dimensions of structure and b1
    delivered the closed-form boundary a4 predicted | docs/supervisor_questions.md
    s-08, docs/b1_phi_efficient_sets.md sections 2.2 and 2.4

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

r-03 | the pdf of [1] is not in the repository and the extracted text lacks its
    reference list and two glyphs.
    cost: section 3's provenance claims and [1]'s own citations cannot be
    resolved.
    trigger: already realised in a0.
    mitigation: obtain the pdf; p-01 and p-02.

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
    trigger: f1 constructing interval returns, a different kind of problem.
    mitigation: treat it as a working rule and not a result, and run the full a1
    diagnostic including the slice check on every new problem before use.

r-11 | the phi_lu inside phi_ls nesting is a theorem in real arithmetic and fails
    by rounding in doubles, one point of 1565 measured on dtlz2 at eps = 0.50.
    cost: d2's delta-coverage and any cross-evaluation of phi_lu against phi_ls
    will show a handful of points on the wrong side of an exact containment, and
    a table reporting them as a finding would be reporting arithmetic.
    trigger: e1 or e2 producing the phi_lu against phi_ls decision-space metrics,
    which is r-06's trigger as well.
    mitigation: v-46 states the exact result and the measured size of the
    artefact, a5's test asserts the containment as a band and not as an equality,
    and d2 reports the pair as a check on r-06 with the artefact named.

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
    land within a few per cent e1 reports the metric both ways.

r-13 | b2's reference front is sampled through b1's weight map, so its density in
    objective space is the parametrisation's and not the front's, and igd is an
    average over reference points.
    cost: igd in d1 is biased by the parametrisation rather than by the solvers.
    trigger: d1 computing igd.
    mitigation: oversample through the map and subsample by farthest-point
    selection in objective space, which changes which points are kept and not the
    derivation; to be done in a b2-b before d1, and not at all if d1 is cut. c3
    is unaffected, measuring recovery by a hausdorff distance in decision space.

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
    mitigation: d1 implements one of two rules c2-b measured and neither builds.
    the recommendation is to report every metric at a common truncated
    cardinality, the truncation a uniform random subsample at a stated seed and
    the common size the smallest front in the comparison; the second rule,
    cardinality printed beside every metric, is kept as well and not instead.

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

r-17 | retired in c3-c, r-10 in a3, r-01 in a4, r-07 in a3-b and r-04 in b1,
    the last filed in repo-clean-b. all five are in docs/answered.md with the
    reasoning that retired them.

## 8. session log

the last three entries only. **the whole log, unchanged and in order, is in
docs/session_log.md**, moved there in repo-clean because it is history and this
file holds current state.

one line per session, appended after review. never edited once written; a
correction is a new entry. the detail behind each line is in that session's
commit message and in its docs/ deliverable.

format:

    date | subpart | files | outcome | next

2026-09-02 | repo-clean-c | CONTEXT.md sections 5 and 11, PROGRESS.md | third and
    last housekeeping pass. **nothing under src/ or tests/ was opened, and no
    phi, problem, derivation, solver, dominance relation, tolerance or measured
    number was touched. no new claim was added anywhere.** the two proposals
    repo-clean-b flagged and did not act on are now taken. first, **CONTEXT.md
    section 5's two tolerance-rejection paragraphs become one line each**
    pointing at docs/a4b_dominance_tolerance.md, the measurement at parts 1.5
    and 1.6 and pymoo's no-op epsilon at part 3; the rule itself, one dominance
    relation and no tolerance, and the exactness-by-evaluation-order paragraph
    are unchanged, and both arguments survive in full in the deliverable that
    measured them. second, **section 11's three anecdotes become three clauses**,
    one on each rule's own line: a1's three unwritten width variants, c2's
    reproducibility grid never overflowing mopso's archive, and c3-e's
    uncommitted session, which was already a clause and is only tightened. the
    full stories are in docs/session_log.md at c2-b and at c-close and, for the
    first, in docs/a1_uncertainty_model.md section 1 rather than in the log.
    section 5 goes 79 lines to 70 and section 11's evidence rules 25 to 20.
    third, two corrections to PROGRESS.md against the files themselves: the
    header said docs/verified.md holds v-01 to v-46 where it holds v-01 to v-57,
    which is what the same header's highest-numbers line already said; and
    **r-15 is added to the phase d dependency list**, its trigger naming d2
    filtering large sets repeatedly and its mitigation ruling out pymoo's
    NonDominatedSorting as a speed-up, so the list d2 must respect is six rows
    and not four. fourth, **the narrative check is still owed and still could
    not be done**: docs/project_narrative.md did not arrive with this session's
    brief either and is not in the repository, so nothing in it has been checked
    against anything, while CONTEXT.md section 12 has named it since repo-clean.
    that entry is the one thing in the docs/ inventory that does not correspond
    to a file. the fast run is 293 passed and 501 deselected in 94.51s and the
    full run is 782 passed and 12 xfailed in 879.49s, the same counts as
    repo-clean-b at a longer wall time | the research chat, on d2 and on
    docs/project_narrative.md. phase d is not blocked

2026-09-02 | d2 | new src/metrics_decision.py and tests/test_metrics_decision.py;
    CONTEXT.md line 10; PROGRESS.md | the decision-space metrics, the ones
    comparable across phi, and the instrument CONTEXT.md section 10 e3 takes its
    headline number from. compute_hausdorff returns both directed distances and
    the symmetric one and they are read apart, a-to-b asking whether what was
    found is correct and b-to-a whether what exists was found; compute_coverage
    is asymmetric and is one call per direction; compute_overlap is the
    delta-neighbourhood intersection over the union, which is 2|A|/(|A|+|B|)
    whenever A is contained in B and is therefore pinned on two of the three
    pairs; cross_evaluate filters set_a's image under a second phi through
    src/random_search.py's non_dominated_indices and phi_image, neither
    reimplemented, **one filter call per call and not one per pair**, r-15, whose
    cost the module states at the sizes e1 will use, 586 to 2256 rows against
    v-57's 66 s at n = 25000. **delta has no default**, for the reason
    include_singular_segments has none, s-12, and it is refused if negative or
    not finite; no comparison anywhere rounds, snaps or admits an epsilon, d-02.
    compare_phi_on_one_sample is built on filter_one_sample_under_every_phi and
    not on the solver runs, c-close's amendment to section 10 e3: the sample is a
    pure function of the box, the budget and the seed, so the three sets differ
    only through the order, and c3-f measured that a difference read off nsga-ii
    output is confounded with nsga-ii's own phi-conditional coverage. **every
    returned pair carries a status field**, check or finding, so a table built
    from the return value cannot present either phi_ls pair as a measured
    difference: the note names r-06's containment, r-11's rounding artefact with
    its one point of 1565 and s-11's status, and the violation count is None on
    the phi_lu against phi_cw pair so that a zero there cannot be read as
    agreement. 28 tests: the three set-geometry functions on identical, disjoint
    and strictly nested sets by hand, both directed distances against an explicit
    pair loop, coverage asymmetric on a constructed case, coverage and overlap
    non-decreasing over nine deltas, b2's efficient set at distance zero from
    itself under both flag settings and bounded by a subsample's fill distance
    computed by loop, the containment as a unit test of cross_evaluate with
    s-11's status cited in place, the three index sets shown to index one array,
    the labelling, no mutation, and the shape and delta refusals. **one
    documentation correction**: CONTEXT.md's line 10, "nothing has been built
    yet. this is subpart zero.", is deleted as false by three phases and nothing
    replaces it; the before and after are in the session reply. **the narrative
    check owed since repo-clean is done**, docs/project_narrative.md having
    arrived in the repository committed by hand: eighteen items reported in the
    session reply, four wrong, seven overstated, one unsourceable and six caveats
    the deliverables carry and the narrative drops, and **nothing in that file
    was corrected**. the fast run is 321 passed and 501 deselected in 77.25s and
    the full run is 810 passed and 12 xfailed in 752.17s, the twelve being the
    strict xfails c3-c left | the research chat, on d2 and on the narrative
    report. next is e1

2026-09-02 | d2-b | docs/project_narrative.md, CONTEXT.md section 11,
    PROGRESS.md; new tag phase-b-complete | the narrative corrected against d2's
    audit of it, and the two gaps that audit exposed. **nothing under src/ or
    tests/ was opened, and no phi, problem, derivation, solver, dominance
    relation, tolerance or measured number was touched. no new claim was added to
    the narrative: every correction names the deliverable it came from.** three
    jobs. first, **all eighteen audit items are applied to
    docs/project_narrative.md**, which goes 332 lines to 502. the four the
    research chat ruled on: the phi_wu paragraph is kept and relabelled
    pre-repository history, the third phi being (f_r, half-width) with
    lambda = (0, 1) and beta = (-1/2, 1/2), removed before the seed commit, whose
    own CONTEXT.md section 4 already names the correct three, and named as the
    origin of section 11's leave-it-out rule; the five exclusions become
    docs/c3_validation.md section 5.5's own five, saturation, wasted slots, the
    pullback, anisotropy and alignment, the pullback being the one the narrative
    had dropped and the one that rules out nsga-ii simply being worse, image-space
    percentiles 0.1 to 4.9 under phi_lu against 17 to 86 and 31 to 71 under the
    two failing phi; region size leaves the exclusion list with the
    double-counting sentence, which had no source, and is replaced by what 5.5
    measures, region shape as about half the effect acting on the comparator, a
    uniform draw covering X_lu 40 per cent worse for its area, and the other half
    nsga-ii's own, excluded as a general effect by the random-search control at
    matched cardinality and not by argument; and map distortion is scoped, phi_lu
    and phi_cw differing by a similarity so that no distortion claim separates
    those two, while B is not one, condition number exactly the golden ratio
    squared, so phi_ls is genuinely sheared, with 5.4's actual exclusion beside
    it, the scaled jacobian ordering being the reverse of what a distortion story
    needs. the other fourteen as reported: the phase-b tag, saturation at
    generation three or four on p1 and dtlz2 but 13 to 21 on zdt1 with two dips,
    46 or 47 of 50 generations and not on zdt1, X_cw and X_ls with their box
    constraints and their excluded open segments, the 1/8 prediction exact in
    probability and not accurate to two decimals, the containment's narrower
    constraint after c2's amendment, the parameterized path needing no
    confirmation, and the six dropped caveats, a1's floating-point counterpart,
    r-11, r-12, r-13, the tolerance's 0.95 quantile with the 0.005 to 0.039
    margin, the full minimum path with a5, e2 and e3 off it, and the 794 tests
    with twelve failing on purpose. **the corrected file was then re-audited
    against the same deliverables**: it introduced no new unsourceable statement,
    and it corrected five things the first audit had not caught, the curve
    argument attributed to a1-b where it is a1 part 3's, "four sessions" of
    explanation where c3-d, c3-e and c3-f are three, the archive resize and its
    factor of 16 quoted without the budget 20000 they were measured at, the
    control's percentiles as 13 to 63 where c3-f measures 12.7 to 63.2, and the
    tolerance as 12 to 15 per cent of the box side where section 2.3 gives 12.0,
    14.6 and 11.6. second, **phase b is tagged**: phase-b-complete, annotated, on
    dbd32c3, b2's commit, phase b being b1 and b2 with no addendum session and no
    close-out session, so the commit that closed it is not ambiguous;
    docs/phase_b_summary.md, written after the fact in repo-clean-b, is its
    summary, and PROGRESS.md section 2 now says so. third, **CONTEXT.md section
    11's scratchpad rule is extended to documents**, that a document written
    outside the repository is not a document of this project until it is committed
    and checked against the deliverables and that section 12 does not name a file
    that does not exist; the before and after are in the session reply, and
    PROGRESS.md's file inventory now lists docs/project_narrative.md, which
    existed on disk and was missing from it. the fast run is 321 passed and 501
    deselected in 115.12s and the full run is 810 passed and 12 xfailed in 1171.68s,
    the same counts as d2 at a longer wall time, the twelve being the strict
    xfails c3-c left | the research chat, on d2-b and on the corrected narrative.
    next is e1
