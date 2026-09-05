# e3: the synthesis, and the answer to part 1

session e3, 2026-09-05. no experiment, no module and no re-run: every number
below is read out of a file that experiments/run_tier0.py or
experiments/run_tier1.py wrote, and the file is named beside it. where a number
is derived from two such numbers by an identity stated elsewhere in the project,
it says so and gives the identity. e1 and e2 deliberately did not interpret.
this document interprets, and it is written so that g1 can lift from it.

**this document and docs/part1/part1_closing.md are the nearest overlap in the
repository and the pair most likely to drift, so the difference is stated here and
in that file's header**, docs-clean, 2026-09-05. this one is **the working
synthesis**: the full reasoning, every intermediate step, the alternatives weighed
and rejected, and the section-by-section argument from e1's and e2's artefacts to
part 1's answer. part1_closing is **the settled record**: the same answer
compressed to what a reader needs to act on it, plus what this document does not
have — the question in the supervisors' own terms, the arc, the methodological
results, and what part 1 hands to part 2 with its five-criterion gate. both check
the same four prohibitions, each against its own text. **part1_closing is canonical for part 1
and is the one g1 lifts from**; this document is where g1 goes for why a
conclusion holds, and it is not superseded by it. if the two ever disagree, the
artefact settles it and whichever of the two is wrong is corrected.

what this is the answer to: CONTEXT.md section 10 e3 and docs/plan_after_meeting.md
section a2 stage 4. how much the recovered efficient sets differ across phi, in
the decision space, with the variance across seeds, under which conditions the
difference appears or grows, and how far the benchmark numbers can be trusted
given what the calibration measured.

**the four things this document may not do**, and each is checked at the end.
it may not rank phi: the project has no external criterion and the new part 2
supplies none, docs/plan_after_meeting.md section a2. it may not claim anything
from the containment while s-11 is unanswered, docs/part1/a_close_containment.md
section 6. it may not quote a slice fraction as a quantity, r-22. and it may not
interpret a benchmark number without the instrument's error beside it.


## 1. the answer, in one paragraph

on the one problem where the phi-efficient sets are known in closed form, two of
[1]'s own named orders share **0.103177 of their union** and neither set contains
the other: 0.605290 of X_lu lies outside X_cw and 0.877429 of X_cw lies outside
X_lu, in exact lebesgue measure, with no sampling and no solver in the number.
the same statistic measured on recovered sets at thirty and at twelve variables
gives a jaccard of 0.087 to 0.133 on zdt1 and 0.136 to 0.322 on dtlz2 across the
four positive imprecision levels. the calibration says those measured values are
**upper bounds on true sharing**: on p1, at the same budget and by the same
instrument, the measurement returns 1.81 times the exact jaccard, and the sign
of that bias is shown below to transfer to the benchmarks by direct measurement
rather than by assumption. so the orders share less at thirty and twelve
variables than the tables print, and the difference between two admissible
orders is not a modelling detail on any of the three problems.

what the benchmarks change is the **shape** of the disagreement, not its size.
on p1 the two sets are genuinely non-nested. on both benchmarks X_lu sits largely
inside a much larger X_cw. section 4 reports that rather than letting one jaccard
column imply the geometry is the same.


## 2. the comparison neither run made

e1 has the exact numbers and no benchmarks. e2 has the benchmarks and no exact
numbers. this is the table that puts them on one page, and it is the claim.

the pair throughout is **example 2.2 against example 2.4**, phi_lu against
phi_cw. it is the only one of the three that is nested in neither direction, so
it is the only one where nothing is fixed before a solver runs; the other two are
checks and section 6.4 says why. all rows are random search's one filtered sample
through src/random_search.py's filter_one_sample_under_every_phi, at delta zero,
budget 5000, five seeds. delta zero is the headline, d-08: the three sets of one
comparison are index sets over one array, so two decision vectors are the same
point bitwise or they are two points and the coverage is exactly the shared count
over the count.

| problem | n | level | cov(lu→cw) | cov(cw→lu) | jaccard | \|X_lu\| | \|X_cw\| |
| --- | --- | --- | --- | --- | --- | --- | --- |
| p1, **exact** | 2 | rho = 1/4 | 0.394710 | 0.122571 | **0.103177** | 0.310533 | 1.000000 |
| p1, measured | 2 | rho = 1/4 | 0.555932 | 0.221859 | 0.187190 | 608 | 1528 |
| zdt1 | 30 | eps 0.00 | 1.000000 | 1.000000 | 1.000000 | 18 | 18 |
| zdt1 | 30 | eps 0.05 | 0.846154 | 0.088000 | 0.086614 | 26 | 257 |
| zdt1 | 30 | eps 0.10 | 0.722222 | 0.101167 | 0.094891 | 36 | 257 |
| zdt1 | 30 | eps 0.25 | 0.660000 | 0.120623 | 0.108772 | 53 | 257 |
| zdt1 | 30 | eps 0.50 | 0.545455 | 0.159533 | 0.133117 | 68 | 257 |
| dtlz2 | 12 | eps 0.00 | 1.000000 | 1.000000 | 1.000000 | 150 | 150 |
| dtlz2 | 12 | eps 0.05 | 0.897541 | 0.138267 | 0.136486 | 278 | 1813 |
| dtlz2 | 12 | eps 0.10 | 0.851964 | 0.167527 | 0.162312 | 351 | 1813 |
| dtlz2 | 12 | eps 0.25 | 0.779967 | 0.245375 | 0.229867 | 575 | 1813 |
| dtlz2 | 12 | eps 0.50 | 0.684211 | 0.371760 | 0.321871 | 980 | 1813 |

provenance, key by key. p1's exact row is results/tier0/exact_regions_p1.csv,
keys coverage_a_in_b, coverage_b_in_a and overlap_union_share on the (lu, cw)
pair, with the two areas under key area; the exact areas are lebesgue measures of
the closed-form regions of docs/part1/b1_phi_efficient_sets.md section 2.4 and the two
"lies outside" figures in section 1 are one minus each coverage. p1's measured
row is results/tier0/table_2_measured.csv, decision block, delta 0.0, n_evals
5000; its cardinalities are that table's cardinality_a and cardinality_b. **p1's
measured jaccard is the one derived number in the table**: e1 wrote dice
0.315349 and jaccard = dice / (2 − dice) is the identity e2 section 5 states and
uses throughout, giving 0.187190. the benchmark coverages are
results/tier1/table_2_measured_eps_*.csv, decision block, delta 0.0, n_evals
5000; the benchmark jaccards are results/tier1/overlap_conventions.csv, key
jaccard_median, which e2 computed by the same identity so the two are the same
functional.

### 2.1 the instrument overstates agreement, and by how much

results/tier0/instrument_error_p1.csv is the only file in the project that
compares a derived quantity with the same quantity measured; it carries the exact
value, the measured median and their difference. the **relative** error is
results/tier1/inherited_instrument_error.csv, which e2 wrote by reading tier 0's
artefacts back and dividing, and it is the column quoted here. on the headline
pair at budget 5000 it is **+0.408456** on cov(lu→cw), **+0.810049** on
cov(cw→lu) and **+0.685866** on the dice overlap; at 20000 it is +0.277334,
+0.486096 and +0.421450. every row is positive and every row shrinks when the
budget is quadrupled. in the jaccard convention the measurement is
0.187190 against a true 0.103177 at budget 5000 and 0.153329 against the same
true value at 20000, a factor of 1.81 and then 1.49.

so **a measured coverage is an upper bound on true sharing and therefore a lower
bound on how far two orders differ.** that is e2's sentence and e3 keeps it.

### 2.2 the sign transfers, and it is measured and not assumed

the objection a reviewer will make first: the bias was measured on p1, and
nothing licenses carrying it to a thirty-variable problem. that objection is
correct about the **magnitude** and answerable about the **sign**, and the answer
is in the artefacts rather than in an argument.

on p1 the direction of the bias is known: the measured value exceeds the exact
one and falls toward it as the budget rises. if the bias is a finite-sample
artefact rather than a property of p1, the benchmarks must show the same budget
response even though they have no exact value to fall toward. they do, on every
statistic and on both problems. the tier 1 convergence check runs at eps 0.10,
so that is the level compared.

| statistic | p1 | dtlz2, eps 0.10 | zdt1, eps 0.10 |
| --- | --- | --- | --- |
| cov(lu→cw), 5000 → 20000 | 0.555932 → 0.504177, −9.3% | 0.851964 → 0.767640, −9.9% | 0.722222 → 0.633333, −12.3% |
| cov(cw→lu), 5000 → 20000 | 0.221859 → 0.182152, −17.9% | 0.167527 → 0.128424, −23.3% | 0.101167 → 0.087591, −13.4% |
| dice, 5000 → 20000 | 0.315349 → 0.265889, −15.7% | 0.279292 → 0.219599, −21.4% | 0.173333 → 0.154506, −10.9% |

sources: results/tier0/table_2_measured.csv and
results/tier1/table_2_measured_eps_0.1.csv, decision block, delta 0.0, at both
n_evals. **nine of nine move in the same direction, and on p1 that direction is
known to be toward the truth.** the sizes are of the same order too, 9 to 23 per
cent against p1's 9 to 18. that is as much as can be established: the sign of the
instrument's bias transfers, its magnitude does not, and no correction factor may
be applied to a benchmark number.

### 2.3 what may and may not be said about the benchmark numbers

may be said. the measured jaccard of 0.087 to 0.133 on zdt1 and 0.136 to 0.322
on dtlz2 are upper bounds; the two orders share less than that. the fraction of
X_cw lying outside X_lu, one minus cov(cw→lu), falls from 0.861733 to 0.628240
as eps grows on dtlz2 and from 0.912000 to 0.840467 on zdt1, and every one of
those eight figures is a lower bound.

may not be said. that the benchmark jaccard is "about 0.10 as on p1" — the two
are not the same kind of number and only p1's is exact. that the true benchmark
jaccard is 0.087/1.81 — the factor is p1's alone. and no benchmark number may be
quoted anywhere without this section beside it, which is the fourth prohibition.


## 3. the epsilon dependence

**the coverage of X_lu in X_cw falls monotonically as the imprecision grows: from
0.846154 to 0.545455 on zdt1 and from 0.897541 to 0.684211 on dtlz2, across eps
0.05 to 0.50, at delta zero and budget 5000.** so a growing fraction of what
phi_lu selects would be rejected by a decision maker committed to phi_cw, on both
benchmarks, at thirty and at twelve variables. source:
results/tier1/table_2_measured_eps_*.csv, decision block.

### 3.1 the same movement, honestly, from the other side

the jaccard moves the other way: 0.086614 → 0.133117 on zdt1 and 0.136486 →
0.321871 on dtlz2. the two are not in conflict and a reader who is shown only the
coverage column will think they are, so the reason goes in the memoria beside
both.

**the cardinality column is the explanation and it is in the same table.**
|X_cw| is 257 on zdt1 and 1813 on dtlz2 at **every** positive level; |X_lu| grows
26 → 36 → 53 → 68 and 278 → 351 → 575 → 980. the whole eps dependence of the
headline pair is X_lu's. as X_lu grows against a fixed X_cw, more of it falls
outside X_cw (the coverage falls) and more of X_cw is met (the jaccard rises).

that |X_cw| is constant is not a coincidence and is not a measurement artefact.
under example 2.4 the image is (c_1, r_1, ..., c_m, r_m) and eps enters only as a
positive scalar multiple of the r_i. multiplying a column by a positive constant
is a strictly increasing per-column relabelling, which leaves the pareto relation
on R^2m unchanged, so **the phi_cw non-dominated set of a given sample is the
same index set at every eps > 0.** the cardinality column of
results/tier1/table_2_measured_eps_*.csv confirms it exactly, 257 and 1813 at all
four positive levels, and a1's own slice sweep,
docs/part1/a1_uncertainty_model.md part 4, records phi_cw's x_n band pinned at
[0, 0.5] on both benchmarks at every level. no slice fraction is quoted here,
r-22.

the consequence for the memoria's wording: **"the orders diverge as the
uncertainty grows" is true of the coverage and false of the shared fraction of
the union, and the honest sentence names which.** the recommended form is *as the
imprecision grows, phi_lu's efficient set grows into and past phi_cw's, which is
fixed; the fraction of phi_lu's answer that phi_cw would reject rises from 0.15
to 0.45 on zdt1 and from 0.10 to 0.32 on dtlz2.*

### 3.2 was it predicted, and where

**yes, and before either run.** docs/part1/a1_uncertainty_model.md part 4, "the levels
to sweep", states from the slice sweeps that *phi_lu is the sensitive one*, that
its efficient set grows with eps on both benchmarks, and that *phi_cw is stable*,
its width-variable band pinned on both. the five levels were placed to resolve
exactly that: two where phi_lu is still tight and two where it has opened up.
e2's cardinality column confirms the prediction on the run's own output and not
on the slice, which matters because r-22 makes the slice fractions
grid-resolution dependent and forbids quoting them as quantities. the direction
is what was predicted, the direction is what is confirmed, and no fraction is
carried across.

what was **not** predicted anywhere: that the coverage and the jaccard would move
in opposite directions. that is e3's, and it follows from the invariance in 3.1.


## 4. the shape, which the magnitude hides

### 4.1 p1: genuinely non-nested

results/tier0/exact_regions_p1.csv. 0.394710 of X_lu lies in X_cw and 0.122571 of
X_cw lies in X_lu. both are strictly between zero and one, so neither set
contains the other, and both are small, so the disagreement is two-sided. the
geometry behind the numbers is in docs/part1/b1_phi_efficient_sets.md section 2.4:
X_cw is the closed unit square less one open edge, X_lu is a curved sliver
contained in [0, 4/3] × [4/5, 4/3]. X_lu reaches above x_2 = 1, where X_cw does
not go, and X_cw fills x_2 < 4/5, where X_lu does not go. each set has a region
the other cannot reach.

### 4.2 tier 1: one-sided

on both benchmarks, at every positive level, cov(lu→cw) is far larger than
cov(cw→lu): 0.846 against 0.088 at zdt1 eps 0.05, 0.898 against 0.138 at dtlz2
eps 0.05. |X_lu| is 26 against |X_cw| = 257 and 278 against 1813. **X_lu sits
largely inside a much larger X_cw.** the same magnitude of disagreement as p1 in
the jaccard column, a different geometry underneath it.

reporting only the jaccard would say the two situations are alike. they are not,
and the decision-relevant reading differs: on p1 a decision maker who switches
order loses most of the set in both directions; on the benchmarks at low
imprecision, switching from phi_cw to phi_lu is close to a *restriction* and
switching the other way is close to an *enlargement*. both are still large
changes and neither is nesting — the containment criterion of
docs/part1/a_close_containment.md section 1 does not apply to this pair in either
direction, and tests/test_problems_tier1.py asserts 0 < containment < 1 both ways
at every positive level — but the failure of nesting at tier 1 is by a small
margin in one direction and a large one in the other.

### 4.3 the one statistic that is stable across the dimension change

the symmetric hausdorff distance, in units of the box diameter that
results/tier0/table_2_measured.csv and results/tier1/table_2_measured_eps_0.1.csv
print in the box_scale column of the same row:

| pair | p1, n = 2 | dtlz2, n = 12, eps 0.10 | zdt1, n = 30, eps 0.10 |
| --- | --- | --- | --- |
| lu, cw — the finding | 0.339524 | 0.291658 | 0.386729 |
| lu, ls — a check | 0.342539 | 0.292356 | 0.386729 |
| ls, cw — a check | 0.132605 | 0.254096 | 0.329073 |

the headline pair's normalised hausdorff distance is 0.29 to 0.39 across two,
twelve and thirty variables. the coverage numbers are not comparable across those
three problems — measure becomes count, the sample density per unit volume
collapses, and section 5.1 shows the delta-ball control failing outright — and
this one is, because dividing by the box diameter removes the only quantity that
changed.

**two caveats and they are not small.** the hausdorff distance is a maximum over
one set of the distance to the other, so it is driven by the single
worst-separated point and says nothing about bulk disagreement; and
results/tier0/exact_regions_p1.csv carries **no exact hausdorff**, so unlike the
coverage and the overlap this statistic was never calibrated and section 2.1's
error does not cover it. it is offered as a scale-free corroboration of the
coverage story, not as a second headline number.

### 4.4 what changes the geometry

three candidates were available and the artefacts discriminate between two of
them.

*not the benchmark's structure.* zdt1 has a separable first objective, f_1 = x_1,
and dtlz2 has none; their g functions differ in form and in the location of their
optima; their objective counts differ, m = 2 against m = 3. both show the same
one-sided geometry at every level. so the structure of the underlying crisp
problem is not what produces it.

*not the dimension, between twelve and thirty.* dtlz2 at n = 12 and zdt1 at n = 30
agree in geometry and differ only in degree. if dimension were the driver the two
would separate, and they do not. **what dimension does change is measurable and
is elsewhere**: the delta-ball control collapses between two and twelve variables,
section 5.1, and the delta sweep goes from steep on p1 to exactly flat on both
benchmarks, e2 section 6. so the dimension bites on the *instrument* and not,
between 12 and 30, on the *geometry*.

*the width forms are what is left, and the evidence is indirect.* what p1 has and
neither benchmark has is a half-width whose driver is also a centre driver:
docs/plan_after_meeting.md section b4 records p1 carrying r_1 = rho x_2^2 + delta
and r_2 = rho x_1^2 + delta, each objective's width driven by the other
objective's own variable, so under phi_lu every image column moves with both
variables. on tier 1 under a5-b the drivers are x_29 and x_30 on zdt1 and x_10,
x_11 and x_12 on dtlz2, variables that carry no centre by construction — a5-b's
own rule, PROGRESS.md's a5-b entry, is that no variable carrying a centre may
drive a width. that difference is exactly the difference in the free-set
structure of section 5, and the free set is what the protected-minimiser
mechanism runs on.

**this is a hypothesis and e3 does not close it.** what would decide it is one
run and it is not e3's: p1's own width design transplanted onto zdt1, a width
driven by x_1, which carries a centre. that is a variant of a5 and not a new
problem family, and it is recorded here as the cheapest thing that would turn a
plausible mechanism into a measured one. it is out of scope before 25 september.


## 5. the two things to settle

### 5.1 the noise floor: measured, withdrawn, and what replaces it

**the construction failed, and it failed for a structural reason and not a tier 1
one.** docs/plan_after_meeting.md section b1 requires a noise floor — the same
coverage statistic between two seeds of the *same* phi — and calls it "the single
addition without which the benchmark table cannot be read at all". it is
identically zero on both benchmarks, at every level, under every phi:
results/tier1/table_2_measured_eps_*.csv and e2 section 12.

the reason is that two independent uniform samples of a continuous box share no
point, at any dimension, so the floor is zero at delta zero by construction and
the construction always needed delta > 0. what tier 1 adds is that **delta > 0 is
a step function at these dimensions and never an informative intermediate value.**
results/tier1/noise_floor_sweep.csv at eps 0.10, budget 5000, as a fraction of
the box diameter:

| problem | 0.05 | 0.10 | 0.20 | 0.30 | 0.50 |
| --- | --- | --- | --- | --- | --- |
| zdt1, the three phi | 0.000000 | 0.000000 | 0.000000 | 0.437500 – 0.896000 | 1.000000 |
| dtlz2, the three phi | 0.000000 | 0.002604 – 0.006619 | 0.734139 – 0.951821 | 1.000000 | 1.000000 |

there is no delta at which the floor is a usable small positive number. so the
control is **withdrawn as measured and not omitted**: it was built, run, swept
and found to have no operating point, and a floor that jumps from 0 to 0.9 tells
a reader nothing about seed-to-seed disagreement. the same fact from the other
side is that the delta sweep on the cross-phi numbers is exactly flat at tier 1,
e2 section 6: the headline coverage does not move at all from delta zero to a
tenth of the box diameter on either benchmark, against p1 where that range took
cov(lu→cw) from 0.555932 to 0.996587. **at tier 1 delta does nothing until it does
everything.** that is d-08's dimension argument measured rather than argued, and
it is a result about the metric and worth one paragraph of the memoria's methods.

**what replaces it is already in the tables.** the headline coverage is computed
from ONE sample filtered three ways, so each seed's value is a deterministic
function of that seed's sample and carries no solver stochasticity at all. the
variation of the statistic across seeds is therefore its complete sampling
variability, and it is the interquartile range e2 already reports.

> **the criterion.** a cross-phi coverage is evidence of a difference between two
> orders when its interquartile range over the seeds is small relative to its
> distance from 1.0, since 1.0 is the value the statistic takes when the two
> orders agree — which the eps = 0 rows show it does take, exactly.

the threshold below is **IQR < 0.25 × (1 − median)**, stated here as a convention
and not as a test against a null distribution; there is no null distribution to
test against, which is precisely why the floor was wanted. the five seeds are
11 to 15 throughout. source for every cell:
results/tier1/table_2_measured_eps_*.csv, decision block, delta 0.0, n_evals 5000,
columns median and iqr.

the headline pair, phi_lu against phi_cw:

| problem | eps | metric | median | iqr | 1 − median | ratio | verdict |
| --- | --- | --- | --- | --- | --- | --- | --- |
| zdt1 | 0.05 | cov(lu→cw) | 0.846154 | 0.153595 | 0.153846 | 0.998 | **fails** |
| zdt1 | 0.10 | cov(lu→cw) | 0.722222 | 0.140086 | 0.277778 | 0.504 | **fails** |
| zdt1 | 0.25 | cov(lu→cw) | 0.660000 | 0.116889 | 0.340000 | 0.344 | **fails** |
| zdt1 | 0.50 | cov(lu→cw) | 0.545455 | 0.097234 | 0.454545 | 0.214 | passes |
| dtlz2 | 0.05 | cov(lu→cw) | 0.897541 | 0.029880 | 0.102459 | 0.292 | **fails** |
| dtlz2 | 0.10 | cov(lu→cw) | 0.851964 | 0.019923 | 0.148036 | 0.135 | passes |
| dtlz2 | 0.25 | cov(lu→cw) | 0.779967 | 0.026399 | 0.220033 | 0.120 | passes |
| dtlz2 | 0.50 | cov(lu→cw) | 0.684211 | 0.043134 | 0.315789 | 0.137 | passes |
| zdt1 | 0.05 | cov(cw→lu) | 0.088000 | 0.030856 | 0.912000 | 0.034 | passes |
| zdt1 | 0.10 | cov(cw→lu) | 0.101167 | 0.015439 | 0.898833 | 0.017 | passes |
| zdt1 | 0.25 | cov(cw→lu) | 0.120623 | 0.027470 | 0.879377 | 0.031 | passes |
| zdt1 | 0.50 | cov(cw→lu) | 0.159533 | 0.031159 | 0.840467 | 0.037 | passes |
| dtlz2 | 0.05 | cov(cw→lu) | 0.138267 | 0.006125 | 0.861733 | 0.007 | passes |
| dtlz2 | 0.10 | cov(cw→lu) | 0.167527 | 0.015551 | 0.832473 | 0.019 | passes |
| dtlz2 | 0.25 | cov(cw→lu) | 0.245375 | 0.013678 | 0.754625 | 0.018 | passes |
| dtlz2 | 0.50 | cov(cw→lu) | 0.371760 | 0.009125 | 0.628240 | 0.015 | passes |

**every one of the eight cells in the direction that carries the claim passes,
and by a wide margin, ratios of 0.007 to 0.037. four of the eight cells in the
other direction fail, and every failure is a cell whose median is near 1.0 on a
small X_lu**: 26 points at zdt1 eps 0.05, 36 at 0.10, 53 at 0.25. the cell that
fails hardest, zdt1 eps 0.05, has an interquartile range as wide as its whole
distance from 1.0.

the two check pairs, for completeness, same source and same rule. on the
containment-fixed direction the coverage is 1.000000 with an interquartile range
of 0.000000 at every level on both problems, and that is a theorem and not a
measurement, so no ratio is formed. on the free direction: cov(ls→lu) has ratios
0.007 to 0.030 on dtlz2 and 0.038 to 0.081 on zdt1, all passing; cov(ls→cw) has
ratios 0.055 to 0.108 on dtlz2 and 0.103 to 0.260 on zdt1, one failure at zdt1
eps 0.10.

**what this costs the memoria and what it buys.** it costs the sentence "the
coverage of X_lu in X_cw is 0.85 at thirty variables" — at zdt1 eps 0.05 and 0.10
that number's seed spread will not support it. it buys the sentence that carries
the claim, which is the other direction: **between 0.63 and 0.91 of X_cw lies
outside X_lu, at every level, on both benchmarks, with a seed spread of one to
four per cent of that figure.** that is the number to put in the presentation.

one control the plan did not count as one, and it is worth naming precisely. at
eps = 0 every half-width is zero, half of the 2m transformed objectives are
constant, and the three phi provably coincide with each other and with the crisp
order. the instrument returns coverage and jaccard of exactly 1.000000 for all
three pairs on both benchmarks, results/tier1/table_2_measured_eps_0.0.csv. that
rules out an encoding, column-order or route-pairing error manufacturing a
spurious difference. **it is not a noise floor**: it does not bound sampling
variability, because at that level the three index sets are literally identical
and agreement is a tautology of the encoding. it is the encoding control, it
works, and it should be reported as what it is.

### 5.2 x-01's zdt1 clause: the registered clause became untestable

x-01, PROGRESS.md section 9, predicts the protected-minimiser effect *present on
zdt1 under all three phi*. e2 measures m-2's median overhang strictly positive on
zdt1 under all three phi at twenty seeds, results/tier1/overhang_summary.csv.
that looks like a confirmation and it is not one, and it is not a refutation
either.

**the argument the clause was registered on.** docs/plan_after_meeting.md section
f3 works from a5's forms, where r_1 = r_2 = eps((x_30 − 1/2)^2 + 1/20) and both
widths read x_30. it argues: raising any x_i with 2 ≤ i ≤ 29 raises g, and
df_2/dg > 0 for g ≥ 1 and x_1 ≤ 1, so raising such an x_i strictly raises columns
3 and 4 and leaves columns 1 and 2 unchanged. hence X_phi ⊆ {x_2 = ... = x_29 = 0}
under every phi, and the projection onto any non-empty free set is measure zero.

**a5-b moved r_2 onto x_29.** x_29 now drives a width column, so raising x_29 no
longer leaves the width columns alone and the domination argument does not apply
to it. the argument re-run on a5-b's forms pins one variable fewer:
X_phi ⊆ {x_2 = ... = x_28 = 0}, with x_29 unconstrained by it. that is the second
structure e2 reports and it names both,
results/tier1/overhang_summary.csv column *structure*, values registered_x01 and
a5b_domination_argument. the free sets are what the run measured rather than
asserted, results/tier1/free_sets.csv: under phi_lu, columns 0 and 1 depend on
{x_1, x_30} with a free set of 28 and columns 2 and 3 depend on every variable;
under phi_ls and phi_cw the three width columns depend on one variable each.

**so the measurement is against a reference structure the problem no longer has.**
the registered structure {x_2 = ... = x_29 = 0} is a proper subset of the correct
one, and a distance to a smaller set is larger, which is exactly what the two
columns show: at eps 0.10 under phi_lu the median overhang on column 0 is
3.007057 against a5-b's structure and 3.050320 against x-01's, and on column 1
2.934039 against 3.027359. the difference is small and the sign is systematic,
and it is the whole of what changed.

> **verdict: the zdt1 clause of x-01 is untestable on the problem that was run.**
> it is not scored confirmed, because the prediction was derived from a5's forms
> and the measurement was taken on a5-b's, which is a different problem; a
> registered prediction is about a named object and changing the object voids the
> registration. it is not scored refuted, because nothing measured contradicts it:
> under either structure the median overhang is strictly positive on zdt1 under
> all three phi, and under a5-b's structure — which is a *superset* of the true
> efficient set, so the distance to it is a lower bound on the true overhang — the
> positivity holds a fortiori.

**what the clause would have to be to be testable on a5-b's forms.** three things,
and the third is the one that was missing.

    it must be derived from a5-b's forms. the derivation exists and is the
    a5b_domination_argument structure above; what does not exist is a document
    deriving it before the run rather than a run computing it beside the
    registered one.

    it must name {x_2 = ... = x_28 = 0} as the reference structure and x_29 as
    unconstrained by the domination argument, so that the overhang measures a
    distance to the set the efficient points actually lie in.

    it must be able to come out both ways on this problem, and **on zdt1 it
    cannot.** under a5-b's forms every phi has a non-empty free set whose
    projection is measure zero, so the condition of x-01 says *present* under all
    three and zdt1 can supply a "present" observation and never a discriminating
    one. zdt1 is a one-sided test of the mechanism whichever forms it carries.

that last point is the one that should reach the memoria, because it says where
the mechanism's evidence actually comes from, and it is not zdt1.

### 5.3 the dtlz2 clause: confirmed, and confirmed within one phi

x-01 predicts the effect **present on dtlz2 under examples 2.3 and 2.4 and absent
under example 2.2**, and the reason it gives for the absence is subtle and worth
repeating: not that phi_lu's columns all depend on every variable — two of them
do not — but that the variable they omit, x_2, is one the efficient set does not
constrain, so omitting it costs nothing and P_k = B_k.

a5-b does not touch this clause. it moved r_1, r_2 and r_3 from x_12 onto x_12,
x_11 and x_10, all three of which sit in g's sum; none of them is x_2; so the free
set of phi_lu's columns 4 and 5 is still {x_2} and the derivation is unchanged.
results/tier1/free_sets.csv confirms it at the run: under phi_lu, columns 0 to 3
have an empty free set and columns 4 and 5 have a free set of size 1.

what was measured, results/tier1/overhang_summary.csv, twenty seeds, budget 5000,
both structures agreeing on every row:

| phi | column | free set | predicted | median overhang, eps 0.05 to 0.50 |
| --- | --- | --- | --- | --- |
| lu | 0, 1, 2, 3 | empty | undefined | 0.000000 |
| lu | 4, 5 | {x_2} | absent | **0.000000 at all five levels** |
| cw, ls | 0, 2 | empty | undefined | 0.000000 |
| cw, ls | 4 | {x_2} | absent | **0.000000 at all five levels** |
| cw, ls | 1, 3, 5 | 11 variables | present | **0.737044 to 0.842968** |

> **confirmed, and the confirmation is stronger than a phi-level one.** under
> phi_cw on dtlz2, the same phi, the same seeds and the same sample, column 4 has
> a free set of {x_2} whose projection is the whole box and measures **exactly
> 0.000000** with an interquartile range of 0.000000 over twenty seeds, while
> columns 1, 3 and 5 have free sets of eleven variables whose projection is
> measure zero and measure 0.76 to 0.88. the condition discriminates **column by
> column inside one phi**, which removes every explanation that turns on the order
> being different.

the numbers at eps 0.10 under phi_cw, against a5-b's structure and against
x-01's: column 1, 0.760860 and 0.842968; column 3, 0.779586 and 0.814824; column
5, 0.737044 and 0.792455; column 4, 0.000000 and 0.000000. standard errors over
the twenty seeds are 0.021 to 0.033 on the positive columns and 0.000000 on
column 4.

this is x-01's confirmation and it is the project's second result. it is also
where the mechanism's evidence comes from, section 5.2 having removed zdt1's.

### 5.4 m-1 stays withdrawn

m-1, the tail-survival lift, is withdrawn at x-01's outcome line as an instrument
and e2 did not compute it. e3 does not revive it, does not re-threshold it and
does not reinterpret its e1 numbers. the reason is on the record and is
sufficient: it orders a sample by an image column and asks whether the smallest
members survive the filter, which conflates being *protected* with being a
*genuinely good point*, and under example 2.2 the image columns are the real
objectives so an extreme member survives for ordinary reasons. e1 measured 8.22
where the prediction says at most 1.5 and 1.65 to 2.27 where it says at least 3,
which is the same non-discrimination from both sides. **the mechanism stands and
the instrument does not**, and fixing both thresholds before the run is what made
the failure visible. that is itself a methods result and belongs in the memoria.


## 6. the solver question, answered separately

**this section is never mixed into section 2.** the objective-space metrics are
valid for comparing solvers under one fixed phi and are never a ranking of phi,
CONTEXT.md section 5 step 5; each phi maps the problem into a different space on
a different scale, and a ratio taken across two phi here is a ratio of volumes in
two different spaces. the decision-space pairs of nsga-ii's and mopso's own
output, which the same files carry, are a question about the solvers and never a
pair number of the study, because there phi drives the search as well as the
ordering.

### 6.1 which configurations produced spread results

a configuration whose rank 1 holds at least the population size of the candidate
set in every seed is one where dominance decides nothing from its first saturated
generation onwards: every survivor is chosen out of one front on crowding
distance alone. source: results/tier1/rank_one_summary.csv, read through the
pymoo Callback docs/part1/c3_validation.md section 5.1 describes, which leaves the
front bit-identical.

| problem | solver | saturating in every seed | of |
| --- | --- | --- | --- |
| dtlz2 | nsga2 | 15 | 15 |
| dtlz2 | mopso | 12 | 15 |
| zdt1 | nsga2 | 12 | 15 |
| zdt1 | mopso | 5 | 15 |

**the structure behind those counts is sharper than the counts.** listing the
non-saturating configurations at budget 5000 from the same file:

    dtlz2  mopso  cw, ls, lu   at eps 0.00 only
    zdt1   nsga2  cw, ls, lu   at eps 0.00 only
    zdt1   mopso  cw at every level; lu at eps 0.00, 0.05, 0.10, 0.25

so for nsga-ii **every one of the twenty-four configurations at a positive
imprecision level, on both benchmarks and under all three phi, saturates in every
seed**; the only three that do not are the crisp baseline on zdt1. for mopso the
same holds on dtlz2, and zdt1 under phi_cw is the single (problem, solver, phi)
combination that keeps dominance pressure at every level.

and the generation at which it happens is ordered and monotone. first saturated
generation, median over the seeds, from the same file:

| problem | solver | phi | eps 0.05 | 0.10 | 0.25 | 0.50 |
| --- | --- | --- | --- | --- | --- | --- |
| dtlz2 | nsga2 | cw | 2 | 2 | 2 | 2 |
| dtlz2 | nsga2 | ls | 2 | 2 | 2 | 2 |
| dtlz2 | nsga2 | lu | 6 | 4 | 3 | 2 |
| zdt1 | nsga2 | cw | 5 | 5 | 5 | 5 |
| zdt1 | nsga2 | ls | 4 | 4 | 4 | 3 |
| zdt1 | nsga2 | lu | 23 | 17 | 15 | 13 |

out of 50 generations. **phi_lu retains dominance pressure longest, on both
benchmarks and under both population solvers, and how long falls monotonically as
the imprecision rises.** that is c3-d's ordering reproduced on a5-b's new forms
and extended from p1 to both benchmarks.

**what it means for reading their metrics.** in every saturating configuration
the front nsga-ii returns from that generation onwards is a *spread* result and
not a *convergence* result: dominance selected nothing after generation 2 to 23,
crowding distance selected everything, and the algorithm ran as a spread
maximiser. a hypervolume or a spread number computed on such a front measures
where the crowding operator put a hundred points inside one non-dominated set. it
does not measure how close the solver got. **at tier 1 there is no measurement of
how close any solver got at all**: src/reference_fronts.py derives a reference
front for p1 alone, so no igd is computed on either benchmark and every
objective-space row carries a reference size of zero, e2 section 7.

this is the empirical form of [7]'s objection and it is the second thing the
memoria's answer to [7] rests on, the first being the coverage deficit below.

### 6.2 the three solvers under each fixed phi

results/tier1/table_3_solvers_eps_0.1.csv, objective block, budget 5000, at the
common cardinality of each comparison — 29 rows on zdt1 and 100 on dtlz2, r-16,
taken across solvers, phi, seeds and both budgets. medians over five seeds.

| problem | phi | hypervolume: mopso | nsga2 | random search |
| --- | --- | --- | --- | --- |
| dtlz2 | cw | 0.036000 | 0.036015 | 0.035567 |
| dtlz2 | ls | 0.346117 | 0.343298 | 0.338159 |
| dtlz2 | lu | 1013.808980 | 1096.181202 | 999.200735 |
| zdt1 | cw | 0.003715 | 0.004484 | 0.002941 |
| zdt1 | ls | 0.015458 | 0.018294 | 0.012965 |
| zdt1 | lu | 32.142555 | 45.842202 | 20.451246 |

read within a row and never down a column. at equal cardinality **nsga-ii has the
largest hypervolume in five of the six (problem, phi) cells and mopso is level
with it in the sixth; random search is last in all six.** quadrupling the budget
raises the hypervolume in fifteen of eighteen solver-phi-problem cells and lowers
it in three — dtlz2 lu nsga2, zdt1 cw nsga2 and zdt1 lu random search — which is
r-18's non-monotonicity, reported and not asserted away.

**and every one of those nsga-ii cells is a saturating configuration**, section
6.1. so the correct reading is: at a hundred rows chosen from one front by
crowding distance, nsga-ii encloses more hypervolume than a hundred rows drawn
uniformly at random from the whole box and filtered. that is a statement about
two spread operators, one of which is "none".

**e1's tier 0 objective block answers no solver question and must not be read as
one.** its rows are at full cardinality — 200 for mopso, 100 for nsga-ii and 608
to 2220 for random search, results/tier0/table_3_solvers.csv — and r-16 measured
the cardinality effect on one fixed front at a factor of 6.5 in igd and 10.3 per
cent in hypervolume, larger than the differences a comparison would be trying to
detect. random search leads e1's p1 table on every metric and that is its
cardinality. the two objective blocks are not comparable with each other either,
e2 section 7, and neither the memoria nor the presentation may place them side by
side.

### 6.3 the nsga-ii coverage deficit, at its established scope

docs/part1/c3_validation.md section 5, and the scope is p1 at n = 2 with a
full-dimensional efficient set and a closed-form region to measure against. it is
reported as a property of one solver and never as a result about phi.

for a full-dimensional efficient set, nsga-ii's decision-space coverage is worse
than uniform random sampling of that set at equal cardinality, **under phi_ls and
phi_cw and not under phi_lu**. nsga-ii returns exactly 100 rows, which is the
cardinality the comparison's distribution is measured at, so no correction is
needed. its fill distance sits at the 85th to the 99th percentile of 1000 uniform
100-point draws under phi_ls and phi_cw, worse than the uniform mean in all ten
measurements, and at the 33rd to the 60th under phi_lu. mopso at its own
cardinality of 200 is above the uniform mean in four of five measurements under
phi_ls and two of five under phi_cw. random search, at the 586 to 2256 rows it
returns, is far below any draw of either size, which is cardinality and not
search.

**reported at its measured size and not at its apparent one.** a phi-neutral
control halves it: random search, whose sample is a pure function of the box, the
budget and the seed, carries +0.243 of the +0.483 swing from phi_lu to phi_ls and
+0.244 of the +0.485 to phi_cw, in units of the uniform mean at k = 100. that
half is the regions' shape acting on the comparator — |X_lu| = 0.310533,
|X_ls| = 1.513401, |X_cw| = 1, and a uniform draw covers the thin curved X_lu
about 40 per cent worse for its area than the two fat regions. **the other half is
nsga-ii's own and has no mechanism.** four candidate explanations are excluded by
direct measurement — rank-1 saturation, wasted front slots, the pullback, and the
alignment of the crowding distance's axes — and e3 revives none of them.

what it does not say: that nsga-ii fails to converge, since no solver returns a
point beating the derivation anywhere; and that nsga-ii covers worse *because of*
the phi, which the control forbids. and one consequence for e3's own instruments:
d1's compute_spread is computed in the objective space where nsga-ii sorts, and
this finding is in the decision space where the result lives, so **a spread
statistic is never read as decision-space coverage** anywhere in this document.

this is why the headline is on random search. c1's control is the instrument
carrying the study's main result rather than a baseline to beat, which is what
slide 17 asked of it.

### 6.4 why two of the three pairs are checks

docs/part1/a_close_containment.md. phi_ls's non-dominated set contains both of the
others, ND_lu ⊆ ND_ls and ND_cw ⊆ ND_ls, for every feasible set and every
objective, both following from one criterion on the map between two automorphisms.
so on the (lu, ls) and (ls, cw) pairs **one direction of every coverage and
overlap statistic is fixed before a solver runs**, and the run shows it exactly:
cov(lu→ls) and cov(cw→ls) are 1.000000 with an interquartile range of 0.000000 at
every level, on both benchmarks, at both budgets and at both deltas, and on p1 as
well. a difference measured on those pairs is in part a theorem and reporting it
as evidence of order sensitivity would be reporting the criterion.

the headline pair is the one nested in neither direction, and nothing there is
fixed in advance.

**and no claim is made from any of it while s-11 is unanswered.** the containment
is used here to *withhold* two pairs from the evidence, which is the conservative
direction: if the supervisors refute it, the instruction is removed, all three
pairs are reported alike, and the headline number does not move because it never
came from those pairs. that asymmetry is worth one sentence in the memoria.


## 7. the paper's claim, tested against the evidence

docs/plan_after_meeting.md section a1, clause by clause. for each: what supports
it, how strongly, and what a reviewer attacks.

**c1. "the choice of order relation is not a modelling detail."**
supported, as the conclusion of c2 to c4 rather than on its own. no separate
attack; it stands or falls with them.

**c2. "on one interval optimization problem, moving between two of the
framework's own named orders replaces most of the optimal set."**
**strongly supported, and exactly.** results/tier0/exact_regions_p1.csv: 0.605290
of X_lu lies outside X_cw and 0.877429 of X_cw lies outside X_lu, in lebesgue
measure, with no sampling, no solver and no tolerance in the number. "most" holds
in both directions.
*the attack*: the two sets are the phi-efficient sets of a problem this project
designed. see c3.

**c3. "calibrated on a problem whose phi-efficient sets are known exactly, the
two sets share 10.3 per cent of their union."**
**strongly supported.** 0.103177 is exact, it is
results/tier0/exact_regions_p1.csv key overlap_union_share on the (lu, cw) pair,
and docs/part1/b1_phi_efficient_sets.md section 2.4 verifies the three closed-form
regions in exact rational arithmetic in both directions — 12341 weight vectors
forward with zero points outside the stated region, 301 region points inverted
with zero failures. the calibration then does what no other paper on order
relations can do: the same quantity measured on recovered sets is 0.187190, and
the gap is the instrument's error, section 2.1.
*the attack, and it is the strongest one available against the whole of part 1*:
**the uncertainty model was selected for separation.** a1 part 4 rejected the
linear half-width r = eps x_n precisely because under it phi_lu and phi_ls give
identical sets and phi_cw gives the crisp order; the quadratic form was adopted
because the three phi come out distinct. a reviewer says: you chose the width
function so the orders would differ, then reported that they differ.
*the answer, and it requires changing the claim's form, section 7.1.*

**c4. "the effect reproduces on standard benchmarks at thirty and twelve
variables."**
**supported in an asymmetric form and not in a symmetric one, and the memoria
must say which.** what reproduces at both dimensions, at every positive level,
with a seed spread of one to four per cent of the figure: **between 0.628 and
0.912 of X_cw lies outside X_lu**, section 5.1's passing column. what does not
reproduce with the same confidence: the reverse fraction, where four of eight
cells fail the seed-spread criterion. what changes: the geometry, from two-sided
non-nesting on p1 to a largely one-sided containment failure at tier 1, section 4.
*the attacks, four of them.* (i) there is no truth on the benchmarks — no closed
form, no reference front, no igd — so the number is a disagreement between two
recovered sets and confounds order sensitivity with solver noise. answered in
part: the instrument is one sample filtered three ways, so there is no *solver*
noise in it, only sampling noise, and section 5.1 quantifies that from the seed
IQR. (ii) the plan's own control failed — the noise floor is identically zero and
has no operating point, section 5.1. answered by replacement and the replacement
is weaker; say so. (iii) the same design objection as c3, since a5 and a5-b chose
the benchmarks' width functions. same answer, 7.1. (iv) the effective column
count. this one **was** answered before the run: a5-b gave each objective its own
width driver and e2 checked at the run that the effective column count is 2m under
every phi at every positive level on both problems, so the headline pair is no
longer a four-column problem against a three-column one, e2 section 9.

**c5. "and it persists on problems that are interval-valued at source."**
**not supported by e1 and e2 together, and it cannot be**: that is phase f, f1's
reading gate has not run, and r-21 records that the gate may pass no example of
[16]. the clause must not appear in any document written before f1 returns a
verdict, and docs/plan_after_meeting.md section d2 already holds the fallback
form.

### 7.1 the weaker claim, which is the one the evidence supports

the design objection cannot be argued away and does not need to be, because the
project measured its own negative arm. a1 part 4 records what happens under the
rejected linear half-width: phi_lu and phi_ls identical at every level and phi_cw
equal to the crisp order. that is not an embarrassment; it is the control.

> **the recommended claim.** the choice of order relation is not a modelling
> detail. under a half-width that is non-monotone in a driver the centres do not
> share, two of the framework's own named orders select substantially different
> efficient sets: on a problem whose phi-efficient sets are known in closed form
> they share 0.103177 of their union and neither contains the other, and on zdt1
> and dtlz2 at thirty and twelve variables between 63 and 91 per cent of one set
> lies outside the other at every imprecision level tested, by an instrument
> calibrated to overstate agreement. under a half-width linear in a driver
> aligned with the centres' own optimum, the same three orders collapse onto two,
> and one of them onto the crisp order. **which of the two regimes an application
> is in is a property of its uncertainty model, and it is checkable before any
> solver runs.**

this is longer, it is conditional, and it is stronger. it turns the design choice
from a vulnerability into the result's second half, it makes the claim falsifiable
on a new problem rather than merely reproducible on a chosen one, and it is the
form that survives a reviewer who asks where the width function came from. it
costs the presentation one extra sentence.

it also raises the value of section 4.4's open question, since "aligned with the
centres" is exactly the axis on which p1 and the two benchmarks differ.


## 8. the four prohibitions, checked

*no phi is ranked.* no table above orders the three, and no sentence says one
order is better. section 6.2 orders three **solvers** under each fixed phi,
within a row, and states that a column may not be read down. section 3.1 says
X_lu grows with eps and X_cw does not, which is a statement about set size and
not about quality. section 5.3 says the protected-minimiser condition holds under
two phi on dtlz2 and fails under the third, which is a statement about the
condition and is symmetric in phi by construction — it holds under phi_lu on zdt1
too, section 5.2.

*nothing is claimed from the containment.* section 6.4 uses it only to withhold
two pairs from the evidence, and records that refuting it would not move the
headline number.

*no slice fraction is quoted as a quantity.* r-22. section 3.2 carries a1 part
4's prediction as a direction and confirms it on e2's cardinality column, which
is not a slice statistic.

*no benchmark number is interpreted without the instrument's error.* section 2.1
and 2.2 establish it, section 2.3 states what may and may not be said, and every
later benchmark figure refers back.


## 9. the figures the memoria and the presentation should use

**f1. the calibration figure. exists.**
`results/tier0/figures/decision_sets_p1_random_search_5000.png` — p1's three
recovered sets drawn over b1 section 2.4's three derived regions, at one seed,
with the seed count and each series' cardinality in the legend.
*why*: it is the only image in the project where the derived and the recovered
appear together, so it is the picture of 0.103177 and of the instrument's error
at once; it shows the non-nesting directly, X_lu reaching above x_2 = 1 where
X_cw does not go and X_cw filling x_2 < 4/5 where X_lu does not; and it is drawn
on random search, the instrument that carries the claim. **memoria and
presentation.** it is the one figure the presentation cannot do without.

**f2. the epsilon dependence. g2 must draw it.**
both directions of the headline pair against eps, one panel per benchmark, median
with the interquartile range as the error bar, from
`results/tier1/table_2_measured_eps_*.csv` decision block at delta 0.0 and
n_evals 5000, with the cardinalities |X_lu| and |X_cw| on a secondary axis or in
the panel caption.
*why*: it is the only figure that carries the tier 1 result at all, and the
existing tier 1 decision-space figures do not — they project thirty or twelve
variables onto two and show a scatter. it must show both directions, because
showing only cov(lu→cw) invites the misreading section 3.1 corrects. plotting the
interquartile range makes section 5.1's four failing cells visible instead of
argued. **memoria and presentation.**

**f3. the within-phi discrimination. g2 must draw it.**
m-2's median overhang by image column on dtlz2 under phi_cw at one level, twenty
seeds, with the free-set size printed under each column, from
`results/tier1/overhang_summary.csv`.
*why*: it is the picture of the project's second result and it is the sharpest
single frame in the whole run — four bars near 0.8 on the columns whose free set
is eleven variables and one bar at exactly 0.000000 on the column whose free set
is {x_2}, all under one phi, one sample and one seed set. it removes every
explanation that turns on the order being different. **memoria only**;
docs/plan_after_meeting.md section a1 keeps the mechanism out of the presentation.

not recommended. the tier 1 decision-space figures, which are two-coordinate
projections of a thirty- or twelve-dimensional set with no derived region behind
them and no legible geometry in them. the rank-1 saturation curves, which are a
memoria paragraph and which a1's disposition table keeps out of the presentation.
and any figure placing e1's and e2's objective blocks together, section 6.2.


## 10. what e3 leaves open, and for whom

    x-02, the 1/8 constant on p1 at twenty seeds. e2 ran tier 1 only and
    results/tier1/overhang_summary.csv carries zdt1 and dtlz2 and no p1 row, so
    the measurement x-02 registers does not exist and e3 makes no run. it needs
    twenty seeds of random search on p1 at budget 5000 under example 2.4, column
    3, which is the cheapest thing in the project. it is not a blocker for g1.

    s-11, the containment. unanswered; section 6.4 records that the headline does
    not depend on it.

    section 4.4's question, whether the width driver's alignment with a centre is
    what changes the geometry between p1 and the benchmarks. one variant run
    would decide it. out of scope before 25 september and worth stating in the
    memoria's future work, because section 7.1's claim form makes it the natural
    next measurement.

    what f1 returns. clause c5 stands or is withdrawn on it, and the fallback is
    already written.
