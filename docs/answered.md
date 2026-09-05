# phi-interval-opt: answered questions and retired risks

moved out of PROGRESS.md in session a1-b, unchanged. a p-row or s-row lands here
once it has an answer, a risk once it is retired. numbering is shared with
PROGRESS.md and never reused.

nothing is deleted here. a row is kept with the reasoning that retired it, so a
later session can see why it stopped being live rather than finding it gone.

**this file and the deliverable that retired each row are not the same document
and neither is a copy of the other**, docs-clean, 2026-09-05. **this file is
canonical for the disposition**: that a row is closed, when, by which subpart, and
the reasoning in the compressed form a later session needs to decide whether the
row can be reopened. **the deliverable is canonical for the derivation or the
measurement** that produced the closure, and where a row and its deliverable could
differ, the deliverable wins, on CONTEXT.md section 11's rule. a row states its
conclusion and names its source; it does not reproduce the argument, and nothing
in this file needs to be repeated in a deliverable or the reverse.

the deliverable behind each row, so that neither side has to be searched for:

    p-03  a-close           docs/part1/a_close_containment.md, the whole file
    s-08  plan-after-meeting docs/meeting_2026_09_04.md section 4.3, with
                            docs/part1/a1_uncertainty_model.md part 3 and
                            docs/part1/b1_phi_efficient_sets.md sections 2.2, 2.4
    s-05  plan-after-meeting docs/meeting_2026_09_04.md, the fifth decision
    s-13  c3-b              docs/part1/c3_validation.md section 5.5 and
                            docs/part1/b1_phi_efficient_sets.md section 2.6
    r-03  plan-after-meeting docs/meeting_2026_09_04.md; the pdf itself, papers/
    r-07  a3-b              docs/part1/a4b_dominance_tolerance.md, which measured
                            it; CONTEXT.md sections 4 and 10 carry what remains
    r-01  a4                no deliverable: the premise was a .gitignore line,
                            and git history is the record
    r-10  a3                papers/Presentacion_optimizacion_intervalar.txt
                            slide 5 equation (2), the primary source that
                            replaced the summary; v-39 in docs/verified.md
    r-17  c3-c              docs/part1/c3_validation.md sections 2.2 and 2.3
    r-04  b1                docs/part1/b1_phi_efficient_sets.md section 7.4
    r-20  e2                docs/part1/e2_tier1_results.md section 9, with
                            results/tier1/free_sets.csv
    p-02  lit-review        docs/part2/lit_review.md sections 2.1, 2.2 and 2.5
    p-05  lit-review        docs/part2/lit_review.md sections 3.1, 3.2, 3.3 and 3.4


## answered questions from section 5, questions the papers answer

p-03 | closed in a-close, and closed by a proof rather than by a paper. as raised
    in a0-b this asked whether an interval-space analogue of proposition 5.1
    appears outside [1], the candidates being [1]'s own [9], [26] and [31], and it
    was marked blocked on p-01 because none of the three can be resolved from the
    extracted text, r-03. it is closed because the project no longer needs the
    literature to supply the statement: the interval analogue follows in one line
    from the definitions [1] already gives, phi_ls's image being (c - r, 2r) and
    phi_lu's (c - r, c + r) with c + r = (c - r) + 2r, so phi_ls-dominance implies
    phi_lu-dominance and the phi_lu non-dominated set is contained in the phi_ls
    one. the argument is verified symbolically through the project's own phi
    routes, by exhaustive case analysis in exact rational arithmetic covering both
    strictness branches, and numerically on p0, p1, zdt1 and dtlz2, in
    docs/part1/a_close_containment.md. what the row was really carrying is two questions
    and both are now s-11 to the supervisors: is the argument correct, and is the
    interval statement already published, [26] being where it would sit. the
    project does not build on the result until they answer; it is recorded, not
    used. nothing about a0-b's finding changes: v-25 and v-26 stand exactly as
    written, sections 2 and 3 of [1] state no such analogue, and this session
    derives one rather than finding one

p-02 | closed in lit-review, 2026-09-05, and closed affirmatively. the row asked
    whether ishibuchi and tanaka 1990, [9], state the centre-width comparison in
    the same coefficients as example 2.4 of [1]. **they do**: definition 3.4,
    equations (3.11) and (3.12), printed page 222, a_c <= b_c and a_w <= b_w for
    minimisation. the row stayed open after docs/plan_after_meeting.md section c2
    answered it substantively, because that reading was made while surveying
    papers/ and recorded no printed page numbers, which the evidence rule
    requires; **the page numbers are now recorded** and the row closes on them.
    the a_w-is-the-half-width reading the answer depends on is the paper's own
    **three times over**: by definition at equation (2.4), printed page 220; in
    the proof of proposition 4.1 at equation (4.6), printed page 222; and
    numerically in example 1 at equations (5.10) and (5.11), printed page 224,
    where [1850, 2215] is written (2032.5, 182.5). the paper's prose calls a_w
    "the width" and its formula is the half-width, which is where the question
    came from, and the loose word is the paper's and not the project's. the row's
    second clause, that the closing session should also record definitions 3.1,
    3.2, 3.3 and equation (4.1), is discharged: **six order relations are recorded,
    not five**, the sixth being the minimisation relation <=*_LC at equations
    (4.15) and (4.16), printed page 223, which the row did not anticipate, and
    each of the six carries its containment verdict against the registry.
    **no phi was added to the registry.** <=*_LR is example 2.2 and <=*_cw is
    example 2.4, both already in it; <=_LC and <=*_LC are admissible and excluded
    as checks; <=_cw of definition 3.2 is admissible and nested with none of the
    three, so it would be a finding, and it is recorded as the one genuine
    candidate the open literature adds and nothing more. **and proposition 4.2,
    printed page 223, is a second independent confirmation of the containment
    criterion, on the minimisation side and therefore on the project's own two
    registry members. it is not an answer to s-11**, which asks about the
    containments between phi_lu, phi_ls and phi_cw themselves

p-05 | closed in lit-review, 2026-09-05, in both halves, one affirmatively and one
    negatively. it was raised in a3 and narrowed there, and it was **the one
    unverified number in b1's derivation**, docs/part1/part1_closing.md section
    7.4. the regularity criterion is **theorem 34 of [10], printed page 13**,
    verbatim as docs/part1/b1_phi_efficient_sets.md section 1.3 quoted it from
    literature/gH-differentiability calculus for interval analysis.md: the
    summary's number and statement were both correct and b1's citation needs no
    correction to its conclusion. the supporting items are definition 29, printed
    page 11, and definition 30, printed pages 11-12. **one correction to b1's
    wording and not to its result**: b1 glossed abs-differentiability as "|f~| has
    a classical Frechet derivative", which is not definition 30 but **proposition
    32, printed page 12**, a sufficient condition -- and proposition 32's second
    sentence, that a differentiable non-negative function is abs-differentiable,
    is **wider than the strictly-positive-radius condition a1 imposed on p1** and
    is what part 2 needs, since the interval-native candidates have radii that
    vanish at interior points. the other half of the row, the gH-difference's
    definition number in [10], has a **negative** answer: [10] states it in an
    **unnumbered display** in section 2, printed page 3, with no definition number
    and no equation number. the memoria must cite it by page, or cite the numbered
    statement the corpus does have, [16] definition 2.1, printed page 4, which
    attributes it to the same Stefanini 2008 that [10] does


## answered questions from section 6, questions only the supervisors can answer

s-08 | answered as assumed at the supervisors' meeting of 2026-09-04, and filed
    here in plan-after-meeting. the question was whether to accept p1's
    two-dimensional efficient band or change p1's shape, a curve and three
    distinct phi not being available together at two variables and two interval
    objectives, docs/part1/a1_uncertainty_model.md part 3. the working assumption was to
    accept the band. **the meeting's first decision accepts part 1's results as
    they stand and retracts nothing**, and the band is what b1 derived and what
    docs/meeting_2026_09_04.md section 4.3 presented, including the closed-form
    boundary a4 predicted: two conic arcs for example 2.2, one for example 2.3 and
    none for example 2.4, whose set is the unit square minus one open edge. the
    band is also what makes the coverage finding r-19 measurable at all, covering
    a two-dimensional region being a question a hundred points can answer badly.
    docs/part1/b1_phi_efficient_sets.md sections 2.2 and 2.4.

s-05 | **moot** since the supervisors' meeting of 2026-09-04, and filed here in
    plan-after-meeting. the question was whether CONTEXT.md section 9's exclusion
    of section 5 of [1] stands, given that section 5 holds proposition 5.1, which
    relates two of the three phi this project implements. the working assumption
    was that the exclusion stands for implementation and that proposition 5.1 is a
    prediction to check and never a result the project asserts. **the meeting's
    fifth decision lifts every paper-level exclusion**, so the question no longer
    has a subject: proposition 5.1 may be read and cited like any other published
    result, and it has already been read and transcribed, v-24. what is retained
    is not an exclusion but a working rule, and it is the same rule that has
    always applied: the project does not assert an interval analogue of a fuzzy
    proposition without deriving it, and the analogue it has, s-11's containment
    criterion, was derived independently and is not a corollary of proposition
    5.1. CONTEXT.md section 9 as rewritten, docs/part1/a0_framework.md and its a0-b
    addendum.

s-13 | closed in c3-b, and closed by the derivation rather than by the
    supervisors. as raised in c3 this said that two points returned by a solver
    under phi_cw, (1.42192, -0.00039) from random search at seed 15 and
    (1.50000, 0.00026) from mopso at seed 13, lie on the singular line x_2 = 0
    beyond x_1 = 1 and are dominated by no point of b1's derived set X_cw, so that
    what the phi_cw-optimal set is past x_1 = 1 was undecided. that finding was a
    statement about b2's sample and not about the derived set. b2 reaches X_cw's
    extreme values only in the limit, src/reference_fronts.py and b1 section 2.4,
    its weight sample being dirichlet at concentration 0.3, so no row of the
    1000-point reference front sits close enough to x_1 = 1 to beat either point;
    the derived set itself does. b1 section 2.4 gives X_cw = [0, 1]^2 minus the
    open segment {(x_1, 0) : 0 < x_1 <= 1}, so (0.999, 0.0001) is in it, is off
    the undecided segment since its x_2 is strictly positive, and under phi_cw's
    columns (c_1, r_1, c_2, r_2) has image (1.997801, 0.125000, 0.999801,
    0.374500) against (3.022637, 0.125000, 1.178797, 0.630464) and
    (3.249480, 0.125000, 1.249480, 0.687500), strictly smaller in all four against
    both. the r_1 column is strictly smaller too and not tied: it is
    rho x_2^2 + delta and the witness's x_2 of 1e-04 is smaller in modulus than
    both points', 3.9e-04 and 2.6e-04, so the three values are 0.125 + 2.5e-09,
    0.125 + 3.8e-08 and 0.125 + 1.7e-08 and only the printed rounding hides it. it is not an isolated witness: 28 and 26 of 200000 uniform draws of the
    interior of X_cw dominate the two points respectively. so both points are
    dominated by points of the derived set, both are genuinely not efficient, the
    derivation is missing nothing there, and the ten-of-twelve figure c3 reported
    in its own section 5.4 is twelve of twelve. checked against b1's closed form in
    exact arithmetic on doubles, not against a sample, and carried in
    tests/test_validation.py::test_the_points_raised_as_s13_are_dominated_by_the_derived_set.
    s-12 is untouched and stays open in PROGRESS.md: it asks what the status of the
    segment {(x_1, 0) : 0 < x_1 <= 1} itself is, where the published conditions
    give weak optimality and no verdict either way, and nothing here bears on it |
    b1 section 2.4's closed form, read instead of b2's sample | closed in c3-b |
    docs/part1/c3_validation.md section 5.5 and docs/part1/b1_phi_efficient_sets.md section 2.6

every other s-row is still marked "not yet asked" and stays in PROGRESS.md.


## retired risks

r-03 | retired in plan-after-meeting, 2026-09-04, and retired because its premise
    disappeared rather than because it was mitigated. as raised in a0 the row said
    that the pdf of [1] was not in the repository and that the extracted text
    lacked its reference list and two glyphs, so section 3's provenance claims and
    [1]'s own citations could not be resolved. **the pdf is in papers/**, arriving
    with the whole corpus at the supervisors' meeting of 2026-09-04, and it
    carries its reference list. the row's own mitigation was "obtain the pdf",
    and it has been obtained. what the row leaves behind is not a risk but three
    reading tasks that are now possible for the first time: p-01, which wanted
    [1]'s notation and its references [7], [9], [23], [26] and [31]; p-06, which
    wanted whether [1] identifies its "strict minimum" with one of definition
    3.1's names; and the third part of s-11, whether the containment criterion is
    published, which [1]'s own [9], [26] and [31] are where it would sit.

r-07 | closed in a3-b, its premise removed rather than mitigated. as raised in a1
    this said that computing an image coordinate as f_u - f_l is unsafe when the
    width is constant or near zero, the cancellation error of order eps|f| being
    the entire content of the second coordinate under phi_ls and phi_cw. a4-b
    measured it: eps|c| exactly, 1.1e-07 at |c| = 1e9, and the shattering of a
    width column's 46 true values into 210 on p1's grid. d-02 removed the
    subtraction instead of covering it. every phi now has a centre-radius route,
    the same phi composed with M = [[1, -1], [1, 1]], and a problem declares which
    route applies to it; p1 returns its centre and half-width and builds no
    endpoint, and p0's endpoints are the paper's own and are exact, -|x| + |x|
    being exactly zero and |x| - (-|x|) exactly 2|x|. the a4 test's rounding step
    was deleted and the same grids return a1-b's counts without it, 31, 460, 1505
    and 961 on the box and 40, 724, 2496 and 1600 on the slice | it would have
    cost a study reporting arithmetic as a phi effect, which a1 showed reads as a
    positive result and not as an error | no longer live | what remains is not a
    risk but a discipline, and it is carried in CONTEXT.md sections 4 and 10
    rather than here: a problem must declare the representation it actually
    computes in. a problem that genuinely computes endpoints may still subtract
    them, and there is no better route for it, but one that computes a centre and
    a half-width and declares "endpoints" would put the error back. the tier 1
    eps = 0 baseline is also improved rather than merely labelled: in centre and
    half-width form its second coordinate is exactly zero and not a cancellation
    residue

    note added in a5, beside r-07 because it is about the route r-07 was about.
    a4-b and a3-b measured opposite magnitude-sweep behaviour for the endpoint
    route, on different grids. a4-b, section 1.6, found the spurious count at no
    tolerance moving 7, 8, 2, 3 and 12 for phi_ls as the centre offset grew over
    the 61 x 61 grid. a3-b, on the 41 x 41 grid its test uses, found the endpoint
    route wrong at offset 0, phi_ls 711 against 706 and phi_cw 447 against 441,
    and then in exact agreement with the centre-radius route at 1e3, 1e6 and 1e9.
    the explanation a3-b offered, that the low bits the endpoint route corrupts
    fall off the end of the shifted centre, predicts more tie shattering at large
    offset and not less: a4-b measured the width error growing as eps|c|, to
    1.144e-07 at |c| = 1e9 with all 3721 width values wrong, so the corruption is
    larger at 1e9 and not smaller, and the agreement observed there is not what
    the explanation predicts. this is unresolved and it is deliberately not
    investigated. it does not matter, because the endpoint route is not used: p1
    and both tier 1 problems declare centre_radius and compute no endpoint, and
    p0's endpoints are the paper's own and are exact. the discrepancy is recorded
    so that a later session does not read either measurement as a law

r-01 | closed in a4. as raised in a0 this said the source papers were not under
    version control: .gitignore line 1 is "*.txt", so git mv failed and the two
    files were moved with plain mv. a0-b committed both papers and added the
    "!papers/*.txt" exception to .gitignore, so the premise is gone: the exact
    text a0 verified against is now in history and a re-extraction that differed
    from it would show as a diff | it would have cost the recoverability of the
    verified text, silently | no longer live | none needed. r-03, the missing pdf
    of [1], is a different risk and is still open in PROGRESS.md

r-10 | closed in a3, and the entry is kept rather than deleted because the
    reasoning is worth having on record. as raised in a2 this said gh_difference
    was the first piece of code in the project cited to a literature/ summary
    rather than to a paper, [1] containing no gh-difference at all, v-35. that
    premise no longer holds: slide 5 equation (2) of
    papers/Presentacion_optimizacion_intervalar.txt states the same definition,
    is a primary source in papers/, and is now the citation in the code, with the
    summary kept as a secondary that agrees with it, v-39. the risk as stated,
    that an unverified summary formula propagates through every later use, is
    therefore retired | it would have cost every later use of gh_difference, had
    the summary been wrong | no longer live | none needed. what remains is p-05,
    which is a citation-quality question about the definition number in [10] and
    not a correctness risk

r-17 | retired in c3-c, and retired by a correction to the tolerance rather than
    by a new measurement. as raised in c3 this said the gate's verdict was
    sensitive to its tolerance within a factor of about 1.5, and that no
    derivation of the tolerance from the region gave a sharp gate on p1. both
    causes of that sensitivity are now gone. the first was that the tolerance was
    the sum of two resolution floors, and v-55 shows the reverse direction, which
    is the only direction asserted, is bounded by one of them alone: every
    reference point lies in the derived region, so the supremum over reference
    points of the distance to the solver set is at most the fill distance of the
    solver set with respect to that region, and the reference sample's own
    resolution plays no part in it. the second was that the surviving term was
    read off twenty draws, which is a statistic that moves with the draw count,
    and c3-c replaces the point estimate with a measured distribution over 1000
    draws whose quantiles are printed in docs/part1/c3_validation.md section 2.2 and
    whose 0.95 quantile, fixed before the study ran, is the tolerance. the
    estimator itself is unchanged and the first twenty draws reproduce c3's
    published 0.1246, 0.2174 and 0.1836 to four decimal places, so what was
    corrected is the derivation and not the measurement | it would have cost the
    reader of any recovery tolerance quoted in e1 or the memoria, who would have
    had to be told the verdict moved with a choice | no longer live | none
    needed, and the new tolerance moved in both directions against c3's, up by
    0.0776 under phi_lu and down by 0.0496 and 0.0895 under phi_ls and phi_cw,
    which is the evidence that it was derived and not aimed. what r-17 also said,
    that no sharp gate on p1 is available because the derived sets are
    two-dimensional regions of substantial area, is still true and is now stated
    where it belongs, in docs/part1/c3_validation.md section 2.3, as a property of the
    fixture rather than as a risk about a number

r-04 | retired in b1, and filed here in repo-clean-b: the row stated its own
    retirement while still sitting in PROGRESS.md section 7, which CONTEXT.md
    section 11 does not allow. as raised in a0 this said example 3.9's hypotheses
    fail at p0's anchor x = 0, and b1 found the failure wider than the row
    stated: the differentiability hypothesis fails under all three phi, p0's
    first half-width being |x|, and theorem 3.3 refuses phi-convexity under
    phi_lu and phi_ls as well | realised. p0's efficient set is not reachable
    from the optimality conditions under any phi, and under phi_cw they hold and
    are vacuous, the first image coordinate being identically zero | fired in b1
    | the mitigation this row named worked for the anchor. example 3.8 statement
    3 makes x = 0 an optimal solution under all three phi, so the published
    conclusion is recovered and the procedure is validated before p1, and the
    sets come from definition 3.1 applied directly. the consequence is that p0 is
    a smoke test and not a b2 fixture, docs/part1/b1_phi_efficient_sets.md section 7.4,
    and the row retires with that reasoning

r-20 | retired in e2, and retired by the measurement its mitigation asked for. as
    raised in plan-after-meeting it said that a5's shared width function made the
    transformed problem's effective column count phi-dependent, four against three
    on zdt1 and six against four on dtlz2, so the study's headline pair, example
    2.2 against example 2.4, compared problems of different transformed dimension
    and the measured difference confounded the order with that dimension. d-05
    took the mitigation and a5-b implemented it, giving each objective its own
    width driver with every functional form unchanged. **e2 measured the effective
    column count at the run rather than inheriting it**: on a 512-point dependence
    sample it is 2m under every phi at every positive imprecision level on both
    benchmarks, docs/part1/e2_tier1_results.md section 9 and results/tier1/free_sets.csv,
    and tests/test_run_tier1.py asserts the same property as a test. at eps = 0 the
    columns do coincide, m under example 2.2 and m + 1 under examples 2.3 and 2.4,
    and that level is the crisp baseline that src/problems_tier1.py labels as one
    rather than a data point. the phi-dependence the row was about is therefore
    absent wherever the study measures anything.
