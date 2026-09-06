# phase c: what was established, and what it changed

session c-close, 2026-09-02. phase c of CONTEXT.md section 8, solvers, is
complete: subparts c1, c2 and c3, and the five addendum sessions c2-b, c3-b,
c3-c, c3-d, c3-e and c3-f.

who this is for. a reader who has not followed the sessions: the supervisors, and
the author in october writing the memoria. it repeats no derivation, runs no
measurement and states no new result. every claim below points at the session
deliverable that established it, and where this document and a deliverable could
differ the deliverable wins.

docs/project_narrative.md is one continuous account of phases a to c in plain
words; this document is the close-out of a single phase, organised by subpart,
and every claim in it points at the deliverable that established it. **where the
two could differ, this one wins.** part 1 as a whole is
docs/part1/part1_closing.md, which is the settled record and supersedes neither.

where the detail is, so this document does not become a second copy of it:

    docs/part1/c3_validation.md    the gate, its verdict, and sections 5 to 5.5,
                                   which are the whole of the coverage finding
                                   and of the five mechanisms excluded from it
    docs/verified.md               v-01 to v-56, each with its source and location
    docs/answered.md               answered questions and retired risks
    PROGRESS.md                    the open p-, s- and r-rows and the session log
    git log                        one commit per subpart, with its full session
                                   record
    docs/supervisor_questions.md   the open questions, written to be answered
    docs/part1/phase_a_summary.md  phase a's close-out, on the same model
    docs/part1/phase_b_summary.md  phase b's. phase b's own detail is b1, which
                                   is itself a document,
                                   docs/part1/b1_phi_efficient_sets.md


## 1. what phase c built

phase c is step 4 of the methodology of slide 18: solve the transformed problem.
it produces no result about phi and CONTEXT.md section 2 forbids part 1 from
ranking phi at all. what it produces is three solvers on one contract, and the
gate that decides whether anything they return can be believed.

**c1, src/random_search.py.** the "referencia base" of slide 17, and the module
whose importance is out of proportion to its size. it is the only point in the
design where the effect of the order is separable from the effect of the search.
sample_decision_space takes no phi, so a sample is a pure function of the box, the
budget and the seed, and filter_one_sample_under_every_phi draws one sample,
evaluates it once and filters it under each phi in turn. the three fronts then
differ only through phi. it also fixes the two things the rest of the phase is
built on: the return contract, one SearchResult per seed carrying the front as
(k, 2m) and the matching decision vectors as (k, n_vars), so that analysis code
treats all three solvers identically and CONTEXT.md section 5 step 5's rule that
every cross-phi metric lives in the decision space is available; and
non_dominated_indices, the project's one dominance relation, the ordinary pareto
relation on doubles with no rounding and no epsilon, per d-02.

**c2, src/runners.py.** nsga-ii and mopso_cd from pymoo on the transformed real
problem theorem 3.1 licenses solving, wrapped and not reimplemented: no operator,
survival rule, archive rule or dominance test of pymoo's is replaced, and the
transform, the record and the seed rule are c1's and are not defined a second
time. two decisions in it are worth naming. the budget is spent in evaluations
and not in generations, through MaximumFunctionCallTermination(pop_size * n_gen),
because under pymoo's generation termination mopso_cd spends one population more
than nsga-ii and a budget 10 per cent larger for one solver is not budget parity.
and the archive: pymoo 0.6.2's MultiObjectiveArchive truncates itself with a
generator that neither minimize(seed=s) nor numpy.random.seed reaches, so a mopso
run is not reproducible once the archive overflows, measured at five different
fronts from one seed. that is r-14.

**c2-b** fixes it by seeding the truncation, which changes the generator it draws
from and nothing else, so mopso runs at pymoo's own archive size of 200. setting
the archive to the whole evaluation budget removes the same symptom and is the
larger intervention, since the archive is mopso's leader pool and resizing it
changes what the search does and costs a factor of 16 in time at budget 20000.
the general rule CONTEXT.md section 11 carries with it is about the test and not
the fix: a test that guards a branch must demonstrate the branch was entered. a
reproducibility grid run at a budget where the archive never overflows asserts a
property it cannot observe and passes with the defect present, so c2-b's test
counts the truncation calls and fails if the count is zero.

**c3, tests/test_validation.py and docs/part1/c3_validation.md.** the gate. it runs all
three solvers on p1 under all three phi at the budget r-15 fixed, over five seeds
and both settings of include_singular_segments, ninety measurements, and compares
the recovered decision vectors against the sets b1 derived and b2 encodes. three
things fix what it may assert and how. the forward floor is a proposition with a
proof and not an observation, so the forward direction is reported and never
asserted. the quality measure is exact membership in b1 section 2.4's closed-form
region and not the count of points dominated by b2's reference front, because the
sampled measure moves with reference density, running from 9 per cent at 250
reference rows to 31 per cent at 16000 where the exact answer is 46. and the
tolerance is one resolution floor and not the sum of two, the reverse direction
being bounded by one of them alone.


## 2. the gate's verdict

**asserted, two directions.** that every part of the derived set is reached by the
solver, measured as the reverse hausdorff distance in decision space against a
tolerance that is the 0.95 quantile of the fill distance of a 100-point uniform
draw of the derived region, the quantile and the cardinality both fixed before the
study ran. and that no solver front point dominates any point of the derived set,
which is the claim that the derivation and the solvers agree about where the
efficient set is.

**the second passes in ninety of ninety.** no solver returns a point that beats
the analytic answer anywhere, on any phi, at any seed, under either setting of the
singular flag. that is the direction that would have indicted b1's derivation or
b2's encoding, and it does not.

**the first fails in twelve of ninety, and every one of the twelve is nsga-ii**,
three seeds under phi_ls and three under phi_cw, at both settings of the flag, and
none under phi_lu. the margins are small: the worst gap exceeds the tolerance by
0.005 to 0.039 in a box of side 2.

**why a failing gate did not block phase e.** CONTEXT.md section 8's rule is that
c3 gates phase e if the solvers do not recover the tier 0 sets. what the twelve
failures say is not that a solver failed to recover the set. nsga-ii's front lies
on and around the derived set, it returns no point that beats the derivation, and
its worst gap exceeds the resolution that a 100-point uniform draw of the same
region achieves at the 0.95 quantile. that is a statement about the uniformity of
one solver's spread at one cardinality, not about convergence, and it is reported
as a finding rather than repaired. the derivation, its encoding in b2 and all
three solvers agree about where the efficient set is; two of the three cover it to
within the derivation's own resolution and the third does not. **the twelve
failing tests are left failing on purpose and the count is recorded so that a
later session can see whether it moved.** c3-c refused both ways of making them
green, exempting nsga-ii from the assertion and marking the six configurations
xfail, docs/part1/c3_validation.md section 4.1.


## 3. the findings

each with its evidence, and each bounded by what it does not say.

### the protected extreme, proved

**docs/part1/c3_validation.md section 1, v-54.** under phi_cw the four image columns are
(c_1, r_1, c_2, r_2) and under phi_ls they are (c_1 - r_1, 2 r_1, c_2 - r_2,
2 r_2), so in both the fourth column is a r_2 with a > 0, and r_2 = rho x_1^2 +
delta is a strictly increasing function of |x_1| and of nothing else. in any
finite candidate set the member of strictly smallest |x_1| is therefore the strict
minimiser of that column, and domination requires being no worse in every column,
so **no member dominates it whatever its other coordinate is**. the same holds for
the member of smallest |x_2| through the second column. under phi_lu every column
moves with both variables and the hypothesis has nothing to stand on, which is
measured rather than proved: on 2000 random sets with two members planted at the
worst place the box allows, the argmin of |x_1| is dominated 1066 times under
phi_lu and 0 times under phi_ls and phi_cw.

**the corollary is what does the damage.** ordering by |x_1| ascending, the member
of j-th smallest |x_1| can be dominated only by one of the j - 1 members below it,
so the whole low-|x_1| tail is shielded and not only its first member, and that
tail's other coordinate ranges over the whole box while the derived region's does
not. this is why the forward hausdorff distance, solver to reference, has a floor
that no budget removes: for a uniform draw the elected point's x_2 lies outside
the derived region's range with probability exactly 1/2 and its expected overhang
is exactly 1/8, at every budget. measured over 200 draws at four sizes, the median
smallest |x_1| falls by a factor of four for every factor of four in n, 7.45e-04,
1.41e-04, 4.21e-05, 1.00e-05, while the mean overhang does not move at all,
0.1226, 0.1404, 0.1334, 0.1261.

what it does not say. it is not a defect of any solver: the proposition is about
an arbitrary finite set and holds for a uniform draw, for an nsga-ii population,
for a mopso archive and for the output of a solver that had converged perfectly
and then filtered its own evaluations. **the consequence for phase e is that the
forward hausdorff is reported and never asserted**, and that a reader who takes it
for a quality measure will rank the solvers by where their fronts' protected
extremes happened to fall. it is also why no monotone trend in budget is asserted
of any solver on this problem: a larger budget elects a new protected member of
smaller |x_1| at an x_2 no better placed.

### rank 1 saturates, and it is a cost of the transformation

**docs/part1/c3_validation.md section 5.1, c3-d.** nsga-ii sorts pop_size + offspring =
200 candidates a generation and keeps 100. if rank 1 alone holds at least 100 of
them then dominance never enters the selection and every survivor is chosen on
crowding distance. **it does, under every phi.** on p1 at the gate's budget rank 1
first reaches 100 at generation 4, 3 and 3 under phi_lu, phi_ls and phi_cw, at
every one of the five gate seeds, never falls back in any of them, and holds a
median of 167 to 173 of 200 over the last thirty generations. the survival sort
enumerates a single front where four or five exist, because pymoo stops the sort
once the ranked count reaches the number of survivors. **so for 46 or 47 of the 50
generations dominance decides nothing and nsga-ii is a spread maximiser.**

it holds on both tier 1 benchmarks. dtlz2_interval, six columns in twelve
variables, saturates at generation 3 or 4 exactly as p1 does and sits at a median
rank 1 of 135 to 170; zdt1_interval, four columns in thirty variables, is the one
configuration where dominance survives a while, first reaching 100 at generation
13 to 21 and holding a median of 100 to 144. what orders the three problems is not
the column count, since p1 also transforms to four columns and saturates as fast
as dtlz2 does; what tracks it is the non-dominated fraction of the transformed
image, 0.58, 0.79 and 0.55 on dtlz2 against 0.24, 0.52 and 0.47 on zdt1. three
problems is not enough to assert that and it is not asserted.

**this is a cost of the transformation and it should be read as one.** definition
2.1 of [1] takes m interval objectives to 2m real ones, v-05, so p1 and p0 are
4-objective real problems, zdt1_interval is 4 and dtlz2_interval is 6. the
non-dominated fraction of a sample rises with the number of objectives, and at 2m
objectives it rises far enough that a dominance-based survival operator has
nothing left to discriminate with. **that is the empirical form of the objection
[7] raises against transformation methods**, and this project can now state it as a
measurement on its own problems rather than as a citation. CONTEXT.md section 10
e2 requires every configuration in phase e to report the number.

what it does not say. it does not explain the coverage finding below: a mechanism
that fires equally under all three phi cannot produce a result that appears under
two of them and not the third, which is exactly why c3-d refuted its own
hypothesis. and it is not a statement that nsga-ii is misconfigured; it is a
statement about what 2m objectives do to any dominance-based selection.

### the exact linear relations between the three phi images

**docs/part1/c3_validation.md section 5.5, v-56, c3-f.** each phi is a constant linear
map of the endpoint pair, [1] section 2, so the three images of any decision set
are constant linear images of one another. writing g_lu, g_ls and g_cw for the
four image columns:

    g_lu = A g_cw    A = [[1,-1,0,0],[1,1,0,0],[0,0,1,-1],[0,0,1,1]]
    g_ls = B g_cw    B = [[1,-1,0,0],[0,2,0,0],[0,0,1,-1],[0,0,0,2]]

**A^T A = 2 I.** so A is sqrt(2) times an orthogonal matrix, all four of its
singular values are sqrt(2) and its condition number is exactly 1: the phi_lu
image is a rotation and a uniform scaling of the phi_cw image, and examples 2.2
and 2.4 of [1] present the same geometric object in two alignments. **B is not a
similarity.** B^T B is block diagonal with two copies of [[1,-1],[-1,5]], whose
eigenvalues are 3 +- sqrt 5, so B's singular values are sqrt(3 + sqrt 5) =
2.288246 and sqrt(3 - sqrt 5) = 0.874032, each twice, and its condition number is
exactly

    (1 + sqrt 5)^2 / 4 = 2.618034

the golden ratio squared. the map from the phi_ls image to the phi_lu image has
singular values exactly phi and 1/phi and the same condition number. verified to
0.000e+00 on 500 random points of the box and on all three region samples.

**A and B carry no parameter of p1.** they contain no rho, no delta, no box and no
objective: they are built from the coefficient pairs of examples 2.2, 2.3 and 2.4
alone. so the relations hold for every interval problem in the framework under
these three phi, and they are the one part of phase c's findings that is about
[1] rather than about p1 or about pymoo. one consequence is immediate and negative:
**no statement of the form "the phi_lu map distorts more than the phi_cw map" can
be true**, since pointwise they are the same map up to a similarity, and any
measurement that appears to show one is measuring the region it was averaged over.

what it does not say. it says nothing about the solution sets. dominance is not
preserved by an arbitrary invertible linear map, only by an entrywise non-negative
one, which is the separate criterion of docs/part1/a_close_containment.md and s-11; A
and B both have negative entries. the relations are about the geometry the
operator sees, not about which points are efficient.

### nsga-ii's coverage deficit, at its true scope

**docs/part1/c3_validation.md sections 5 and 5.2 to 5.5.** the finding, stated as
measured: on p1, at k = 100, nsga-ii's fill distance with respect to the derived
region sits **above the 85th percentile** of 1000 uniform 100-point draws of the
same region under phi_ls and phi_cw, worse than the uniform mean in all ten
measurements and at or above the 90th in eight of them, and at the **33rd to the
60th percentile** under phi_lu, which is where a uniform draw itself sits. mopso
shows the same tendency and weaker at its own cardinality of 200. this is what the
twelve gate failures are, and it is r-19.

**about half of it is not about nsga-ii.** random search is phi-neutral by
construction, and at matched cardinality, twenty uniform 100-row subsamples of
each random-search front read against the same k = 100 distribution, it has no
deficit under any phi: 13 to 29, 21 to 63 and 31 to 49, thirteen of the fifteen
below the median. in units of the uniform mean at the same k it nonetheless
carries **exactly half** the swing from phi_lu to each of the other two, +0.243 of
+0.483 and +0.244 of +0.485, the agreement of the two halves to three decimals
being a coincidence of two numbers and read as nothing. that half is region shape
acting on the comparator, and the closed-form areas make it concrete:

    |X_lu| = 0.310533    |X_ls| = 1.513401    |X_cw| = 1

against the box's area of 4 that is 7.8, 37.8 and 25.0 per cent, b1's twelfth,
three eighths and quarter. in units of sqrt(|R|/k), which removes region size, a
uniform draw covers X_lu 40 per cent worse for its area than it covers the other
two, because X_lu is a thin curved sliver between two conic boundaries and the
other two are fat. **so the comparator is itself region-dependent and is weakest
exactly under the phi where nsga-ii looks best.**

**the remaining half is nsga-ii's own and has no mechanism.** five candidates were
put to direct measurement and all five are excluded, and the exclusions are the
work:

    rank-1 saturation, c3-d, section 5.1. refuted because it fires under every
        phi, and a mechanism present under all three cannot produce a result that
        appears under two.
    effective cardinality, c3-e, section 5.2. re-reading each run's percentile at
        the number of front rows within 0.10 of R, which is section 3.3's own cut,
        buys 2 to 11 percentile points of a gap of 50 and leaves all ten failing
        measurements at or above the 74th percentile. only a cut that discards a
        third of the front moves the number, and a correction that has to remove a
        third of the rows is describing the front rather than correcting it.
    the pullback, c3-e, section 5.3. measured in the 2m image space with each
        column normalised by its range over the image of R, which is what crowding
        distance does, nsga-ii is at the 17th to 86th and 31st to 71st percentile
        under phi_ls and phi_cw and at the 0.1st to 4.9th under phi_lu. so it is
        not worse than a uniform draw at the thing it optimises under either
        failing phi, and the deficit is not that it optimises the wrong quantity
        badly.
    map anisotropy, c3-e, section 5.4. under the column-normalised jacobian phi_lu
        is the anisotropic one, median singular-value ratio 3.97 against 1.42 and
        1.45, which is the reverse of the ordering a distortion story needs, and no
        ratio anywhere exceeds 10. v-56 then makes the phi_lu against phi_cw part
        of that table an artefact of averaging over two different regions.
    region size, c3-f, section 5.5. excluded by the control rather than by
        argument: random search at matched cardinality on the same regions against
        the same comparator has no deficit under any phi, so a fixed-cardinality
        effect that any method would inherit is not what nsga-ii is showing.

what it does not say, and phase e must not let it be read as saying. it is not
that nsga-ii fails to converge, since no solver returns a point that beats the
derivation anywhere, ninety of ninety. it is not a result about phi: the sentence
that must not be written is that nsga-ii covers worse than random sampling because
of the order, when half the effect is the regions and the rest is confounded with
nsga-ii's own phi-conditional behaviour. and it is not general: it is one solver,
one problem, one cardinality, five seeds. **the residual half is recorded as
unexplained and no mechanism is offered for it.**


## 4. what phase c means for phase e

five things, none of them optional, and all of them now in CONTEXT.md section 10.

**the phi comparison is made on random search output.** this is c-close's
amendment to section 10 e3 and it follows from the control above. e3's headline
number is the phi_lu against phi_cw pair, those two being nested in neither
direction while ND_lu and ND_cw both sit inside ND_ls; that pair is measured
through filter_one_sample_under_every_phi, so one sample is filtered under each
order and the search is identical by construction. the population methods are
reported separately, as a question about how solvers behave under each order, with
the coverage deficit and the saturation stated beside them. a difference between
recovered sets measured on nsga-ii output is confounded with nsga-ii's own
phi-conditional behaviour and is not evidence about the order.

**every configuration reports the rank-1 size against the population size**,
section 10 e2, because a configuration where rank 1 fills the survivor slots is
one whose front is a spread and not a convergence result, and the number cannot be
predicted from the column count.

**the quality measure in decision space is exact membership in b1 section 2.4's
closed-form region**, reported as a fraction with the cardinality beside it. the
count of points dominated by a reference front is retired: its bias was measured
at a factor of three and it moves with reference density in the same run.

**the forward hausdorff is reported and never asserted**, with the note that it
carries the protected extreme; and no monotone trend in budget is asserted of any
solver on this problem, four times the budget buying nsga-ii nothing at all under
phi_ls and phi_cw.

**include_singular_segments has no default and its value belongs in every table**,
beside the seed and the point count, the two settings being two different
reference objects. and any recovery tolerance quoted anywhere is a quantile of a
measured fill-distance distribution at a stated cardinality, quoted with the
distribution.


## 5. what is verified, and what is still open

verified. docs/verified.md holds v-01 to v-56. phase c added v-48 to v-56; of
those, v-54, v-55 and v-56 are the proposition of section 1, the one-fill-distance
bound behind the corrected tolerance, and the linear relations above. v-56 is the
one row in the file that no test guards, c3-f having added nothing to the suite,
and it says so in place. anything not on that list is not established.

the test suite is the executable half of the record: 794 tests, of which 782 pass
and **twelve fail on purpose**, all of them
test_the_derived_set_is_reached_by_the_solver at nsga-ii under phi_ls and phi_cw.
they are the gate's stated verdict and are recorded here so that they are never
read as a regression.

open, and this document does not restate the rows. what phase d depends on is
listed in PROGRESS.md and named in docs/supervisor_questions.md; the short answer
is that **nothing blocks d2, the decision-space metrics, which is the only phase d
subpart on CONTEXT.md section 8's minimum presentable path.** what d1 would depend
on if it is built, r-12 and r-13 and s-12, is recorded there.

what phase c does not contain, stated so that no reader looks for it. no result
about phi: c1's isolation makes the comparison possible and phase e makes it. no
tier 1 solver run beyond the six diagnostic configurations of section 5.1, which
measured saturation and nothing else. no metric module, no plot and no results/
directory, those being phases d and e. and no mechanism for the residual half of
r-19.
