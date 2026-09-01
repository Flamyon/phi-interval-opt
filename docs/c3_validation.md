# c3: the validation gate

subpart c3. output: this file and tests/test_validation.py. a gate, not a report:
it decides whether phase e starts. CONTEXT.md section 8 states the rule, "c3 gates
phase e. if the solvers do not recover the tier 0 sets, no tier 1 result is
trustworthy and none is produced."

**the gate does not pass.** twelve of the forty-five configurations exceed the
tolerance, all of them in one direction, and section 5 diagnoses them. phase e
does not start on this evidence. what follows states what was run, what the
tolerance is and where it comes from, which configurations failed and by how much,
and what the three checks the brief prescribes returned.


## 1. what was run

    problem            p1, docs/a1_uncertainty_model.md a1-b, rho = 1/4, delta = 1/8
    phi                lu, ls, cw, the three named examples of [1]
    solvers            random search c1, nsga-ii c2, mopso_cd c2 with c2-b's archive
    budget             5000 evaluations, pop_size 100 and n_gen 50 for the two
                       pymoo solvers, n_evals 5000 for random search. this is the
                       budget r-15 fixes for e1 and e2, and the gate runs at it
                       because a gate passed at a budget nothing else uses says
                       nothing about the runs that follow it
    seeds              11, 12, 13, 14, 15
    reference set      src/reference_fronts.py, efficient_set at 1000 points, at
                       both settings of include_singular_segments, per r-12
    measure            hausdorff distance in the decision space, both directions
                       reported separately, and never igd

recovery is measured in the decision space and never by igd, CONTEXT.md section 10
c3 and r-13: b2 samples through b1's weight map, whose density in objective space
is the parametrisation's and not the front's, and igd is an average over reference
points, so it weights a densely sampled region more heavily. hausdorff is a
maximum and is insensitive to that.

the two directions are not summaries of one another and are never averaged:

    solver to reference   is what was found correct. the largest distance from a
                          recovered point to the derived set. it fails when a
                          solver returns points that are not in the set.
    reference to solver   was what exists found. the largest distance from a point
                          of the derived set to the recovered set. it fails when a
                          solver misses part of the set.

p0 is treated separately, in section 6, as the smoke test b1 section 7.4 says it is.


## 2. the tolerance, and where it comes from

both sets in every comparison are finite samples of the same two-dimensional
region, and each carries its own resolution floor. the tolerance is the sum of the
two floors, per phi, with no free multiplier: every term is measured, at a size
fixed before the runs, on the region b1 section 2.4 derived.

    h_reference   the covering radius of the derived region by the 1000-point
                  reference sample. no distance to that sample can be read as
                  smaller than this, whatever the solver did.
    h_design      the covering radius of the derived region by 100 points drawn
                  uniformly from it, the mean over 20 draws at a stated seed. this
                  is what a perfect solver returning a design-sized front achieves
                  in the reference-to-solver direction, and it is a property of the
                  region and not of any solver. 100 is nsga-ii's population, the
                  smallest front the design fixes in advance rather than reads off
                  a run: mopso's archive bound is 200 and random search's count is
                  whatever is non-dominated.

both are measured against a uniform sample of the region, 20000 points by rejection
from the decision box, and not against b2's weight sample, which is dirichlet at
concentration 0.3 and carries the parametrisation's density rather than the
region's.

    phi   h_reference   h_design   tolerance
    lu    0.0383        0.1246     0.1629
    ls    0.1241        0.2174     0.3415
    cw    0.1377        0.1836     0.3213

the sum and not either floor alone: the forward direction is floored by
h_reference and the reverse by h_design, and a gate taking one floor for both
directions would leave no room for the other. the two are of the same order here,
0.04 to 0.14 against 0.12 to 0.22, so neither term is decoration.

the box is [-1/2, 3/2]^2, of side 2, so the tolerance is 8.1, 17.1 and 16.1 per
cent of the box side for phi_lu, phi_ls and phi_cw.

**this tolerance is coarse and the reason is structural, not a concession.** the
derived sets are two-dimensional regions of substantial area, b1 section 2.4:
X_cw is the unit square up to one edge and a quarter of the box's area, X_ls is
about three eighths of it and X_lu about a twelfth. a hundred-point front cannot cover a region of that size
to better than about 0.15 in a box of side 2, and that is what h_design measures.
a tighter gate on p1 is not available at this budget from any solver, and the
table in section 3 carries every margin so that a pass with no margin is visible
as one.

what the tolerance would be under a different reading of h_design, recorded so the
sensitivity is on the record rather than discovered later. taking the largest of
the 20 draws instead of their mean gives h_design 0.2384, 0.2880 and 0.2807 and
tolerances 0.2767, 0.4121 and 0.4184. three of the twelve failures survive that
tolerance and nine do not. the mean is used because the maximum over a finite
number of draws is itself a noisy statistic whose value moves with the draw count,
and because a floor is a typical resolution and not a worst case. **the gate's
verdict is sensitive to that choice within a factor of about 1.5, and this document
does not hide that.**

no tolerance is used anywhere in a dominance comparison. CONTEXT.md section 5 and
d-02 stand: every dominance test here is the ordinary pareto relation on doubles,
through src/random_search.py's non_dominated_indices and pymoo's own sorting. the
number above is a reporting tolerance on a distance and touches no order.


## 3. p1 recovery, per solver, per phi, per seed

columns F and T are include_singular_segments False and True. k_run is the front
cardinality the solver returned and k_ref the reference sample's, reported beside
every number per r-16. nothing is truncated to a common cardinality: r-16 is about
objective-space metrics that move with the number of rows, and hausdorff is a
maximum over two sets, so truncating either would discard real coverage.

    solver         phi  seed  k_run  k_ref   fwd F   fwd T   rev F   rev T   tol     verdict
    random_search lu     11    610   1000  0.1154  0.1154  0.0509  0.0509  0.1629  pass
    random_search lu     12    622   1000  0.0958  0.0958  0.0392  0.0392  0.1629  pass
    random_search lu     13    590   1000  0.0935  0.0935  0.0416  0.0416  0.1629  pass
    random_search lu     14    586   1000  0.1049  0.1049  0.0445  0.0445  0.1629  pass
    random_search lu     15    608   1000  0.0895  0.0895  0.0393  0.0393  0.1629  pass
    random_search ls     11   2220   1000  0.1796  0.1567  0.0477  0.0477  0.3415  pass
    random_search ls     12   2253   1000  0.3691  0.3691  0.0412  0.0412  0.3415  fail
    random_search ls     13   2256   1000  0.2222  0.1773  0.0414  0.0414  0.3415  pass
    random_search ls     14   2195   1000  0.2191  0.2191  0.0473  0.0473  0.3415  pass
    random_search ls     15   2182   1000  0.1883  0.1596  0.0391  0.0391  0.3415  pass
    random_search cw     11   1544   1000  0.4155  0.4155  0.0406  0.0406  0.3213  fail
    random_search cw     12   1528   1000  0.3691  0.3691  0.0449  0.0449  0.3213  fail
    random_search cw     13   1591   1000  0.2551  0.2307  0.0362  0.0362  0.3213  pass
    random_search cw     14   1501   1000  0.3071  0.2752  0.0373  0.0394  0.3213  pass
    random_search cw     15   1504   1000  0.4525  0.4249  0.0403  0.0403  0.3213  fail
    nsga2         lu     11    100   1000  0.1105  0.1105  0.1098  0.1098  0.1629  pass
    nsga2         lu     12    100   1000  0.1268  0.1268  0.1165  0.1165  0.1629  pass
    nsga2         lu     13    100   1000  0.1702  0.1702  0.1127  0.1127  0.1629  fail
    nsga2         lu     14    100   1000  0.1761  0.1761  0.1379  0.1379  0.1629  fail
    nsga2         lu     15    100   1000  0.1379  0.1379  0.1098  0.1098  0.1629  pass
    nsga2         ls     11    100   1000  0.2602  0.2602  0.3309  0.3309  0.3415  pass
    nsga2         ls     12    100   1000  0.2118  0.2112  0.2523  0.2523  0.3415  pass
    nsga2         ls     13    100   1000  0.2216  0.2216  0.3244  0.3244  0.3415  pass
    nsga2         ls     14    100   1000  0.2236  0.1874  0.2922  0.3093  0.3415  pass
    nsga2         ls     15    100   1000  0.3484  0.3483  0.2378  0.2378  0.3415  fail
    nsga2         cw     11    100   1000  0.2067  0.2068  0.2159  0.2159  0.3213  pass
    nsga2         cw     12    100   1000  0.1981  0.1985  0.2432  0.2432  0.3213  pass
    nsga2         cw     13    100   1000  0.2310  0.2310  0.2503  0.2503  0.3213  pass
    nsga2         cw     14    100   1000  0.2388  0.2388  0.2367  0.2367  0.3213  pass
    nsga2         cw     15    100   1000  0.1894  0.1894  0.2167  0.2167  0.3213  pass
    mopso         lu     11    200   1000  0.1785  0.1785  0.0918  0.0918  0.1629  fail
    mopso         lu     12    200   1000  0.1228  0.1228  0.0829  0.0829  0.1629  pass
    mopso         lu     13    200   1000  0.1766  0.1766  0.0688  0.0688  0.1629  fail
    mopso         lu     14    200   1000  0.1470  0.1470  0.0963  0.0963  0.1629  pass
    mopso         lu     15    200   1000  0.1447  0.1447  0.0787  0.0787  0.1629  pass
    mopso         ls     11    200   1000  0.5000  0.5000  0.1867  0.1867  0.3415  fail
    mopso         ls     12    200   1000  0.2444  0.2444  0.1397  0.1397  0.3415  pass
    mopso         ls     13    200   1000  0.2559  0.2568  0.2011  0.2011  0.3415  pass
    mopso         ls     14    200   1000  0.2772  0.2772  0.1702  0.1702  0.3415  pass
    mopso         ls     15    200   1000  0.2743  0.2743  0.1685  0.1685  0.3415  pass
    mopso         cw     11    200   1000  0.2224  0.2223  0.1098  0.1191  0.3213  pass
    mopso         cw     12    200   1000  0.2523  0.2523  0.1108  0.1172  0.3213  pass
    mopso         cw     13    200   1000  0.5301  0.5000  0.1304  0.1304  0.3213  fail
    mopso         cw     14    200   1000  0.1974  0.1974  0.1107  0.1107  0.3213  pass
    mopso         cw     15    200   1000  0.3247  0.3247  0.1226  0.1226  0.3213  fail

on both settings of include_singular_segments, per r-12. the flag is a no-op under
phi_lu, where b1 section 2.3 finds no singular ray at all, and the two columns are
identical there by construction. under phi_ls and phi_cw the two reference sets
differ in the 32 rows b2 puts on the segment, and the effect on the gate is small:
the forward distance falls by up to 0.0449 in eleven rows and rises by at most
0.0009 in three, and the reverse distance moves by at most 0.0171, in both
directions. **no verdict changes at either setting.** the two settings do not
disagree about the gate on p1, which is a narrower statement than r-12's igd
finding and does not touch it.


## 4. the verdict, stated as the brief asks

**every failure is in the solver-to-reference direction. the reference-to-solver
direction passes in all ninety measurements.** what the solvers miss of the derived
set is inside the tolerance everywhere; what they return that is not in the derived
set is not.

    solver          phi   seeds failing   worst excess over the tolerance
    random_search   lu    none             --
    random_search   ls    12               0.0276 at seed 12
    random_search   cw    11, 12, 15       0.1312 at seed 15
    nsga2           lu    13, 14           0.0132 at seed 14
    nsga2           ls    15               0.0069 at seed 15
    nsga2           cw    none             --
    mopso           lu    11, 13           0.0156 at seed 11
    mopso           ls    11               0.1585 at seed 11
    mopso           cw    13, 15           0.2088 at seed 13

twelve of forty-five configurations, spread over three solvers and three phi. no
solver passes every phi and no phi is passed by every solver. the two clean cells
are random search under phi_lu and nsga-ii under phi_cw.

the tightest passes are worth reading beside the failures, because a gate this
coarse can pass without margin: nsga-ii under phi_ls at seed 11 passes the reverse
direction by 0.0106 and at seed 13 by 0.0171, and mopso under phi_cw at seed 15
fails the forward direction by 0.0034. those three are inside the tolerance's own
sensitivity, section 2.


## 5. the diagnosis, in the order the brief prescribes

no tolerance was adjusted and no assertion was weakened. the three checks were run
on the twelve failing configurations, and a fourth was added because the first
three did not settle what the offending points are.

### 5.1 do the failing points sit on a box face

a metaheuristic can converge onto a face where a uniform draw does not, so this is
checked first. the point attaining the forward distance, per failing configuration:

    solver          phi  seed   the worst point         fwd     on a face   outside the region
    random_search   ls    12   (-0.00000, -0.36913)   0.3691   no            343 of 2253
    random_search   cw    11   ( 0.00026,  1.41550)   0.4155   no            279 of 1544
    random_search   cw    12   (-0.00000, -0.36913)   0.3691   no            296 of 1528
    random_search   cw    15   ( 1.42192, -0.00039)   0.4525   no            280 of 1504
    nsga2           lu    13   ( 0.48691,  0.70388)   0.1702   no             39 of 100
    nsga2           lu    14   ( 0.67076,  1.29396)   0.1761   no             51 of 100
    nsga2           ls    15   (-0.34835,  0.00015)   0.3484   no             40 of 100
    mopso           lu    11   ( 0.60782,  1.31494)   0.1785   no             98 of 200
    mopso           lu    13   ( 0.63934,  1.30693)   0.1766   no             78 of 200
    mopso           ls    11   (-0.50000,  0.00617)   0.5000   yes            49 of 200
    mopso           cw    13   ( 1.50000,  0.00026)   0.5301   yes            58 of 200
    mopso           cw    15   (-0.32474,  0.00030)   0.3247   no             70 of 200

**the box face is not the cause.** two of the twelve worst points are on a face,
both mopso's, and mopso puts 9 and 2 of its outside-the-region points there; every
other configuration puts none on a face at all.

what the table does show is a different pattern the check was not looking for.
**eight of the twelve worst points lie on one of the two lines x_1 = 0 and
x_2 = 0**, within 0.01 of it, and those are exactly the two singular lines b1
section 2.3 characterises and b1 section 2.6 leaves undecided. all eight sit on
the part of those lines b1 does not cover: at negative coordinates, where the
derived regions require x_1 >= 0 and x_2 >= 0, or beyond the region's extent, b2
sampling the segment over x_1 in [0, 4/3] under phi_ls and [0, 1] under phi_cw.
the four that are not on a line are all under phi_lu, which is the one phi with no
singular ray at all, b1 section 2.3, and they are ordinary interior points that
the search had not converged onto the set. the split is exactly along the phi that
has a singular ray and the phi that does not.

### 5.2 is the budget simply too small

each failing configuration re-run at four times the budget, 20000 evaluations,
same seed, everything else unchanged:

    solver          phi  seed   k_run   fwd      rev      tol      verdict
    random_search   ls    12     8506   0.3691   0.0213   0.3415   fail
    random_search   cw    11     5726   0.3616   0.0200   0.3213   fail
    random_search   cw    12     5742   0.3691   0.0192   0.3213   fail
    random_search   cw    15     5723   0.4525   0.0213   0.3213   fail
    nsga2           lu    13      100   0.1490   0.1122   0.1629   pass
    nsga2           lu    14      100   0.0963   0.1065   0.1629   pass
    nsga2           ls    15      100   0.2297   0.3315   0.3415   pass
    mopso           lu    11      200   0.1837   0.0802   0.1629   fail
    mopso           lu    13      200   0.1313   0.0842   0.1629   pass
    mopso           ls    11      200   0.2363   0.1644   0.3415   pass
    mopso           cw    13      200   0.4184   0.1256   0.3213   fail
    mopso           cw    15      200   0.2753   0.1322   0.3213   pass

**the answer differs by solver, which is itself the finding.**

    nsga-ii     all three failures are budget. four times the budget fixes every
                one, and the forward distance falls by 0.021 to 0.119.
    mopso       three of five are budget. two are not: lu seed 11 gets slightly
                worse, 0.1785 to 0.1837, and cw seed 13 improves to 0.4184 and
                still fails by 0.0971.
    random      none is budget. the forward distance is unchanged at seed 12 under
    search      both phi to four decimal places and at cw seed 15, and improves by
                0.054 at cw seed 11. quadrupling the sample does not help, and
                section 5.4 says why it cannot.

### 5.3 is it one seed or all of them

no (solver, phi) pair fails on all five seeds. the worst is random search under
phi_cw at three of five; every other failing pair is one or two of five. the
failures are seed-dependent, so they are not a systematic disagreement between the
solvers and b1's derivation, and a single-seed gate would have reported the
opposite verdict depending on which seed it drew. that is the case for the seed
list CONTEXT.md section 10 c2 requires, made concrete.

### 5.4 is the offending point efficient at all

the three prescribed checks leave the question of what the offending points are, so
one more was run: is the worst point of each failing configuration dominated by
some point of b2's reference front. if it is, the point is genuinely not efficient
and the derivation is not at fault. if it is not, the point is one no derived point
beats and the derivation's coverage is in question.

    ten of the twelve worst points are dominated by the reference front.

for those ten the reading is that the solver returned a point that is not
phi-efficient and that b1's set is not missing anything there. for random search
this is a structural property of the control and not a defect: the sampled point
with the smallest x_1^2 in the draw uniquely minimises the image coordinate
B_2^T f = rho x_1^2 + delta over the sample, so it is non-dominated within the
sample whatever its x_2 is, and likewise for the smallest x_2^2. the non-dominated
subset of any finite uniform draw therefore contains two points sitting on the two
lines at arbitrary positions along them, and a larger draw supplies a new such pair
rather than removing the old one. that is why 5.2 finds no budget effect for random
search, and it is a fact about filtering a finite sample rather than about phi.

    two are not dominated by any reference point:
        random_search, phi_cw, seed 15, at (1.42192, -0.00039)
        mopso,         phi_cw, seed 13, at (1.50000,  0.00026)

both are under phi_cw, both lie on the line x_2 = 0, and both lie beyond x_1 = 1,
which is where b1 section 2.4 puts the end of X_cw and where b2 stops sampling the
singular segment. these two points are **s-12 made concrete**: b1 section 2.6
records that on the singular rays the published conditions give weak optimality and
no optimality verdict either way, while a4's grid says part of each segment is
non-dominated. here two solver runs land on that segment past its sampled end, and
the derived set neither contains them nor dominates them. this is consistent with
tests/test_runners.py's test_no_solver_point_dominates_the_reference_front, which
passes: these points neither dominate nor are dominated by the reference front,
which is what an undecided region looks like from the outside.

**this is not a claim that b1 is wrong.** b1 closed what the published conditions
close and recorded what they do not, and this is the recorded gap being reached by
a solver rather than by a grid. it is raised as s-13 in PROGRESS.md and belongs in
the research chat, not in a patch to the derivation.


## 6. p0, the smoke test

b1 section 7.4: p0 is not a fixture. under phi_lu and phi_ls its optimal set is the
whole decision box, and under phi_cw it is the single point x = 0, which is the
published anchor itself. src/reference_fronts.py raises for p0 rather than
returning something that would pass for a front. what p0 supports is one check,
and this section runs that check and nothing more: **does a solver find the
published anchor x = 0.**

tolerance 0.02, on the same principle as p1's and in one dimension: the box is
[-1, 1], of length 2, and a design-sized front of 100 points resolves it to
2 / 100.

    solver          phi   k_run   nearest point to x = 0, over the five seeds
    random_search   lu     5000   0.000141 to 0.000371
    random_search   ls     5000   0.000141 to 0.000371
    random_search   cw        1   0.000141 to 0.000371
    nsga2           lu      100   0.000168 to 0.000324
    nsga2           ls      100   0.000168 to 0.000324
    nsga2           cw        1   0.000000 to 0.000026
    mopso           lu      200   0.000000
    mopso           ls      200   0.000000
    mopso           cw        1   0.000000

**all forty-five pass, by two orders of magnitude.**

and it must be said what that is worth. **under phi_lu and phi_ls the whole box is
optimal, b1 section 7.3, so every point of every front is an optimal solution and
finding the anchor is a weaker statement than it looks.** the k_run column shows it
directly: under phi_lu and phi_ls the recovered front is the solver's entire
output, 5000, 100 and 200 rows, because no point dominates any other; under phi_cw
it is one row, which is the anchor and the whole optimal set. the phi_cw column is
the only one where finding the anchor is finding the answer, and there nsga-ii
lands on x = 0 to within 2.6e-05 and mopso lands on it exactly. random search's
single row is its own closest draw to the origin, 1.4e-04 to 3.7e-04, which is the
resolution of a 5000-point uniform sample of [-1, 1] and not a property of the
search.

this section is a smoke test in the ordinary sense. it says the pipeline evaluates
p0, transforms it, filters it and returns something sane. it says nothing about
whether a solver can recover a set of positive extent, which is what section 3 is
for and where the gate fails.


## 7. the phi_lu points absent from the phi_ls set

CONTEXT.md section 10 c3 asks for one number that is not a recovery check: the
count of points in the phi_lu non-dominated set that are not in the phi_ls one,
over every tier 0 problem and every run the gate filters.
docs/a_close_containment.md corollary 1 makes ND_lu a subset of ND_ls exactly, in
real arithmetic, so this count is zero as an identity and any positive value is a
violation of an identity in doubles. it is reported as a diagnostic of the
pipeline's arithmetic and never as a result about phi.

    ninety runs filtered, forty-five on p1 and forty-five on p0, three solvers by
    three phi by five seeds by two problems.

    the count is zero in every one of them.

the set sizes behind that zero, which is what makes the zero worth reading. on p1
the phi_ls non-dominated set is the whole recovered front in every run, and the
phi_lu set inside it is a strict subset except under phi_lu itself:

    run filtered              n in ND_lu     n in ND_ls
    random_search under lu    586 to 622     the same
    random_search under ls    586 to 622     2182 to 2256
    random_search under cw    310 to 345     1501 to 1591
    nsga2 under lu            100            100
    nsga2 under ls            34 to 43       100
    nsga2 under cw            30 to 36       100
    mopso under lu            200            200
    mopso under ls            59 to 69       200
    mopso under cw            52 to 62       200

on p0 the two sets coincide in every run, at 5000, 100 and 200 rows under phi_lu
and phi_ls and at 1 row under phi_cw, which is b1 section 7.3's table appearing in
the pipeline: p0's optimal set is the whole box under both orders, so ND_lu and
ND_ls are both the whole front and the containment is an equality there.

r-11 records one measured violation of this containment, on dtlz2 at eps = 0.50,
one point of 1565. **no violation occurs anywhere on tier 0.** r-11 is not retired
by this: it is a tier 1 finding about a cancellation inside phi's own first
coordinate c - r, and tier 0's p1 has no point where the centre is 6e-17 against a
half-width of 0.5.


## 8. cardinality, per r-16

every number in sections 3, 6 and 7 carries the front cardinality it was computed
at. nothing is truncated to a common size, and that is deliberate rather than an
omission: r-16 is about objective-space metrics that move with the number of rows,
and hausdorff is a maximum over two sets. truncating a recovered set before
measuring a maximum discards real coverage and makes the measured distance a
property of the subsample. CONTEXT.md section 10 d1 now records that the r-16 rule
is for objective-space metrics only.

what the cardinality column does carry here is the reading of the two directions.
the three solvers return 586 to 2256, exactly 100, and at most 200 rows, and the
reverse direction tracks that ordering almost exactly: random search 0.036 to
0.051, mopso 0.069 to 0.201, nsga-ii 0.110 to 0.331. that is largely the
cardinality and not the search, which is why the reverse direction is read against
h_design, the floor a design-sized front cannot beat, and not against zero.


## 9. what this means for phase e

phase e does not start. the rule is CONTEXT.md section 8's and it is not
discretionary.

what the gate does establish, and it is not nothing:

    the reverse direction passes everywhere. every solver finds every part of
        every derived set to within the tolerance, at every seed, under every phi.
        the derivation, its encoding in b2 and the three solvers agree about where
        the efficient set is.
    p0's anchor is found by every solver under every phi, by two orders of
        magnitude.
    the containment diagnostic is zero in all ninety runs, so the transform, the
        route pairing, the column order and the dominance relation are consistent
        across the whole tier 0 pipeline.
    nsga-ii's three failures are budget and are fixed at 20000 evaluations.

what it does not establish, and what has to be settled before e1:

    whether the recovered sets are correct, in the sense that a solver returns
        only phi-efficient points. twelve of forty-five configurations return at
        least one point outside the derived set by more than the tolerance.
    what the two undecided points of section 5.4 are. that is s-12 and s-13 and
        it is a question for the research chat, since the published conditions are
        what leave the singular rays open.

three things are worth deciding there and none is decided here, because each is a
change to the design rather than a measurement:

    the budget. nsga-ii passes at 20000 and three of mopso's five failures are
        fixed there. r-15's plan puts e1's sweep at 5000 with a single 20000
        convergence check per problem; the gate's evidence is that 5000 is below
        nsga-ii's convergence on p1 and that 20000 is not enough for mopso under
        phi_cw.
    whether the forward direction should be measured against the derived set alone
        or against the derived set together with the singular segments extended to
        the box. that is s-12 again and it decides two of the twelve failures.
    whether random search's structural behaviour of section 5.4 should be reported
        as a property of the control rather than as a failure. it is not a
        convergence problem and no budget removes it.


## 10. open items this session raises

    s-13  two solver points under phi_cw, at (1.42192, -0.00039) and
          (1.50000, 0.00026), lie on the singular line x_2 = 0 beyond x_1 = 1 and
          are dominated by no point of the derived set. b1 section 2.6 leaves the
          singular rays undecided and b2 samples the segment only to x_1 = 1. what
          the phi_cw-optimal set is on that line past x_1 = 1 is not settled by
          the published conditions and is not settled here. it is a supervisors'
          question and it extends s-12 rather than repeating it: s-12 asks about
          the segment b1 bounds, s-13 about the line beyond that bound.

    r-17  the gate's verdict is sensitive to the tolerance within a factor of
          about 1.5, section 2: nine of the twelve failures disappear if h_design
          is read as the largest of twenty draws rather than their mean. the
          derived sets are two-dimensional and a design-sized front cannot resolve
          them finely, so no derivation of the tolerance from the region gives a
          sharp gate on p1.

    s-12 is touched and not resolved. r-12 is touched: the two settings of
        include_singular_segments do not disagree about the gate on p1, which is a
        narrower statement than r-12's igd finding and does not retire it.
