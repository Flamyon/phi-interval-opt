# phi-interval-opt: what has been done, in plain words

written 2026-09-02, at the end of phase c. this document is for a reader who has
not followed the sessions: the supervisors, and the author in october writing the
memoria. it explains what each subpart was for, what it found, what went wrong and
how that was handled. it makes no claim that is not already recorded somewhere
else in the repository, and it names where.

PROGRESS.md is the working state file and is read by the coding agent. this file
is the human one.


## the project in three sentences

interval optimization replaces unknown numbers with intervals, and intervals have
no single natural order. the supervisors' framework generates a whole family of
orders from automorphisms of the plane, written phi, and fixing one turns an
interval problem into an ordinary multiobjective problem. this project measures,
empirically, how much the solutions change when phi changes.


## phase a, formulation. building the problems and the orders

### a0, reading the paper properly

the project had been carrying a third phi, called phi_wu, that nobody had ever
checked against costa et al. 2024. a0 read the paper claim by claim and recorded
every statement with its example number and page.

what it found. the condition for an automorphism to be admissible is exactly that
its 2x2 coefficient matrix has nonzero determinant, and nothing more. the paper
names three phi that each carry a convexity notion: example 2.2 is the identity,
giving the lower and upper bounds; example 2.3 gives the lower bound and the full
width; example 2.4 gives the centre and the half-width. it also names a fourth,
example 2.1, in a car-purchase illustration, which carries no convexity notion and
is not used. phi_wu was in none of them.

what was done. phi_wu was deleted, not flagged. the third phi became example 2.3.
the project's rule became that an unverified item is left out rather than kept
behind a warning comment.

a0 also confirmed the two structural facts everything downstream rests on: phi is
applied to each interval objective separately, and a problem with m interval
objectives becomes a real problem with 2m objectives.

### a1, how imprecision enters a problem

this is the subpart that saved the project from producing nothing.

the original plan added a constant band to each objective: f becomes
[f - eps, f + eps]. a1 measured what that does and confirmed the suspicion: with a
constant width, all three phi produce exactly the same efficient set, and it is
the same set as the crisp problem. the reason is geometric. if the width never
changes, the image of the problem in the (centre, width) plane is a flat line
rather than a region, and any injective map sends a monotone curve to another
monotone curve. the three orders coincide by construction, not by result. the
study would have measured nothing and would have looked like a null result.

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

### a1-b, fixing the test problem

the small two-variable problem p1 originally gave both objectives the same width
function, which made two of the four transformed columns identical. a1-b gave them
different width drivers and re-measured everything.

what it cost: the efficient set is a two-dimensional band and not a curve, and
a1-b established that a curve is not available at this size. two variables and two
interval objectives make a four-objective real problem whose efficient set is
generically two-dimensional, and forcing a curve requires the width and the centre
to share an optimum, which is the exact case where phi_cw collapses to the crisp
order. a curve and three genuinely different phi cannot both be had.

### a2 and a3, the arithmetic and the orders

a2 built interval arithmetic. it has three separate names for centre, half-width
and full width, because example 2.3 uses the full width and example 2.4 uses the
half-width, and one word for both would erase the difference between two of the
three orders.

a3 built the orders as one constructor over coefficient pairs, validating against
the paper's determinant condition, with the three named examples as instances. it
was built this way so that if the supervisors confirm a continuous path between
named examples is admissible, sampling it is a loop rather than a redesign.

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

while checking the benchmarks, the containment ND_lu inside ND_ls turned up, and
it is a theorem rather than an observation. the general form: if one phi's image is
a non-negative invertible linear map of another's, then dominance under the second
implies dominance under the first, so the first's non-dominated set sits inside the
second's. applying it to the paper's own coefficient matrices:

    the phi_lu efficient set sits inside the phi_ls one, exactly, for every problem
    the phi_cw efficient set sits inside the phi_ls one, exactly, for every problem
    phi_lu and phi_cw are nested in neither direction

this matters for what the study can claim. a measured difference between phi_ls
and either of the other two is partly a theorem and cannot be reported as evidence
that the order matters. **the pair that carries the real signal is phi_lu against
phi_cw.** the containments are recorded and sent to the supervisors, and nothing is
built on them until they answer.


## phase b, ground truth. deriving the answer the solvers are judged against

### b1, the derivation

b1 derived, on paper, what the efficient set of p1 actually is under each phi,
using the published optimality conditions of costa et al. and nothing invented.

it works because every image coordinate of p1 is a quadratic with a constant
second derivative matrix, so the optimality condition becomes a linear system and
the answer comes out as an explicit formula mapping weight vectors to points. the
three sets:

    phi_lu   a region bounded by two conic arcs, x_2 between 4/5 and 4/3
    phi_ls   the region 7 x_1 x_2 - 4 x_1 + 12 x_2 <= 16
    phi_cw   exactly the unit square

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
the choice costs.


## phase c, the solvers, and where the project learned the most

### c1, random search

not a competitor. slide 17 calls it the reference base, and it is the control.
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
generator that no seed reaches. the first fix, enlarging the archive so it never
overflows, was wrong and was reversed — it changed the leader pool from 200 to
6295, which changes what the algorithm does, and cost a factor of 16 in runtime.
the second fix seeds the truncation and changes nothing about the search.

c2 also established the single most reassuring fact in the project: pymoo's
non-domination and the project's agree exactly, on every problem and every phi.
there is one dominance relation from end to end.

c2-b measured a confound nobody had noticed: all the objective-space metrics move
with how many points a front carries, and the three solvers return very different
numbers. on one fixed front, igd improves by a factor of 6.5 between 25 and 610
rows from cardinality alone. any comparison across solvers has to be made at a
common front size.

### c3 through c3-f, the validation gate

the gate asks whether the solvers recover the sets b1 derived. it took six
sessions, and most of them consisted of the project being wrong and finding out.

**the first version asserted the wrong thing.** it measured the distance from the
solver's front to the derived set, and that distance cannot be small, for a reason
that is a theorem. under phi_ls and phi_cw one image column depends on a single
decision variable, so the sample point with the smallest value of that variable is
strictly best in that column and nothing can dominate it, whatever its other
coordinate is. it is non-dominated in any sample containing it, and it can sit
anywhere. no budget removes it; a bigger budget re-elects it. this was proved, and
its expected cost predicted to two decimals what was measured.

**the tolerance was derived wrongly.** it summed two terms where only one belongs.
correcting it made the gate tighter under two phi and looser under one, which is
what a tolerance that has not been tuned looks like.

**what the gate now says.** every part of every derived set is reached by random
search and by mopso, at every seed, under every phi. nsga-ii reaches it under
phi_lu and fails at three of five seeds under each of the other two. no solver
ever returns a point that beats the derivation. the failure is about how evenly
nsga-ii spreads its hundred points, not about whether the pipeline is correct, so
phase e is not blocked.

**the finding, and four sessions of trying to explain it.** at equal front size,
nsga-ii covers this efficient set worse than uniform random sampling does, under
phi_ls and phi_cw but not under phi_lu. five candidate explanations were tested and
excluded by measurement:

    that the non-dominated rank saturates and dominance stops selecting. it does
        saturate, under every phi, which is why it cannot explain a split between
        them.
    that far-away points waste front slots. they do, but not nearly enough.
    that the two phi align the same geometry differently to the operator's axes.
        the advantage travels with the run and not with the frame.
    that one map distorts more than another. impossible: phi_lu and phi_cw differ
        by a rotation and a uniform scaling, so pointwise they are the same map.
    that it is simply the size of the regions. the comparison already controls for
        that, and adding a second correction would have double-counted.

what remains is a decomposition. about half of the effect is that phi_lu's region
is thin and curved, which makes the uniform yardstick weaker there. the other half
is nsga-ii specifically, because random search shows no such deficit under any phi.
that half is unexplained, and it is recorded as unexplained.

**one thing found along the way that is about the framework rather than this
project.** the three phi images of any problem are fixed linear maps of one
another, with no problem parameter in them. the map between example 2.2 and
example 2.4 is a rotation times the square root of two, condition number exactly
one. the map to example 2.3 has condition number exactly the golden ratio squared.
this is offered to the supervisors for comment.

**and one thing that matters for the whole approach.** after generation three or
four, in every configuration the project runs, the non-dominated rank fills the
entire population and dominance stops deciding anything: nsga-ii selects on spread
alone for 46 of 50 generations. this is a cost of the transformation itself, since
turning m interval objectives into 2m real ones pushes even a two-objective problem
into the many-objective regime. it is the empirical form of the objection cui et
al. raise against transformation-based methods, arrived at with the project's own
numbers.


## what the project can say so far

    the three phi are the paper's named examples, verified with page and example
        numbers, and one that was not in the paper was removed.
    a constant-width uncertainty model makes the whole study vacuous, and the
        replacement was designed and measured rather than assumed.
    two of the three efficient sets are provably contained in the third, so the
        informative comparison is phi_lu against phi_cw.
    the efficient sets of the test problem are known in closed form under all
        three phi.
    the solvers recover them, random search and mopso completely, nsga-ii under
        one phi of three.
    nsga-ii has a coverage deficit that depends on phi, half of which is
        explained and half of which is not.
    the transformation costs dominance-based selection its pressure, everywhere.

none of these is the answer to the research question yet. that comes from phase e.


## where the project is, and what is left

phase a, b and c are complete and tagged. the current subpart is d2.

    d2, the decision-space metrics. hausdorff distance, coverage, overlap and
        cross-evaluation, all computed on decision vectors, which is the one space
        every phi shares. these are the metrics that answer the research question.
    e1, the tier 0 experiments. all three solvers, all three phi, all seeds, on
        the small problems, with the phi comparison made on random search because
        it is the only phi-neutral solver.
    e2, the same on zdt1 and dtlz2.
    e3, the synthesis. how much the efficient sets differ across phi, measured in
        decision space, and which phi is carried into part 2.

    then phase f, the portfolio application, which is where "which phi is better"
        becomes a well-posed question, because out-of-sample performance is a
        criterion external to the transformed problem and applies equally to every
        phi.

off the minimum path and built only if time allows: d1, the objective-space
metrics, which cannot compare phi against each other and carry two unresolved
problems of their own; and d3, the plotting and table code.

open with the supervisors: docs/supervisor_questions.md, twelve questions in four
parts, none of them blocking. the highest-value thing they can supply is not an
answer but a file: the pdf of costa et al. with its reference list would close
several open questions at once.
