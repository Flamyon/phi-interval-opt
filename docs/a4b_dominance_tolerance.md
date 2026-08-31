# a4-b: the dominance tolerance decision

session a4-b, 2026-08-31. a small session with one job: decide, on measurements
rather than on judgement, what rule the whole project uses to compare two
objective rows, so that c1's random search, c2's pymoo runs and d2's coverage and
cross-evaluation cannot disagree with one another.

the problem, as a4 left it. the r-08 test in tests/test_problems_tier0.py rounds
image rows to nine decimals before taking a non-dominated set, because
(c + r) - (c - r) is not exactly 2r in double precision. that rounding is a
tolerance on the dominance relation. it lives in one test file. three other
places will compute dominance and none of them shares it. pymoo applies no
tolerance at all.

nothing in src/ implements a rule this session. the rule is recommended here and
recorded as d-02 in PROGRESS.md, open, for the research chat. what this session
does change in src/ is p1's default delta, and only because part 2 confirmed the
two claims that make the change free.

every number below is from throwaway scripts in the session scratchpad, numpy and
pymoo only, nothing committed. where a reference set is called exact it was
computed in integer arithmetic: p1's grid points are rationals with denominator
30 or 32, so every image coordinate times a fixed integer is an integer, and the
non-dominated set of those integers is the exact answer with no floating point
anywhere in it.


## part 1, the error measured

### 1.1 the two routes

p1 evaluates to endpoints. the transformed columns can be reached two ways:

    endpoint route     make_phi(lam, beta) applied to (f_l, f_u), which is what
                       CONTEXT.md section 4 and subpart a3 specify and what
                       src/phi_transforms.py builds.
    centre-radius      the same columns written in terms of c and r directly,
                       (c - r, c + r) for phi_lu, (c - r, 2r) for phi_ls,
                       (c, r) for phi_cw.

the two are the same map on the reals. they are not the same map on doubles.

### 1.2 the discrepancy, per coordinate

61 x 61 grid on [-0.5, 1.5]^2, 3721 points, delta = 1/10, rho = 1/4, against the
exact reference. "wrong" counts the points where the computed double is not the
correctly rounded exact value.

    centre offset 0           centre range [0, 4.5]
    phi_lu
      f_l  obj1   endpoint  max abs 8.882e-16  max rel 1.860e-14  wrong 2350/3721  |  centre-radius  max abs 8.882e-16  wrong 2350
      f_u  obj1   endpoint  max abs 1.332e-15  max rel 4.250e-16  wrong 1802/3721  |  centre-radius  max abs 1.332e-15  wrong 1802
      f_l  obj2   endpoint  max abs 1.332e-15  max rel 5.640e-14  wrong 2398/3721  |  centre-radius  max abs 1.332e-15  wrong 2398
      f_u  obj2   endpoint  max abs 1.332e-15  max rel 4.419e-16  wrong 1884/3721  |  centre-radius  max abs 1.332e-15  wrong 1884
    phi_ls
      f_l  obj1   endpoint  max abs 8.882e-16  max rel 1.860e-14  wrong 2350/3721  |  centre-radius  max abs 8.882e-16  wrong 2350
      2r   obj1   endpoint  max abs 7.216e-16  max rel 2.379e-15  wrong 2450/3721  |  centre-radius  max abs 2.220e-16  wrong 1647
      f_l  obj2   endpoint  max abs 1.332e-15  max rel 5.640e-14  wrong 2398/3721  |  centre-radius  max abs 1.332e-15  wrong 2398
      2r   obj2   endpoint  max abs 7.216e-16  max rel 2.379e-15  wrong 2456/3721  |  centre-radius  max abs 2.220e-16  wrong 1647
    phi_cw
      c    obj1   endpoint  max abs 8.882e-16  max rel 6.440e-15  wrong 2079/3721  |  centre-radius  max abs 8.882e-16  wrong 2053
      r    obj1   endpoint  max abs 3.608e-16  max rel 2.379e-15  wrong 2450/3721  |  centre-radius  max abs 1.110e-16  wrong 1647
      c    obj2   endpoint  max abs 8.882e-16  max rel 6.440e-15  wrong 2177/3721  |  centre-radius  max abs 8.882e-16  wrong 2162
      r    obj2   endpoint  max abs 3.608e-16  max rel 2.379e-15  wrong 2456/3721  |  centre-radius  max abs 1.110e-16  wrong 1647

at unit magnitude the two routes look alike: everything is one or two ulps. the
absolute error is not the quantity that matters and this table is not the
finding. section 1.3 is.

### 1.3 the finding: structural ties, not error size

r_1 depends on x_2 alone. on a 61-point axis it therefore takes 46 distinct
values and not 3721, and every pair of points sharing x_2 shares r_1 exactly.
that exact tie is the whole reason phi_ls and phi_cw see fewer distinct rows than
phi_lu. destroy the tie and points that were incomparable become comparable, or
worse, points that were dominated stop being dominated.

    centre offset 0
    phi_ls
      2r   obj1   distinct values  exact    46   endpoint   210   centre-radius    46
      2r   obj2   distinct values  exact    46   endpoint   207   centre-radius    46
    phi_cw
      c    obj1   distinct values  exact   850   endpoint  1361   centre-radius  1339
      r    obj1   distinct values  exact    46   endpoint   210   centre-radius    46
      c    obj2   distinct values  exact   850   endpoint  1319   centre-radius  1204
      r    obj2   distinct values  exact    46   endpoint   207   centre-radius    46

the endpoint route shatters 46 true values into 210. the centre-radius route
returns exactly 46. the centre column is shattered by both routes, 850 into 1361
and 1339, and that is ordinary rounding of a column whose values are genuinely
almost all distinct; it is not a broken tie and it is not what produces spurious
points.

phi_lu has no width column, and that is why phi_lu is untouched everywhere below.

### 1.4 how the error scales

the same measurement with a constant added to both centres. adding a constant to
a column cannot change dominance, so the exact answer is unchanged and everything
that moves is arithmetic.

    offset      endpoint route, width column      centre-radius route, width column
    0           max abs 7.216e-16                 max abs 2.220e-16
    1e3         max abs 1.091e-13   all 3721 wrong    max abs 2.220e-16
    1e6         max abs 1.118e-10   all 3721 wrong    max abs 2.220e-16
    1e9         max abs 1.144e-07   all 3721 wrong    max abs 2.220e-16

the endpoint route's width error is exactly proportional to the magnitude of the
centre: three decades of offset give three decades of error, twice. it is
eps * |c| and nothing else, which is what a1 predicted and never measured. the
centre-radius route's width error does not move at all, because it never forms
the difference.

inside the box at offset 0 the centre spans less than one decade, so the law is
only faintly visible there: bucketed by centre, the max absolute error on the
phi_cw width column runs 2.220e-16 on [0, 2) and 3.608e-16 on [3, 4.5). the
offset sweep is the measurement of the scaling, not the bucket table.

### 1.5 spurious and lost points against tolerance

absolute tolerance tau on the dominance relation: j dominates i when
img_j <= img_i + tau in every column and img_j < img_i - tau in some column.
spurious is what survives that the exact answer excludes, lost is what the exact
answer contains and the tolerance kills. 61 x 61 grid, delta = 1/10, endpoint
route.

  phi_lu   |exact| = 460          phi_ls   |exact| = 1505      phi_cw   |exact| = 961
      tau      |nd|  sp  lost         |nd|  sp  lost               |nd|  sp  lost
      0         460   0     0         1512   7     0                974  13     0
      1e-18     460   0     0         1512   7     0                974  13     0
      1e-17     460   0     0         1512   7     0                973  12     0
      1e-16     460   0     0         1510   5     0                968   7     0
      1e-15     460   0     0         1505   0     0                961   0     0
      1e-14 ..  460   0     0         1505   0     0                961   0     0
      1e-04     460   0     0         1505   0     0                961   0     0
      1e-03     447   0    13         1424   0    81                899   0    62
      1e-02     185   0   275          763   0   742                176   0   785
      1e-01       0   0   460            0   0  1505                  2   0   959

**there is a plateau, and it is eleven decades wide**: every tau from 1e-15 to
1e-4 gives exactly the exact set for all three phi, no spurious point and none
lost. genuine points start being lost at 1e-3, which is the scale of the real
gaps on this grid, multiples of 1/3600. so a tolerance is safe here, and the
answer to the question the session asked first is yes.

### 1.6 the clean band as the magnitude grows

the same sweep at four centre offsets, for three ways of setting the tolerance:
one absolute number, a number scaled by each column's own maximum absolute value,
and a number scaled by each column's own span. a band is clean when no spurious
point survives and no genuine one is lost.

    offset   phi     absolute            relative to max     relative to span
    0        lu      1e-18..1e-04 (15)   1e-18..1e-05 (14)   1e-18..1e-05 (14)
    0        ls      1e-15..1e-04 (12)   1e-15..1e-05 (11)   1e-15..1e-05 (11)
    0        cw      1e-15..1e-04 (12)   1e-15..1e-04 (12)   1e-15..1e-04 (12)
    1e3      ls      1e-12..1e-04  (9)   1e-13..1e-07  (7)   1e-12..1e-05  (8)
    1e3      cw      1e-13..1e-04 (10)   1e-13..1e-06  (8)   1e-12..1e-04  (9)
    1e6      ls      1e-09..1e-04  (6)   1e-10..1e-10  (1)   1e-09..1e-05  (5)
    1e6      cw      1e-10..1e-04  (7)   1e-10..1e-09  (2)   1e-09..1e-04  (6)
    1e9      ls      1e-06..1e-04  (3)   none exists         1e-06..1e-05  (2)
    1e9      cw      1e-07..1e-04  (4)   1e-16..1e-12  (5)   1e-07..1e-04  (4)
    1e12     ls      none exists         none exists         none exists
    1e12     cw      1e-04..1e-04  (1)   none exists         none exists

    phi_lu keeps 1e-18..1e-04 at every offset, having no width column.

three things to read off it.

the absolute band loses one decade of floor per decade of magnitude and its
ceiling does not move, because the floor is the noise eps|c| and the ceiling is
the problem's real gaps. by |c| = 1e12 there is no clean absolute tolerance for
phi_ls at all.

**scaling per column by that column's own size is worse than not scaling**, which
is the result this session did not expect. the noise in the width column is not
proportional to the width; it is proportional to the **centre** the width was
subtracted out of. a per-column relative tolerance therefore gives the width
column a tolerance of rtol times about 0.5 when what it needs is rtol times |c|,
and it runs out three decades earlier than the absolute rule. the phi_cw row at
1e9, clean over 1e-16..1e-12 and not above, is the same effect seen from the
other side and is not a band anyone would choose deliberately.

span normalisation behaves almost exactly like the absolute rule here, because
p1's spans are of order one. it would diverge from it on a column with a large
offset and a small spread, and would then fail for the same reason as relative to
max: the noise tracks the offset and the tolerance tracks the spread.

the spurious count with no tolerance moves around with the offset without a
pattern, 7, 8, 2, 3 and 12 for phi_ls. that is v-41's sample dependence again.

### 1.7 the counts on the committed grid

the spurious counts at tau = 0 are 7 and 13 on this grid. on the grid the
committed test actually uses, numpy's linspace rather than k/30, they are 9 and
17 at delta = 1/10 and 4 and 10 at delta = 1/8. the two grids are the same
rationals and differ only in which doubles numpy produces for them. that the
count changes with that is v-41's point again: the artefact is sample-dependent,
which is exactly what makes it dangerous.


## part 2, the free fix: delta = 1/8

delta = 1/10 was the only constant in p1 that is not a dyadic rational. the claim
put to this session was that it is also dominance-irrelevant and gradient-free,
so it can be replaced by 1/8 at no cost. both halves were checked rather than
assumed, and both hold.

### claim 1, delta enters every image coordinate as an additive constant

subtracting the delta = 1/10 coordinate arrays from the delta = 1/8 ones over the
whole box, in exact integer arithmetic, numerators over 576000:

    phi_lu   f_l obj1  -14400   f_u obj1  +14400   f_l obj2  -14400   f_u obj2  +14400
    phi_ls   f_l obj1  -14400   2r  obj1  +28800   f_l obj2  -14400   2r  obj2  +28800
    phi_cw   c   obj1       +0   r  obj1  +14400   c   obj2       +0   r  obj2  +14400

every column's difference has min equal to max, so it is exactly constant, and
the constants are -1/40, +1/40, +1/20 and 0 as predicted, one per coordinate.

### claim 2, no gradient, hessian, stationary point or interiority claim moves

a function whose difference from another is exactly constant has the same
gradient and the same hessian everywhere, so claim 1 proves claim 2 outright.
checked numerically as well, by central differences at 500 random interior points
with step 2^-20, which is exact for a quadratic up to rounding:

    worst |grad(1/8) - grad(1/10)| over all twelve coordinates and both axes:
    5.821e-10, against gradients of magnitude up to 3.0

5.8e-10 is the rounding floor of the difference quotient itself, eps|f|/2h with
h = 2^-20, and not a residual disagreement. a1-b's convexity table, its
stationary points and its interiority verdict all carry over unchanged.

### claim 3, the efficient sets are identical

exact integer non-dominated sets on a1-b's 61 x 61 grid:

    phi_lu   |delta=1/10| =  460   |delta=1/8| =  460   identical: True
    phi_ls   |delta=1/10| = 1505   |delta=1/8| = 1505   identical: True
    phi_cw   |delta=1/10| =  961   |delta=1/8| =  961   identical: True

identical as index sets, not merely equal in size. the half-width range moves
from [0.1000, 0.6625] to [0.1250, 0.6875], the same span shifted by 1/40, and
stays strictly positive.

### what the change buys, measured

on a dyadic grid, 65 x 65 with step 1/32 on the same box, where every decision
coordinate is a power-of-two rational:

    delta = 1/10   f_u - f_l equals 2r bitwise:   911 / 4225 points
                   width column distinct values: exact 49, subtracted 150
                   max |f_u - f_l - 2r| = 7.216e-16
    delta = 1/8    f_u - f_l equals 2r bitwise:  4225 / 4225 points
                   width column distinct values: exact 49, subtracted  49
                   max |f_u - f_l - 2r| = 0.000e+00

at delta = 1/8 the endpoint route is **exact** on a dyadic sample. every tie is
preserved, the width column has precisely the values it should, and no tolerance
is needed there at all.

two honest qualifications, both of which cut against reading this as a solution.

first, the spurious count on that dyadic grid is zero for both deltas. at
delta = 1/10 the ties are shattered, 150 values where there are 49, and it
happened not to produce a spurious non-dominated point on that particular grid.
so the spurious count is the wrong instrument: the corruption was present and
invisible. the bitwise and distinct-value tests are the right ones.

second, on a1-b's non-dyadic 61 x 61 grid the change helps only a little, because
there the grid step 1/30 is itself non-dyadic and delta is no longer the binding
constraint:

    delta = 1/10   phi_ls  1512 against exact 1505,  7 spurious   phi_cw  974 against 961, 13 spurious
    delta = 1/8    phi_ls  1509 against exact 1505,  4 spurious   phi_cw  971 against 961, 10 spurious

**verdict: make the change, and do not mistake it for the fix.** it is free, it
is verified, and it makes p1 exactly evaluable whenever the sample is dyadic,
which is a property b2 can choose to give its reference grid. random search and
pymoo produce arbitrary doubles, so it does nothing for them, and the project
still needs one dominance rule. src/problems_tier0.py now carries
delta = 1/8 with this reasoning at the constant, and the two tests that pinned
the old value were updated with it.


## part 3, one rule for the whole project

### what pymoo does, checked

    NonDominatedSorting()                front = [0, 1]
    NonDominatedSorting(epsilon=1e-15)   front = [0, 1]
    NonDominatedSorting(epsilon=1e-06)   front = [0, 1]
    NonDominatedSorting(epsilon=1     )  front = [0, 1]

    on 400 random rows in 4 columns: |front| = 58 without epsilon and 58 with
    epsilon = 1e-3, identical sets: True

pymoo 0.6.2 has an `epsilon` argument on `NonDominatedSorting` that looks like a
tolerance and is not one: it computes `F - epsilon` and ranks that, and
subtracting the same number from every entry of every row is a translation, to
which dominance is invariant. it cannot change a front. nsga-ii's default
survival constructs `NonDominatedSorting()` with `epsilon=None` in any case, and
ranks through `moocore.pareto_rank` on raw doubles.

two consequences. pymoo's internal selection cannot be given a tolerance without
supplying a custom dominator, which is beyond this project. and any rule of the
first three kinds below is therefore applied to pymoo's **output** only, while
the generations that produced that output were selected under exact comparison of
corrupted columns.

### the options

**(1) absolute rounding or an absolute tolerance, what the a4 test does now.**
curve: clean over twelve decades at p1's magnitudes, 1e-15 to 1e-4, and the best
of the three at every offset measured. scale stability: none, and measured: the
band narrows by one decade per decade of magnitude and is gone by |c| = 1e12. post hoc on pymoo: yes. memoria: "objective
values were compared after rounding to nine decimals" is defensible and arbitrary,
and invites the question of what happens at other magnitudes.

**(2) a relative tolerance scaled per column.** curve: measured in 1.6, and it
is the worst of the three, 1 clean decade at |c| = 1e6 against the absolute
rule's 6, and none at 1e9. scale stability: none, and for an instructive reason.
the intuition that a relative tolerance tracks the noise is wrong here, because
the noise in the width column is proportional to the centre it came out of and
not to the width. scaling a column by its own size is scaling by the wrong
quantity. post hoc on pymoo: yes. memoria: "values were compared to a relative
precision of 1e-12" is the standard sentence, and on this problem it is the
standard sentence attached to the worst of the three rules.

**(3) per-column normalisation before comparison, by the column's span.** curve:
measured in 1.6, indistinguishable from the absolute rule on p1 and one to two
decades narrower. scale stability: it tracks the span, so it fails wherever the
offset and the spread diverge, which is exactly a portfolio return series in part
2. post hoc on pymoo: yes. memoria: defensible, and it changes what dominance
means when a column is nearly constant, which is a substantive change and not a
numerical one.

**(4) compute the phi image from the centre and the half-width.** curve: no
tolerance needed at all, measured below. scale stability: complete, and measured
to 1e12. post hoc on pymoo: it is better than post hoc, because it fixes the
columns before pymoo ever sees them, so pymoo's internal exact comparisons are
then comparisons of clean numbers and the project's rule and pymoo's rule agree
by construction rather than by patching afterwards. memoria: "the transformed
objectives were evaluated in the centre and half-width parameterization, in which
they are exact, rather than by subtracting endpoints" is one sentence and it is a
statement about arithmetic, not about the order.

it is an interface change and this is what it costs. CONTEXT.md section 4 and
subpart a3 specify `make_phi(lam, beta)` as returning a function of `(f_l, f_u)`,
and subparts a4 and a5 specify `evaluate` as returning interval bounds. option 4
needs the image path to reach c and r, so either `make_phi`'s argument changes or
the problems grow a second accessor. it is not a change to the family: for any
admissible phi,

    lam_1 f_l + lam_2 f_u  = (lam_1 + lam_2) c + (lam_2 - lam_1) r
    beta_1 f_l + beta_2 f_u = (beta_1 + beta_2) c + (beta_2 - beta_1) r

so the coefficient constructor survives intact and only its arguments move. and
it pre-empts s-06, which asks the supervisors this exact question and has not
been asked. that is the real cost: the project would be answering for itself a
question it has already decided belongs to the supervisors.

### option 4 measured, with no tolerance at all

centre-radius route, plain exact comparison, no tolerance, against the exact
integer set, 61 x 61 grid, delta = 1/10:

    offset     phi   |nd|   spurious   lost   width column distinct (exact 46)
    0          ls     1505          0      0      46
    0          cw      961          0      0      46
    1e3        ls     1505          0      0      46
    1e3        cw      961          0      0      46
    1e6        ls     1505          0      0      46
    1e6        cw      961          0      0      46
    1e9        ls     1505          0      0      46
    1e9        cw      961          0      0      46
    1e12       ls     1505          0      0      46
    1e12       cw      961          0      0      46

    phi_lu is 460 with 0 spurious and 0 lost at every offset by both routes,
    having no width column to corrupt.

twelve decades of magnitude, no tolerance parameter, and the exact answer every
time.

### the recommendation

**option 4: compute every phi image from the centre and the half-width, and then
compare with one untoleranced dominance relation everywhere.** recorded as d-02
in PROGRESS.md, proposed, not taken and not implemented this session.

the reason, in the order the measurements give it.

the other three rules all work today and all stop working at a magnitude this
project may well reach: none of them has a clean band at |c| = 1e12, and part 2
of the project puts a portfolio's objective values at whatever scale the data
comes at. option 4 has no band to run out of. it needs no parameter, so there is
no number to justify in the memoria and no number that could be tuned to change a
result.

it is the only one that reaches inside pymoo. pymoo's non-dominated sorting takes
no tolerance and its epsilon argument is a no-op, so options 1 to 3 can only
re-filter what nsga-ii returns, while the generations that produced it were
selected by exact comparison of corrupted columns. option 4 hands pymoo clean
columns, and then pymoo's exact comparison and the project's exact comparison are
the same relation by construction. the reproducibility requirement that opened
this session is met rather than patched.

it is measured, not argued: zero spurious and zero lost at every offset from 1 to
1e12, on both phi that have a width column, with no tolerance at all.

one condition on it, stated plainly because it bounds the recommendation. option
4 is exact only where the problem is *defined* in centre and half-width form, so
that c and r are computed rather than recovered. that holds for p1 by
construction, for p0, whose two objectives are [-|x|, |x|] and [0, x^2] with
c = 0, r = |x| and c = r = x^2/2, and for a1's tier 1 construction
F = [f - r, f + r]. a problem given as two unrelated endpoint functions would
force c = (f_l + f_u)/2 and r = (f_u - f_l)/2 and put the subtraction straight
back. so the rule to record is not "use centre and half-width" but "a problem
declares its centre and half-width, and the phi image is computed from those".

and one cost, which is the reason this is proposed and not done. it is an
interface change against CONTEXT.md section 4 and subpart a3, which specify
make_phi as a function of (f_l, f_u), and against subparts a4 and a5, which
specify evaluate as returning interval bounds. more seriously it pre-empts s-06,
which puts this exact question to the supervisors and has not been asked. the
project should not answer its own supervisor question by implementing the answer.
so: ask s-06, or have the research chat take d-02 knowingly.

if d-02 is rejected, the fallback is option 1, an absolute tolerance, fixed once
in one place and applied identically in c1, d2 and post hoc to c2's output, with
the magnitude of every objective column reported in every results table so that a
reader can check the band is still open. that is a worse answer and it is a
workable one.


## what this session did not settle

s-06 is unchanged and unasked, and d-02 cannot be taken over it.

the measurements are all on p1. p0's arithmetic was not swept, because p0's
widths are |x| and x^2/2 and carry no delta to make dyadic; nothing suggests it
behaves differently, and nothing here checks it. tier 1 was not touched at all,
and a5 will meet the same question on zdt1 and dtlz2, where the objective
magnitudes differ between f_1 and f_2 by an order of magnitude, which is the
condition under which option 3 and option 1 diverge.

no rule is implemented anywhere. the a4 test still rounds to nine decimals
locally, which is inside every clean band measured at p1's magnitudes and is
correct for that test today. it is not the project's rule and the test now says
so.
