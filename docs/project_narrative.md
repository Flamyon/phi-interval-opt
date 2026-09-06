# phi-interval-opt: what has been done, in plain words

this document is for a reader who has not followed the sessions: the supervisors,
and the author in october writing the memoria. it covers phases a to c: what each
subpart was for and what it found. it makes no claim that is not already recorded
somewhere else in the repository, and it names where. where this document and a
deliverable could differ the deliverable wins, on the model of the three phase
summaries.

PROGRESS.md is the working state file and is read by the coding agent. this file
is the human one.

docs/explicacion_proyecto.md is the second plain-language account. it is in
spanish, it is written for the author rather than for the supervisors, and it
covers the whole project — phases a to e, part 2, the counterexample and the
presentation skeleton — where this file stops at phase c. neither restates the
other's numbers independently, and both defer to the deliverables.

docs/part1/phase_a_summary.md, docs/part1/phase_b_summary.md and
docs/part1/phase_c_summary.md are the close-out of one phase each, organised by
subpart, and every claim in them points at the deliverable that established it.
this file is one continuous account of phases a to c in plain words. the readers
are different and so is the register; **where this file and a phase summary could
differ, the summary wins**, on the same rule that puts the deliverable above the
summary.

part 1 as a whole is docs/part1/part1_closing.md, the settled record of phases a
to e, and part 2 is docs/part2/part2_closing.md. this file stops at phase c and
supersedes neither.


## the project in three sentences

interval optimization replaces unknown numbers with intervals, and intervals have
no single natural order. the supervisors' framework generates a whole family of
orders from automorphisms of the plane, written phi, and fixing one turns an
interval problem into an ordinary multiobjective problem. this project measures,
empirically, how much the solutions change when phi changes.


## phase a, formulation. building the problems and the orders

### a0, reading the paper properly

a0 read the paper claim by claim and recorded every statement with its example
number and page.

what it found. the condition for an automorphism to be admissible is exactly that
its 2x2 coefficient matrix has nonzero determinant, and nothing more. the paper
names three phi that each carry a convexity notion: example 2.2 is the identity,
giving the lower and upper bounds; example 2.3 gives the lower bound and the full
width; example 2.4 gives the centre and the half-width. it also names a fourth,
example 2.1, in a car-purchase illustration, which carries no convexity notion and
is not used. a0 section c9 establishes that the list is complete by enumerating
every explicit automorphism in sections 2 and 3 of [1], line by line, rather than
by skimming.

a0 also confirmed the two structural facts everything downstream rests on: phi is
applied to each interval objective separately, and a problem with m interval
objectives becomes a real problem with 2m objectives.

### a1, how imprecision enters a problem

this is the subpart the rest of the project rests on.

the obvious way to make a crisp problem interval-valued is to add a constant band
to each objective: f becomes [f - eps, f + eps]. a1 measured what that does: with
a constant width, all three phi produce exactly the same efficient set, and it is
the same set as the crisp problem. the reason is geometric. if the width never
changes, the image of the problem in the (centre, width) plane is a flat line
rather than a region, and any injective map sends a monotone curve to another
monotone curve. the three orders coincide by construction, not by result. the
study would have measured nothing and would have looked like a null result.

one caveat the deliverable carries and this account must not drop: that verdict is
in exact arithmetic. computing phi from the endpoint pair instead makes the same
degenerate construction look like a discovery. on zdt1 at eps = 0.05 the crisp
order and phi_lu return 16 non-dominated points and phi_ls and phi_cw return 30,
and every bit of that
difference is cancellation noise of order machine epsilon times |f| landing in a
width column that is constant by construction. the expected symptom of a
degenerate model is that the three phi coincide, which is easy to notice; the
floating-point symptom is that they differ, which reads as a positive result. that
is r-07, and the evaluation-order rule of a3-b below is what keeps it from
happening.
docs/part1/a1_uncertainty_model.md part 1.

the fix is that the width must vary independently of the centre as the decision
variables move. a1 evaluated putting the imprecision in the coefficients and
putting it in the objective, and recommended the second with the width driven by
decision variables other than those driving the centre.

a1 also found something nobody had asked for. on zdt1 the obvious choice, a width
proportional to the last variable, passes every statistical check on a uniform
sample and still fails, because the width vanishes exactly where the solutions
live, so phi_cw reproduces the crisp order on the part of the space that matters.
the lesson recorded: checking that the three phi differ on a uniform sample of a
large box is not evidence, because such a sample contains almost nothing near the
efficient set.

### a1-b, the width drivers of the test problem

giving both objectives of the small two-variable problem p1 the same width
function makes two of the four transformed columns identical, so each objective's
half-width is driven by the other objective's variable.

the band, and it is a1's finding rather than a1-b's: the efficient set is
two-dimensional and not a curve, and no design at this size fixes that. two
variables and two interval objectives make a four-objective real problem whose
efficient set is generically min(m - 1, n) = 2 dimensional, and forcing a curve
requires the width coordinate and the centre coordinate to share an optimum in
x_2, which is the exact case where phi_cw reproduces the crisp order. a curve and
three distinct phi are not simultaneously available at n = 2, m = 2.
docs/part1/a1_uncertainty_model.md part 3.

that design costs one property, and it is recorded rather than patched: the
efficient set is not a product of intervals under phi_lu and phi_ls, 13 and
11 distinct x_2 ranges across the occupied x_1 columns, while phi_cw keeps its
single range. that is the premise s-08 was answered on, so b1 derives a region
with a curved boundary rather than a rectangle for two of the three phi.
docs/part1/a1_uncertainty_model.md, a1-b section 3.

### a2 and a3, the arithmetic and the orders

a2 built interval arithmetic. it has three separate names for centre, half-width
and full width, because example 2.3 uses the full width and example 2.4 uses the
half-width, and one word for both would erase the difference between two of the
three orders.

a3 built the orders as one constructor over coefficient pairs, validating against
the paper's determinant condition, with the three named examples as instances. it
was built this way because the parameterized extension needs no confirmation to be
admissible: admissibility is exactly the determinant condition, so a family
interpolating between two named examples is admissible by the paper's own
definition, and sampling it at nine or eleven values would give a sensitivity
curve rather than three isolated cases. it is an extension and not the plan, taken
up only if the three named examples are done and time remains, and the constructor
is what makes it a loop rather than a redesign. CONTEXT.md section 4, the
parameterized extension, available and not required.

### a3-b, an arithmetic problem that would have corrupted every result

computing phi from the endpoint pair means computing the width as
(c + r) - (c - r), which is not exactly 2r in floating point. the error is
proportional to the size of the centre, and it lands entirely in the width column,
which is the second coordinate of two of the three phi. measured: a width that
truly takes 46 distinct values on a grid took 210.

the fix is not a tolerance. phi is a linear map, and so is the map from (centre,
radius) to (lower, upper), so composing them gives the same phi evaluated in a
different order. the project evaluates phi as a single linear map on whichever
representation the problem actually computes in, and never rebuilds endpoints from
a centre and a radius in order to subtract them back. this is an evaluation-order
change and not a change to the mathematics: the paper's definition and its
admissibility condition both stand unchanged.

the project therefore uses one dominance relation everywhere with no tolerance,
no rounding and no epsilon.

### a4 and a5, the problems

a4 built the two small analytic problems. p0 is the worked function costa et al.
give after their optimality conditions, which comes with a published answer.
p1 is the two-variable design from a1-b.

a5 built the two benchmarks, zdt1 and dtlz2, as interval problems. both were read
from their original papers, which were fetched for the purpose, because citing a
paper that is not in the repository is not checkable.

### a-close, an unexpected result

the containment ND_lu inside ND_ls is a theorem rather than an observation. the
general form: if one phi's image is
a non-negative invertible linear map of another's, then dominance under the second
implies dominance under the first, so the first's non-dominated set sits inside the
second's. applying it to the paper's own coefficient matrices:

    the phi_lu efficient set sits inside the phi_ls one, exactly, for every problem
    the phi_cw efficient set sits inside the phi_ls one, exactly, for every problem
    phi_lu and phi_cw are nested in neither direction

this matters for what the study can claim. a measured difference between phi_ls
and either of the other two is partly a theorem and cannot be reported as evidence
that the order matters. **the pair that carries the real signal is phi_lu against
phi_cw.**

the constraint the containments carry is narrower than "nothing is built on them".
the project claims no result from either containment
and b1 does not shorten a derivation with them; but a test may assert either as a
self-check on the encoding, which c1 does on random search output and c2 on
nsga-ii's and mopso's, because the containment holds for the non-dominated set of
any finite point set whatever produced it, so what such a test can fail on is the
sample, the route pairing, the column order or the dominance relation. d2 and e3
report the two phi_ls pairs as checks on r-06's prediction and never as
independent findings. that stands until the supervisors answer s-11, and if they
refute the criterion the tests asserting it are deleted and no result moves,
because none was claimed from them. docs/part1/a_close_containment.md, the standing
constraint.

one caveat, r-11: the nesting is a theorem in real arithmetic and fails by
rounding in doubles, one point of 1565 measured on dtlz2 at eps = 0.50. a table
that reported those points as a finding would be reporting arithmetic, so a5
asserts the containment as a band rather than as an equality and d2 names the
artefact in the pair's own status field.


## phase b, ground truth. deriving the answer the solvers are judged against

### b1, the derivation

b1 derived, on paper, what the efficient set of p1 actually is under each phi,
using the published optimality conditions of costa et al. and nothing invented.

it works because every image coordinate of p1 is a quadratic with a constant
second derivative matrix, so the optimality condition becomes a linear system and
the answer comes out as an explicit formula mapping weight vectors to points. the
three sets:

    phi_lu   a region bounded by two conic arcs, x_2 between 4/5 and 4/3
    phi_ls   the box 0 <= x_1 <= 4/3, 0 <= x_2 <= 4/3 cut by
                 7 x_1 x_2 - 4 x_1 + 12 x_2 <= 16, minus the open segment
                 { (x_1, 0) : 0 < x_1 <= 4/3 }
    phi_cw   the closed unit square, minus the open segment
                 { (x_1, 0) : 0 < x_1 <= 1 }

the two excluded segments are reached only in the limit of a singular weight ray,
which is the second of the two limitations below, and they are the whole of what
the closed forms leave out. phi_lu has no singular ray at all. b1 sections 2.3
and 2.4.

all three are strictly inside the decision box, which matters because the paper's
optimality condition has no constraint multipliers and applies only in the
interior. the derived sets reproduce what an independent grid search finds, and
they satisfy the containments derived in a-close, by a route independent of them.

two honest limitations, both recorded rather than patched. p0 cannot be a
reference: its hypotheses fail at the very point the paper discusses, and under
two of the three phi its optimal set is the whole box, so it is a smoke test
rather than a fixture. and on two singular weight directions the published
conditions give only weak optimality, which the project did not resolve because
resolving it would mean inventing a condition, and that is the supervisors' side
of the line.

### b2, encoding it

b2 turned the derivation into code that produces a reference front. it samples the
weight simplex and pushes the sample through the derived formula, rather than
sampling inside the region's boundary, so the code encodes the derivation and not
its conclusion. the tests check the sampled points against the closed-form regions,
which live only in the test file, so a passing test means two independent things
agree rather than one file agreeing with itself.

the undecided singular segments became a required argument with no default, so
whoever computes a metric has to state which set they used, and b2 measured what
the choice costs rather than arguing about it. that is r-12: with the region
sample held fixed and the segment added on top, the igd of a fixed test front
moves by -0.63 to +5.36 per cent at 1000 reference points and by -0.11 to +1.35
at 20000, so the flag can flip a comparison already inside a few per cent and its
value belongs in every table beside the seed and the point count.

a second caveat belongs here and it is d1's rather than b2's, r-13: the front is
sampled through the weight map, so its density in objective space is the
parametrisation's and not the front's, and igd averages over reference points. its
mitigation is a b2-b before d1 and none at all if d1 is cut; c3 is unaffected,
measuring recovery by a hausdorff distance, which is a maximum.
docs/part1/phase_b_summary.md sections 3 and 6.


## phase c, the solvers, and where the project learned the most

### c1, random search

not a competitor. slide 17 calls it the "referencia base", and it is the control.
its sample is a pure function of the box, the budget and the seed, so one sample
can be filtered under each phi in turn and the three results then differ only
through the order. in nsga-ii and mopso, phi drives the search as well as the
ordering, so the two effects cannot be separated. **random search is the only
phi-neutral instrument the project has**, and by the end of phase c it turned out
to be the one carrying the study's main comparison.

### c2 and c2-b, the population methods

two problems found and fixed.

pymoo's generation-count stopping rule gives mopso one extra population of
evaluations, so the two solvers were not on equal budgets. both now stop on an
evaluation count.

mopso was not reproducible: pymoo truncates an overflowing archive using a random
generator that no seed reaches. the fix is to seed the truncation, which changes
the generator it draws from and nothing else. enlarging the archive so that it
never overflows removes the same symptom and is the wrong intervention: the
archive is mopso's leader pool, so taking it from 200 to the 6295 rows the run
returns at budget 20000 changes what the algorithm does, and costs a factor of 16
in runtime at that budget.

c2 also established the single most reassuring fact in the project: pymoo's
non-domination and the project's agree exactly, on every problem and every phi.
there is one dominance relation from end to end.

c2-b measured a confound that runs through every objective-space comparison: all
the objective-space metrics move with how many points a front carries, and the
three solvers return very different numbers. on one fixed front, igd improves by
a factor of 6.5 between 25 and 610 rows from cardinality alone. any comparison
across solvers has to be made at a common front size.

### c3 through c3-f, the validation gate

the gate asks whether the solvers recover the sets b1 derived.

**the forward direction cannot be asserted, and the reason is a theorem.** the
distance from the solver's front to the derived set cannot be small. under
phi_ls and phi_cw one image column depends on a single decision variable, so the
sample point with the smallest value of that variable is strictly best in that
column and nothing can dominate it, whatever its other
coordinate is. it is non-dominated in any sample containing it, and it can sit
anywhere. no budget removes it; a bigger budget re-elects it. this was proved, and
the prediction it carries is exact in probability rather than accurate to two
decimals: for a uniform draw the elected point's other coordinate lies outside
X_cw's [0, 1] with probability exactly 1/2 and its expected overhang is exactly
1/8, at every budget. the measurement is of that constancy and not of the value.
over 200 draws at each of four budgets the mean overhang is 0.1226, 0.1404, 0.1334
and 0.1261, which does not move with the budget, while the median smallest |x_1|
falls by a factor of four for every factor of four in it.
docs/part1/c3_validation.md section 1.3.

**what the tolerance is.** the 0.95 quantile of a measured fill-distance
distribution, 1000 uniform 100-point draws of the derived region, at the
design-fixed front size of 100 and fixed in writing before the study ran. that
is 0.2405, 0.2919 and 0.2318 under the three phi, which is 12.0, 14.6 and 11.6
per cent of the box side. at that quantile a solver whose front were a uniform
draw would exceed it in about one measurement in
twenty, so one isolated failure at a margin near zero is not evidence of a defect
while a failure concentrated in one solver across seeds and phi is, and that
reading was fixed in advance too. docs/part1/c3_validation.md sections 2.3 and 2.4.

**what the gate now says.** every part of every derived set is reached by random
search and by mopso, at every seed, under every phi, at both settings of the
singular flag: sixty of sixty measurements, with margins of 0.09 to 0.25. nsga-ii
reaches it under phi_lu at every seed and fails at three of five seeds under each
of the other two, twelve of its thirty measurements over the tolerance and by
0.005 to 0.039 in a box of side 2. no solver ever returns a point that beats the
derivation, in all ninety measurements. the failure is about how evenly nsga-ii
spreads its hundred points, not about whether the pipeline is correct, so phase e
is not blocked.

those twelve are in the test suite and are meant to be. phase c closed with 794
tests of which 782 pass and twelve fail on purpose, all of them
test_the_derived_set_is_reached_by_the_solver at nsga-ii under phi_ls and phi_cw;
exactly those twelve parameter sets are marked xfail(strict=True), so a
thirteenth failure is a plain failure and an unexpected pass is an error, and the
assertion itself still runs on all ninety. the suite is 822 tests after d2's 28.
docs/part1/phase_c_summary.md section 5, PROGRESS.md.

**the finding, and the five explanations put to measurement.** at equal front size,
nsga-ii covers this efficient set worse than uniform random sampling does, under
phi_ls and phi_cw but not under phi_lu. c3-d, c3-e and c3-f put five candidate
explanations to measurement and excluded all five. the list below is the one
docs/part1/c3_validation.md's section 5.5 closes on, in its own terms:

    that the non-dominated rank saturates and dominance stops selecting. it does
        saturate, under every phi, which is why it cannot explain a split between
        them. section 5.1.
    that far-away points waste front slots. they do, and more under the two
        failing phi, but re-reading each percentile at the number of rows within
        0.10 of the region buys 2 to 11 percentile points of a gap of 50 and
        leaves all ten failing measurements at or above the 74th percentile. only
        a cut that discards a third of the front moves the number, and that is
        describing the front rather than correcting the reading of it.
        section 5.2.
    that nsga-ii is simply bad at what it optimises. it is not, and this is the
        exclusion the plain account most needs, because it is what rules out
        nsga-ii being worse rather than different. measured in the image space it
        actually sorts and spreads in, each column normalised by its range as the
        crowding distance normalises it, nsga-ii sits at the 17th to 86th
        percentile of a uniform draw under phi_ls and the 31st to 71st under
        phi_cw, which is where a uniform draw itself sits, while under phi_lu it
        is at the 0.1st to 4.9th, better than 95 per cent of them. the deficit is
        in the pullback. section 5.3.
    that one map distorts more than another. under the column-scaled jacobian, the
        map the operator works in, the ordering is the reverse of what a
        distortion story needs: phi_lu is the anisotropic one, median
        singular-value ratio 3.97 against phi_ls's 1.42 and phi_cw's 1.45, and no
        ratio anywhere in the table exceeds 10. section 5.4.
    that the two phi align the same geometry differently to the operator's axes.
        the advantage travels with the run and not with the frame: a phi_cw front
        read in phi_lu's frame sits at the 44th to 81st percentile, nowhere near
        the phi_lu runs' 0.1 to 4.9, and the crowding distance is equalised alike
        under all three phi, its coefficient of variation lowest in the run's own
        frame in all fifteen runs. section 5.5.

the fourth of those needs scoping, because its short form is wrong. phi_lu and
phi_cw differ by a similarity, A with A^T A = 2 I, so their images are the same
object up to a rotation and a uniform scaling and no distortion claim can separate
those two at all; the apparent gap between their raw jacobian ratios is a
difference of the region each is averaged over and not of the map. but the map to
phi_ls's image is not a similarity: its condition number is exactly the golden
ratio squared, so phi_ls genuinely is a sheared version of the same object, and
what excludes distortion there is the measurement above and not the identity.
sections 5.4 and 5.5.

what remains is a decomposition, and region size is not a term in it: the
comparison is at equal cardinality and the dimensional check divides area out.
what is left of the region is its shape, and it is about half the effect, acting
on the comparator rather than on the solver. in units that have had region size
divided out, a uniform draw covers X_lu 40 per cent worse for its area than it
covers X_ls or X_cw, X_lu being a thin curved sliver between two conic boundaries
and the other two fat, so the yardstick is weakest exactly where nsga-ii looks
best. the other half is nsga-ii's own, and it is excluded as a general
fixed-cardinality effect by the phi-neutral control rather than by argument:
random search at the same k, on the same regions, against the same comparator sits
between the 12.7th and the 63.2nd percentile under all three phi and shows no
deficit anywhere,
while nsga-ii is at 33 to 60, 85 to 98 and 90 to 99. the swing from phi_lu to each
of the others is +0.483 and +0.485 for nsga-ii against +0.243 and +0.244 for the
control, which is where the halves come from. that half is unexplained, and it is
recorded as unexplained. section 5.5.

**one thing found along the way that is about the framework rather than this
project.** the three phi images of any problem are fixed linear maps of one
another, with no problem parameter in them. the map between example 2.2 and
example 2.4 is a rotation times the square root of two, condition number exactly
one. the map to example 2.3 has condition number exactly the golden ratio squared.
this is offered to the supervisors for comment.

**and one thing that matters for the whole approach.** in all nine problem-phi
configurations c3-d measured, the non-dominated rank fills the entire population
and dominance stops deciding anything. on p1 and on dtlz2 it happens at generation
three or four, so nsga-ii selects on spread alone for 46 or 47 of its 50
generations; on zdt1 it takes until generation 13, 13 and 21 under the three phi
and dips back below the population size twice under phi_lu, at generations 16 and
17, but it arrives all the same. this is a cost of the transformation itself,
since turning m interval objectives into 2m real ones pushes even a two-objective
problem into the many-objective regime. it is the empirical form of the objection
cui et al. raise against transformation-based methods, arrived at with the
project's own numbers. what orders the three problems is not the column count,
which p1 and zdt1 share: it is the non-dominated fraction of the transformed
image, 0.58, 0.79 and 0.55 on dtlz2 against 0.24, 0.52 and 0.47 on zdt1, and three
problems is not enough to assert that as a law, so c3 does not.
docs/part1/c3_validation.md section 5.1.


## what the project can say so far

    the three phi are the paper's named examples, verified with page and example
        numbers.
    a constant-width uncertainty model makes the whole study vacuous, and the
        replacement was designed and measured rather than assumed.
    two of the three efficient sets are provably contained in the third, so the
        informative comparison is phi_lu against phi_cw.
    the efficient sets of the test problem are known in closed form under all
        three phi.
    the solvers recover them, random search and mopso completely, nsga-ii under
        one phi of three.
    nsga-ii has a coverage deficit that depends on phi, half of which is region
        shape acting on the comparator and half of which has no mechanism.
        five candidate mechanisms were put to measurement and excluded.
    the transformation costs dominance-based selection its pressure, everywhere.

none of these is the answer to the research question yet. that comes from phase e.


## where the rest of the account is

phases a, b and c are complete and tagged, and this file stops there. what phases
d and e measured, and what part 1 concluded from it, is
docs/part1/part1_closing.md; part 2 is docs/part2/part2_closing.md. the open rows
are PROGRESS.md, and the questions to the supervisors are
docs/supervisor_questions.md, each carrying the working assumption the project
proceeds on.
