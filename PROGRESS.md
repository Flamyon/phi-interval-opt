# phi-interval-opt: progress

state, not specification. the specification is CONTEXT.md and this file never
repeats it. edited by the human only, from session record blocks reviewed in the
research chat.

this file holds current state and open items only. everything settled lives
elsewhere:

    docs/verified.md    every verified fact, v-01 to v-46
    docs/answered.md    answered questions and retired risks
    docs/session_log.md the whole session log, moved out of section 8 in
                        repo-clean. this file keeps the last three entries
    docs/row_history.md the history the d-rows and r-rows had accumulated,
                        moved out of sections 3 and 7 in repo-clean
    docs/supervisor_questions.md
                        the full text of every open s-row. section 6 is the index
    git log             session-by-session detail, one commit per subpart

    highest numbers in use: v-56, p-06, s-13, r-19, d-03.
    numbering continues across those files and numbers are never reused.

project started 2026-08-30.

## 1. where the project stands

    current phase:      d, analysis. **phase c is complete and tagged
                        phase-c-complete**, closed out in
                        docs/phase_c_summary.md. its gate does not pass: twelve of
                        ninety reverse measurements exceed the corrected
                        tolerance, every one of them nsga-ii, and the failure is
                        understood and is a finding rather than a defect
    current subpart:    d2, metrics_decision.py, not started. it is the only phase
                        d subpart on CONTEXT.md section 8's minimum presentable
                        path; d1 and d3 are off it and are not prerequisites for
                        e1. **nothing open blocks d2**, section 6 and section 7
                        below and docs/phase_c_summary.md section 5.
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
                        phase b is complete. phase a is complete: a0, a0-b, a1,
                        a1-b, a2, a3, a3-b, a4, a4-b, a5 and a-close are all done
                        and docs/phase_a_summary.md is the close-out document
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
    phase d depends on: **no open row blocks d2**, the only phase d subpart on the
                        minimum path. what d2 must carry rather than wait on:
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
                        pairs are reported alike; and r-16, cardinality is printed
                        beside every metric. **d1, if it is built, does have two
                        prerequisites**: r-13, whose mitigation is a b2-b before
                        d1 and is not needed at all if d1 is cut, and r-12, whose
                        trigger is d1 computing igd. r-19 bears on how e3 reads a
                        spread statistic, not on whether d2 can be written
    the suite:          twelve tests fail on purpose, all
                        test_the_derived_set_is_reached_by_the_solver at nsga-ii,
                        and the count is recorded so a later session can see
                        whether it moved. c3-c refused both ways of making them
                        green, exempting nsga-ii from the assertion and marking
                        the six configurations xfail, docs/c3_validation.md
                        section 4.1
    files on disk:      docs/a0_framework.md, docs/a1_uncertainty_model.md,
                        docs/a4b_dominance_tolerance.md,
                        docs/a_close_containment.md, docs/phase_a_summary.md,
                        docs/b1_phi_efficient_sets.md,
                        docs/verified.md, docs/answered.md,
                        docs/phase_c_summary.md, docs/supervisor_questions.md,
                        docs/session_log.md, docs/row_history.md
                        papers/new_preference_order_relationships_paper.txt
                        papers/Presentacion_optimizacion_intervalar.txt
                        papers/zitzler_deb_thiele_2000_comparison.pdf
                        papers/deb_thiele_laumanns_zitzler_2002_scalable.pdf
                        src/interval_math.py, src/phi_transforms.py,
                        src/problems_tier0.py, src/problems_tier1.py,
                        src/reference_fronts.py, src/random_search.py,
                        src/runners.py
                        docs/c3_validation.md
                        tests/conftest.py, tests/test_interval_math.py,
                        tests/test_phi_transforms.py, tests/test_problems_tier0.py,
                        tests/test_problems_tier1.py, tests/test_reference_fronts.py,
                        tests/test_random_search.py, tests/test_runners.py,
                        tests/test_validation.py
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

phase b, ground truth
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
    d2  metrics_decision.py                 not started, next subpart
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
field; the reasoning each rests on is in the source named, and the text these
rows carried before repo-clean reshaped them is in docs/row_history.md.

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
    source read in c2 and c2-b; the candidate rejected and its cost are in
    docs/row_history.md | c2, rebuilt this way in c2-b; c3, e1 and e2, which no
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
accumulated are in the deliverable named in its mitigation, and the text these
rows carried before repo-clean reshaped them is in docs/row_history.md.

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

r-04 | example 3.9's hypotheses fail at p0's anchor x = 0 under all three phi,
    and theorem 3.3 refuses phi-convexity under phi_lu and phi_ls as well.
    cost: realised. p0's efficient set is not reachable from the optimality
    conditions under any phi, and under phi_cw they hold and are vacuous.
    trigger: fired in b1.
    mitigation: example 3.8 statement 3 recovers the published conclusion at the
    anchor and the sets come from definition 3.1 applied directly, which makes p0
    a smoke test and not a b2 fixture; docs/b1_phi_efficient_sets.md section 7.4.

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
    cost: measured. at budget 5000 per run, nsga-ii 0.33 to 0.50 s, mopso 1.13 to
    3.21 s and random search 1.69 to 2.06 s; the filter alone takes 66 s at
    n = 25000 and 381 s at n = 50000, and peak memory stays under 145 MiB, so
    time and not memory is the constraint.
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

r-17 | retired in c3-c, r-10 in a3, r-01 in a4 and r-07 in a3-b. all four are
    in docs/answered.md with the reasoning that retired them.

## 8. session log

the last three entries only. **the whole log, unchanged and in order, is in
docs/session_log.md**, moved there in repo-clean because it is history and this
file holds current state.

one line per session, appended after review. never edited once written; a
correction is a new entry. the detail behind each line is in that session's
commit message and in its docs/ deliverable.

format:

    date | subpart | files | outcome | next

2026-09-02 | c3-f | docs/c3_validation.md new sections 5.2 to 5.5 and its head
    note, section 5's closing paragraph, sections 10 and 11; docs/verified.md v-56;
    CONTEXT.md section 10 e3; PROGRESS.md | one diagnostic and it closes phase c.
    **no code changed: no module added, nothing under src/ or tests/ touched, pymoo
    unmodified, no assertion added to the suite, and no tolerance or number in
    sections 1 to 4 moved.** it also records c3-e, which never committed. the
    session's own prompt supplied the rereading and it is verified against c3-e's
    tables before being acted on: the image-space percentiles really are 0.1 to 4.9
    under phi_lu against 17 to 86 and 31 to 71 under the other two, so the anomaly
    is phi_lu being extraordinarily good and not the other two being bad.
    the hypothesis tested: since J_lu = A J_cw with A^T A = 2 I, the phi_lu and
    phi_cw images are the same object up to a rotation and a uniform scaling, and
    crowding distance is computed per column and normalised by column range, so it
    is not rotation invariant; the candidate is that the operator favours one
    alignment. **it is refuted.** reading each nsga-ii front in every frame with its
    own decision set and its own region held fixed, so that only alignment moves,
    the phi_cw runs read in the lu frame sit at 44.3 to 80.5 and the phi_lu runs
    read in the cw frame stay at 12.9 to 46.0: **the advantage travels with the run
    and not with the frame.** the frame change is asserted and not inspected, since
    A^T A = 2 I forces every raw distance in the lu frame to be exactly sqrt(2)
    times the same distance in the cw frame, and over all thirty runs the maximum
    relative departure is 4.5e-15. pymoo's own calc_crowding_distance on the same
    front in each frame confirms the operator works and splits nothing: the
    coefficient of variation is lowest in the run's own frame in all fifteen runs,
    which is the best instrument check in the document, and the diagonal values are
    0.25 to 0.32, 0.24 to 0.43 and 0.25 to 0.30, one behaviour and not three.
    **the control that should have been in the first framing.** random search is
    phi-neutral by construction, c1's sample being a pure function of the box, the
    budget and the seed, so the three phi filter one identical draw. at matched
    cardinality, twenty uniform 100-row subsamples of each front read against the
    same k = 100 distribution nsga-ii is read against, it has no deficit under any
    phi: 12.7 to 29.4, 21.4 to 63.2 and 31.1 to 48.7, thirteen of fifteen below the
    median, against nsga-ii's 33 to 60, 85 to 98 and 90 to 99. so the split is the
    operator meeting the order and not a property of the phi-efficient sets that
    any method at fixed cardinality would inherit.
    **the dimensional check, added to this session on review rather than opened as
    another.** the three region areas in closed form, |X_lu| = 0.310533,
    |X_ls| = 1.513401 and |X_cw| = 1, agreeing with adaptive quadrature to 3.9e-16
    and with a 4-million-point monte carlo of the gate's own in_region to 7e-4, and
    matching b1's twelfth, three eighths and quarter. in units of sqrt(|R|/k) a
    uniform draw covers X_lu 40 per cent worse for its area than it covers the
    other two, so the comparator is itself region-dependent and weakest exactly
    where nsga-ii looks best. it does not dissolve the finding, and the control is
    what shows that: in units of the uniform mean at the same k, random search
    carries +0.243 of nsga-ii's +0.483 swing from phi_lu to phi_ls and +0.244 of
    its +0.485 to phi_cw, **exactly half**, the agreement to three decimals being a
    coincidence of two numbers and read as nothing. the gap between the solvers at
    the same k, region and comparator is +0.165, +0.405 and +0.406.
    **where phi_ls sits, and this is the part that outlives the split.** all three
    images are constant linear images of one another because each phi is a constant
    linear map of the endpoint pair. g_lu = A g_cw with A^T A = 2 I, a similarity,
    ratio exactly 1; g_ls = B g_cw with B^T B block diagonal in two copies of
    [[1,-1],[-1,5]], eigenvalues 3 +- sqrt 5, singular values sqrt(3 + sqrt 5) and
    sqrt(3 - sqrt 5) each twice and condition number exactly
    (1 + sqrt 5)^2 / 4 = 2.618034, the golden ratio squared; and the phi_ls to
    phi_lu map has singular values exactly phi and 1/phi. verified to 0.000e+00 on
    500 random points and on all three region samples, and to 7.1e-15 for the
    pointwise equality of phi_lu's and phi_cw's raw jacobian ratios. **so no
    statement of the form "the phi_lu map distorts more than the phi_cw map" can be
    true**, and 5.4's apparent difference between their raw rows is averaging over
    two different regions. this is v-56, it contains no parameter of p1, and it is
    reported and not asserted, this session adding nothing to the suite.
    **what closes.** four candidate mechanisms excluded by direct measurement,
    across c3-d, c3-e and c3-f: saturation, wasted slots, the pullback, the
    anisotropy of the map, and the alignment of the operator's axes. what replaces
    them is a decomposition, half the swing carried by a method with no operator
    and half nsga-ii's own, and **the residual half has no mechanism and is not
    given one here.** phase c closes with the split measured, bounded, halved and
    honestly unexplained, which is what the brief asked for if it came to that.
    the suite is unchanged because nothing in it changed: the fast run is 310
    passed in 148.58s and the full run 782 passed and 12 failed in 899.35s, the
    same twelve gate tests at nsga-ii as c3-c left | the research chat, on
    whether the residual half is worth another session or whether e1 reports it
    as measured. e1 is not blocked

2026-09-02 | c-close | CONTEXT.md sections 10 e3 and 11; new
    docs/phase_c_summary.md and docs/supervisor_questions.md; PROGRESS.md | the
    phase c close-out. **no measurement was run and no mechanism was proposed.
    no code changed: nothing under src/ or tests/ touched, no phi, problem,
    derivation, solver, dominance relation or tolerance moved, and the two new
    documents cite session deliverables and add no claim of their own.**
    three changes outside the two new documents. **CONTEXT.md section 11 gains a
    commit rule**, prompted by c3-e ending without committing and its numbers
    surviving only in a scratchpad, the second uncommitted session in a row: a
    session commits whatever it has established before starting any run expected
    to take more than a few minutes, and again at its end; a measurement that
    exists only in a scratchpad is not a result of this project, since the
    scratchpad is not in the repository, is not reviewed and does not survive the
    session; and where a session ends without committing, the next session
    records the gap in the session log rather than absorbing the work silently,
    as c3-f did for c3-e. **CONTEXT.md section 10 e3 gains the instruction that
    the phi_lu against phi_cw comparison is made on random search output**,
    through src/random_search.py's filter_one_sample_under_every_phi, which is
    the amendment c3-f's control forces: random search is phi-neutral by
    construction, sample_decision_space taking no phi and the sample being a pure
    function of the box, the budget and the seed, while nsga-ii's coverage of the
    derived region is phi-conditional at matched cardinality, so a difference
    between recovered sets measured on nsga-ii output is confounded with
    nsga-ii's own behaviour and is not evidence about the order. the population
    methods are reported separately with the coverage deficit and the saturation
    beside them. c1 is therefore the instrument carrying the study's main result
    and not a baseline to beat, which is what its own module comment always said
    it was for and what slide 17 asked for it. **PROGRESS.md moves phase c to
    complete and the current subpart to d2**, with d1 and d3 marked off
    CONTEXT.md section 8's minimum presentable path, and records what phase d
    depends on: no open row blocks d2, which must carry s-12 and r-12 through
    include_singular_segments having no default, r-11 and r-06 through naming the
    doubles artefact in the phi_lu against phi_ls pair, s-11 through reporting
    that pair as a check and not a finding, and r-16 through printing cardinality
    beside every metric; d1, if it is built at all, does have two prerequisites,
    r-13's b2-b and r-12's igd trigger.
    **docs/phase_c_summary.md** is the close-out, on docs/phase_a_summary.md's
    model and for the same two readers. it states what phase c built, the gate's
    verdict in one section, and four findings each bounded by what it does not
    say: the protected extreme and its shielded-chain corollary, proved; rank 1
    saturating by generation three or four under every phi and on both tier 1
    benchmarks, stated as a cost of the transformation taking m interval
    objectives to 2m real ones and as the empirical form of the objection [7]
    raises against transformation methods; v-56's exact linear relations with the
    observation that A and B carry no parameter of p1; and nsga-ii's coverage
    deficit at its true scope, half attributable to X_lu's shape making the
    uniform comparator weaker there and the remainder unexplained after five
    named exclusions, saturation, effective cardinality, the pullback, map
    anisotropy and region size. **the exclusions are the work and the document
    says so.**
    **docs/supervisor_questions.md** is the accumulated list written to be
    answered in one sitting: s-01 to s-12, each as question, working assumption
    and what depends on the answer, with s-11 and s-12 first because they are the
    two that change a number in the memoria. one correction to the brief, which
    asked for s-12 and s-13 on the singular segments: **s-13 is closed**, and
    closed by b1's derivation rather than by the supervisors, so it appears as
    context under s-12 with the reason it is not being asked, and the document
    says explicitly that s-12 is untouched by it. v-56 is included as part e, a
    result offered for comment and not a question, with two consistency checks
    against s-11: dominance is preserved by an entrywise non-negative map and not
    by an arbitrary invertible one, and the per-objective blocks of A and B both
    carry a negative entry, which is exactly why phi_lu and phi_cw are nested in
    neither direction while both sit inside phi_ls. the document closes by
    pointing out that supplying any of [1]'s pdf, [26], [9], [31], [10], [7] or
    [8] would close more open rows than any answer on the page.
    the suite is unchanged because nothing in it changed: the full run is 782
    passed and 12 failed in 694.42s, **the same twelve gate tests at nsga-ii as
    c3-c left, which are the gate's stated verdict and not a regression**.
    tagged phase-c-complete | the research chat, on d2. phase d is not blocked

2026-09-02 | repo-clean | PROGRESS.md, CONTEXT.md section 12, pytest.ini,
    tests/test_problems_tier1.py, tests/test_reference_fronts.py,
    tests/test_validation.py; new docs/session_log.md and docs/row_history.md |
    housekeeping. **nothing under src/ was opened, and no phi, problem,
    derivation, solver, dominance relation, tolerance or measured number was
    touched.** four jobs. first, PROGRESS.md is back to the row shapes CONTEXT.md
    section 11 requires and 1470 lines become 735, this entry included.
    section 8, the session log, moved whole and unchanged to
    docs/session_log.md, this file keeping the last three entries and a
    pointer; section 6 became a twelve-row index into
    docs/supervisor_questions.md, which already carries the full text of every
    s-row and is the version the supervisors read; section 7 went to risk, cost,
    trigger, mitigation and nothing else; section 3 to decision, source, affects.
    the history trimmed out of sections 3 and 7 is in docs/row_history.md
    verbatim, kept whole rather than pruned: 68 of its 76 measured figures are a
    second copy of something in docs/c3_validation.md or the session log, and the
    eight that are not are r-15's filter timings, so the research chat can prune
    it against the deliverables rather than take an agent's word for what was
    duplicated. nothing was deleted and every line of the old file has a verbatim
    home except section 6's, which is what the brief directed. second,
    docs/project_narrative.md is entered in CONTEXT.md section 12 as the human
    narrative kept alongside PROGRESS.md's machine state, together with the three
    docs/ files the layout did not name; **the narrative itself has not arrived,
    so nothing in it has been checked against the repository and the claim-by-
    claim pass the brief asked for is still owed.** third, the fast run: it is
    not b2 and a5 that dominate it. measured with --durations=0, of 122 seconds
    tests/test_random_search.py is 60, tests/test_validation.py 29,
    tests/test_reference_fronts.py 17, tests/test_problems_tier0.py 9 and
    tests/test_problems_tier1.py 5. four tests are large-sample diagnostics
    rather than correctness checks and are now marked slow: b2's
    test_no_dense_sample_point_dominates_the_front at 20000 points, c3's
    shielded-tail pair, and a5's separation report. c1's tests are the real cost
    and are not marked, being contract checks; what makes them expensive is d-02's
    untoleranced O(N^2) filter at the test size of 2000, which is r-15's subject
    and a decision rather than tidying. the fast run is 310 passed in 122s before
    and 293 passed in 76s after. fourth, pytest.ini's marker text was widened from
    "runs a solver" to cover the new category. the full run is unchanged: 782
    passed and 12 failed in 707.20s, the same twelve
    test_the_derived_set_is_reached_by_the_solver at nsga-ii, three seeds under
    phi_ls and three under phi_cw at both flag settings, which are the gate's
    verdict and not a regression | the research chat, on d2; and on
    docs/project_narrative.md, which repo-clean could not check because it is not
    in the repository. phase d is not blocked
