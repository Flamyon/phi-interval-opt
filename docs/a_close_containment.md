# a-close: containments between the three phi

session a-close, 2026-08-31, generalised in session a-close-b, 2026-09-01. no
module was written or changed in either session and none of what follows is used
by any of them.

what this document is for. a5 recorded, as v-46 and r-11, that the phi_lu
non-dominated set is contained in the phi_ls one and that the containment is exact
in real arithmetic. a-close verified that argument and wrote it out. a-close-b then
had to explain why a5's own separation report appeared to contradict the same
statement for phi_cw on dtlz2, found that it does not, and generalised: both
containments are instances of one criterion on the map between two automorphisms,
and that criterion is stated once here rather than proved twice.

the standing constraint, stated first because it governs everything below, and
amended in session c2, 2026-09-01. the project claims no result from either
containment. they are recorded, not used. b1 derives its efficient sets from [1]'s
own results and does not shorten a derivation with them, and d2 and e3 report the
pairs as checks on r-06's prediction and never as independent findings. that
stands until the supervisors answer s-11.

what the constraint does not forbid, which is the amendment. a test may assert
either containment as a self-check on the encoding. c1 asserted both on random
search output and c2 asserts both on nsga-ii's and mopso's, and neither test
claims anything about the orders: the containment holds for the non-dominated
sets of any finite point set whatever produced it, so what such a test can fail on
is the sample, the route pairing, the column order or the dominance relation, and
that is the whole of what it is for. it is the cheapest end-to-end check the
project has. the earlier wording of this paragraph read "no test asserts either
containment for phi_cw", which was a statement about the state of the suite and
not a rule, and c1's phi_cw assertion stands. if s-11 refutes either containment
the tests asserting it are deleted along with the e3 instruction, and no result
moves, because none was claimed from them.

[1] is papers/new_preference_order_relationships_paper.txt, costa, osuna-gomez
and chalco-cano, "new preference order relationships and their application to
multiobjective interval and fuzzy interval optimization problems", fuzzy sets and
systems 477 (2024) 108812.


## 1. the criterion, and the two containments that follow

fix a feasible set S and a multi-interval-valued objective F with m interval
components, and write each component as its centre and half-width, c_i(x) and
r_i(x) >= 0, so that F_i(x) = [c_i - r_i, c_i + r_i]. let ND_phi(S) be the
non-dominated set of the transformed real problem under phi, under the ordinary
pareto relation on R^2m that CONTEXT.md section 5 step 5 fixes for the whole
project.

    criterion. let phi_A and phi_B be two admissible automorphisms of the class of
    [1] section 2, and let M be the 2 x 2 real matrix with phi_B = M phi_A acting
    on each interval objective. if every entry of M is non-negative and M is
    invertible, then phi_A-dominance implies phi_B-dominance, and therefore

        ND_B(S) is contained in ND_A(S)

    for every S and every F.

M is not a choice. each phi in the class is invertible, [1]'s admissibility
condition being exactly a non-zero determinant, v-02, so M = phi_B phi_A^-1 is
uniquely determined by the pair. whether the criterion applies to an ordered pair
of automorphisms is therefore a property of that pair and of nothing else.

the three phi this project implements, in centre and half-width coordinates,
CONTEXT.md section 4 and v-43, with example numbers verified in a0 as v-06 to
v-08:

    phi_lu   example 2.2   (c_i - r_i,  c_i + r_i)
    phi_ls   example 2.3   (c_i - r_i,  2 r_i)
    phi_cw   example 2.4   (c_i,        r_i)

the six maps between them, each computed as phi_B phi_A^-1 and each checked
against the images themselves:

    from       to        M                    det     non-negative
    phi_ls     phi_lu    [[1, 0], [1, 1]]     1       yes
    phi_ls     phi_cw    [[1, 1/2], [0, 1/2]] 1/2     yes
    phi_lu     phi_ls    [[1, 0], [-1, 1]]    1       no
    phi_lu     phi_cw    [[1/2, 1/2], [-1/2, 1/2]]  1/2   no
    phi_cw     phi_ls    [[1, -1], [0, 2]]    2       no
    phi_cw     phi_lu    [[1, -1], [1, 1]]    2       no

so exactly two of the six qualify, both out of phi_ls, and the criterion gives the
two corollaries at once:

    corollary 1.  ND_lu(S) is contained in ND_ls(S).
    corollary 2.  ND_cw(S) is contained in ND_ls(S).

and one consequence that matters more to the project than either of them, because
it is what the experiment measures:

    corollary 3.  phi_ls's non-dominated set is the largest of the three and
    contains both others. no map into phi_ls is non-negative, and neither map
    between phi_lu and phi_cw is, so those two are nested in neither direction and
    nothing here relates them.

a word on the direction, because "largest set" and "strongest order" point
opposite ways and a table can get it backwards. phi_ls-dominance implies the other
two, so the phi_ls dominance relation is the weakest of the three, holding for the
fewest pairs, and its non-dominated set is correspondingly the largest.

these are statements about real arithmetic. section 3 states what happens in
doubles, and section 5 says what they are not.


## 2. the proof

### the criterion

let x, y in S and suppose x dominates y under phi_A. write u = phi_A(F(x)) and
v = phi_A(F(y)) for their images in R^2m and put d = v - u. dominance in R^2m is
componentwise, definition 2.1 of [1] and v-04, so

    d >= 0 componentwise, and d != 0.

phi_B = M phi_A acts on each interval objective, so on R^2m it is the block
diagonal matrix with M in each of the m blocks, and

    phi_B(F(y)) - phi_B(F(x)) = M d, block by block.

two steps, one for each hypothesis.

    non-negativity gives M d >= 0. every entry of M d is a sum of products of a
    non-negative entry of M with a non-negative entry of d, so no inequality can
    be reversed by the map.

    invertibility gives M d != 0. the block diagonal matrix is invertible exactly
    when M is, so d != 0 forces M d != 0, and the strictness cannot be cancelled.

together, M d >= 0 and M d != 0, which is exactly phi_B-dominance of x over y.
taking the contrapositive: a point not dominated under phi_B is dominated by
nothing under phi_A either, since any phi_A-dominator would be a phi_B-dominator.
hence ND_B(S) is contained in ND_A(S).

no convexity, no differentiability, no regularity and no structure on S is used,
and the sign of a half-width is never used either. the argument is about the two
image spaces and the map between them, not about F.

the strictness step is the one the criterion turns on, and it is worth saying
exactly how much of invertibility it uses: it uses only that no column of M is
zero, since that is what makes M d != 0 for every non-negative d != 0. a
non-negative M with a zero column loses strictness and the implication fails; the
witness in section 3 is M = [[1, 0], [1, 0]], which maps the distinct phi_ls
images (-2, 0) and (-2, 1) to the same point (-2, -2), an exact tie where there
was a strict inequality. invertibility is nonetheless the right hypothesis to
state, for two reasons: it implies no zero column, and a composite that is not
invertible is not an admissible phi at all, [1]'s condition on the coefficients
being a non-zero determinant and the composite determinant being 2 det phi, v-43.
so a singular M cannot arise between two members of the class.

### the two corollaries, written out

corollary 1, phi_ls to phi_lu, M = [[1, 0], [1, 1]], det 1. writing the phi_ls
image of one objective as (ls_1, ls_2) = (c - r, 2r), the phi_lu image is

    lu_1 = ls_1,   lu_2 = ls_1 + ls_2

which is the identity c + r = (c - r) + 2r. suppose x dominates y under phi_ls,
that is c_x - r_x <= c_y - r_y and r_x <= r_y with one strict. the first phi_lu
coordinate is the first phi_ls coordinate, so it carries unchanged, and adding the
first inequality to twice the second gives c_x + r_x <= c_y + r_y. strictness
carries through either branch: if the first inequality is strict it is already the
strict phi_lu inequality in the first coordinate; if only the second is, then
2 r_x < 2 r_y added to the weak first gives c_x + r_x < c_y + r_y. this is the
argument a-close wrote out and it is the criterion at M = [[1, 0], [1, 1]].

corollary 2, phi_ls to phi_cw, M = [[1, 1/2], [0, 1/2]], det 1/2. the phi_cw image
is

    cw_1 = ls_1 + ls_2 / 2,   cw_2 = ls_2 / 2

which is c = (c - r) + r and r = (2r) / 2. both coefficients are non-negative and
the determinant is 1/2, so the same two steps apply. strictness again carries
through either branch: a strict first phi_ls coordinate makes cw_1 strict, and a
strict second makes cw_2 strict directly, cw_2 being a positive multiple of ls_2.

corollary 3 is the absence of the other four. the map into phi_ls from either of
the others carries a negative entry, -1 from phi_lu and -1 from phi_cw, and so
does each map between phi_lu and phi_cw; since M is unique for each ordered pair,
there is no other matrix to try. the criterion is silent there, and section 3
measures that the implication genuinely fails in those four directions rather than
merely failing to be provable this way.


## 3. the numerical check

run from throwaway scripts in the session scratchpads, numpy and the standard
library only, nothing under src/ and nothing committed. a-close ran parts a, b and
c; a-close-b added the criterion sweep and the audit of section 3.4.

### 3.1 symbolic, through the project's own routes

the four quantities c_A, r_A, c_B, r_B are carried as linear forms with exact
rational coefficients and pushed through phi_registry["ls"].of_centre_radius and
phi_registry["lu"].of_centre_radius of src/phi_transforms.py, so what is checked is
the implemented map and not a restatement of the paper.

    part a. symbolic, through src/phi_transforms.py's own routes
        phi_ls(c_A, r_A) = (c_A + -r_A, 2 r_A)
        phi_lu(c_A, r_A) = (c_A + -r_A, c_A + r_A)
      phi_ls image is (c - r, 2r)                                    ok
      phi_lu image is (c - r, c + r)                                 ok
      lu_2 = ls_1 + ls_2 identically                                 ok
      lu_1(B) - lu_1(A) = ls_1(B) - ls_1(A)                          ok
      lu_2(B) - lu_2(A) = [ls_1(B) - ls_1(A)] + [ls_2(B) - ls_2(A)]  ok
      that combination has coefficients 1 and 1, both non-negative   ok

### 3.2 the criterion itself, in exact rational arithmetic

the six maps are each recomputed as phi_B phi_A^-1 and checked against the images
they are supposed to produce, then every ordered pair of 45 intervals on a rational
grid is tested for whether phi_A-dominance carries to phi_B.

    from       to        M                          det    non-negative   carried
    phi_ls     phi_lu    [[1, 0], [1, 1]]           1      yes            465 of 465
    phi_ls     phi_cw    [[1, 1/2], [0, 1/2]]       1/2    yes            465 of 465
    phi_lu     phi_ls    [[1, 0], [-1, 1]]          1      no             465 of 750
    phi_lu     phi_cw    [[1/2, 1/2], [-1/2, 1/2]]  1/2    no             465 of 750
    phi_cw     phi_ls    [[1, -1], [0, 2]]          2      no             465 of 630
    phi_cw     phi_lu    [[1, -1], [1, 1]]          2      no             465 of 630

    random M, exact rationals, 300 trials each
      non-negative and invertible, m = 1:  0 trials with a pair that fails
      non-negative and invertible, m = 2:  0 trials with a pair that fails
      at least one negative entry, m = 1:  263 trials with a pair that fails

    the two hypotheses, each removed in turn
      M = [[1, 0], [1, 0]], non-negative and singular, det 0: 70 dominating pairs
        lost. witness: ls images (-2, 0) and (-2, 1) both map to (-2, -2).
      M = [[1, -1], [1, 1]], invertible with a negative entry, det 2: 165 lost.

    d >= 0 and d != 0 implies M d >= 0 and M d != 0, over 2000 random
    non-negative invertible M and non-negative d: 0 failures.

both directions matter here. the two non-negative maps carry every dominating pair,
465 of 465, and the four others carry strictly fewer than they are given, which is
what makes each containment strict and section 5's point.

### 3.3 the containments on the project's own problems

p0 on 401 points of its box, p1 on a4's 41 x 41 grid, and zdt1 and dtlz2 at all
four positive levels on a5's constructed separation samples, rebuilt with a5's seed
and sizes. each case is filtered twice. the exact column converts the doubles the
problem returns to the rationals they exactly are, forms the phi columns in exact
rational arithmetic, and replaces each column by its dense rank, which is a
strictly monotone relabelling and therefore leaves the dominance relation
unchanged; the double column is the ordinary computation.

    part c. numerical, on the project's own problems
        p0              n   401 | exact |lu|  401 |ls|  401 violations 0 | doubles |lu|  401 |ls|  401 violations 0 containment 1.000000
        p1              n  1681 | exact |lu|  237 |ls|  706 violations 0 | doubles |lu|  237 |ls|  706 violations 0 containment 1.000000
        zdt1 eps=0.05   n  1024 | exact |lu|  209 |ls|  533 violations 0 | doubles |lu|  208 |ls|  533 violations 0 containment 1.000000
        zdt1 eps=0.1    n  1024 | exact |lu|  247 |ls|  535 violations 0 | doubles |lu|  246 |ls|  535 violations 0 containment 1.000000
        zdt1 eps=0.25   n  1024 | exact |lu|  439 |ls|  535 violations 0 | doubles |lu|  439 |ls|  535 violations 0 containment 1.000000
        zdt1 eps=0.5    n  1024 | exact |lu|  519 |ls|  537 violations 0 | doubles |lu|  519 |ls|  537 violations 0 containment 1.000000
        dtlz2 eps=0.05  n  1728 | exact |lu|  838 |ls| 1281 violations 0 | doubles |lu|  813 |ls| 1256 violations 0 containment 1.000000
        dtlz2 eps=0.1   n  1728 | exact |lu|  995 |ls| 1362 violations 0 | doubles |lu|  951 |ls| 1318 violations 0 containment 1.000000
        dtlz2 eps=0.25  n  1728 | exact |lu| 1284 |ls| 1507 violations 0 | doubles |lu| 1213 |ls| 1436 violations 0 containment 1.000000
        dtlz2 eps=0.5   n  1728 | exact |lu| 1654 |ls| 1691 violations 0 | doubles |lu| 1565 |ls| 1601 violations 1 containment 0.999361

      zero violations in exact arithmetic over every case            ok
        total violations in doubles over the same cases: 1

the columns are reflowed to fit; the numbers are literal.

### 3.4 the audit of a5's separation helper, a-close-b

a5's separation report prints |ls&cw| as 940, 934, 919 and 908 on dtlz2 against
|cw| = 947, which reads as 7, 13, 28 and 39 phi_cw points outside the phi_ls set,
while on zdt1 it equals |cw| in all four rows. a theorem does not hold on one
benchmark and fail on another, so the helper was read and audited before anything
else was believed.

the helper is correct. tests/test_problems_tier1.py's non_dominated_indices returns
a frozenset of row indices, and efficient_sets builds all four sets from one sample
array and one params dictionary, so |ls&cw| is an intersection of index sets over
one array and not of value tuples or of sets indexed against different arrays. it
was recomputed with a second implementation, an explicit pair loop with no
broadcasting, and the index sets are identical in all eight cases, crisp and all
three phi.

    A. the helper's own numbers against a second implementation, both in doubles
       dtlz2 at eps 0.05, 0.10, 0.25, 0.50 and zdt1 at the same four levels:
       index sets identical in 8 of 8 cases, 0 mismatches.

the shortfall is arithmetic. all 39 of the dtlz2 eps = 0.50 points were checked
directly: every one of them is dominated under phi_ls in doubles by a specific
named point, none of them is dominated under phi_ls in exact arithmetic, and none
is dominated under phi_cw in exact arithmetic either. the first, index 1588 against
its double dominator 1600, shows the mechanism whole:

    ls col 0: exact j-i = -6.9699e-19   double j-i =  0.0000e+00
    ls col 2: exact j-i =  8.8838e-18   double j-i =  0.0000e+00
    ls col 4: exact j-i = -1.0061e-03   double j-i = -1.0061e-03
    cw col 0: exact j-i = -6.9699e-19   double j-i = -6.9699e-19
    cw col 2: exact j-i =  8.8838e-18   double j-i =  8.8838e-18
    cw col 4: exact j-i = -1.0061e-03   double j-i = -1.0061e-03

exactly, column 2 is positive, so 1600 is worse than 1588 there and does not
dominate it. computed as c - r, columns 0 and 2 both round to an exact tie,
1600 is then better in column 4 and no worse anywhere, and it dominates. under
phi_cw nothing is subtracted, the 8.9e-18 survives, and 1588 stays non-dominated.

why phi_cw shows a larger count than phi_lu, which is the question the two numbers
raise. phi_cw's centre-radius route is (c, r) with coefficients 1 and 0, so it
commits no arithmetic at all and its columns are the problem's own doubles;
phi_ls's and phi_lu's shared first coordinate is computed as c - r and rounds. so
every rounded tie in c - r is a chance for a phi_cw point to leave the phi_ls set,
while phi_lu, built on the same rounded column, mostly moves with phi_ls and leaves
it only through the rarer c + r against (c - r) + 2r discrepancy of v-46. and why
dtlz2 and not zdt1: the affected points sit at x_1 = 1, where dtlz2's first centre
is (1 + g) cos(pi/2) = 6.1e-17 against a half-width of up to 0.5, so c - r absorbs
the centre entirely; zdt1 has no such face.

every number the helper prints was then recomputed in exact rational arithmetic,
since a helper that miscounted one intersection could miscount the others and these
are the numbers that will fill the e1 and e2 tables.

    B. sizes, exact against double, crisp/lu/ls/cw, and the two violation counts
       dtlz2 0.05    144/838/1281/947    144/813/1256/947    lu\ls 0   cw\ls 7
       dtlz2 0.10    144/995/1362/947    144/951/1318/947    lu\ls 0   cw\ls 13
       dtlz2 0.25   144/1284/1507/947   144/1213/1436/947    lu\ls 0   cw\ls 28
       dtlz2 0.50   144/1654/1691/947   144/1565/1601/947    lu\ls 1   cw\ls 39
       zdt1  0.05      32/209/533/483      32/208/533/483    lu\ls 0   cw\ls 0
       zdt1  0.10      32/247/535/483      32/246/535/483    lu\ls 0   cw\ls 0
       zdt1  0.25      32/439/535/483      32/439/535/483    lu\ls 0   cw\ls 0
       zdt1  0.50      32/519/537/483      32/519/537/483    lu\ls 0   cw\ls 0
       in exact arithmetic lu\ls and cw\ls are 0 in all eight cases.

three things are visible in that table and all three are worth naming. the crisp
column never moves, 144 and 32 in exact and in doubles alike, because it is the
centre columns and no arithmetic is done to them. |cw| never moves either, 947 and
483, for the same reason. every quantity that does move involves phi_ls or phi_lu,
whose first coordinate is the subtraction. the noise is not spread over the report;
it is exactly where the arithmetic is.

the containments were audited the same way, and the two the report did not print
are the two that moved most.

    C. containments, doubles then exact, dtlz2 at eps = 0.50
       doubles  lu<ls 0.999  ls<lu 0.977  lu<cw 0.557  cw<lu 0.920  crisp<cw 1.000  cw<ls 0.959  ls<cw 0.567
       exact    lu<ls 1.000  ls<lu 0.978  lu<cw 0.550  cw<lu 0.961  crisp<cw 1.000  cw<ls 1.000  ls<cw 0.560

the fix, and it is worth being plain about which half of the report was wrong.
nothing in the helper's computation was wrong and no assertion in the suite was
wrong; every assertion that existed passed and still passes, and every index set
it produced was right. what was wrong is that the report printed |ls&cw| with no
containment beside it and no noise count anywhere, so a shortfall that is entirely
double-precision presented as though it were a property of the orders. the report
now prints cw<ls and ls<cw with the other containments and a noise line carrying
|lu \ ls| and |cw \ ls|, which is the count CONTEXT.md section 10 c3 has the
validation gate report. no assertion was added for the phi_cw containment in that
session; c1 added one and c2 added another, as self-checks on the encoding and not
as claims, per the amended standing constraint above.


## 4. relation to proposition 5.1 of [1]

corollary 1 above, the phi_lu case, is the interval-space analogue of
proposition 5.1 of [1]. corollary 2, the phi_cw case, has no counterpart anywhere
in the paper: v-25 records that example 2.4's solution set is related to no other
automorphism's in any statement of [1], fuzzy or interval.

what the paper states, transcribed in docs/a0_framework.md c16 and verified as
v-24: for the multiobjective **fuzzy** interval problems (1MFIOP_phi) and
(1MFIOP_psi) sharing S and F-tilde, with phi the automorphism of example 2.2 and
psi that of example 2.3, if x-bar is an optimal solution for (1MFIOP_phi) then
x-bar is also an optimal solution for (1MFIOP_psi). so Opt(example 2.2) is
contained in Opt(example 2.3): the example 2.3 set is the larger one. the
proposition carries no convexity, no differentiability, no constraint
qualification and no structure on S, is stated for the optimal solution concept
of definition 5.1(2) only, and has no converse.

what a0-b established about the interval side, v-25 and v-26 and the search method
in docs/a0_framework.md c17: sections 2 and 3 of [1] contain no stated relation
between the solution sets of two different automorphisms and no interval-space
analogue of proposition 5.1. psi does not occur anywhere in lines 99 to 771, no
line of those sections names two different examples from 2.1 to 2.4 together, and
the comparative and containment vocabulary sweep returns only the car-purchase
prose of example 2.1. that was the answer a0-b was asked for and it stopped there,
raising p-03.

so this document does not find the interval statement in [1]. it proves it, from
the definitions [1] gives, as one instance of the criterion of section 1, and for
the phi_lu case the correspondence is exact in three respects and worth stating in
all three:

    same two automorphisms, examples 2.2 and 2.3, in the same direction, from 2.2
    to 2.3, giving the same containment, the example 2.3 set the larger one.

    same absence of hypotheses. proposition 5.1 assumes nothing beyond a shared S
    and F-tilde; the argument of section 2 assumes nothing beyond a shared S and F.

    same one-directionality. [1] states no converse and none holds here, section 5.

it is not a corollary of proposition 5.1 and is not derived from it. the fuzzy
result is about fuzzy problems, and theorem 5.1 of [1], v-27, is what relates the
fuzzy and the interval formulations; nothing in this document goes through either.
the interval statement is proved directly and independently, and the relation to
proposition 5.1 is a resemblance of statements and not a chain of implication.

that resemblance is the reason for s-11 rather than a reason to be confident. the
proof is a few lines, which usually means either that it is right or that the
interesting content is somewhere else, and the paper's own framing of proposition
5.1 is "there exist cases", docs/a0_framework.md c16, which is the framing of an
exception rather than of a general relation between automorphisms. the criterion
of section 1 is a general relation between automorphisms, which is a larger claim
than the one [1] makes, and that is the second reason to hand it to the
supervisors before using it.




## 5. what these are not, and what they cost the experiment

five limits, each of which a table or a memoria paragraph could get wrong.

they are containments and not equalities. the converse fails in every case, and
section 3.2 counts it: the four maps with a negative entry carry 465 dominating
pairs out of the 750, 750, 630 and 630 they are given. on the project's own
problems the sets are measured strictly different at every level, |lu| < |ls| and
|cw| < |ls| in every row of section 3.3 and 3.4, and a containment that is total in
one direction is not evidence that two sets are close: at dtlz2 eps = 0.05 the
exact ls<lu containment is 0.654 and ls<cw is 0.739.

they say nothing about phi_lu against phi_cw. neither map between those two is
non-negative, section 1, and section 3.2 measures the implication failing in both
directions, 465 of 750 and 465 of 630. a1-b and a5 measure the same thing on the
problems and tests/test_problems_tier1.py asserts it, 0 < containment(lu, cw) < 1
and 0 < containment(cw, lu) < 1 at every positive level on both benchmarks. so the
three phi are not a chain and no table may present them as one.

the consequence for e3, which is the reason this section is not only a caution.
phi_ls is the largest of the three sets and contains both others, so a measured
difference between phi_ls and phi_lu, or between phi_ls and phi_cw, is in part a
theorem: one direction of any coverage or overlap statistic on those pairs is
constrained before a solver is run, and reporting it as evidence that the
efficient set is sensitive to the order would be reporting the criterion of section
1. the comparison that carries the sensitivity signal is phi_lu against phi_cw,
which are nested in neither direction and where nothing is fixed in advance. this
is recorded in CONTEXT.md section 10 e3 and it is the one place where these results
change what the project will report, rather than what it will claim.

they are statements about non-dominated sets and not about recovered fronts. what a
solver returns is not ND(S) but an approximation of it under a budget, and nothing
here says a run under phi_lu returns a subset of a run under phi_ls. c3's recovery
check and d2's coverage measure the recovered sets, and these results constrain the
exact sets those approximate and not the approximations.

they do not hold in doubles, and that is not a defect of the statements. section
3.4 measures both failures and their cause, one rounded subtraction, and section 3.3
shows the exact filter putting every point back. a violation of an exact containment
in floating point is by definition numerical noise, and that observation needs no
confirmation from anyone: it is recorded in CONTEXT.md section 10 c3, where the
validation gate reports the violation count as a measure of that noise in the
pipeline, and it is on a5's separation report as the noise line.


## 6. what is asked of the supervisors

s-11, raised in PROGRESS.md section 6 with this document as its reference, asks
three things and nothing else.

    is the criterion of section 1 correct? it is written out in section 2 with both
    hypotheses used explicitly, with the strictness step isolated, and with each
    hypothesis removed in turn in section 3.2 to show that it is needed.

    are both containments correct? corollary 1 for phi_lu is the case a-close
    verified and the one the project already carries two tests around, v-46 and the
    band assertion in tests/test_problems_tier1.py. corollary 2 for phi_cw was
    reached in a-close-b, and since c1 both are asserted on solver output as
    self-checks on the encoding, exactly and with no band, on p1 and on both tier 1
    benchmarks. that is evidence that the project's own arithmetic reproduces them
    and it is not evidence that they are correct as mathematics, which is what is
    being asked here.

    is any of it already published? [1] cites its own reference [26] for
    LS-convexity in example 2.3 and for LS-Pareto in the conclusion, line 1526,
    docs/a0_framework.md, so [26] is where the phi_lu statement would sit. [9], the
    m = 1 predecessor where the order relations on C are defined, and [31], cited
    for LU-convexity and CW-convexity, are the other two candidates. the phi_cw
    statement and the general criterion have no candidate location at all: v-25
    records that [1] relates example 2.4's solution set to nothing, and the
    criterion is about the class rather than about a pair of its members, which is
    a kind of statement [1] makes nowhere in sections 2 or 3, v-26. none of the
    three references is resolvable from the extracted text, r-03, and none is among
    the five papers of CONTEXT.md section 3.

the reason the third question matters most. if the statements are published, the
memoria cites them and this document becomes a verification of known results on
this project's problems. if they are not, the memoria has a small original
observation in it, and one that a project whose own rules forbid it from proving
theorems, CONTEXT.md section 7, should hand to its supervisors rather than present
on its own authority. the criterion is the part to be most careful with, being a
statement about the whole class and not about three named examples.

until an answer arrives, p-03 is closed by this document, r-06 carries the
correction a-close-b made to it, e3 is told in CONTEXT.md which comparison carries
the signal, and nothing else is built on any of it.
