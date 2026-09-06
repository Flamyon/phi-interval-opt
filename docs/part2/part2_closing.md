# part 2, closed: what was asked, what was done, what was found

session f4, 2026-09-05. no experiment, no module, no run and **no new claim and no
new number**, with one exception the brief names and this document makes once:
**the judgement on clause c5**, which f2 and f3 both refused as not theirs and
which is stated in section 3.3. every figure below is read out of an f2 or f3
artefact and the artefact is named beside it; where a figure is part 1's it is
quoted from docs/part1/part1_closing.md with the tier 0 or tier 1 file that
document names. where a number is derived from two such numbers by an identity,
the identity is stated at the point of use.

who this is for. the supervisors, and whoever drafts the memoria. **it is the
document g1 lifts part 2 from**, and it is written to be complete enough that g1
opens nothing else for part 2's results. where this document and an f2 or f3
artefact could differ, the artefact wins.

its model is docs/part1/part1_closing.md, deliberately: the two are read together
and a reader who has finished part 1's document should find the same sections in
the same order here. **that document is canonical for part 1 and this one is
canonical for part 2**, and neither restates the other's numbers independently.

what it may not do, and each is checked in section 9. it may not rank phi,
CONTEXT.md section 2. it may not claim anything from the containment while s-11
is unanswered, docs/part1/a_close_containment.md section 6. it may not quote a
slice fraction as a quantity, r-22. it may not interpret a measured number
without the instrument's error beside it. and it carries one prohibition of part
2's own, which the shape of I-BK1's answer forces: **no nested pair may be
presented as a measured difference between two orders**, docs/part2/f3_native_run.md
section 5.

where the detail is, so this document does not become a second copy of it:

    docs/part2/lit_review.md            f1: the reading of six papers, the twenty
                                        problems of [16] transcribed, the gate
                                        applied, ten ambiguities
    docs/part2/f2_ibk1_derivation.md    f2: the derivation on I-BK1, criterion 3
                                        answered exactly, the two external checks
    docs/part2/f3_native_run.md         f3: the run record, generated
    results/part2/                      f3's artefacts: the tables, the per-seed
                                        values, the raw arrays and 24 figures
    docs/part1/part1_closing.md         part 1's settled record, and sections 3.1,
                                        3.2, 6.4, 7.1, 7.2 and 7.3 in particular
    docs/plan_after_meeting.md          section d: the gate, the reading prompt,
                                        the fallback and the derivation branch
    PROGRESS.md                         the open rows and the registered
                                        predictions


## 1. the question, and the answer

### 1.1 the question part 2 was set

part 1 ended with a clause it could not support. docs/part1/part1_closing.md
section 7.1 tests the recommended claim clause by clause and marks c5 —
**"and it persists on problems that are interval-valued at source"** — as *not
supported, and it cannot be by e1 and e2*, because both of part 1's benchmark
problems are crisp problems the project put a band around. the same document
states, in section 7.2, a five-criterion gate an interval-native problem must
pass, written before any example was seen; and in section 7.3, the three specific
weaknesses that follow from part 1's quantitative authority resting on **one**
problem whose answer is known.

so part 2 was set three questions, and they are not the same question:

    is there a published problem, interval-valued in its own coefficients, that
        passes the gate?
    if there is, what do the three orders do on it, and can that be known exactly
        rather than sampled?
    and does the project's own instrument, run on it without being told the
        answer, reproduce what the derivation says?

### 1.2 the answer

**yes, on I-BK1, problem 1 of appendix A of [16], printed page 27.** the three
orders of [1] give three distinct phi-efficient sets on it, in closed form and
with no sampling anywhere: they are the wedges nu ∈ [3/4, 3/2], [2/3, 5/3] and
[1/2, 2] in the coordinate nu = x_2(5 − x_1) / (x_1(5 − x_2)), with Lebesgue
measures 2.875612, 3.790332 and 5.685282, so that **0.494201 of the largest lies
outside the smallest**. the independence of half-width from centre that makes
this possible is [16]'s own: no objective of any of the five candidate problems
has proportional centre and half-width coefficient vectors, and the project chose
nothing about it. the instrument reproduces the derived statistics with a
relative error between −0.088235 and +0.482801 at budget 5000, every magnitude
inside the +0.810049 measured on the calibration problem.

**and the three sets nest.** X_cw ⊊ X_lu ⊊ X_ls, all three inclusions strict, so
on this problem there is no pair nested in neither direction and **part 1's
headline quantity has no counterpart here**. what I-BK1 supplies is a second
calibration point and an exact statement that the orders differ; what it does not
supply is a second measurement of *how much* they differ in the sense part 1
measured it. section 3.3 states clause c5 in the form that evidence supports,
which is narrower than the draft.

one further thing, and it is the most consequential result either part produced:
**the point [16] publishes as the Pareto optimal solution of its own first test
problem is not Pareto optimal in the paper's own definition**, and two printed
statements it rests on are false as printed. section 5 states that as a
correction, with the checkable facts first.


## 2. what was done, in the order of the arc

three stages, two of them paper and pencil. each names its close-out document.

**read the corpus and apply the gate.** [16], [9], [10], [7], [8] and [13] read
against their printed pages; the twenty problems of [16]'s appendix A transcribed
one block each with n, m, the 2m column count, the box and every objective in the
paper's own notation; and the five criteria of docs/part1/part1_closing.md
section 7.2 applied per problem. **no example passes the gate on the reading
alone and none fails it**: criterion 3 needs a sample near the efficient set, the
paper supplies none, and not determinable is not a pass. **criterion 5 passes on
nineteen of twenty** — the problems are ⊕_j [a_ij, b_ij] ⊙ h_ij(x), imprecision
in the paper's own coefficients, attributed to Mondal and Ghosh 2025 — and only
I-CH fails it, being f(x) ± 1, which is also part 1's constant-width degeneracy
occurring in a published problem. **five pass every criterion a reading can
settle**: I-BK1, I-SD, I-IKK1, I-VFM1 and I-MHHM2. the session also closed p-02
and p-05, which removed the one unverified number in b1's derivation, and
recorded ten ambiguities without resolving any. docs/part2/lit_review.md.

**derive the answer exactly, and let the derivation answer the gate's last
criterion.** criterion 3 asks whether the three phi give distinct non-trivial
sets, and on a problem whose efficient sets are derivable the derivation answers
it in Lebesgue measure rather than by a sampled diagnostic, which is strictly
better evidence. docs/part2/lit_review.md section 7.2 states the argument. b1's
route — image coordinates written out, phi-convexity by theorem 3.3 of [1],
regularity by [10] proposition 32 then [10] theorem 34, condition (15) of example
3.9 for the candidate set, example 3.8 statement 3 to lift to optimality — closes
on I-BK1 **under all three phi with no reservation**, which on p1 it did under one
of three. **criterion 3 passes and I-BK1 passes the gate.** it also produced the first
external checks the project has ever had on a derivation, one of which passes and
one of which does not, section 5. docs/part2/f2_ibk1_derivation.md.

**encode it and measure it.** I-BK1 as [16] states it, coefficients cited to
printed page 27, representation declared "endpoints" because every h_ij is a
square and Moore's product does not interchange the boundary functions there;
**no uncertainty added and no width function written**. f2's three wedges encoded
as pairs of integer-coefficient inequalities, so membership carries no tolerance.
then the same grid part 1 ran: three solvers, three phi, five seeds, budget 5000
with the convergence check at 20000 — 18 configurations, 90 runs, 741.927417
seconds, 24 figures, every number in the record read back out of a file the run
wrote. results/part2/summary.csv, docs/part2/f3_native_run.md.


## 3. the result: the second calibration point

### 3.1 the derived sets, exact, and the three pair statistics

the whole answer on I-BK1 is one scalar. writing U = x_1/(5 − x_1) and
V = x_2/(5 − x_2), which map [0,5) increasingly onto [0,∞), condition (15) reads
U = Q_1/P_1 and V = Q_2/P_2 with U free, so each derived set is the set of points
whose **nu := V/U** lies in a closed interval determined by the aspect ratios the
phi exposes. docs/part2/f2_ibk1_derivation.md sections 2.1 and 2.4:

    X_lu = { x ∈ [0,5]² :  2 x_1(5−x_2) ⩽ 3 x_2(5−x_1) ⩽ 5 x_1(5−x_2) }
    X_ls = { x ∈ [0,5]² :    x_1(5−x_2) ⩽ 2 x_2(5−x_1) ⩽ 4 x_1(5−x_2) }
    X_cw = { x ∈ [0,5]² :  3 x_1(5−x_2) ⩽ 4 x_2(5−x_1) ⩽ 6 x_1(5−x_2) }

each is the region between two hyperbolas of constant nu running from (0,0) to
(5,5), and all three are pinned at those two corners. under all three phi the
optimal set and the weak optimal set both equal X_phi exactly, f2 section 2.6.

the exact statistics. source: results/part2/exact_regions_ibk1.csv, reproduced by
a second route in results/part2/table_1_exact_ibk1.csv, decision block, and
tabulated in docs/part2/f3_native_run.md section 2.

| phi | band of nu | area | source |
| --- | --- | --- | --- |
| cw | [3/4, 3/2] | 2.875612 | `exact_regions_ibk1.csv`, key area |
| lu | [2/3, 5/3] | 3.790332 | same |
| ls | [1/2, 2] | 5.685282 | same |

| pair | cov(a→b) | cov(b→a) | jaccard | dice |
| --- | --- | --- | --- | --- |
| lu, ls | 1.000000 | 0.666692 | 0.666692 | 0.800018 |
| lu, cw | 0.758670 | 1.000000 | 0.758670 | 0.862777 |
| ls, cw | 0.505799 | 1.000000 | 0.505799 | 0.671802 |

all six coverages and both overlap conventions are keys of
results/part2/exact_regions_ibk1.csv — `coverage_a_in_b`, `coverage_b_in_a`,
`overlap_union_share` for the jaccard and `overlap_d2_convention` for the dice.
coverage leads and any overlap is named, d-09. **the jaccard equals the smaller
coverage on every pair here, and that is the nesting and not a coincidence**: for
nested sets the intersection is the smaller and the union the larger.

**what separates on I-BK1 is size, and it is exact.** by division of the areas,
|X_ls| is 1.499943 times |X_lu| and 1.977068 times |X_cw|, and |X_lu| is 1.318096
times |X_cw|; equivalently, and this is the same fact read as the coverages
report it, **0.333308 of X_ls lies outside X_lu, 0.241330 of X_lu lies outside
X_cw and 0.494201 of X_ls lies outside X_cw**, those three being one minus the
coverages above. these are derived quantities and carry
no instrument error at all. **they are not a measured difference between two
orders and must never be printed as one**: on two of the three pairs one direction
is fixed by the containment criterion before anything runs, and on the third the
nesting is f2's finding about the problem, not a measurement.

### 3.2 the instrument's error, measured a second time

this is what part 2 was for. docs/part1/part1_closing.md section 3.2 records
`results/tier0/instrument_error_p1.csv` as the only file in the project comparing
a derived quantity with the same quantity measured; **results/part2/instrument_error_ibk1.csv
is the second, on a problem of a different origin.** the error is the measured
median minus the exact value and the relative error is that gap over the exact
value, which is the form part 1 states p1's in. all rows below are random search's
one filtered sample — one uniform sample of the box, evaluated once, filtered
under each phi in turn, so the three sets differ only through the order — at delta
zero, budget 5000, five seeds, cardinalities 121, 145 and 106 under lu, ls and cw.

| pair | metric | exact | measured | error | relative |
| --- | --- | --- | --- | --- | --- |
| lu, ls | cov(a→b) | 1.000000 | 1.000000 | 0.000000 | 0.000000 |
| lu, ls | cov(b→a) | 0.666692 | 0.834483 | +0.167791 | +0.251677 |
| lu, ls | dice | 0.800018 | 0.909774 | +0.109756 | +0.137192 |
| lu, cw | cov(a→b) | 0.758670 | 0.815126 | +0.056456 | +0.074414 |
| lu, cw | cov(b→a) | 1.000000 | 0.911765 | −0.088235 | −0.088235 |
| lu, cw | dice | 0.862777 | 0.866071 | +0.003294 | +0.003818 |
| ls, cw | cov(a→b) | 0.505799 | 0.750000 | +0.244201 | +0.482801 |
| ls, cw | cov(b→a) | 1.000000 | 1.000000 | 0.000000 | 0.000000 |
| ls, cw | dice | 0.671802 | 0.857143 | +0.185341 | +0.275886 |

source: results/part2/instrument_error_ibk1.csv, delta 0.0, n_evals 5000; the
per-seed values behind every median are in
results/part2/decision_metrics_by_seed.csv.

**three things this establishes, and one it does not.**

**the sign transfers to a problem the project did not construct.** six of the nine
rows measure above the exact value, two land exactly on it and one below,
docs/part2/f3_native_run.md section 4. the two that land exactly on it are the two
containments, and they are fixed before any solver runs. **the one that measures
below is cov(cw→lu)**, the one direction no containment covers: f2's nesting of
X_cw inside X_lu is a statement about the derived regions, and the finite
non-dominated sets of a sample need not nest for that pair. so on every row where
the measurement is free to move, **the instrument reports more agreement than
there is**, which is the direction part 1 measured on p1 and the direction that
makes a measured coverage an upper bound on true sharing.

**the magnitude does not transfer, and that is the finding.**
docs/part1/part1_closing.md section 7.3 says a second calibration point would say
"whether the bias is stable across problems or whether 1.81 is a property of p1's
geometry, which is the difference between a calibrated instrument and a calibrated
measurement". it is a property of p1's geometry. by the identity
factor = measured jaccard / exact jaccard, which is the form part 1 states p1's
1.81 in, and reading the measured jaccards from
results/part2/overlap_conventions.csv, key jaccard_median at delta 0.0, against
the exact ones from results/part2/exact_regions_ibk1.csv:

| pair | exact jaccard | measured, 5000 | factor | measured, 20000 | factor |
| --- | --- | --- | --- | --- | --- |
| lu, ls | 0.666692 | 0.834483 | 1.2517 | 0.817204 | 1.2258 |
| lu, cw | 0.758670 | 0.763780 | 1.0067 | 0.794872 | 1.0477 |
| ls, cw | 0.505799 | 0.750000 | 1.4828 | 0.728543 | 1.4404 |

p1's headline pair, for comparison and from
docs/part1/part1_closing.md section 3.2: 0.103177 exact against 0.187190
measured, a factor of 1.81 at budget 5000 and 1.49 at 20000. **no factor is
transported anywhere by this document and none may be by g1**: the four numbers
above are four measurements of one instrument on two problems, they differ by a
factor of nearly two between pairs of one problem, and their spread is itself the
result. what a reader may take from them is the sign and nothing else.

**every magnitude on I-BK1 is inside p1's.** the largest relative error at delta
zero and budget 5000 is +0.482801 against p1's +0.810049 on the same statistic
family. the brief's stopping rule — that a magnitude outside p1's would indict the
encoding or the derivation — did not fire, and nothing was adjusted to fit.

**what it does not establish is a general bound.** two problems are two problems,
the bias is not modelled, and no correction factor is applied to any number in
either part.

### 3.3 clause c5, judged

this is the judgement docs/part2/f2_ibk1_derivation.md section 7 and
docs/part2/f3_native_run.md section 11 both declined to make, each saying it was
f4's. it is made here, once, and in the narrowest form the evidence carries.

**what is established.** on I-BK1 — problem 1 of [16]'s appendix A, published by a
third party for a different purpose, whose intervals are imprecision in its own
printed coefficients, to which this project added no uncertainty and for which it
wrote no width function — the three orders of [1] give **three distinct
phi-efficient sets**, in closed form, with the difference exact: bands
[3/4, 3/2] ⊊ [2/3, 5/3] ⊊ [1/2, 2] in nu and areas 2.875612, 3.790332, 5.685282,
so that 0.494201 of the largest lies outside the smallest. the distinctness does
not depend on a design choice of ours: f2 section 0's check shows that centre and
half-width are proportional exactly when every coefficient interval of an
objective has the same relative half-width, which is the degeneracy part 1's
section 6.1 records, and **no objective of any of the five candidate problems is
proportional** — on I-BK1 the ratios are 1/3 against 1/2 on G_1 and 1/2 against
2/3 on G_2, in exact rationals. and the project's own instrument, run on the
problem under all three phi at five seeds and two budgets without being told the
derivation, reproduces the derived statistics within the error of section 3.2.

**what is not established.** all three sets nest, so **there is no non-nested pair
on I-BK1 and therefore no counterpart to part 1's headline number.** part 1's
quantity is how much of each of two sets, neither containing the other, lies
outside the other — 0.103177 of the union shared on p1, 63 to 91 per cent outside
on the benchmarks. that question has no answer here, because on I-BK1 one
direction of every pair is exactly one. and one problem is one problem: nothing
here is a statement about interval-native problems in general.

**so the clause, in the form the evidence supports:**

> **c5, as supported.** on a problem published by a third party and
> interval-valued in its own coefficients, the three orders of the framework
> select three different efficient sets, and on that problem the difference is
> known exactly rather than sampled: the sets are strictly nested with measures
> 2.875612, 3.790332 and 5.685282, and 0.494201 of the largest lies outside the
> smallest. the project's instrument, applied to it under the same protocol as to
> the adapted problems, reproduces those statistics with the same direction of bias
> on every statistic free to move, and a smaller magnitude than on the calibration
> problem. **what does not carry over
> is the shape of the disagreement**: on the adapted problem two of the orders
> cross and on this one all three nest, so the magnitude part 1 reported has no
> counterpart here and none is claimed.

**that is narrower than the draft clause in three ways, and each is deliberate.**
it says *different sets* and not *substantially different answers in the sense of
part 1's number*. it says *on a problem* and not *on problems*. and it says
nothing about persistence as a property of the class, because the class was
sampled once. **c5 stops being marked unsupported and becomes supported in that
form, and in no wider one.** the wider form — that the effect persists on
problems interval-valued at source, plural, with a magnitude — remains
unsupported, and section 7 says what would move it.


## 4. the structural finding: crossing on an adapted problem, nesting on a native one

**this was not predicted anywhere and it is a real difference between the two
kinds of problem.** on p1, which the project constructed, phi_lu and phi_cw are
nested in neither direction: docs/part1/part1_closing.md sections 3.1 and 4.1
record that 0.605290 of X_lu lies outside X_cw and 0.877429 of X_cw outside X_lu
in exact Lebesgue measure, X_lu reaching above x_2 = 1 where X_cw does not go and
X_cw filling x_2 < 4/5 where X_lu does not — each set holds a region the other
cannot reach, and that is why part 1 has a headline pair at all. on I-BK1, which
the project did not construct, **all three orders are totally ordered by
inclusion**, docs/part2/f2_ibk1_derivation.md section 3.1.

**what is known about why, and it is the place to look.** on I-BK1 both image
coordinates of objective 1 are supported at the origin and both of objective 2 at
(5, 5), and every one of the twelve image coordinates is a diagonal quadratic with
strictly positive coefficients, f2 section 1.2. that has two consequences. first,
there is **no singular weight direction under any phi**, f2 section 2.3, where on
p1 phi_ls and phi_cw each had two; the reason is that p1's width coordinates are
functions of one variable each, while [16] put a non-degenerate interval on both
terms of both objectives. second, the stationarity system collapses onto **one
scalar**: every derived set is the preimage of a closed interval of nu, so the
three sets differ only in which interval of one number they expose, and the
comparison of three regions in the plane becomes the comparison of three intervals
on a line. the six endpoints are ratios of published coefficients and they order
strictly, 1/2 < 2/3 < 3/4 < 3/2 < 5/3 < 2, f2 section 3.1. **that ordering is the
nesting.**

**and the honest limit of the explanation.** the wedge structure explains why the
disagreement on I-BK1 is one-dimensional — three intervals rather than three
regions of different shapes, as p1 has, where X_lu is bounded by two conic arcs,
X_ls by one and X_cw is the unit square less one open edge. it does **not** force
the nesting: two intervals can overlap partially, and two sets so defined would
cross exactly as p1's do. the nesting itself is a numerical property of [16]'s printed
coefficients: the six band endpoints are ratios formed from the aspect ratios of
the twelve image coordinates, f2 section 2.4's table, and on these coefficients
they happen to order strictly. one visible feature of that table is worth naming
because it is checkable in the problem statement — every one of the four
coefficient intervals carries the same lower endpoint 0.1, so both lower boundary
functions have aspect ratio 1 and the diagonal nu = 1 lies inside all three bands
— but that places the bands around a common point and does not order their
endpoints, so it is a feature and not a proof.

**so this is an observation with a mechanism and it is not a result.** one problem
of each kind cannot establish that adapted problems cross and native ones nest,
and the sentence "the orders nest on interval-native problems" must not be
written. what can be written is that the two geometries are different, that the
difference has a located mechanism in the coefficient structure, and that the
mechanism is checkable on any new problem before it is run.

**the observation is also testable cheaply, and section 7.2 names the test.**
I-IKK1 is interval-native and has p1's structure rather than I-BK1's: its
half-widths 0.5x_2², 0.5(x_2−20)² and 0.5x_1² are functions of one variable each
and are minimised on lines rather than at their centres' minimisers,
docs/part2/lit_review.md sections 1.9 and 1.10. **it therefore separates the two
explanations** — "adapted against native" from "these coefficients against those"
— which no second problem of I-BK1's shape could do.


## 5. a correction to a published result

**this is the most consequential thing either part of the project found, and it is
written so that a reader can check it without trusting the project.** the facts
come first, the mechanism second, and the limits of the claim last. it is stated
as a correction and not as a criticism: the project read [16] closely because
[16]'s problems are the only interval-native problems available to it, and
everything below was found by taking the paper's own definitions and its own
printed numbers seriously.

### 5.1 the transcription, confirmed against the paper before anything is claimed

I-BK1 as printed on page 27 of [16] is

    G_1 = [0.1, 0.2] ⊙ x_1²  ⊕  [0.1, 0.3] ⊙ x_2²
    G_2 = [0.1, 0.3] ⊙ (x_1 − 5)²  ⊕  [0.1, 0.5] ⊙ (x_2 − 5)²,  x ∈ [−10, 10]².

every h_ij is a square, so Moore's product does not interchange the boundary
functions anywhere and the four boundary functions are the obvious ones. **two
independent confirmations that this reading is the paper's own**, both from the
paper. first, the gH-gradients and gH-Hessians [16] prints for I-BK1 on printed
page 18 are exactly the derivatives of those four functions, endpoint by endpoint,
docs/part2/f2_ibk1_derivation.md section 1.1. second, **recomputing G at the
paper's own printed x⋆ = (3.914930, 1.428474) gives
([1.736721, 3.677497], [1.393317, 6.731112]) against the paper's printed
([1.736722, 3.677497], [1.393317, 6.731112])** — agreement to the last printed
digit in all four values, f2 section 4.2. the reading is settled before any claim
rests on it.

### 5.2 x⋆ is dominated, in the paper's own relation, by an explicit point

[16] Table 1, printed page 20, gives x⋆ as the output of its Algorithm 1 after
twelve iterations, and printed page 21 calls it a Pareto optimal point of I-BK1.
its definition 2.17, printed page 7, is that no other feasible x has
G_i(x) ⪯ G_i(x⋆) for all i, with ⪯ its definition 2.2, printed page 4:
componentwise ⩽ on the endpoint pair. **there is such a point.** take

    y = (2.897500, 2.397500),

which is inside the box, and compare in exact rational arithmetic against the
paper's **own printed** G(x⋆):

| coordinate | G(y) | printed G(x⋆) | margin | strictly smaller |
| --- | --- | --- | --- | --- |
| G_1 lower | 1.414351 | 1.736721 | +0.322370 | yes |
| G_1 upper | 3.403503 | 3.677497 | +0.273994 | yes |
| G_2 lower | 1.119351 | 1.393317 | +0.273966 | yes |
| G_2 upper | 4.712655 | 6.731112 | +2.018457 | yes |

source: docs/part2/f2_ibk1_derivation.md section 4.2. **all four strictly
smaller**, so G_i(y) ≺ G_i(x⋆) for i = 1, 2, and x⋆ is not a Pareto optimal point
of I-BK1 under definition 2.17, nor a weakly Pareto optimal point under definition
2.16, which forbids an x strict in every objective.

**the verdict is not an artefact of the printed rounding.** the tightest of the
four margins is 0.273966, and perturbing x⋆ by 10⁻⁶ in each coordinate — more than
its six printed decimals leave open — moves any endpoint value by at most about
4 × 10⁻⁶, five orders of magnitude smaller than that margin, f2 section 4.2. the
four inequalities are checkable by hand against the paper's own printed row and
need nothing from this project.

### 5.3 the run reproduces it independently, by a different route and without being told

f3's run was given the problem and the three phi and nothing about section 5.2.
the question it asks is not f2's: run the project's three solvers, do they return
points that beat the paper's printed row, in [16]'s own definition 2.2, which does
not depend on which phi drove the search. **they do, in every configuration.**

| what | value | source |
| --- | --- | --- |
| configurations with a dominator | 18 of 18 | `dominators_summary.csv` |
| seeds with a dominator, each configuration | 5 of 5 | same, `seeds_with_a_dominator` |
| median dominating points, budget 5000 | 5 to 15 | same, across solvers and phi |
| median dominating points, budget 20000 | 4 to 40 | same |
| widest margin over all rows | 0.269627 | same, `widest_margin_over_seeds` |

source: results/part2/dominators_summary.csv, with the per-seed counts in
results/part2/dominators_by_seed.csv. the margin of a returned point is the
smallest of its four gaps against the printed row, and the widest such margin any
seed achieved is 0.269627, at random search and budget 20000 —
**against f2's algebraic 0.273966**, which is a point f2 found by exhaustive
search and not one any solver was steered toward. two routes, two arithmetics, one
answer.

### 5.4 the mechanism, which is why the paper's algorithm stops where it does

a failed external check that is not explained is indistinguishable from a failed
derivation, so f2 section 4.3 located the mechanism and it is checkable.

[16]'s definition 2.18 calls x⋆ Pareto critical when no v has
∇_gH G_i(x⋆)^T ⊙ v ≺ 0 for all i, where that product is a **Minkowski sum of
Moore products**, printed page 6. summing termwise loses the correlation between
the coordinates, so the interval's upper endpoint is at least
max(∇G̲_i^T v, ∇Ḡ_i^T v) and strictly greater whenever the two boundary gradients
disagree in sign pattern. requiring the interval to be ≺ 0 is therefore **strictly
stronger** than requiring both boundary functions to descend, and a point can have
no interval descent direction while still admitting a direction that lowers all
2m image coordinates. the consequence for I-BK1, worked out in closed form:

| set | description | measure over [0,5]² |
| --- | --- | --- |
| X_cw | nu ∈ [3/4, 3/2] | 2.8756 |
| X_lu | nu ∈ [2/3, 5/3] | 3.7903 |
| X_ls | nu ∈ [1/2, 2] | 5.6853 |
| [16]'s Pareto critical set, definition 2.18 | nu ∈ (1/9, 10) | 16.0714 |

**the critical set is 4.24 times X_lu and strictly contains all three derived
sets.** the closed form was checked against a brute-force scan of directions,
computed from the paper's own printed gH-gradients, at twelve points spread across
the quadrant including x⋆ itself and points on both sides of both boundaries:
**twelve test points against a 60000-direction scan, 0 disagreements**. and x⋆
sits at nu = 0.110854 against the boundary 1/9 = 0.111111, just outside the
critical set, which is consistent with the paper's own reported
ξ(x⋆) = −2.8154e−07 against its tolerance 10⁻⁶: **x⋆ is the algorithm's output at
tolerance, approaching a set that is itself four times too large.** all from f2
section 4.3.

### 5.5 what is claimed, and what is not

**claimed, because it was checked.** [16]'s **proposition 2.1** (printed page 7:
critical plus positive definite gH-Hessians implies Pareto optimal) and **lemma
2.4(ii)** (printed page 7: critical plus I(ℝ)^m convexity implies weakly Pareto
optimal) are **false as printed**, and [16]'s own first test problem is the
counterexample. the witness is x = (5/2, 5/6), nu = 1/5, strictly inside the
critical set. every hypothesis was verified rather than assumed: U convex; the
boundary functions polynomial and gH-differentiability everywhere by [10]
proposition 32 and theorem 34; ∇²_gH G_i ≻ 0 from the interval Hessian entries the
paper prints on page 18; I(ℝ)^m convexity checked directly on 200000 random chords
with 0 violations; and x Pareto critical by a scan of 200000 directions finding
none with both intervals ≺ 0. and x is dominated in all four endpoint coordinates
by y = (1.886667, 1.440000) with a minimum margin of 0.124351. f2 section 4.3.

**not claimed.** **where the proof fails is not claimed**: proposition 2.1's proof
is given in [16] as "similar to the proof of item (ii) of Lemma 2.4", and lemma 2.4
is attributed to [16]'s reference [27], Mondal and Ghosh 2025, which is not on disk
and whose proof is not reproduced in [16]. so the two failures are one failure, it
is inherited rather than original to [16], and this project has not read the proof
it would have to fault. nothing is claimed about [16]'s Newton method, which may
converge exactly as its theorems say to exactly what definition 2.18 defines;
nothing is claimed about the other nineteen problems of appendix A; and nothing is
claimed about the paper's numerical work beyond the two printed items named.

**what it obliges the memoria to do**, and this disposes of ambiguity a-11, which
PROGRESS.md leaves for this document:

    **the memoria must not cite proposition 2.1 or lemma 2.4(ii)** of [16], in any
        form, including as a justification for a published point's status.
    **Table 1's x⋆ must not be used as a fixture, a checkpoint or a reference
        point** anywhere in the project. f2 section 7 already forbids it.
    **the published checkpoint that does hold may be used and should be**:
        equation (25)'s one-parameter curve is exactly nu = 162/169 = 0.958580,
        constant along its whole length, and lies strictly inside all three derived
        sets; eight of Table 2's eleven published points reproduce it to six
        decimals and two more are its corners, f2 section 4.1. **that is the first
        external check the project has ever had on a derivation, and it passes.**
    **a-4 of docs/part2/lit_review.md is resolved in the negative and must be
        recorded as such**: the paper's printed argument for x⋆'s optimality —
        mutual non-domination with eleven particular points — is invalid, as a-4
        says, and the rescue a-4 offered through proposition 2.1 does not survive.
    **a-12 travels with it**: Table 2's α = 0.8 row carries the α = 0.9 row's
        second coordinate, 4.628566 where equation (25) gives 4.235294, and the
        row's objective values were computed from the printed value. f2 section 4.4.
    and the disposition of both, as findings addressed to the authors rather than
        to the memoria's argument, is the research chat's; **this document records
        them and claims nothing further.**


## 6. two conventions that needed stating once rather than three times

### 6.1 delta: zero is the only readable value, and the reasons differ per problem

delta is the tolerance at which two decision vectors count as the same point. the
project states it as a fraction of the box diameter, which is a convention and not
a measurement, and **I-BK1 is its third distinct failure**. the three failures do
not share a cause, which is why the convention and not any one problem is the
thing to record.

**on p1, at two variables, a positive delta reports a choice.** the coverage of
X_lu in X_cw at budget 5000 runs 0.555932, 0.624590, 0.726230, 0.930508, 0.996587
and 1.000000 across box fractions 0, 0.01, 0.02, 0.05, 0.10 and 0.20 —
`results/tier0/delta_sweep.csv`, quoted in docs/part1/e1_tier0_run.md section 8.
the statistic nearly doubles across the range and saturates inside it, so any
positive value is a tuning decision reported as a measurement.

**at tier 1 the same fraction is a different instrument at each dimension**,
because distances scale with the square root of the number of variables, d-08.
measured: the seed-to-seed noise floor at a fifth of the box diameter is 0.734139
to 0.951821 on dtlz2 at twelve variables and **exactly 0.000000** on zdt1 at
thirty, and at three tenths it is 1.000000 on dtlz2 and 0.437500 to 0.896000 on
zdt1 — `results/tier1/noise_floor_sweep.csv`, docs/part1/e2_tier1_results.md. one
fraction, two dimensions, opposite readings.

**on I-BK1 the failure is scale and not dimension, and it is the sharpest of the
three.** the box is [−10, 10]², diameter 28.284271, while all three derived sets
live in [0, 5]², whose diameter is 7.071068 — f2 section 2.5 puts every derived
point at least 5 from every face. so the project's standard 0.05 of the box
diameter is delta = 1.414214, which is **a fifth of the derived sets' own
diameter**, and at that value:

    every cross-phi coverage and overlap in the run is exactly 1.000000, at both
        budgets and on all three pairs — results/part2/table_2_measured.csv,
        decision block, delta 1.4142135623730951.
    **and so is the noise floor**, all eighteen rows of one phi against itself at
        two seeds — same file. the floor equals the signal, so nothing at that
        delta is evidence of anything.
    the sweep says where it goes: the (ls, cw) coverage runs 0.750000, 0.892857,
        0.993007, 1.000000, 1.000000, 1.000000 across the six fractions, and the
        (lu, cw) pair is already saturated at 0.02 —
        results/part2/delta_sweep.csv.

**so, as a property of the convention rather than of any problem: delta zero is
the only readable value in this project.** it is also exact rather than a limit
wherever the headline instrument is used, d-08 and docs/part1/part1_closing.md
section 3.1: the three sets of one comparison are index sets over one array, so
two decision vectors are the same point bitwise or they are two points, and the
statistic is a shared count over a count with no tolerance in it. every headline
number in both parts is at delta zero, and every positive-delta row in either
part's tables is there because two *different* samples are being compared, which
is the noise floor and the population solvers' own pairs.

**one consequence beyond delta**, recorded here because it has the same cause. the
symmetric hausdorff distance is the one statistic part 1 found stable across the
dimension change, docs/part1/part1_closing.md section 3.1, and it is quoted there
in units of the box diameter. on I-BK1 that normalisation divides by a scale the
derived sets do not occupy, so the I-BK1 hausdorff medians — 0.549099 on (lu, cw),
0.690402 on (lu, ls), 0.699738 on (ls, cw) at budget 5000,
docs/part2/f3_native_run.md section 3 — **are not comparable with p1's 0.339524**
and are not normalised here.

### 6.2 the budget response is not one-directional, and what that costs the bias argument

docs/part1/part1_closing.md section 3.2 argues that the *sign* of the instrument's
bias transfers even though its magnitude does not, and the argument leans on a
uniform budget response: quadrupling the budget lowers all three statistics on p1,
zdt1 and dtlz2, **nine of nine**, and on p1 that direction is known to be toward
the exact value.

**on I-BK1 that uniformity does not hold.** by the identity
error = measured median − exact value, taking the medians at delta zero from
results/part2/table_2_measured.csv at both budgets and the exact values from
results/part2/exact_regions_ibk1.csv:

| pair | metric | exact | error at 5000 | error at 20000 | movement |
| --- | --- | --- | --- | --- | --- |
| lu, ls | cov(a→b) | 1.000000 | 0.000000 | 0.000000 | exact at both |
| lu, ls | cov(b→a) | 0.666692 | +0.167791 | +0.150512 | toward |
| lu, ls | dice | 0.800018 | +0.109756 | +0.099390 | toward |
| lu, cw | cov(a→b) | 0.758670 | +0.056456 | +0.078977 | **away** |
| lu, cw | cov(b→a) | 1.000000 | −0.088235 | −0.060606 | toward |
| lu, cw | dice | 0.862777 | +0.003294 | +0.022937 | **away** |
| ls, cw | cov(a→b) | 0.505799 | +0.244201 | +0.222744 | toward |
| ls, cw | cov(b→a) | 1.000000 | 0.000000 | 0.000000 | exact at both |
| ls, cw | dice | 0.671802 | +0.185341 | +0.171154 | toward |

**five of the nine rows move toward the exact value, two move away and two are on
it at both budgets and cannot move.** the two that move away are on the (lu, cw)
pair, and all three of that pair's statistics *rise* with budget where the other
six fall or stay; on p1 every statistic fell. so the sentence "every row shrinks
when the budget is quadrupled", true on p1 and used there, **is not universally
true and must not be written as a general property of the instrument.**

**what that costs the argument.** part 1's transfer argument has two legs: the sign
of the bias, and a budget response that is uniform and, on p1, known to point at
the truth. **the second leg does not survive on I-BK1** and no longer supports the
first anywhere. it is not replaced by a weaker version of itself here.

**what survives, and it is stated as the whole of what survives.** the sign of the
bias on I-BK1 is measured directly against a known answer and does not need the
budget argument at all: six of nine rows measure above the exact value, one below
— the one direction no containment covers — and two exactly on it, section 3.2.
and the largest relative magnitude on I-BK1 is +0.482801 against p1's +0.810049
at the same budget, so every I-BK1 row is inside p1's largest. **on the two
problems where the truth is known, the instrument overstates agreement; how much
it overstates it is a property of the problem, and neither part transports a
factor.** that is what the second calibration point
bought, and it is less than part 1 hoped for in section 7.3 and more than part 1
had.


## 7. what could not be settled, and what would settle it

### 7.1 four items, stated as such

**the magnitude question has no counterpart on I-BK1 and cannot acquire one.**
part 1's headline is a statement about two sets neither of which contains the
other. all three of I-BK1's sets nest, so the question is not askable there, and
no run on I-BK1 at any budget would make it askable. section 3.3 states c5 without
it.

**the hausdorff distance is still uncalibrated.**
docs/part1/part1_closing.md section 7.3 names this as the second of the three
weaknesses a second calibration point would remove: the statistic that travels
best across the dimension change is the one with no exact value, because
`results/tier0/exact_regions_p1.csv` carries no hausdorff. **it is not removed.**
results/part2/exact_regions_ibk1.csv carries no hausdorff either — f2 derived the
regions and their measures, and a hausdorff distance between two closed-form
regions was neither derived nor asked for. so the promotion question stays exactly
where part 1 left it, and section 6.1 adds a second reason not to promote it: on
I-BK1 the normalisation part 1 used is not available.

**the geometry question is untouched, as was known in advance.**
docs/part2/lit_review.md section 7.2 recorded before f2 ran that I-BK1's
half-widths are minimised where its centres are, which is p1's own regime, so a
measurement there is a second point in the same regime. it is. **the deciding
measurement remains p1's width design transplanted onto zdt1**, a width driven by
x_1, which docs/part1/part1_closing.md section 7.3 places out of scope before 25
september and in the memoria's future work. nothing in part 2 moves it.

**the containment is used and not claimed from, exactly as in part 1.** on I-BK1
the (lu, ls) and (ls, cw) relations are what
docs/part1/a_close_containment.md's criterion predicts, so they are checks and are
withheld from the evidence; the (lu, cw) relation is predicted by nothing and is
f2's finding about the problem, derived from the closed forms without the
criterion. **s-11 is untouched and nothing here rests on it.** if the supervisors
refute the criterion, the two withheld pairs are reported like the third and no
number in section 3 moves, because none came from them. one thing part 2 did add,
and it is recorded as not being an answer: [9]'s proposition 4.2, printed page
223, proves for a fourth relation the containment the criterion predicts, which is
a second independent check of the criterion and **not** a check of the two
containments s-11 asks about, docs/part2/lit_review.md section 2.4.

### 7.2 what a second interval-native problem would add, and what it would cost

**the candidate is I-IKK1**, problem 11 of [16]'s appendix A, printed page 29,
n = 2, m = 3, six image columns, box [−50, 50]²:

    G_1 = [1,1] ⊙ x_1²  ⊕  [0,1] ⊙ x_2²
    G_2 = [1,1] ⊙ (x_1−20)²  ⊕  [0,1] ⊙ (x_2−20)²
    G_3 = [0,1] ⊙ x_1²  ⊕  [1,1] ⊙ x_2²

it passes every criterion a reading can settle and closes b1's route cheaply, all
image coordinates being non-negative-coefficient diagonal quadratics,
docs/part2/lit_review.md section 1.9. **it would add three things I-BK1 cannot.**

**it separates the two explanations of section 4.** its half-widths 0.5x_2²,
0.5(x_2−20)² and 0.5x_1² are functions of **one** variable each and are minimised
on lines rather than at their centres' minimisers, so it is interval-native and
outside the alignment regime, with p1's structure and not I-BK1's,
docs/part2/lit_review.md section 1.10. **if its three sets cross**, part 1's
geometry occurs on a problem nobody adapted, the difference between the two
geometries is located in the width structure and not in the problem's provenance,
and c5 becomes statable in part 1's own terms with a magnitude. **if they nest**,
a second native problem with p1's width structure has nested anyway, which is the
first evidence that provenance and not structure is what separates the two cases —
evidence and not proof, two problems being two problems. **either outcome is worth
having**, which is not true of a second problem of I-BK1's own shape, where a
nesting would say nothing new.

**it is a third registered test of the protected-minimiser condition, on three
columns at once.** x-01's condition applies where an image column is a function of
a strict subset of the decision variables; under every phi three of I-IKK1's six
columns are, docs/part2/lit_review.md section 1.9 criterion 4. **I-BK1 could supply
no test at all**, and that absence is itself one of part 2's measured results:
none of its twelve image columns has a non-empty free set and none is constant,
results/part2/free_sets.csv, measured at the run by redrawing each variable rather
than asserted, which is what f2 section 1.2 predicts from the forms — every image
coordinate is a diagonal quadratic in both variables, because [16] put a
non-degenerate interval on both terms of both objectives. **I-BK1 is the first
problem in the project where the effect is structurally absent under every phi**,
so m-2 is not computed on it and the absence is the finding, not a gap.

**and it would give a third calibration point**, which is what would turn two
error factors into a statement about the instrument rather than about two
problems.

**what it costs, and what it does not buy.** docs/part2/lit_review.md section 7.4
prices it at **two sessions** beyond part 2's three — one derivation and one for
the encoding and the statistics — and it lands where the schedule has no slack
before 25 september. **it has no published checkpoint**: I-BK1 is the only problem
in appendix A that has one, so the confirmation equation (25) gave — a published
one-parameter family landing inside the derived set along its whole length —
would not be available, and a derivation there would rest on the project's own
algebra as p1's does. and at m = 3 the derivation is a three-objective
version of f2's, which lit_review judges cheap but which nothing has yet done. **it
is recorded here as the single most valuable thing part 2 did not do**, and it is
where the memoria's future-work paragraph should point first, ahead of the
portfolio application.


## 8. what the two parts say together

this section is what g1 turns into the paper's conclusion.

### 8.1 the arc, and what each stage established

    **read and verify.** [1] checked line by line against the printed page: the
        automorphism class, the three named orders with their exact coefficients,
        definition 3.1's three solution concepts and examples 3.8 and 3.9 with
        condition (15). docs/part1/a0_framework.md.
    **construct a calibration problem, and measure the trap first.** the literal
        reading of the supervisors' slide 19 is degenerate — a constant half-width,
        or any half-width that is an exact function of the centre, makes all three
        orders and the crisp order return the identical index set. p1 was built to
        the rule that follows. docs/part1/a1_uncertainty_model.md.
    **derive its answer exactly.** three closed-form regions on p1, verified in
        exact rational arithmetic in both directions, which is what makes a
        coverage question askable rather than plottable.
        docs/part1/b1_phi_efficient_sets.md.
    **validate the instrument.** three solvers on one contract against the derived
        sets, ninety measurements: no solver returns a point that beats the
        derivation anywhere, and the reverse direction fails in twelve, every one
        NSGA-II, left failing on purpose as strict xfails.
        docs/part1/c3_validation.md.
    **calibrate it.** the same statistics measured on recovered sets beside the
        derived ones, so the gap between them is a number:
        `results/tier0/instrument_error_p1.csv`.
    **extend to benchmarks.** zdt1 at thirty variables and dtlz2 at twelve, five
        imprecision levels, 540 runs, and the exact and measured numbers on one
        page. docs/part1/e2_tier1_results.md, docs/part1/e3_synthesis.md.
    **read the interval-native corpus and apply a gate written in advance.** twenty
        published problems transcribed, five passing every criterion a reading can
        settle, nineteen of twenty interval-valued at source.
        docs/part2/lit_review.md.
    **derive on one of them.** I-BK1's three phi-efficient sets in closed form,
        with no reservation under any phi, and the gate's last criterion answered
        exactly rather than sampled. docs/part2/f2_ibk1_derivation.md.
    **measure it with the same instrument.** the same grid, the same seeds, the
        same budgets, a second instrument-error row, and a published claim
        independently contradicted. docs/part2/f3_native_run.md.

### 8.2 the objection to transformation methods, and what answers it

CONTEXT.md section 10 f4 makes this part of part 2's subject and part 2 is where
the reading half of it was done, so it is stated here once and in full.

**the objection, from the three papers that make it**, transcribed with printed
pages in docs/part2/lit_review.md section 4.1. [7] says converting an interval
problem to a deterministic one "loses interval information, which has a negative
impact on the accuracy of the original problem" — asserted, with "obviously" as
the whole of the support. [8]'s is the strongest and the only conditional one: a
transformation "may inadvertently disrupt the inherent conflict relationship
between objectives" **when the span of the interval is too large**. [13]'s is
about the solver's behaviour, "slow convergence and unreliable feasible
solutions". **and a fourth, from [16] itself, is not the same objection and must
not be quoted as if it were**: its first statement, printed page 3, is about the
scalarisation f_l + f_u and not about the 2m transformation, lit_review section
1.7.

**what answers it, in three parts, and none of them is an argument.**

    **the transformation's validity condition is published and checkable, and it
        is [16]'s own.** its conclusion, printed page 27, states that the 2m
        reading is available exactly where the lower and upper boundary functions
        do not interchange. the project's construction satisfies it by design on
        p1 and both benchmarks, and on I-BK1 it holds because every h_ij is a
        square. **the memoria cites that condition rather than defending the
        construction unaided**, from a paper that is not defending it either.
    **the selection-pressure loss the objection points at was measured by this
        project on its own problems**, docs/part1/part1_closing.md section 4.3:
        every one of NSGA-II's twenty-four positive-imprecision configurations
        saturates rank 1 in every seed, with the saturating generation ordered and
        monotone. that is the empirical form of the objection, stated as a
        measurement rather than as a citation.
    **and the direct-interval literature reports the same difficulty about its own
        methods**, lit_review section 4.3: [8] says the count of non-dominated
        solutions "will greatly increase" under its own IP-dominance "even if the
        objective does not rise to a high dimension", and [13] that interval
        dominance sorting alone "may lead to insufficient selection pressure".
        **[8]'s per-objective relation is phi_lu itself**, its Remark 1 printed
        page 5, so the difficulty is not a property of transforming.

**what that licenses and what it does not.** it licenses one sentence in the
memoria: the saturation the project measured is not an artefact of the
transformation, because the papers raising the objection report the same
difficulty and treat it as the reason for adding a second criterion. **it does not
license calling the two the same quantity** — the project measured a rank-1
saturation fraction under one transformation at one population size, and [8] and
[13] make a qualitative statement with no number — so it is a convergent
observation and never a corroborating measurement. and none of the three papers'
dominance relations is an automorphism of the framework, for three different
reasons, lit_review section 4.2: [7]'s score depends on the whole population,
[13]'s on the comparison partner, and [8]'s aggregation admits an "or
incomparable" disjunct that componentwise ⩽ on R^2m cannot.

### 8.3 the one claim, in the form both parts support

> **the recommended claim.** the choice of order relation is not a modelling
> detail. under a half-width that is non-monotone in a driver the centres do not
> share, two of the framework's own named orders select substantially different
> efficient sets: on a problem whose phi-efficient sets are known in closed form
> they share 0.103177 of their union and neither contains the other, and on zdt1
> and dtlz2 at thirty and twelve variables between 63 and 91 per cent of one set
> lies outside the other at every imprecision level tested, by an instrument
> calibrated to overstate agreement. under a half-width linear in a driver aligned
> with the centres' own optimum, the same three orders collapse onto two and one
> of them onto the crisp order. **which of the two regimes an application is in is
> a property of its uncertainty model, and it is checkable before any solver
> runs.**
>
> **and the effect is not an artefact of problems built to display it.** on
> problem 1 of the appendix of [16], published by other authors for another
> purpose and interval-valued in its own coefficients, the same three orders again
> give three distinct efficient sets, derived in closed form with measures
> 2.875612, 3.790332 and 5.685282, so that 0.494201 of the largest lies outside
> the smallest; the same instrument, applied under the same protocol, reproduces
> those statistics with the same direction of bias on every statistic free to
> move, and a smaller magnitude than on the calibration problem. **there the three
> sets are strictly nested rather than crossing, so the disagreement is one of size
> and not of direction, and the magnitude reported for the adapted problems has no
> counterpart on it.**

the first paragraph is part 1's, unchanged from
docs/part1/part1_closing.md section 7.1. the second is part 2's and is section
3.3's clause c5 in claim form. **the concession in its last sentence is not
optional and may not be dropped in compression**: without it the paragraph reads
as a second measurement of part 1's quantity, which it is not.

### 8.4 what is still open

    **s-11**, the containment criterion, both containments and whether any of it
        is published. neither part's headline depends on it, and part 2 added a
        published check of the criterion on a fourth relation which is explicitly
        not an answer.
    **s-12**, the singular weight segments. p1's alone, priced there; I-BK1 has no
        singular weight direction under any phi, so the gap does not recur but is
        not closed.
    **s-02**, example 3.9's weight phrase, now carrying two witnesses against the
        strict reading — b1's pointwise one on p1 and f2's structural one on
        I-BK1, where every weight vector reaching a boundary ray of any derived set
        has two zero components. no conclusion in either part depends on the
        answer, every optimality verdict being drawn from example 3.8.
    **p-01, p-04, p-06**, three reading tasks, each one look in a pdf now on disk.
    **x-02**, twenty seeds of random search on p1 under example 2.4, column 3 —
        the cheapest measurement in the project and still not run.
    **the geometry question**, section 7.1, and **a second interval-native
        problem**, section 7.2.
    **a-11 and a-12**, section 5.5, whose disposition toward the authors is the
        research chat's.
    **a-1 and a-3**: [16] is an arXiv preprint with no venue, and its appendix
        credits its problems to Mondal and Ghosh 2025 with a phrase that does not
        settle whether they are taken from it. **the memoria cites [16] as a
        preprint with its identifier and names both sources for the problems.**

### 8.5 what a reader must not conclude

    **not that any order is better than another.** neither part ranks phi, no
        table in either orders the three, and the question "which phi should an
        application use" is not one this study asks or answers.
    **not that I-BK1's numbers are a second measurement of part 1's.** they are
        exact and part 1's headline is measured; they describe nested sets and part
        1's describe crossing ones. the two are different quantities about
        different geometries.
    **not that nesting is a property of interval-native problems.** one problem,
        with a mechanism located and explicitly not general, section 4.
    **not that any measured error factor transports.** 1.81 is p1's, 1.0067 to
        1.4828 are I-BK1's, and no number in either part is corrected by any of
        them.
    **not that any row of the I-BK1 run is a measured difference between two
        orders.** all three pairs nest, so one direction of each is fixed before a
        solver runs, docs/part2/f3_native_run.md section 5.
    **not that [16]'s method is wrong.** section 5.5 states precisely what is
        claimed about that paper and what is not.
    **not that the two objective-space blocks may be compared.** e1's tier 0 block
        is at full cardinality and f3's is truncated to the common cardinality 100,
        r-16, so they may never be placed side by side, and neither may be read as
        a solver ranking across phi.

### 8.6 what g1 lifts from part 2

    the exact table and the three areas, section 3.1, from
        results/part2/exact_regions_ibk1.csv.
    the instrument-error table, section 3.2, from
        results/part2/instrument_error_ibk1.csv, and the three jaccard factors at
        budget 5000 beside p1's 1.81, with the warning that none of them
        transports.
    clause c5 in the form of section 3.3, and the claim paragraph of section 8.3.
    the correction of section 5, with its four inequalities and the independent
        reproduction, which is the one part 2 result that is about the literature
        rather than about this study.
    the answer to the transformation objection, section 8.2, which is the reading
        of three papers plus part 1's own saturation measurement and is what the
        memoria's methods section needs.
    the twenty-problem table and the per-criterion verdicts,
        docs/part2/lit_review.md sections 1.8, 1.9 and 6, which go into the
        memoria whatever else does: they are what says the corpus was read and why
        one problem of twenty was used.
    the figures: results/part2/figures/ holds 24, six fronts and eighteen
        decision-space panels with f2's derived set drawn behind the recovered
        points, one phi per panel; the decision-space panels at budget 5000 are
        where the nesting is visible, and they are the natural companions to part
        1's p1 figures, which show the crossing.


## 9. the prohibitions, checked

*no phi is ranked.* no table here orders the three and no sentence says one order
is better. section 3.1 gives the three set sizes, which is a statement about
measure; section 4 explains why they nest, which is a statement about geometry;
section 7.2 recommends a **problem** and no order, and part 2 ran all three phi
everywhere.

*nothing is claimed from the containment.* section 7.1 states the use exactly as
part 1 does: two of the three pairs are withheld from the evidence because the
criterion predicts them, the third is derived from the closed forms without it,
and refuting the criterion would move no number in section 3. section 7.1 also
records that [9]'s proposition 4.2 is a check on the criterion and not an answer to
s-11.

*no slice fraction is quoted as a quantity.* none appears. every quantitative
statement in this document rests on an exact Lebesgue measure, on a measured
median with its file named, on a cardinality column or on a count of rows.

*no measured number is interpreted without the instrument's error beside it.*
section 3.2 establishes the error on I-BK1 before section 3.3 reads anything from
the run, section 6.2 states what the budget response does and does not license, and
every measured figure in this document refers back to one of the two.

*no nested pair is presented as a measured difference between two orders.* section
3.1 states the size separation as derived and exact and says in terms that it is
not a measurement; section 3.3 says the headline quantity has no counterpart here;
section 8.5 repeats it as a prohibition on the reader. the only measured pair
numbers quoted anywhere in this document are the instrument-error table of section
3.2 and the budget-response table of section 6.2, and in both they are read
against a known answer as a property of the instrument and never as a property of
the orders.
