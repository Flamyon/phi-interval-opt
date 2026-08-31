# a-close: the phi_lu inside phi_ls containment

session a-close, 2026-08-31. phase a close-out. no module was written or changed
in this session and none of what follows is used by any of them.

what this document is for. a5 recorded, as v-46 and r-11, that the phi_lu
non-dominated set is contained in the phi_ls one and that the containment is
exact in real arithmetic. that was recorded there as an observation with a proof
sketch beside it. this session verifies the argument, symbolically and
numerically, writes it out in full, and places it against proposition 5.1 of [1].

the standing constraint, stated first because it governs everything below. the
project does not build on this result. it is recorded, not used. b1 derives its
efficient sets from [1]'s own results and does not shorten a derivation with it;
d2 and e3 report the phi_lu against phi_ls pair as a check on r-06's prediction
and never as an independent finding. that stands until the supervisors answer
s-11.

[1] is papers/new_preference_order_relationships_paper.txt, costa, osuna-gomez
and chalco-cano, "new preference order relationships and their application to
multiobjective interval and fuzzy interval optimization problems", fuzzy sets and
systems 477 (2024) 108812.


## 1. the statement

fix a feasible set S and a multi-interval-valued objective F with m interval
components, and write each component as its centre and half-width, c_i(x) and
r_i(x) >= 0, so that F_i(x) = [c_i - r_i, c_i + r_i]. write phi_lu for the
automorphism of example 2.2 of [1] and phi_ls for that of example 2.3, verified
as v-06 and v-07. in centre and half-width coordinates, CONTEXT.md section 4 and
v-43:

    phi_lu   (c_i - r_i,  c_i + r_i)
    phi_ls   (c_i - r_i,  2 r_i)

let ND_phi(S) be the non-dominated set of the transformed real problem under phi,
under the ordinary pareto relation on R^2m that CONTEXT.md section 5 step 5 fixes
for the whole project.

    claim. for every x, y in S: if x dominates y under phi_ls then x dominates y
    under phi_lu. equivalently ND_lu(S) is contained in ND_ls(S).

the claim is about real arithmetic. section 3 states what happens in doubles and
section 5 says what the claim is not.


## 2. the proof

one objective first, then the lift to m of them.

### one interval objective

let A and B be two intervals with centres c_A, c_B and half-widths r_A, r_B.
suppose A dominates B under phi_ls. by the componentwise definition of the order,
that is

    (1)  c_A - r_A <= c_B - r_B
    (2)  2 r_A <= 2 r_B, that is r_A <= r_B

with at least one of the two strict. the first coordinate of phi_lu is the first
coordinate of phi_ls, so (1) is already the first phi_lu inequality. for the
second, add (1) and twice (2):

    c_A + r_A = (c_A - r_A) + 2 r_A <= (c_B - r_B) + 2 r_B = c_B + r_B

so both phi_lu inequalities hold. strictness carries through either branch:

    branch 1, (1) strict. then c_A - r_A < c_B - r_B is itself the strict phi_lu
    inequality in the first coordinate, and the second coordinate holds weakly by
    the sum above. phi_lu dominance holds.

    branch 2, (2) strict and (1) weak. then r_A < r_B, so 2 r_A < 2 r_B, and
    adding the weak (1) to it gives c_A + r_A < c_B + r_B strictly. the strictness
    has moved from the second coordinate of phi_ls to the second coordinate of
    phi_lu. phi_lu dominance holds.

in both branches every phi_lu coordinate is weakly better and at least one is
strictly better, which is phi_lu dominance. that is the whole argument.

the structural reason, which is what makes it hold and not a coincidence of these
two examples: the phi_lu image is an order-preserving linear function of the phi_ls
image, coordinate by coordinate,

    lu_1 = ls_1,    lu_2 = ls_1 + ls_2

with non-negative coefficients only, so no phi_ls inequality can be reversed by
the map and no strictness can be cancelled by it. the map is not injective on
inequalities in the other direction, which is section 5's point.

### m interval objectives

dominance in R^2m is componentwise, definition 2.1 of [1] and v-04, and the order
decomposes objective by objective. so if x dominates y under phi_ls then for every
i the four inequalities (1) and (2) hold for objective i, weakly, with at least
one strict somewhere among the 2m coordinates. applying the single-objective
argument to each i gives every phi_lu coordinate weakly better; and the strict one,
wherever it sits, carries by branch 1 if it is a first coordinate and by branch 2
if it is a second. so x dominates y under phi_lu.

### the contrapositive, which is the containment

if x is not dominated under phi_lu then it is dominated by nothing under phi_ls
either, since any phi_ls dominator would be a phi_lu dominator. hence

    ND_lu(S) is contained in ND_ls(S)

for every S and every F. no convexity, no differentiability, no regularity and no
structure on S is used, and the argument never uses the sign of a half-width
either: it uses r_A <= r_B and nothing about r_A >= 0.


## 3. the numerical check

run from a throwaway script in the session scratchpad, numpy and the standard
library only, nothing under src/ and nothing committed. three parts. the literal
output is reproduced below.

part a is symbolic and runs through the project's own routes. the four quantities
c_A, r_A, c_B, r_B are carried as linear forms with exact rational coefficients
and pushed through phi_registry["ls"].of_centre_radius and
phi_registry["lu"].of_centre_radius of src/phi_transforms.py, so what is checked is
the implemented map and not a restatement of the paper. it confirms the two images,
the identity lu_2 = ls_1 + ls_2, and the difference decomposition
lu_2(B) - lu_2(A) = [ls_1(B) - ls_1(A)] + [ls_2(B) - ls_2(A)] with both
coefficients equal to 1.

part b is an exhaustive case analysis in exact rational arithmetic over a grid of
45 intervals, all 1980 ordered pairs. every phi_ls-dominating pair is
phi_lu-dominating, 465 of 465, and both strictness branches are exercised, 395
pairs strict in the first coordinate and 70 strict in the second only. part b2
repeats it at m = 2 over 81 interval vectors and 6480 ordered pairs, 648 of 648,
608 and 40. the same enumeration finds 285 pairs dominating under phi_lu and not
under phi_ls, which is section 5's containment-and-not-equality, with a witness
printed.

part c is the containment itself on the project's own problems: p0 on 401 points
of its box, p1 on a4's 41 x 41 grid, and zdt1 and dtlz2 at all four positive levels
on a5's constructed separation samples, which are rebuilt here with a5's seed and
sizes and reproduce a5's sets. each case is filtered twice. the exact column
converts the doubles the problem returns to the rationals they exactly are, forms
the phi columns in exact rational arithmetic, and replaces each column by its dense
rank, which is a strictly monotone relabelling and therefore leaves the dominance
relation unchanged; the double column is the ordinary computation. the exact
filter shows zero violations in every case. the double filter shows one, on dtlz2
at eps = 0.50, which is exactly the point v-46 and r-11 record.

    part a. symbolic, through src/phi_transforms.py's own routes
        phi_ls(c_A, r_A) = (c_A + -r_A, 2 r_A)
        phi_lu(c_A, r_A) = (c_A + -r_A, c_A + r_A)
      phi_ls image is (c - r, 2r)                                    ok
      phi_lu image is (c - r, c + r)                                 ok
      lu_2 = ls_1 + ls_2 identically                                 ok
      lu_1(B) - lu_1(A) = ls_1(B) - ls_1(A)                          ok
      lu_2(B) - lu_2(A) = [ls_1(B) - ls_1(A)] + [ls_2(B) - ls_2(A)]  ok
      that combination has coefficients 1 and 1, both non-negative   ok
        lu_2(B) - lu_2(A) as a form:  -c_A + -r_A + c_B + r_B
        ls_1(B) - ls_1(A) as a form:  -c_A + r_A + c_B + -r_B
        ls_2(B) - ls_2(A) as a form:  -2 r_A + 2 r_B

    part b. exhaustive case analysis in exact rational arithmetic
        45 points, 1980 ordered pairs
        ls dominating pairs                      465
        of which lu dominating                   465
        strict in the first coordinate           395
        strict in the second coordinate only     70
        lu dominating but not ls dominating      285
      every ls-dominating pair is lu-dominating                      ok
      both strictness branches are exercised                         ok
      the converse fails, so it is a containment and not an equality ok
        converse witness: A = (c -2, r 1/2), B = (c -3/2, r 0)
          lu images (-5/2, -3/2) and (-3/2, -3/2); ls images (-5/2, 1) and (-3/2, 0)

    part b2. the same, lifted to m = 2 interval objectives
        81 vectors, 6480 ordered pairs
        ls dominating pairs                      648
        of which lu dominating                   648
        strict in some first coordinate          608
        strict in second coordinates only        40
      the lift holds at m = 2 with both branches exercised           ok

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

    all checks passed

the part c columns line up wider than the terminal, so they are reflowed here;
the numbers are literal and nothing else is edited.

two things in that table are worth naming and neither is the claim.

the single double-precision violation is v-46's and r-11's, reproduced with an
independent implementation: dtlz2 at eps = 0.50, one point of the 1565 that
survive under phi_lu, containment 0.999361. the exact filter puts it back, which
is the direct demonstration that it is rounding and nothing else.

the exact and double set sizes differ by more than that one point. on dtlz2 the
exact non-dominated sets are larger at every level, 838 against 813 at eps = 0.05
up to 1654 against 1565 at eps = 0.50, and on zdt1 by one point at two levels.
that is not a containment violation and nothing in the project has so far
depended on it, but the mechanism is worth naming because it is the same
cancellation. the phi_ls set at eps = 0.05 loses 25 points in doubles, and the
first of them is dominated in doubles and not in exact arithmetic by one column
alone: the exact difference in that column is +7.1e-19 in the surviving point's
favour, and computing it as c - r rounds it to exactly 0.0, an exact tie, which
removes the only coordinate that was keeping the point non-dominated. so the noise
does not only break ties, it manufactures them, and it does so through the same
c - r subtraction that produces the containment violation. it is measured here and
it is not carried into any claim.


## 4. relation to proposition 5.1 of [1]

the claim above is the interval-space analogue of proposition 5.1 of [1].

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

so this document does not find the interval statement in [1]. it proves it, in one
line, from the definitions [1] gives, and the correspondence is exact in three
respects and worth stating in all three:

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
proof is one line, which usually means either that it is right or that the
interesting content is somewhere else, and the paper's own framing of proposition
5.1 is "there exist cases", docs/a0_framework.md c16, which is the framing of an
exception rather than of a general relation between automorphisms.


## 5. what it is not

four limits, each of which a table or a memoria paragraph could get wrong.

it says nothing about phi_cw. the claim relates examples 2.2 and 2.3 and only
those two, which is exactly the pair proposition 5.1 relates, and phi_cw enters no
part of section 2. in particular it is not a statement that the three phi form a
chain, and nothing here changes what a1-b and a5 measured about phi_cw against
phi_lu: those two are nested in neither direction, structurally because the map
from either image to the other carries a negative coefficient, and measurably
because tests/test_problems_tier1.py asserts 0 < containment(lu, cw) < 1 and
0 < containment(cw, lu) < 1 at every positive level on both benchmarks. v-25
records that [1] relates example 2.4's solution set to nothing at all.

one observation was made while checking that and is written down here rather than
developed, because this session's brief is to record the phi_lu containment and no
further. the coefficients that carry section 2 are non-negative because the phi_lu
image is ls_1 and ls_1 + ls_2. the phi_cw image is ls_1 + ls_2 / 2 and ls_2 / 2,
whose coefficients are non-negative as well, which would put ND_cw inside ND_ls by
the same argument. the same throwaway script measures it: 465 of 465 dominating
pairs carry on the rational grid of section 3 part b, and the exact filter returns
ND_cw contained in ND_ls with zero exceptions on p1 and on both benchmarks at
eps = 0.05 and eps = 0.50, |cw| of 441, 483, 483, 947 and 947 against the |ls| of
section 3. it is recorded and not claimed: it has not been written out, it is not
in section 2, it is not in s-11, and nothing is built on it. it is here so that a
later session finds it instead of rediscovering it, and so that r-06's remark that
"the phi_cw comparisons are unaffected" is re-examined in the research chat rather
than relied on. what does not change either way is the phi_lu against phi_cw pair
above, which is nested in neither direction.

it is a containment and not an equality. the converse fails, and section 3 part b
counts 285 ordered pairs on a small rational grid that dominate under phi_lu and
not under phi_ls, with the witness A = (c = -2, r = 1/2), B = (c = -3/2, r = 0),
whose phi_lu images are (-5/2, -3/2) and (-3/2, -3/2), where A dominates, and
whose phi_ls images are (-5/2, 1) and (-3/2, 0), where neither dominates. the two
sets are measured strictly different at every level in a5, |lu| < |ls| in every
row of section 3 part c, and the containment being total in one direction is not
evidence that the sets are close.

it is a statement about non-dominated sets and not about the recovered fronts.
what a solver returns is not ND(S) but an approximation of it under a budget, and
nothing here says a run under phi_lu returns a subset of a run under phi_ls. c3's
recovery check and d2's coverage measure the recovered sets, and this result
constrains the exact sets those approximate and not the approximations.

it does not hold in doubles, and that is not a defect of the statement. r-11 and
section 3 measure the violation, one point of 1565 on dtlz2 at eps = 0.50 where
the first centre is (1 + g) cos(pi/2) = 6.1e-17 against a half-width of 0.5, so
that c - r absorbs a difference that c + r keeps. a violation of an exact
containment in floating point is by definition numerical noise, and that
observation needs no confirmation from anyone: it is recorded in CONTEXT.md
section 10 c3, where the validation gate reports the violation count as a measure
of that noise in the pipeline.


## 6. what is asked of the supervisors

s-11, raised in PROGRESS.md section 6 with this document as its reference, asks
two things and nothing else.

    is the argument correct? it is one line and it is written out in section 2
    with both strictness branches and with the lift to m objectives. an error in
    it would be an error the project has already built two tests around, v-46 and
    the band assertion in tests/test_problems_tier1.py.

    is the interval statement already published? [1] cites its own reference [26]
    for LS-convexity in example 2.3 and for LS-Pareto in the conclusion, line 1526,
    docs/a0_framework.md, so [26] is where such a statement would sit. [9], the
    m = 1 predecessor where the order relations on C are defined, and [31], cited
    for LU-convexity and CW-convexity, are the other two candidates. none of the
    three is resolvable from the extracted text, r-03, and none is among the five
    papers of CONTEXT.md section 3.

the reason the second question matters more than the first. if the statement is
published, the memoria cites it and this document becomes a verification of a
known result on this project's problems. if it is not, the memoria has a small
original observation in it, and one that a project whose own rules forbid it from
proving theorems, CONTEXT.md section 7, should hand to its supervisors rather than
present on its own authority.

until either answer arrives, p-03 is closed by this document and nothing is built
on the result.
