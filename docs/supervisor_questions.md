# questions for the supervisors

session c-close, 2026-09-02, at the end of phase c. this is the accumulated list,
written to be answered in one sitting rather than one at a time.

**none of these blocks work.** every one carries the assumption the project is
proceeding on, and the project has proceeded. what an answer changes is stated
under each. where an answer agrees with the assumption, the row retires and
nothing is rebuilt.

how to read a row. **the question** is what is being asked. **working assumption**
is what the code and the documents currently do. **what depends on it** is the
concrete consequence of a different answer, in subparts and files. **where it is
written up** points at the deliverable that discusses it, so that no answer has to
be given from this page alone.

the papers are in CONTEXT.md section 3's numbering, which is yours:

    [1] costa, osuna-gomez and chalco-cano, "new preference order relationships
        and their application to multiobjective interval and fuzzy interval
        optimization problems", fuzzy sets and systems 477 (2024) 108812.
    [2] zitzler, deb and thiele, evolutionary computation 8(2) (2000) 173-195.
    [3] deb, thiele, laumanns and zitzler, congress on evolutionary computation
        2002.

the three phi are [1]'s examples 2.2, 2.3 and 2.4, written phi_lu, phi_ls and
phi_cw throughout:

    phi_lu   lambda = (1, 0),     beta = (0, 1)       (f_l, f_u)
    phi_ls   lambda = (1, 0),     beta = (-1, 1)      (f_l, f_u - f_l), full width
    phi_cw   lambda = (1/2, 1/2), beta = (-1/2, 1/2)  (centre, half-width)


## part a. the two that change what the study reports

these two are the ones worth spending the most time on. everything else on this
page is a reading or a design choice; these two change a number in the memoria.

### s-11. the containment criterion, and the two containments it gives

**the question, in three parts.**

first, **is the criterion correct?** the claim is: if phi_B = M phi_A with M
entrywise non-negative and invertible, then phi_A-dominance implies
phi_B-dominance, and therefore the phi_B non-dominated set is contained in the
phi_A one. the argument is two lines. non-negativity preserves every weak
inequality under the map, so a point no worse in every phi_A column is no worse in
every phi_B column; invertibility preserves the strict one, since a strict
improvement cannot map to equality without M being singular.

second, **are both containments correct?** applying the criterion per objective,
on the image of one interval objective:

    from phi_ls to phi_lu    M = [[1, 0], [1, 1]]        non-negative
    from phi_ls to phi_cw    M = [[1, 1/2], [0, 1/2]]    non-negative

so **ND_lu and ND_cw both sit inside ND_ls**, exactly and for every problem. and
no map into phi_ls, and no map between phi_lu and phi_cw, is entrywise
non-negative: from phi_cw to phi_lu the block is [[1, -1], [1, 1]] and from phi_cw
to phi_ls it is [[1, -1], [0, 2]]. so those two are nested in neither direction,
which is why they are the pair the study's headline comparison uses.

third, **is any of it published?** the phi_lu case is the interval-space analogue
of proposition 5.1 of [1], which the project found nowhere in sections 2 or 3, the
paper stating it for the fuzzy problems only. [1] cites its own [26] for
LS-convexity and LS-Pareto, so [26] is where it would sit, with [9] and [31] the
other candidates. the phi_cw case and the criterion itself have no candidate
location: the project found [1] relating example 2.4's solution set to nothing,
and the criterion is about the class rather than about a pair of named examples.
**this third part cannot be settled inside the project**, because the pdf of [1]
is not in the repository and the extracted text lacks its reference list, which is
r-03.

**working assumption.** the project does not build on any of it. b1 derives from
[1]'s own results and does not shorten a derivation with the containment, no test
asserts the phi_cw containment, and the phase e synthesis reports the phi_ls pairs
as checks and never as independent findings. it is recorded, not used.

**what depends on it.** one instruction in CONTEXT.md section 10 e3. because both
containments hold, one direction of every coverage and overlap statistic on the
phi_ls against phi_lu pair and on the phi_ls against phi_cw pair is fixed before a
solver is run, so a difference measured there is in part a theorem and must not be
reported as evidence that the efficient set is sensitive to the order. **if the
criterion is refuted, that instruction is removed and all three pairs are reported
alike.** nothing else changes: two consequences already hold whichever way it is
answered, the gate reporting the containment's violation count as numerical noise
and the tier 1 separation report printing the same counts.

one measured caveat, which is r-11 and is arithmetic and not mathematics. the
nesting is exact in real arithmetic and fails by rounding in doubles, c + r and
(c - r) + 2r not being the same double. one violation was measured, dtlz2 at
eps = 0.50, one point of 1565, where the centre is 6.1e-17 against a half-width of
0.5. the decision-space tables name the artefact rather than reporting it.

**where it is written up.** docs/a_close_containment.md; v-24, v-25, v-26, v-46,
v-47.

### s-12. the singular segments: undecided, and it is your call

**the question.** for phi_ls and phi_cw, b1's derivation has two singular weight
rays, where the stationarity system degenerates. on those rays the published
conditions give **weak optimality and no optimality verdict either way**, so the
status of

    {(x_1, 0) : 0 < x_1 <= 4/3}   under phi_ls
    {(x_1, 0) : 0 < x_1 <= 1}     under phi_cw

is undecided. **are those points optimal solutions for (1MIOP_phi)?** three
published routes were tried and none applies. example 3.8 statement 3 does not
apply there, the scalar problem having a line of minimisers rather than one.
example 3.8 statement 2 and example 3.9 statement 3 both need every weight
strictly positive, which the singular rays do not have. and no regular weight
reaches the interior of the segments, x_2(w) = 0 forcing w_1 = w_3 = 0. phi_lu has
no singular ray at all, so the question does not arise there.

**every measurement the project has made says they are non-dominated**: a4's
61 x 61 grid, and b2's dense random sample of 50000 box points at three seeds,
where 0 of 2000 front points are dominated under either setting. the published
conditions say only that they are weakly optimal. so the measurement and the
theory do not disagree; the theory is silent.

**working assumption.** b2 does not choose and does not patch. efficient_set and
reference_front take include_singular_segments **with no default**, so a caller
states which of the two sets it wants, and the value is recorded in every table
beside the seed and the point count. the two settings are two different reference
objects and a metric computed against one is not comparable with a metric computed
against the other.

**what depends on it.** the size of the effect was measured so that the question
can be priced rather than argued. holding the region sample fixed and adding the
segment on top, the igd of a fixed test front moves by -0.63 to +5.36 per cent at
1000 reference points, -0.27 to +2.62 per cent at 5000 and -0.11 to +1.35 per cent
at 20000. **so the choice cannot flip a comparison that is not already inside a few
per cent, and it can flip one that is.** that is r-12. the gate is unaffected: it
measures recovery by hausdorff distance in decision space, which is a maximum and
insensitive to reference density, and the two settings move its asserted number by
at most 0.0171 on p1 and change no verdict.

**a related question is already closed and is not being asked.** s-13 asked what
the phi_cw-optimal set is past x_1 = 1, after two solver points on the line
x_2 = 0 beyond x_1 = 1 came back dominated by no point of b2's 1000-row reference
front. that was a statement about b2's sample and not about the derived set: b2's
weight sample is dirichlet at concentration 0.3 and reaches the region's extreme
values only in the limit, so no reference row sat close enough to beat them, while
the derived set itself does. checked against b1's closed form in exact arithmetic,
(0.999, 0.0001) is in X_cw, is off the undecided segment since its x_2 is strictly
positive, and dominates both points in all four columns. it is closed by the
derivation, is carried as a test, and **s-12 is untouched by it**: s-12 asks about
the segment itself, where the published conditions give no verdict, and the s-13
witness bears on neither.

**where it is written up.** docs/b1_phi_efficient_sets.md section 2.6, the module
comment of src/reference_fronts.py, and docs/answered.md for the closed s-13.


## part b. readings of [1] the project has taken a position on

each of these is a place where the paper admits two readings and the project chose
one, recorded the choice, and proceeded. a confirmation retires the row.

### s-01. the subscripts in (16)

**the question.** (16) of [1] is inconsistent in the w subscripts on the beta
terms: the expanded line carries w_2i and the collected line w_2i-1. which is
intended?

**working assumption.** the project does not cite (16). b1 expands (15) from the
definitions of Lambda_i and B_i instead.

**what depends on it.** nothing, until the memoria wants to print (16). b1 has run
and the assumption held.

**where it is written up.** docs/a0_framework.md c14.

### s-02. the weight condition in example 3.9

**the question.** example 3.9's "w_i >= 0 not equal zero for all i": does it mean
nonnegative and not all zero, or strictly positive?

**working assumption.** the former. under the strict reading, statement 3 of the
same example is redundant.

**what depends on it.** the row now carries a witness and not only the redundancy
argument. b1 found a point of p1, **x = (4/3, 1) under phi_lu**, that example 3.8
statement 3 certifies as an optimal and hence weak optimal solution, and at which
(15) holds for w = (0, 0, 1, 0) and for no strictly positive w. **so the strict
reading makes example 3.9 statement 1 false there.** no b1 result depends on the
answer: every optimality conclusion is drawn from example 3.8, whose weight
condition is unambiguous, and the strict reading would cost only the necessity
direction.

**where it is written up.** docs/a0_framework.md c14 and a-2,
docs/b1_phi_efficient_sets.md section 6.

### s-03. which efficiency does theorem 3.1 mean

**the question.** [1]'s efficient solution for (12) requires no strictness, which
is strong efficiency and not definition 3.1(2). which does theorem 3.1 mean?

**working assumption.** the usual pareto definition, as in definition 3.1(2) and
as pymoo implements it.

**what depends on it.** the two differ only when two decision vectors share an
image, so the choice is recorded in b2 rather than assumed away.

**where it is written up.** docs/a0_framework.md.

### s-05. does the exclusion of section 5 of [1] stand

**the question.** CONTEXT.md section 9 excludes sections 4 and 5 of [1], the fuzzy
branch. but section 5 holds proposition 5.1, which relates two of the three phi
this project implements. does the exclusion stand?

**working assumption.** it stands for implementation. proposition 5.1 is a
prediction to be checked, never a result the project asserts, and no interval
analogue is derived from it. the analogue the project does have is s-11's
criterion, derived independently.

**what depends on it.** wanted before the phase e synthesis touches section 5. the
project has read proposition 5.1 and transcribed it, v-24: for the fuzzy problems,
optimal under example 2.2 implies optimal under example 2.3, with no convexity, no
differentiability and no converse.

**where it is written up.** docs/a0_framework.md and its a0-b addendum; v-24,
v-26.

### s-06. is the centre-radius form of phi the working form, or an implementation note

**the question.** computing the second image coordinate as f_u - f_l loses it at
constant or near-zero width. the project built both routes. **should the memoria
present the centre-radius form as the working form of phi, or keep it as an
implementation note?**

**working assumption.** both routes exist and the presentation question is open.
make_phi keeps [1]'s specified (f_l, f_u) signature and is unchanged;
make_phi_of_centre_radius is the same automorphism in the other coordinates, and a
problem declares which route applies to it. the mathematics is unchanged: the
composite is phi o M with M = [[1, -1], [1, 1]] and determinant 2 det phi, so it
vanishes exactly when [1]'s admissibility condition fails and never otherwise, and
no order, efficient set or result depends on the route.

**what depends on it.** presentation only; the row is no longer blocking. the
measurement behind it is worth one line because it is the reason the project
carries two routes at all: on p1's grid, p1's r_1 depends on x_2 alone and takes
exactly 46 distinct values, and the endpoint route gives it **210** while the
centre-radius route gives it 46. an order built on a column is built on that
column's ties, and the subtraction shatters them.

**where it is written up.** docs/a4b_dominance_tolerance.md part 3, CONTEXT.md
section 4, v-41 and v-42.


## part c. design choices wanting a ruling

### s-07. should the degeneracy check run on the slice as well as the box

**the question.** the step 1 degeneracy check runs on a uniform sample of the
decision box. zdt1 with half-width eps*x_n passes it while phi_cw reproduces the
crisp efficient set exactly on the slice where that set lives. should the check
also run on the slice?

**working assumption.** yes, and the tier 1 forms were chosen against the stronger
check. it is built: the problem modules re-grid the union bounding box of the
three efficient sets and assert separation there.

**what depends on it.** this is the finding with the most consequence in phase a
and it is a finding about a diagnostic rather than about a problem. on the slice
at eps = 0.25, phi_cw's efficient set is the crisp efficient set exactly, 81 of
6561, while phi_lu and phi_ls are the whole slice. **the uniform sample reported
separation where the efficient sets coincide**, because a uniform sample of a
30-dimensional box contains essentially nothing near the efficient set. the
residual is r-09: the rule was derived from two benchmarks and one tier 0 design,
so it is a working rule and every new problem, including the portfolio returns of
part 2, runs the full diagnostic before use.

**where it is written up.** docs/a1_uncertainty_model.md part 2 and a1-b.

### s-08. accept p1's two-dimensional efficient set

**the question.** p1's phi-efficient set is a two-dimensional band and not a
curve, and a curve and three distinct phi are not both available at two variables
and two interval objectives. accept the band, or change p1's shape?

**working assumption.** accept the band. it gives spread and coverage two
dimensions of structure rather than one.

**what depends on it.** it is answered as assumed and b1 delivered what was
predicted: the stationarity map is an explicit rational function of the weight
vector for all three phi, and the band has a closed-form boundary, two conic arcs
for phi_lu, one for phi_ls and none for phi_cw, whose set is the unit square minus
one open edge. **the row can retire on your acknowledgement.** it is also what
makes the coverage finding of part e below measurable at all, since covering a
two-dimensional region is a question a hundred points can answer badly.

**where it is written up.** docs/a1_uncertainty_model.md part 3 and a1-b section
3, docs/b1_phi_efficient_sets.md sections 2.2 and 2.4.

### s-09. one absolute half-width per objective, or scaled

**the question.** tier 1 uses one absolute half-width for every objective, which
on zdt1 is large relative to f_1 and small relative to f_2. scale it per
objective?

**working assumption.** keep the common absolute width as the closest reading of
slide 19, and record the asymmetry in every tier 1 table.

**what depends on it.** a one-line change in src/problems_tier1.py if the answer
differs, plus a rerun of tier 1.

**where it is written up.** docs/a1_uncertainty_model.md part 4.

### s-10. keep the double seeding

**the question.** CONTEXT.md section 10 c2 justifies seeding pymoo twice by its
independent generator, but the project measured the opposite: minimize(seed=s)
alone is bit-reproducible, v-38. keep the double seeding?

**working assumption.** keep it. c1's own uniform sampling does need a seeded
global state, so the instruction is right though its stated reason is inverted,
and CONTEXT.md was not edited because the licence to correct it is against a
paper and a project diagnostic is not a paper.

**what depends on it.** nothing; the global seeding costs nothing. the reason to
keep it rather than tidy it is r-14, measured in c2: pymoo 0.6.2 **does** reach a
generator that neither seeding call controls, in the archive truncation of any
algorithm holding an archive, so removing either call on the strength of one
measurement is not warranted.

**where it is written up.** docs/verified.md v-38 and v-48.


## part d. one wording question

### s-04. should CONTEXT.md record that [1] does compare two phi

**the question.** CONTEXT.md section 2 forbids part 1 from ranking phi. [1]'s own
conclusion does compare two phi, under a quasilinear-space criterion. should
section 2 record that?

**working assumption.** no amendment. the rule that part 1 may not rank phi is
about what **this study** can measure empirically; [1]'s criterion is structural,
not empirical, and the two are not in conflict.

**what depends on it.** wording only.

**where it is written up.** docs/verified.md v-23.


## part e. one result offered for comment, not a question

this is not a question and needs no answer. it is put here because it is the one
finding of phase c that is about [1]'s framework rather than about this project's
problems or about the solver library, and because it may be of interest
independently of this study.

**v-56, the exact linear relations between the three phi images.** each phi is a
constant linear map of the endpoint pair, so the three images of any decision set
are constant linear images of one another. writing g for the 2m image columns:

    g_lu = A g_cw    A = [[1,-1,0,0],[1,1,0,0],[0,0,1,-1],[0,0,1,1]]
    g_ls = B g_cw    B = [[1,-1,0,0],[0,2,0,0],[0,0,1,-1],[0,0,0,2]]

**A^T A = 2 I.** A is sqrt(2) times an orthogonal matrix, all four singular values
sqrt(2), condition number exactly 1. so **examples 2.2 and 2.4 present the same
geometric object in two alignments**, differing by a rotation and a uniform
scaling and nothing else. **B is not a similarity**: B^T B is block diagonal with
two copies of [[1,-1],[-1,5]], eigenvalues 3 +- sqrt 5, so B's singular values are
sqrt(3 + sqrt 5) = 2.288246 and sqrt(3 - sqrt 5) = 0.874032, each twice, and its
condition number is exactly

    (1 + sqrt 5)^2 / 4 = 2.618034

the golden ratio squared. the map from the phi_ls image to the phi_lu image has
singular values exactly the golden ratio and its reciprocal, and the same
condition number.

**A and B carry no parameter of any problem.** they are built from the coefficient
pairs of examples 2.2, 2.3 and 2.4 alone, with no rho, no delta, no box and no
objective in them, so the relations hold for every interval problem in the
framework under these three phi.

two remarks, and both are consistency checks rather than new claims. first, this
does **not** contradict s-11: dominance is preserved by an entrywise non-negative
map, not by an arbitrary invertible one, and the per-objective blocks of A and B
both carry a negative entry, which is exactly why phi_lu and phi_cw are nested in
neither direction while both sit inside phi_ls. the two facts describe different
things, one the geometry the solver's operators see and the other which points are
efficient. second, it forces a negative statement that the project needed:
**no claim of the form "the phi_lu map distorts more than the phi_cw map" can be
true**, since pointwise they are the same map up to a similarity, so any
measurement appearing to show one is measuring the region it was averaged over and
not the map.

it is verified to 0.000e+00 on 500 random points and on all three region samples.
**no test in the suite guards it**, the session that established it having added
no assertions, and docs/verified.md says so in its row.

**where it is written up.** docs/c3_validation.md section 5.5, "where phi_ls
sits"; docs/verified.md v-56.


## what is not on this page

questions the papers answer rather than you: p-01, p-02, p-04, p-05 and p-06 in
PROGRESS.md section 5. all five need a document the repository does not have, and
three of them would be closed by the pdf of [1] with its reference list, which is
r-03. **if any of [1]'s pdf, [26], [9], [31], [10], [7] or [8] can be supplied,
that closes more of the project's open questions than any answer on this page**,
including the third part of s-11.
