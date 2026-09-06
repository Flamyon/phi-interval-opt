# part 1, closed: what was asked, what was done, what was found

session part1-close, 2026-09-05. no experiment, no module, no re-run and **no new
claim and no new number**: every figure below is read out of a file
`experiments/run_tier0.py` or `experiments/run_tier1.py` wrote, or out of
docs/part1/e3_synthesis.md, which read those files, and the artefact is named beside
it. where a number is derived from two such numbers by an identity stated
elsewhere in the project, it says so and gives the identity.

who this is for. the supervisors, and whoever drafts the memoria. **it is the
document g1 lifts part 1 from**, and it is written to be complete enough that g1
opens nothing else for the results. where this document and an e1, e2 or e3
artefact could differ, the artefact wins.

docs/part1/e3_synthesis.md is **the working synthesis**: it carries the full
reasoning, every intermediate step, the alternatives weighed and rejected, and
the section-by-section argument that got from e1's and e2's artefacts to part 1's
answer. this document is **the settled record**: the same
answer with the reasoning compressed to what a reader needs to act on it, plus
what e3 does not have — the question in the supervisors' own terms, the arc, the
methodological results, and what part 1 hands to part 2 with its five-criterion
gate. both documents check the same four prohibitions, each against its own text.
**this one is canonical for part 1 and it is the one g1 lifts from**; e3 is where
to go for why a conclusion holds, and it is not superseded. neither restates the
other's numbers independently: every figure here is read out of an e1 or e2
artefact or out of e3, and named. if the two ever disagree, the artefact settles
it.

what it may not do, and each is checked at the end. it may not rank phi,
CONTEXT.md section 2. it may not claim anything from the containment while s-11
is unanswered, docs/part1/a_close_containment.md section 6. it may not quote a slice
fraction as a quantity, r-22. and it may not interpret a benchmark number without
the instrument's error beside it.

where the detail is, so this document does not become a second copy of it:

    docs/part1/e1_tier0_run.md           the tier 0 run and the exact table
    docs/part1/e2_tier1_results.md       the tier 1 run
    docs/part1/e3_synthesis.md           the synthesis, and part 1's answer
    docs/part1/phase_a_summary.md        formulation, closed out
    docs/part1/phase_b_summary.md        ground truth, closed out
    docs/part1/phase_c_summary.md        solvers and the gate, closed out
    docs/part1/b1_phi_efficient_sets.md  the derivation, section 2.4 the closed
                                         forms
    docs/part1/a_close_containment.md    the containment criterion and s-11
    docs/plan_after_meeting.md           the claim and the path, section a
    PROGRESS.md                          the open rows and the registered
                                         predictions


## 1. the question, and the answer

### 1.1 the question, in the supervisors' own terms

slide 17 of `papers/Presentacion_optimizacion_intervalar.txt`, "Doble enfoque de
la propuesta", sets the goal:

> Meta: comparar cómo cambian las soluciones aproximadas al variar φ, sin buscar
> un algoritmo nuevo, sino comprender la interacción orden–algoritmo.

and splits the work into an *enfoque teórico* — revisión del marco de relaciones
⪯φ; transformación de problemas intervalares en multiobjetivo real (extremos,
centro-radio, anchura); estudio de condiciones de φ-eficiencia — and an *enfoque
computacional* — búsqueda aleatoria (random search) como referencia base;
algoritmos evolutivos multiobjetivo (tipo NSGA-II); inteligencia de enjambre (PSO
multiobjetivo).

slide 18, "Metodología propuesta", gives five steps: formular el problema
intervalar (o difuso); fijar automorfismo φ (orden ⪯φ); transformar en problema
multiobjetivo real; resolver con búsqueda aleatoria / evolutivo / enjambre;
analizar el frente obtenido y su sensibilidad a φ.

slide 19, "Ejemplos y benchmarks previstos", gives the problems: problemas
sencillos de una o dos variables, con imprecisión artificial en los coeficientes
o en la función objetivo; adaptación intervalar de benchmarks multiobjetivo
clásicos (familias ZDT, DTLZ), introduciendo incertidumbre acotada ±ε en los
objetivos; implementación reproducible en Python, comparando distintos φ sobre el
mismo problema base.

so the question part 1 was set is the fifth step of slide 18 read against the
goal of slide 17: **how much does the answer change when only the order changes**,
measured on slide 19's two tiers of problem, with slide 17's three solvers, and
without proposing an algorithm.

### 1.2 the answer

on the one problem where the phi-efficient sets are known in closed form, two of
[1]'s own named orders — example 2.2 and example 2.4 — share 0.103177 of their
union, 0.605290 of X_lu lies outside X_cw and 0.877429 of X_cw lies outside X_lu,
in exact lebesgue measure with no sampling and no solver in the number;
the same statistics measured on recovered sets at thirty and at twelve variables
reproduce it in the asymmetric form section 3.1 states, between 63 and 91 per cent of X_cw
lying outside X_lu at every imprecision level on both benchmarks, with a
seed spread of one to four per cent of that figure; and because the same
instrument, on the same problem and at the same budget, was measured to return
1.81 times the exact shared fraction, every measured agreement is an upper bound
and the two orders share **less** at thirty and twelve variables than the tables
print. the choice of order relation is therefore not a modelling detail on any of
the three problems — subject to one condition on the uncertainty model that the
project measured rather than assumed and that section 7 states as part of the
claim.


## 2. what was built, in the order of the arc

five stages. no implementation detail; each names its close-out document.

**read and verify.** [1] was read as a verification pass and not as a summary:
its claims about the framework were checked line by line against the printed page,
giving v-01 to v-23 with an equation or example number and a page for each — the
automorphism class and its admissibility condition, the three named examples with
their exact coefficients and the convexity notion each coincides with, definition
3.1's three solution concepts, theorems 3.1 to 3.3 with their hypotheses, and
examples 3.8 and 3.9 with their numbered statements and condition (15). a fourth
named example exists, example 2.1, carrying four different coefficient pairs and
no convexity notion. section 5 of [1] was read
once and deliberately, because it contains proposition 5.1, which relates two of
the three phi in the fuzzy setting; the interval side was searched exhaustively
and contains no analogue. docs/part1/phase_a_summary.md, docs/part1/a0_framework.md.

**construct a calibration problem.** the literal reading of slide 19 is
degenerate and the project measured that before building anything on it: with a
constant half-width the three phi and the crisp order return the identical index
set, and so does any half-width that is an exact function of the centre, which is
why imprecision in the coefficients was rejected as well. the half-width must
therefore be driven by a decision variable the centre does not resolve. that rule
produced p1, two variables and two interval objectives, with each objective's
half-width driven by the *other* objective's variable, and it produced the two
tier 1 forms; it also produced the design rule that all image coordinates are
convex under all three phi exactly when c − r and r are both convex, which is what
makes the next stage possible. docs/part1/a1_uncertainty_model.md, docs/part1/phase_a_summary.md.

**derive its answer exactly.** on p1 the published conditions of [1] close under
all three phi: theorem 3.3 gives phi-convexity globally, the regularity criterion
is trivial, and condition (15) of example 3.9 is a diagonal linear system, so the
weight-parameterised stationarity map is an explicit rational function with no
root-finding anywhere. eliminating the weights gives three closed-form regions —
X_lu bounded by two conic arcs, X_ls by one, X_cw exactly the closed unit square
less one open edge — every one of them strictly interior to the box. the three
descriptions were verified in exact rational arithmetic in both directions, 12341
weight vectors forward with none landing outside the stated region and 301 region
points inverted with none lacking a witness weight. that is what makes a coverage
question askable rather than merely plottable. docs/part1/b1_phi_efficient_sets.md
sections 2.4 and 2.6, docs/part1/phase_b_summary.md.

**validate the instrument.** three solvers on one contract — random search as
slide 17's *referencia base*, pymoo's NSGA-II and MOPSO_CD used as published —
and a gate that runs all three on p1 under all three phi over five seeds and both
settings of the singular-segment flag, ninety measurements, against the derived
sets. two directions are asserted. **no solver returns a point that beats the
derivation anywhere, ninety of ninety**, which is the direction that would have
indicted the derivation or its encoding. the reverse direction fails in twelve,
every one of them NSGA-II, and that failure is a finding and not a defect,
section 5.4. e1 then did the thing the whole arc was built for: it measured the
same pair statistics on recovered sets at the same budget, so that the gap between
the derived value and the measured value is a number and not a worry.
docs/part1/phase_c_summary.md, docs/part1/e1_tier0_run.md.

**extend to benchmarks.** zdt1 at thirty variables and dtlz2 at twelve, in
interval form with each objective driving its own half-width, across five
imprecision levels, all three solvers, all three phi, five seeds, at budget 5000
with one convergence check per problem at 20000: 108 configurations and 540 runs
for e2, after e1's 36 configurations and 180 runs. e3 then put e1's exact numbers
and e2's measured ones on one page, which is the comparison neither run made and
is the claim. docs/part1/e2_tier1_results.md, docs/part1/e3_synthesis.md.


## 3. the result

### 3.1 the headline pair, exact and measured

the pair throughout is **example 2.2 against example 2.4**, phi_lu against
phi_cw. it is the only one of the three pairs nested in neither direction, so it
is the only one where nothing is fixed before a solver runs; section 4.1 says why
the other two are checks. all rows are random search's one filtered sample —
one uniform sample of the box, evaluated once, filtered under each phi in turn, so
the three sets differ only through the order — at delta zero, budget 5000, five
seeds. delta zero is exact here and not a limit, d-08: the three sets of one
comparison are index sets over one array, so two decision vectors are the same
point bitwise or they are two points.

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

provenance. p1's exact row is `results/tier0/exact_regions_p1.csv`, keys
coverage_a_in_b, coverage_b_in_a, overlap_union_share and area on the (lu, cw)
pair, the areas being lebesgue measures of the closed-form regions of
docs/part1/b1_phi_efficient_sets.md section 2.4. p1's measured row is
`results/tier0/table_2_measured.csv`, decision block, delta 0.0, n_evals 5000;
its jaccard is the one derived number in the table, from e1's dice 0.315349 by the
identity jaccard = dice / (2 − dice) that e2 section 5 states and uses throughout.
the benchmark coverages are `results/tier1/table_2_measured_eps_*.csv`, decision
block, delta 0.0, n_evals 5000; the benchmark jaccards are
`results/tier1/overlap_conventions.csv`, key jaccard_median, computed by the same
identity. coverage leads and any overlap is named, d-09.

**the presentation number is the reverse direction**, one minus cov(cw→lu):

> **between 63 and 91 per cent of X_cw lies outside X_lu, at every imprecision
> level, on both benchmarks** — 0.628240 to 0.912000 across the eight cells —
> with an across-seed interquartile range of one to four per cent of that figure.

it is the direction that passes the seed-spread criterion of docs/part1/e3_synthesis.md
section 5.1 in all eight of its cells, ratios IQR / (1 − median) of 0.007 to
0.037, and it is therefore the sentence the memoria and the presentation carry.

**the other direction is reported and its instability is named.** cov(lu→cw) falls
monotonically from 0.846154 to 0.545455 on zdt1 and from 0.897541 to 0.684211 on
dtlz2, which is a real and predicted movement, section 3.3; but four of its eight
cells fail the same criterion — zdt1 at eps 0.05, 0.10 and 0.25 and dtlz2 at eps
0.05 — and every failure is a cell whose median is near 1.0 on a small X_lu, 26,
36 and 53 points on zdt1. the cell that fails hardest, zdt1 at eps 0.05, has an
interquartile range as wide as its whole distance from 1.0. so the sentence "the
coverage of X_lu in X_cw is 0.85 at thirty variables" is **not available**, and
the loss is stated rather than absorbed. docs/part1/e3_synthesis.md section 5.1, from
`results/tier1/table_2_measured_eps_*.csv` columns median and iqr.

**one statistic is stable across the dimension change and is uncalibrated.** the
symmetric hausdorff distance in decision space, in units of the box diameter, is
0.339524 on p1, 0.291658 on dtlz2 at eps 0.10 and 0.386729 on zdt1 at eps 0.10 for
the headline pair. dividing by the box diameter removes the only quantity that
changed between the three problems. two caveats, and they are not small: a
hausdorff distance is a maximum and is driven by the single worst-separated point,
and `results/tier0/exact_regions_p1.csv` carries **no exact hausdorff**, so this
statistic was never calibrated and section 3.2's error does not cover it. it is a
scale-free corroboration and not a second headline number.
docs/part1/e3_synthesis.md section 4.3.

**the shape differs where the magnitude does not.** on p1 the two sets are
genuinely non-nested — both coverages strictly between zero and one, X_lu reaching
above x_2 = 1 where X_cw does not go and X_cw filling x_2 < 4/5 where X_lu does
not, each set holding a region the other cannot reach. on both benchmarks X_lu
sits largely inside a much larger X_cw. the jaccard column alone would say the two
situations are alike; they are not, and the decision-relevant reading differs.
docs/part1/e3_synthesis.md sections 4.1 and 4.2.

### 3.2 the instrument's error, measured once, and what it licenses

`results/tier0/instrument_error_p1.csv` is the only file in the project comparing
a derived quantity with the same quantity measured. on the headline pair at budget
5000 the relative error is **+0.408456** on cov(lu→cw), **+0.810049** on cov(cw→lu)
and **+0.685866** on the dice overlap; at 20000 it is +0.277334, +0.486096 and
+0.421450. in the jaccard convention the measurement is 0.187190 against a true
0.103177 at 5000 and 0.153329 at 20000, a factor of **1.81** and then 1.49.
every row is positive and every row shrinks when the budget is quadrupled.
`results/tier1/inherited_instrument_error.csv` is the relative column, written by
e2 reading tier 0's artefacts back.

**so a measured coverage is an upper bound on true sharing and a lower bound on
how far two orders differ.**

**the sign of that bias is measured to transfer and is not assumed.** the
objection is that the bias was measured at two variables and nothing licenses
carrying it to thirty. that objection is right about the magnitude and answerable
about the sign: if the bias were a finite-sample artefact rather than a property
of p1, the benchmarks would have to show the same budget response with no exact
value to fall toward, and they do. quadrupling the budget lowers all three
statistics on p1, dtlz2 and zdt1 — nine of nine — by 9 to 23 per cent against p1's
9 to 18, and on p1 that direction is known to be toward the truth.
`results/tier0/table_2_measured.csv` and
`results/tier1/table_2_measured_eps_0.1.csv`, decision block, delta 0.0, at both
n_evals. **the magnitude does not transfer and no correction factor is applied to
any benchmark number anywhere.** docs/part1/e3_synthesis.md sections 2.1 and 2.2.

what may not be said, and g1 must not: that the benchmark jaccard is "about 0.10
as on p1", the two not being the same kind of number and only p1's being exact;
and that the true benchmark jaccard is 0.087 / 1.81, the factor being p1's alone.

### 3.3 the epsilon dependence, and which quantity moves

the coverage of X_lu in X_cw falls monotonically as the imprecision grows and the
jaccard rises. the two are not in conflict, and **the cardinality column in the
same table is the whole explanation**: |X_cw| is 257 on zdt1 and 1813 on dtlz2 at
*every* positive level, while |X_lu| grows 26 → 36 → 53 → 68 and 278 → 351 → 575 →
980. the entire eps dependence of the headline pair is X_lu's.

that |X_cw| is constant is structural and not an artefact. under example 2.4 the
image is (c_1, r_1, ..., c_m, r_m) and eps enters only as a positive scalar
multiple of the r_i; multiplying a column by a positive constant is a strictly
increasing per-column relabelling, which leaves the pareto relation on R^2m
unchanged, so the phi_cw non-dominated set of a given sample is the same index set
at every eps > 0. the cardinality column confirms it exactly at all four positive
levels. docs/part1/e3_synthesis.md section 3.1.

**the direction was predicted before either run**, in docs/part1/a1_uncertainty_model.md
part 4, where the five levels were placed: phi_lu is the sensitive one and its
efficient set grows with eps on both benchmarks; phi_cw is stable. it is confirmed
here on the run's own cardinality column and not on a slice fraction, r-22. what
was *not* predicted anywhere is that coverage and jaccard would move in opposite
directions; that follows from the invariance above and is e3's.

the honest sentence, and it is the one g1 should carry: *as the imprecision grows,
phi_lu's efficient set grows into and past phi_cw's, which is fixed; the fraction
of phi_lu's answer that phi_cw would reject rises from 0.15 to 0.45 on zdt1 and
from 0.10 to 0.32 on dtlz2.*

### 3.4 the second result: the protected-minimiser condition, and what it is a fact about

x-01, registered in PROGRESS.md section 9 before either run, predicts that the
member of a finite candidate set minimising an image column g_k strictly is
dominated by nothing in that set, so where g_k is a function of a strict subset of
the decision variables its remaining coordinates are unconstrained by that
protection; the effect is present exactly where some column has a non-empty free
set F_k and the phi-efficient set's projection onto F_k is a proper subset of the
box's, of positive co-measure.

**it is confirmed on dtlz2, and by a stronger comparison than the one it asked
for.** `results/tier1/overhang_summary.csv`, twenty seeds, budget 5000, both
reported structures agreeing on every row: under phi_cw, on one sample and one seed
set, column 4 has a free set of {x_2} and measures a median overhang of **exactly
0.000000 with an interquartile range of 0.000000** at all five levels, while
columns 1, 3 and 5 have eleven-variable free sets and measure **0.737044 to
0.842968**, with standard errors over the twenty seeds of 0.021 to 0.033 on the
positive columns and 0.000000 on column 4. the condition therefore discriminates
**column by column inside one phi**, which removes every explanation that turns on
the order being different. `results/tier1/free_sets.csv` confirms the free sets at
the run rather than asserting them.

> **and here is what that result is a fact about, stated so that no reader
> generalises it wrongly.** the mechanism behind column 4's exact zero is that
> **the efficient set's projection onto x_2 is the whole box, because x_1 and x_2
> are the two parameters of dtlz2's own front**; a protected member's x_2
> coordinate is therefore inside the projection whatever it is, and the overhang
> is zero by construction. that is a fact about **dtlz2's structure**, not about
> example 2.2. x-01's own registered wording says as much — the reason it gives
> for the absence under phi_lu is not that phi_lu's columns all depend on every
> variable, two of them do not, but that the variable they omit is one the
> efficient set does not constrain — and it is repeated here because the
> tabulated form invites the wrong reading. **the sentence "phi_cw has protected
> minimisers and phi_lu does not" must not be written.** on dtlz2 it happens that
> phi_cw's width columns are the ones with small free sets and phi_lu's only
> free-set columns are the two that omit x_2; on zdt1, under a5-b's forms, every
> phi has a non-empty free set of measure-zero projection and the condition says
> *present* under all three. the condition is a property of a column, and the
> orders enter only by determining which columns exist.

the zdt1 arm of x-01 is in section 5.3: it became untestable when a5-b changed the
problem, and it could not have discriminated in any case. m-1, the second
registered measurement, is withdrawn as an instrument and is not revived,
re-thresholded or reinterpreted anywhere; section 6.4 records why that is itself a
result.

### 3.5 the one table in the results a reader could misread, and the decision taken

**e1's tier 0 objective block answers no solver question, and it must carry a
caption saying so.** its rows are at full cardinality — 100 for NSGA-II, 200 for
MOPSO and 608 to 2220 for random search, 1528 under phi_cw on p1 —
`results/tier0/table_3_solvers.csv`. r-16 measured the cardinality effect on one
fixed front at a factor of 6.5 in igd and 10.3 per cent in hypervolume, which is
**larger than the differences a solver comparison would be trying to detect**.
random search leads that table on every metric on p1 — hypervolume 4.107893
against 4.065803 and 4.019418 under phi_cw, igd 0.020972 against 0.065101 and
0.109468 — and that is its row count and not its search.

two courses were available: recompute the block at a common cardinality, or label
the table. **the decision taken here is to label it, and the reason is that
recomputation is a run and part1-close makes none.** the label is binding on g1
and on g3:

> e1's tier 0 objective block is reported at each solver's full cardinality. it is
> a record of what each solver returned and **not a comparison between solvers**;
> r-16's cardinality effect exceeds the differences it displays, and random search
> leading it is its row count. no ranking of solvers may be read from it.

it is not written into docs/part1/e1_tier0_run.md, because that document is generated and
re-running the script must reproduce it exactly; the label lives here, where g1
reads it, and it travels with the table.

e2's objective block is different and is comparable within a row: it is truncated
to the common cardinality of each comparison, 100 on dtlz2 and 15 to 66 on zdt1
depending on the level, r-16 and CONTEXT.md section 10 d1,
`results/tier1/table_3_solvers_eps_*.csv`. at that cardinality NSGA-II has the
largest hypervolume in five of the six (problem, phi) cells at eps 0.10 and MOPSO
is level with it in the sixth; random search is last in all six. **the two
objective blocks are not comparable with each other and may never be placed side
by side**, in the memoria or in the presentation. docs/part1/e3_synthesis.md section 6.2.


## 4. the structural findings

three of them, compressed into one section because a short applied memoria cannot
give each a section of its own, d-07. all three are guards on how the claim may be
phrased, which is why they sit in the body and before the reader has finished with
the claim rather than in an appendix after it.

### 4.1 the containment, and why it makes one pair the informative one

for every feasible set and every objective, the non-dominated sets under example
2.2 and example 2.4 are both contained in the one under example 2.3:
ND_lu ⊆ ND_ls and ND_cw ⊆ ND_ls. both follow from one criterion on the map between
two automorphisms — if M = phi_B phi_A^-1 is entrywise non-negative and invertible
then phi_A-dominance implies phi_B-dominance — and exactly two of the six maps
between the three phi qualify, both out of phi_ls. neither map between phi_lu and
phi_cw is non-negative, so **those two are nested in neither direction and nothing
relates them.** docs/part1/a_close_containment.md sections 1 and 2, reproduced
independently from b1's closed forms in docs/part1/b1_phi_efficient_sets.md section 5.

the consequence, and it is the reason the study has one headline pair rather than
an average over three: on the (lu, ls) and (ls, cw) pairs **one direction of every
coverage and overlap statistic is fixed before a solver runs**, and the runs show
it exactly — cov(lu→ls) and cov(cw→ls) are 1.000000 with an interquartile range of
0.000000 at every level, on both benchmarks, at both budgets, at both deltas and
on p1. a difference measured there is in part a theorem, and reporting it as
evidence of order sensitivity would be reporting the criterion.

**no claim is made from any of it while s-11 is unanswered.** the containment is
used only to *withhold* two pairs from the evidence, which is the conservative
direction: if the supervisors refute the criterion, the instruction is removed,
all three pairs are reported alike, and the headline number does not move, because
it never came from those pairs. s-11 asks three things — is the criterion correct,
are both containments correct, and is any of it published — and the third is what
decides whether the memoria cites a known result or records a small original
observation. docs/part1/a_close_containment.md section 6.

### 4.2 v-56, the exact linear relations, which carry no problem parameter

each phi is a constant linear map of the endpoint pair, so the three images of any
decision set are constant linear images of one another. writing the four image
columns of p1 under each phi:

    g_lu = A g_cw    A = [[1,-1,0,0],[1,1,0,0],[0,0,1,-1],[0,0,1,1]]
    g_ls = B g_cw    B = [[1,-1,0,0],[0,2,0,0],[0,0,1,-1],[0,0,0,2]]

**A^T A = 2 I**, so A is √2 times an orthogonal matrix, all four singular values
are √2 and its condition number is exactly 1: the phi_lu image is a rotation and a
uniform scaling of the phi_cw image, and examples 2.2 and 2.4 of [1] present the
same geometric object in two alignments. **B is not a similarity**: B^T B is block
diagonal with two copies of [[1,−1],[−1,5]], eigenvalues 3 ± √5, so B's singular
values are 2.288246 and 0.874032, each twice, and its condition number is exactly
(1 + √5)^2 / 4 = 2.618034, the golden ratio squared; the map from the phi_ls image
to the phi_lu image has singular values exactly φ and 1/φ. verified to 0.000e+00
on 500 random points of the box and on all three region samples.
docs/part1/c3_validation.md section 5.5.

**A and B contain no parameter of p1** — no rho, no delta, no box, no objective.
they are built from the coefficient pairs of examples 2.2, 2.3 and 2.4 alone, so
they hold for every interval problem in the framework under these three phi. this
is the one part of the project's findings that is about [1] rather than about this
study's problems, and it is load-bearing negatively: **no sentence of the form
"the phi_lu map distorts more than the phi_cw map" can be true**, since pointwise
the two are the same map up to a similarity, and any measurement appearing to show
one is measuring the region it was averaged over.

what it does not say: nothing about the solution sets. dominance is not preserved
by an arbitrary invertible linear map, only by an entrywise non-negative one,
which is section 4.1's separate criterion; A and B both have negative entries.

### 4.3 the loss of selection pressure under the 2m transformation

definition 2.1 of [1] takes m interval objectives to 2m real ones, so p1 and p0
are 4-objective real problems, zdt1_interval is 4 and dtlz2_interval is 6. the
non-dominated fraction of a sample rises with the number of objectives, and at 2m
it rises far enough that a dominance-based survival operator has nothing left to
discriminate with.

measured, `results/tier1/rank_one_summary.csv`, read through a pymoo callback that
leaves the front bit-identical: **every one of NSGA-II's twenty-four
positive-imprecision configurations — both benchmarks, all three phi, all four
positive levels — saturates rank 1 in every seed.** the only three that do not are
the crisp baseline on zdt1. dtlz2 15 of 15, zdt1 12 of 15; MOPSO 12 of 15 and 5 of
15, with zdt1 under phi_cw the single (problem, solver, phi) combination that keeps
dominance pressure at every level. and the generation at which it happens is
ordered and monotone, out of 50. NSGA-II's median first saturated generation
across eps 0.05, 0.10, 0.25 and 0.50: on dtlz2, 2 at every level under phi_cw and
under phi_ls, and 6, 4, 3, 2 under phi_lu; on zdt1, 5 at every level under phi_cw,
4, 4, 4, 3 under phi_ls, and 23, 17, 15, 13 under phi_lu. **phi_lu retains dominance
pressure longest under both population solvers on both problems, and how long
falls monotonically as the imprecision rises** — c3-d's ordering reproduced on
a5-b's new forms and extended from p1 to both benchmarks.

what it means for reading those fronts: from the saturating generation onwards
dominance selects nothing and crowding distance selects everything, so the front
is a **spread** result and not a **convergence** result. and at tier 1 there is no
measurement of convergence at all: src/reference_fronts.py derives a reference
front for p1 alone, so no igd exists on either benchmark and every objective-space
row carries a reference size of zero.

**this is the empirical form of the objection [7] raises against transformation
methods**, stated by this project as a measurement on its own problems rather than
as a citation. it is a statement about what 2m objectives do to any
dominance-based selection and it is not a statement that any solver is
misconfigured. together with section 5.2 it is the memoria's answer to [7].
docs/part1/c3_validation.md section 5.1, docs/part1/e2_tier1_results.md section 8,
docs/part1/e3_synthesis.md section 6.1.


## 5. what could not be settled

four items, stated as such. none of them is apologised for and none of them is
patched; in three of the four the cost of not knowing was measured rather than
argued about.

### 5.1 the singular weight segments: the published conditions give no verdict

on the weight rays putting all mass on one width coordinate, the scalarised
problem has a line of minimisers rather than one, so example 3.8 statement 3 does
not apply; example 3.8 statement 2 and example 3.9 statement 3 require every
weight strictly positive, which those rays do not have; and no regular weight
reaches the interior of the segments. **the published conditions therefore give
weak optimality there and no optimality verdict either way**, under phi_ls and
phi_cw; phi_lu has no singular ray at all. docs/part1/b1_phi_efficient_sets.md
section 2.6.

CONTEXT.md section 10 b1's stopping rule is that a derivation which does not close
with the published results as they stand stops and goes to the research chat, and
is not patched. it was honoured. `efficient_set` and `reference_front` take
`include_singular_segments` with no default, so a caller must state which of the
two reference objects it wants and the value goes in every table beside the seed
and the point count. **the cost was priced**: with the region sample held fixed and
the segment added on top, the igd of a fixed test front moves by −0.63 to +5.36 per
cent at 1000 reference points and by −0.11 to +1.35 at 20000, so the choice can
flip a comparison already inside a few per cent. it is s-12 to the supervisors and
r-12 in PROGRESS.md, and it is open.

### 5.2 half of NSGA-II's coverage deficit has no mechanism

the finding, at its established scope — p1 at two variables, with a
full-dimensional efficient set and a closed-form region to measure against, one
solver, one cardinality, five seeds. **for a full-dimensional efficient set,
NSGA-II's decision-space coverage is worse than uniform random sampling of that
set at equal cardinality, under phi_ls and phi_cw and not under phi_lu.** its fill
distance sits at the 85th to 99th percentile of 1000 uniform 100-point draws under
the two, worse than the uniform mean in all ten measurements, and at the 33rd to
60th under phi_lu, which is where a uniform draw itself sits. it returns exactly
100 rows, so no cardinality correction is needed. this is what the twelve gate
failures are. docs/part1/c3_validation.md section 5.

**about half of it is not about NSGA-II**, and the halving is by control and not
by argument: random search, whose sample is a pure function of the box, the budget
and the seed, carries +0.243 of the +0.483 swing from phi_lu to phi_ls and +0.244
of the +0.485 to phi_cw, in units of the uniform mean at k = 100. that half is the
regions' shape acting on the comparator — |X_lu| = 0.310533, |X_ls| = 1.513401,
|X_cw| = 1, and a uniform draw covers the thin curved X_lu about 40 per cent worse
for its area than the two fat regions.

**the other half is NSGA-II's own and has no mechanism after five exclusions**,
each by direct measurement: rank-1 saturation, refuted because it fires under
every phi and a mechanism present under all three cannot produce a result that
appears under two; effective cardinality, which buys 2 to 11 percentile points of
a gap of 50 and leaves all ten failing measurements at or above the 74th; the
pullback, where in the normalised image space NSGA-II is not worse than a uniform
draw at the thing it optimises under either failing phi; map anisotropy, where
phi_lu is the anisotropic one, which is the reverse of the ordering a distortion
story needs, and which v-56 then makes an artefact of averaging over two different
regions; and region size, excluded by the phi-neutral control above. **the
residual half is recorded as unexplained and no mechanism is offered for it.**

what it does not say, and g1 must not let it be read as saying: not that NSGA-II
fails to converge — no solver returns a point beating the derivation anywhere,
ninety of ninety — and not that NSGA-II covers worse *because of* the phi, which
the control forbids. one consequence for the project's own instruments: a spread
statistic is computed in the objective space where NSGA-II sorts and this finding
is in the decision space where the result lives, so **a spread statistic is never
read as decision-space coverage**. and this is why the headline is on random
search: slide 17's *referencia base* is the instrument carrying the study's main
result rather than a baseline to beat.

### 5.3 x-01's zdt1 clause became untestable when a5-b changed the problem

the clause was registered against a5's forms, where both zdt1 half-widths read
x_30 and the domination argument of docs/plan_after_meeting.md section f3 gives
X_phi ⊆ {x_2 = … = x_29 = 0} under every phi. **a5-b moved r_2 onto x_29**, so x_29
now drives a width column, the argument no longer applies to it, and re-run on
a5-b's forms it pins one variable fewer, {x_2 = … = x_28 = 0}. e2 reports the
overhang against both structures and names them,
`results/tier1/overhang_summary.csv` column *structure*; the registered structure
is a proper subset of the correct one, so the registered distance is to a set the
efficient points need not lie in and comes out systematically the larger — at eps
0.10 under phi_lu, 3.050320 against 3.007057 on column 0 and 3.027359 against
2.934039 on column 1.

> **verdict: untestable on the problem that was run.** not scored confirmed,
> because a registered prediction is about a named object and the object changed
> after registration. not scored refuted, because nothing measured contradicts it:
> under either structure the median overhang is strictly positive on zdt1 under
> all three phi, and a5-b's structure is a *superset* of the true efficient set,
> so the distance to it is a lower bound and positivity holds a fortiori.

**and zdt1 could not have decided it either way.** under a5-b's forms every phi has
a non-empty free set of measure-zero projection, so x-01's condition says *present*
under all three and zdt1 can supply a "present" observation and never a
discriminating one. the mechanism's evidence is dtlz2's and not zdt1's, section
3.4. docs/part1/e3_synthesis.md section 5.2.

**x-02 is open and that is a fact about which run happened.** it re-registers the
1/8 overhang constant on p1 under example 2.4 at twenty seeds instead of five; e2
ran tier 1 only, so `results/tier1/overhang_summary.csv` carries no p1 row and no
artefact of e1 or e2 decides it. the standing five-seed reading is a mean of
0.162794 with a standard error of 0.094140 against a predicted 0.125, from
`results/tier0/registered_measurements_summary.csv`, and it is **not a
confirmation**: 0.125 lies inside that spread and so does zero. what would close
it is twenty seeds of random search on p1 at budget 5000 under example 2.4, column
3 — the same estimator and the same code path e1 already ran, and the cheapest
thing in the project. it is not on g1's critical path.

### 5.4 the twelve strict xfails, and what they encode

the gate's reverse direction — that every part of the derived set is reached by
the solver, measured as the reverse hausdorff distance in decision space against a
tolerance fixed before the study ran, the 0.95 quantile of the fill distance of a
100-point uniform draw of the derived region — fails in twelve of ninety
measurements. every one is NSGA-II: three seeds under phi_ls (11, 13, 14) and three
under phi_cw (12, 13, 14), at both settings of the singular-segment flag, six
configurations times two settings. the margins are small, the worst gap exceeding
the tolerance by 0.005 to 0.039 in a box of side 2.

**they are left failing on purpose.** exempting the one solver the gate catches
converts the gate into a report at the moment it does its job, and would do so on
the strength of the result; a non-strict xfail makes the suite green while the
assertion fails. what is done instead is `xfail(strict=True)` pinned to those twelve parameter
sets: **the assertion is unchanged and still runs
on all ninety**, a thirteenth failure is a plain failure, and an unexpected pass is
an error. so the twelve encode the finding of section 5.2 and encode that it has
not moved. the suite is 1074 tests, 1062 passing and 12 xfailed.
docs/part1/c3_validation.md sections 4.1 and 5, PROGRESS.md.

what the twelve do *not* say: that a solver failed to recover the set. the
derivation, its encoding and all three solvers agree about where the efficient set
is; two of the three cover it to within the derivation's own resolution and the
third does not.


## 6. the methodological results

four of them. they are about method and they are results: each one is a place
where the study would have measured nothing, or measured the wrong thing, and the
project found out by measuring rather than by argument.

### 6.1 the constant-width degeneracy, which would have made the study vacuous

slide 19's literal tier 1 prescription, "introduciendo incertidumbre acotada ±ε en
los objetivos", is a constant half-width, and under it **the crisp non-dominated
set and the three phi non-dominated sets are not merely equal in size but
identical as index sets, all four of them**, on zdt1 at thirty variables and dtlz2
at twelve, at eps ∈ {0.05, 0.5}, over 5000 uniform points. the reason is
structural: with the width constant, the image of the feasible set in the
centre-width plane is a curve, every injective phi maps a curve to a monotone
curve, and the three orders coincide.

it is not confined to a constant width. **a half-width that is any exact function
of the centre does the same**: proportional imprecision f → [f(1−ε), f(1+ε)] on
zdt1 gives width spans of 0.84 and 2.19, nowhere near constant, with correlation
+1.0000 and all four index sets identical. that is why imprecision in the
coefficients was rejected: any objective that is a monomial in an imprecise
coefficient has a half-width that is an exact linear function of its centre, and
slide 19's own tier 0 problems, "problemas sencillos de una o dos variables", are
exactly where objectives are monomials — measured on zdt1 with f_1 = c_1 x_1 and
c_1 ∈ [1−d, 1+d], correlation +1.0000 and phi_cw returning the crisp non-dominated
set exactly, at d = 0.10 and 0.25.

**had this not been measured first, every table in part 1 would have been a table
of ones.** the consequence is the project's standing rule — the half-width must be
driven by a decision variable the centre does not resolve — and the proportional
construction is kept as a negative control, asserted as a test.
docs/part1/a1_uncertainty_model.md part 1, docs/part1/phase_a_summary.md, v-30 to v-32.

### 6.2 the uniform-sample separation check is no evidence

the natural half-width for zdt1 is ε·x_n, and it passes every check the project's
own step-1 prescription asks for: on a uniform sample of the thirty-dimensional
box its width span is 0.4999, its correlation with the centre is −0.0111 and
+0.1027, its within-bin spread is 0.9943 and 0.9932 of the span, and the three phi
separate. by the prescribed check it is a good construction.

it is not. restricted to the slice where zdt1's efficient set actually lives, at
ε = 0.25, **phi_cw's efficient set on the slice is the crisp efficient set
exactly** and phi_lu's and phi_ls's are the whole slice. the uniform sample
reported separation where the efficient sets coincide, and it did so because a
uniform sample of a high-dimensional box contains essentially nothing near the
efficient set. the cause is alignment: [2]'s g is minimised at x_n = 0 and ε·x_n
is minimised there too, so under phi_cw nothing trades. reversing the alignment
breaks it the other way.

three things follow and all three are in the code: zdt1's half-width is quadratic
with an interior optimum while dtlz2's stays linear because [3]'s g is already
quadratic, each carrying its reason in a comment; the check itself was
strengthened, so the separation assertion is made on a grid of the region where
the efficient sets live and not on the box, which is r-08 built as a test and
repeated in a5 and again in a5-b when the width forms changed; and whether the
stronger check is the right one is s-07 to the supervisors, with the tier 1 forms
chosen against the stronger check meanwhile. **the residual is r-09: the rule was
derived from two benchmarks and one tier 0 design and is a working rule, not a
result**, so every new problem runs the full diagnostic before use — which is what
criterion 3 of the part 2 gate, section 7.2, exists to enforce.

**and this is why no slice fraction is a quantity anywhere.** r-22: phi_lu's zdt1
slice fraction at ε = 0.10 runs 0.2441, 0.1435, 0.1392 and 0.0769 at grid sides
32, 61, 64 and 128, a factor of three across the four. a fraction quoted as a
number would be quoting the grid. a5-b's verdict is untouched, being about whether
the three sets are distinct and not about how large any is, and every quantitative
statement in section 3 rests on the runs' cardinality columns instead.
docs/part1/a1_uncertainty_model.md parts 2 and 4 and appendix a5-b.

### 6.3 the endpoint cancellation, and the evaluation-order fix

the second image coordinate of phi_ls and phi_cw is a width, and the obvious route
to it is to subtract endpoints. the error is ε|c| and nothing else: on p1's 61 × 61
grid against an integer-arithmetic reference, the width column's maximum absolute
error runs 7.2e-16, 1.1e-13, 1.1e-10 and 1.1e-07 as the centre offset runs 0, 1e3,
1e6 and 1e9, while the same column computed from the centre and the half-width
holds 2.2e-16 at all four.

**the size of the error is not the finding.** the finding is what it does to the
structure of the column: p1's r_1 depends on x_2 alone and takes exactly 46
distinct values on that grid; the endpoint route gives it 210 and the
centre-radius route gives it 46. an order built on a column is built on that
column's ties, and the subtraction shatters them.

the obvious remedy was measured and rejected. a tolerance works at p1's
magnitudes — every value from 1e-15 to 1e-04 returns the exact set for all three
phi — but the band narrows by one decade per decade of centre magnitude and is
gone by |c| = 1e12; scaling per column by that column's own size is worse than not
scaling, the noise in a width column being proportional to the centre it was
subtracted out of; and a tolerance would have had to be shared by pymoo, whose
0.6.2 epsilon argument is a no-op because it computes F − ε and dominance is
translation invariant.

**so the subtraction was removed instead.** composing [1]'s phi with the endpoint
map gives the same automorphism read in the other coordinates, with determinant
2·det φ, so it vanishes exactly when the paper's admissibility condition fails and
never otherwise — checked entry by entry in exact rational arithmetic on 2000
random coefficient sets before anything was implemented. a problem now declares the
representation its intervals are actually computed in, phi is applied once through
the matching route, and no round trip is formed anywhere: p1 and both benchmarks
declare centre-radius, p0 declares endpoints, which is the form [1] states it in.
**the project therefore uses one untoleranced pareto relation everywhere, and the
reason it can is that the arithmetic error a tolerance would have covered is not
committed in the first place.** d-02, docs/part1/a4b_dominance_tolerance.md,
docs/part1/phase_a_summary.md.

### 6.4 the instrument overstates agreement, and one registered instrument failed

the calibration's own result is a methods result: **the measurement of a
set-overlap statistic on recovered sets is biased toward agreement**, by +0.41 to
+0.81 relative on the headline pair at budget 5000 and by +0.28 to +0.49 at 20000,
section 3.2. the sign was then shown to transfer by direct measurement — nine of
nine statistics moving the same way under a quadrupled budget on all three
problems — and **the magnitude was not transferred and no correction factor is
applied to any benchmark number**. that combination, a bias whose direction is
established and whose size is deliberately not extrapolated, is what the
calibration problem exists to buy and is what no measurement on the benchmarks
alone could have produced.

the second methods result is a negative one and is kept. **m-1, the tail-survival
lift, was registered before the run with both of its thresholds fixed, and it
failed as an instrument.** it orders a sample by an image column and asks whether
the smallest members survive the filter, which conflates being *protected* with
being a *genuinely good point*: under example 2.2 the image columns are the real
objectives, so an extreme member survives for ordinary reasons. e1 measured a lift
of 8.22 on p1 under example 2.2, where the prediction says at most 1.5 because the
effect is absent there, and 1.65 to 2.27 on the columns where it is present, where
the prediction says at least 3 — the same non-discrimination seen from both sides.
**the mechanism stands and the instrument does not**; m-1 is withdrawn, not
re-thresholded and not reinterpreted, and its companion m-2 confirmed on the same
run. that both thresholds were fixed before the run is exactly what made the
failure visible, and that is the result.
PROGRESS.md x-01, docs/part1/e3_synthesis.md section 5.4.

a fourth item belongs here in one sentence and is section 5.1's counterpart: a
same-phi seed-to-seed noise floor **has no operating point** — identically zero at
delta zero at any
dimension because two independent uniform samples share no point, and a step
function in delta at tier 1 dimensions, 0.002604 to 0.006619 at a tenth of the box
diameter and 0.734139 to 0.951821 at a fifth on dtlz2 — so it is withdrawn *as measured*
and replaced by the across-seed interquartile range of a statistic computed from
one sample filtered three ways, which is that statistic's complete sampling
variability. `results/tier1/noise_floor_sweep.csv`, docs/part1/e3_synthesis.md section
5.1. the replacement is weaker than a floor and the memoria says so.


## 7. what part 1 hands to part 2

### 7.1 the claim, in the form the evidence supports, with c5 marked unsupported

the design objection cannot be argued away and does not need to be, because the
project measured its own negative arm: docs/part1/a1_uncertainty_model.md part 4 records
that under the rejected **linear** half-width phi_lu and phi_ls give identical
sets at every level and phi_cw gives the crisp order. that is the control, and it
turns the design choice from a vulnerability into the claim's second half.

> **the recommended claim.** the choice of order relation is not a modelling
> detail. under a half-width that is non-monotone in a driver the centres do not
> share, two of the framework's own named orders select substantially different
> efficient sets: on a problem whose phi-efficient sets are known in closed form
> they share 0.103177 of their union and neither contains the other, and on zdt1
> and dtlz2 at thirty and twelve variables between 63 and 91 per cent of one set
> lies outside the other at every imprecision level tested, by an instrument
> calibrated to overstate agreement. under a half-width linear in a driver aligned
> with the centres' own optimum, the same three orders collapse onto two, and one
> of them onto the crisp order. **which of the two regimes an application is in is
> a property of its uncertainty model, and it is checkable before any solver
> runs.**

it is conditional, and it is stronger for being so: it is falsifiable on a new
problem rather than merely reproducible on a chosen one, and it survives a reviewer who asks where the
width function came from. it costs the presentation one extra sentence.
docs/part1/e3_synthesis.md section 7.1.

clause by clause against the evidence, docs/part1/e3_synthesis.md section 7:

    c1  "not a modelling detail"            the conclusion of c2 to c4; stands or
                                            falls with them
    c2  "replaces most of the optimal set"  strongly supported and exact, 0.605290
                                            and 0.877429 in lebesgue measure
    c3  "they share 10.3 per cent"          strongly supported and exact, with the
                                            instrument's error measured beside it
    c4  "reproduces on the benchmarks"      supported in its **asymmetric** form
                                            and not its symmetric one, section 3.1
    c5  "persists on problems interval-      **not supported, and it cannot be by
        valued at source"                    e1 and e2**

> **c5 is not supported by e1 and e2 and cannot be**, both of part 1's benchmark
> problems being crisp problems with a band put around them. it is part 2's to
> settle, on a problem that is interval-valued at source.

### 7.2 the five-criterion gate an interval-native problem must pass

stated before any example was seen, so that no example is admitted by a criterion
invented after looking at it. an example serves only if it satisfies **all five**;
one that passes four is reported with the one it failed and is not used.
docs/plan_after_meeting.md section d0.

1. **dimension.** n small enough that the recovered sets can be compared in the
   decision space at the project's budget, and m small enough that the transformed
   problem's 2m columns do not saturate rank 1 at the project's population size.
   recorded and not predicted, because section 4.3 measured that the column count
   does not on its own order the saturation.

2. **closed form.** whether the phi-efficient set is derivable in closed form and
   **by which published result of a paper in scope**, named by theorem or example
   number. the available route is b1's, and it closes cheaply where the objectives
   are quadratic with constant diagonal hessians, since condition (15) then
   decouples into n scalar equations as it does for p1.

3. **phi-separation, checked where the efficient set lives.** the three phi must
   give distinct non-trivial sets, none equal to the crisp set and none the whole
   box — **checked near the efficient set and never on a uniform sample of the
   box**, which is section 6.2 made into an admission rule.

4. **the width driver.** whether any image column under any phi is a function of a
   strict subset of the decision variables, and if so which variables are free and
   what the phi-efficient set's projection onto them is. not a disqualification: it
   is section 3.4's condition, and an example that has it is a third registered
   test of the mechanism. it is recorded because a recovered front on such an
   example carries points whose distance from the efficient set is a property of
   the order and not of the solver.

5. **genuinely interval-valued at source.** the intervals are the paper's own and
   are not a band added around a crisp problem. an example whose objective is f(x)
   plus or minus a constant, or plus or minus a function the paper introduced to
   make the problem interval-valued, **fails**, because such an example is what
   part 1 already did.

part 2 runs all three phi. e3 selects none and this document selects none.

### 7.3 what a second calibration point would remove

the whole of part 1's quantitative authority rests on one problem where the answer
is known. that is one point, and three specific weaknesses follow from its being
one.

**the instrument's error has a measured sign and an unmeasured magnitude.** the
factor 1.81 is p1's alone and is not carried anywhere, section 3.2. a second
problem with closed-form phi-efficient sets would say whether the bias is stable
across problems or whether 1.81 is a property of p1's geometry, which is the
difference between a calibrated instrument and a calibrated measurement.

**the hausdorff distance is the one statistic stable across the dimension change
and it is the one statistic with no exact value.** `exact_regions_p1.csv` carries
no hausdorff, so the statistic that travels best is the one that was never
calibrated, section 3.1. a second derivation would decide whether to promote it.

**the geometry question is open and one run would decide it.** what changes the
shape of the disagreement between p1 and the benchmarks is neither the benchmark's
structure — zdt1 and dtlz2 differ in separability, in g, and in m and agree in
geometry — nor the dimension between twelve and thirty. what is left is the width
driver's alignment: p1 has a half-width whose driver is also a centre driver, and
under a5-b's rule no tier 1 variable carrying a centre may drive a width. **the
deciding measurement is p1's own width design transplanted onto zdt1, a width
driven by x_1**; it is a variant of a5 and not a new problem family, and it is
out of scope before 25 september. section 7.1's conditional claim makes it the
natural next measurement, so it belongs in the memoria's future work.
docs/part1/e3_synthesis.md section 4.4.

two cheaper things sit beside it and are recorded rather than scheduled. **x-02**
needs twenty seeds of random search on p1 under example 2.4, column 3 — one
measurement, the cheapest in the project, closing a registered prediction, section
5.3. and **b1-b**, the optional closed form along the one-parameter family from
example 2.4 to example 2.2, would make the overlap with X_cw a function of t rather
than three numbers; it is admissible by [1]'s own determinant condition at every t,
it needs no run, and it strengthens the calibration rather than the exploration.
PROGRESS.md section 2, docs/plan_after_meeting.md section c3.

### 7.4 what else is owed, in one list

    s-11   the containment criterion, both containments and whether any of it is
           published. the headline does not depend on it, section 4.1, and the
           third question decides whether the memoria cites or observes
    s-12    the singular segments; priced, section 5.1
    s-07, s-09  the slice check and the per-objective width scaling; the tier 1
           forms were chosen against the stronger check meanwhile
    p-01, p-06  two reading tasks, both answerable now that the corpus is open

**p-02 and p-05 are closed**, docs/answered.md and docs/part2/lit_review.md
sections 2 and 3: [9]'s a_w is the half-width by its own equation (2.4), its
definition 3.4 is example 2.4 of [1] in the same coefficients, and [10]'s
regularity criterion is theorem 34 exactly as b1 cited it — **so b1's derivation
carries no unverified number.** **f1 has run**, docs/part2/lit_review.md: no
example of [16] passes the gate on the reading alone and none fails it, because
criterion 3 cannot be answered by reading and not determinable is not a pass;
**five pass every criterion a reading can settle and criterion 5 passes on
nineteen of twenty**. **clause c5 of section 7.1 is reachable**, and it is judged
in docs/part2/part2_closing.md section 3.3.


## 8. the four prohibitions, checked

*no phi is ranked.* no table here orders the three and no sentence says one order
is better. section 3.3 says X_lu grows with eps and X_cw does not, which is a
statement about set size. section 3.4 says the protected-minimiser condition holds
on some columns and not others, and says explicitly that the condition is a
property of a column and that the orders enter only by determining which columns
exist. section 3.5 orders three **solvers** within a row under one fixed phi and
states that a column may not be read down and that the two objective blocks may
not be juxtaposed.

*nothing is claimed from the containment.* section 4.1 uses it only to withhold
two pairs from the evidence and records that refuting it would not move the
headline number.

*no slice fraction is quoted as a quantity.* r-22, and section 6.2 states the
factor-of-three grid dependence as the reason. every quantitative statement rests
on a cardinality column or on an exact area.

*no benchmark number is interpreted without the instrument's error.* section 3.2
establishes it, states what may and may not be said, and every benchmark figure in
sections 3.1 and 3.3 refers back to it.
