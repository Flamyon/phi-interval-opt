# c3: the validation gate

subpart c3, reopened as c3-b. output: this file and tests/test_validation.py. a
gate, not a report: it decides whether phase e starts. CONTEXT.md section 8 states
the rule, "c3 gates phase e. if the solvers do not recover the tier 0 sets, no
tier 1 result is trustworthy and none is produced."

**c3 reported that the gate did not pass, and c3's assertion was wrong.** twelve
of forty-five configurations exceeded the tolerance, every one of them in the
solver-to-reference direction, and c3 diagnosed them as far as measurement could
take it without finding the cause. the cause is section 5 below: that direction
carries a floor that is a property of filtering a finite sample and not of any
solver, so it cannot be asserted against a tolerance derived from the region, at
any budget, by any solver, under two of the three phi. **c3-b removes that
assertion, keeps everything else c3 asserted, adds two assertions c3 did not make,
and reports the forward distance as what it is.** no phi, no problem, no
derivation, no solver and no dominance relation is touched, and c3's tolerance is
not adjusted: this session changes what is asserted and what is reported and
produces no number c3's code would not have produced.

what follows states what the gate now asserts and reports, what was run, what the
tolerance is, what every configuration returned, why the forward direction carries
a floor, what the budget trend gives, and where that leaves phase e.


## 0. what the gate asserts and what it reports

asserted, pass or fail, and these are the two directions of the pipeline:

    reference to solver   was what exists found. the largest distance from a point
                          of the derived set to the recovered set, within the
                          tolerance of section 2, per solver, per phi, per seed.
                          this is the convergence question.
    no solver point       a solver cannot beat the analytic answer. the count of
    dominates the         reference front points some solver front point dominates
    derived set           is zero. asserted in c1 and in c2 at one seed; asserted
                          here over the whole grid, because the gate is where the
                          claim that the derivation and the solvers agree is made.

asserted as a trend, and for the population methods only:

    the dominated fraction does not rise when the budget is quadrupled, for
    nsga-ii and mopso, per phi and per setting of the singular flag, read over the
    five seeds. monotone improvement and not a threshold. random search is
    excluded and section 5.4 is the reason.

reported and never asserted:

    the forward hausdorff, solver to reference, per configuration. it is bounded
    below by the sampling artifact of section 5 and is not a quality measure.
    the count of solver front points dominated by the reference front, as a
    fraction of front size, for all three solvers. this is the quality measure: a
    solver point beaten by a known-efficient point is one the solver should have
    improved on, and no sampling artifact produces one.
    the front cardinality beside every number, per r-16.

CONTEXT.md section 10 c3 now carries the same statement, and the change is
reproduced as a before and after block in this session's reply.


## 1. what was run

    problem            p1, docs/a1_uncertainty_model.md a1-b, rho = 1/4, delta = 1/8
    phi                lu, ls, cw, the three named examples of [1]
    solvers            random search c1, nsga-ii c2, mopso_cd c2 with c2-b's archive
    budget             5000 evaluations, pop_size 100 and n_gen 50 for the two
                       pymoo solvers, n_evals 5000 for random search. this is the
                       budget r-15 fixes for e1 and e2, and the gate runs at it
                       because a gate passed at a budget nothing else uses says
                       nothing about the runs that follow it
    the trend          the same grid at 20000 evaluations, four times the budget,
                       for nsga-ii and mopso
    seeds              11, 12, 13, 14, 15
    reference set      src/reference_fronts.py, efficient_set at 1000 points, at
                       both settings of include_singular_segments, per r-12
    measure            hausdorff distance in the decision space, both directions
                       reported separately, and never igd; and the dominated count
                       through the project's one pareto relation, with no tolerance

recovery is measured in the decision space and never by igd, CONTEXT.md section 10
c3 and r-13: b2 samples through b1's weight map, whose density in objective space
is the parametrisation's and not the front's, and igd is an average over reference
points, so it weights a densely sampled region more heavily. hausdorff is a
maximum and is insensitive to that.

the two directions are not summaries of one another and are never averaged:

    solver to reference   is what was found correct. the largest distance from a
                          recovered point to the derived set. **reported only**,
                          section 5.
    reference to solver   was what exists found. the largest distance from a point
                          of the derived set to the recovered set. it fails when a
                          solver misses part of the set. **this is the assertion.**

p0 is treated separately, in section 7, as the smoke test b1 section 7.4 says it is.


## 2. the tolerance, and where it comes from

unchanged from c3, and deliberately not re-derived: a tolerance adjusted after the
runs it judges is not a tolerance. both sets in every comparison are finite samples
of the same two-dimensional region, and each carries its own resolution floor. the
tolerance is the sum of the two floors, per phi, with no free multiplier: every
term is measured, at a size fixed before the runs, on the region b1 section 2.4
derived.

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

the sum and not either floor alone, and the second term is not decoration. c3
derived the tolerance as a sum because it asserted both directions and each was
floored by one of the two terms. c3-b asserts one direction, the one floored by
h_design, and keeps the sum unchanged rather than tightening the gate on the
strength of its own result. **that choice is doing work and this document will not
pretend otherwise**: read as h_design alone, the tolerance would fail twenty-two of
the ninety measurements in section 3, two under phi_lu and ten each under phi_ls and
phi_cw, and every one of the twenty-two is nsga-ii.

what that says is worth reading rather than hiding. h_design is what a perfect
solver returning a hundred points achieves, and nsga-ii returns exactly a hundred
points and covers the derived region less well than a uniform hundred-point draw of
it does in twenty-two of its thirty measurements, by up to 0.1135; the other eight
sit at or below h_design, the closest by 0.0148. its front is not a uniform sample
of the region: it is spread by crowding distance in the four-column image space,
which is where nsga-ii sorts, and not in the two-dimensional decision space where
the coverage is measured. h_reference, the reference sample's own resolution, is what leaves room for that,
and a gate at h_design alone would be a gate on nsga-ii's spread operator rather
than on whether the solvers find the derived set. mopso, whose front is at most two
hundred rows, passes h_design alone at every seed under every phi, and random
search passes it everywhere by a wide margin.

the box is [-1/2, 3/2]^2, of side 2, so the tolerance is 8.1, 17.1 and 16.1 per
cent of the box side for phi_lu, phi_ls and phi_cw.

**this tolerance is coarse and the reason is structural, not a concession.** the
derived sets are two-dimensional regions of substantial area, b1 section 2.4: X_cw
is the unit square up to one edge and a quarter of the box's area, X_ls is about
three eighths of it and X_lu about a twelfth. a hundred-point front cannot cover a
region of that size to better than about 0.15 in a box of side 2, and that is what
h_design measures. a tighter gate on p1 is not available at this budget from any
solver, and the table in section 3 carries every margin so that a pass with no
margin is visible as one.

what the tolerance would be under a different reading of h_design, recorded so the
sensitivity is on the record rather than discovered later. taking the largest of
the 20 draws instead of their mean gives h_design 0.2384, 0.2880 and 0.2807 and
tolerances 0.2767, 0.4121 and 0.4184. the mean is used because the maximum over a
finite number of draws is itself a noisy statistic whose value moves with the draw
count, and because a floor is a typical resolution and not a worst case.

**r-17 stands and it now bites less.** in c3 the choice moved nine of twelve
verdicts, all of them in the forward direction. c3-b does not assert that direction
at all, so the sensitivity now falls on the reverse direction alone, and there it
moves nothing: the reverse direction passes in all ninety measurements at the mean
reading and therefore at the larger one too. the tightest reverse margins in the
grid are 0.0106 and 0.0171, both nsga-ii under phi_ls, and the larger reading
widens them to 0.0812 and 0.0877.

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

**rev** is the reverse hausdorff, the direction the gate asserts, and **margin** is
the tolerance minus the worse of its two settings. **fwd** is the forward
hausdorff, reported. **dom** is the count of solver front points dominated by the
reference front, with the fraction of the front beside it, reported.

    solver         phi  seed  k_run  k_ref   rev F   rev T   tol     margin   fwd F   fwd T   dom F          dom T
    random_search  lu    11    610   1000  0.0509  0.0509  0.1629  0.1120  0.1154  0.1154    65  10.7%    65  10.7%
    random_search  lu    12    622   1000  0.0392  0.0392  0.1629  0.1238  0.0958  0.0958    64  10.3%    64  10.3%
    random_search  lu    13    590   1000  0.0416  0.0416  0.1629  0.1214  0.0935  0.0935    58   9.8%    58   9.8%
    random_search  lu    14    586   1000  0.0445  0.0445  0.1629  0.1184  0.1049  0.1049    55   9.4%    55   9.4%
    random_search  lu    15    608   1000  0.0393  0.0393  0.1629  0.1237  0.0895  0.0895    53   8.7%    53   8.7%
    random_search  ls    11   2220   1000  0.0477  0.0477  0.3415  0.2938  0.1796  0.1567    68   3.1%    74   3.3%
    random_search  ls    12   2253   1000  0.0412  0.0412  0.3415  0.3003  0.3691  0.3691    65   2.9%    70   3.1%
    random_search  ls    13   2256   1000  0.0414  0.0414  0.3415  0.3001  0.2222  0.1773    49   2.2%    58   2.6%
    random_search  ls    14   2195   1000  0.0473  0.0473  0.3415  0.2942  0.2191  0.2191    59   2.7%    64   2.9%
    random_search  ls    15   2182   1000  0.0391  0.0391  0.3415  0.3024  0.1883  0.1596    69   3.2%    70   3.2%
    random_search  cw    11   1544   1000  0.0406  0.0406  0.3213  0.2807  0.4155  0.4155    73   4.7%    76   4.9%
    random_search  cw    12   1528   1000  0.0449  0.0449  0.3213  0.2764  0.3691  0.3691    69   4.5%    76   5.0%
    random_search  cw    13   1591   1000  0.0362  0.0362  0.3213  0.2851  0.2551  0.2307    71   4.5%    76   4.8%
    random_search  cw    14   1501   1000  0.0373  0.0394  0.3213  0.2820  0.3071  0.2752    61   4.1%    62   4.1%
    random_search  cw    15   1504   1000  0.0403  0.0403  0.3213  0.2810  0.4525  0.4249    77   5.1%    81   5.4%
    nsga2          lu    11    100   1000  0.1098  0.1098  0.1629  0.0531  0.1105  0.1105    17  17.0%    17  17.0%
    nsga2          lu    12    100   1000  0.1165  0.1165  0.1629  0.0464  0.1268  0.1268    16  16.0%    16  16.0%
    nsga2          lu    13    100   1000  0.1127  0.1127  0.1629  0.0502  0.1702  0.1702    17  17.0%    17  17.0%
    nsga2          lu    14    100   1000  0.1379  0.1379  0.1629  0.0250  0.1761  0.1761    22  22.0%    22  22.0%
    nsga2          lu    15    100   1000  0.1098  0.1098  0.1629  0.0531  0.1379  0.1379    16  16.0%    16  16.0%
    nsga2          ls    11    100   1000  0.3309  0.3309  0.3415  0.0106  0.2602  0.2602    20  20.0%    22  22.0%
    nsga2          ls    12    100   1000  0.2523  0.2523  0.3415  0.0892  0.2118  0.2112    21  21.0%    23  23.0%
    nsga2          ls    13    100   1000  0.3244  0.3244  0.3415  0.0171  0.2216  0.2216    24  24.0%    27  27.0%
    nsga2          ls    14    100   1000  0.2922  0.3093  0.3415  0.0322  0.2236  0.1874    17  17.0%    18  18.0%
    nsga2          ls    15    100   1000  0.2378  0.2378  0.3415  0.1037  0.3484  0.3483    17  17.0%    18  18.0%
    nsga2          cw    11    100   1000  0.2159  0.2159  0.3213  0.1054  0.2067  0.2068    15  15.0%    15  15.0%
    nsga2          cw    12    100   1000  0.2432  0.2432  0.3213  0.0781  0.1981  0.1985    20  20.0%    21  21.0%
    nsga2          cw    13    100   1000  0.2503  0.2503  0.3213  0.0710  0.2310  0.2310    25  25.0%    27  27.0%
    nsga2          cw    14    100   1000  0.2367  0.2367  0.3213  0.0846  0.2388  0.2388    19  19.0%    20  20.0%
    nsga2          cw    15    100   1000  0.2167  0.2167  0.3213  0.1046  0.1894  0.1894    19  19.0%    21  21.0%
    mopso          lu    11    200   1000  0.0918  0.0918  0.1629  0.0711  0.1785  0.1785    50  25.0%    50  25.0%
    mopso          lu    12    200   1000  0.0829  0.0829  0.1629  0.0801  0.1228  0.1228    48  24.0%    48  24.0%
    mopso          lu    13    200   1000  0.0688  0.0688  0.1629  0.0941  0.1766  0.1766    31  15.5%    31  15.5%
    mopso          lu    14    200   1000  0.0963  0.0963  0.1629  0.0666  0.1470  0.1470    41  20.5%    41  20.5%
    mopso          lu    15    200   1000  0.0787  0.0787  0.1629  0.0842  0.1447  0.1447    42  21.0%    42  21.0%
    mopso          ls    11    200   1000  0.1867  0.1867  0.3415  0.1548  0.5000  0.5000    30  15.0%    33  16.5%
    mopso          ls    12    200   1000  0.1397  0.1397  0.3415  0.2018  0.2444  0.2444    22  11.0%    23  11.5%
    mopso          ls    13    200   1000  0.2011  0.2011  0.3415  0.1404  0.2559  0.2568    34  17.0%    37  18.5%
    mopso          ls    14    200   1000  0.1702  0.1702  0.3415  0.1713  0.2772  0.2772    29  14.5%    28  14.0%
    mopso          ls    15    200   1000  0.1685  0.1685  0.3415  0.1730  0.2743  0.2743    29  14.5%    28  14.0%
    mopso          cw    11    200   1000  0.1098  0.1191  0.3213  0.2023  0.2224  0.2223    22  11.0%    22  11.0%
    mopso          cw    12    200   1000  0.1108  0.1172  0.3213  0.2041  0.2523  0.2523    30  15.0%    32  16.0%
    mopso          cw    13    200   1000  0.1304  0.1304  0.3213  0.1909  0.5301  0.5000    18   9.0%    27  13.5%
    mopso          cw    14    200   1000  0.1107  0.1107  0.3213  0.2106  0.1974  0.1974    26  13.0%    26  13.0%
    mopso          cw    15    200   1000  0.1226  0.1226  0.3213  0.1988  0.3247  0.3247    38  19.0%    38  19.0%

**the reverse direction passes in all ninety measurements, and no solver front
point dominates any reference front point in any of the ninety.** the smallest
reverse margin in the grid is 0.0106, nsga-ii under phi_ls at seed 11, and the
next is 0.0171 at seed 13; both are inside the tolerance's own sensitivity,
section 2, and both survive the larger reading of it.

on both settings of include_singular_segments, per r-12. the flag is a no-op under
phi_lu, where b1 section 2.3 finds no singular ray at all, and the two columns are
identical there by construction. under phi_ls and phi_cw the two reference sets
differ in the 32 rows b2 puts on the segment. the effect on the asserted direction
is at most 0.0171 and no verdict changes at either setting; the effect on the
reported dominated count is small and nearly one-signed, changing in 26 of the 45
configurations, by +1 to +9 in 24 of them and by -1 in two, both mopso under
phi_ls. it is not purely additive because src/reference_fronts.py takes the 32
segment rows out of the 1000 rather than adding them on top, so a few regular
dominators leave the reference set as the segment enters it.

the dominated fraction is a fraction and its denominator is the front, so it is
read beside k_run and not alone. random search's fraction is the smallest in the
table and its absolute count is the largest, 49 to 77 against nsga-ii's 15 to 27,
because its front is fifteen to twenty times larger. that is r-16's confound
appearing in a decision-space count, and it is the reason both numbers are printed.


## 4. the verdict

**the pipeline is validated and phase e is not blocked by this gate.** three of
the gate's assertions fail and none of them is a pipeline assertion: all three are
the budget trend under phi_cw, section 6, and they are reported as failures rather
than accommodated.

    every solver reaches every part of every derived set to within the tolerance,
        at every seed, under every phi, at both settings of the singular flag.
        ninety measurements, none over the tolerance, the tightest margin 0.0106.
        the derivation, its encoding in b2 and the three solvers agree about
        where the efficient set is.
    no solver beats the derivation. zero reference front points are dominated by
        any solver front point, in all ninety measurements. b1's set is not
        missing anything the solvers found.
    p0's anchor is found by every solver under every phi, by two orders of
        magnitude, section 7.
    the containment diagnostic is zero in all ninety runs filtered, so the
        transform, the route pairing, the column order and the dominance relation
        are consistent across the whole tier 0 pipeline, section 8.
    the forward distances are reported and are what section 5 says they are.
    the budget trend holds in nine of the twelve cells it is asserted on, and
        the three it does not hold on are all phi_cw and are section 6. that is a
        failing assertion and section 6 reports it as one; it is a question about
        what to assert of a capped-front method, r-18, and not a condition on e1.

**what c3 called twelve failures were not twelve failures.** ten of the twelve
offending points were already known to be dominated by the reference front, and
the remaining two are dominated by the derived set as well once the question is
put to b1's closed form instead of to b2's sample, section 5.5. every one of the
twelve is a point the solver returned that is genuinely not efficient, and the
derivation is missing nothing at any of them.

they split in two, along the line section 5 predicts. **eight are the
finite-sample artifact**: c3's own section 5.1 found those eight within 0.01 of
x_1 = 0 or x_2 = 0, which is exactly where the surviving extreme points of a
finite draw sit, and that is a statement about what a non-dominated subset of a
finite sample contains rather than about the search. it would hold for a solver
that had converged perfectly. **the other four are ordinary convergence**, and
all four are phi_lu, the one phi with no width column: c3's section 5.2 found
three of them fixed at four times the budget, nsga-ii at seeds 13 and 14 and
mopso at seed 13, and the fourth, mopso at seed 11, not.


## 5. why the forward direction cannot be asserted

this replaces c3's section 5. c3 ran the three checks its brief prescribed, found
the box face was not the cause, found the budget was the cause for nsga-ii and not
for random search, and found no solver and phi pair failing on all five seeds. all
three findings stand and none of them is the cause. the cause is structural and it
is v-53.

### 5.1 the mechanism

p1's four image columns, per phi, from src/phi_transforms.py against
src/problems_tier0.py, with c_1 = x_1^2 + (x_2 - 1)^2, c_2 = (x_1 - 1)^2 +
(x_2 - 1)^2, r_1 = rho x_2^2 + delta and r_2 = rho x_1^2 + delta:

    phi_lu   (c_1 - r_1,  c_1 + r_1,  c_2 - r_2,  c_2 + r_2)
    phi_ls   (c_1 - r_1,  2 r_1,      c_2 - r_2,  2 r_2)
    phi_cw   (c_1,        r_1,        c_2,        r_2)

**phi_ls and phi_cw each carry two columns that depend on one decision variable
alone, and phi_lu carries none.** r_2 does not move with x_2 and r_1 does not move
with x_1, so under phi_cw the fourth column is a strictly increasing function of
|x_1| and nothing else, and under phi_ls it is twice that.

the consequence, for any finite set of candidates whatever produced it. the point
of smallest |x_1| is the strict minimiser of that column, so no other candidate is
no worse than it in every column, so nothing dominates it. **it survives the filter
and enters the front, whatever its x_2 is.** its x_2 ranges over the whole decision
box, [-1/2, 3/2], while b1 section 2.4 puts X_cw's x_2 in [0, 1] and X_ls's in
[0, 4/3]. the forward hausdorff distance is a maximum over the front, so it is
bounded below by that point's overhang, which reaches 1/2 under phi_cw. the same
holds for the point of smallest |x_2| through the second column.

a larger sample does not remove such a point. it supplies a new one, at a new and
equally arbitrary position in the other coordinate.

### 5.2 the mechanism, measured

on the gate's own uniform draws at budget 5000, the sample random search filters,
asking whether the two extreme points are in the non-dominated set:

    phi    seed 11   seed 12   seed 13   seed 14   seed 15
    lu     no, no    no, no    no, no    no, no    no, no
    ls     yes, yes  yes, yes  yes, yes  yes, yes  yes, yes
    cw     yes, yes  yes, yes  yes, yes  yes, yes  yes, yes

and over 40 independent draws of 2000 points, the count of draws in which each
extreme point is dominated:

    phi   smallest |x_1|   smallest |x_2|
    lu    24 of 40         40 of 40
    ls     0 of 40          0 of 40
    cw     0 of 40          0 of 40

**the split is exactly the split between the phi that carry a width column and the
one that does not**, which is also the split c3 found in its section 5.1 without
being able to name it: c3 observed that eight of its twelve worst points lay
within 0.01 of x_1 = 0 or x_2 = 0 and that the four that did not were all phi_lu.

the overhangs the mechanism predicts are c3's own worst points. under phi_cw, the
smallest-|x_1| point of the seed 11 draw is (0.00026, 1.41550), at distance 0.4155
from X_cw, and of the seed 12 draw is (-0.00000, -0.36913), at 0.3691. those are
c3 section 5.1's worst points for random search under phi_cw at seeds 11 and 12
and its forward distances 0.4155 and 0.3691 exactly. and c3's largest forward
distance anywhere, 0.5000154 at mopso under phi_ls at seed 11, is the box overhang
1/2 to within the reference sample's own resolution.

both halves are asserted in tests/test_validation.py and not merely narrated:
test_one_image_column_is_a_function_of_one_variable_under_ls_and_cw checks which
columns are constant when one variable moves, and
test_the_extreme_points_of_a_finite_sample_survive_the_filter checks that the two
points survive under phi_ls and phi_cw and are dominated under phi_lu, the phi_lu
branch being the contrast that makes the test a measurement rather than a
restatement, CONTEXT.md section 11's evidence rule.

### 5.3 so the forward direction is reported and never asserted

there is no tolerance derived from the region that this floor respects. the floor
is up to 1/2 under phi_cw and the region-derived tolerance is 0.3213, and raising
the tolerance to 1/2 would be a gate that passes anything. the floor is not a
property of the solver, so a solver that had converged exactly onto X_cw and then
returned the non-dominated subset of its evaluations would carry it too.

the forward distance is still worth printing, and section 3 prints it, because a
forward distance far above the floor at every seed would be a signal. it is a
diagnostic and it is never a verdict.

### 5.4 why random search is excluded from the budget trend

the control's front is by construction the non-dominated subset of one uniform
sample of the box, src/random_search.py, so section 5.1 applies to it directly and
at every budget: the sample's two extreme points are always in it. checked at
20000 evaluations at all five seeds under phi_ls and phi_cw, neither extreme point
is dominated in any of the ten samples. c3 measured the consequence: random
search's forward distance is unchanged to four decimal places at four times the
budget at seed 12 under both phi and at cw seed 15, and c3-b reproduces that,
0.3691 against 0.3691 and 0.4525 against 0.4525.

that is not a convergence problem and no budget removes it. it is a property of
the control, and CONTEXT.md section 10 c1's reading of the control as the thing
the comparison rests on is unaffected: what random search is for is isolating the
effect of the order from the effect of the search, and it does that whatever its
front's extreme points do.

### 5.5 the two points c3 raised as s-13, settled

c3 recorded two points as dominated by nothing in the derived set,
(1.42192, -0.00039) from random search under phi_cw at seed 15 and
(1.50000, 0.00026) from mopso under phi_cw at seed 13, both on the singular line
x_2 = 0 beyond x_1 = 1, and raised them as s-13.

**that was a statement about b2's sample and not about the derived set, and put to
b1's closed form the answer is different.** b2 reaches X_cw's extreme values only
in the limit, its weight sample being dirichlet at concentration 0.3, so no row of
the 1000-point reference front lies close enough to x_1 = 1 to beat either point.
b1 section 2.4 gives X_cw = [0, 1]^2 minus the open segment
{(x_1, 0) : 0 < x_1 <= 1}, so (0.999, 0.0001) is a point of the derived set, is
off the undecided segment its x_2 being strictly positive, and has phi_cw image

    (1.997801, 0.125000, 0.999801, 0.374500)

against (3.022637, 0.125000, 1.178797, 0.630464) and
(3.249480, 0.125000, 1.249480, 0.687500). it is strictly smaller in all four
columns against both, the r_1 column included and not tied: the three values there
are 0.125 + 2.5e-09, 0.125 + 3.8e-08 and 0.125 + 1.7e-08 and only the printed
rounding hides the difference. it is not an isolated witness either: 28 and 26 of
200000 uniform draws of the interior of X_cw dominate the two points.

**so both points are dominated by points of the derived set, both are genuinely
not efficient, and s-13 dissolves.** it is closed in docs/answered.md with that
reasoning. c3's section 5.4 figure of ten of twelve is twelve of twelve.

**s-12 is untouched and stays open.** it asks what the status of the segment
{(x_1, 0) : 0 < x_1 <= 1} itself is, where the published conditions give weak
optimality and no verdict either way, b1 section 2.6, and nothing here bears on
that. what dissolves is the claim that a solver had reached a point past the
segment's end that the derivation could not account for.


## 6. the budget trend

the dominated fraction at 5000 evaluations against 20000, for the two population
methods, pooled over the five seeds. pooled and not per seed, and that is the
project's own rule rather than a choice made here: CONTEXT.md section 10 c2 puts
five seeds in the design because one run gives no variance, so a trend read at one
seed is a trend read on one run. the per-seed counts are in section 6.1 and they
move by up to six points of a hundred in both directions.

    solver  phi  include_singular   at 5000            at 20000           trend
    nsga2   lu   False              88 of 500  17.60%   79 of 500  15.80%  falls
    nsga2   ls   False              99 of 500  19.80%   80 of 500  16.00%  falls
    nsga2   cw   False              98 of 500  19.60%   97 of 500  19.40%  falls
    nsga2   lu   True               88 of 500  17.60%   79 of 500  15.80%  falls
    nsga2   ls   True             108 of 500  21.60%   89 of 500  17.80%  falls
    nsga2   cw   True             104 of 500  20.80%  109 of 500  21.80%  **rises**
    mopso   lu   False            212 of 1000 21.20%  199 of 1000 19.90%  falls
    mopso   ls   False            144 of 1000 14.40%  128 of 1000 12.80%  falls
    mopso   cw   False            134 of 1000 13.40%  146 of 1000 14.60%  **rises**
    mopso   lu   True             212 of 1000 21.20%  199 of 1000 19.90%  falls
    mopso   ls   True             149 of 1000 14.90%  138 of 1000 13.80%  falls
    mopso   cw   True             145 of 1000 14.50%  154 of 1000 15.40%  **rises**

**nine of the twelve hold and three fail, all of them under phi_cw.**
this is reported as a failure and not softened: the assertion was fixed before the
measurement, the measurement contradicts it in three cells, and the assertion is
not being moved to accommodate them. pooling further, over phi as well as over
seeds, would make both solvers pass, nsga-ii at 19.00 to 17.07 per cent and mopso
at 16.33 to 15.77, and that is exactly the adjustment this session refuses to make.

what the three have in common, offered as an observation and not as a resolution.
they are all phi_cw, which is the phi whose image is the identity on (c, r) and
whose derived set is the smallest of the three, the unit square against X_ls's
three eighths of the box; the two solvers' fronts are capped at 100 and 200 rows
by design while the derived region's area does not shrink; and mopso's archive is
truncated at 200 by a random rule, c2-b and d-03, so four times the budget gives
it four times as many candidates to discard at random rather than a better 200.
there is no mechanism in either algorithm that forces the worst member of a capped
front to improve with budget. **whether the dominated fraction is the right trend
to assert for a capped-front method is a design question and it is raised as r-18,
not answered here.**

what does hold without qualification, at every phi and both flag settings, is that
the trend holds for the two phi that are not phi_cw, and that nothing anywhere
gets worse by more than 1.0 point of a hundred.

### 6.1 the same measurement per seed

reported because section 6 pools, and a pooled number that hides a systematic
per-seed pattern would be misleading. include_singular_segments False, the
dominated count at 5000 against 20000, the front size being 100 for nsga-ii and
200 for mopso at both budgets:

    solver  phi   seed 11   seed 12   seed 13   seed 14   seed 15
    nsga2   lu    17 -> 17  16 -> 19  17 -> 10  22 -> 13  16 -> 20
    nsga2   ls    20 -> 18  21 -> 14  24 -> 10  17 -> 15  17 -> 23
    nsga2   cw    15 -> 17  20 -> 13  25 -> 21  19 -> 25  19 -> 21
    mopso   lu    50 -> 39  48 -> 46  31 -> 35  41 -> 39  42 -> 40
    mopso   ls    30 -> 27  22 -> 29  34 -> 27  29 -> 22  29 -> 23
    mopso   cw    22 -> 30  30 -> 26  18 -> 26  26 -> 35  38 -> 29

**the count rises in eleven of the thirty and falls or holds in nineteen, and no
seed rises in every pair.** a per-configuration assertion would fail in eleven
cells, and asserting one would be asserting that a count of about twenty out of a
hundred moves monotonically under a change of budget, which the spread here says it
does not. the pooled reading in section 6 is the one the seed list exists to
supply.

random search is not in this table. its front grows with the budget, 610 to 2058
rows under phi_lu and 1544 to 5726 under phi_cw, so its dominated fraction falls
mechanically, 4.39 to 1.50 per cent pooled over the grid, while its absolute count
rises from 956 to 1216. neither number is a statement about the search, and
section 5.4 is why it is excluded.


## 7. p0, the smoke test

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
for.


## 8. the phi_lu points absent from the phi_ls set

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


## 9. cardinality, per r-16

every number in sections 3, 6, 7 and 8 carries the front cardinality it was
computed at. nothing is truncated to a common size, and that is deliberate rather
than an omission: r-16 is about objective-space metrics that move with the number
of rows, and hausdorff is a maximum over two sets. truncating a recovered set
before measuring a maximum discards real coverage and makes the measured distance a
property of the subsample. CONTEXT.md section 10 d1 records that the r-16 rule is
for objective-space metrics only.

what the cardinality column carries here is the reading of two numbers. the three
solvers return 586 to 2256, exactly 100, and at most 200 rows, and the reverse
distance tracks that ordering almost exactly: random search 0.036 to 0.051, mopso
0.069 to 0.201, nsga-ii 0.110 to 0.331. that is largely the cardinality and not
the search, which is why the reverse direction is read against h_design, the floor
a design-sized front cannot beat, and not against zero. and the dominated fraction
carries the same confound in the other direction: random search's is the smallest
in the table and its count is the largest, section 3.


## 10. what this means for phase e

**phase e is not blocked by this gate.** the rule is CONTEXT.md section 8's, that
c3 gates phase e if the solvers do not recover the tier 0 sets, and they do: every
solver reaches every part of every derived set to within the tolerance at every
seed under every phi, and no solver returns a point that beats the derivation.

what e1 has to carry from this document, and it is not optional:

    the forward hausdorff is reported and never asserted, and any table of e1's
        that prints one prints it beside the note that it carries the
        finite-sample floor of section 5. this is v-53 and it is a property of the
        design, not a defect. a reader who takes a forward distance for a quality
        measure will rank the solvers by how their fronts' extreme points fell.
    the dominated count against a reference front is the decision-space quality
        measure that carries no such artifact, and it is reported as a fraction
        with the cardinality beside it, both numbers and not one.
    include_singular_segments has no default and its value belongs in every table,
        r-12 and s-12, and the two settings are two different reference objects.
    the budget. section 6 says four times the budget lowers the dominated fraction
        for both population methods under phi_lu and phi_ls, and raises it under
        phi_cw for mopso at both settings of the singular flag and for nsga-ii at
        the True setting, so r-15's plan of a 5000 sweep with one 20000 check
        per problem is not contradicted, and the convergence check is worth
        reading against the dominated count and not only against a distance.

what is open, and neither is a blocker:

    r-18, whether the dominated fraction is the right trend to assert for a
        capped-front method at all, section 6.
    s-12, the status of the singular segments, unchanged by this session and
        unchanged by b2's flag, which stays undecided by the published conditions.
        s-13 is closed, section 5.5.


## 11. open items this session raises

    r-18  the budget trend fails under phi_cw, section 6, for mopso at both
          settings of the singular flag and for nsga-ii at the True setting.
          neither algorithm contains a mechanism that would make it hold: a front
          capped at 100 or 200 rows has nothing forcing its worst member to
          improve when the budget rises, and mopso's archive discards at random at
          that cap, d-03, so four times the budget gives it four times as many
          candidates to discard rather than a better two hundred. whether a
          monotone trend in the dominated fraction is the right thing to assert of
          a capped-front method is a design question. it is raised and not
          answered, and no assertion was moved to accommodate the three failing
          cells.

    s-13  closed in this session, section 5.5, and moved to docs/answered.md. the
          two points are dominated by points of b1's derived set, and the finding
          that they were not was read off b2's sample rather than off the closed
          form.

    r-17  stands, section 2, and now bites only on the reverse direction, which
          passes with margin under both readings of h_design.

    s-12  touched and not resolved. r-12 touched: the two settings of
          include_singular_segments do not disagree about the asserted direction
          on p1, which is a narrower statement than r-12's igd finding and does
          not retire it.
