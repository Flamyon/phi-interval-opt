# c3: the validation gate

subpart c3, third pass, as c3-c. output: this file and tests/test_validation.py.
a gate, not a report: it decides whether phase e starts. CONTEXT.md section 8
states the rule, "c3 gates phase e. if the solvers do not recover the tier 0
sets, no tier 1 result is trustworthy and none is produced."

**c3 asserted the wrong direction. c3-b removed that assertion and left three
mistakes of its own behind. this session corrects all three, and none of them is
a mistake about the solvers.** no phi, no problem, no derivation, no solver and
no dominance relation is touched by any of the three.

    correction 1   c3-b called the forward floor "a property of filtering a
                   finite sample" and then asserted a budget trend that the same
                   property forbids. the property is a proposition with a
                   two-line proof, section 1, and its corollary is that a larger
                   budget re-elects the offending points rather than removing
                   them. the budget trend is removed here for all three solvers
                   and reported as a number.
    correction 2   "dominated by b2's reference front" was the quality measure,
                   and it depends on b2's sampling density: measured on one run
                   it runs from 9 per cent at 250 reference rows to 31 per cent
                   at 16000 and the exact answer is 46. it is replaced by exact
                   membership in b1 section 2.4's closed-form region, section 3.
    correction 3   the tolerance summed two resolution floors where the reverse
                   direction is bounded by one of them alone, section 2. under
                   the corrected tolerance, estimated as a distribution rather
                   than as one draw, the gate fails twelve of ninety, every one
                   nsga-ii, and that is a finding and not a tolerance problem,
                   section 5.

what follows states the proposition and its proof, the corrected tolerance and
its derivation, what every configuration returned, what the outside points
actually are, the finding about nsga-ii's coverage, the budget trend as a number,
and where that leaves phase e.

**c3-d, c3-e and c3-f are diagnostic passes on top of this file and none of them
changes a number in sections 1 to 4.** c3-d is described in the paragraph below and
is section 5.1. c3-e and c3-f continued the same question, why the finding of
section 5 appears under two phi and not the third, and they are sections 5.2 to
5.5. **c3-e did not commit: its session ended before it wrote, and its measurements
are recorded here for the first time**, marked as its where they appear. what the
two sessions together establish is a decomposition and not a mechanism, section
5.5's closing part, and the finding of section 5 is unchanged by either.

**c3-d is a diagnostic pass on top of this file and it changes one paragraph.** it
tested whether the reading section 5 offers for the phi split is a demonstration,
by instrumenting nsga-ii's non-dominated sorting through a pymoo callback. the
answer is no: rank 1 fills the survivor slots under all three phi from generation
three or four onwards, so the mechanism is present everywhere and cannot carry a
result that appears under two phi and not the third. section 5's mechanism
paragraph is rewritten to say that and section 5.1 is the measurement. **no
assertion, no tolerance and no number in sections 1 to 4 is touched by c3-d**, and
the finding of section 5 itself is unchanged. what the saturation does change is
what e2 has to report, CONTEXT.md section 10 e2, since a configuration where rank 1
fills the slots is one where the solver's front is a spread and not a convergence
result.


## 0. what the gate asserts and what it reports

asserted, pass or fail, and these are the two directions of the pipeline:

    reference to solver   was what exists found. the largest distance from a point
                          of the derived set to the recovered set, within the
                          tolerance of section 2, per solver, per phi, per seed,
                          per setting of the singular flag. this is the
                          convergence question. **it fails in twelve of the
                          ninety measurements, all nsga-ii, section 4.**
    no solver point       a solver cannot beat the analytic answer. the count of
    dominates the         reference front points some solver front point dominates
    derived set           is zero. asserted in c1 and in c2 at one seed; asserted
                          here over the whole grid, because the gate is where the
                          claim that the derivation and the solvers agree is made.
                          **zero in all ninety.**

the reverse direction is asserted **for all three solvers and nsga-ii is not
exempted from it**. the alternative was on the table and section 4.1 says why it
was refused.

reported and never asserted:

    the fraction of solver front points outside b1 section 2.4's closed-form
    region, with the distribution of the excess. this is the quality measure and
    it is exact: it needs no sample, so no sampling density can move it, and a
    point outside the region is not efficient whatever any sample says.
    the forward hausdorff, solver to reference, per configuration. it is bounded
    below by the protected extreme of section 1 and is not a quality measure.
    the count of solver front points dominated by b2's reference front, kept for
    one run at seven reference sizes so the bias it carries is quantified once,
    section 3.2, and not otherwise.
    the budget trend, on both measures, at 5000 against 20000, section 6.
    the front cardinality beside every number, per r-16.

CONTEXT.md section 10 c3 carries the same statement, and the change is reproduced
as a before and after block in this session's reply.


## 1. the protected extreme

this is correction 1. c3-b had the mechanism and did not have it as a theorem, so
it did not see that the same mechanism forbids the trend it went on to assert.

### 1.1 the proposition

p1's four image columns, per phi, from src/phi_transforms.py against
src/problems_tier0.py, with c_1 = x_1^2 + (x_2 - 1)^2, c_2 = (x_1 - 1)^2 +
(x_2 - 1)^2, r_1 = rho x_2^2 + delta and r_2 = rho x_1^2 + delta, rho in (0, 1)
and delta > 0:

    phi_lu   (c_1 - r_1,  c_1 + r_1,  c_2 - r_2,  c_2 + r_2)
    phi_ls   (c_1 - r_1,  2 r_1,      c_2 - r_2,  2 r_2)
    phi_cw   (c_1,        r_1,        c_2,        r_2)

**proposition (the protected extreme).** let S be any finite set of decision
vectors in p1's box, of at least two elements, and let g be p1's image map under
phi. suppose x* in S satisfies |x*_1| < |y_1| for every other y in S. then under
phi_ls and under phi_cw no element of S dominates x*, whatever x*_2 is. the same
holds for the element of strictly smallest |x_2|. under phi_lu neither statement
holds.

**proof.** under phi_cw the fourth column is g_4 = r_2 and under phi_ls it is
g_4 = 2 r_2, so in both cases g_4(x) = a (rho x_1^2 + delta) with a > 0. that is
a strictly increasing function of |x_1| and of |x_1| alone: it does not contain
x_2. by hypothesis |x*_1| < |y_1| for every other y in S, so
g_4(x*) < g_4(y) for every other y in S. domination of x* by y requires
g_j(y) <= g_j(x*) in every column j, and at j = 4 that is g_4(y) <= g_4(x*),
which contradicts the strict inequality just established. so no y in S dominates
x*, and x* is in the non-dominated subset of S. nothing in the argument mentions
x*_2, so x*_2 is unconstrained. the statement for smallest |x_2| is the same
argument on the second column, which is r_1 or 2 r_1 and is a strictly increasing
function of |x_2| alone. under phi_lu the four columns are c_1 -+ r_1 and
c_2 -+ r_2, and every one of them has both partial derivatives non-zero at a
generic point, d(c_1 - r_1)/dx_1 = 2 x_1 and d(c_1 - r_1)/dx_2 =
2 (x_2 - 1) - 2 rho x_2, so no column is a function of one variable alone and the
hypothesis of the argument is unavailable. that the conclusion also fails there
is not proved but measured, section 1.4. **qed**

two remarks the proof needs. the strictness matters: two elements sharing a value
of |x_1| tie in that column and either can dominate the other through the rest, so
the proposition is about the strict minimiser and, in a draw from a continuous
distribution, ties occur with probability zero. and the proposition is about an
arbitrary finite set and not about a sampler: it holds for a uniform draw, for an
nsga-ii population, for a mopso archive, and for the output of a solver that had
converged perfectly and then filtered its own evaluations.

recorded as v-54 in docs/verified.md.

### 1.2 the corollary, and it is the corollary that does the damage

**corollary (the shielded chain).** order S by |x_1| ascending. under phi_ls and
phi_cw the element of j-th smallest |x_1| can be dominated only by one of the
j - 1 elements below it in that order.

**proof.** domination requires being no worse in the fourth column, which by the
proposition's first step means |y_1| <= |x_1|. **qed**

so the protection does not stop at the first element. the j-th element is exposed
to j - 1 candidate dominators instead of |S| - 1, and for small j that is nearly
as strong as for j = 1. **the whole low-|x_1| tail is over-represented in the
front, and its x_2 is unconstrained throughout.** the same holds for the
low-|x_2| tail through the second column.

### 1.3 what it costs the forward direction

the protected element's other coordinate ranges over the whole box, [-1/2, 3/2],
while b1 section 2.4 puts X_cw's x_2 in [0, 1] and X_ls's in [0, 4/3]. the
forward hausdorff is a maximum over the front, so it is bounded below by that
overhang, which reaches 1/2 under phi_cw. for a uniform draw the elected point's
x_2 is uniform on the box independently of its |x_1|, so it lies outside [0, 1]
with probability exactly 1/2 and its expected overhang is exactly 1/8, **at every
budget**. measured over 200 uniform draws at each of four sizes:

    n         median min |x_1|   mean overhang of the elected point's x_2
    1000      7.45e-04           0.1226
    5000      1.41e-04           0.1404
    20000     4.21e-05           0.1334
    80000     1.00e-05           0.1261

the first column falls by a factor of four for every factor of four in n. the
second does not move. that is the whole of correction 1 in two columns.

### 1.4 the same, measured on the pipeline's own samples

whether the two extreme points of the gate's own uniform draws survive the filter,
at budget 5000, per phi and per gate seed:

    phi    seed 11   seed 12   seed 13   seed 14   seed 15
    lu     no, no    no, no    no, no    no, no    no, no
    ls     yes, yes  yes, yes  yes, yes  yes, yes  yes, yes
    cw     yes, yes  yes, yes  yes, yes  yes, yes  yes, yes

the proposition as a statement about an arbitrary set, on 2000 random sets of
random size between 2 and 60 with two members planted at the worst place the box
allows, one of |x_1| below 1e-6 at an extreme x_2 and one of |x_2| below 1e-6 at
an extreme x_1. tests/test_validation.py runs the same construction at 400 sets,
which is the size that keeps it in the fast run:

    phi   argmin |x_1| dominated   argmin |x_2| dominated
    lu    1066 of 2000             1939 of 2000
    ls       0 of 2000                0 of 2000
    cw       0 of 2000                0 of 2000

the corollary, on the sample random search actually filters. the survival rate of
the j-th smallest |x_1| over the five gate draws of 5000 points, for j = 1 to 30,
against the rate for a member of the sample at large:

    phi   ranks 1 to 10                              rate over ranks 1-30   sample at large
    lu    0.0 0.2 0.4 0.4 0.4 0.0 0.2 0.4 0.4 0.6    0.32                   0.12
    ls    1.0 0.6 1.0 1.0 0.6 0.4 1.0 0.8 0.8 0.8    0.73                   0.44
    cw    1.0 0.6 1.0 1.0 0.4 0.4 0.8 0.4 0.4 0.6    0.60                   0.31

and by |x_2|, where phi_lu is the contrast: **the thirty smallest |x_2| of every
one of the five gate draws are dominated, 150 of 150, under phi_lu**, against
rates of 0.79 and 0.69 under phi_ls and phi_cw over the same thirty ranks.

both halves of the proposition and both halves of the corollary are asserted in
tests/test_validation.py, in
test_the_strict_minimiser_of_a_width_column_is_never_dominated,
test_one_image_column_is_a_function_of_one_variable_under_ls_and_cw,
test_the_whole_low_width_tail_is_shielded_and_not_only_its_first_member and
test_the_low_width_tail_is_not_shielded_under_lu.

### 1.5 so the budget trend is removed, for all three solvers

c3-b asserted that the dominated fraction does not rise when the budget is
quadrupled, for the two population methods, and reported that three of its twelve
cells failed. **the assertion should not have been made.** the proposition says a
larger budget elects a new protected element of smaller |x_1| at an x_2 that is no
better placed, so nothing in a larger budget removes the offending points; the
corollary says the same of the whole tail. there is a floor that no budget crosses
and **monotonicity in budget is not a property either algorithm has under phi_ls
or phi_cw**, nor random search under any phi.

the assertion is removed entirely and not weakened, not pooled differently and not
restricted to phi_lu. **restricting it to phi_lu would be the same accommodation
in a smaller box**: phi_lu is exactly the phi where the mechanism is absent, so a
trend asserted there and nowhere else would be an assertion selected by the
measurement it is supposed to judge. section 6 reports the trend as a number, on
both measures, with this section beside it.

the re-election is asserted in
test_a_larger_budget_re_elects_the_protected_extreme, at four times the budget at
every gate seed. at seed 12 it is at its plainest: the minimiser of |x_1| in the
20000-point draw is the same point as in the 5000-point draw, still protected,
still in the front, after four times the work.

r-18 is rewritten accordingly. it said no mechanism forces improvement; the truth
is that a mechanism protects the offending points.


## 2. the tolerance, and where it comes from

this is correction 3.

### 2.1 what c3 summed, and why one of the two terms does not belong

c3 set the tolerance to h_reference + h_design, the covering radius of the derived
region by b2's 1000-point reference sample plus the covering radius by a
design-sized front, on the grounds that "both sets in every comparison are finite
samples of the same two-dimensional region, and each carries its own resolution
floor".

that reasoning is wrong for the direction the gate asserts. write R for the
derived region and S for the recovered set. the reverse direction is

    sup over p in the reference set of dist(p, S).

every reference point lies in R, docs/b1_phi_efficient_sets.md section 2.4 and
tests/test_reference_fronts.py::test_sampled_points_lie_in_the_derived_region, so
the supremum over the reference set is at most the supremum over R:

    sup_{p in reference} dist(p, S)  <=  sup_{y in R} dist(y, S)  =:  fill(S),

the fill distance of S with respect to R. **the reference sample enters only
through being a subset of R, and its own resolution plays no part in this
direction at all.** the bound requires nothing of S: S need not lie in R, and the
protected extremes of section 1 do not.

the same argument in the other direction bounds the forward distance by fill of
the reference set, and for any two subsets A and B of R,

    dH(A, B) = max( sup_{a in A} dist(a, B), sup_{b in B} dist(b, A) )
             <= max( fill(B), fill(A) ),

which is a maximum and never a sum. checked on 300 random pairs of subsets of each
region, sizes 1000 and 100: the bound held 300 of 300 in both directions under all
three phi, with the reverse slack reaching 0.0000, so the bound is attained and is
not merely valid. the sum is 0.189, 0.293 and 0.238 against maxima of 0.143, 0.219
and 0.177 for phi_lu, phi_ls and phi_cw: about a third of c3's tolerance was slack
that no argument put there. asserted in
tests/test_validation.py::test_the_reverse_distance_is_bounded_by_the_solver_fill_distance,
which sweeps the reference-like set's size by a factor of sixteen while comparing
against fill(B) alone, so that a hidden dependence on the reference's own
resolution would show.

**the argument is right and the reverse-direction tolerance is h_design alone.**
recorded as v-55 in docs/verified.md.

### 2.2 h_design stops being one draw

c3 read h_design as the mean of twenty draws. r-17 is the record of how much that
choice moved, and its complaint is that a statistic resting on a small number of
draws moves with the draw count. so h_design is estimated here as a distribution:
the fill distance with respect to R of a uniform k-point draw of R, over 1000
independent draws, the supremum taken over the same fixed 20000-point uniform
sample of R at the same seed c3 used. **the estimator is c3's and only the draw
count and the summary taken from it have changed**, which the first twenty draws
confirm by reproducing c3's published h_design to four decimal places, 0.1246,
0.2174 and 0.1836, asserted in
tests/test_validation.py::test_the_fill_distance_estimator_is_the_one_c3_used.

the distribution, at k = 100, nsga-ii's population and the smallest front size the
design fixes in advance, and at k = 200, mopso's archive bound:

    phi  k    mean    sd      min     q25     median  q75     q90     q95     q99     max
    lu   100  0.1420  0.0511  0.0773  0.1030  0.1254  0.1691  0.2125  0.2405  0.3105  0.4396
    lu   200  0.1032  0.0370  0.0566  0.0750  0.0909  0.1203  0.1598  0.1776  0.2160  0.2666
    ls   100  0.2232  0.0373  0.1549  0.1975  0.2166  0.2430  0.2698  0.2919  0.3483  0.4211
    ls   200  0.1599  0.0227  0.1135  0.1439  0.1564  0.1725  0.1886  0.2022  0.2278  0.3061
    cw   100  0.1783  0.0270  0.1267  0.1591  0.1733  0.1910  0.2147  0.2318  0.2606  0.3204
    cw   200  0.1291  0.0180  0.0914  0.1168  0.1259  0.1383  0.1527  0.1628  0.1877  0.2130

the distribution is wide and skewed, especially under phi_lu, whose region is the
smallest and the most elongated of the three: its 1000 draws run from 0.077 to
0.440, a factor of 5.7, at a fixed k on a fixed region. **that spread is why one
draw, or twenty, is not a floor**, and it is r-17's finding measured properly
rather than estimated from a factor.

### 2.3 the quantile, fixed before the study was run

    fill_quantile = 0.95, at k = front_design_size = 100.

    phi   tolerance
    lu    0.2405
    ls    0.2919
    cw    0.2318

the choice was written down before the study executed, with three reasons, and it
is not moved by what the study returned.

    a floor has to be an upper bound on what a correct design-sized front
        achieves, not a typical value. read at the mean, as c3 read it, a perfect
        uniform-sampling solver exceeds the tolerance in about half of its
        measurements, which makes the gate a coin flip rather than a gate.
    it has to be estimable from the draw count fixed in advance. at 1000 draws the
        0.95 quantile rests on the 50th and 51st largest values. the 0.99 quantile
        rests on the 10th and 11th and the maximum rests on one, and a statistic
        that moves with the draw count is exactly r-17's objection.
    the consequence is stated rather than hidden. at 0.95 a solver whose front were
        a uniform draw of R would exceed this tolerance in about one measurement in
        twenty, so **one isolated failure at a margin near zero is not evidence of
        a defect, while a failure concentrated in one solver across seeds and phi
        is.** that reading was fixed in advance too, before it was known which case
        the grid would produce. it produced the second, section 5.

k = 100 and not each solver's own k, because the gate is one gate and 100 is the
smallest front size the design fixes before a run rather than reads off one. the
k = 200 distribution is measured so that mopso's coverage can also be read at its
own cardinality, section 5, and it is not the tolerance.

the box is [-1/2, 3/2]^2, of side 2, so the tolerance is 12.0, 14.6 and 11.6 per
cent of the box side for phi_lu, phi_ls and phi_cw.

**this tolerance is still coarse and the reason is structural.** the derived sets
are two-dimensional regions of substantial area, b1 section 2.4: X_cw is the unit
square up to one edge and a quarter of the box's area, X_ls about three eighths of
it and X_lu about a twelfth. a hundred-point front cannot cover a region of that
size to better than 0.13 to 0.22 at the median in a box of side 2, and that is
what the table in 2.2 measures. a tighter gate on p1 is not available at this budget from any
solver, and section 3 carries every margin so that a pass with no margin is
visible as one.

### 2.4 what changed against c3's number

    phi   c3's tolerance   c3-c's tolerance   direction
    lu    0.1629           0.2405             looser by 0.0776
    ls    0.3415           0.2919             tighter by 0.0496
    cw    0.3213           0.2318             tighter by 0.0895

the tolerance did not move in one direction, which is worth saying plainly:
removing h_reference tightens it and reading h_design at a quantile rather than at
a mean loosens it, and under phi_lu the second effect is the larger. **a tolerance
that had been adjusted to a purpose would not have gone up for one phi and down
for two.**

r-17 is retired by this section and moved to docs/answered.md. the sensitivity it
records was the sensitivity of a sum in which one term did not belong and the
other was estimated from twenty draws; both causes are removed, and what replaces
the point estimate is a measured distribution with its quantiles printed in 2.2.

no tolerance is used anywhere in a dominance comparison. CONTEXT.md section 5 and
d-02 stand: every dominance test here is the ordinary pareto relation on doubles,
through src/random_search.py's non_dominated_indices and pymoo's own sorting. the
number above is a reporting tolerance on a distance and touches no order.


## 3. p1 recovery, per solver, per phi, per seed

columns rev F and rev T are the reverse hausdorff at include_singular_segments
False and True, **margin** is the tolerance minus the worse of the two, and
**verdict** is the gate's. **out** is the count of solver front points outside b1
section 2.4's closed-form region, with the fraction of the front beside it, and
**excess med** is the median constraint residual over those points. **fwd** is the
forward hausdorff, reported and never asserted, section 1.3. k_run is the front
cardinality and k_ref the reference sample's, beside every number per r-16.
nothing is truncated to a common cardinality: hausdorff is a maximum over two sets
and truncating either would discard real coverage.

    solver         phi  seed  k_run  k_ref   rev F   rev T   tol     margin  verdict  out    out%   excess med  fwd F   fwd T
    random_search  lu    11    610   1000  0.0509  0.0509  0.2405  +0.1896  pass    227   37.2%    0.4226  0.1154  0.1154
    random_search  lu    12    622   1000  0.0392  0.0392  0.2405  +0.2013  pass    219   35.2%    0.4293  0.0958  0.0958
    random_search  lu    13    590   1000  0.0416  0.0416  0.2405  +0.1989  pass    194   32.9%    0.4081  0.0935  0.0935
    random_search  lu    14    586   1000  0.0445  0.0445  0.2405  +0.1960  pass    219   37.4%    0.3718  0.1049  0.1049
    random_search  lu    15    608   1000  0.0393  0.0393  0.2405  +0.2012  pass    203   33.4%    0.3549  0.0895  0.0895
    random_search  ls    11   2220   1000  0.0477  0.0477  0.2919  +0.2442  pass    320   14.4%    0.0482  0.1796  0.1567
    random_search  ls    12   2253   1000  0.0412  0.0412  0.2919  +0.2508  pass    343   15.2%    0.0569  0.3691  0.3691
    random_search  ls    13   2256   1000  0.0414  0.0414  0.2919  +0.2506  pass    329   14.6%    0.0549  0.2222  0.1773
    random_search  ls    14   2195   1000  0.0473  0.0473  0.2919  +0.2447  pass    318   14.5%    0.0554  0.2191  0.2191
    random_search  ls    15   2182   1000  0.0391  0.0391  0.2919  +0.2528  pass    330   15.1%    0.0534  0.1883  0.1596
    random_search  cw    11   1544   1000  0.0406  0.0406  0.2318  +0.1912  pass    279   18.1%    0.0373  0.4155  0.4155
    random_search  cw    12   1528   1000  0.0449  0.0449  0.2318  +0.1869  pass    296   19.4%    0.0337  0.3691  0.3691
    random_search  cw    13   1591   1000  0.0362  0.0362  0.2318  +0.1956  pass    275   17.3%    0.0398  0.2551  0.2307
    random_search  cw    14   1501   1000  0.0373  0.0394  0.2318  +0.1924  pass    258   17.2%    0.0304  0.3071  0.2752
    random_search  cw    15   1504   1000  0.0403  0.0403  0.2318  +0.1914  pass    280   18.6%    0.0381  0.4525  0.4249
    nsga2          lu    11    100   1000  0.1098  0.1098  0.2405  +0.1307  pass     36   36.0%    0.4797  0.1105  0.1105
    nsga2          lu    12    100   1000  0.1165  0.1165  0.2405  +0.1240  pass     52   52.0%    0.4155  0.1268  0.1268
    nsga2          lu    13    100   1000  0.1127  0.1127  0.2405  +0.1278  pass     39   39.0%    0.3522  0.1702  0.1702
    nsga2          lu    14    100   1000  0.1379  0.1379  0.2405  +0.1026  pass     51   51.0%    0.4307  0.1761  0.1761
    nsga2          lu    15    100   1000  0.1098  0.1098  0.2405  +0.1307  pass     44   44.0%    0.3197  0.1379  0.1379
    nsga2          ls    11    100   1000  0.3309  0.3309  0.2919  -0.0389  FAIL     50   50.0%    0.1246  0.2602  0.2602
    nsga2          ls    12    100   1000  0.2523  0.2523  0.2919  +0.0397  pass     48   48.0%    0.1108  0.2118  0.2112
    nsga2          ls    13    100   1000  0.3244  0.3244  0.2919  -0.0325  FAIL     57   57.0%    0.1173  0.2216  0.2216
    nsga2          ls    14    100   1000  0.2922  0.3093  0.2919  -0.0174  FAIL     44   44.0%    0.0936  0.2236  0.1874
    nsga2          ls    15    100   1000  0.2378  0.2378  0.2919  +0.0541  pass     40   40.0%    0.1195  0.3484  0.3483
    nsga2          cw    11    100   1000  0.2159  0.2159  0.2318  +0.0158  pass     46   46.0%    0.0506  0.2067  0.2068
    nsga2          cw    12    100   1000  0.2432  0.2432  0.2318  -0.0114  FAIL     52   52.0%    0.0700  0.1981  0.1985
    nsga2          cw    13    100   1000  0.2503  0.2503  0.2318  -0.0186  FAIL     56   56.0%    0.0760  0.2310  0.2310
    nsga2          cw    14    100   1000  0.2367  0.2367  0.2318  -0.0049  FAIL     43   43.0%    0.0782  0.2388  0.2388
    nsga2          cw    15    100   1000  0.2167  0.2167  0.2318  +0.0151  pass     38   38.0%    0.0580  0.1894  0.1894
    mopso          lu    11    200   1000  0.0918  0.0918  0.2405  +0.1487  pass     98   49.0%    0.5779  0.1785  0.1785
    mopso          lu    12    200   1000  0.0829  0.0829  0.2405  +0.1576  pass     90   45.0%    0.8473  0.1228  0.1228
    mopso          lu    13    200   1000  0.0688  0.0688  0.2405  +0.1717  pass     78   39.0%    0.4894  0.1766  0.1766
    mopso          lu    14    200   1000  0.0963  0.0963  0.2405  +0.1442  pass     83   41.5%    0.6318  0.1470  0.1470
    mopso          lu    15    200   1000  0.0787  0.0787  0.2405  +0.1618  pass     87   43.5%    0.7811  0.1447  0.1447
    mopso          ls    11    200   1000  0.1867  0.1867  0.2919  +0.1053  pass     49   24.5%    0.1667  0.5000  0.5000
    mopso          ls    12    200   1000  0.1397  0.1397  0.2919  +0.1522  pass     72   36.0%    0.1565  0.2444  0.2444
    mopso          ls    13    200   1000  0.2011  0.2011  0.2919  +0.0908  pass     63   31.5%    0.1536  0.2559  0.2568
    mopso          ls    14    200   1000  0.1702  0.1702  0.2919  +0.1218  pass     61   30.5%    0.1276  0.2772  0.2772
    mopso          ls    15    200   1000  0.1685  0.1685  0.2919  +0.1235  pass     59   29.5%    0.1645  0.2743  0.2743
    mopso          cw    11    200   1000  0.1098  0.1191  0.2318  +0.1127  pass     49   24.5%    0.0582  0.2224  0.2223
    mopso          cw    12    200   1000  0.1108  0.1172  0.2318  +0.1146  pass     67   33.5%    0.0735  0.2523  0.2523
    mopso          cw    13    200   1000  0.1304  0.1304  0.2318  +0.1014  pass     58   29.0%    0.0387  0.5301  0.5000
    mopso          cw    14    200   1000  0.1107  0.1107  0.2318  +0.1210  pass     65   32.5%    0.0628  0.1974  0.1974
    mopso          cw    15    200   1000  0.1226  0.1226  0.2318  +0.1092  pass     70   35.0%    0.0796  0.3247  0.3247

**the reverse direction fails in six of the forty-five configurations and twelve
of the ninety measurements, every one of them nsga-ii**, at three seeds under
phi_ls and three under phi_cw, and at none under phi_lu. random search passes with
margins of 0.19 to 0.25 and mopso with margins of 0.09 to 0.17. **no solver front
point dominates any reference front point in any of the ninety.**

the outside fraction is flag-independent and the table therefore prints one
column. that is not an omission: the measure is membership in a closed-form
region, so no reference sample and no setting of a reference sample's flag enters
it, which is the point of correction 2.

on the singular flag, per r-12. it is a no-op under phi_lu, where b1 section 2.3
finds no singular ray, and the two reverse columns are identical there by
construction. under phi_ls and phi_cw the two reference sets differ in the 32 rows
b2 puts on the segment, and the effect on the asserted direction is at most
0.0171, at nsga-ii under phi_ls at seed 14, where it moves no verdict: that cell
fails at both settings.

### 3.2 the exact measure against the sampled one, and the bias quantified once

c3 and c3-b reported the count of solver front points dominated by b2's reference
front as the quality measure. one run, nsga-ii on p1 under phi_cw at seed 11, at
seven reference sizes:

    reference rows    dominated, of 100 front points
    250                9
    500               12
    1000              15    <- the size c3 and c3-b reported at
    2000              18
    4000              24
    8000              26
    16000             31

    exact, b1 section 2.4 membership: 46 outside the region, and it does not move
    with any sample at all.

and against a uniform sample of the region rather than b2's weight sample, which
removes the parametrisation's density and leaves only the density:

    uniform region sample of   1000 rows: 10 dominated
    uniform region sample of  20000 rows: 28 dominated
    uniform region sample of 150000 rows: 34 dominated

**the sampled number is biased downward at every finite reference size, by a
factor of three at the size the earlier sessions used, and it rises monotonically
with density towards the exact answer without reaching it.** two runs measured
against two reference sizes are not comparable, and a quality ranking read off it
is a ranking of how densely each reference happened to be drawn near each front.
that is why it is retired as the measure. it is kept in this section, at seven
sizes on one run, and nowhere else.

asserted in
tests/test_validation.py::test_the_exact_region_measure_does_not_move_with_the_reference_and_the_sampled_one_does.

on the helper. tests/test_reference_fronts.py already implements the algebraic
test as region_excess, and this session **duplicated it into
tests/test_validation.py rather than moving it to src/**. the reason is the one
tests/test_reference_fronts.py already gives for holding the regions in a test
file at all: a region that src/ also held would make both checks a file agreeing
with itself, and the regions are the derivation's output, which the modules are
being tested against. the duplicate exposes the per-point residual as well as the
file-level maximum, because the distribution of the excess is what this session
reports. c2's precedent for copying a helper between test files rather than
sharing it is followed rather than reopened.

### 3.3 what the outside points are

the diagnosis correction 2 asks for: are the outside points clustered at the
region boundary, which would be crowding-driven spread pushing the population past
the edge, or scattered, which would be non-convergence. the excess is a constraint
residual and for phi_lu and phi_ls the binding constraints are quadratic forms, so
it is not a distance and the euclidean distance to the region is printed beside
it, measured against a uniform sample of 150000 points of the region, whose own
resolution is about 0.002.

    solver         phi   outside/k    excess: med   q90     max  |  distance to R: med    q90     max  | <=0.01  <=0.05   >0.1
    random_search  lu   1062/3016      0.3930  1.0750  2.0162  |          0.0238  0.0587  0.1037  |  21.4%   85.1%   0.1%
    random_search  ls   1640/11106     0.0543  0.6285  1.7815  |          0.0330  0.0835  0.3695  |  17.1%   69.6%   4.8%
    random_search  cw   1388/7668      0.0362  0.0862  0.4249  |          0.0367  0.0865  0.4251  |  15.7%   65.1%   5.6%
    nsga2          lu    222/500       0.3968  1.4440  3.5273  |          0.0252  0.0760  0.1704  |  27.9%   79.3%   4.5%
    nsga2          ls    239/500       0.1159  1.5110  3.9934  |          0.0740  0.1505  0.3485  |  10.9%   33.5%  31.8%
    nsga2          cw    235/500       0.0674  0.1512  0.2387  |          0.0675  0.1516  0.2389  |  13.2%   41.3%  31.9%
    mopso          lu    436/1000      0.6352  1.5968  2.9749  |          0.0401  0.0871  0.1758  |  13.8%   62.2%   6.0%
    mopso          ls    304/1000      0.1529  1.3838  4.1648  |          0.0910  0.1705  0.5001  |   9.5%   31.2%  47.0%
    mopso          cw    309/1000      0.0642  0.1643  0.5000  |          0.0650  0.1647  0.5002  |   7.4%   41.7%  31.7%

**the answer is both, and the split is by phi and not by solver.**

    under phi_lu, and for random search under all three phi, the outside points
    hug the boundary. the median distance is 0.024 to 0.040, two thirds to five
    sixths are within 0.05, and at most 6 per cent are further than 0.1. the
    residual tally says the same: 925 of random search's 1062 phi_lu outside
    points, and 201 of nsga-ii's 222, violate one of the two curved boundaries
    rather than a coordinate bound. that is spread past the edge of a region whose
    boundary is a curve, and it is not non-convergence.
    under phi_ls and phi_cw the two population methods carry a genuine scattered
    tail. between 32 and 47 per cent of their outside points are more than 0.1 from
    the region, the median of the tail is 0.13 to 0.17, and it reaches 0.50, which
    is the box's own half-width. those points are spread over all four faces of the
    box: of nsga-ii's 77 far points under phi_ls, 33 are past x_1 = 4/3, 27 are at
    x_1 < 0, 5 below x_2 = 0 and 4 above x_2 = 4/3, with x_1 quantiles
    -0.348, -0.109, 0.633, 1.460, 1.500. that is not a boundary effect, it is a
    population that still holds members at the corners of the box after fifty
    generations.

**and the protected extremes of section 1 are not the explanation.** the two
protected points are two points of a front:

    solver         phi   argmin |x_1| outside   argmin |x_2| outside   share of the outside points
    random_search  lu    3 of 5 runs            5 of 5 runs            8 of 1062, 0.8%
    random_search  ls    4 of 5                 3 of 5                 7 of 1640, 0.4%
    random_search  cw    4 of 5                 3 of 5                 7 of 1388, 0.5%
    nsga2          lu    3 of 5                 5 of 5                 8 of  222, 3.6%
    nsga2          ls    2 of 5                 3 of 5                 5 of  239, 2.1%
    nsga2          cw    3 of 5                 2 of 5                 5 of  235, 2.1%
    mopso          lu    4 of 5                 5 of 5                 9 of  436, 2.1%
    mopso          ls    1 of 5                 3 of 5                 4 of  304, 1.3%
    mopso          cw    3 of 5                 2 of 5                 5 of  309, 1.6%

the corollary of section 1.2 reaches further than the two points and it still does
not carry the fraction. taking the front's own bottom decile in |x_1| together
with its bottom decile in |x_2|, which is about 19 per cent of the rows:

    solver         phi   outside points in the two tails   if outside were spread evenly
    random_search  lu    32%                               19%
    random_search  ls    42%                               19%
    random_search  cw    38%                               19%
    nsga2          lu    22%                               17%
    nsga2          ls    22%                               19%
    nsga2          cw    22%                               19%
    mopso          lu    31%                               19%
    mopso          ls    31%                               19%
    mopso          cw    32%                               19%

**for random search the shielded tail carries about twice its share and explains a
large part of the outside fraction; for nsga-ii it carries 1.15 times its share
and explains almost none of it.** so nsga-ii's 36 to 57 per cent is not the
mechanism of section 1: it is the front sitting off the derived set, which is the
same thing the reverse distance measures and the same thing section 5 is about.

that is worth stating against the expectation this session started with. the brief
put the outside fraction at 13 to 21 per cent and the protected extremes at a floor
near 2 per cent of it. **the fraction is 14 to 57 per cent and the extremes account
for 0.4 to 3.6 per cent of the outside points, not of the front.** the direction of
the expectation was right, that the extremes are a small part; the size of what
they are a small part of is two to four times larger than the sampled measure
suggested, and that gap is correction 2's bias appearing in every row of section 3.


## 4. the verdict

**the gate does not pass, the failure is understood, and phase e is not blocked by
it.** the two statements are not in tension and section 10 says why.

    every part of every derived set is reached to within the tolerance by random
        search and by mopso, at every seed, under every phi, at both settings of
        the singular flag: sixty of sixty measurements, margins 0.09 to 0.25.
    nsga-ii reaches it under phi_lu at every seed, and fails at three of five
        seeds under phi_ls and three of five under phi_cw: twelve of its thirty
        measurements over the tolerance, by 0.005 to 0.039.
    no solver beats the derivation. zero reference front points are dominated by
        any solver front point, in all ninety measurements. b1's set is not
        missing anything the solvers found.
    p0's anchor is found by every solver under every phi, by two orders of
        magnitude, section 7.
    the containment diagnostic is zero in all forty-five p1 runs and all
        forty-five p0 runs, so the transform, the route pairing, the column order
        and the dominance relation are consistent across the whole tier 0
        pipeline, section 8.
    the exact quality measure, the forward distances and the budget trend are
        reported and are what sections 3, 1.3 and 6 say they are.

### 4.1 asserted for all three solvers, and nsga-ii is not exempted

the alternative was explicit: assert the reverse direction for random search and
mopso and report it for nsga-ii with the finding attached. **it is refused, and
this is the recommendation with its reason.**

    an assertion that is dropped for whichever solver it catches is not an
    assertion. the gate exists to answer one question, do the solvers recover the
    tier 0 sets, and the tolerance was derived from the region and from a
    design-fixed front size before the runs. exempting the one solver that fails
    it converts the gate into a report at the exact moment it does its job, and it
    would do so on the strength of the result, which is the adjustment this
    subpart has now refused three times.
    the exemption that was granted once, random search's exclusion from the budget
    trend in c3-b, rested on a proof that the assertion was vacuous for that
    solver, and section 1 has now made that proof cover all three. there is no
    analogous proof here. nothing forces nsga-ii's reverse distance above the
    tolerance; it is contingent, it is measured, and under phi_lu it does not
    happen at all. an exemption would be excluding a solver for a property that is
    exactly what the gate measures.
    a per-cell expected-failure list, pytest's xfail, was considered and refused
    for the same reason in different spelling: it makes the suite green while the
    assertion fails, and it would need a hard-coded list of six configurations
    read off this measurement.

so **the suite runs red, in twelve tests, and it is meant to.** section 5 is the
finding those twelve carry and PROGRESS.md's session log records the count so a
later session can see whether it moved.


## 5. the finding: nsga-ii covers this efficient set worse than random sampling

c3-b saw this and called it a tolerance question. it is not.

nsga-ii returns exactly 100 rows, which is exactly the k the tolerance's
distribution is measured at, so the comparison is at equal cardinality and needs
no correction. where each run's fill distance sits in the distribution of 1000
uniform 100-point draws of the same region:

    solver  phi  k    fill distance, five seeds         percentile in the uniform draw   worse than the uniform mean
    nsga2   lu   100  0.1100 0.1229 0.1211 0.1404 0.1202   33  49  47  60  45              0 of 5
    nsga2   ls   100  0.3352 0.2670 0.3337 0.3126 0.2571   98  89  98  97  85              5 of 5
    nsga2   cw   100  0.2321 0.2549 0.2557 0.2462 0.2152   95  98  99  98  90              5 of 5
    mopso   lu   200  0.0953 0.0850 0.0724 0.1002 0.0817   55  43  18  61  36              0 of 5
    mopso   ls   200  0.1869 0.1467 0.2086 0.1670 0.1735   89  30  97  68  77              4 of 5
    mopso   cw   200  0.1234 0.1226 0.1457 0.1275 0.1477   43  41  85  54  86              2 of 5

random search has no design-fixed cardinality and is not in the table; at the 586
to 2256 rows it returns, its fill distance is 0.043 to 0.052, far below any
100-point or 200-point draw, which is cardinality and not search.

**the finding, stated as a finding.** for a full-dimensional efficient set,
nsga-ii's decision-space coverage is worse than uniform random sampling of that
set at equal cardinality, **under phi_ls and phi_cw and not under phi_lu**. under
the two phi where it holds, all ten measurements are worse than the uniform mean
and eight of the ten sit at the 90th percentile of that distribution or above. under
phi_lu all five sit between the 33rd and the 60th percentile, which is where a
uniform draw itself sits. mopso shows the same tendency and weaker, four of five
above the mean under phi_ls and two of five under phi_cw, at its own cardinality
of 200.

**the phi-conditionality is the part c3-b did not have**, and it is the part that
makes the finding a finding rather than a complaint about nsga-ii. the split is
the same split section 1 draws: phi_ls and phi_cw are the two phi whose image
carries a column depending on one decision variable alone, phi_lu is the one that
does not. nsga-ii sorts and spreads by crowding distance in the four-column image
space, not in the two-dimensional decision space where the coverage is measured,
and under phi_ls and phi_cw two of those four columns are functions of a single
decision variable, so the crowding distance nsga-ii equalises is computed in a
space whose relation to the decision space is different from phi_lu's. **this is
offered as the reading and not as a demonstration.** c3-d set out to turn it into
one by measuring the operator's internals directly, and the measurement does not
carry the split. section 5.1 is what it measured and why the reading stays a
reading; the finding above is unchanged by it and nothing in sections 1 to 4
moves. **the reading did not survive c3-e and c3-f either, and neither did three
further candidates.** sections 5.2 to 5.5 put the wasted-slot account, the
pullback account, the anisotropy of the map and the alignment of the crowding
distance's axes to direct measurement and refute all four, and then separate what
is left with a phi-neutral control: half the swing between phi_lu and the other
two is carried by random search, which has no operator at all, and half is
nsga-ii's own and has no mechanism. **the finding above is unchanged in every one
of its numbers and is now bounded**: section 5.5's closing part is what phase c
closes on.

what it does **not** say, and e1 must not let it be read as saying: it is not that
nsga-ii fails to converge, since it does not return points that beat the
derivation anywhere, and it is not that the pipeline is wrong. it says that a
front of 100 rows chosen by nsga-ii covers this particular two-dimensional
efficient set less uniformly than 100 points drawn uniformly from it, and
therefore that the largest gap between the derived set and nsga-ii's front is
larger than the derivation's own resolution at that cardinality.

recorded in CONTEXT.md section 10 e3 as something e3 must report.

### 5.1 rank 1 saturates, under every phi, and the reading stays a reading

the hypothesis c3-d tested, stated before the run. nsga-ii sorts
pop_size + offspring = 200 candidates per generation. if rank 1 alone holds at
least pop_size of them then dominance never enters the selection: every survivor
is chosen by crowding distance, and the algorithm is a spread maximiser with no
convergence pressure. a4 measured p1's exact non-dominated sets at 460, 1505 and
961 points for phi_lu, phi_ls and phi_cw, docs/a4b_dominance_tolerance.md section
1.5, on the 61 x 61 grid of 3721 points on [-0.5, 1.5]^2 that section 1.2 states,
so the fractions are 0.124, 0.404 and 0.258. if a generation's candidate set
behaved like that grid the expected rank-1 size among 200 would be about 25, 81
and 52. that is a phi split of the right shape and in the right order, and it
would have explained the finding above and the population members
section 3.3 finds at all four corners of the box after fifty generations, which
crowding distance in the image space alone does not.

one arithmetic correction to the hypothesis as it was put, and it does not change
what the hypothesis predicts. the expected sizes were given as 53, 174 and 111,
which is 460, 1505 and 961 over 1728; 1728 is the size of dtlz2's separation
sample and p1's
grid is 61 x 61 = 3721, so the correct figures are the 25, 81 and 52 above. both
sets of numbers predict the same split in the same order and both are refuted the
same way.

**it is not what happens. rank 1 saturates under all three phi, by generation four
at the latest, and it never falls back.** the hypothesis's conclusion is right
under phi_ls and phi_cw and it is right under phi_lu as well, which is what
refutes it as an explanation: a mechanism present under every phi cannot be what
distinguishes phi_lu from the other two. the sizes it predicted are wrong under
all three, 25, 81 and 52 against measured medians of about 170, 172 and 170 over
the second half of the run, and the direction of the error is the same in each.
so the crowding-distance reading of the paragraph above is left as a reading, and
the saturation is recorded as its own fact rather than as an explanation of that
one.

the route taken, and there were two available. the four series are read out of the
algorithm's state after every generation through a pymoo Callback, which pymoo
calls at the end of _post_advance, core/algorithm.py line 329, after survival has
run. **pymoo is not modified and nsga2.py is not touched**: a callback reads state
and the one used here writes nothing back. two of the four series come straight
off that state. the survivors' rank attribute, which RankAndCrowding._do sets on
every individual it sorts, operators/survival/rank_and_crowding/classes.py line 99,
gives the number of survivors that came from rank 1; comparing it to the population
size gives whether rank 1 filled the slots. the other two cannot be reached that
way, because pymoo keeps the survivors and discards the merged set they were
chosen from, so the number of fronts and the size of rank 1 among the 200
candidates are obtained by **re-running pymoo's own NonDominatedSorting** on a
matrix the callback records, the previous generation's survivors stacked on this
generation's offspring, algorithm.off. that is the second route, and no sorting is
reimplemented: the class called is pymoo's. the instrument is checked against
src/runners.py's own solve_once at the same seed and the front comes back
bit-identical under all three phi, so the callback does not perturb the run. the
harness is a session diagnostic and is not committed: it adds no module and
changes no file under src/ or tests/, and this paragraph is what it would take to
rebuild it.

p1, nsga-ii, pop_size 100, n_gen 50, budget 5000, seed 11, which is the gate's
own configuration. generations 1 to 6 and then every fifth. one caveat on the
first column: generation 1 is the initialisation, where pymoo runs survival on the
initial population alone with n_survive equal to its own size, so the candidate
set there is 100 and not 200 and nothing is discarded; from generation 2 on it is
200:

    gen                    1    2    3    4    5    6   10   15   20   25   30   35   40   45   50
    phi_lu
      fronts, all sorted  12   18    8    5    4    4    5    4    5    4    4    5    4    4    4
      fronts, survival    12    4    2    1    1    1    1    1    1    1    1    1    1    1    1
      rank 1 of 200       26   49   74  112  156  172  168  167  167  159  174  177  179  176  169
      survivors from r1   26   49   74  100  100  100  100  100  100  100  100  100  100  100  100
      infinite crowding   41   19   10    4    4    4    6    6    4    4    5    6    7    5    5
    phi_ls
      fronts, all sorted   5    8    3    3    4    4    3    3    4    3    4    3    3    3    4
      fronts, survival     5    2    1    1    1    1    1    1    1    1    1    1    1    1    1
      rank 1 of 200       57   99  174  184  175  159  172  173  168  167  174  176  167  172  175
      survivors from r1   57   99  100  100  100  100  100  100  100  100  100  100  100  100  100
      infinite crowding   23    9    8    8    8    7    8    7    8    8    8    8    8    7    8
    phi_cw
      fronts, all sorted   7    9    5    4    4    3    4    4    5    3    4    3    3    4    3
      fronts, survival     7    2    1    1    1    1    1    1    1    1    1    1    1    1    1
      rank 1 of 200       48   75  120  165  165  169  157  174  173  169  171  170  169  168  175
      survivors from r1   48   75  100  100  100  100  100  100  100  100  100  100  100  100  100
      infinite crowding   30   13    7    7    7    7    8    8    6    8    7    8    8    8    8

the front count is given twice because they are two different numbers. "all
sorted" is the full sort of the 200. "survival" is how many fronts pymoo actually
enumerates, since RankAndCrowding calls the sort with n_stop_if_ranked = n_survive,
operators/survival/rank_and_crowding/classes.py line 69, and NonDominatedSorting
breaks as soon as the ranked count reaches it,
util/nds/non_dominated_sorting.py lines 46 to 48. from generation three or four
onwards that number is **one**: nsga-ii enumerates a single front and fills the
entire population out of it, and the four or five other fronts that exist are
never looked at.

the decisive number, over the five gate seeds, at the gate's budget:

    phi   rank 1 at gen 1   first generation with rank 1 >= 100   rank 1 over gens 21 to 50, min median max   later dips below 100
    lu    19 to 26          4, 4, 4, 4, 4                         159 to 163   168 to 172   175 to 179       none, in any seed
    ls    57 to 65          3, 3, 3, 3, 2                         157 to 165   170 to 173   177 to 184       none, in any seed
    cw    46 to 54          3, 4, 3, 3, 3                         148 to 161   167 to 170   176 to 179       none, in any seed

generation 1 is the only generation whose candidate set is a draw of the box, and
it is the only one where a grid's non-dominated fraction is a comparable quantity
at all. there the split is present and in the predicted order: rank 1 is 19 to 26,
57 to 65 and 46 to 54 of 100, against the 12, 40 and 26 of 100 the 3721-point
grid's fractions give: between 1.4 and 2.1 times the grid's figure under every
phi, which is the sample size and not the phi, and lu below cw below ls in both.
**by generation 3 or 4 rank 1 holds about 170 of the 200 candidates under every
phi, and for the remaining 46 or 47 generations of the run every one of the 100
survivors is a rank-1 member selected on crowding distance alone.** dominance
decides nothing after generation four under any of the three orders.

**the extreme points, and they are not the outside points of section 3.3 either.**
nsga-ii's crowding distance assigns infinity to the extreme member in each
objective column, so with four columns up to eight members per generation are
unremovable while they stay extreme. from generation four onwards the count sits
at 4 to 8, as the series above show; in the first generations, before the sort
collapses to one front, it is 23 to 41, because a crowding distance is computed
per front and every front contributes its own extremes.

whether section 3.3's outside points are those members, or
their descendants, needs a genealogy pymoo does not record: no operator writes a
parent link onto an offspring. it is obtained by giving the algorithm a Mating
subclass that delegates to pymoo's own _do with the selected parents hoisted out
so they are visible, and tags each offspring with whether either parent held or
descended from an infinite crowding distance. it is a wrapper of the same kind
src/runners.py's SeededArchiveMopso already is, pymoo is again unmodified, and the
check is the same one: with the traced mating installed the fronts and every
series above come back identical to the plain run under all three phi. the final
generation, all five gate seeds, against the outside points of section 3.3:

    phi   front   outside   infinite crowding now   of those, outside   outside points that are extreme now   ever an extreme itself   descends from an extreme
    lu    500     222       28                      18, 64%             18 of 222, 8.1%                       21 of 222, 9.5%          222 of 222, 100%
    ls    500     239       37                      29, 78%             29 of 239, 12.1%                      33 of 239, 13.8%         239 of 239, 100%
    cw    500     235       39                      33, 85%             33 of 235, 14.0%                      37 of 235, 15.7%         235 of 235, 100%

the outside counts 222, 239 and 235 are section 3.3's own, which is the check that
this is the same run and the same measure. **the extremes are strongly enriched
among the outside points and they do not carry them.** an extreme is outside the
region 64 to 85 per cent of the time against a base rate of 44 to 48 per cent for
the front as a whole, so being unremovable and being outside go together; but the
extremes are 28 to 39 points and the outside points are 222 to 239, so they
account for 8 to 14 per cent of them, and the points that were ever an extreme
during the run account for 10 to 16 per cent. the descent column is reported and
is vacuous: after fifty generations every member of the front descends from some
individual that held an infinite crowding distance, and so does every member of
the population, so the number is 100 per cent against a base rate of 100 per cent
and separates nothing. that is what a genealogy in a population of 100 over 50
generations looks like, and it is stated rather than used.

**tier 1, where it matters more.** the same instrument on zdt1_interval, which
transforms to 4 columns in 30 variables, and dtlz2_interval, which transforms to 6
columns in 12, at eps = 0.10 and seed 11, at the same budget:

    problem          columns  phi   rank 1 at gen 1   first gen with rank 1 >= 100   rank 1 gens 21 to 50, min median max   fronts, median   infinite crowding, median
    zdt1_interval    4        lu    16                14                             110  124  144                          6                5
    zdt1_interval    4        ls    29                13                             111  131  143                          5                6
    zdt1_interval    4        cw    26                21                             100  118  137                          4                5
    dtlz2_interval   6        lu    50                 4                             129  146  155                          4                9
    dtlz2_interval   6        ls    64                 3                             144  155  167                          3                7
    dtlz2_interval   6        cw    56                 3                             135  153  170                          3                8

**it saturates in all six tier 1 configurations, and it is worse on dtlz2 than on
zdt1.** dtlz2 saturates at generation 3 or 4, exactly as p1 does, and then sits at
a median rank 1 of 146 to 155 of 200 with three or four fronts in the sort, so
nsga-ii spends 46 or 47 of its 50 generations selecting on crowding distance alone
in a six-column image space. zdt1 is the one configuration where dominance
survives a while: rank 1 does not reach 100 until generation 13, 13 and 21 under
the three phi, it dips back below 100 twice under phi_lu at generations 16 and 17,
and its median over the last thirty generations is 118 to 131 rather than p1's or
dtlz2's 146 to 173.

what orders the three problems is not the column count, and this is worth saying
because the column count is the obvious candidate and it is wrong. p1 transforms
to 4 columns and saturates at generation 3 or 4, as fast as dtlz2's 6; zdt1 also
transforms to 4 and takes 13 to 21. what does track the ordering is the
non-dominated fraction of the transformed image, on a5's separation samples,
recomputed in exact arithmetic in docs/a_close_containment.md section 3.3: at
eps = 0.10 dtlz2 gives 995, 1362 and 947 of 1728, which is 0.58, 0.79 and 0.55,
against zdt1's 247, 535 and 483 of 1024, which is 0.24, 0.52 and 0.47. three
problems is not enough to assert that as a law and it is not asserted here; what
is asserted is the measurement, that every one of the nine problem-phi
configurations run in this section reaches saturation and, apart from two
generations on zdt1 under phi_lu, stays there for the rest of the run. **e2 cannot be read without this
number**, and CONTEXT.md section 10 e2 now requires every configuration to report
it.

what 5.1 concludes, and what it does not. it concludes that from generation three
or four onwards nsga-ii on this transformed problem is selecting on crowding
distance and not on dominance, that this holds under every phi and on both tier 1
benchmarks, and that on zdt1 it takes until generation 13 to 21 rather than 3 to 4
but arrives all the same. it does **not** conclude that this explains section 5's
finding, because a mechanism
that fires equally under all three phi cannot produce a result that appears under
two of them and not the third. the phi split therefore keeps the reading it had,
and a second hypothesis is not constructed here to replace it; that goes to the
research chat.


### 5.2 the effective cardinality, and it is not where the deficit is

measured in c3-e. section 3.3 found that under phi_ls and phi_cw 32 to 47 per
cent of nsga-ii's outside points lie more than 0.1 from R while under phi_lu they
hug the boundary within 0.05, and a point far from R occupies a front slot
without contributing coverage. if that is what the deficit is then section 5
reads its percentile at the wrong k: a 100-row front with 25 far rows covers R
like a smaller front, and it should be compared against a uniform draw of about
75 and not of 100.

**the stated distance is 0.10, and the reason is that it is section 3.3's own
cut.** that is the distance at which section 3.3 measured the phi split in the
outside points, so reading the percentile at it tests exactly the hypothesis
section 3.3 raises and no other. the choice is not forced and it is not made
load-bearing: 0.02, 0.05 and 0.20 are reported beside it, and so is a companion
that states no distance at all, the number of front rows that are the nearest
front row to at least one point of the 20000-point region sample. that last is
"the rows that contribute any coverage" with no cut to choose, and it is the
number of non-empty voronoi cells of the front within R.

distance to R is measured against a uniform sample of the region of 150000
points, whose own resolution is about 0.002, which is the sample section 3.3
used. a point inside R is at distance zero.

    phi  seed  outside/100   distance to R: med   q90     max   |  k_eff at 0.02  0.05  0.10  0.20   voronoi
    lu   11    36            0.0301  0.0694  0.1100            |          79    94    99   100     86
    lu   12    52            0.0238  0.0631  0.1256            |          70    91    99   100     80
    lu   13    39            0.0232  0.0586  0.1702            |          80    94    97   100     84
    lu   14    51            0.0274  0.0682  0.1704            |          71    89    99   100     79
    lu   15    44            0.0241  0.0927  0.1361            |          77    86    96   100     82
    ls   11    50            0.0666  0.1330  0.2602            |          59    68    87    98     75
    ls   12    48            0.0869  0.1569  0.2119            |          56    64    80    98     66
    ls   13    57            0.0684  0.1632  0.2223            |          54    64    81    97     72
    ls   14    44            0.0836  0.1408  0.1659            |          60    66    89   100     72
    ls   15    40            0.0752  0.1498  0.3485            |          70    76    86    97     77
    cw   11    46            0.0509  0.1582  0.2072            |          64    77    85    97     73
    cw   12    52            0.0705  0.1263  0.1982            |          59    69    83   100     72
    cw   13    56            0.0764  0.1495  0.1886            |          53    63    81   100     68
    cw   14    43            0.0786  0.1286  0.2388            |          64    74    86    99     74
    cw   15    38            0.0584  0.1563  0.1624            |          69    79    89   100     82

the uniform-draw distribution at every k a percentile is read at below, measured
exactly as section 2.2 measures it, 1000 uniform k-point draws of the same
20000-point region sample at the same seed. the k = 100 rows are section 2.2's
own and reproduce it:

    phi  k     mean    sd      min     q25     median  q75     q90     q95     q99     max
    lu    70   0.1692  0.0614  0.0863  0.1233  0.1508  0.2011  0.2554  0.2924  0.3648  0.4242
    lu    71   0.1647  0.0570  0.0890  0.1202  0.1512  0.1945  0.2468  0.2821  0.3253  0.4114
    lu    77   0.1603  0.0566  0.0874  0.1159  0.1463  0.1881  0.2415  0.2737  0.3350  0.4603
    lu    79   0.1598  0.0563  0.0772  0.1165  0.1450  0.1900  0.2406  0.2706  0.3353  0.4370
    lu    80   0.1595  0.0573  0.0806  0.1152  0.1463  0.1868  0.2451  0.2706  0.3419  0.4844
    lu    82   0.1561  0.0569  0.0815  0.1137  0.1393  0.1869  0.2383  0.2693  0.3360  0.4330
    lu    84   0.1515  0.0521  0.0765  0.1131  0.1372  0.1778  0.2246  0.2556  0.3227  0.4218
    lu    86   0.1505  0.0529  0.0812  0.1107  0.1337  0.1768  0.2299  0.2621  0.3150  0.3857
    lu    89   0.1496  0.0534  0.0799  0.1079  0.1322  0.1793  0.2333  0.2558  0.2981  0.3594
    lu    91   0.1500  0.0544  0.0768  0.1101  0.1335  0.1794  0.2298  0.2572  0.3167  0.4250
    lu    94   0.1465  0.0530  0.0762  0.1062  0.1283  0.1741  0.2237  0.2498  0.3124  0.4034
    lu    96   0.1452  0.0502  0.0726  0.1055  0.1295  0.1723  0.2237  0.2448  0.2849  0.3571
    lu    97   0.1441  0.0519  0.0786  0.1044  0.1252  0.1723  0.2198  0.2520  0.2964  0.3519
    lu    99   0.1423  0.0506  0.0743  0.1036  0.1275  0.1659  0.2156  0.2457  0.2898  0.3735
    lu   100   0.1420  0.0511  0.0773  0.1030  0.1254  0.1691  0.2125  0.2405  0.3105  0.4396
    ls    54   0.2937  0.0504  0.2016  0.2582  0.2860  0.3184  0.3565  0.3836  0.4542  0.5684
    ls    56   0.2883  0.0499  0.1902  0.2532  0.2787  0.3167  0.3517  0.3746  0.4443  0.6036
    ls    59   0.2856  0.0506  0.1961  0.2486  0.2749  0.3125  0.3524  0.3851  0.4454  0.5166
    ls    60   0.2843  0.0528  0.1898  0.2472  0.2740  0.3075  0.3511  0.3897  0.4551  0.5943
    ls    64   0.2720  0.0460  0.1902  0.2382  0.2638  0.2973  0.3342  0.3579  0.4038  0.6686
    ls    66   0.2675  0.0454  0.1786  0.2358  0.2586  0.2883  0.3238  0.3553  0.4212  0.5093
    ls    68   0.2622  0.0425  0.1773  0.2322  0.2530  0.2854  0.3195  0.3445  0.3934  0.4725
    ls    70   0.2633  0.0461  0.1845  0.2288  0.2543  0.2889  0.3271  0.3528  0.3994  0.4537
    ls    72   0.2582  0.0442  0.1726  0.2278  0.2510  0.2801  0.3147  0.3404  0.3948  0.5073
    ls    75   0.2537  0.0448  0.1750  0.2219  0.2440  0.2755  0.3136  0.3349  0.3984  0.5073
    ls    76   0.2520  0.0431  0.1694  0.2204  0.2444  0.2739  0.3081  0.3327  0.3896  0.4970
    ls    77   0.2505  0.0431  0.1768  0.2198  0.2420  0.2727  0.3053  0.3328  0.3934  0.4750
    ls    80   0.2432  0.0393  0.1670  0.2166  0.2362  0.2616  0.2948  0.3178  0.3773  0.4479
    ls    81   0.2451  0.0426  0.1700  0.2161  0.2359  0.2642  0.3019  0.3263  0.3763  0.5183
    ls    86   0.2377  0.0388  0.1643  0.2101  0.2307  0.2583  0.2905  0.3074  0.3626  0.4530
    ls    87   0.2380  0.0412  0.1677  0.2094  0.2304  0.2550  0.2889  0.3240  0.3779  0.4433
    ls    89   0.2326  0.0376  0.1654  0.2069  0.2255  0.2496  0.2828  0.3075  0.3435  0.4618
    ls    97   0.2259  0.0369  0.1610  0.2004  0.2191  0.2425  0.2728  0.2989  0.3468  0.4615
    ls    98   0.2251  0.0387  0.1562  0.1978  0.2171  0.2441  0.2745  0.2979  0.3533  0.4449
    ls   100   0.2232  0.0373  0.1549  0.1975  0.2166  0.2430  0.2698  0.2919  0.3483  0.4211
    cw    53   0.2373  0.0391  0.1653  0.2082  0.2304  0.2598  0.2891  0.3113  0.3498  0.5038
    cw    59   0.2283  0.0380  0.1536  0.2003  0.2219  0.2482  0.2787  0.2961  0.3507  0.4012
    cw    63   0.2208  0.0357  0.1485  0.1962  0.2149  0.2410  0.2648  0.2864  0.3355  0.3918
    cw    64   0.2192  0.0359  0.1557  0.1923  0.2122  0.2375  0.2697  0.2886  0.3231  0.3828
    cw    68   0.2130  0.0349  0.1514  0.1877  0.2062  0.2298  0.2635  0.2825  0.3144  0.3973
    cw    69   0.2136  0.0368  0.1443  0.1876  0.2061  0.2327  0.2619  0.2812  0.3343  0.4221
    cw    72   0.2065  0.0321  0.1344  0.1837  0.2005  0.2245  0.2484  0.2677  0.2957  0.4017
    cw    73   0.2066  0.0339  0.1434  0.1822  0.2011  0.2230  0.2527  0.2738  0.3160  0.3464
    cw    74   0.2055  0.0350  0.1430  0.1814  0.1986  0.2228  0.2503  0.2738  0.3253  0.3693
    cw    77   0.2011  0.0335  0.1403  0.1777  0.1946  0.2166  0.2437  0.2631  0.3084  0.4481
    cw    79   0.1987  0.0320  0.1404  0.1752  0.1922  0.2156  0.2438  0.2619  0.2883  0.3269
    cw    81   0.1951  0.0297  0.1313  0.1740  0.1911  0.2117  0.2343  0.2523  0.2815  0.3224
    cw    82   0.1958  0.0328  0.1398  0.1728  0.1892  0.2116  0.2372  0.2567  0.2966  0.3731
    cw    83   0.1950  0.0311  0.1385  0.1717  0.1892  0.2119  0.2348  0.2556  0.2899  0.3312
    cw    85   0.1917  0.0307  0.1360  0.1699  0.1863  0.2080  0.2319  0.2487  0.2906  0.3361
    cw    86   0.1917  0.0318  0.1321  0.1686  0.1857  0.2096  0.2358  0.2488  0.2847  0.3339
    cw    89   0.1890  0.0308  0.1217  0.1676  0.1827  0.2043  0.2308  0.2459  0.2838  0.3454
    cw    97   0.1817  0.0288  0.1284  0.1611  0.1753  0.1964  0.2198  0.2378  0.2708  0.3237
    cw    99   0.1799  0.0287  0.1260  0.1604  0.1745  0.1936  0.2173  0.2340  0.2767  0.3681
    cw   100   0.1783  0.0270  0.1267  0.1591  0.1733  0.1910  0.2147  0.2318  0.2606  0.3204

and the percentile of each run's own fill distance, read at k = 100 as section 5
reads it and then at each effective k:

    phi  seed  fill     pct at k = 100   at 0.02   0.05   0.10   0.20   voronoi
    lu   11    0.1100   33.0             17.4      29.7   31.5   33.0   23.9
    lu   12    0.1229   48.7             24.8      41.9   47.8   48.7   33.7
    lu   13    0.1211   46.8             31.2      44.0   47.8   46.8   36.5
    lu   14    0.1404   59.7             43.3      54.7   58.1   59.7   48.0
    lu   15    0.1202   45.4             29.8      39.1   42.7   45.4   34.2
    ls   11    0.3352   98.3             85.4      93.6   96.1   98.4   95.0
    ls   12    0.2670   89.1             40.4      53.1   78.0   86.9   57.4
    ls   13    0.3337   98.3             82.6      89.8   95.6   98.5   93.3
    ls   14    0.3126   97.2             77.1      86.3   95.5   97.2   89.0
    ls   15    0.2571   84.7             52.2      61.6   74.4   84.1   64.3
    cw   11    0.2321   95.0             69.8      85.3   90.1   93.0   81.2
    cw   12    0.2549   98.4             78.9      86.6   94.7   98.4   91.7
    cw   13    0.2557   98.7             72.4      85.8   96.0   98.7   87.8
    cw   14    0.2462   97.8             80.4      89.4   94.4   97.1   89.4
    cw   15    0.2152   90.1             60.4      74.8   82.6   90.1   77.2

**the percentiles move, and they do not move to the middle.** at the stated 0.10
the effective cardinality is 96 to 99 under phi_lu and 80 to 89 under phi_ls and
phi_cw, so the correction is from 100 to about 85, and it buys 2 to 11 percentile
points: the median falls from 97.2 to 95.5 under phi_ls and from 97.8 to 94.4
under phi_cw, while under phi_lu it does not move at all, 46.8 to 47.8. all ten
measurements under the two failing phi are still at or above the 74th percentile
and six of them are still above the 94th. the assumption-free companion says the
same and splits less: 66 to 82 of the 100 rows carry a non-empty voronoi cell
under phi_ls and phi_cw against 79 to 86 under phi_lu, and reading the percentile
there leaves phi_ls at 57 to 95 and phi_cw at 77 to 92.

only the most aggressive cut moves the number substantially, 0.02, and it moves
it by discarding a third of the front: phi_ls lands at 40 to 85 and phi_cw at 60
to 80. **a correction that has to remove a third of the rows before the number
moves is describing the front, not correcting the reading of it.**

so the answer to the question this part asked is no. wasted slots are real, they
are larger under phi_ls and phi_cw than under phi_lu, and they account for a
small part of the deficit and not for it. random search, for contrast, has almost
none: at the 0.10 cut it loses at most one row of the 586 to 622 it returns under
phi_lu, 14 to 19 of 2182 to 2256 under phi_ls and 11 to 24 of 1501 to 1591 under
phi_cw, which is at most 1.6 per cent of the front under any phi against
nsga-ii's 11 to 20. **section 5's finding is measured at equal
nominal cardinality, it stands as measured, and nothing in it is restated on the
strength of this section.**


### 5.3 spread in the image space against spread in the decision space

measured in c3-e. nsga-ii optimises spread in the 2m-dimensional image space,
through a crowding distance computed per image column and summed, while section 5
measures coverage in the two-dimensional decision space. section 5.1 established
that from generation three or four onwards that crowding distance is the whole of
the selection. so the open question is what uniform image-space spread becomes
when it is pulled back, and whether that differs across phi.

the measurement is section 2.2's, moved into the image and nothing else changed.
the image of R is the same fixed 20000-point uniform sample of R that every fill
distance in this document is taken over, pushed through phi by
src/reference_fronts.py's transformed_image. **each column is divided by its range
over that image, because that is the normalisation the crowding distance applies**,
and the unnormalised reading is carried beside it as a robustness column. the
comparison distribution is 1000 uniform k-point draws of that same image, drawn
with the same generator and the same seed as the decision-space draws, so at one k
the image draws are the images of the same index draws and the two readings are
paired rather than merely parallel.

three checks before the numbers, because the whole of this section is a
comparison of two estimators and an error in either would produce a split of its
own. the solver's own output is used and no image is recomputed: run.front is
bit-identical to the image of run.decision_vectors under phi over all thirty runs,
maximum absolute difference 0.000e+00. the nearest-neighbour route used here, a
kd-tree rather than the squared-norm expansion, reproduces
tests/test_validation.py's own fill_distance to 1.6e-15 and reproduces its
1000-draw distribution at k = 100 to 7.0e-15, so the distributions in 5.2 and the
decision-space column below are the gate's own numbers and not a second estimate
of them. and the decision-space percentiles below reproduce section 5's published
33, 49, 47, 60 and 45 exactly.

    solver         phi  seed     k   decision: fill    mean   pct  |  image, normalised: fill    mean   pct  |  image, raw: pct
    nsga2          lu     11   100     0.1100   0.1420    33  |              0.1013   0.3004     0  |             1
    nsga2          lu     12   100     0.1229   0.1420    49  |              0.0899   0.3004     0  |             0
    nsga2          lu     13   100     0.1211   0.1420    47  |              0.1021   0.3004     0  |             1
    nsga2          lu     14   100     0.1404   0.1420    60  |              0.1394   0.3004     5  |             6
    nsga2          lu     15   100     0.1202   0.1420    45  |              0.1140   0.3004     1  |             1
    nsga2          ls     11   100     0.3352   0.2232    98  |              0.3092   0.2576    86  |            64
    nsga2          ls     12   100     0.2670   0.2232    89  |              0.2637   0.2576    61  |            74
    nsga2          ls     13   100     0.3337   0.2232    98  |              0.3086   0.2576    85  |            88
    nsga2          ls     14   100     0.3126   0.2232    97  |              0.2439   0.2576    45  |            70
    nsga2          ls     15   100     0.2571   0.2232    85  |              0.2108   0.2576    17  |            65
    nsga2          cw     11   100     0.2321   0.1783    95  |              0.2827   0.2807    59  |            80
    nsga2          cw     12   100     0.2549   0.1783    98  |              0.3002   0.2807    71  |            82
    nsga2          cw     13   100     0.2557   0.1783    99  |              0.2484   0.2807    31  |            68
    nsga2          cw     14   100     0.2462   0.1783    98  |              0.2973   0.2807    69  |            47
    nsga2          cw     15   100     0.2152   0.1783    90  |              0.2921   0.2807    66  |            71
    random_search  lu     11   610     0.0520   0.0586    48  |              0.0448   0.1287     1  |             0
    random_search  lu     12   622     0.0427   0.0574    23  |              0.0586   0.1244     7  |             8
    random_search  lu     13   590     0.0455   0.0588    33  |              0.0519   0.1273     3  |             2
    random_search  lu     14   586     0.0503   0.0595    46  |              0.0431   0.1295     0  |             1
    random_search  lu     15   608     0.0435   0.0584    24  |              0.0397   0.1265     0  |             0
    random_search  ls     11  2220     0.0516   0.0501    67  |              0.0690   0.0586    91  |            20
    random_search  ls     12  2253     0.0465   0.0494    33  |              0.0472   0.0576     3  |            22
    random_search  ls     13  2256     0.0518   0.0495    71  |              0.0521   0.0578    25  |            38
    random_search  ls     14  2195     0.0486   0.0502    43  |              0.0530   0.0586    23  |             9
    random_search  ls     15  2182     0.0493   0.0503    50  |              0.0505   0.0592    10  |            45
    random_search  cw     11  1544     0.0463   0.0494    33  |              0.0653   0.0838     4  |            27
    random_search  cw     12  1528     0.0465   0.0497    34  |              0.0679   0.0846     7  |            63
    random_search  cw     13  1591     0.0471   0.0481    50  |              0.0720   0.0822    24  |            39
    random_search  cw     14  1501     0.0486   0.0497    50  |              0.0661   0.0845     4  |            53
    random_search  cw     15  1504     0.0449   0.0497    18  |              0.0749   0.0840    26  |            40

**the reading fixed in advance is the first of the three, and it holds with one
wrinkle that has to be stated rather than smoothed.** under phi_ls and phi_cw,
where the decision-space percentile is 85 to 99, the image-space percentile is 17
to 86 and 31 to 71. nsga-ii is not worse than a uniform draw at the thing it
actually optimises under either of the two phi where it fails the gate: it is
indistinguishable from one. the deficit is in the pullback.

the wrinkle is phi_lu, where the reading anticipated "middling" and the
measurement is 0.1 to 4.9. nsga-ii does not merely match a uniform draw of the
phi_lu image, it covers that image better than 95 to 99 per cent of them. so the
image-space percentile is not middling under all three phi, and the phi split does
not disappear in the image space; it changes size and sign. **what the section
establishes is the negative half, and it is the half section 5 needed: the
deficit under phi_ls and phi_cw is not present in the space nsga-ii sorts and
spreads in.** what it does not establish is that the map alone carries the
difference, and 5.4 is why that cannot be assumed either.

the raw column, the same measurement without the per-column normalisation, moves
individual numbers by up to 30 percentile points and changes none of that.


### 5.4 the jacobian of the map

measured in c3-e, and reported as a measured quantity with the reading beside it.
a map close to a similarity carries spread from one space to the other; one that
is strongly anisotropic does not. the map is x -> the four image columns, its
jacobian is the four gradients of b1 section 1.1's image coordinates, every one
of them a constant hessian times x plus a constant vector, so it is available in
closed form:

    phi_lu   (2 x_1,  (3/2) x_2 - 2)   (2 x_1,  (5/2) x_2 - 2)
             ((3/2) x_1 - 2,  2 x_2 - 2)   ((5/2) x_1 - 2,  2 x_2 - 2)
    phi_ls   (2 x_1,  (3/2) x_2 - 2)   (0,  x_2)
             ((3/2) x_1 - 2,  2 x_2 - 2)   (x_1,  0)
    phi_cw   (2 x_1,  2 x_2 - 2)   (0,  x_2 / 2)
             (2 x_1 - 2,  2 x_2 - 2)   (x_1 / 2,  0)

checked against central differences of src/reference_fronts.py's own
transformed_image on 400 random points of the box, maximum absolute difference
7.6e-10 under each phi, which is the step size and not a disagreement.

the ratio of largest to smallest singular value of that 4 x 2 jacobian, over the
same 20000-point uniform sample of R the fill distance is taken over. **raw** is
the map as written; **scaled** divides each image column by its range over the
image of R, which is the map 5.3 actually measures and the one the crowding
distance works in:

    raw
    phi   mean     sd      min     q10     q25     median  q75     q90     q99     max     > 3      > 10
    lu    3.0493  0.6236  1.8492  2.2789  2.6425  2.9622  3.4057  3.8621  4.9367  5.6229   46.9%    0.0%
    ls    1.8011  0.4454  1.0048  1.3111  1.5091  1.6909  2.0310  2.4527  3.0988  3.2870    1.8%    0.0%
    cw    2.1546  0.6706  1.0089  1.3965  1.6735  2.0216  2.4726  3.1646  3.9932  4.2500   13.1%    0.0%

    scaled
    phi   mean     sd      min     q10     q25     median  q75     q90     q99     max     > 3      > 10
    lu    4.1961  1.0795  2.2193  2.9744  3.3660  3.9719  4.9352  5.8519  6.7666  7.0180   89.2%    0.0%
    ls    1.4961  0.3471  1.0016  1.1229  1.2325  1.4162  1.6961  1.9617  2.6383  3.0779    0.1%    0.0%
    cw    1.4721  0.3154  1.0012  1.0823  1.2018  1.4463  1.6835  1.9079  2.3364  2.6061    0.0%    0.0%

**the reading, and it points the wrong way for a distortion story.** under the
scaled map, the one the operator works in, phi_lu is the anisotropic one, median
3.97 with 89 per cent of R above a ratio of 3, and phi_ls and phi_cw are close to
similarities, medians 1.42 and 1.45 with essentially nothing above 3. if
anisotropy of the pullback were what turns good image spread into bad decision
coverage then phi_lu should be the phi where that happens, and phi_lu is the one
where it does not happen. no ratio anywhere in the table exceeds 10, so no phi's
map is strongly distorting on this problem by any ordinary standard.

**one exact fact the table would otherwise hide, and it is the useful one.**
g_lu = A g_cw exactly, for every x, with

    A = [[1, -1, 0, 0], [1, 1, 0, 0], [0, 0, 1, -1], [0, 0, 1, 1]],   A^T A = 2 I

so A is sqrt(2) times an orthogonal matrix, J_lu = A J_cw pointwise, the singular
values of J_lu are exactly sqrt(2) times those of J_cw, and **the raw ratio of
phi_lu and the raw ratio of phi_cw are identical at every point of the box.**
verified to 7.1e-15 over 500 random points. the two raw rows above differ, 3.05
against 2.15, only because each is averaged over its own region, X_lu against
X_cw. **so the apparent difference between phi_lu's map and phi_cw's map is a
difference of region and not of map at all**, and any statement about "the phi_lu
map being more distorting" is, for those two phi, a statement about where it is
averaged. this is what c3-f takes up.

three phi is three data points and none of this is promoted to a mechanism here.


### 5.5 the frame, the control, and where phi_ls sits

measured in c3-f, which starts from 5.4's exact identity. since g_lu = A g_cw with
A a similarity, the phi_lu image and the phi_cw image of any decision set are the
same geometric object up to a rotation and a uniform scaling. crowding distance is
computed per column and normalised by column range, so it is not rotation
invariant: the two phi present the same shape to the operator in two alignments to
the axes it measures along. that is a testable candidate and this section tests it,
then runs the control that separates the operator from the order, then asks where
phi_ls sits.

**the instrument, and its assertion.** a front produced under one phi can be read
in another phi's frame because the three images are constant linear images of one
another. the frame change is checked three ways: reading a decision set in frame
f reproduces src's own image under phi_f exactly, difference 0.000e+00 under all
three; g_lu = A g_cw and g_ls = B g_cw hold to 0.000e+00 on all three region
samples; and, since A^T A = 2 I, every raw distance in the lu frame must be
exactly sqrt(2) times the same distance in the cw frame. that last is the check
that the rotation is implemented right and it is asserted, not inspected: over all
thirty runs the maximum relative departure of the raw image fill distance from the
sqrt(2) factor is 4.5e-15.

**the harness is a session diagnostic and is not committed**, as c3-d's was: it
adds no module and changes no file under src/ or tests/, and this is what it would
take to rebuild it. it imports tests/test_validation.py as a module and takes
region_sample, in_region, fill_distance, fill_distances, solver_runs and every
seed and size constant from it, so no region, no draw and no estimator is defined
a second time; that import is the reason the decision-space columns here are the
gate's own numbers rather than a second estimate of them. it adds four things.
nearest-neighbour distances go through scipy.spatial.cKDTree rather than the
squared-norm expansion, which is what makes 1000 draws at k = 2256 affordable and
is checked against the expansion to 1.6e-15 and against tv.fill_distances to
7.0e-15; scipy is not added to requirements.txt and nothing committed depends on
it. the image of a decision set in a stated frame is
transformed_image composed with a constant 4 x 4 matrix, A or B or the identity.
the jacobian is the closed form of 5.4, checked against central differences. and
the crowding distance is pymoo's own calc_crowding_distance from
operators/survival/rank_and_crowding/metrics.py, called on a front's image and
never reimplemented. the region areas are the closed forms of 5.5, checked against
scipy.integrate.quad and against a monte carlo of tests/test_validation.py's own
in_region.

#### the frame test

each row is one nsga-ii run. **the decision set and the region R are the run's own
and do not move; only the frame the image is read in moves**, so a difference along
a row is alignment and normalisation and nothing else. each cell is the fill
distance and its percentile against 1000 uniform draws of that region read in that
frame. the diagonal, frame = the run's own phi, is 5.3's normalised column:

    run phi  seed   frame lu          frame ls          frame cw
    lu        11    0.1013    0.5     0.1681   15.9     0.1762   13.5
    lu        12    0.0899    0.1     0.1700   16.8     0.1744   12.9
    lu        13    0.1021    0.5     0.1625   12.5     0.1773   14.4
    lu        14    0.1394    4.9     0.2365   46.9     0.2475   46.0
    lu        15    0.1140    0.8     0.1810   20.7     0.1839   16.4
    ls        11    0.2638   46.7     0.3092   85.6     0.3120   77.9
    ls        12    0.3077   66.7     0.2637   61.4     0.2682   52.7
    ls        13    0.3584   81.7     0.3086   85.4     0.3211   80.7
    ls        14    0.2960   62.8     0.2439   45.1     0.2629   48.8
    ls        15    0.2758   52.6     0.2108   17.1     0.2211   18.0
    cw        11    0.2865   78.1     0.2759   58.8     0.2827   59.2
    cw        12    0.2949   80.5     0.2926   69.5     0.3002   70.7
    cw        13    0.2561   66.6     0.2489   36.1     0.2484   30.7
    cw        14    0.2182   44.3     0.2914   69.3     0.2973   69.3
    cw        15    0.2633   69.2     0.2916   69.4     0.2921   65.9

**the alignment hypothesis is refuted, and cleanly.** it predicts that a phi_cw
front rotated into phi_lu's alignment should acquire phi_lu's advantage. it does
not: the phi_cw runs read in the lu frame sit at 44.3 to 80.5, worse than in their
own frame and nowhere near the phi_lu runs' 0.1 to 4.9. and the converse fails in
the same direction: the phi_lu runs read in the cw frame stay at 12.9 to 46.0,
still better than any phi_cw run in any frame. **the phi_lu advantage travels with
the run and not with the frame.**

the crowding distance itself, which is the quantity that is genuinely not rotation
invariant, says the operator is working correctly and says nothing that splits by
phi. pymoo's own calc_crowding_distance on the same front in each frame, over the
finite members, with the coefficient of variation as the number a
spread-equalising operator drives down:

    run phi  seed   frame lu: inf  mean    cv     | frame ls: inf  mean    cv     | frame cw: inf  mean    cv
    lu        11         5  0.0202  0.2810 |            5  0.0204  0.4330 |            7  0.0204  0.4703
    lu        12         7  0.0207  0.2512 |            5  0.0204  0.3832 |            6  0.0203  0.4125
    lu        13         6  0.0205  0.2900 |            6  0.0192  0.5387 |            7  0.0196  0.5001
    lu        14         5  0.0201  0.3158 |            6  0.0204  0.4422 |            7  0.0208  0.4806
    lu        15         5  0.0204  0.2678 |            5  0.0207  0.3884 |            6  0.0206  0.4058
    ls        11         6  0.0202  0.7128 |            8  0.0202  0.3091 |            8  0.0203  0.3893
    ls        12         6  0.0205  0.6367 |            8  0.0208  0.2404 |            8  0.0206  0.3360
    ls        13         6  0.0198  0.6003 |            7  0.0203  0.3120 |            7  0.0204  0.3366
    ls        14         6  0.0201  0.4111 |            7  0.0204  0.2354 |            7  0.0204  0.2627
    ls        15         6  0.0191  0.8775 |            7  0.0199  0.4264 |            6  0.0198  0.4854
    cw        11         6  0.0204  0.6097 |            7  0.0207  0.3114 |            8  0.0205  0.2549
    cw        12         6  0.0202  0.4477 |            8  0.0203  0.2663 |            8  0.0206  0.2483
    cw        13         6  0.0202  0.5827 |            7  0.0200  0.2940 |            7  0.0202  0.2954
    cw        14         6  0.0200  0.5793 |            8  0.0200  0.3177 |            8  0.0202  0.2981
    cw        15         6  0.0201  0.5426 |            7  0.0202  0.3043 |            8  0.0206  0.2795

**the profile is alignment-sensitive, and it is alike across phi.** in every one of
the fifteen runs the coefficient of variation is lowest in the run's own frame,
which is the operator doing exactly what it is supposed to do and is the best
instrument check in this document: the crowding distance really is equalised, and
really is frame-dependent. but the diagonal values are 0.25 to 0.32 under phi_lu,
0.24 to 0.43 under phi_ls and 0.25 to 0.30 under phi_cw, which is one behaviour and
not three. **the operator does not equalise better under one phi than another, so
its alignment is not what distinguishes them.**

#### the control that separates operator from order

random search is phi-neutral by construction: c1's sample is a pure function of the
box, the budget and the seed, so the three phi filter one identical draw and the
order is isolated exactly. at seed 11 that one draw yields fronts of 610, 2220 and
1544 rows under phi_lu, phi_ls and phi_cw, and at seed 12, 622, 2253 and 1528.

read at its own cardinality it shows no deficit anywhere, which 5.3 already
carried. the measurement that decides the question is at **matched cardinality**:
twenty uniform 100-row subsamples of each random-search front, read against the
same k = 100 distribution nsga-ii is read against, so region, cardinality and
comparator are all held fixed and the only difference between the two solvers is
the solver. median over the twenty:

    phi  seed   decision: fill    pct   | image: fill    pct
    lu     11       0.0969   15.3       |     0.1528    8.2
    lu     12       0.1070   29.4       |     0.1302    3.0
    lu     13       0.1013   21.9       |     0.1290    2.9
    lu     14       0.0968   14.8       |     0.1306    3.5
    lu     15       0.0952   12.7       |     0.1195    1.4
    ls     11       0.2253   61.2       |     0.2455   46.1
    ls     12       0.1944   21.4       |     0.2277   31.1
    ls     13       0.2084   39.0       |     0.2296   33.0
    ls     14       0.1977   25.2       |     0.2125   17.9
    ls     15       0.2275   63.2       |     0.2330   35.9
    cw     11       0.1693   42.4       |     0.2467   29.2
    cw     12       0.1652   35.0       |     0.2665   46.8
    cw     13       0.1711   45.7       |     0.2549   36.8
    cw     14       0.1730   48.7       |     0.2571   38.5
    cw     15       0.1631   31.1       |     0.2338   18.0

**at matched cardinality random search has no deficit under any phi**: 12.7 to 29.4
under phi_lu, 21.4 to 63.2 under phi_ls, 31.1 to 48.7 under phi_cw, every one of
the fifteen at or below the 64th percentile and thirteen of them below the
median.
nsga-ii at the same k on the same regions against the same comparator is at 33 to
60, 85 to 98 and 90 to 99. **random search shows no phi split of the kind nsga-ii
shows, so the split is the operator meeting the order and not a property of the
phi-efficient sets that any method at fixed cardinality would inherit.**

#### the dimensional check, and what the control does to it

a k-point cover of a region of area |R| has a fill distance of order
sqrt(|R| / k), so dividing by that removes region size. the three areas are
available in closed form from b1 section 2.4's inequalities, X_cw being the unit
square and the other two the integrals of the binding curves:

    |X_lu| = |X_ls| - (16/3 - 64 ln(16/15)) = 0.310533
    |X_ls| = (1/49)(112/3 + 64 ln(16/9))    = 1.513401
    |X_cw| = 1 exactly

against the box's area of 4 that is 7.8, 37.8 and 25.0 per cent, which is b1's "a
twelfth, three eighths and a quarter". the closed forms agree with adaptive
quadrature to 3.9e-16 and with a 4-million-point monte carlo of the gate's own
in_region predicate to 7e-4.

    phi   |R|        sqrt(|R|/100)   uniform mean at k=100   uniform / sqrt(|R|/k)
    lu    0.310533   0.055725        0.1420                  2.548
    ls    1.513401   0.123020        0.2232                  1.814
    cw    1.000000   0.100000        0.1783                  1.783

**the last column is the one that matters and it is not flat.** it is what a
uniform draw achieves in units that have had region size divided out, so it is a
pure measure of region shape, and a uniform draw covers X_lu 40 per cent worse for
its area than it covers X_ls or X_cw. X_lu is a thin curved sliver between two
conic boundaries; the other two are fat. so the comparator section 5 measures
against is itself region-dependent, and it is weakest exactly under the phi where
nsga-ii looks best.

that is a real effect and it is not the whole effect. in units of the uniform mean
at the same k, where 1.00 is a front that covers R exactly as well as a uniform
100-point draw does:

    phi   nsga-ii, five seeds                    mean  |  random search at k = 100          mean
    lu    0.775 0.865 0.852 0.989 0.847         0.866  |  0.683 0.753 0.713 0.681 0.671    0.700
    ls    1.502 1.196 1.495 1.400 1.152         1.349  |  1.009 0.871 0.934 0.886 1.019    0.944
    cw    1.301 1.430 1.434 1.381 1.207         1.351  |  0.949 0.927 0.960 0.970 0.915    0.944

and the swing from phi_lu to each of the others decomposes:

    phi        nsga-ii   random search   the part the phi-neutral control carries
    lu -> ls   +0.483    +0.243          50%
    lu -> cw   +0.485    +0.244          50%

**half of the phi swing is carried by a method that has no operator, no crowding
distance and no population, and half is not.** the control's half is the region
effect the shape column measures: any fixed-cardinality method looks better on
X_lu than on X_ls or X_cw because a uniform draw of X_lu is a weaker thing to be
compared against. the other half is nsga-ii's own, and it is what carries the
front over the tolerance. the two halves coming out at 50 per cent under both phi,
to three decimal places, is a coincidence of two numbers and is not read as
anything.

the gap between the solvers at the same k, the same region and the same
comparator is +0.165 under phi_lu, +0.405 under phi_ls and +0.406 under phi_cw:
nsga-ii covers worse than the control under every phi, and about two and a half
times worse under the two where the gate fails.

#### where phi_ls sits

phi_ls is not related to the other two as they are related to each other, and this
is exact. all three images are constant linear images of one another, because each
phi is a constant linear map of the endpoint pair, [1] section 2. writing
g_lu = A g_cw and g_ls = B g_cw:

    A,      lu <- cw    singular values  sqrt2, sqrt2, sqrt2, sqrt2    ratio 1
    B,      ls <- cw    singular values  2.288246 twice, 0.874032 twice  ratio 2.618034
    A B^-1, lu <- ls    singular values  1.618034 twice, 0.618034 twice  ratio 2.618034

with

    A^T A = 2 I
    B^T B = [[1, -1, 0, 0], [-1, 5, 0, 0], [0, 0, 1, -1], [0, 0, -1, 5]]

**B is not a similarity and the numbers are closed-form.** B^T B is block diagonal
with two copies of [[1, -1], [-1, 5]], whose eigenvalues are 3 +- sqrt 5, so B's
singular values are sqrt(3 + sqrt 5) = 2.288246 and sqrt(3 - sqrt 5) = 0.874032,
each twice, and its condition number is exactly

    (3 + sqrt 5) / (3 - sqrt 5)  under the square root  =  (1 + sqrt 5)^2 / 4  =  2.618034

which is the golden ratio squared. the map from the phi_ls image to the phi_lu
image has singular values exactly phi and 1/phi and the same condition number.
**so phi_lu and phi_cw present the same object in two alignments, while phi_ls
presents a genuinely sheared version of it, at a fixed anisotropy of phi^2.** that
this falls out of example 2.3's coefficient matrix, lambda = (1, 0),
beta = (-1, 1), is a structural fact about [1]'s framework rather than about this
problem or about pymoo, and it is recorded as v-56, reported here and
guarded by no assertion, this session adding none to the suite.

phi_ls is therefore the case any mechanism has to also explain, and the mechanisms
this document has examined do not. its jacobian ratio is 1.42, next to phi_cw's
1.45 and far from phi_lu's 3.97, so on 5.4's statistic it belongs with phi_cw; its
image is the sheared one of the three, so on the closed form it belongs with
neither; its region is the largest of the three; and its decision-space deficit
matches phi_cw's while its image-space percentile range, 17 to 86, is the widest.
no single one of these orders the three phi the way the finding does.

#### what 5.2 to 5.5 conclude

they conclude a decomposition and not a mechanism, and the honest statement of it
is this. **section 5's finding is measured correctly, survives every control put
to it, and is about half the size it appears.** what has been excluded is
substantial: it is not rank-1 saturation, which fires under every phi, 5.1; it is
not wasted front slots, which account for 2 to 11 percentile points of a gap of 50,
5.2; it is not that nsga-ii is bad at what it optimises, since in the image space
it is ordinary under the failing phi and exceptional under the passing one, 5.3; it
is not anisotropy of the pullback, whose ordering is the reverse of what is needed
and whose apparent phi_lu-versus-phi_cw difference is an artefact of averaging over
different regions, 5.4; and it is not the alignment of the crowding distance's
axes, which does not transfer the advantage when the frame is changed and which the
operator handles identically under all three phi, 5.5.

what has been identified is that **half the swing is region shape acting on the
comparator, measured on a phi-neutral control that has no operator at all, and half
is nsga-ii's own and remains without a mechanism.** the residual is a real,
reproducible, correctly measured property of this solver on this problem, it is
what the twelve gate failures are, and it is not explained here. **an unexplained
phi split that is correctly measured and now bounded and halved is where phase c
closes**, and CONTEXT.md section 10 e3 carries it forward as something e3 reports
rather than something e3 resolves.


## 6. the budget trend, reported and no longer asserted

section 1.5 removes the assertion. the numbers, pooled over the five seeds, at
5000 evaluations against 20000, on both measures, for all three solvers:

    solver         phi  flag   k 5000  k 20000   outside 5000    outside 20000   dominated 5000  dominated 20000  worst rev 5000  worst rev 20000
    random_search  lu   False    3016    10426   1062  35.2%     2701  25.9%      295   9.8%      410   3.9%      0.0509          0.0225
    random_search  ls   False   11106    42183   1640  14.8%     4179   9.9%      310   2.8%      371   0.9%      0.0477          0.0213
    random_search  cw   False    7668    28703   1388  18.1%     3544  12.3%      351   4.6%      435   1.5%      0.0449          0.0215
    random_search  ls   True    11106    42183   1640  14.8%     4179   9.9%      336   3.0%      407   1.0%      0.0477          0.0213
    random_search  cw   True     7668    28703   1388  18.1%     3544  12.3%      371   4.8%      460   1.6%      0.0449          0.0242
    nsga2          lu   False     500      500    222  44.4%      211  42.2%       88  17.6%       79  15.8%      0.1379          0.1296
    nsga2          ls   False     500      500    239  47.8%      242  48.4%       99  19.8%       80  16.0%      0.3309          0.3315
    nsga2          cw   False     500      500    235  47.0%      269  53.8%       98  19.6%       97  19.4%      0.2503          0.2531
    nsga2          ls   True      500      500    239  47.8%      242  48.4%      108  21.6%       89  17.8%      0.3309          0.3315
    nsga2          cw   True      500      500    235  47.0%      269  53.8%      104  20.8%      109  21.8%      0.2503          0.2531
    mopso          lu   False    1000     1000    436  43.6%      415  41.5%      212  21.2%      199  19.9%      0.0963          0.0860
    mopso          ls   False    1000     1000    304  30.4%      292  29.2%      144  14.4%      128  12.8%      0.2011          0.1758
    mopso          cw   False    1000     1000    309  30.9%      306  30.6%      134  13.4%      146  14.6%      0.1304          0.1478
    mopso          ls   True     1000     1000    304  30.4%      292  29.2%      149  14.9%      138  13.8%      0.2011          0.1758
    mopso          cw   True     1000     1000    309  30.9%      306  30.6%      145  14.5%      154  15.4%      0.1304          0.1478

the phi_lu rows are the same at both flag settings by construction and are printed
once. the dominated columns reproduce c3-b's section 6 table exactly, which is the
check that this session's runs are c3-b's runs.

read with section 1 beside it, which is the only way it should be read:

    on the exact measure, four times the budget lowers the outside fraction for
    nsga-ii and mopso under phi_lu, by 2.2 and 2.1 points, and does not lower it
    under phi_ls or phi_cw for nsga-ii, 47.8 to 48.4 and 47.0 to 53.8, nor
    materially for mopso, 30.4 to 29.2 and 30.9 to 30.6. **the split is exactly the
    split section 1 predicts.**
    the worst reverse distance behaves the same way. nsga-ii improves under phi_lu,
    0.1379 to 0.1296, and does not improve under phi_ls or phi_cw, 0.3309 to
    0.3315 and 0.2503 to 0.2531. its gate failures are not a budget problem: at
    four times the budget the same six configurations fail by the same margins.
    random search's numbers fall on every measure and none of them is a statement
    about the search: its front grows from 610 to 2058 rows under phi_lu and from
    1544 to 5726 under phi_cw, so the fraction falls mechanically while the
    absolute counts rise, 1062 to 2701 outside and 295 to 410 dominated.
    on the old sampled measure the three cells c3-b reported as failures are still
    the three that rise, mopso under phi_cw at both flag settings and nsga-ii at
    the True setting. **c3-b's three failing cells were not a measurement error;
    what was wrong was asserting a trend that no mechanism supports and that the
    proposition of section 1 forbids.**

no assertion was moved to accommodate any of this and none is made. the trend is a
number.


## 7. p0, the smoke test

b1 section 7.4: p0 is not a fixture. under phi_lu and phi_ls its optimal set is the
whole decision box, and under phi_cw it is the single point x = 0, which is the
published anchor. src/reference_fronts.py raises for p0 rather than returning
something that would pass for a front. what p0 supports is one check: **does a
solver find the published anchor x = 0.**

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

**all forty-five pass, by two orders of magnitude**, and the numbers are c3-b's
exactly.

and it must be said what that is worth. **under phi_lu and phi_ls the whole box is
optimal, b1 section 7.3, so every point of every front is an optimal solution and
finding the anchor is a weaker statement than it looks.** the k_run column shows it
directly: under phi_lu and phi_ls the recovered front is the solver's entire
output, because no point dominates any other; under phi_cw it is one row, which is
the anchor and the whole optimal set. the phi_cw column is the only one where
finding the anchor is finding the answer.


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

the set sizes behind that zero, on p1, which is what makes the zero worth reading:

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

on p0 the two sets coincide in every run, which is b1 section 7.3's table appearing
in the pipeline. r-11 records one measured violation of this containment on tier 1,
on dtlz2 at eps = 0.50, one point of 1565; **no violation occurs anywhere on tier
0** and r-11 is not retired by that.


## 9. cardinality, per r-16

every number in sections 3, 5, 6, 7 and 8 carries the front cardinality it was
computed at. nothing is truncated to a common size: r-16 is about objective-space
metrics that move with the number of rows, and hausdorff is a maximum over two
sets, so truncating a recovered set before measuring a maximum discards real
coverage and makes the measured distance a property of the subsample. CONTEXT.md
section 10 d1 records that the r-16 rule is for objective-space metrics only.

what the cardinality column carries here is the reading of two numbers. the three
solvers return 586 to 2256, exactly 100, and at most 200 rows, and the reverse
distance tracks that ordering: random search 0.036 to 0.051, mopso 0.069 to 0.201,
nsga-ii 0.110 to 0.331. **that is why the tolerance is a fill distance at a stated
k and not a number**, and it is why section 5 reads each solver against a draw of
its own cardinality before calling anything a finding. the exact quality measure
carries the same confound in the other direction: random search's outside fraction
is the smallest in the table under every phi and its absolute count is the
largest, by a factor of four to seven.


## 10. what this means for phase e

**phase e is not blocked by this gate, and the gate does not pass.** the rule is
CONTEXT.md section 8's, that c3 gates phase e if the solvers do not recover the
tier 0 sets. what the twelve failures say is not that a solver failed to recover
the set: nsga-ii returns no point that beats the derivation, its front lies on and
around the derived set, and its worst gap exceeds the resolution a 100-point
uniform draw of the region achieves at the 0.95 quantile, by 0.005 to 0.039 in a
box of side 2. **that is a statement about the uniformity of one solver's spread at
one cardinality, and it is exactly what section 5 reports as a finding.** the
derivation, its encoding in b2 and all three solvers agree about where the
efficient set is; two of the three cover it to within the derivation's own
resolution and the third does not.

phase e starts, and it carries the following from this document, none of it
optional:

    the quality measure in decision space is membership in b1 section 2.4's
        closed-form region, reported as a fraction with the cardinality beside it.
        the count of points dominated by a reference front is retired: section 3.2
        measures its bias at a factor of three and shows it moving with reference
        density in the same run.
    the forward hausdorff is reported and never asserted, and any table of e1's
        that prints one prints it beside the note that it carries the protected
        extreme of section 1. this is v-53 and v-54 and it is a property of the
        design, not a defect. a reader who takes a forward distance for a quality
        measure will rank the solvers by where their fronts' protected extremes
        fell.
    no monotone trend in budget is asserted of any solver on this problem, and any
        statement in the memoria that more budget buys a better front must carry
        section 6's numbers, in which four times the budget buys nsga-ii nothing at
        all under phi_ls and phi_cw.
    e3 must report the finding of section 5 with its numbers, CONTEXT.md section 10
        e3, and must not report nsga-ii's spread as a quality result about phi.
    include_singular_segments has no default and its value belongs in every table,
        r-12 and s-12, and the two settings are two different reference objects.
    a recovery tolerance quoted anywhere in e1 or the memoria is a quantile of a
        measured fill-distance distribution at a stated cardinality, section 2, and
        the distribution is quoted with it.

what is open, and none of it is a blocker:

    r-19, whether nsga-ii's spread should be measured or repaired, section 11,
        and after c3-e and c3-f it is halved and still open: sections 5.2 to 5.5
        exclude four candidate mechanisms, attribute half the phi swing to region
        shape acting on the comparator through a phi-neutral control, and leave
        the other half without one.
    s-12, the status of the singular segments, unchanged by this session.
    r-18, rewritten rather than closed, section 11.


## 11. open items this session raises and touches

    r-19  new. nsga-ii's decision-space coverage of a full-dimensional efficient
          set is worse than uniform random sampling at equal cardinality, under
          the two phi whose image carries a width column and not under the third,
          section 5. the gate asserts the reverse direction and nsga-ii fails it
          in twelve of ninety measurements. what is open is not the measurement
          but what to do with it: whether e1 reports nsga-ii's spread as measured,
          which is the cheap option and the one this session takes, or whether a
          decision-space diversity operator belongs in the comparison at all,
          which would be a change to c2 and is out of scope here. the answer bears
          on how e3 reads any spread statistic, d1's compute_spread included,
          since that statistic is computed in the objective space where nsga-ii
          sorts and the finding is in the decision space where the result lives.
          extended in c3-d. the crowding-distance reading of the split was put to
          a direct measurement and does not survive as an explanation: rank 1
          saturates under all three phi by generation four and never falls back,
          section 5.1, and on tier 1 it saturates at generation 3 or 4 on dtlz2's
          six columns and at 13 to 21 on zdt1's four. so the split still has a
          reading and not a mechanism, and what to do with it is still what is
          open. what c3-d adds under the same row is a second thing e2 and e3 must
          report, the rank-1 size against the population size, which is a property
          of the transformation and not of any one phi.
          extended again in c3-e and c3-f, sections 5.2 to 5.5, and the row is
          now smaller and sharper than it was. four candidate mechanisms are
          excluded by direct measurement: wasted front slots, which move the
          percentile by 2 to 11 points of a gap of 50; the pullback, since in the
          image space nsga-ii is ordinary under the two failing phi and
          exceptional under the passing one; the anisotropy of the map, whose
          ordering is the reverse of what is needed and whose phi_lu against
          phi_cw difference is an artefact of averaging over two different
          regions, the two maps being related by an exact similarity; and the
          alignment of the crowding distance's axes, which does not carry the
          advantage when a front is read in another frame and which the operator
          handles identically under all three phi. what replaces them is a
          decomposition rather than a mechanism: at matched cardinality random
          search, which is phi-neutral by construction, carries half the swing
          from phi_lu to each of the other two, +0.243 and +0.244 of +0.483 and
          +0.485 in units of the uniform mean, and nsga-ii carries the other
          half. **so half of r-19 is region shape acting on the comparator and is
          not about nsga-ii at all, and half is nsga-ii's own and is what the
          twelve gate failures are.** what is open is unchanged in kind and
          halved in size, and it is still whether e1 reports the residual or
          whether a decision-space diversity operator belongs in the comparison.

    r-18  rewritten. it said the budget trend fails under phi_cw and that no
          mechanism forces improvement. the truth is stronger and is section 1: a
          mechanism protects the offending points, so no monotone trend in budget
          is a property either population method has under phi_ls or phi_cw, and
          the assertion is removed for all three solvers rather than qualified.
          what remains open under the number is the reporting question, what a
          capped-front method's budget response should be reported as at all, and
          section 6 reports the raw numbers on both measures meanwhile.

    r-17  retired in this session and moved to docs/answered.md, section 2.4. the
          sensitivity it described was the sensitivity of a sum in which one term
          did not belong and the other was a mean of twenty draws. both causes are
          removed and the point estimate is replaced by a measured distribution.

    s-12  touched and not resolved. the two settings of include_singular_segments
          move the asserted direction by at most 0.0171 on p1 and change no
          verdict, which is a narrower statement than r-12's igd finding and does
          not retire it. the closed-form region used by correction 2's measure is
          the closed one, so no point is called outside on the strength of the
          undecided segment.

    s-13  closed in c3-b and unchanged here. section 3.2 is the general form of
          the same error: an exact question put to a sample gets the sample's
          answer.
