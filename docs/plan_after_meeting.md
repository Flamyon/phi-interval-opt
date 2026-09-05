# plan after the supervisors' meeting of 4 september 2026

state document, written in the research chat on 2026-09-04, after the meeting
recorded in docs/meeting_2026_09_04.md. it decides what to do. it implements
nothing, adds no phi to the registry, changes no width function and runs no
experiment.

it is written against one arc, and every section below is placed on it.


## the arc

    read and verify the framework
      -> build a controlled problem small enough to answer exactly
      -> validate the measurement against that known answer
      -> extend the validated measurement to standard benchmarks
      -> apply the validated measurement to problems that are interval-valued
         at source

five stages. the project has finished the first three and has built the
instruments for the fourth. two consequences, and every section respects them.

**p1 is not a toy. it is the calibration.** it is the only problem in the project
whose phi-efficient sets are known exactly, and therefore the only place where
the measurement can be checked against a known answer at all. the numbers of
docs/meeting_2026_09_04.md section 4.3 are areas of exact regions: under example
2.2 against example 2.4, 60.5 per cent of one set is outside the other, 87.7 per
cent of the other is outside the first, and the two share 10.3 per cent of their
union. nothing later in the project supplies a number of that kind, and nothing
later can be trusted without it. zdt1 and dtlz2 are the same instrument carried
to a case where no answer exists; that is what makes them an extension rather
than a separate experiment, and section b is about the conditions under which
that sentence is true.

**the interval-native problems are the arc's ending and not a fallback.** they
are where the method meets a problem nobody adapted, and they are the answer to
the objection [7] raises against transformation-based methods, which is that
adapting a crisp problem into an interval one throws away interval information
before the method ever sees it. a study that adds its own half-width cannot
answer that objection with anything but an argument. a study that runs on
problems stated as interval-valued in a published paper answers it with a result.

part 1 was a test, and it is reported as one. adapting crisp problems to the
interval framework was never meant to produce good solutions; its purpose was to
make the order relations comparable at all, and it did. p1's closed-form result
stands, nothing is retracted, and part 1's results are reported as what they
are: a controlled test on adapted problems.


## papers/, as it now stands

every paper is in papers/. previous exclusions are lifted; see section e.

    3.4 mb   10-Fréchet and Gateaux gH-differentiability for interval valued
             functions of multiple variables.pdf
             = [10]. stefanini, arana-jiménez and sorini, information sciences
             691 (2025) 121601. already in scope. **new on disk**, and it closes
             p-05: the gh-difference's definition number and the midpoint-radius
             regularity criterion's theorem number can now be cited to the paper
             instead of to a literature summary.
    1.2 mb   12-An adaptive interval many-objective evolutionary algorithm
             with.pdf
             **this is the same paper as [7]**: cui, qu, zhang, jin, cai, zhang
             and chen, "an adaptive interval many-objective evolutionary
             algorithm with information entropy dominance", swarm and
             evolutionary computation 91 (2024) 101749. same title, same journal,
             same volume, same article number, different file size. a duplicate
             on disk and not a second source.
    1.9 mb   13-A two-stage evolutionary algorithm for uncertain constrained
             multi-objective problems with interval-valued objective.pdf
             wen, wang, cui, cai and chen, information sciences 741 (2026)
             123217. **new to scope.** an interval-valued constrained
             many-objective evolutionary algorithm from the same group as [7] and
             [8]. it is a third comparison reference of the same kind: a
             direct-interval method that does not transform. relevant to p-04,
             which asks whether any construction in that literature drives the
             interval width from the decision vector rather than by a constant
             band, and to the memoria's answer to the transformation objection.
             not relevant to the framework of [1].
    210 kb   14-A Multi-Period Optimization Framework for Portfolio Selection
             Using Interval Analysis.pdf
             florentin șerban, bucharest university of economic studies. **new to
             scope.** multi-period portfolio selection with interval-valued
             returns, risk and liquidity, with entropy diversification and
             downside risk control. it is a portfolio paper and the portfolio
             application is now future work, section a2. it is the citation that
             lets the memoria's future-work section say what a study of that kind
             would look like rather than gesturing at one.
    88 kb    15-PORTFOLIO OPTIMIZATION USING INTERVAL ANALYSIS.pdf
             șerban, costea and ferrara. **new to scope.** the same subject at
             shorter length and the same disposition: future work.
    837 kb   1-New preference order relationships ... .pdf
             = [1], the theoretical spine. **new on disk**, and this is the
             single most consequential arrival. r-03 said the pdf was not in the
             repository and that the extracted text lacked its reference list and
             two glyphs. r-03 retires. p-01 becomes answerable, and the third
             part of s-11 -- whether the containment criterion is published --
             becomes checkable through [1]'s own citations [9], [26] and [31].
    1.2 mb   7-An adaptive interval many-objective evolutionary algorithm with
             information entropy dominance.pdf
             = [7]. **new on disk.** p-04's first source.
    4.2 mb   8-An interval evolutionary algorithm based on dynamic relation
             adjustment strategy for many-objective problems.pdf
             = [8]. zhang, zhang, cai, cai and chen, swarm and evolutionary
             computation 93 (2025) 101853. **new on disk.** p-04's second source
             and the methodological template for extending a crisp benchmark into
             an interval benchmark, which is what a5 did.
    509 kb   9-Multiobjective programming in optimization of the interval
             objective function.pdf
             = [9]. ishibuchi and tanaka, european journal of operational
             research 48 (1990) 219-225. **new on disk**, and it is the source
             section c draws on. it holds four order relations and a fifth, and
             only one of them has been used so far.
    437 kb   deb_thiele_laumanns_zitzler_2002_scalable.pdf   = [3], dtlz2's
             source. already in scope.
    1.8 mb   Newton Method for Multiobjective Optimization Problems of
             Interval-Valued Maps.pdf
             mondal, ghosh and kim, 33 pages, arXiv. **new to scope, and it is
             the paper part 2 now rests on.** numbered **[16]** by this project:
             [11] is not on disk and may be occupied in the supervisors' own
             bibliography, of which 12 to 15 are, so the project takes the next
             number that cannot collide and records that it did so. sections 1 to
             4 develop a newton method for multiobjective interval-valued
             problems using gh-gradient and gh-hessian information; section 5 is
             numerical experiments; section 6 is a portfolio application;
             **appendix a is a list of twenty interval-valued test problems**,
             i-bk1 to i-comet, each given with its objective functions and its
             variable bounds, referred to mondal and ghosh's earlier steepest-
             descent paper. those twenty are the candidate problems for part 2.
    15 kb    Presentacion_optimizacion_intervalar.txt   the supervisors' proposal.
             slide 21, "posibles líneas de investigación futuras", reads
             "extensiones futuras diseño en ingeniería bajo incertidumbre /
             aplicacion a optimización robusta de carteras". the portfolio
             application is placed there by the supervisors themselves, which is
             where section a2 now records it.
    723 kb   zitzler_deb_thiele_2000_comparison.pdf   = [2], zdt1's source and
             the source of compute_spread. already in scope.

    papers/resumed/ holds six literature summaries. CONTEXT.md section 12 names
    a directory literature/ that does not exist; the summaries are here. the
    evidence rule is unchanged: where a summary and a paper disagree, the paper
    wins.

one factual correction found while surveying, not acted on because it is outside
this session's output list: **FASES.md's a1 entry says the distinct-width variant
was "medida y descartada"**, measured and rejected. it was measured in a1-b and
**adopted**; src/problems_tier0.py carries r_1 = rho x_2^2 + delta and
r_2 = rho x_1^2 + delta, and b1's derivation and the meeting document both rest
on the distinct-width p1. the line should be corrected before the memoria draws
on FASES.md.


## a. the claim and the path

### a1. the single claim

**the claim.**

> the choice of order relation is not a modelling detail. on one interval
> optimization problem, moving between two of the framework's own named orders
> replaces most of the optimal set. calibrated on a problem whose phi-efficient
> sets are known exactly, the two sets share 10.3 per cent of their union; the
> effect reproduces on standard benchmarks at thirty and twelve variables; and it
> persists on problems that are interval-valued at source.

one claim, three stages of evidence, in the arc's own order.

**why this one and not another.** three properties make it the strongest
available, and each is a property the project has and an alternative claim would
not.

*it is exactly quantified somewhere.* the great majority of empirical papers
about order relations report that different criteria give different answers and
show a plot. this project can state the magnitude in closed form on p1, as an
area of exact regions with no sampling and no solver in it, and then show the
same quantity measured. that combination is what the calibration buys and it is
what no reviewer can wave away.

*it is not an artefact of the solver.* the headline comparison is made on random
search output, through filter_one_sample_under_every_phi, which draws one uniform
sample, evaluates it once and filters it under each phi in turn, so the three
fronts differ only through the order. no other instrument in the project has that
property. c1's control is therefore the instrument carrying the result rather
than a baseline to beat, which is what slide 17 asked of it.

*it survives its own caveats.* the nsga-ii coverage deficit, the rank-1
saturation and the containment each remove a way the claim could have been an
illusion, and none of them removes the claim.

**alternatives considered and rejected.** "the transformation costs
dominance-based selection its pressure" is a real result of this project and is
[7]'s objection made empirical, but it is a negative result about pymoo and about
the 2m construction, it does not need three phi, and it does not use the
calibration at all -- the arc would have been built for nothing. "one phi is
better than another" is not available inside part 1 and part 2 no longer supplies
an external criterion, section a2. "the framework unifies the known orders" is
[1]'s claim and not this project's.

**disposition of every other finding.** each has one and nothing is left
floating.

| finding | source | disposition |
| --- | --- | --- |
| the containment, ND_lu and ND_cw inside ND_ls | docs/part1/a_close_containment.md, s-11 | **supporting, and structurally load-bearing.** it is the reason the headline pair is example 2.2 against example 2.4 and not an average over three pairs. one subsection of the results document's theory section; one paragraph in the memoria; **not in the presentation**. it must appear wherever the two phi_ls pairs are reported, because one direction of every coverage statistic there is fixed before a solver runs. |
| the exact linear relations between the three images, v-56 | docs/part1/c3_validation.md 5.5 | **its own short section in the results document, an appendix in the memoria, out of the presentation.** it is about [1]'s framework rather than about this study, which is why it is worth publishing, and it is load-bearing negatively: A^T A = 2 I forbids any sentence of the form "the phi_lu map distorts more than the phi_cw map", so it is the guard on how the claim may be phrased. |
| the nsga-ii decision-space coverage deficit, r-19 | docs/part1/c3_validation.md 5 | **its own section in the results document, a section in the memoria, out of the presentation.** it is reported as a property of one solver on a full-dimensional efficient set and never as a result about phi; half of it is the comparator's region shape and half has no mechanism after five exclusions. it protects the claim by explaining why the headline is on random search. |
| the rank-1 saturation, c3-d and e2 | docs/part1/c3_validation.md 5.1 | **supporting evidence in the same section as the coverage deficit**, and together with it the memoria's answer to [7]. one paragraph. out of the presentation. |
| the protected-minimiser effect, v-54 and section f | docs/verified.md v-54 | **its own section, ranked second after the claim.** it is the mechanism behind both of the two above, it is registered as a prediction before phase e runs, and section f generalises it. if section f's analysis survives the measurement it is the project's second publishable result. |
| p0 and the recovery of [1]'s published anchor | docs/part1/b1_phi_efficient_sets.md 7 | **appendix.** it is the check on the derivation procedure before it was trusted on p1, which is a methods statement and not a result. |
| the singular segments, s-12, and what did not close | docs/part1/b1_phi_efficient_sets.md 2.6 | **appendix, plus one sentence in the memoria's limitations.** the value is that the project priced not knowing rather than arguing about it. |
| the reference-front density correction, r-13 and b2-b | docs/part1/b2b_reference_density.md | **appendix or out.** it is an instrument correction, it changes no reported claim, and it costs a page. include only if the memoria has room. |
| the dominance-tolerance measurements, a4-b | docs/part1/a4b_dominance_tolerance.md | **out**, except one sentence in the methods: the project uses one untoleranced pareto relation everywhere and obtains exactness by evaluation order. |

### a2. the path

ordered by arc stage, not by phase letter. no subpart is deleted. a subpart whose
subject changed keeps its identifier, is rewritten in place, and the change is
recorded.

**stage 3, validate the measurement against the known answer.**

    e1   tier 0 run. all three solvers, all three phi, all seeds, on p1 and p0,
         with the tables and the figures. this is where the calibration stops
         being a derivation and becomes a measurement: the same pair statistic
         that section 4.3 of the meeting document gives exactly, computed on
         recovered sets, so that the gap between the two is a number. that gap is
         the instrument's error and it is measurable exactly once, here.
         **prerequisite: none. it is the next session.**

**stage 4, extend the validated measurement to standard benchmarks.**

    a5-b **new subpart.** give each tier 1 objective its own width driver, per
         section b's recommendation, and re-run a1 part 4's slice sweep to
         confirm the eps levels still separate the three phi on the slice where
         the efficient set lives. this is a5 rewritten, not a new problem family;
         a5 keeps its identifier and gains the correction, as a4 gained a4-b.
         **prerequisite: the decision in section b. it is a decision and not a
         measurement, so it does not wait on e1.**

    e2   tier 1 run. zdt1 and dtlz2 across eps in {0, 0.05, 0.10, 0.25, 0.50},
         with the rank-1 size against the population size for every
         configuration.
         **prerequisites: a5-b, and e1 reviewed.**

    e3   results synthesis, unchanged in subject. it also selects nothing for
         part 2 any more, since part 2's phi are all three; the sentence in
         CONTEXT.md section 10 e3 about carrying one phi into part 2 is
         superseded, section e.
         **prerequisites: e1, e2.**

**stage 5, apply the validated measurement to problems interval-valued at
source.** phase f, rewritten. the portfolio application is recorded as future
work, which is where slide 21 of the supervisors' own presentation puts it.

    f1   the reading session on [16], with the gate. document only, no code.
         section d is its prompt. it ends with a verdict per example and the
         application proceeds only on an example that passes.
         **prerequisite: none. it is a document session and runs in parallel with
         e1 and e2.**

    f2   problems_native.py. the example or examples f1 passed, in the same
         interface as a4 and a5, with the representation declared and the
         no-round-trip rule applied. **no uncertainty is added to them and no
         width function is written**: the intervals are the paper's own.
         **prerequisite: f1 passing at least one example.**

    f3   the native run, plus the closed-form derivation where f1 reports one is
         available by a published result. all three solvers, all three phi, the
         same seeds and budget as e1 and e2, decision-space metrics, and the
         derived set behind the recovered ones where a derivation exists.
         **prerequisites: f2, and e2 reviewed. e2 precedes f3 because "extend
         the validated instrument to benchmarks" is what licenses applying it
         where no reference exists at all; running f3 without e2 asserts a
         calibration that has not been extended.**

    f4   part 2 write-up: what the method finds on a problem nobody adapted, and
         the answer to [7]'s objection. **if f1's gate passes nothing, f4 is
         written in the fallback form of section d instead**, and f2 and f3 do
         not run.
         **prerequisites: f3, or f1 alone in the fallback case.**

**the write-up. phase g, new, and it is work.**

    g1   the results document. the paper-like write-up with results, in the shape
         of docs/meeting_2026_09_04.md but reporting measurements rather than
         plans. it holds the two central tables of section b and every finding
         with the disposition a1 gives it.
         **prerequisites: e1, e3. f3 if it happened.**

    g2   the figure set. one script under experiments/ that regenerates every
         figure the memoria and the presentation use, into results/figures/, from
         the run artefacts under results/ and from nothing else. no figure is
         drawn by hand and no figure is produced inside a memoria build.
         **prerequisites: e1, e2. it can start on e1's output alone.**

    g3   the latex memoria.
         **prerequisites: g1, g2, and the number-provenance rule below.**

    g4   the presentation, short, no implementation detail. it carries the claim,
         one or two figures and the numbers, and nothing about pymoo, seeds,
         tolerances or test suites.
         **prerequisites: g3's claim sentence and the three headline numbers
         frozen; g2's figures.**

**the number-provenance rule, and it is cheap now and expensive later.**

> every number and every figure in the memoria, in the results document and in
> the presentation comes from a generated file under results/. no number is
> typed. a number reaches the memoria as a \input of a generated fragment or as a
> named cell of a generated csv, and the memoria names the file and the key.

this is a requirement on e1, e2, f3, g1, g2, g3 and g4 alike. it costs each
experimental session one extra emit and it costs the memoria nothing, because
d3's tables already refuse a row that omits the seed count, the budget, the
cardinality, the median with its interquartile range, the reference size, the
sampling mode, include_singular_segments, the hypervolume reference point with
the rule that produced it, delta, the box scale and the pair's status. what the
rule adds is that the number in the pdf and the number in the csv are the same
object rather than two objects that agreed on the day they were copied.


## b. what phase e must report to be comparable with p1

this is the arc's third-to-fourth step and the comparability is the whole point
of it. a benchmark number that cannot be read against p1's is not an extension of
a calibrated instrument; it is a separate experiment reported next to one.

### b1. the yardstick, and its counterpart, named exactly

p1's pair result, from docs/meeting_2026_09_04.md section 4.3 and
docs/part1/b1_phi_efficient_sets.md section 2.4:

    example 2.2 against example 2.4:
        0.394710 of X_lu lies in X_cw, so 60.5 per cent of X_lu lies outside it
        0.122571 of X_cw lies in X_lu, so 87.7 per cent of X_cw lies outside it
        0.103177 of the union is shared

    |X_lu| = 0.310533, |X_ls| = 1.513401, |X_cw| = 1, the box's area being 4,
    and |X_lu ∩ X_cw| = 64 ln(21/20) − 3 = 0.1225705068...

those are lebesgue measures of exact regions. zdt1 and dtlz2 have no closed form
and the counterpart is measured on recovered sets. named exactly:

    which metric        d2's compute_coverage(set_a, set_b, delta), asymmetric
                        and reported both ways, and d2's compute_overlap(set_a,
                        set_b, delta). the shared fraction of the union is the
                        overlap; the two "lies outside" numbers are one minus
                        each coverage.
    on which output     **random search only**, through
                        src/random_search.py's filter_one_sample_under_every_phi:
                        one uniform sample of the box, evaluated once, filtered
                        under each phi in turn, so the three sets differ only
                        through the order. nsga-ii and mopso are reported in a
                        separate table as a question about how solvers behave
                        under each order, with the coverage deficit and the
                        rank-1 saturation beside them, and they are never the
                        source of a pair number.
    in which space      the decision space, R^n, n = 2 for p1, 30 for zdt1, 12
                        for dtlz2. the decision space is the only space common to
                        every phi; the image spaces are not comparable and an
                        objective-space metric may never appear in this table.
    at what cardinality **the full recovered sets, untruncated**, per d1's rule
                        that the common-cardinality truncation is for
                        objective-space metrics only. |A| and |B| are printed on
                        every row. random search returns between 32 and 2220 rows
                        depending on the configuration, r-16, so the cardinality
                        is not a footnote.
    with what sampling  five seeds, median with interquartile range across them,
    error               which d3 refuses a row without. **and a noise floor**:
                        for each phi and problem, the same coverage statistic
                        computed between two seeds of the *same* phi. that is the
                        seed-to-seed disagreement of the instrument, and a
                        cross-phi number that does not exceed it is not evidence
                        of anything. this is the single addition without which
                        the benchmark table cannot be read at all, since on p1
                        the derivation supplies the truth and on the benchmarks
                        nothing does.
    delta               a reporting parameter, printed with the scale of the
                        decision box. **stated as a fraction of the box diameter
                        and not as an absolute number**, because a fixed absolute
                        delta means something different in a 2-box and in a
                        30-box; both the fraction and the absolute value go in
                        the table.

### b2. what is lost between the exact number and the measured one

five things, and each has to be written down beside the table rather than
discovered by a reader.

*measure becomes count.* the exact number weights by lebesgue measure. the
measured one weights by however the solver sampled the set. random search is
uniform on the *box* and then filtered, which is not uniform on the efficient
set; r-19 measured exactly this on p1, where a uniform draw covers X_lu about 40
per cent worse for its area than it covers X_ls and X_cw because X_lu is a thin
curved sliver and the other two are fat.

*derived becomes recovered.* the exact number is what an exact solver would
deliver. the measured one inherits the solver's coverage deficit, and the sign of
that bias is not fixed in general.

*a tolerance appears.* the exact statement has none. the measured one needs delta
to decide when two decision vectors are the same point, and the number moves with
delta.

*dimension bites.* in thirty dimensions a delta-ball is a vanishing fraction of
the box, so coverage numbers collapse toward zero unless delta scales with the
box. that is why delta is a box fraction.

*there is no truth to be outside of.* on p1 "outside X_cw" is exact and
algebraic. on zdt1 and dtlz2 the counterpart measures the disagreement between
two recovered sets, which confounds order sensitivity with solver noise. the
noise floor above is the only control for that, and it is why it is a required
column and not a diagnostic.

### b3. one table or two: two, with p1 in both, and that is the relation

**recommendation: two tables. p1 appears in both, and its two rows are the
relation between them.**

    table 1, exact, p1 only. three rows, one per phi pair, each with the share of
    the first lying in the second, the share of the second lying in the first,
    and the shared fraction of the union, all in closed form, with the two phi_ls
    rows marked as checks on the containment and the example 2.2 against example
    2.4 row marked as the finding.

    table 2, measured, every problem including p1. **the memoria's central
    table.** its columns, decided now:

        problem | eps | pair | status | |A| | |B| |
        cov(A→B) median [iqr] | cov(B→A) median [iqr] | overlap median [iqr] |
        noise floor A | noise floor B |
        delta as box fraction | delta absolute | box scale |
        seeds | budget | solver

    p1's row of table 2 is the measured counterpart of p1's row of table 1, and
    **the difference between the two is the instrument's error, measured once, on
    the only problem where it can be measured.** zdt1's and dtlz2's rows of table
    2 are read subject to that error and are stated as such in the caption.

the alternative, one table with a column saying "exact" or "measured", was
considered and rejected: it invites a reader to compare 0.103177 with a measured
overlap of, say, 0.09 as though the difference were a property of the benchmark,
when on p1 that same difference is a property of the instrument. two tables with
p1 in both makes the instrument's error visible instead of hiding it in a column
header. the cost is one extra table in the memoria.

### b4. a defect that blocks the comparison, and it was not raised at the meeting

**the defect.** in a5 every objective of zdt1 shares one width function and every
objective of dtlz2 shares one width function:

    zdt1    r_1(x) = r_2(x) = eps ((x_n − 1/2)^2 + 1/20)
    dtlz2   r_1(x) = r_2(x) = r_3(x) = eps x_n

so the transformed images carry duplicate columns:

    zdt1  under phi_cw   (c_1, r, c_2, r)         columns 2 and 4 identical
          under phi_ls   (c_1−r, 2r, c_2−r, 2r)   columns 2 and 4 identical
          under phi_lu   (c_1−r, c_1+r, c_2−r, c_2+r)   all four distinct
    dtlz2 under phi_cw   (c_1, r, c_2, r, c_3, r) columns 2, 4 and 6 identical
          under phi_ls   likewise
          under phi_lu   all six distinct

this is exactly the redundancy a1-b removed from p1. p1 now carries
r_1 = rho x_2^2 + delta and r_2 = rho x_1^2 + delta, so all four of its image
columns are distinct under all three phi. tier 1 still carries the defect, so
**the calibration problem and the benchmarks are not built on the same terms.**

**what it does to the comparison, and it is worse than a uniform loss.** the
duplication is *phi-dependent*. zdt1's transformed problem has four effective
objectives under example 2.2 and three under examples 2.3 and 2.4; dtlz2's has
six under example 2.2 and four under the other two. dominance in more columns is
strictly harder to establish, so more points survive. **the headline comparison
of the whole study is example 2.2 against example 2.4, and on tier 1 as built
that comparison is between a four-column problem and a three-column problem.**
the measured difference then confounds the order with the dimension of the
transformed problem, and no caption can separate them afterwards. on p1 the
comparison is four columns against four columns and is clean; that is precisely
the property a1-b bought and tier 1 does not have.

**the options.**

*option 1, leave it and state it.* cost: every tier 1 table carries the effective
column count per phi, and the memoria states that the example 2.2 against example
2.4 number on tier 1 is not separable into an order effect and a dimension
effect. the headline claim's third clause -- "the effect reproduces on standard
benchmarks" -- then rests on a number with a known confound. price: zero sessions
now, and the confound is permanent.

*option 2, give each objective its own width driver, as p1 has.* the minimal
change that inherits a1's own reasoning rather than needing new reasoning:

    zdt1    r_1 = eps ((x_30 − 1/2)^2 + 1/20),  r_2 = eps ((x_29 − 1/2)^2 + 1/20)
            both x_29 and x_30 sit in g's sum, i >= 2, and enter g linearly with
            slope 9/29, so a1 part 4's argument for the quadratic form -- that a
            half-width linear in the driver is either aligned with g's optimum,
            giving phi_cw the crisp order, or opposed to it, giving every phi the
            whole slice -- applies to x_29 verbatim.
    dtlz2   r_1 = eps x_12,  r_2 = eps x_11,  r_3 = eps x_10
            x_10, x_11 and x_12 all sit in g's sum, i >= m = 3, and enter g
            quadratically with an interior optimum at 1/2, so a1 part 4's
            argument that a linear half-width already differs from g's optimum
            applies to each verbatim.

cost: one session, a5-b, rewriting the two width functions and their tests; plus
re-running a1 part 4's slice sweep on the new forms, because r-08 is exactly the
risk that a new width form passes every uniform statistic and still gives phi_cw
the crisp efficient set on the slice where that set lives, and s-07 says the
slice check is the one that catches it. **nothing already built is re-run**: e2
has not started, b1 does not cover tier 1, and c3's gate is tier 0 only. it also
does not touch s-09, which asks whether the half-width should be scaled per
objective rather than absolute; distinct drivers and per-objective scaling are
independent choices and s-09 stays open.

**recommendation: option 2.** the deciding argument is not the redundancy itself
but its phi-dependence. a defect that costs every phi equally could be stated and
lived with; one that changes the transformed problem's dimension between the two
phi the headline compares corrupts the headline. two sessions of cost against a
confound in the study's central number is not a close call.

**do not implement it in this session.** a5-b is scheduled in section g and its
prompt is written there.

one measurement bearing on the size of what option 2 buys, and it cuts both ways:
a1-b found that on p1 the phi_cw efficient set was **bit-identical** under the
identical-width and distinct-width designs, 961 grid points either way with the
same index set, while phi_lu moved from 527 to 460 and phi_ls from 1271 to 1505.
so the redundant column contributed nothing to phi_cw's membership decisions
there. that says the correction buys little for phi_cw's own numbers and a great
deal for phi_ls's, and it says nothing either way about the dimension confound,
which is a statement about comparing two phi and not about either one alone.


## c. more phi, with a stopping condition

admissibility in [1] is a nonzero determinant and nothing else,
lambda_(2i−1) beta_2i ≠ lambda_2i beta_(2i−1), so 𝔄_1 is a four-parameter family
minus a measure-zero set and "search for more" does not terminate unless a
criterion is supplied. the project already owns one.

### c1. the stopping condition, in the framework's own terms

**the containment criterion.** if the per-objective coefficient matrices satisfy
phi_B = M phi_A with M entrywise non-negative and invertible, then phi_A-dominance
implies phi_B-dominance and therefore ND_B ⊆ ND_A. the argument is two lines:
non-negativity preserves every weak inequality under the map, so a point no worse
in every phi_A column is no worse in every phi_B column; invertibility preserves
the strict one, since a strict improvement cannot map to equality without M being
singular. docs/part1/a_close_containment.md; s-11.

**used as a filter.** a candidate phi related to a registry member by an
entrywise non-negative invertible M, in either direction, is admitted to the
project as a *check* and not as a *finding*: its non-dominated set is nested in
the other's, so one direction of every coverage and overlap statistic between the
two is fixed before a solver runs, and a difference measured there is in part a
theorem. that is r-06's instruction applied in advance to a candidate instead of
after the fact to a pair.

**what it excludes, stated concretely.** every phi is M phi_A for a unique
M = phi phi_A^{-1}, each phi_A being invertible, so the test is a computation. in
centre and half-width coordinates the registry is

    phi_lu = [[1, −1], [1, 1]]     phi_ls = [[1, −1], [0, 2]]     phi_cw = I

and therefore, relative to example 2.4:

> **in centre and half-width coordinates, any phi whose four coefficients are
> non-negative is a refinement of example 2.4 and carries no new information
> about the order.**

that one sentence removes the whole positive orthant: every "weighted combination
of centre and half-width", every "alpha times the centre plus beta times the
width", every convex mixture of the two, is excluded. relative to example 2.2 the
same computation excludes, for instance, the order given by (f_l, f_l + f_u),
lambda = (1, 0) and beta = (1, 1): its M against phi_lu is [[1, 0], [1, 1]],
entrywise non-negative, so its non-dominated set sits inside ND_lu.

**what remains, characterised.** what survives the filter must fail
non-negativity against all three registry members in both directions, and since
the registry already spans the natural positive constructions, **a genuinely new
order must carry a sign change relative to every registry member.** a sign change
is not a re-parametrisation: it is a decision maker reversing a preference
direction, preferring a wider interval to a narrower one. that is the stopping
condition in the framework's own terms, and it makes the search finite in
practice rather than infinite in principle.

### c2. the small set the criterion admits, with its sources

[9] is now in papers/ and it holds four order relations and a fifth, of which the
project has used one. read from the paper, european journal of operational
research 48 (1990) 219-225, ishibuchi and tanaka. **note that the paper's a_w is
the half-width and not the full width**: its own proof of proposition 4.1 uses
a_R = a_L + 2 a_w, equation (4.6).

| candidate | source | coefficients (lambda; beta) on (f_l, f_u) | criterion verdict |
| --- | --- | --- | --- |
| ≤_LR, definition 3.1, equations (3.1) and (3.2); and ≤*_LR, definition 3.3, equations (3.9) and (3.10), which the paper says is the same relation | [9] | (1, 0); (0, 1) | **already in the registry**: it is example 2.2 of [1]. |
| ≤*_cw, definition 3.4, equations (3.11) and (3.12), the minimisation order by centre and half-width | [9] | (1/2, 1/2); (−1/2, 1/2) | **already in the registry**: it is example 2.4 of [1], in the same coefficients. **this closes the substantive half of p-02**, which asked exactly whether [9] states the centre-width comparison in example 2.4's coefficients. it does, subject to the a_w-is-the-half-width reading above, and the reading is the paper's own. |
| ≤_LC, definition in equations (4.1) and (4.2): a_L ≤ b_L and a_c ≤ b_c | [9] | (1, 0); (1/2, 1/2), determinant 1/2 | **admissible, and excluded as a check.** M against example 2.2 is [[1, 0], [1/2, 1/2]], entrywise non-negative and invertible, so ND_LC ⊆ ND_lu. and [9]'s own proposition 4.1 says why: A ≤_LC B holds exactly when A ≤_LR B or A ≤_cw B, so ≤_LC is the union of two orders, dominates more often, and has the smaller non-dominated set. **the criterion and the published proposition agree, which is the first independent check the criterion has had.** |
| ≤_cw, definition 3.2, equations (3.3) and (3.4): a_c ≤ b_c and a_w ≥ b_w, [9]'s maximisation order, the decision maker preferring the higher expected value **and less uncertainty** | [9] | (1/2, 1/2); (1/2, −1/2), determinant −1/2 | **admissible, and admitted: it is nested with none of the three.** in centre and half-width coordinates it is [[1, 0], [0, −1]], and the sign change is exactly what section c1 predicts a new order must carry. this is the one genuine candidate the now-open literature adds. |
| example 2.1 of [1], the car-purchase illustration | [1], verified in docs/part1/a0_framework.md | as recorded in a0 | **already known and already excluded, on a different ground**: it carries no convexity notion and no optimality condition, so b1's route does not run on it and it can be an experiment but never a calibration. its criterion verdict should be computed in the same session that computes any other, for completeness. |
| the path phi_t between examples 2.4 and 2.2, t in [0, 1] | **constructed by this project**, and admissible by [1]'s own definition, the determinant condition being the whole of admissibility | in centre and half-width coordinates [[1, −(1−t)], [1−t, 1]], determinant 1 + (1−t)^2 > 0 for every real t | **admitted**: it carries a negative entry for every t < 1 and is nested with no registry member. |
| the dominance relations of [7], [8] and [13] -- possibility degree, information entropy dominance, direct interval comparison | [7], [8], [13] | none | **not excluded by the criterion but by admissibility**: they are not automorphisms of the plane and do not lie in 𝔄_m at all, so they cannot enter the registry. they remain what CONTEXT.md section 3 says they are, comparison references, and the memoria's answer to them is the interval-native application and not a fourth phi. |

**two properties of the path, and they are why it is the recommendation below.**
first, on p1 every member of the path has convex image coordinates: its first row
is c − (1−t) r = (1−t)(c − r) + t c, a convex combination of two functions b1
already proved convex, and its second row is (1−t) c + r, a sum of two convex
functions. so theorem 3.3 holds along the whole path and b1's route is available
at every t. second, the hessians stay diagonal and constant, so condition (15)
stays the two decoupled scalar equations of section 4.2 of the meeting document,
with t carried as a symbol. **the closed form is therefore derivable for the whole
path in one paper-and-pencil session with symbolic verification, and it needs no
experiment at all.**

**the risk on ≤_cw, stated before anyone spends a session on it.** its second
image coordinate is −r, which is concave wherever r is convex, so theorem 3.3's
phi-convexity fails for every problem the project has. worse, it minimises the
centre and maximises the half-width, and [1] covers minimisation in theorem 3.1
and maximisation in theorem 3.2 through −phi but not a mixed sense directly. the
*order* is well defined, so an experiment can run under it; the *derivation* may
not close, and the project's rule is to stop rather than patch. so ≤_cw is a
benchmark-side candidate and never a calibration point, and any session on it
starts by checking whether theorem 3.1 applies at all.

### c3. does adding phi strengthen the claim or dilute it

**one addition strengthens it; two dilute it; and the one to add is the path, not
the fourth named order.**

the claim in a1 is about the magnitude of the change between two named orders.
the path turns three isolated points into a curve: |X_t| and the overlap with
X_cw become explicit functions of t, and the headline sentence becomes "the
overlap falls from 1 to 0.103 as the order moves continuously from example 2.4 to
example 2.2, and here is the function". that is the same claim with a derivative
attached, computed in closed form, on the calibration problem, with no new run.
it strengthens the calibration itself, which is the stage the whole arc rests on.

adding ≤_cw instead extends the *exploration*: a fourth column in every table, a
fourth phi in every run, a run matrix multiplied by 4/3 across three solvers,
five seeds, five eps levels and two benchmarks, and no calibration behind it
because b1 derived closed forms for three phi and may not be able to derive one
for this. it answers a question nobody asked -- whether the effect also shows for
a width-seeking decision maker -- and it does so with weaker evidence than the
three phi already have. that dilutes.

**where in the arc.** the path sits at stage 3, beside the calibration, as a
b1 addendum, and it is the only phi work that belongs before the write-up.
≤_cw, if it ever happens, sits at stage 4 or 5 and is out of scope for 25
september.

**recommendation.** register both candidates now, with their criterion verdicts,
in PROGRESS.md. schedule **b1-b, the closed-form derivation of the path phi_t on
p1**, as the first optional session, taken only if two scheduled sessions finish
early, section g. do not add either phi to src/phi_transforms.py in this session
or in any session before b1-b's derivation exists, since CONTEXT.md section 4's
rule -- a phi is proposed in the research chat with a reason and recorded as a
decision first -- is satisfied by this section for the proposal and by a decision
row for the addition, and the two are not the same step.


## d. the interval-native problems: a reading prompt, a gate and a fallback

this is the arc's ending, and it is also the least certain part of the plan. the
paper has not been read and its examples may not serve.

### d0. the criteria, stated before any example is seen

an example of [16] serves as a test problem for this method only if it satisfies
all five. they are stated here, in advance, so that no example is admitted by a
criterion invented after looking at it.

1. **dimension.** n and m are recorded, and n is small enough that the recovered
   sets can be compared in the decision space at the project's budget, and m
   small enough that the transformed problem's 2m columns do not saturate rank 1
   at the project's population size. c3-d measured that the column count does not
   on its own order the saturation, so this is recorded and not predicted; but an
   example at n = 4 and m = 2 is preferable to one at n = 3 and m = 3 on that
   ground alone, all else equal.

2. **closed form.** whether the phi-efficient set is derivable in closed form,
   and **by which published result of a paper in scope**, named by theorem or
   example number. the route the project has is b1's: image coordinates written
   out, phi-convexity by theorem 3.3 of [1], regularity by the criterion of [10],
   condition (15) of example 3.9 to get the candidate set, and example 3.8
   statement 3 to lift it from weak optimality to optimality. that route closes
   when the image coordinates are differentiable and convex and the stationarity
   system is solvable. an example whose objectives are quadratic with constant
   diagonal hessians is the case where it closes cheaply, because (15) then
   decouples into n scalar equations exactly as it does for p1.

3. **phi-separation, checked where the efficient set lives.** the three phi must
   give distinct, non-trivial efficient sets: none equal to the crisp set, none
   the whole box. **checked near the efficient set and not on a uniform sample of
   the box**, per r-08 and s-07: zdt1 with a linear half-width passed every
   uniform statistic and still gave phi_cw the crisp efficient set exactly on the
   slice where that set lives, and the uniform sample reported separation because
   a uniform sample of a high-dimensional box contains essentially nothing near
   the efficient set.

4. **the width driver, per v-54.** whether any image column, under any of the
   three phi, is a function of a strict subset of the decision variables, and if
   so which variables are free and what the phi-efficient set's projection onto
   the free variables is. this is not a disqualification: it is the
   protected-minimiser condition of section f, and an example that has it is a
   third registered test of section f's prediction. it is recorded because a
   recovered front on such an example carries points whose distance from the
   efficient set is a property of the order and not of the solver, and a table
   that does not say so misreads them.

5. **genuinely interval-valued at source.** the intervals are the paper's own and
   are not a band added around a crisp problem. an example whose objective is
   f(x) plus or minus a constant, or plus or minus a function the paper
   introduced to make the problem interval-valued, fails this criterion and is
   reported as failing it, because such an example is what part 1 already did.

**the gate.** the reading session ends with a verdict per example against these
five, and the application proceeds only on an example that passes all five. an
example that passes four is reported with the one it failed and is not used.

### d1. the reading-session prompt for f1

written in the a0 style. it goes into a session as it stands.

> **f1: reading pass over [16], mondal, ghosh and kim, "newton method for
> multiobjective optimization problems of interval-valued maps",
> papers/Newton Method for Multiobjective Optimization Problems of
> Interval-Valued Maps.pdf.**
>
> output: docs/f1_interval_native_reading.md. **no code, no module, no
> implementation.** read from the paper itself, not from a summary and not from
> this prompt.
>
> **the subject of this session is the paper's test problems and not its
> method.** the newton method of [16] is not this project's subject unless a
> later session argues otherwise: this project takes existing solvers and
> measures what changes when the order changes, CONTEXT.md section 1, and
> implementing a new algorithm is a different project. **do not implement it, do
> not derive from it, and do not let reading it become planning it.** what the
> method section is read for is one thing only: whether the paper's own
> definition of an efficient solution for an interval multiobjective problem is
> the one [1] definition 3.1 gives, and if not, how they differ. record that with
> its definition number and page and stop.
>
> transcribe, separately from anything else, and each located by number and page:
>
>     the problem class the paper optimizes over, with its definition number.
>     its efficiency concept or concepts, with definition numbers, and its
>         relation to [1] definition 3.1 as above.
>     **every test problem of appendix a**, one block per problem, with its
>         problem number, its name, its n, its m, every objective written out in
>         the paper's own notation, and its lower and upper bounds. twenty are
>         listed, i-bk1 through i-comet.
>     the worked example of section 5 that the paper carries through iteration by
>         iteration, with its table number, so that any solution the project
>         recovers can be checked against a published point.
>     the portfolio application of section 6, at one paragraph, for the future-
>         work section and no further.
>     the source appendix a cites for its test problems, with its reference
>         number and full citation, since the problems may be that paper's rather
>         than [16]'s and the memoria must cite whichever is correct.
>
> then, **per test problem, the five criteria of docs/plan_after_meeting.md
> section d0, with a verdict on each and an overall pass or fail**:
>
>     1. n, m, and the transformed problem's 2m column count.
>     2. is the phi-efficient set derivable in closed form, and by which
>        published result of [1] and [10], named by theorem or example number?
>        say explicitly whether the objectives are differentiable, whether the
>        image coordinates under each of the three phi are convex, and whether
>        the hessians are constant. **do not derive the set in this session**;
>        say whether the route closes and what it would cost.
>     3. do the three phi separate on it? **this is the one criterion this
>        session cannot answer from the paper**, since it needs a sample. record
>        what would have to be computed -- a1's diagnostic, run on the union
>        bounding box of the three efficient sets and not on the whole box, per
>        s-07 -- and mark the criterion "not checkable without a run", which is
>        not a pass.
>     4. under each of the three phi, list every image column and the decision
>        variables it depends on. name any column that is a function of a strict
>        subset, name the free variables, and say what is known about the
>        efficient set's projection onto them.
>     5. is the problem interval-valued at source? quote the objective and say
>        whether its intervals are the paper's own or a band the paper added.
>
> report separately, and do not resolve:
>
>     any place where the paper is ambiguous, where the extracted text is
>         corrupted, or where a symbol cannot be read.
>     any disagreement between the paper and this prompt. the paper wins.
>     any test problem whose bounds, objectives or interval coefficients are
>         printed inconsistently between appendix a and section 5.
>
> do not: implement anything, derive an efficient set, add a phi, propose a
> modification to a test problem, or resolve an ambiguity by choosing the
> convenient reading.
>
> the session ends with a table of twenty rows and a one-line verdict, and with a
> recommendation of which single example to carry into f2, or with the statement
> that none passes.

**one preliminary observation, offered as a reason to expect the gate to pass and
not as a substitute for it.** while surveying papers/ for this plan, appendix a's
listing was read. the twenty problems are stated as sums of interval coefficients
times real functions, of the shape G_i(x) = ⊕_j [a_ij, b_ij] ⊙ h_ij(x), which is
interval-valued at source in the sense of criterion 5 and is imprecision in the
coefficients, the construction slide 19 offers first and a1 rejected for tier 0.
several are quadratic with what appear to be constant diagonal hessians at n = 2
and m = 2 or 3, which is the shape where b1's route closes cheaply. **none of
that is a verdict.** the criteria of d0 stand as written, f1 checks them against
the paper with page numbers, and f1's verdict is what f2 proceeds on.

### d2. the fallback, written now so it is not improvised later

**if no example passes the gate, part 2 becomes a reading result and the arc
still closes.** f4 is written in this form, f2 and f3 do not run, and the
schedule of section g gains four days:

> we read [16], which states twenty multiobjective optimization problems that are
> interval-valued at source. here are those problems. here is, for each, whether
> it can serve as a test problem for a study of order sensitivity in the
> framework of [1], against five criteria stated before the problems were read.
> here is why each does or does not serve. and here is what a study using them
> would need: [the missing criteria, named].

**what the paper loses.** the third clause of the claim -- "and it persists on
problems that are interval-valued at source" -- is removed from the claim and the
claim becomes a two-stage one, calibration and benchmarks. that is a real loss
and it is the loss of the answer to [7]'s objection, which then reverts to an
argument in the discussion rather than a result. the paper remains publishable
and the arc remains intact, ending one stage early, because CONTEXT.md section
8's minimum presentable path already says that a study calibrated and extended is
a complete result.

**what the presentation loses.** one slide, and the strongest closing sentence
available. the fallback closing sentence is "the effect is calibrated exactly and
reproduces on standard benchmarks; whether it persists on problems stated as
interval-valued at source is the next step, and here is the gate we would apply",
which is weaker but is not an apology.

**both are known before the reading and not after it**, which is the point of
writing this paragraph today.

### d3. if one example is small enough to derive in closed form

**that is a second calibration point on an unadapted problem, and it is
materially stronger than anything else available to this project.**

what it adds: the whole force of the claim's first clause -- exactly quantified,
not sampled -- transferred from a problem the project designed to a problem a
third party published for a different purpose. the standing objection to p1 is
that it was built to make the three phi differ, which it was, a1 part 3 being the
record of four designs rejected for making them coincide. a published
interval-native problem on which the three phi differ, with the difference in
closed form, removes that objection completely. no other work in the plan removes
it.

what it costs: one derivation session on the b1 template, plus b2's encoding of
the closed form as a reference set, plus the reference-front machinery for a new
problem. call it two sessions beyond f2 and f3, and it lands in the schedule's
last week where there is no slack. **it is therefore scheduled as an optional
session and taken only if f1's gate passes an example whose objectives are
quadratic with constant hessians, where the derivation is the same linear system
as p1's and the two sessions are realistic.** if f1 passes only an example with
exponentials, trigonometric terms or gh-differences in it, the derivation is not
attempted and f3 runs without a reference set.

### d4. the newton method is not this project's subject

stated so that reading does not become implementing. this project does not invent
an algorithm, CONTEXT.md section 1. [16] is read for its problems. the method of
[16] enters this project only if a later session argues for it explicitly and
that argument is recorded as a decision, and no session between here and 25
september has room for it.


## e. the open scope

section 5 of the meeting's decisions: scope is open, every paper is in papers/,
previous exclusions are lifted, search freely, bring in better material, revisit
what was closed off. below is every CONTEXT.md scope statement that supersedes,
with its before and after. the edits are applied to CONTEXT.md in this session
and reproduced in the session reply.

    superseded, with the diff in the session reply:

    section 2, part 2's definition        portfolio out-of-sample performance
                                          becomes the interval-native problems
    section 3, "five papers, no others"   the corpus is open and papers/ is the
                                          corpus
    section 3, the four entries pointing  they point at papers/ now; the pdfs
      at literature/*.md                  have arrived and literature/ does not
                                          exist
    section 4, the clause forbidding a    the supervisors authorised the search;
      phi not named in the paper          the proposal route stays and gains the
                                          containment stopping condition
    section 6, "use optimality theory     removed; the positive list of section 6
      from any paper outside the five     stays and gains [16]
      of section 3"
    section 8, phase f                    rewritten for the interval-native
                                          problems; phase g added
    section 9, the whole list             the fuzzy branch stays a scope choice;
                                          the four exclusions by paper are lifted
    section 10, e3's "selects the phi     part 2 runs all three phi; there is
      carried into part 2"                nothing to select
    section 10, f1 to f4                  rewritten
    section 11, "yfinance is added at     removed with f1's old subject
      f1 and not before"
    section 12, literature/               corrected to papers/resumed/

    **not superseded, and restated because open scope raises its value:**

    the evidence rule. every claim is sourced to a paper by section, example or
    equation number, or to a project deliverable by name and section. an
    unverified item is left out rather than flagged and kept. where a summary and
    a paper disagree the paper wins. an ambiguity is recorded as an ambiguity and
    not resolved by choosing the convenient reading.

    **why open scope raises its value rather than relaxing it.** a five-paper
    corpus is self-policing: with five papers on disk, a claim's source can be
    checked by reading all five. an open corpus is not, and the number of places a
    number could have come from is now the number of places a wrong number could
    have come from. the rule is what keeps an open corpus from becoming an
    unsourced one, and CONTEXT.md now says so in section 11.


## f. the prediction, corrected before it is registered

### f1. what is already proved, and is therefore not registered

the draft prediction -- that under phi_ls and phi_cw a solver's front carries
points outside the derived region and under phi_lu it does not -- is not a
prediction. it is proved twice over.

*by the closed form.* docs/part1/b1_phi_efficient_sets.md section 2.4 gives X_cw as the
closed unit square minus the open segment {(x_1, 0) : 0 < x_1 ≤ 1}, so the origin
lies in X_cw; the origin lies in X_ls likewise; and X_lu is contained in
[0, 4/3] x [4/5, 4/3], whose x_2 range excludes it. so the three sets already
differ at a named point and no measurement is needed to establish it.

*by the general mechanism.* v-54 proves it: under phi_ls the fourth image column
is 2 r_2 and under phi_cw it is r_2, both being rho x_1^2 + delta, a strictly
increasing function of |x_1| and of nothing else, so the member of any finite set
with strictly smallest |x_1| is its strict minimiser in that column and nothing
dominates it, whatever its x_2 is; under phi_lu every column moves with both
variables and the hypothesis is unavailable.

**two corrections of fact carried into everything below.** delta is 1/8 and not
1/10, since d-01 and docs/part1/a4b_dominance_tolerance.md part 2. and the condition is
that the column be a function of a **strict subset** of the decision variables
with a unique minimiser, **not** that the minimiser be interior: dtlz2's width is
minimised at x_n = 0, on a face, and the mechanism applies there.

### f2. the general condition, stated

let phi be admissible and let the transformed problem have image columns
g_1, ..., g_2m. for each k let T_k be the set of decision variables g_k actually
depends on, and let F_k = {1, ..., n} \ T_k be its **free set**. let X_phi be the
phi-efficient set, let P_k be the projection of X_phi onto the coordinates F_k,
and let B_k be the projection of the box onto the same coordinates.

> **the protected-minimiser effect appears at the pair (problem, phi) exactly
> when some column k has F_k non-empty and P_k a proper subset of B_k of positive
> co-measure, that is |B_k \ P_k| > 0.**

*the mechanism, in two steps.* first, protection: for any finite candidate set S,
the member minimising g_k strictly over S is dominated by no member of S, since
domination requires being no worse in every column and therefore no worse in
column k. this half is elementary and holds for any column. second, and this is
where F_k enters: because g_k does not depend on the variables in F_k, the
protected member's F_k-coordinates are entirely unconstrained by its protection,
so for a uniform draw of the box they are uniform on B_k, and the protected member
lies outside X_phi with probability |B_k \ P_k| / |B_k| > 0 at every budget.

*it reproduces v-54's constants exactly*, which is the check that the
generalisation is the right one. take p1 under phi_cw and k = 4, where
g_4 = r_2 = rho x_1^2 + delta: T_4 = {1}, F_4 = {2}, P_4 = [0, 1] from b1 section
2.4, B_4 = [−1/2, 3/2]. the probability is (2 − 1)/2 = **1/2** and the expected
overhang is

    ∫_{−1/2}^{0} (−x_2) dx_2 / 2 + ∫_{1}^{3/2} (x_2 − 1) dx_2 / 2
      = (1/2)(1/8) + (1/2)(1/8) = **1/8**

which are v-54's two constants, derived here from the general form rather than
from p1's algebra.

*and it explains why phi_lu is exempt on p1 and not by anything about phi_lu.*
under phi_lu the four columns are c_1 ∓ r_1 and c_2 ∓ r_2, and every one moves
with both variables, so every F_k is empty and the condition fails. **that is a
property of the pair (p1, phi_lu) and not of phi_lu**, and the analysis below is
what makes the difference matter.

### f3. confirmed or refuted analytically for zdt1 and dtlz2, from their a5 forms

**zdt1**, n = 30, box [0, 1]^30, m = 2, eps > 0. a5's form: c_1 = f_1 = x_1,
c_2 = f_2 = g (1 − sqrt(x_1/g)) with g = 1 + 9 (Σ_{i=2}^{30} x_i)/29, and
r_1 = r_2 = r = eps((x_30 − 1/2)^2 + 1/20).

    phi_cw   g_1 = x_1            T = {1},      F = {2..30}
             g_2 = g_4 = r        T = {30},     F = {1..29}
             g_3 = f_2            T = all,      F = empty
    phi_ls   g_1 = x_1 − r        T = {1, 30},  F = {2..29}
             g_2 = g_4 = 2r       T = {30},     F = {1..29}
             g_3 = f_2 − r        T = all
    phi_lu   g_1 = x_1 − r        T = {1, 30},  F = {2..29}
             g_2 = x_1 + r        T = {1, 30},  F = {2..29}
             g_3 = f_2 − r, g_4 = f_2 + r      T = all

the free sets are non-empty under **all three phi**, phi_lu included, because
zdt1's own first objective is f_1 = x_1, a function of one variable, and the
shared half-width depends on x_30 alone. and the projections are as degenerate as
they can be: raising any x_i with 2 ≤ i ≤ 29 raises g, and f_2 = g − sqrt(x_1 g)
has df_2/dg = 1 − sqrt(x_1)/(2 sqrt g) > 0 for g ≥ 1 and x_1 ≤ 1, so raising such
an x_i strictly raises columns 3 and 4 and leaves columns 1 and 2 unchanged.
hence X_phi ⊆ {x_2 = ... = x_29 = 0} under **every** phi, and P_k is a
measure-zero subset of B_k for every k with F_k non-empty.

> **refuted for zdt1.** the effect is present under phi_lu as well as under
> phi_ls and phi_cw, and with probability 1 rather than 1/2. the clause "and not
> under phi_lu" is false there, and it is false for a structural reason: p1 has
> no separable objective and zdt1 has one, f_1 = x_1, which is a property of the
> whole zdt family and not of the interval construction.

**dtlz2**, n = 12, box [0, 1]^12, m = 3, eps > 0. a5's form:
g = Σ_{i=3}^{12}(x_i − 1/2)^2, c_1 = (1+g) cos(x_1 π/2) cos(x_2 π/2),
c_2 = (1+g) cos(x_1 π/2) sin(x_2 π/2), c_3 = (1+g) sin(x_1 π/2), and
r_1 = r_2 = r_3 = r = eps x_12.

    phi_cw   g_2 = g_4 = g_6 = r  T = {12},          F = {1..11}
             g_1 = c_1            T = all
             g_3 = c_2            T = all
             g_5 = c_3            T = {1, 3..12},    F = {2}
    phi_ls   g_2 = g_4 = g_6 = 2r T = {12},          F = {1..11}
             the three centre-minus-width columns as under phi_lu below
    phi_lu   g_1 = c_1 − r, g_2 = c_1 + r           T = all
             g_3 = c_2 − r, g_4 = c_2 + r           T = all
             g_5 = c_3 − r, g_6 = c_3 + r           T = {1, 3..12},  F = {2}

under phi_cw and phi_ls the width column has F = {1..11}, and raising any x_i
with 3 ≤ i ≤ 11 raises g and hence every centre, so X_phi ⊆ {x_3 = ... = x_11 =
1/2} and P is measure zero in [0, 1]^11. **effect present, and maximal.**

under phi_lu **no column has a free set whose projection is a proper subset**.
the only columns with a non-empty free set are g_5 and g_6, whose free set is
{2}, because c_3 = (1+g) sin(x_1 π/2) does not involve x_2. and the projection of
X_lu onto x_2 is the whole of [0, 1]: x_1 and x_2 parametrise dtlz2's front and
are unconstrained on it, the same domination argument as above pinning only
x_3 through x_11. so P = B for the only k with F_k non-empty, and the condition
fails.

> **confirmed for dtlz2**, and confirmed for a subtler reason than the draft
> gave. it is not that phi_lu's columns all depend on every variable -- two of
> them do not -- but that the variable they omit is one the efficient set does
> not constrain, so omitting it costs nothing.

**the registered prediction, in its corrected form:**

> the protected-minimiser effect appears at a pair (problem, phi) exactly when
> some image column under phi is a function of a strict subset of the decision
> variables and the phi-efficient set's projection onto the complementary
> variables is a proper subset of the box's, of positive co-measure. it is
> therefore predicted present on p1 under examples 2.3 and 2.4 and absent under
> example 2.2; present on zdt1 under **all three**; present on dtlz2 under
> examples 2.3 and 2.4 and absent under example 2.2; and present on any
> interval-native problem satisfying the same condition, which f1 records per
> example under criterion 4 of section d0.

### f4. the two measurements, fixed now

both are fixed before phase e runs so that neither is available afterwards as an
explanation of whatever phase e returns. they are computed from e1's and e2's
existing artefacts and need no new module.

**m-1, the tail-survival lift. this is the confirming measurement.** for each
problem, each phi, and each column k with F_k non-empty: take random search's
uniform sample of the box at the gate budget of 5000, at each of the five seeds;
filter it under phi; order the sample ascending by g_k; record s_30, the fraction
of the thirty smallest that survive the filter, and the chance rate
c = |front| / 5000. the lift is L = s_30 / c, reported per seed with the median
and interquartile range.

    predicted present  L >= 3
    predicted absent   L <= 1.5, taken as the maximum over all columns, since
                       where no column has a free set the statistic is computed
                       on every column and the largest one is what must be small

**m-2, the overhang. this is the refuting measurement.** for each seed, take the
protected member -- the argmin of g_k in that seed's sample -- and record the
distance from its F_k-coordinates to the projection of the known efficient
structure: b1 section 2.4's closed form for p1, the set {x_2 = ... = x_29 = 0}
for zdt1, the set {x_3 = ... = x_11 = 1/2} for dtlz2.

    predicted present  median overhang strictly positive
    predicted absent   overhang exactly zero
    and, on p1 under example 2.4, **the mean overhang over seeds equals 1/8 to
    within the seed-to-seed spread.**

that last line is the sharpest refutation available anywhere in this project.
1/8 is derived in section f2 from the general form and is not fitted to anything.
**if p1's measured mean overhang under example 2.4 is not 1/8 within the seed
spread, the mechanism as stated in f2 is wrong**, and the correct response is to
say so and to withdraw the generalisation, not to adjust the constant.

**what is not evidence either way**, written down so it cannot be offered later:
that the efficient sets differ more under one phi than another; that nsga-ii
covers X_cw worse than X_lu; that the outside fraction is higher under examples
2.3 and 2.4. all three are already established, all three have other
explanations on record, and none of them is m-1 or m-2.


## g. sequencing against four artefacts and one arc

four workstreams -- phase e, more phi, the interval-native problems, the write-up
-- and the presentation is on 25 september. twenty-one days.

### g1. the schedule

    sep 5-6    e1        tier 0 run. stage 3, the calibration measured.
    sep 6      f1        the reading session and its gate. stage 5's gate, and a
                         document session, so it runs beside e1 rather than
                         after it.
    sep 7-8    a5-b      tier 1 width drivers, section b's option 2, plus a1
                         part 4's slice sweep re-run on the new forms.
    sep 9-11   e2        tier 1 run. stage 4.
    sep 12     f2        problems_native.py, if f1's gate passed an example.
    sep 13     e3        results synthesis. stage 4 closed.
    sep 14     f3        the native run, plus its derivation only if d3's
                         condition holds.
    sep 15-16  g1        the results document.
    sep 17     g2        the figure set.
    sep 18-22  g3        the latex memoria.
    sep 23-24  g4        the presentation.
    sep 25     delivery.

    optional, taken in this order and only if two scheduled sessions finish
    early:
       1. b1-b, the closed-form derivation of the path phi_t on p1, section c.
          one session, no runs, and it strengthens the calibration.
       2. the second calibration point of section d3, two sessions, and only if
          f1 passed a quadratic example with constant hessians.

### g2. the cut points, and what each costs the four artefacts

ordered so that the arc stays intact at every cut. **the rule is that stages are
dropped from the end and never from the middle**: a schedule that drops a middle
stage leaves a story with a hole, one that drops the last stage leaves a story
that ends early but ends.

    cut 1, first to go: the optional sessions.
        an extension and not a stage. the paper loses a sensitivity curve it
        never promised; the memoria, the code and the presentation lose nothing.

    cut 2: f3, then f2 -- the native run.
        part 2 becomes f1's reading verdict, section d2's fallback.
        results document: loses one results section, gains a reading section.
        memoria: loses its final chapter's results and keeps its final chapter.
        code: loses one module, which was never built.
        presentation: loses one slide and its strongest closing sentence.
        **the arc ends at the benchmarks, which is where CONTEXT.md section 8's
        original plan ended.**

    cut 3: e2 -- the benchmarks.
        results document, memoria and presentation drop the claim's second
        clause. the arc ends at the calibration, which CONTEXT.md section 8
        already names the minimum presentable path and already calls a complete
        result and not a truncated one.
        **and if e2 is cut, f2 and f3 are cut with it**, whatever the calendar
        says. running the native problems on an instrument calibrated but never
        extended asserts a generality that has not been tested, and it is the
        one ordering in this plan that must not be violated to save days.

    never cut: e1, e3, g1, g3, g4.
        without e1 there is no measurement at all; without e3 there is no
        synthesis; without g1 and g3 there is no artefact; without g4 there is no
        25 september.

### g3. what the supervisors most want, and whether it is what the paper needs

**on the evidence of what they said, the interval-native problems.** point 4 of
the meeting is the longest and most specific of the five: the real subject is
genuine uncertainty, adding a half-width ourselves is what part 1 did and what
part 2 should not need, and [16]'s examples are the problems for part 2. point 2
merely says phase e proceeds as specified, and point 3 says more phi *may* be
searched for, which is permission and not a request.

**that is not what the paper most needs, and the difference should be stated
plainly.** the claim's magnitude comes from the calibration and its generality
comes from the benchmarks. the native problems supply neither: they have no
closed form guaranteed, no reference set, and at f1's gate they may supply
nothing at all. what they supply is the answer to [7]'s objection and the arc's
ending, which are worth a great deal to the *narrative* and nothing to the
*evidence* for the magnitude.

so where the two conflict -- and they conflict for about two days, sep 12 to 14
-- **the middle wins**: a5-b and e2 keep their slots and f2 and f3 give way. the
reason is asymmetric risk. a claim calibrated and extended survives the native
problems failing, and section d2 says exactly what it looks like when they do. a
claim calibrated and applied, with the extension skipped, does not survive a
reviewer asking whether the effect is a property of one two-variable fixture the
authors designed to have it.

**this disagreement is worth putting to the supervisors in one sentence rather
than resolving silently**, since it is their project as much as this repository's:
"we are keeping the benchmark runs ahead of the interval-native application in
the schedule, because the benchmark stage is what makes the p1 number
generalisable and the native stage is what makes it interesting; if you would
rather have the reverse we will do that instead."

### g4. what must exist before each artefact can start

**before the memoria (g3) can be drafted:**

    e1 complete and reviewed, and e3 complete: the claim's first clause has a
        measured number beside its exact one.
    g1 complete: the results document is the memoria's source and the memoria is
        not a second place where results are decided.
    g2 complete: every figure exists as a file under results/figures/ produced by
        a script, and no figure is pending.
    section b's two tables built, with their columns as decided there.
    the number-provenance rule in force, section a2: a memoria that starts before
        the generated fragments exist is a memoria whose numbers are typed.
    the memoria's expected length and language settled, section h.

**before the presentation (g4) can be built:**

    g3's claim sentence frozen, word for word, since the presentation carries the
        claim and must carry the same one.
    the three headline numbers frozen: p1's exact pair statistic, its measured
        counterpart, and the benchmark counterpart.
    two figures chosen from g2's set. the candidates are
        results/meeting/derived_regions_p1.png, which shows the whole project in
        one picture, and one decision-space recovery figure from e1.
    a written list of what is excluded: pymoo, seeds, tolerances, test suites,
        cardinality rules, the reference-front sampling mode, and every subpart
        identifier.


## h. open questions

### h1. what the meeting answered

    s-08, p1's two-dimensional efficient band. **answered.** point 1 accepts part
        1's results as they stand, and the band is what b1 derived and what the
        meeting document presented. the row retires to docs/answered.md.
    the deliverable format. **answered and recorded**: a paper-like results
        document, a latex memoria, the code repository, and a short presentation
        without implementation detail. this was not an s-row and is now recorded
        as one closed on arrival.
    whether part 1's adapted problems undermine the study. **answered, and it was
        the meeting's own point 1.** part 1 was a test; its purpose was to make
        the order relations comparable at all; it succeeded; nothing is retracted.
        this was never an s-row and it is recorded because it is the reason part 1
        is reported as a controlled test on adapted problems rather than defended
        as a realistic one.
    whether more phi may be added. **answered: yes, subject to the framework's
        conditions.** this converts CONTEXT.md section 4's prohibition into a
        procedure, section e, and section c supplies the stopping condition the
        answer does not.
    the subject of part 2. **answered**: the interval-native examples of [16],
        with no uncertainty added by us. the portfolio application moves to future
        work, where slide 21 already places it.

### h2. what the meeting did not answer, and which are now moot

    **still open and unanswered, and all of them still worth asking:**
    s-01  the w subscripts in (16) of [1].
    s-02  example 3.9's weight phrase, nonnegative-and-not-all-zero against
          strictly positive, with b1's witness at (4/3, 1) under example 2.2.
    s-03  which efficiency theorem 3.1 means.
    s-04  whether CONTEXT.md section 2 should record that [1]'s own conclusion
          compares two phi.
    s-06  whether the memoria presents the centre-radius form as the working form
          of phi or as an implementation note.
    s-09  one absolute half-width per tier 1 objective, or scaled per objective.
          **note that section b's option 2 does not answer it**: distinct width
          drivers and per-objective scaling are independent choices.
    s-10  the double seeding.
    s-11  the containment criterion, its two containments, and whether any of it
          is published. **its third part is no longer unanswerable inside the
          project**: [1]'s pdf is now in papers/ with its reference list, so [1]'s
          own [9], [26] and [31] can be resolved, and section c has already found
          that ishibuchi and tanaka's proposition 4.1 agrees with the criterion on
          a case the criterion decides. s-11 stays open for the supervisors and
          gains a project-side reading task.
    s-12  the singular segments.

    **moot now that scope has opened:**
    s-05  whether CONTEXT.md section 9's exclusion of section 5 of [1] stands.
          **moot.** section 9's paper-level exclusions are lifted, so proposition
          5.1 may be read and cited like any other published result. what is not
          moot and is retained as a working rule is that the project does not
          assert an interval analogue of a fuzzy proposition without deriving it;
          the analogue it has, s-11's criterion, was derived independently.
          s-05 moves to docs/answered.md with that reasoning.

    **p-rows, and open scope changes all of them.**
    p-01  [1]'s notation and its references [7], [9], [23], [26], [31].
          **now answerable**: [1]'s pdf is in papers/. it stops being a question
          for the supervisors and becomes a reading task.
    p-02  whether [9] states the centre-width comparison in example 2.4's
          coefficients. **substantively answered in section c2 from the paper**,
          which is now in papers/: definition 3.4, equations (3.11) and (3.12),
          with a_w the half-width by the paper's own equation (4.6). the row
          moves to docs/answered.md when a session records it with printed page
          numbers, which section c did not.
    p-04  whether [7] or [8] drives the interval width from the decision vector.
          **now answerable**: both pdfs are in papers/, and [13] is a third source
          of the same kind. e3 no longer has to cite the summaries.
    p-05  [10]'s definition and theorem numbers for the gh-difference and the
          midpoint-radius regularity criterion. **now answerable**: [10]'s pdf is
          in papers/. this closes the one unverified number in b1's derivation.
    p-06  whether [1] identifies its "strict minimum" with one of definition
          3.1's names. **now answerable** with [1]'s pdf, and the answer is wanted
          before the memoria prints p0's status.

    **r-03 retires.** its whole content was that [1]'s pdf was absent and the
    extracted text lacked its reference list and two glyphs. the pdf is in
    papers/. it moves to docs/answered.md.

### h3. two email-today items

neither is in the meeting record and both block g3.

    **the memoria's expected length.** a twenty-page memoria and an eighty-page
    memoria are different documents with different section structures, and g3
    starts on 18 september. what is wanted is a page range and whether appendices
    count toward it.

    **the memoria's language.** the supervisors' proposal is in spanish, this
    repository's documents are in english, and every source paper is in english.
    a spanish memoria means translating the whole of the results document, which
    is a real cost that has to sit in the schedule rather than be discovered on 18
    september; and it means fixing spanish terms for centre, half-width, full
    width, order relation, efficient set and automorphism before anything is
    written, so that one word is not used for the half-width and the full width,
    which CONTEXT.md section 4 forbids in english for a reason that does not
    change with the language.

both are one email. it should go today.
