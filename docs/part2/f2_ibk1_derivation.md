# f2: the analytic derivation of the phi-efficient sets of I-BK1

subpart f2 of phase f, CONTEXT.md section 10 and docs/plan_after_meeting.md
section a2. **paper and pencil with symbolic verification. no module, no run, no
code beyond the algebra, and nothing from [16] implemented.** this is
docs/part1/b1_phi_efficient_sets.md's method applied to a problem the project did
not construct.

sources read in this session:

    docs/part2/lit_review.md, all of section 1, for the transcription of I-BK1
        (1.8), the checkpoints (1.6), the gate verdicts (1.9) and the ordering
        decision (7.2); section 3.2 for [10] proposition 32.
    docs/part1/b1_phi_efficient_sets.md, as the model and for the route.
    docs/part1/part1_closing.md sections 6.1, 7.2 and 7.3.
    papers/Newton Method for Multiobjective Optimization Problems of
        Interval-Valued Maps.pdf, [16], for problem 1 (printed page 27), the
        gH-gradients and gH-Hessians (printed page 18), Table 1 and equations
        (23)-(25) and Table 2 (printed pages 20-21), definitions 2.2 (printed page
        4), 2.14 (printed page 6), 2.16 to 2.19, lemma 2.4 and proposition 2.1
        (all printed page 7).
    docs/part1/a0_framework.md, for [1]'s theorem 3.3 (c12, printed page 9),
        example 3.8 (c13, printed page 10), example 3.9 and condition (15) (c14,
        printed page 10) and definition 3.1 (c10, printed page 6).

every theorem, example and equation below is cited by number and printed page. no
condition is invented, extended or weakened anywhere in what follows.

symbolic work used exact rational arithmetic from `fractions`, the standard
library, sympy not being in the venv and CONTEXT.md section 11 not permitting a
dependency added for one session — the same constraint b1 worked under. every
script was a throwaway in the session scratchpad; nothing was added under src/ and
no test was changed.

**the headline, stated first because one half of it is a negative.** the
derivation closes, exactly and under all three phi, with no singular weight
directions and no reservation of the kind b1 carried on p1. **criterion 3 passes**:
the three sets are distinct, and they are strictly nested. **the first external
check passes** — equation (25)'s published one-parameter curve lies inside all
three derived sets, and eight of Table 2's eleven published points sit on it,
two more being its corners.
**the second external check fails, and the failure is located in the paper and not
in the derivation**: Table 1's x⋆ is not a Pareto optimal point of I-BK1 in [16]'s
own definition 2.17, and that is demonstrated in section 4.2 by an explicit
dominating point checked against the paper's own printed G(x⋆) row, without using
anything derived here. section 4.3 identifies the mechanism and section 6 states
what the stopping rule makes of it.


## 0. the cheap check the brief asks for first

under coefficient imprecision the objective is G_i = ⊕_j [a_ij, b_ij] ⊙ h_ij(x)
with h_ij real-valued, which is the shape docs/part2/lit_review.md claim 1.1
confirms for nineteen of [16]'s twenty problems. where every h_ij is non-negative
on the box — true of all five candidates, whose h_ij are squares, positive linear
terms or positive reciprocals — Moore's product does not interchange the
boundary functions and

    G_i(x)  =  [ Σ_j a_ij h_ij(x),  Σ_j b_ij h_ij(x) ]

so the centre and the half-width are **two different linear combinations of the
same basis functions h_ij**:

    c_i(x) = Σ_j μ_ij h_ij(x),   μ_ij = (a_ij + b_ij)/2
    r_i(x) = Σ_j ρ_ij h_ij(x),   ρ_ij = (b_ij − a_ij)/2

**the general statement, which is what answers the standing objection.** ρ_i is
proportional to μ_i exactly when ρ_ij/μ_ij is the same number for every j, that is
exactly when **every coefficient interval of that objective has the same relative
half-width** (b−a)/(b+a). in that case r_i = t·c_i with t that common ratio, the
half-width is an exact function of the centre, and
docs/part1/part1_closing.md section 6.1's degeneracy applies: the image of the
feasible set in the centre-half-width plane is a curve, every injective phi maps
it to a monotone curve, and the three orders coincide. where the h_ij are linearly
independent as functions — true here, the h_ij being x_1², x_2² and their
translates — proportionality of the coefficient vectors is also **necessary** for
r_i to be a fixed multiple of c_i, so the check is not merely sufficient.

**this is the analytic form of the check a1 had to make by measurement**, and the
point of recording it is that on these problems the answer is fixed by the
published coefficients. the project chose nothing.

the check, one line per objective, in exact rationals. `r_j/c_j` is the column
ρ_ij/μ_ij:

    problem   objective   r_j/c_j per term                proportional
    I-BK1     G_1         1/3, 1/2                        no
    I-BK1     G_2         1/2, 2/3                        no
    I-SD      G_1         0.2, 0.101021, 0.101021, 0.5    no
    I-SD      G_2         0.2, 0.295059, 0.295059, 0.2    no
    I-IKK1    G_1         0, 1                            no
    I-IKK1    G_2         0, 1                            no
    I-IKK1    G_3         1, 0                            no
    I-VFM1    G_1         1/3, 1/2                        no
    I-VFM1    G_2         1/2, 1/3, 0                     no
    I-VFM1    G_3         1/3, 2/3, 0                     no
    I-MHHM2   G_1         1/5, 1/3                        no
    I-MHHM2   G_2         1/3, 1/5                        no
    I-MHHM2   G_3         1/9, 1/11                       no

**no objective of any of the five candidates has proportional centre and
half-width coefficient vectors.** I-SD's two irrational entries are the only ones
computed in floating point, and the gaps there (0.2 against 0.101021, and 0.2
against 0.295059) are far outside any rounding. I-MHHM2's G_3 is the closest call
in the table, 1/9 against 1/11, and it is still a strict inequality in exact
rationals.

three things are worth saying about the table rather than leaving it to be read.

**I-IKK1's zeros are not a failure of the check.** its degenerate coefficient
[1,1] gives ρ_ij = 0 on one term and [0,1] gives ρ_ij/μ_ij = 1 on the other, so
the two vectors are as far from proportional as they can be: the half-width
depends on a variable the centre's ratio does not weight the same way. that is the
structure lit_review section 1.10 records as putting I-IKK1 outside the alignment
regime.

**the degenerate constants in I-VFM1 contribute ρ = 0 with μ ≠ 0** and so are
themselves a source of non-proportionality; but I-VFM1's first two terms are
already non-proportional without them, so the verdict does not rest on the
constants.

**I-BK1's ratios are 1/3 against 1/2 on G_1 and 1/2 against 2/3 on G_2**, which is
docs/part2/lit_review.md section 1.10's observation restated exactly: the
half-width is not a multiple of the centre. the reading could say no more than
that; sections 2 and 3 below say what it is worth.


## 1. the hypotheses, per phi

### 1.1 I-BK1, and why the boundary functions are what they are

problem 1 of appendix A, [16] printed page 27, transcribed by
docs/part2/lit_review.md section 1.8 and re-read from the paper this session:

>     G_1(x_1, x_2) := [0.1, 0.2] ⊙ x_1²  ⊕  [0.1, 0.3] ⊙ x_2²
>     G_2(x_1, x_2) := [0.1, 0.3] ⊙ (x_1 − 5)²  ⊕  [0.1, 0.5] ⊙ (x_2 − 5)²
>     lb^T = (−10, −10) and ub^T = (10, 10)

so n = 2, m = 2, 2m = 4, and S is the box [−10, 10]².

**every h_ij is a square, hence non-negative on the whole plane**, so ⊙ does not
interchange the boundary functions anywhere and [16]'s own condition of printed
page 27 for the 2m transformation — docs/part2/lit_review.md section 1.7 — is
satisfied. the boundary functions are

    G̲_1 = (1/10)x_1² + (1/10)x_2²        Ḡ_1 = (1/5)x_1² + (3/10)x_2²
    G̲_2 = (1/10)(x_1−5)² + (1/10)(x_2−5)²  Ḡ_2 = (3/10)(x_1−5)² + (1/2)(x_2−5)²

and the centre and half-width representation is

    c_1 = (3/20)x_1² + (1/5)x_2²          r_1 = (1/20)x_1² + (1/10)x_2²
    c_2 = (1/5)(x_1−5)² + (3/10)(x_2−5)²  r_2 = (1/10)(x_1−5)² + (1/5)(x_2−5)²

**this reading is the paper's own, and the paper confirms it.** the gH-gradients
and gH-Hessians [16] prints for I-BK1 on printed page 18,

    ∇_gH G_1 = ([0.2,0.4]⊙x_1, [0.2,0.6]⊙x_2)^T,
    ∇_gH G_2 = ([0.2,0.6]⊙(x_1−5), [0.2,1]⊙(x_2−5))^T,
    ∇²_gH G_1 = diag([0.2,0.4], [0.2,0.6]),  ∇²_gH G_2 = diag([0.2,0.6], [0.2,1]),

are exactly the derivatives of the four boundary functions above, endpoint by
endpoint. that is an independent confirmation, from the paper, that the project
and the paper are working with the same object.

### 1.2 the twelve image coordinates

with Λ_i^T f = λ_{2i−1} f_i + λ_{2i} f̄_i and B_i^T f = β_{2i−1} f_i + β_{2i} f̄_i
from theorem 3.3's proof, [1] printed page 9, transcribed in
docs/part1/a0_framework.md c12, and the three registry members as
docs/part1/a0_framework.md c6, c7 and c8 verify them:

    phi_lu, example 2.2 of [1], lambda = (1, 0), beta = (0, 1)

      g_1 = Λ_1^T f = G̲_1 = (1/10)x_1² + (1/10)x_2²
      g_2 = B_1^T f = Ḡ_1 = (1/5)x_1² + (3/10)x_2²
      g_3 = Λ_2^T f = G̲_2 = (1/10)(x_1−5)² + (1/10)(x_2−5)²
      g_4 = B_2^T f = Ḡ_2 = (3/10)(x_1−5)² + (1/2)(x_2−5)²

    phi_ls, example 2.3, lambda = (1, 0), beta = (−1, 1)

      g_1 = G̲_1, as above
      g_2 = 2 r_1 = (1/10)x_1² + (1/5)x_2²
      g_3 = G̲_2, as above
      g_4 = 2 r_2 = (1/5)(x_1−5)² + (2/5)(x_2−5)²

    phi_cw, example 2.4, lambda = (1/2, 1/2), beta = (−1/2, 1/2)

      g_1 = c_1 = (3/20)x_1² + (1/5)x_2²
      g_2 = r_1 = (1/20)x_1² + (1/10)x_2²
      g_3 = c_2 = (1/5)(x_1−5)² + (3/10)(x_2−5)²
      g_4 = r_2 = (1/10)(x_1−5)² + (1/5)(x_2−5)²

these were verified in exact rational arithmetic against the problem statement —
built up from Moore's product and the Minkowski sum as [16] definition 2.1 states
them, then compared with the three phi applied to (G̲_i, Ḡ_i) — on 4000 random
rational points of the box:

    image coordinates vs the problem statement: 0 mismatches, 4000 points x 3 phi

**every one of the twelve is a two-term diagonal quadratic with strictly positive
coefficients.** writing each as (1/2)x^T H_k x + b_k^T x + const:

    phi_lu   H_1 = diag(1/5, 1/5)     b_1 = ( 0,  0)
             H_2 = diag(2/5, 3/5)     b_2 = ( 0,  0)
             H_3 = diag(1/5, 1/5)     b_3 = (−1, −1)
             H_4 = diag(3/5, 1)       b_4 = (−3, −5)

    phi_ls   H_1 = diag(1/5, 1/5)     b_1 = ( 0,  0)
             H_2 = diag(1/5, 2/5)     b_2 = ( 0,  0)
             H_3 = diag(1/5, 1/5)     b_3 = (−1, −1)
             H_4 = diag(2/5, 4/5)     b_4 = (−2, −4)

    phi_cw   H_1 = diag(3/10, 2/5)    b_1 = ( 0,  0)
             H_2 = diag(1/10, 1/5)    b_2 = ( 0,  0)
             H_3 = diag(2/5, 3/5)     b_3 = (−2, −3)
             H_4 = diag(1/5, 2/5)     b_4 = (−1, −2)

**every hessian is diagonal, constant and strictly positive definite.** that last
word is the difference from p1 and it governs everything below. on p1 the width
coordinates were functions of one variable each, so their hessians had a zero
eigenvalue and produced b1's two singular weight rays; **on I-BK1 no image
coordinate is a function of one variable**, because each objective's coefficient
interval is non-degenerate on both terms, so no hessian is singular and no
non-negative combination of them is.

### 1.3 convexity, by theorem 3.3 of [1]

theorem 3.3, [1] printed page 9, transcribed in docs/part1/a0_framework.md c12 and
recorded as v-12:

> **Theorem 3.3.** ... Then F is φ-convex if and only if Λ_i^T f and B_i^T f are
> convex for all i ∈ {1, …, m}, where f = (f_1, f̄_1, …, f_m, f̄_m).

each g_k is a quadratic with a constant hessian, so it is convex on ℝ² if and only
if that hessian is positive semidefinite, and the verdict is global rather than
pointwise. every hessian above is diagonal, so its eigenvalues are its diagonal
entries:

    phi   coordinate            hessian            eigenvalues    convex
    lu    g_1 = G̲_1            diag(1/5, 1/5)     1/5, 1/5       yes, positive definite
    lu    g_2 = Ḡ_1            diag(2/5, 3/5)     2/5, 3/5       yes, positive definite
    lu    g_3 = G̲_2            diag(1/5, 1/5)     1/5, 1/5       yes, positive definite
    lu    g_4 = Ḡ_2            diag(3/5, 1)       3/5, 1         yes, positive definite
    ls    g_1 = G̲_1            diag(1/5, 1/5)     1/5, 1/5       yes, positive definite
    ls    g_2 = 2 r_1           diag(1/5, 2/5)     1/5, 2/5       yes, positive definite
    ls    g_3 = G̲_2            diag(1/5, 1/5)     1/5, 1/5       yes, positive definite
    ls    g_4 = 2 r_2           diag(2/5, 4/5)     2/5, 4/5       yes, positive definite
    cw    g_1 = c_1             diag(3/10, 2/5)    3/10, 2/5      yes, positive definite
    cw    g_2 = r_1             diag(1/10, 1/5)    1/10, 1/5      yes, positive definite
    cw    g_3 = c_2             diag(2/5, 3/5)     2/5, 3/5       yes, positive definite
    cw    g_4 = r_2             diag(1/5, 2/5)     1/5, 2/5       yes, positive definite

so by theorem 3.3, **F is φ-convex for all three phi, globally on ℝ² and a
fortiori on the box**, and remark 2.2, the pointwise form transcribed in a0 c12
and recorded as v-13, holds at every point. **there is no semidefinite row**,
which on p1 there were four of.

this reproduces docs/part2/lit_review.md section 1.9's criterion-2 verdict for
I-BK1 — "all twelve image coordinates under the three phi are
non-negative-coefficient diagonal quadratics" — and sharpens it from non-negative
to strictly positive.

### 1.4 regularity, by [10] proposition 32 and then [10] theorem 34

the brief instructs that regularity be checked by proposition 32 rather than by a
strict-positivity rule, per docs/part2/lit_review.md section 3.2, and this is the
place where that instruction earns its keep.

**proposition 32**, [10] printed page 12, transcribed in
docs/part2/lit_review.md section 3.2:

> **Proposition 32.** If f : K ⊆ ℝⁿ → ℝ is such that its absolute value
> |f| : K ⊆ ℝⁿ → ℝ is Fréchet differentiable at x⁽⁰⁾ ∈ K with differential function
> D|f|(x⁽⁰⁾), then f is abs-differentiable at x⁽⁰⁾ with the same differential.
>
> In particular, **if f : K ⊆ ℝⁿ → ℝ⁺ ∪ {0} is differentiable then it is also
> abs-differentiable.**

**theorem 34**, [10] printed page 13:

> **Theorem 34.** The IV-function 𝙵 : K ⊆ ℝⁿ → I(ℝ), 𝙵(x) = (f̂(x); f̃(x)) is
> Fréchet gH-differentiable at a point x⁽⁰⁾ ∈ K, if and only if, f̂ and f̃ are
> (respectively) Fréchet differentiable and abs-differentiable at x⁽⁰⁾.

the check, per objective, with f̂ = c_i and f̃ = r_i as section 1.1 gives them:

    objective 1: c_1 = (3/20)x_1² + (1/5)x_2² is a polynomial, Fréchet
        differentiable everywhere. r_1 = (1/20)x_1² + (1/10)x_2² is a polynomial
        and is **non-negative** on ℝ², with r_1 = 0 exactly at the origin. by
        proposition 32's second sentence it is abs-differentiable everywhere,
        including at the origin.
    objective 2: c_2 and r_2 the same, with r_2 = 0 exactly at (5, 5).

so by theorem 34, **F is Fréchet gH-differentiable at every point of ℝ²**, and in
particular at every point of the box.

**this is not a formality on I-BK1 and it would have been on p1.** p1's radii were
bounded below by delta = 1/8 and a1 imposed strict positivity by design;
docs/part1/b1_phi_efficient_sets.md section 1.3 leans on that. **I-BK1's radii
vanish, and they vanish at (0, 0) and (5, 5), which sections 2.4 and 2.5 show are
points of all three derived sets** — they are the two corners the sets are pinned
at. under a1's strict-positivity rule the derivation would have had a hole at
exactly the two points that anchor its answer. proposition 32 covers non-negative
radii including their zeros and there is no hole. **that is the concrete payoff of
docs/part2/lit_review.md section 3.2, and it is the reason the reading was worth
doing before the derivation.**

independently of [10], the hypothesis example 3.9 actually states is
differentiability of Λ_i^T f and B_i^T f, v-15, and all twelve of those are degree-2
polynomials. that hypothesis is satisfied by inspection and does not depend on
[10] at all; [10] is what licenses calling F gH-differentiable, which is the
language [16] states its own problem in.

### 1.5 the hypotheses of example 3.9 and example 3.8, assembled

example 3.9's three statements, [1] printed page 10, transcribed in a0 c14 and
recorded as v-16; example 3.8's four, [1] printed page 10, a0 c13. hypothesis by
hypothesis, for I-BK1 under each of the three phi:

    Λ_i^T f, B_i^T f differentiable   yes, all four are degree-2 polynomials
    S convex                          yes, S is the box [−10, 10]²
    F phi-convex                      yes, theorem 3.3 and section 1.3

so all three statements of example 3.9 and all four of example 3.8 are available,
under all three phi. **that is the whole of the hypothesis check and none of it is
conditional.**

two readings this document commits to, both already on record and neither
resolved here, exactly as b1 committed to them.

**s-02**, example 3.9's weight phrase "w_i ⩾ 0 not equal zero for all i" in
statements 1 and 2. this document takes reading one, non-negative and not all
zero, which is CONTEXT.md section 6's commitment. section 5 below reports a second
witness against reading two, on a problem the project did not construct.

**the interiority reading.** condition (15) is unconstrained stationarity and
carries no constraint multipliers, so read literally statement 1 would be false at
a weak optimal point on a face of S. this project reads example 3.9 as an interior
condition, which is what docs/part1/a1_uncertainty_model.md part 3 states and what
b1 section 1.4 committed to. **on I-BK1 the reading costs nothing at all**, and
section 2.5 shows why: no point outside [0, 5]² is even weakly optimal under any
phi, by a direct domination argument that does not use example 3.9, so the faces
of the box are excluded without appeal to the reading.


## 2. the derivation

### 2.1 the system, and the one substitution that makes it readable

condition (15), [1] printed page 10, is stationarity of Σ_k w_k g_k, as b1
section 0 confirmed from the definitions of Λ_i and B_i and as a0 c14 records.
with every g_k a quadratic with constant hessian it is the linear system

    ( Σ_k w_k H_k ) x = − Σ_k w_k b_k                                        (b1-1)

and since every H_k is diagonal it splits into two scalar equations. the index
convention is example 3.8's, a0 c13: w_1 on Λ_1^T f, w_2 on B_1^T f, w_3 on
Λ_2^T f, w_4 on B_2^T f.

writing d_1, d_2 for the diagonal entries of Σ_k w_k H_k and ρ_1, ρ_2 for the
components of −Σ_k w_k b_k:

    phi_lu   d_1 = (1/5)w_1 + (2/5)w_2 + (1/5)w_3 + (3/5)w_4   ρ_1 = w_3 + 3w_4
             d_2 = (1/5)w_1 + (3/5)w_2 + (1/5)w_3 +      w_4   ρ_2 = w_3 + 5w_4

    phi_ls   d_1 = (1/5)w_1 + (1/5)w_2 + (1/5)w_3 + (2/5)w_4   ρ_1 = w_3 + 2w_4
             d_2 = (1/5)w_1 + (2/5)w_2 + (1/5)w_3 + (4/5)w_4   ρ_2 = w_3 + 4w_4

    phi_cw   d_1 = (3/10)w_1 + (1/10)w_2 + (2/5)w_3 + (1/5)w_4  ρ_1 = 2w_3 + w_4
             d_2 = (2/5)w_1  + (1/5)w_2  + (3/5)w_3 + (2/5)w_4  ρ_2 = 3w_3 + 2w_4

**the substitution.** each objective's two image coordinates are supported at the
same point — objective 1's at the origin, objective 2's at (5, 5) — so the two
scalar equations have the same shape. write, for a weight vector w,

    P_1 = Σ_{k ∈ obj 1} w_k κ_{k,1}      Q_1 = Σ_{k ∈ obj 2} w_k κ_{k,1}
    P_2 = Σ_{k ∈ obj 1} w_k κ_{k,2}      Q_2 = Σ_{k ∈ obj 2} w_k κ_{k,2}

where κ_{k,1} and κ_{k,2} are the coefficients of image coordinate k on its x_1
and x_2 terms. then (b1-1) reads x_1 (P_1 + Q_1) = 5 Q_1 and x_2 (P_2 + Q_2) =
5 Q_2, so

    x_1 = 5 Q_1 / (P_1 + Q_1)        x_2 = 5 Q_2 / (P_2 + Q_2)

and in the coordinates

    **U := x_1 / (5 − x_1)      V := x_2 / (5 − x_2)**

which map [0, 5) bijectively and increasingly onto [0, ∞), the system becomes
simply

    **U = Q_1 / P_1        V = Q_2 / P_2**

that is the substitution the whole of the rest of the document runs on. it is not
a change of problem: U and V are an explicit monotone reparameterisation of the
box's relevant quadrant, and every statement below is translated back at the end
of section 2.4.

### 2.2 the map x(w), in closed form

wherever P_1 + Q_1 and P_2 + Q_2 are non-zero, which for w ⩾ 0 not all zero is
always, section 2.3, the system has the unique solution

    phi_lu   x_1(w) = 5(w_3 + 3w_4) / (w_1 + 2w_2 + w_3 + 3w_4)
             x_2(w) = 5(w_3 + 5w_4) / (w_1 + 3w_2 + w_3 + 5w_4)

    phi_ls   x_1(w) = 5(w_3 + 2w_4) / (w_1 +  w_2 + w_3 + 2w_4)
             x_2(w) = 5(w_3 + 4w_4) / (w_1 + 2w_2 + w_3 + 4w_4)

    phi_cw   x_1(w) = 5(4w_3 + 2w_4) / (3w_1 + w_2 + 4w_3 + 2w_4)
             x_2(w) = 5(3w_3 + 2w_4) / (2w_1 + w_2 + 3w_3 + 2w_4)

that is the deliverable s-08 asks for, in the same form b1 section 2.2 produced it
for p1. (15) is homogeneous of degree one in w, so x(w) depends on the ray through
w and not on its length; example 3.8's standing condition normalises the weights
to sum to one and example 3.9 does not, a0 c14, and the normalisation is stated
wherever it matters.

verified in exact rational arithmetic by substituting x(w) back into the gradient
of Σ_k w_k g_k and checking it is the zero vector, on 4000 random non-negative
integer weight vectors per phi:

    phi_lu: 4000 weights, 0 singular, max |gradient at x(w)| = 0
    phi_ls: 4000 weights, 0 singular, max |gradient at x(w)| = 0
    phi_cw: 4000 weights, 0 singular, max |gradient at x(w)| = 0

exactly zero, not approximately: the arithmetic was rational throughout.

### 2.3 the singular weight directions, characterised

Σ_k w_k H_k fails to be invertible exactly when d_1(w) = 0 or d_2(w) = 0. **every
diagonal entry of every H_k is strictly positive**, section 1.2, so for w ⩾ 0 with
w ≠ 0 both d_1 and d_2 are strictly positive. enumerating the fifteen non-empty
supports of w confirms it:

    phi_lu: 0 of the 15 non-empty supports give a singular matrix
    phi_ls: 0 of the 15 non-empty supports give a singular matrix
    phi_cw: 0 of the 15 non-empty supports give a singular matrix

**there are no singular weight directions on I-BK1, under any of the three phi.**
this is stated as a result and not as an absence, because it is the structural
difference from p1 and it is what makes section 2.6's closure exact. on p1, φ_ls
and φ_cw each had two singular rays, the weight vectors putting all their mass on
a single width coordinate, and each produced a line of solutions rather than a
point; docs/part1/b1_phi_efficient_sets.md section 2.6 and
docs/part1/part1_closing.md section 5.1 record that the published conditions give
no optimality verdict on those two segments, and s-12 prices them. **I-BK1 has no
such segment.** the reason is exactly the one section 1.2 gives: p1's r_1 depended
on x_2 alone, while I-BK1's r_1 depends on both variables with strictly positive
coefficients, because [16] put a non-degenerate interval on both terms of both
objectives.

so nothing is excluded silently here, because there is nothing to exclude.

### 2.4 the derived sets, in closed form

by section 2.1 the whole answer is the reachable set of the pair (U, V) =
(Q_1/P_1, Q_2/P_2). define, for each image coordinate k, its **aspect ratio**

    a_k := κ_{k,2} / κ_{k,1}

the ratio of its x_2 coefficient to its x_1 coefficient. the twelve read off
section 1.2:

    objective 1     G̲_1  1      Ḡ_1  3/2     c_1  4/3     r_1  2     2r_1  2
    objective 2     G̲_2  1      Ḡ_2  5/3     c_2  3/2     r_2  2     2r_2  2

then P_2/P_1 is a convex-combination-like ratio of objective 1's two aspect
ratios and sweeps the closed interval between them as (w_1, w_2) sweeps the
non-negative quadrant, and Q_2/Q_1 does the same for objective 2. since

    V / U  =  (Q_2/P_2) / (Q_1/P_1)  =  (Q_2/Q_1) / (P_2/P_1)

and the two ratios are controlled by disjoint pairs of weights and are therefore
independent, the reachable set of V/U is the closed interval

    [ min(objective 2's aspect ratios) / max(objective 1's aspect ratios),
      max(objective 2's aspect ratios) / min(objective 1's aspect ratios) ]

and U itself is free in [0, ∞] independently, by scaling the objective-2 weights
against the objective-1 weights. so each derived set is a **wedge** in the (U, V)
plane, and writing ν := V/U:

    phi_lu   objective 1 exposes {1, 3/2}, objective 2 exposes {1, 5/3}
             **ν ∈ [ 2/3 , 5/3 ]**
    phi_ls   objective 1 exposes {1, 2},   objective 2 exposes {1, 2}
             **ν ∈ [ 1/2 , 2 ]**
    phi_cw   objective 1 exposes {4/3, 2}, objective 2 exposes {3/2, 2}
             **ν ∈ [ 3/4 , 3/2 ]**

translated back to the decision variables, with U = x_1/(5−x_1) and
V = x_2/(5−x_2), and cleared of denominators so that the two corner points are
covered without a case split:

    **X_lu = { x ∈ [0,5]² :  2 x_1(5−x_2) ⩽ 3 x_2(5−x_1) ⩽ 5 x_1(5−x_2) }**

    **X_ls = { x ∈ [0,5]² :    x_1(5−x_2) ⩽ 2 x_2(5−x_1) ⩽ 4 x_1(5−x_2) }**

    **X_cw = { x ∈ [0,5]² :  3 x_1(5−x_2) ⩽ 4 x_2(5−x_1) ⩽ 6 x_1(5−x_2) }**

each is the region between two curves of constant ν, and the curve ν = c is the
hyperbola

    x_2  =  5 c x_1 / ( 5 + (c − 1) x_1 )

running from (0, 0) to (5, 5) for every c > 0, with c = 1 giving the diagonal
x_2 = x_1. so all three sets are pinned at the same two corners, **(0, 0), where
r_1 vanishes, and (5, 5), where r_2 vanishes** — the two points section 1.4's
appeal to proposition 32 was needed for. the corner (0, 0) is reached at
w_3 = w_4 = 0 and (5, 5) at w_1 = w_2 = 0, and those are the only weights reaching
them: x_1 = 0 forces Q_1 = 0 forces w_3 = w_4 = 0, which forces Q_2 = 0 and
x_2 = 0, so **the two corners are the only points of any derived set on the axes
x_1 = 0 and x_1 = 5.**

verification of these three descriptions, both directions, in exact rational
arithmetic. forward, the 4000 random non-negative integer weight vectors per phi
of section 2.2:

    phi_lu: 0 of 4000 images x(w) outside the stated region
    phi_ls: 0 of 4000 images x(w) outside the stated region
    phi_cw: 0 of 4000 images x(w) outside the stated region

converse, inverting the parameterisation exactly at 400 random rational points of
each stated region, constructed from a random ν in the band and a random U:

    phi_lu: 400 region points, 400 with an exact non-negative witness weight, 0 without
    phi_ls: 400 region points, 400 with an exact non-negative witness weight, 0 without
    phi_cw: 400 region points, 400 with an exact non-negative witness weight, 0 without

each witness w was checked to be non-negative and to satisfy x(w) = x exactly, not
approximately.

### 2.5 interiority

condition (15) is unconstrained stationarity and carries no constraint
multipliers, so a candidate on a face of the box would be outside example 3.9's
scope, per section 1.5.

all three derived sets are contained in [0, 5]². the box is [−10, 10]², so **every
point of all three derived sets is strictly interior to the box, with a margin of
at least 5 on every side.** no candidate lies on or near a face and example 3.9
applies to all of them. unlike p1, where the margin was 1/6 and was obtained by
a1's choice of box and of rho, the margin here is a property of the published
problem.

**and the interiority reading is not load-bearing on I-BK1, which it was on p1.**
every one of the twelve image coordinates is a positive combination of x_1²,
x_2², (x_1−5)² and (x_2−5)², and each of those four is strictly decreased by
clipping the offending coordinate into [0, 5]. so any x outside [0, 5]² is
strictly dominated in all four image coordinates by its projection onto [0, 5]²,
under every phi, and is therefore not weakly optimal — by definition 3.1(3)
directly, with no appeal to example 3.9 at all. checked on 20000 random rational
points outside [0, 5]²:

    20000 points outside [0,5]^2: 0 not dominated by their projection onto it

so the faces of S are excluded by domination and the necessity direction of
section 2.6 needs the reading only on the interior, where example 3.9 is
uncontroversial. **b1 section 2.5's caveat does not recur here.**

### 2.6 optimal against weakly optimal, and the sandwich

**every x(w) with w on the simplex is an optimal solution.** the route is
**example 3.8 statement 3**, [1] printed page 10:

> 3. If x̄ ∈ S is the only optimal solution for (MOP_φ(w)), then x̄ ∈ S is an
>    optimal solution for (1MIOP_φ).

the scalarised objective Σ_k w_k g_k is a quadratic whose hessian Σ_k w_k H_k is
positive definite for every w ⩾ 0 with w ≠ 0, section 2.3, so it is strictly
convex; x(w) is its stationary point and therefore its unique global minimiser
over ℝ², and since x(w) is interior to the box it is the unique minimiser over S
as well. the hypothesis of statement 3 is exactly uniqueness, with no positivity
required of the weights and no convexity of F required. **so every point of every
derived set is an optimal solution, including at weight vectors with zero
components.**

**example 3.9 statement 3** is available as well and agrees where it applies: for
w with every component strictly positive, S convex and F phi-convex both hold and
(15) holds at x(w) by construction. it is used here only as a cross-check, since
3.8 statement 3 covers those weights and more.

**the necessity direction is example 3.9 statement 1**, [1] printed page 10:

> 1. If x̄ ∈ S is a weak optimal solution for (1MIOP_φ), then there are
>    w_1, …, w_2m ∈ ℝ, with w_i ⩾ 0 not equal zero for all i ∈ {1, …, 2m}, such
>    that (15).

its only hypothesis is differentiability of the image coordinates, which holds
everywhere, section 1.5. so for x̄ interior to the box — and section 2.5 disposes
of the rest of S by domination —

    x̄ weakly optimal ⇒ (15) holds at x̄ for some w ⩾ 0, w ≠ 0 ⇒ x̄ ∈ X_phi

there being no singular weight and hence no line of solutions to escape into.
combining with the sufficiency direction and with definition 3.1's implication
chain, a0 c10:

    **X_phi ⊆ optimal set ⊆ weak optimal set ⊆ X_phi**

so all three coincide:

    **under all three phi, the optimal set and the weak optimal set both equal
    X_phi exactly.**

that is stronger than b1 obtained on p1, where the collapse held for phi_lu only
and phi_ls and phi_cw carried two singular segments each on which the published
conditions give weak optimality and no optimality verdict. **on I-BK1 the
derivation closes without reservation under all three phi**, and it does so using
published results as they stand, with nothing patched and no condition added.


## 3. criterion 3, answered exactly

docs/part1/part1_closing.md section 7.2, criterion 3: "the three phi must give
distinct non-trivial sets, none equal to the crisp set and none the whole box —
checked near the efficient set and never on a uniform sample of the box".
docs/part2/lit_review.md section 7.2 movement two decided that on a problem whose
efficient sets are derivable the derivation answers this exactly rather than by
sample. it does.

### 3.1 the three sets are distinct, and strictly nested

the bands are ν ∈ [3/4, 3/2] for phi_cw, [2/3, 5/3] for phi_lu and [1/2, 2] for
phi_ls, and the six endpoints are in strict order

    1/2  <  2/3  <  3/4  <  3/2  <  5/3  <  2

so, **as sets and exactly**,

    **X_cw ⊊ X_lu ⊊ X_ls**

all three inclusions strict, with no reliance on a sample, a grid or a tolerance.

the Lebesgue measures have closed forms. parameterising by (U, ν) and integrating
the Jacobian 25U / ((1+U)²(1+νU)²) gives |X_φ| = 25 [ I(L) − I(R) ] with
I(c) = c ln c/(c−1)² + 1/(1−c), so

    |X_lu| = 25 [ 9/2 − 6 ln(3/2) − (15/4) ln(5/3) ] = 3.790332
    |X_ls| = 25 [ 3 − 4 ln 2 ]                       = 5.685282
    |X_cw| = 25 [ 6 − 12 ln(4/3) − 6 ln(3/2) ]       = 2.875612

cross-checked against direct two-dimensional quadrature over [0, 5]² at 6000 × 6000
midpoints: 3.790365, 5.685313, 2.875622, agreeing to five significant figures,
which is the quadrature's own accuracy on a curved boundary.

the sets being nested, every pairwise intersection is the smaller and every union
the larger, so the overlap fractions are ratios of the three numbers above:

    pair        |A ∩ B| / |A ∪ B|
    lu, ls      0.666692
    cw, lu      0.758670
    cw, ls      0.505799

**the separation is real and it is substantial**: phi_ls's set is half again as
large as phi_lu's and twice phi_cw's. it is also **weaker in kind than p1's**,
where docs/part1/b1_phi_efficient_sets.md section 5 found phi_lu and phi_cw nested
in neither direction, crossing with 42.6 per cent of one inside the other. that
difference is reported in 3.2 rather than buried.

### 3.2 which of the three relations the containment criterion predicts

docs/part1/a_close_containment.md proves, from the criterion that φ_B = M φ_A with
M entrywise non-negative and invertible makes φ_A-dominance imply φ_B-dominance,
that **ND_lu ⊆ ND_ls and ND_cw ⊆ ND_ls, exactly and for every problem**. as in b1
section 5, that result was not used anywhere in the derivation and is applied here
only as an independent test.

    X_lu ⊊ X_ls    **predicted.** a check on the derivation, not a finding.
    X_cw ⊊ X_ls    **predicted.** a check on the derivation, not a finding.
    X_cw ⊊ X_lu    **not predicted.** the criterion gives nothing for this pair in
                   either direction, docs/part1/b1_phi_efficient_sets.md section 5,
                   and on p1 the two genuinely crossed. **this one is a finding
                   about I-BK1.**

both predicted containments hold on the derived closed forms, which is a second
independent confirmation of docs/part1/a_close_containment.md's corollaries, on a
problem the project did not construct. **and the third relation is the informative
one**, exactly as docs/part1/part1_closing.md section 4.1 records the phi_lu
against phi_cw pair being the informative one on p1 — except that here the pair
does not cross but nests, which is a different answer from p1's and is the thing
this problem says that p1 could not.

### 3.3 none of the three is a crisp set, and none is the box

a real two-objective problem built from one image coordinate per interval
objective has, by the same computation, a Pareto set that is a **single curve** of
constant ν. the natural crisp comparators:

    comparator                        ν        in X_lu   in X_ls   in X_cw
    the centres (c_1, c_2)            9/8      yes       yes       yes
    the lower ends (G̲_1, G̲_2)        1        yes       yes       yes
    the upper ends (Ḡ_1, Ḡ_2)        10/9     yes       yes       yes
    the half-widths (r_1, r_2)        1        yes       yes       yes

every one is one-dimensional and every one of the three X_phi is two-dimensional,
so **no derived set equals a crisp set**, and the containment runs the only way it
can. and X_ls ⊆ [0, 5]² has area 5.685 against the box's 400, so **no derived set
is the whole box**, by a factor of seventy.

**criterion 3 passes on I-BK1, exactly.** with it, all five criteria of
docs/part1/part1_closing.md section 7.2 are settled for I-BK1: criteria 1, 2, 4
and 5 by docs/part2/lit_review.md section 1.9, criterion 3 here. **I-BK1 passes the
gate.** what that licenses is stated in section 7 and it is deliberately less than
clause c5.


## 4. the external checks

this is why I-BK1 was chosen over the four cleaner candidates, and it is the first
external check the project has ever had on a derivation.
docs/part2/lit_review.md section 1.4 establishes that [16]'s own order relation,
its definition 2.2 on printed page 4, is example 2.2 of [1] and therefore φ_lu, so
its published points are φ_lu points.

### 4.1 checkpoint two: equation (25)'s curve. passes

[16] printed pages 20-21. the paper scalarises I-BK1 by weighted sum, equation
(23), then by Bhurjee and Panda's parametric method with weight function
w(t_1,t_2,t_3,t_4) := t_2 + t_3, giving equation (24) and its solution (25):

>     (25)  x_1 := 2.1667α / (0.3 + 0.13334α)   and
>           x_2 := 3α / (0.43334 + 0.16666α),   α ∈ [0,1]

docs/part2/lit_review.md section 1.6 re-derived (24)'s four coefficients as the
w-weighted means of the interval-coefficient parameters, and this session repeated
that derivation in exact rationals: they are

    a = 3/20 on x_1²,  b = 13/60 on x_2²,  b = 13/60 on (x_1−5)²,  c = 3/10 on (x_2−5)²

the printed 0.15, 0.21667, 0.21667, 0.3 being 13/60 = 0.216666… rounded. setting
the gradient of (24) to zero gives x_1 = 5bα/(a(1−α) + bα) and
x_2 = 5cα/(b(1−α) + cα), which is (25) as printed.

**in the coordinates of section 2.1 the curve collapses to a point.**
U = x_1/(5−x_1) = (b/a)·α/(1−α) and V = (c/b)·α/(1−α), so

    **ν = V/U = a c / b² = (3/20)(3/10) / (13/60)² = 162/169 = 0.958580,
    constant along the whole of (25).**

so equation (25) is exactly a curve of constant ν, the same kind of object as the
crisp comparators of section 3.3, and the check is one comparison of a rational
number against three intervals:

    phi_lu   band [2/3, 5/3]   162/169 inside: **yes**
    phi_ls   band [1/2, 2]     162/169 inside: **yes**
    phi_cw   band [3/4, 3/2]   162/169 inside: **yes**

**the published curve lies inside all three derived sets, and strictly inside**:
162/169 = 0.9586 sits well away from the nearest band endpoint, 3/4. verified
exactly at α = 0.1, …, 0.9, with α = 0 giving the corner (0, 0) and α = 1 the
corner (5, 5), both of which are in all three sets by section 2.4.

Table 2's eleven published points were checked individually against (25) and
against the three bands. **eight of the eleven — α = 0.1 to 0.7 and α = 0.9 —
reproduce ν = 0.958551 to six decimals**, the residual being the paper's rounding
of 13/60 to 0.21667 in the printed formula, and all eight lie in all three sets.
two more are α = 0 and α = 1, the corners (0, 0) and (5, 5), which are in all
three sets by section 2.4. **the eleventh, α = 0.8, does not, and it is a printing
error, reported in 4.4.**

**this is the check that matters and it passes.** it is a one-parameter family of
published points, not a single point, and it lands inside the derived φ_lu set
along its whole length.

### 4.2 checkpoint one: Table 1's x⋆. fails, and the failure is in the paper

[16] Table 1, printed page 20, last row, k = 12:

    x⋆ = (3.914930, 1.428474)
    G(x⋆) = ([1.736722, 3.677497], [1.393317, 6.731112])
    ξ(x⋆) = −2.8154e−07

recomputing G(x⋆) from the problem statement at the printed x⋆ gives
([1.736721, 3.677497], [1.393317, 6.731112]), agreeing with the paper to the last
printed digit and confirming once more that the boundary-function reading of
section 1.1 is the paper's.

**x⋆ is outside all three derived sets.**

    ν(x⋆) = x_2(5−x_1) / (x_1(5−x_2)) = 0.110854

against band lower ends 2/3, 1/2 and 3/4. it is not marginally outside: it is
below phi_ls's lower end by a factor of four and a half.

**the stopping rule the brief states is that a published φ_lu point outside the
derived φ_lu set means the derivation is wrong. the premise fails, and it fails to
an argument that does not use the derivation at all.**

x⋆ is published as a **Pareto optimal point** of I-BK1, [16] printed page 21.
[16]'s definition 2.17, printed page 7, is

> **Definition 2.17 (Pareto optimal point [27]).** An x⋆ ∈ U is said to be a
> Pareto optimal point of the MIOP (1) if there does not exist any other x ∈ U
> such that G_i(x) ⪯ G_i(x⋆) for all i = 1, 2, …, m.

and ⪯ is definition 2.2, printed page 4, componentwise ⩽ on the endpoint pair. so
x⋆ is Pareto optimal exactly when no other feasible point has all four endpoint
values ⩽ its own. **there is such a point.** take

    y = (2.897500, 2.397500)

which is in the box, and compare, in exact rational arithmetic, against the
paper's own printed G(x⋆):

    coordinate    G(y)         G(x⋆)        margin      strictly smaller
    G_1 lower     1.414351     1.736721     +0.322370   yes
    G_1 upper     3.403503     3.677497     +0.273994   yes
    G_2 lower     1.119351     1.393317     +0.273966   yes
    G_2 upper     4.712655     6.731112     +2.018457   yes

**all four strictly smaller**, so G_i(y) ≺ G_i(x⋆) for i = 1, 2 and x⋆ is not a
Pareto optimal point of I-BK1 in [16]'s own definition 2.17. it is not weakly
Pareto optimal in [16]'s definition 2.16 either, that definition forbidding an x
strict in every objective, which y is.

**the verdict is not an artefact of the printed rounding.** the tightest of the
four margins is 0.273966, and perturbing x⋆ by 10⁻⁶ in each coordinate moves any
endpoint value by at most about 4 × 10⁻⁶, five orders of magnitude smaller. y was
found by exhaustive search over a grid of [0, 5]² and reported as the widest-margin
dominator; the four inequalities above are checkable by hand against the paper's
printed row.

**so x⋆ is not a φ_lu point, the rule's premise is false, and the disagreement is
located in [16].** section 4.3 says where.

**and this closes docs/part2/lit_review.md's ambiguity a-4 in the direction the
reading did not expect.** a-4 records that the paper's printed argument for x⋆'s
Pareto optimality — mutual non-domination with Table 2's eleven points — is
invalid, and records that **proposition 2.1, printed page 7, supplies the
conclusion independently**, so that "the checkpoint stands on proposition 2.1".
it does not. the conclusion is false, so no valid argument supplies it, and
section 4.3 shows what goes wrong with proposition 2.1 on this problem.

### 4.3 the mechanism: [16]'s Pareto critical set is much larger than the efficient set

this section is not required by the brief. it is included because a failed external
check that is not explained is indistinguishable from a failed derivation, and
because the explanation is checkable.

**definition 2.18**, [16] printed page 7:

> **Definition 2.18 (Pareto critical point [27]).** A point x⋆ ∈ U is said to be
> Pareto critical point of the MIOP (1) if there does not exist any v ∈ ℝⁿ such
> that ∇_gH G_i(x⋆)^⊤ ⊙ v ≺ 0 for all i = 1, 2, …, m.

with, from printed page 6, ∇_gH H(x̃)^⊤ ⊙ v := ⊕_{j=1}^{n} D_j H(x̃) ⊙ v_j, a
Minkowski sum of Moore products.

**the structural point.** the interval ⊕_j D_j G_i ⊙ v_j has

    upper endpoint = Σ_j max( ∂G̲_i/∂x_j · v_j ,  ∂Ḡ_i/∂x_j · v_j )
                   ⩾ max( ∇G̲_i^T v ,  ∇Ḡ_i^T v )

with the inequality strict whenever the two boundary gradients disagree in sign
pattern across the coordinates. that is the ordinary dependency effect of interval
arithmetic: summing termwise loses the correlation between the coordinates.
requiring the interval to be ≺ 0 is therefore **strictly stronger** than requiring
both boundary functions to descend, so **a direction can lower all 2m image
coordinates without being a descent direction in definition 2.19's sense**, and
consequently

    a point with no genuine 2m-descent direction is Pareto critical,
    **but a Pareto critical point need not have no 2m-descent direction.**

for I-BK1 the critical set can be written down. for x in (0, 5)² the only
candidate directions are the mixed-sign ones, and working the two cases out gives:
a direction v = (−1, b) with b > 0 makes both intervals ≺ 0 exactly when
3(5−x_1)/(5−x_2) ⩽ b ⩽ x_1/(3x_2), which is non-empty exactly when
9x_2(5−x_1) ⩽ x_1(5−x_2); and v = (1, −b) exactly when 10x_1(5−x_2) ⩽ x_2(5−x_1).
in the coordinate ν of section 2.4 those two read ν ⩽ 1/9 and ν ⩾ 10. so

    **[16]'s Pareto critical set for I-BK1 is exactly ν ∈ (1/9, 10).**

this closed form was checked against a brute-force scan of directions — the
interval ∇_gH G_i^T ⊙ v computed from the paper's own printed gH-gradients and
tested for ≺ 0 under definition 2.2(ii) — at twelve points spread across the
quadrant, including x⋆ itself and points on both sides of both boundaries:

    12 test points, closed form against a 60000-direction scan: 0 disagreements

the sizes, in Lebesgue measure over [0, 5]²:

    X_cw                                    ν ∈ [3/4, 3/2]    2.8756
    X_lu                                    ν ∈ [2/3, 5/3]    3.7903
    X_ls                                    ν ∈ [1/2, 2]      5.6853
    [16]'s Pareto critical set, def. 2.18   ν ∈ (1/9, 10)    16.0714

**the critical set is 4.24 times X_lu and strictly contains all three derived
sets.** that is the whole explanation of the failed checkpoint: Algorithm 1
converges to a Pareto critical point, and on this problem the Pareto critical set
is four times the efficient set, so convergence does not deliver optimality.

**x⋆ itself is not even Pareto critical.** at x⋆, 9x_2(5−x_1) = 13.949949 against
x_1(5−x_2) = 13.982274, so a descent direction exists, in the narrow cone
b ∈ (0.911434, 0.913546); ν(x⋆) = 0.110854 sits just below 1/9 = 0.111111. that is
consistent with the paper's own ξ(x⋆) = −2.8154e−07 against its tolerance
ε = 10⁻⁶: **x⋆ is the algorithm's output at tolerance, approaching the boundary
ν = 1/9 of the critical set from outside.** the criticality curve at x⋆'s first
coordinate passes through x_2 = 1.430837, against x⋆'s 1.428474.

**consequences for two published statements, reported and not softened.**

**proposition 2.1**, [16] printed page 7:

> **Proposition 2.1.** If U is convex, G ∈ C²_gH(U, I(ℝ)^m), ∇²_gH G_i(x) ≻ 0 for
> all i = 1, 2, …, m and all x ∈ U, and if x⋆ ∈ U is a Pareto critical point of
> the MIOP (1), then x⋆ is a Pareto optimal point of the MIOP (1).

take x = (5/2, 5/6), for which ν = 1/5, strictly inside (1/9, 10). the hypotheses:

    U convex                                     yes, the open box
    G ∈ C²_gH                                    yes, the boundary functions are
                                                 polynomials and section 1.4 gives
                                                 gH-differentiability everywhere
    ∇²_gH G_i(x) ≻ 0 for all i and all x         yes. the interval Hessian entries
                                                 the paper prints on page 18 are
                                                 [0.2,0.4], [0.2,0.6], [0.2,0.6]
                                                 and [0.2,1], so v^T ⊙ ∇²_gH G_i ⊙ v
                                                 has both endpoints strictly
                                                 positive for every v ≠ 0
    x is a Pareto critical point                 yes; a scan of 200000 directions
                                                 found none with both intervals ≺ 0

conclusion asserted: x is Pareto optimal. but x is dominated in all four endpoint
coordinates by y = (1.886667, 1.440000), with a minimum margin of 0.124351:

    G(x) = ([0.694444, 1.458333], [2.361111, 10.555556])
    G(y) = ([0.563311, 1.333982], [2.236644,  9.244653])

**so proposition 2.1 is false as printed, and [16]'s own first test problem is a
counterexample.**

**lemma 2.4(ii)**, [16] printed page 7, attributed to [27]:

> (ii) If U is convex, G is I(ℝ)^m convex, and x⋆ ∈ U is a Pareto critical point of
>      the MIOP (1), then x⋆ is a weakly Pareto optimal point of the MIOP (1).

the same point refutes this too. I(ℝ)^m convexity is definition 2.14, printed page
6, which under definition 2.2's componentwise ⪯ is exactly convexity of the four
boundary functions; all four are positive definite quadratics, so it holds, and
the paper asserts the same on printed page 7 — "Under this assumption, G is
I(ℝ)^m convex on each convex subset of U". checked directly on 200000 random
chords, 0 violations of definition 2.14. and x = (5/2, 5/6) is not weakly Pareto
optimal in definition 2.16's sense, y being strictly better in both objectives.
**proposition 2.1's proof is given as "similar to the proof of item (ii) of Lemma
2.4", printed page 7, so the two failures are one failure**, and it is inherited
from [16]'s reference [27], Mondal and Ghosh 2025, rather than original to [16].

**what this session does and does not claim.** it claims exactly what it checked:
these two printed statements have a counterexample in I-BK1, verified in exact
rational arithmetic against the paper's own printed gradients, Hessians and
objective values. it does **not** claim to have found the error in a proof it has
not read — [27] is not on disk and lemma 2.4's proof is not in [16] — nor that the
Newton method is wrong, nor anything about [16]'s other nineteen problems.
**recorded as ambiguity a-11 in section 6 and carried to the research chat.**

### 4.4 Table 2's α = 0.8 row is a printing error

the row reads x = (4.262305, 4.628566). equation (25) at α = 0.8 gives
(4.262295, 4.235294): the first coordinate matches, **the second does not, and the
printed value 4.628566 is the α = 0.9 row's second coordinate repeated.** the row's
G(x) values are internally consistent with the printed (wrong) x_2, so the whole
row was computed from it.

that point has ν = 2.156737, outside all three bands, and the derivation therefore
says it is not weakly optimal under any phi. **it is reported as a printed error
and not as a failed check**: the point is not on the curve the paper's own formula
(25) defines, so it is not a published φ_lu point in the sense the check needs.
recorded as ambiguity a-12.


## 5. a second witness on s-02, on a problem the project did not construct

s-02 asks whether example 3.9's "w_i ⩾ 0 not equal zero for all i" in statements 1
and 2 means non-negative and not all zero, reading one, or strictly positive,
reading two. docs/part1/b1_phi_efficient_sets.md section 6 offers a witness on p1
against reading two. **I-BK1 supplies a second, and it is structural rather than
pointwise.**

take phi_lu and any point on the upper boundary ray ν = 5/3. by section 2.4 that
requires Q_2/Q_1 = 5/3, which forces w_3 = 0, and P_2/P_1 = 1, which forces
w_2 = 0. so **every weight vector reaching that ray has two zero components**, and
no strictly positive w reaches it: with w_3 > 0 the ratio Q_2/Q_1 is strictly below
5/3, and with w_2 > 0 the ratio P_2/P_1 is strictly above 1. meanwhile every such
point is the unique global minimiser of w_1 g_1 + w_4 g_4, a strictly convex
quadratic, so **example 3.8 statement 3 makes it an optimal solution**, hence a
weak optimal solution by definition 3.1's implication chain.

under reading two, example 3.9 statement 1 would assert a strictly positive w
satisfying (15) at such a point, and there is none. **reading two therefore makes
statement 1 false along a whole boundary curve of the derived set**, and reading
one is the one under which the published statement holds. the same argument
applies to phi_lu's lower ray ν = 2/3 and to all four boundary rays of phi_ls and
phi_cw.

this is evidence and not a resolution: s-02 is a question for the authors about
their own sentence, and it stays open. **nothing in sections 2, 3 or 4 depends on
the answer**, every optimality conclusion above being drawn from example 3.8,
whose weight condition is unambiguous. what reading two would cost is the
necessity direction of section 2.6, which would then leave the derived sets proved
contained in the efficient set but not proved to exhaust it, and would leave the
four boundary rays as the gap.


## 6. open items this session raises or touches

    **a-11, new. [16]'s proposition 2.1 and lemma 2.4(ii) are false as printed,
        with I-BK1 as a counterexample.** section 4.3, verified in exact rational
        arithmetic against the paper's own printed gradients and Hessians. lemma
        2.4 is attributed to [16]'s reference [27], Mondal and Ghosh 2025, which is
        not on disk, so this session cannot say where the proof goes wrong.
        **the memoria must not cite either statement**, and
        docs/part2/lit_review.md a-4's remark that "the checkpoint stands on
        proposition 2.1" must be withdrawn.

    **a-12, new. [16]'s Table 2, row α = 0.8, has the α = 0.9 row's second
        coordinate.** section 4.4. equation (25) gives x_2 = 4.235294 and the row
        prints 4.628566. the row's objective values were computed from the printed
        value, so the error is in x_2 and propagates. it does not affect the
        α = 0.8 point's status as a feasible point, only its status as a point of
        the curve (25) defines.

    **a-4, from docs/part2/lit_review.md. resolved in the negative.** the printed
        argument for x⋆'s Pareto optimality is invalid, as a-4 says, **and the
        conclusion is false**, section 4.2. a-4's rescue through proposition 2.1
        does not survive a-11.

    s-02, example 3.9's weight phrase. **evidence added**, section 5, on a problem
        the project did not construct and along a whole boundary curve rather than
        at a point. the row stays open and now carries two witnesses.

    s-08, whether b1 produces a map. **answered again as expected**: section 2.2 is
        the map, section 2.4 the region, no bounding box needed.

    s-11, the containment. untouched and not used. section 3.2 tested the derived
        forms against docs/part1/a_close_containment.md's corollaries as an
        independent check and they agree; that is a check on this derivation, not
        evidence for the containment, and nothing here is built on it.

    s-12, the singular segments. **does not arise on I-BK1**, section 2.3. the row
        is p1's and stays open on p1's terms; I-BK1 has no singular weight under
        any phi, so the gap b1 could not close does not recur here.

    p-05. **closed in lit-review and used here for the first time.** section 1.4
        applies [10] proposition 32, printed page 12, to radii that vanish at (0,0)
        and (5,5), which are points of all three derived sets. under a1's
        strict-positivity rule the derivation would have had a hole at exactly the
        two points that anchor its answer.

    r-09, the working rule that a new problem runs the full diagnostic before use.
        **discharged for I-BK1 by derivation rather than by diagnostic**, which is
        the reversal docs/part2/lit_review.md section 7.2 argued for and the human
        accepted. the derivation answers criterion 3 exactly, section 3, so no
        sample-based separation check is owed on this problem.

    **the one thing this session cannot check.** the derivation has been verified
        against the algebra, against [16]'s published curve (25), and against
        [16]'s own printed objective values at x⋆. it has **not** been verified
        against an independent implementation, because the brief forbids a module
        and a run. the checks section 2.2 and 2.4 report are self-consistency
        checks of the closed form; the check of section 4.1 is external and is the
        one that carries weight.

no source read in this session refutes anything in CONTEXT.md, so CONTEXT.md is
unchanged.


## 7. summary, and what f3 takes from this

    problem  phi   convexity  regularity          x(w)      singular w  interior  closes
    I-BK1    lu    yes, p.d.  yes, prop. 32       sec. 2.2  none        yes       yes, fully
    I-BK1    ls    yes, p.d.  yes, prop. 32       sec. 2.2  none        yes       yes, fully
    I-BK1    cw    yes, p.d.  yes, prop. 32       sec. 2.2  none        yes       yes, fully

**the derivation closes under all three phi with no reservation**, which p1 did
under one of three. the route was b1's throughout: image coordinates written out,
phi-convexity by theorem 3.3 of [1] printed page 9, regularity by [10] proposition
32 printed page 12 then theorem 34 printed page 13, condition (15) of example 3.9
of [1] printed page 10 for the candidate set, and example 3.8 statement 3 printed
page 10 to lift to optimality. **nothing was patched and no condition was added.**

what f3 takes:

    the map x(w), section 2.2, for all three phi. a closed-form rational function
        of the weight vector, no root-finding.
    the closed-form regions X_lu, X_ls and X_cw, section 2.4, as three pairs of
        polynomial inequalities, for sampling directly and for testing membership.
        each is a wedge between two hyperbolas through (0,0) and (5,5), so a
        reference set can be generated by sweeping ν across the band and U along
        it, with the Jacobian of section 3.1 available if a uniform sample in the
        decision space is wanted.
    the witnessing weights: section 2.4's converse construction returns, for any
        point of any region, an exact non-negative w producing it.
    **no singular weight set to exclude**, section 2.3, so f3's weight sample needs
        no special handling and b1's caveat about structured lattices does not
        apply here.
    the exact areas and overlap fractions, section 3.1, which are the second
        calibration point docs/part1/part1_closing.md section 7.3 asks for, in the
        Lebesgue-measure form `exact_regions_p1.csv` carries for p1.
    the published curve (25) as an implementation check, section 4.1: any encoding
        of X_lu must contain ν = 162/169 along its whole length.
    **and not Table 1's x⋆**, which section 4.2 shows is not a point of any of the
        three sets and must not be used as a fixture.

**what this does not license.** clause c5 of docs/part1/part1_closing.md section
7.1 stays marked unsupported. criterion 3 is answered and I-BK1 passes the gate,
which is what lit_review section 7.2 said would follow, but the claim c5 states is
about measured behaviour under the project's own instrument and that measurement
is f3's, not this session's. **no slice fraction, no benchmark number and no
ranking of the three phi appears anywhere above.** the three sets are reported as
nested, with the measures beside them, and which of the three an application should
prefer is not a question this document asks.

one further thing the memoria gains, and it is a negative: **on I-BK1 the three
orders are totally ordered by inclusion**, where on p1 phi_lu and phi_cw crossed.
that is a second geometry rather than a confirmation of the first, and it belongs
in the memoria beside p1's rather than instead of it.
