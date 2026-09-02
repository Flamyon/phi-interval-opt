# b2-b: the reference front's density, and what it does to igd

subpart b2-b. one file changed under `src/`, `src/reference_fronts.py`, and one
argument added to its two entry points. this document records the risk that made
the change necessary, r-13, the measurements that fix the one constant it
introduces, the density it corrects measured directly, and the test that decides
whether the correction is decision-relevant or cosmetic. it is decision-relevant
and the numbers are in section 6.

**why this is a separate file and not an appendix to
docs/b1_phi_efficient_sets.md.** b1 derives the phi-efficient sets of p1 from the
optimality conditions of [1], and every section of it is a statement about the
paper's hypotheses and their consequences, checked in exact arithmetic. nothing
here is such a statement. b2-b changes no line of the derivation: not the system
of b1 section 2.1, not the map x(w) of b1 section 2.2, not the regions of b1
section 2.4, not the undecided segment of b1 section 2.6. what it changes is
which of the points sampled through that map are kept, which is a property of the
sampling code and of the metric it feeds, and putting a study of igd's sensitivity
to sampling density inside the derivation document would blur exactly the line b2
was built to keep: the module encodes b1's derivation, and b1 says nothing about
igd. b1 is cited here, section by section, and not restated.

[1] is papers/new_preference_order_relationships_paper.txt, costa, osuna-gomez
and chalco-cano, fuzzy sets and systems 477 (2024) 108812.


## 1. the risk, stated

r-13, raised at b2 and carried since:

> b2's reference front is sampled through b1's weight map, so its density in
> objective space is the parametrisation's and not the front's, and igd is an
> average over reference points.

the mechanism, in one line. b2 draws weights from a dirichlet on the simplex at
concentration 0.3 and pushes them through the rational map w -> x(w) of b1 section
2.2, then through phi. the map is rational and is nowhere an isometry, so a
sample that is evenly spread on the simplex is not evenly spread on the front
either: it piles up wherever the map contracts and thins out wherever it
stretches, and the dirichlet draw at concentration 0.3, chosen at b2 to reach the
extremes of b1 section 2.4, is not evenly spread on the simplex to begin with.
igd is

    igd(F, R) = (1/|R|) sum over r in R of min over f in F of ||r - f||

an average over the **reference** points, so a region of the front carrying twice
the reference points contributes twice the terms and counts twice. the number then
depends on where the parametrisation happens to put its mass, and a solver that
covers the piled-up region well scores better than one that covers the thin region
equally well. that is a property of the weight simplex and not of the solvers.

what this does not touch, and why the risk was not urgent before now. the c3 gate
measures recovery by a directed hausdorff distance in the decision space,
CONTEXT.md section 10 c3, which is a maximum over the reference and not an
average: it is insensitive to how densely the reference samples a region it
already reaches. d2's metrics are a maximum and two coverage counts in the
decision space, and none of them averages over a reference. the dominance checks
in tests/test_runners.py, tests/test_random_search.py and
tests/test_reference_fronts.py ask whether any point dominates any point, which is
a relation between points that no density enters. igd is the one instrument in the
project the bias reaches, and igd is d1's.


## 2. what changed

`efficient_set` and `reference_front` take a fifth argument, `sampling_mode`, in
the position after `include_singular_segments` and with no default:

    dirichlet         the draw as b2 built it, unchanged
    farthest_point    the same draw at oversampling_factor times the size,
                      subsampled to n_points by greedy farthest-point selection
                      in objective space

the selection keeps, repeatedly, the point farthest from the points already kept,
starting from the point farthest from the image's centroid. that start is a
function of the draw alone, so the selection carries no second seed and the front
is bitwise reproducible at a stated seed and mode, which is what
tests/test_reference_fronts.py asserts.

four properties of the change, each of which is a test:

**it changes which points are kept and nothing else.** every kept point is still
x(w) at a weight the draw produced and the module recorded, and the kept front is
a subsequence of the oversample:
`test_the_selection_is_a_subsequence_of_the_oversample` rebuilds the oversample
from the module's own draw and map at the same seed and walks the kept rows
through it in order, checking that the weight travels with the point. b1 section 2.4's inequalities are still nowhere in `src/`, only in the
tests, which is b2's own principle and the reason the module samples the map
rather than the region.

**the selection is in objective space.** igd is computed on the front and it is
the front's density that biases it, so a selection made in the decision space
would correct the wrong distribution. the two are not the same: phi and p1's image
coordinates are quadratic, b1 section 1.1, so decision-space spacing and
objective-space spacing differ by the local jacobian.

**the caller's delta does not move the selection.** the image is built at the
derivation's own parameters. rho is fixed at 1/4 for every reference front, and
delta enters every image coordinate as an additive constant, b1 section 1.2, so a
different delta translates the whole image and leaves every distance in it
unchanged. `test_rho_is_fixed_and_delta_is_free` runs under both modes and checks
the shifted front differs from the base front by a constant, which it could not if
the selection had been made in the caller's delta.

**the singular segment is not touched by the mode.** it is a linspace on a
one-dimensional set, b1 section 2.6, already as evenly spaced as it can be, and
its share of n_points is unchanged. the correction is to the two-dimensional part,
whose density is the parametrisation's.

`oversampling_factor` is a module constant and not an argument. it is not a
reporting parameter: unlike the mode and the flag it does not name a different
object, it converges to the same evenly spaced front from below, so a table
carrying it would invite comparing two fronts that differ only in how well one
selection was resolved. section 3 fixes its value.

everywhere else in the suite that builds a reference front — the c3 gate, the two
dominance checks, d2's tests — states `dirichlet_mode` explicitly, with the reason
at the call site. those measurements are maxima, counts or relations, none of them
biased by the reference's density, and every number
docs/c3_validation.md tables was measured against that reference; changing it
there would silently restate published numbers for no gain.


## 3. the oversampling factor, fixed by measurement

the factor is the one number the correction introduces, so it is measured and not
chosen. for each phi, a 1000-point front was built at factor 1, 2, 5, 10, 20 and
40 — factor 1 being the dirichlet draw itself, no selection made — and two
statistics were computed on it: the coefficient of variation of the
nearest-neighbour distance within the front, which is the evenness the correction
is for, and the fill distance of the front with respect to a 40000-point covering
draw of the same front, which is the largest hole it leaves. seconds are the
selection's own, on one core.

    phi   factor   nn mean    nn sd      nn cv    fill       seconds
    lu     1       0.011443   0.008463   0.7395   0.064125   0.00
    lu     2       0.017294   0.004302   0.2488   0.053098   0.10
    lu     5       0.020466   0.003133   0.1531   0.031361   0.25
    lu    10       0.021725   0.002651   0.1220   0.025386   0.56
    lu    20       0.022412   0.002623   0.1170   0.023793   1.27
    lu    40       0.022794   0.002481   0.1088   0.023018   2.51
    ls     1       0.026974   0.030405   1.1272   0.302511   0.00
    ls     2       0.038813   0.018854   0.4858   0.187565   0.10
    ls     5       0.049493   0.011618   0.2347   0.127225   0.33
    ls    10       0.055394   0.008929   0.1612   0.091648   0.50
    ls    20       0.058294   0.007606   0.1305   0.089641   1.03
    ls    40       0.060567   0.006474   0.1069   0.066519   2.06
    cw     1       0.014852   0.021096   1.4205   0.228843   0.00
    cw     2       0.021620   0.016281   0.7531   0.152777   0.13
    cw     5       0.029995   0.010183   0.3395   0.121045   0.30
    cw    10       0.034882   0.007001   0.2007   0.067848   0.59
    cw    20       0.038339   0.005390   0.1406   0.060417   1.12
    cw    40       0.040318   0.004684   0.1162   0.043152   2.21

**factor 10 is what the module uses.** the reduction in the coefficient of
variation between factor 1 and factor 40 is 0.63, 1.02 and 1.30 for phi_lu,
phi_ls and phi_cw, and factor 10 takes 98, 95 and 94 per cent of it at a quarter
of factor 40's cost. the cost is linear in the factor and the selection is
quadratic in the kept count, so the choice is not free at the sizes d1 will use:
the whole call, draw and selection, takes 0.14 s at 500 kept points, 0.61 s at
1000, 2.18 s at 2000, 16.95 s at 5000 and 189 s at 20000. a reference front is
built once per phi, flag and size, so this is a per-table cost and not a per-run
one, but it is why the b2 test that runs at 20000 points stays in the dirichlet
mode and its farthest-point companion runs at 2000.

the fill distance falls with the factor as well and is still falling at 40, most
visibly under phi_ls and phi_cw. that is the same statement from the other side
and it is not an argument for a larger factor: the fill distance of a
1000-point front is bounded below by the front's own geometry, and what the
correction is for is the density that biases igd, which the coefficient of
variation measures and which has flattened by ten.


## 4. the density itself, measured directly

the distribution of the nearest-neighbour distance within the reference front, at
1000 points, under both modes, per phi and under both settings of
`include_singular_segments`. a front whose points are evenly spread has a tight
distribution; one whose spacing is the parametrisation's does not.

    phi   flag    mode             mean       sd         cv       min        median     max
    lu    False   dirichlet        0.011443   0.008463   0.7395   0.000629   0.009340   0.052433
    lu    False   farthest_point   0.021725   0.002651   0.1220   0.018132   0.021225   0.037497
    lu    True    dirichlet        0.011443   0.008463   0.7395   0.000629   0.009340   0.052433
    lu    True    farthest_point   0.021725   0.002651   0.1220   0.018132   0.021225   0.037497
    ls    False   dirichlet        0.026974   0.030405   1.1272   0.000016   0.017934   0.277524
    ls    False   farthest_point   0.055394   0.008929   0.1612   0.044970   0.052981   0.119979
    ls    True    dirichlet        0.027391   0.028912   1.0555   0.000016   0.018454   0.217570
    ls    True    farthest_point   0.054534   0.011110   0.2037   0.000000   0.053343   0.100112
    cw    False   dirichlet        0.014852   0.021096   1.4205   0.000006   0.006743   0.177775
    cw    False   farthest_point   0.034882   0.007001   0.2007   0.027431   0.032924   0.074210
    cw    True    dirichlet        0.015672   0.020609   1.3150   0.000006   0.007218   0.169581
    cw    True    farthest_point   0.034869   0.007900   0.2266   0.000001   0.033320   0.072568

what the table says, and it is the direct evidence for r-13.

**the dirichlet front is not evenly spaced, and under two of the three phi it is
extremely uneven.** its coefficient of variation is 0.74 under phi_lu, 1.13 under
phi_ls and 1.42 under phi_cw. a spacing whose standard deviation exceeds its mean
is not a spread-out sample with some jitter; it is a sample with clusters. the
extremes say the same thing: under phi_cw the closest pair of the 1000 points sits
6e-06 apart while the loneliest point is 0.178 from its nearest neighbour, a ratio
of 3e+04, against a ratio of 2.7 under the selection.

**the selection spreads the same count over more of the front.** the mean nearest-
neighbour distance roughly doubles under every phi, 0.0114 to 0.0217, 0.0270 to
0.0554 and 0.0149 to 0.0349. the same 1000 points cover the front at twice the
spacing because they are no longer spending themselves on the region the map
contracts into.

**phi_lu is the least biased of the three and phi_cw the most.** that ordering is
the one b1 section 2.4 would predict: X_lu is the region whose two coordinates are
coupled through u = w_3 + w_4, while X_cw is the unit square reached by two
independently parameterised ratios 2s/(2 + w_4/2) and 2/(2 + w_2/2), each of which
compresses its whole tail of large w into a neighbourhood of zero. the front that
is a product of intervals is the one whose parametrisation is worst behaved.

**the flag changes the picture only slightly, and only for the two phi that have a
singular segment at all.** under phi_lu the two rows are identical to the bit,
b1 section 2.3 finding no singular ray there, so the flag is a no-op and the mode
does not interact with it. under phi_ls and phi_cw the segment adds
ceil(sqrt(1000)) = 32 points on a line, which lowers the dirichlet coefficient of
variation slightly, 1.1272 to 1.0555 and 1.4205 to 1.3150, and raises the
selection's, 0.1612 to 0.2037 and 0.2007 to 0.2266. the raising is the segment's
own doing and not the selection's: the segment is placed by linspace and not
selected, so where it runs close to the selected part of the front it produces the
smallest gaps in the set, which is the 0.000000 and 0.000001 in the min column.
the two settings remain two objects under both modes, r-12 and s-12, and nothing
here decides between them.


## 5. what the correction moves, on one fixed test front

the test front is a random-search run on p1 at budget 5000 and seed 41, filtered
to its non-dominated rows by src/random_search.py: 590 rows under phi_lu, 2181
under phi_ls and 1500 under phi_cw. it is held fixed while the reference under it
is swapped, so every difference below is the reference's and the front's.

    phi   flag    n_ref    rows    igd dirichlet   igd farthest   difference   per cent
    lu    False     500     590    0.01874660      0.01990847     +0.00116187    +6.20
    lu    False    1000     590    0.01885752      0.02013746     +0.00127994    +6.79
    lu    False    5000     590    0.01892073      0.02006477     +0.00114404    +6.05
    lu    False   20000     590    0.01913052      0.02010010     +0.00096958    +5.07
    lu    True      500     590    0.01874660      0.01990847     +0.00116187    +6.20
    lu    True     1000     590    0.01885752      0.02013746     +0.00127994    +6.79
    lu    True     5000     590    0.01892073      0.02006477     +0.00114404    +6.05
    lu    True    20000     590    0.01913052      0.02010010     +0.00096958    +5.07
    ls    False     500    2181    0.02226098      0.02422591     +0.00196494    +8.83
    ls    False    1000    2181    0.02240435      0.02567328     +0.00326893   +14.59
    ls    False    5000    2181    0.02246980      0.02528200     +0.00281220   +12.52
    ls    False   20000    2181    0.02245314      0.02531145     +0.00285831   +12.73
    ls    True      500    2181    0.02267806      0.02474662     +0.00206856    +9.12
    ls    True     1000    2181    0.02268822      0.02594477     +0.00325656   +14.35
    ls    True     5000    2181    0.02260828      0.02529047     +0.00268219   +11.86
    ls    True    20000    2181    0.02252393      0.02535633     +0.00283240   +12.58
    cw    False     500    1500    0.01668002      0.02175194     +0.00507193   +30.41
    cw    False    1000    1500    0.01678733      0.02160068     +0.00481335   +28.67
    cw    False    5000    1500    0.01699718      0.02150599     +0.00450881   +26.53
    cw    False   20000    1500    0.01697768      0.02142607     +0.00444839   +26.20
    cw    True      500    1500    0.01739653      0.02228278     +0.00488625   +28.09
    cw    True     1000    1500    0.01726308      0.02184042     +0.00457735   +26.52
    cw    True     5000    1500    0.01717696      0.02163073     +0.00445377   +25.93
    cw    True    20000    1500    0.01707081      0.02150075     +0.00442994   +25.95

**the correction raises igd, by 5.07 to 30.41 per cent, and the size of the rise
follows the size of the bias.** phi_lu, the least unevenly sampled of the three by
section 4, moves by 5 to 7 per cent; phi_ls by 9 to 15; phi_cw, the worst, by 26 to
30. the direction is the one the mechanism predicts. the dirichlet reference
concentrates its points where the map contracts, and that is where any front of a
few hundred points is already well covered, so it averages over easy terms; moving
those points out to the thin regions replaces easy terms with hard ones and the
average rises.

**the difference does not shrink with the reference size, which is what separates
it from r-12.** at 20000 reference points the two references still differ by 5.07,
12.73 and 26.20 per cent. that is the signature of a bias rather than of noise:
both references converge, but to different numbers, because they are averaging the
same distance function against different densities. the singular-flag difference
on this same front behaves the other way, as r-12 said it would — under the
dirichlet reference the flag moves igd by 1.87, 1.27, 0.62 and 0.32 per cent under
phi_ls at 500, 1000, 5000 and 20000 points and by 4.30, 2.83, 1.06 and 0.55 under
phi_cw, falling with density throughout, and it moves it by 2.15 to 0.18 and 2.44
to 0.35 per cent under the corrected reference. **r-13's effect on this front is
between five and fifty times r-12's, and unlike r-12's it does not go away by
sampling harder.**

**under phi_lu the flag changes nothing at all**, the eight rows being equal to
the last digit at both settings, which is b1 section 2.3's finding that phi_lu has
no singular ray, restated by the measurement.

what the table does not say is which front is better. it is one front measured
against two references, so the difference is a level and not a ranking, and a
level does not by itself justify changing anything. section 6 is the part that
does.


## 6. the test that decides it: whether the two references can rank two fronts
differently

section 5 shows the correction moves the number. that on its own would not
justify anything: a metric that moves by a constant factor ranks the same fronts
in the same order and the choice would be cosmetic. what matters is whether two
fronts of the same quality, differing only in **where** they put their points, can
be ranked one way by the dirichlet reference and the other way by the corrected
one. they can.

### 6.1 the construction

for each phi and each setting of the flag:

    the split. the front is cut in two by the median of its first image column,
        taken over the 2000-point farthest-point reference. the two halves
        therefore carry 1000 corrected-reference points each, which is equal
        measure under a reference whose density is the front's. the dirichlet
        reference of the same size splits 1228 against 772 under phi_lu, 1407
        against 593 under phi_ls and 1405 against 595 under phi_cw, and 1228,
        1383 and 1397 with the flag on. the half it overfills is the dense half,
        and it is the upper half under phi_lu and the lower half under the other
        two.

    the fronts. a candidate front of k = 200 points is built from a 40000-point
        draw of the exact efficient set, by taking m of its points in the dense
        half and k - m in the sparse half, each chosen by the same farthest-point
        selection so that within a half the points are as evenly spread as the
        correction itself would make them. every candidate is therefore a subset
        of the exact front — none of them is wrong anywhere — and they differ only
        in the allocation m.

    the quality measure, which must not be igd. the fill distance of the
        candidate with respect to an independent 40000-point covering draw of the
        front, that is the largest distance from a point of the front to the
        nearest candidate point. it is a maximum, so unlike igd it does not weight
        a region by how densely the covering draw samples it, and it is the same
        measure c3 uses for the same reason, CONTEXT.md section 10 c3.

    the two references. the dirichlet and the farthest-point reference front at
        2000 points, at the flag setting under test.

### 6.2 the allocation each reference prefers

the first result is visible without pairing anything. for each phi and flag, the
allocation minimising igd against each reference, and the allocation minimising
the fill distance, over m in 20, 25, ..., 180:

    phi   flag    dirichlet   farthest_point   fill
    lu    False   130         105              105
    lu    True    130         105              105
    ls    False   125         100              85
    ls    True    115          90              80
    cw    False   115          90              65
    cw    True    110         105              80

**under every phi and both flags the dirichlet reference asks for more points in
the half it oversamples than the corrected reference does**, by 25 of 200 in five
of the six rows, 12.5 per cent of the whole front. the corrected reference sits
between the dirichlet one and the density-free fill measure in every row, and
coincides with the fill optimum under phi_lu. the exception is phi_cw with the
flag on, where the gap is 5 and the corrected curve is flat to within 0.0002 over
m in 90 to 110, so the argument there is the direction and not the size.

that is the bias in its plainest form: a solver tuned to the dirichlet reference's
idea of a good front would be tuned to put an eighth of its points in the wrong
place.

### 6.3 the mirror pairs, and the ranking flip

pair each allocation m in the dense half with its mirror k - m, so the two fronts
place the same two counts on the two halves the other way round. under phi_ls and
phi_cw:

    ls, flag False   m/k-m     fill dense    fill sparse   dirichlet   farthest
                     110/ 90   0.158294      0.137600      dense       sparse
                     120/ 80   0.165925      0.142780      dense       sparse
                     130/ 70   0.175112      0.152443      dense       sparse
                     140/ 60   0.185785      0.166653      dense       sparse
                     150/ 50   0.206909      0.180671      dense       sparse
                     160/ 40   0.245007      0.202723      dense       sparse
                     170/ 30   0.278960      0.243518      dense       sparse
                     180/ 20   0.333866      0.291219      dense       sparse

    cw, flag False   110/ 90   0.106337      0.098772      dense       sparse
                     120/ 80   0.122120      0.098772      dense       sparse
                     130/ 70   0.129635      0.097692      dense       sparse
                     140/ 60   0.131636      0.100814      dense       sparse
                     150/ 50   0.141385      0.108922      dense       sparse
                     160/ 40   0.168706      0.130253      dense       sparse
                     170/ 30   0.204216      0.163489      dense       sparse
                     180/ 20   0.248409      0.178750      dense       sparse

**every one of these pairs is ranked in opposite orders by the two references**,
and the density-free fill distance agrees with the corrected one and not with the
dirichlet one: the sparse-favouring front leaves the smaller hole and the
corrected reference says it is better, while the dirichlet reference says the
dense-favouring front is. the same holds at the other flag setting: 8 of 8 mirror
pairs flip under phi_ls with the flag on, and 7 of 8 under phi_cw, the exception
being 110/90 where the corrected reference has the two within 0.00007 of each
other. 31 of the 32 mirror pairs measured under phi_ls and phi_cw flip.

phi_lu is the phi where mirror pairs do not flip: there the upper half is the
oversampled one and is also the half a front genuinely needs more points in, so
the fill distance, the corrected igd and the dirichlet igd all prefer the
dense-favouring front, 16 pairs of 16. the flip under phi_lu appears instead among
the pairs of **equal** fill distance, which is the sharper form of the same test.

### 6.4 the equal-fill pairs

pairing every dense-favouring allocation, m at least 120, with every
sparse-favouring one, m at most 80, and keeping the pairs whose fill distances
agree to within one per cent — two fronts of equal quality by a measure that no
density enters — gives 23 such pairs in all: 4 under phi_lu at each flag setting,
4 and 2 under phi_ls, and 5 and 4 under phi_cw. one of the 23 is ranked in
opposite orders by the two references, and it is phi_lu's, the same pair at both
flag settings:

    m_a 160, m_b 50, fill 0.080595 against 0.080788, the two within 0.24 per cent
    igd against the dirichlet reference   0.024664 against 0.030017, prefers a
    igd against the corrected reference   0.028762 against 0.027886, prefers b

the front with 160 of its 200 points in the oversampled half and the front with 50
there are equally good on the density-free measure to within a quarter of a per
cent, and the two references disagree about which is better, by 22 per cent one
way and 3 per cent the other.

### 6.5 the answer to r-13's question

the ranking can flip, so the bias is decision-relevant and d1 must use the
corrected reference. the two forms of the evidence are worth keeping apart:

    the flip on a pair of exactly equal quality is rare in this sample, one pair
        of the 23 found, because it requires a coincidence of fill distances that
        a grid of allocations in steps of 5 rarely produces.
    the systematic effect behind it is not rare at all. it is in every row of
        section 6.2 and in 31 of 32 mirror pairs: the dirichlet reference prefers
        fronts weighted toward the half it oversamples, in a direction that is the
        same under every phi and both flags, and against a density-free measure of
        quality that agrees with the corrected reference instead.

a comparison of two solvers that place their points differently — which is exactly
what nsga-ii, mopso and random search do, docs/c3_validation.md section 5 — is a
comparison of the kind these pairs are.


## 7. the recommendation, and r-13's status

**d1 computes igd against the farthest-point reference and records the mode in
every table**, beside the seed, the point count and `include_singular_segments`.
CONTEXT.md section 10 d1 now says so. the dirichlet mode is kept and is not
deprecated: it is what every number already published in docs/c3_validation.md was
measured against, and the tests that use a maximum, a count or a dominance
relation state it explicitly and are unaffected.

**r-13 is not retired.** the question it was raised to ask has been answered —
the bias is real, it is large in the density itself, and it can reverse a
comparison — so the row keeps its risk and trigger and its mitigation becomes the
built correction rather than a plan. what has changed is that the mitigation is no
longer conditional on d1 being built: it exists now, and if d1 is cut nothing is
owed.

**the two reporting parameters do not interact and neither substitutes for the
other.** `include_singular_segments` decides which set the reference is, r-12 and
s-12, and the published conditions do not settle it. `sampling_mode` decides how
evenly that set is sampled, and the measurement above settles it. section 4 shows
the flag moving the density statistics slightly under phi_ls and phi_cw and not at
all under phi_lu, and section 6 shows the flip appearing at both settings; a table
that states one and not the other is missing half of what its igd depends on.

**what would change this recommendation.** a d1 that reported igd only as a ratio
between two solvers measured against the same reference would still be biased,
since section 6 is about exactly such a comparison. what would remove the need is
abandoning igd for a maximum-based measure, which is what c3 already does and what
CONTEXT.md section 10 c3 gives its reason for; that is a decision about d1's
instrument list and not one this document takes.


## 8. what this does not change

    the derivation. b1 sections 2.1 to 2.6 are untouched and nothing here is
        evidence for or against any of them.
    the map. `stationary_points` is b1 section 2.2 as it was, and the selection
        chooses among its outputs.
    the region inequalities. still only in tests/test_reference_fronts.py and
        tests/test_validation.py, never in `src/`.
    src/problems_tier0.py. not opened.
    the c3 gate and every number in docs/c3_validation.md. the gate states the
        dirichlet mode and measures a directed hausdorff distance, and its
        reference is bitwise the front it was before b2-b.
    d2's metrics. decision-space, a maximum and two counts, and its tests state
        the dirichlet mode for that reason.
    the dominance checks in tests/test_runners.py, tests/test_random_search.py and
        tests/test_reference_fronts.py. a dominance relation between two points
        has no density in it.
    s-12 and r-12. the singular segment question is where it was and this document
        does not touch it.
