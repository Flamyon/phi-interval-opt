# b1: the analytic derivation of the phi-efficient sets

subpart b1 of the phase plan in CONTEXT.md section 8. paper and pencil with
symbolic verification, no module. b2 encodes what this document derives.

sources read in this session:

    papers/new_preference_order_relationships_paper.txt, [1], for example 3.9's
        condition (15) and its weight condition, read at lines 709-746 directly
        and cross-read against the transcription in docs/part1/a0_framework.md c13,
        c14 and c15.
    docs/part1/a0_framework.md, for theorem 3.3 (c12), example 3.8 (c13), example 3.9
        (c14), the worked function (c15), definition 3.1 (c10) and the three
        order relations (3), (6), (7) (c4).
    docs/part1/a1_uncertainty_model.md, part 3 and the a1-b section, for p1's design,
        its image coordinates, hessians, eigenvalues and stationary points.
    src/problems_tier0.py, for what p0 and p1 actually are, including d-01's
        delta = 1/8.
    docs/part1/a_close_containment.md, for the containment the derived sets must satisfy.
    literature/gH-differentiability calculus for interval analysis.md, for the
        regularity criterion of [10]. flagged below: the theorem number is not
        verified against the paper, which is not in papers/.

every theorem is cited by number and taken from the transcription or from the
paper. no condition is invented, extended, or weakened anywhere in what follows.

symbolic work used exact rational arithmetic from `fractions`, the standard
library, since sympy is not installed in the venv and CONTEXT.md section 11 does
not permit adding a dependency for one session. every script was a throwaway in
the session scratchpad; nothing was added under src/ and no test was changed.


## 0. the precondition the brief asks to be checked first

the brief instructs that condition (15) be confirmed to be stationarity of a
weighted sum of the image coordinates before the linear-system route is used, and
that the derivation stop if it is not.

it is. [1] lines 715-723, transcribed in docs/part1/a0_framework.md c14 and recorded as
v-17, chains three expressions and sets the last to the zero vector of R^n:

>     Σ_{i=1}^{m} w_2i−1 ∇Λ_i^T f(x̄)  +  Σ_{i=1}^{m} w_2i ∇B_i^T f(x̄)
>         = Σ_{i=1}^{m} ∇[ ( w_2i−1 Λ_i^T + w_2i B_i^T ) f ](x̄)
>         = ∇{ Σ_{i=1}^{m} [ ( w_2i−1 Λ_i^T + w_2i B_i^T ) f ] }(x̄)
>         = 0.                                                              (15)

the middle and last expressions are the gradient of the single real-valued
function Σ_i ( w_2i−1 Λ_i^T f + w_2i B_i^T f ), which is exactly the objective of
example 3.8's scalar problem (14). so (15) is first-order stationarity of that
weighted sum, the weights being the same 2m numbers as in (14) save that (14)
also normalises them to sum to one.

the index convention, which matters and is easy to invert: the sum runs over the
m interval objectives, and weight w_2i−1 is paired with the lambda coordinate
Λ_i^T f while w_2i is paired with the beta coordinate B_i^T f. for m = 2 the four
weights are therefore

    w_1 on Λ_1^T f,  w_2 on B_1^T f,  w_3 on Λ_2^T f,  w_4 on B_2^T f.

equation (16) is not used anywhere in this document. it is internally
inconsistent in the weight subscripts on the beta terms, a0 ambiguity a-1 and
s-01, and a0's instruction is to expand (15) from the definitions of Λ_i and
B_i instead. that is what section 2 below does.

consequence for a degree-2 image coordinate. if every image coordinate is a
quadratic

    g_k(x) = (1/2) x^T H_k x + b_k^T x + const,   H_k constant,

then (15) reads

    ( Σ_k w_k H_k ) x = − Σ_k w_k b_k                                        (b1-1)

which is a linear system in x whose coefficients are linear in w. this is the
form the whole p1 derivation uses, and per the s-08 answer the deliverable is the
map w ↦ x(w) and not a bounding box.


## 1. the hypotheses, per problem and per phi

### 1.1 p1's image coordinates

p1 is a1-b's modified design as built in src/problems_tier0.py, with rho = 1/4
and delta = 1/8 per d-01:

    box        x = (x_1, x_2) in [-1/2, 3/2] x [-1/2, 3/2]
    centres    c_1 = x_1^2 + (x_2 - 1)^2      c_2 = (x_1 - 1)^2 + (x_2 - 1)^2
    widths     r_1 = (1/4) x_2^2 + 1/8        r_2 = (1/4) x_1^2 + 1/8
    objectives F_i(x) = [ c_i - r_i,  c_i + r_i ],  i = 1, 2

so m = 2, n = 2, and the transformed real problem has 2m = 4 objectives, per
theorem 3.1 and v-05. the four image coordinates per phi, with Λ_i^T f =
λ_2i−1 f_i + λ_2i f̄_i and B_i^T f = β_2i−1 f_i + β_2i f̄_i taken from theorem
3.3's proof, [1] lines 647 and 656:

    phi_lu, example 2.2, lambda = (1, 0), beta = (0, 1)

      g_1 = Λ_1^T f = c_1 − r_1 = x_1^2 + (3/4) x_2^2 − 2 x_2 + 7/8
      g_2 = B_1^T f = c_1 + r_1 = x_1^2 + (5/4) x_2^2 − 2 x_2 + 9/8
      g_3 = Λ_2^T f = c_2 − r_2 = (3/4) x_1^2 − 2 x_1 + x_2^2 − 2 x_2 + 15/8
      g_4 = B_2^T f = c_2 + r_2 = (5/4) x_1^2 − 2 x_1 + x_2^2 − 2 x_2 + 17/8

    phi_ls, example 2.3, lambda = (1, 0), beta = (−1, 1)

      g_1 = Λ_1^T f = c_1 − r_1, as above
      g_2 = B_1^T f = 2 r_1 = (1/2) x_2^2 + 1/4
      g_3 = Λ_2^T f = c_2 − r_2, as above
      g_4 = B_2^T f = 2 r_2 = (1/2) x_1^2 + 1/4

    phi_cw, example 2.4, lambda = (1/2, 1/2), beta = (−1/2, 1/2)

      g_1 = Λ_1^T f = c_1 = x_1^2 + (x_2 − 1)^2
      g_2 = B_1^T f = r_1 = (1/4) x_2^2 + 1/8
      g_3 = Λ_2^T f = c_2 = (x_1 − 1)^2 + (x_2 − 1)^2
      g_4 = B_2^T f = r_2 = (1/4) x_1^2 + 1/8

these are a1-b's ten distinct coordinates with delta moved from 1/10 to 1/8. they
were re-derived in this session as exact rational quadratic forms and checked
against src/problems_tier0.py composed with the declared centre-radius route of
src/phi_transforms.py, on 400 random points of the box:

    image coordinates agree with src, phi_lu: max abs diff 8.882e-16
    image coordinates agree with src, phi_ls: max abs diff 8.882e-16
    image coordinates agree with src, phi_cw: max abs diff 8.882e-16

so what follows is derived about the problem the code actually evaluates.

the hessians and linear parts, all exact and all constant, every hessian diagonal:

    phi_lu   H_1 = diag(2, 3/2)   b_1 = (0, −2)
             H_2 = diag(2, 5/2)   b_2 = (0, −2)
             H_3 = diag(3/2, 2)   b_3 = (−2, −2)
             H_4 = diag(5/2, 2)   b_4 = (−2, −2)

    phi_ls   H_1 = diag(2, 3/2)   b_1 = (0, −2)
             H_2 = diag(0, 1)     b_2 = (0, 0)
             H_3 = diag(3/2, 2)   b_3 = (−2, −2)
             H_4 = diag(1, 0)     b_4 = (0, 0)

    phi_cw   H_1 = diag(2, 2)     b_1 = (0, −2)
             H_2 = diag(0, 1/2)   b_2 = (0, 0)
             H_3 = diag(2, 2)     b_3 = (−2, −2)
             H_4 = diag(1/2, 0)   b_4 = (0, 0)

every hessian is diagonal, so every non-negative combination of them is diagonal
too, and the maximum off-diagonal entry of Σ_k w_k H_k over the three phi at
w = (1,1,1,1) is exactly 0. that is why (b1-1) decouples into two scalar
equations below.

### 1.2 p1, convexity, by theorem 3.3

theorem 3.3 of [1], transcribed in docs/part1/a0_framework.md c12 and recorded as v-12:

> **Theorem 3.3.** ... Then F is φ-convex if and only if Λ_i^T f and B_i^T f are
> convex for all i ∈ {1, …, m}, where f = (f_1, f̄_1, …, f_m, f̄_m).

each g_k above is a quadratic with a constant hessian, so it is convex on R^2 if
and only if that hessian is positive semidefinite, and the verdict is global
rather than pointwise. verdicts, per coordinate, with the hessian and its
eigenvalues, which are the diagonal entries since every hessian is diagonal:

    phi   coordinate                 hessian          eigenvalues    convex
    lu    g_1 = c_1 − r_1            diag(2, 3/2)     3/2, 2         yes, positive definite
    lu    g_2 = c_1 + r_1            diag(2, 5/2)     2, 5/2         yes, positive definite
    lu    g_3 = c_2 − r_2            diag(3/2, 2)     3/2, 2         yes, positive definite
    lu    g_4 = c_2 + r_2            diag(5/2, 2)     2, 5/2         yes, positive definite
    ls    g_1 = c_1 − r_1            diag(2, 3/2)     3/2, 2         yes, positive definite
    ls    g_2 = 2 r_1                diag(0, 1)       0, 1           yes, semidefinite
    ls    g_3 = c_2 − r_2            diag(3/2, 2)     3/2, 2         yes, positive definite
    ls    g_4 = 2 r_2                diag(1, 0)       0, 1           yes, semidefinite
    cw    g_1 = c_1                  diag(2, 2)       2, 2           yes, positive definite
    cw    g_2 = r_1                  diag(0, 1/2)     0, 1/2         yes, semidefinite
    cw    g_3 = c_2                  diag(2, 2)       2, 2           yes, positive definite
    cw    g_4 = r_2                  diag(1/2, 0)     0, 1/2         yes, semidefinite

so by theorem 3.3, F is phi-convex for all three phi, globally on R^2 and a
fortiori on the box. remark 2.2, the pointwise form transcribed in a0 c12 and
recorded as v-13, therefore also holds at every point.

the four semidefinite rows are the width coordinates. each is affine, in fact
constant, in the variable it does not depend on, so it has a stationary line and
not a stationary point. that degenerate direction is what produces the singular
weights of section 2.3, and it is the reason phi_lu has none: no image coordinate
of phi_lu is a pure width.

this reproduces a1-b's own eigenvalue table, which was computed at delta = 1/10.
delta enters every g_k as an additive constant, so no hessian and no gradient
moves with it; a4-b part 2 verified that in exact integer arithmetic and it is
d-01.

### 1.3 p1, regularity, by the criterion of [10]

the criterion, from `literature/gH-differentiability calculus for interval
analysis.md`, which is a summary and not the paper:

> **Theorem 34** F = (f̂; f̃) is Fréchet gH-differentiable at x⁽⁰⁾ iff f̂ is
> Fréchet differentiable and f̃ is abs-differentiable at x⁽⁰⁾.

with abs-differentiability of f̃ at x⁽⁰⁾ meaning that |f̃| has a classical Fréchet
derivative there, per definition 30 of the same summary.

**[the number was verified in session lit-review, 2026-09-05: it is theorem 34 of
[10], printed page 13, verbatim. and the criterion this section actually applies —
that a differentiable non-negative radius is abs-differentiable — is [10]'s
proposition 32, printed page 12, which covers radii that vanish and not only
strictly positive ones. p-05 is closed, docs/answered.md and
docs/part2/lit_review.md sections 3.1 and 3.2. the paragraph below is left as
written, being the record of what b1 could check on the day.]**

the number is unverified. [10], stefanini, arana-jiménez and sorini 2025, is not
in papers/, so "theorem 34" is the summary's number and this session could not
check it against the paper. that is p-05, whose scope CONTEXT.md section 6 widens
from the gh-difference's definition number to this criterion. the citation is to
the summary and it is a weaker citation than every other in this document. it is
recorded as such rather than dropped, because the outcome of the check is not in
doubt for p1 and CONTEXT.md section 11's rule against keeping unverified items
is about content that could be wrong, not about a label on a check whose result
is forced by the functions themselves.

the check, per objective, with f̂ = c_i and f̃ = r_i as p1 declares them:

    objective 1: c_1 = x_1^2 + (x_2 − 1)^2 is a polynomial, Fréchet differentiable
        everywhere. r_1 = (1/4) x_2^2 + 1/8 is a polynomial and is strictly
        positive on R^2, minimum 1/8, so |r_1| = r_1 is a polynomial too and is
        classically differentiable everywhere. abs-differentiable everywhere.
    objective 2: identical with the roles of x_1 and x_2 exchanged. r_2 has the
        same minimum 1/8.

so p1 is Fréchet gH-differentiable at every point of R^2, and in particular at
every point of the box. the check is trivial because every function involved is
a polynomial with a strictly positive radius, which is exactly the design
requirement a1 imposed on p1 and delta's job.

independently of [10], the hypothesis example 3.9 actually states is
differentiability of Λ_i^T f and B_i^T f, v-15, and all four of those are
degree-2 polynomials for every one of the three phi. that hypothesis is
satisfied by inspection and does not depend on the unverified theorem number.

### 1.4 p1, the hypotheses of example 3.9 and example 3.8, assembled

example 3.9's three statements, transcribed in a0 c14 and recorded as v-16:

> 1. If x̄ ∈ S is a weak optimal solution for (1MIOP_φ), then there are
>    w_1, …, w_2m ∈ ℝ, with w_i ⩾ 0 not equal zero for all i ∈ {1, …, 2m}, such
>    that (15).
> 2. If x̄ ∈ S, S is convex, F is φ-convex and there are w_1, …, w_2m ∈ ℝ, with
>    w_i ⩾ 0 not equal zero for all i ∈ {1, …, 2m}, such that (15) holds, then x̄
>    is a weak optimal solution for (1MIOP_φ).
> 3. If x̄ ∈ S, S is convex, F is φ-convex and there are w_1, …, w_2m ∈ ℝ, with
>    w_i > 0 for all i ∈ {1, …, 2m}, such that (15) holds, then x̄ is an optimal
>    solution for (1MIOP_φ).

hypothesis by hypothesis, for p1 under each of the three phi:

    Λ_i^T f, B_i^T f differentiable   yes, all four are degree-2 polynomials.
    S convex                          yes, S is the box [-1/2, 3/2]^2.
    F phi-convex                      yes, theorem 3.3 and section 1.2 above.

so all three statements are available for p1 under all three phi, and example
3.8's four statements are available too: statements 1, 2 and 3 of 3.8 need no
hypothesis beyond the standing weight condition, and statement 4 needs S convex
and F phi-convex, both of which hold.

two readings that this document commits to, both already on record and neither
resolved here.

s-02, the weight phrase "w_i ⩾ 0 not equal zero for all i" in statements 1 and 2.
this document takes reading one, non-negative and not all zero, which is
CONTEXT.md section 6's commitment. section 6 below reports a witness on p1 that
tells against reading two; it is offered as evidence for the supervisors and s-02
is not closed here.

the interiority reading. condition (15) is unconstrained stationarity and carries
no constraint multipliers, unlike examples 3.4 to 3.7. read literally, statement
1 would be false at any weak optimal point on a face of S, since a constrained
minimum need not have a vanishing gradient. this project reads example 3.9 as an
interior condition, which is what docs/part1/a1_uncertainty_model.md part 3 already
states and what fixed p1's box, and applies it only at interior points. every
derived set below is strictly interior to the box, so nothing in the p1 result
depends on this reading; it is stated because the necessity direction of
section 4 is the place where it would matter.

### 1.5 p0's image coordinates, convexity and regularity

p0 is the worked function [1] gives after example 3.9, [1] lines 752-753, v-18:
F : R → (C)^2 with F_1(x) = [−|x|, |x|] and F_2(x) = [0, x^2], so
f = (−|x|, |x|, 0, x^2). the project's box is [−1, 1], src/problems_tier0.py,
holding the published anchor x = 0 at its centre.

the four image coordinates, per phi:

    phi_lu   Λ_1^T f = −|x|    B_1^T f = |x|      Λ_2^T f = 0     B_2^T f = x^2
    phi_ls   Λ_1^T f = −|x|    B_1^T f = 2|x|     Λ_2^T f = 0     B_2^T f = x^2
    phi_cw   Λ_1^T f = 0       B_1^T f = |x|      Λ_2^T f = x^2/2 B_2^T f = x^2/2

convexity, by theorem 3.3, checked by hand and confirmed on 200000 midpoint
chords over [−1, 1]. a positive number in the table is a violation of the
midpoint convexity inequality:

    phi   coordinate 1   coordinate 2   coordinate 3   coordinate 4   F phi-convex
    lu    +0.998689      +0.000000      +0.000000      −0.000000      no
    ls    +0.998689      +0.000000      +0.000000      −0.000000      no
    cw    +0.000000      +0.000000      −0.000000      −0.000000      yes

the single failing coordinate is Λ_1^T f = −|x|, which is concave and not convex,
and it is the first coordinate under phi_lu and under phi_ls alike. under phi_cw
that coordinate is instead (f_1 + f̄_1)/2 = 0, which is convex, and all four are
convex. so:

    **F is phi_cw-convex. F is neither phi_lu-convex nor phi_ls-convex.**

regularity, by the criterion of [10] cited above with the number unverified, on
p0's centre and half-width, which src/problems_tier0.py records in closed form:

    objective 1: ĉ_1 = 0, differentiable everywhere. r̃_1 = |x|, and |r̃_1| = |x|
        has no classical derivative at x = 0. so F_1 is not gH-differentiable at
        x = 0, and is gH-differentiable at every x ≠ 0.
    objective 2: ĉ_2 = x^2/2 and r̃_2 = x^2/2 with |r̃_2| = x^2/2, both
        polynomials. gH-differentiable everywhere.

the same failure shows up directly in the hypothesis example 3.9 states, which is
differentiability of the image coordinates: under phi_lu, Λ_1^T f = −|x| and
B_1^T f = |x| are both non-differentiable at x = 0; under phi_ls, −|x| and 2|x|;
under phi_cw, Λ_1^T f = 0 is smooth but B_1^T f = |x| is not. so example 3.9's
differentiability hypothesis fails at x = 0 under **all three** phi, and holds at
every x ≠ 0 under all three.

this confirms r-04, which was raised for phi_lu, and widens it: the obstruction is
not particular to phi_lu. it is p0's first interval objective having |x| as its
half-width, and since every phi_i is invertible the non-differentiability cannot
be transformed away, which is the point a0 records under c15 and under
disagreement d-b.


## 2. the derivation for p1

### 2.1 the system

with the four image coordinates written as (1/2) x^T H_k x + b_k^T x + const,
condition (15) is (b1-1). all four hessians are diagonal, so the system is
diagonal too and splits into two scalar equations,

    d_1(w) x_1 = ρ_1(w),        d_2(w) x_2 = ρ_2(w),

where d_1, d_2, ρ_1, ρ_2 are the linear forms in w = (w_1, w_2, w_3, w_4) below,
read off Σ_k w_k H_k and −Σ_k w_k b_k and computed exactly:

    phi_lu   d_1 = 2 w_1 + 2 w_2 + (3/2) w_3 + (5/2) w_4
             d_2 = (3/2) w_1 + (5/2) w_2 + 2 w_3 + 2 w_4
             ρ_1 = 2 w_3 + 2 w_4
             ρ_2 = 2 w_1 + 2 w_2 + 2 w_3 + 2 w_4

    phi_ls   d_1 = 2 w_1 + (3/2) w_3 + w_4
             d_2 = (3/2) w_1 + w_2 + 2 w_3
             ρ_1 = 2 w_3
             ρ_2 = 2 w_1 + 2 w_3

    phi_cw   d_1 = 2 w_1 + 2 w_3 + (1/2) w_4
             d_2 = 2 w_1 + (1/2) w_2 + 2 w_3
             ρ_1 = 2 w_3
             ρ_2 = 2 w_1 + 2 w_3

(15) is homogeneous of degree one in w, so x(w) depends on the ray through w and
not on its length. example 3.8's standing condition normalises the weights to sum
to one and example 3.9 does not, a0 c14; both are used below and the
normalisation is stated wherever it matters.

### 2.2 the map x(w), in closed form

wherever d_1(w) and d_2(w) are both non-zero, which for w ⩾ 0 means both
positive, the system has the unique solution

    phi_lu   x_1(w) = ( 2 w_3 + 2 w_4 ) / ( 2 w_1 + 2 w_2 + (3/2) w_3 + (5/2) w_4 )
             x_2(w) = ( 2 w_1 + 2 w_2 + 2 w_3 + 2 w_4 )
                      / ( (3/2) w_1 + (5/2) w_2 + 2 w_3 + 2 w_4 )

    phi_ls   x_1(w) = 2 w_3 / ( 2 w_1 + (3/2) w_3 + w_4 )
             x_2(w) = ( 2 w_1 + 2 w_3 ) / ( (3/2) w_1 + w_2 + 2 w_3 )

    phi_cw   x_1(w) = 2 w_3 / ( 2 w_1 + 2 w_3 + (1/2) w_4 )
             x_2(w) = ( 2 w_1 + 2 w_3 ) / ( 2 w_1 + (1/2) w_2 + 2 w_3 )

that is the deliverable s-08 asks for. it was verified in exact rational
arithmetic by substituting x(w) back into the gradient of Σ_k w_k g_k and
checking it is the zero vector, on 3000 random integer weight vectors per phi:

    phi_lu: 3000 regular weights, 0 singular, max |gradient| = 0
    phi_ls: 3000 regular weights, 0 singular, max |gradient| = 0
    phi_cw: 3000 regular weights, 0 singular, max |gradient| = 0

exactly zero, not approximately: the arithmetic was rational throughout.

### 2.3 the singular weights, characterised

Σ_k w_k H_k fails to be invertible exactly when d_1(w) = 0 or d_2(w) = 0. every
coefficient in those linear forms is non-negative, so for w ⩾ 0 a form vanishes
exactly when every weight sitting on a positive coefficient is zero. enumerating
the sixteen supports gives the complete answer, and it was computed that way:

    phi_lu: none. every coefficient of d_1 and of d_2 is strictly positive, so
        d_1(w) > 0 and d_2(w) > 0 for every w ⩾ 0 with w ≠ 0. the system is
        non-singular on the whole weight simplex and x(w) is defined everywhere
        on it.

    phi_ls: exactly two rays.
        w = (0, w_2, 0, 0), w_2 > 0.  d_1 = 0, ρ_1 = 0, d_2 = w_2 > 0, ρ_2 = 0.
        w = (0, 0, 0, w_4), w_4 > 0.  d_2 = 0, ρ_2 = 0, d_1 = w_4 > 0, ρ_1 = 0.

    phi_cw: exactly the same two rays, with the same vanishing right-hand sides.

so the singular set is the two weight vectors that put all their mass on a single
width coordinate: w_2 alone, which weights 2 r_1 under phi_ls and r_1 under
phi_cw, and w_4 alone, which weights 2 r_2 and r_2. that is the degenerate
direction of section 1.2 appearing where it was expected.

**what each singular case means, since the brief asks and since silently
restricting to invertible w would hide it.** in both cases the vanishing row of
the matrix comes with a vanishing right-hand side, so the system is **consistent**
and has a line of solutions, never no solution:

    w = (0, w_2, 0, 0): the scalarised objective is a positive multiple of r_1,
        a function of x_2 alone with its minimum at x_2 = 0. the system reads
        0 · x_1 = 0 and (coefficient) · x_2 = 0, so the solution set is the whole
        line **x_2 = 0**, every x_1.
    w = (0, 0, 0, w_4): the scalarised objective is a positive multiple of r_2,
        a function of x_1 alone with its minimum at x_1 = 0. the solution set is
        the whole line **x_1 = 0**, every x_2.

there is no weight for which the system is inconsistent, under any of the three
phi. that is not an accident of the numbers: the right-hand side −Σ_k w_k b_k is
a combination of the same b_k, and each width coordinate has b_k = 0, so a
support that kills a row of the matrix kills the matching entry of the right-hand
side with it.

### 2.4 the derived sets, in closed form

x(w) over the non-singular part of the weight simplex sweeps out a
two-dimensional region, and it has an explicit description. by homogeneity the
weights can be normalised conveniently, and the resulting parameterisations
decouple, which is what makes the region computable rather than merely samplable.

**phi_lu.** normalise Σ w = 1 and write u = w_3 + w_4 in [0, 1]. then
d_1 = 2 − u/2 + w_4 and d_2 = 3/2 + u/2 + w_2, and

    x_1 = 2u / (2 − u/2 + w_4),   w_4 in [0, u]
    x_2 = 2  / (3/2 + u/2 + w_2), w_2 in [0, 1 − u]

so for each u the two coordinates are controlled by two weights that vary
independently, and the reachable set at that u is the closed rectangle

    [ 4u/(4+u), 4u/(4−u) ] x [ 4/(5−u), 4/(3+u) ].

the union over u in [0, 1] is, eliminating u,

    **X_lu = { (x_1, x_2) : x_1 ⩾ 0,
                            4 x_1 − x_1 x_2 − 20 x_2 + 16 ⩽ 0,
                            7 x_1 x_2 − 4 x_1 + 12 x_2 − 16 ⩽ 0 }**

a region bounded below by x_1 = (20 x_2 − 16)/(4 − x_2) for x_2 in [4/5, 1] and
above by x_1 = (16 − 12 x_2)/(7 x_2 − 4) for x_2 in [1, 4/3], the two curves
meeting at (4/3, 1) and both reaching x_1 = 0, at x_2 = 4/5 and at x_2 = 4/3.

**phi_ls.** for w with w_1 + w_3 > 0, normalise w_1 + w_3 = 1 and put s = w_3 in
[0, 1]. then w_2 and w_4 are unconstrained non-negative reals and

    x_1 = 2s / (2 − s/2 + w_4),      w_4 ⩾ 0,  giving x_1 in (0, 4s/(4−s)]
    x_2 = 2  / (3/2 + s/2 + w_2),    w_2 ⩾ 0,  giving x_2 in (0, 4/(3+s)]

independently. the union over s in [0, 1], together with the point (0, 0) reached
by w_1 = w_3 = 0 with w_2, w_4 both positive, is

    **X_ls = { (x_1, x_2) : 0 ⩽ x_1 ⩽ 4/3, 0 ⩽ x_2 ⩽ 4/3,
                            7 x_1 x_2 − 4 x_1 + 12 x_2 − 16 ⩽ 0 }
              minus the open segment { (x_1, 0) : 0 < x_1 ⩽ 4/3 }**

the excluded segment is reached only in the limit w_2 → ∞, that is only at the
singular ray, and section 2.5 says what happens there. the upper boundary is the
same curve x_1 = (16 − 12 x_2)/(7 x_2 − 4) that bounds X_lu above.

**phi_cw.** the same normalisation, w_1 + w_3 = 1 and s = w_3:

    x_1 = 2s / (2 + w_4/2),   w_4 ⩾ 0,  giving x_1 in (0, s]
    x_2 = 2  / (2 + w_2/2),   w_2 ⩾ 0,  giving x_2 in (0, 1]

independently, and the union over s in [0, 1] is

    **X_cw = [0, 1] x [0, 1] minus the open segment { (x_1, 0) : 0 < x_1 ⩽ 1 }**

so phi_cw's set is the closed unit square, up to that one edge, and it is the one
of the three that is a product of intervals. that matches a1-b's finding that
phi_cw's efficient set had one distinct x_2 range across all occupied x_1 columns
where phi_lu and phi_ls had thirteen and eleven.

verification of these three descriptions, both directions, in exact rational
arithmetic. forward, on the simplex grid at denominator 40, 12341 weight vectors:

    phi_lu: 12341 regular, 0 singular, 0 outside the stated region
    phi_ls: 12339 regular, 2 singular, 0 outside the stated region
    phi_cw: 12339 regular, 2 singular, 0 outside the stated region

with x_1 ranging over [0, 4/3] and x_2 over [4/5, 4/3] for phi_lu, both over
[0, 4/3] for phi_ls, and both over [0, 1] for phi_cw. converse, inverting the
parameterisation exactly at 301 random rational points of each stated region:

    phi_lu: 301 region points tested, 0 without a witness weight
    phi_ls: 301 region points tested, 0 without a witness weight
    phi_cw: 301 region points tested, 0 without a witness weight

the four extreme values 4/5, 1, 4/3 and 4/3 are the stationary points a1-b lists
for c + r, c, c − r and r in their own width variable, at 1/(1+rho), 1, 1/(1−rho)
and 0 with rho = 1/4. the derivation puts them exactly where a1-b's grid found
them.

### 2.5 interiority

condition (15) is unconstrained stationarity and carries no constraint
multipliers, so a candidate on a face of the box is outside example 3.9's scope,
per section 1.4.

    X_lu is contained in [0, 4/3] x [4/5, 4/3].
    X_ls and X_cw are contained in [0, 4/3] x [0, 4/3] and [0, 1]^2.

the box is [−1/2, 3/2]^2 and 4/3 < 3/2, so **every point of all three derived
sets is strictly interior to the box**, with a margin of at least 1/6 on every
side. no candidate lies on a face and example 3.9 applies to all of them. this is
the property a1 chose the box and rho = 1/4 to obtain, and it is confirmed here
rather than assumed.

the two singular lines are the exception and are the only one. the line x_2 = 0
runs the full width of the box and meets the faces x_1 = −1/2 and x_1 = 3/2, and
the line x_1 = 0 meets x_2 = −1/2 and x_2 = 3/2. the four endpoints are on faces
and are outside example 3.9's scope; every other point of those lines is interior
and inside it.

### 2.6 optimal against weakly optimal

three published routes are available and they give different strengths. the
shortest route to each conclusion is named, per the brief's instruction to say
where example 3.8 was used and where example 3.9 was.

**every x(w) with w in the simplex and Σ_k w_k H_k non-singular is an optimal
solution.** the route is **example 3.8 statement 3**, not example 3.9. the
scalarised objective Σ_k w_k g_k is a quadratic whose hessian Σ_k w_k H_k is
positive definite exactly when the system is non-singular, so it is strictly
convex; x(w) is its stationary point and therefore its unique global minimiser
over R^2, and since x(w) is interior to the box it is the unique minimiser over
S as well. example 3.8 statement 3 reads

> 3. If x̄ ∈ S is the only optimal solution for (MOP_φ(w)), then x̄ ∈ S is an
>    optimal solution for (1MIOP_φ).

and its hypothesis is exactly uniqueness, with no positivity required of the
weights and no convexity of F required. so uniqueness carries the conclusion all
the way to optimality, including at weight vectors with zero components. this is
strictly stronger than example 3.9 statement 3, which would deliver optimality
only for w with every component strictly positive, and it is the reason example
3.8 is the shorter route for the whole regular family.

**example 3.9 statement 3** is available as well and agrees where it applies: for
w with every component strictly positive, S convex and F phi-convex both hold and
(15) holds at x(w) by construction, so x(w) is an optimal solution. it is used
here only as a cross-check, because 3.8 statement 3 already covers those weights
and more.

**example 3.9 statement 2** gives weak optimality for every w ⩾ 0 not all zero at
which (15) holds, which under reading one of s-02 is every non-singular w and
both singular rays. **example 3.8 statement 1** gives the same conclusion,

> 1. If x̄ ∈ S is an optimal solution for (MOP_φ(w)), then x̄ ∈ S is a weak
>    optimal solution for (1MIOP_φ).

from the same fact and without any weight-condition ambiguity, since 3.8's
standing condition is plainly w_i ⩾ 0 with Σ w_i = 1. every point of the two
singular lines minimises the corresponding width coordinate globally, hence is an
optimal solution of MOP_φ(w) for that w, hence is a weak optimal solution. this
document takes the weak-optimality of the singular lines from **example 3.8
statement 1**, which makes that conclusion independent of s-02.

so the separation, per phi:

    phi_lu   optimal:        every point of X_lu, by example 3.8 statement 3.
             weakly optimal: the same set, plus nothing else; there is no
                             singular weight.
    phi_ls   optimal:        every point of X_ls, by example 3.8 statement 3.
             weakly optimal: X_ls, plus the whole line x_2 = 0 and the whole
                             line x_1 = 0 inside the box, by example 3.8
                             statement 1.
    phi_cw   optimal:        every point of X_cw, by example 3.8 statement 3.
             weakly optimal: X_cw, plus the same two lines.

and the necessity direction, section 4 below, closes the set from the other side.

**where this does not close, and it is the one place in the p1 derivation.** on
the two singular lines the published results give weak optimality and no
optimality verdict either way. example 3.8 statement 3 does not apply, the scalar
problem there having a line of minimisers rather than one; statement 2 needs
w_i > 0 for all i, which the singular rays do not have; example 3.9 statement 3
needs the same. and no non-singular weight reaches the interior of those
segments: x_2(w) = 0 forces w_1 = w_3 = 0 under phi_ls and under phi_cw, which is
the singular ray itself. the segments concerned are

    { (x_1, 0) : 0 < x_1 ⩽ 4/3 } for phi_ls and { (x_1, 0) : 0 < x_1 ⩽ 1 } for
    phi_cw, together with their reflections on the line x_1 = 0 outside the
    derived region.

these are exactly the closure of X_ls and of X_cw minus the sets themselves. the
grid measurement of section 3 says the parts of those lines with x_1 in [0, 4/3]
respectively [0, 1] are non-dominated and the rest are dominated, and that is a
finer separation than the published conditions produce. **the derivation does not
close there and it is not patched.** it is a boundary of measure zero in a
two-dimensional set and b2 can sample the closure or the open set without the
difference being visible to any metric that integrates, but the statement stands
as an open item and is listed in section 7.


## 3. the check that matters, against a4's grid

the derived sets must reproduce what a4's grid measured. the comparison is run in
both directions and reported with numbers. the grid, the box, the filter and the
route are a4's own: the 61 x 61 grid on [−1/2, 3/2]^2, phi applied to p1's
declared centre-radius representation through the matching route of
src/phi_transforms.py, and the ordinary pareto relation on doubles with no
tolerance, per d-02.

grid spacing is 2/60 = 0.03333.

### 3.1 direction one, do the derived points survive the grid filter

20000 points of each derived set, sampled through x(w) from a dirichlet sample of
the weight simplex, tested against the whole 3721-point grid:

    phi_lu  20000 derived points, 0 dominated by any grid point
    phi_ls  20000 derived points, 0 dominated by any grid point
    phi_cw  20000 derived points, 0 dominated by any grid point

and the same test the other way round, on the grid points that lie inside the
closed-form region:

    phi_lu  289 of 289 in-region grid points survive the grid filter
    phi_ls  1418 of 1418 in-region grid points survive the grid filter
    phi_cw  961 of 961 in-region grid points survive the grid filter

not one derived point is dominated, by any grid point, under any phi. this
direction is exact.

### 3.2 direction two, do the grid points lie near the derived set

    grid        phi   |ND|   inside the region   outside   max distance to region
    61 x 61     lu     460    289  (0.628)        171       0.08718 = 2.62 spacing
    61 x 61     ls    1505   1418  (0.942)         87       0.07620 = 2.29 spacing
    61 x 61     cw     961    961  (1.000)          0       0
    121 x 121   lu    1530   1136  (0.742)        394       0.04521 = 2.71 spacing
    121 x 121   ls    5759   5559  (0.965)        200       0.04453 = 2.67 spacing
    121 x 121   cw    3721   3721  (1.000)          0       0

on the r-08 slice grid, which is what a4's test actually filters on, the union
bounding box of the three efficient sets widened by 0.1 and re-gridded at 61 x 61
on [−0.1, 1.4333]^2 with spacing 0.02556:

    phi_lu  |ND| =  724   in-region  483 (0.667)   outside 241   max 0.06707 = 2.62 spacing
    phi_ls  |ND| = 2496   in-region 2377 (0.952)   outside 119   max 0.06066 = 2.37 spacing
    phi_cw  |ND| = 1600   in-region 1600 (1.000)   outside   0   max 0

phi_cw agrees exactly, at every resolution and on both grids. 961 is 31^2, 3721
is 61^2 and 1600 is 40^2, which are precisely the grid points of [0, 1]^2 at each
resolution, and X_cw is [0, 1]^2. there is nothing to explain there.

phi_lu and phi_ls have a residue and it has to be accounted for rather than
tolerated.

### 3.3 the residue is the finite grid, and here is why that is the answer

the brief requires a verdict on whether a disagreement is the derivation, the
grid's coarseness, or the measurement, and requires stopping rather than adjusting
the derivation to fit. the verdict is **the grid's coarseness**, on four
independent pieces of evidence, and the derivation was not adjusted.

first, the mechanism is not in question. the grid's non-dominated set is the
non-dominated set of a **finite** point set. a grid point can be non-dominated
among grid points while being dominated by a point that is not on the grid. so the
grid filter necessarily over-includes near the boundary of the true efficient set,
and never under-includes: it can keep a point it should drop, but it cannot drop a
point nothing dominates. that predicted asymmetry is exactly what section 3.1 and
3.2 show, a perfect score in one direction and a boundary residue in the other.

second, the residue's size scales with the spacing and its shape does not. the
maximum distance from an excess point to the derived region is 2.62 spacings at
spacing 0.03333, 2.71 spacings at 0.01667, and 2.62 spacings on a third grid with
spacing 0.02556. the ratio is stable near 2.6 while the absolute distance halves
when the spacing halves, 0.08718 to 0.04521 for phi_lu and 0.07620 to 0.04453 for
phi_ls. the median excess point sits 1.08 and 1.04 spacings out. a wrong
derivation would give a residue at a fixed distance, not one proportional to the
spacing.

third, the fraction of the grid's set that the derivation explains rises with
resolution, which is convergence rather than a fixed discrepancy:

    phi_lu  0.628 at 61 x 61  to  0.742 at 121 x 121
    phi_ls  0.942 at 61 x 61  to  0.965 at 121 x 121
    phi_cw  1.000 at both

fourth, and most directly, the excess points fall when the grid is refined around
them. a local search on a 193 x 193 neighbourhood of radius four spacings, which
is 24 times the grid resolution, was run at every one of the 61 x 61 grid's
non-dominated points:

    phi_lu  in-region 289: 0 fall under refinement | outside 171: 153 fall
    phi_ls  in-region 1418: 0 fall under refinement | outside 87: 76 fall
    phi_cw  in-region 961: 0 fall under refinement | outside 0: 0 fall

every point the derivation claims is non-dominated survives a 24-fold refinement,
under all three phi, without exception. of the points the derivation does not
claim, 153 of 171 and 76 of 87 are dominated by a point the coarse grid simply
did not contain. widening to a radius of twelve spacings leaves 19 and 12
survivors, and all of them lie within about 0.7 of a spacing of the derived
boundary, close enough that a dominator would have to sit inside the refinement's
own step. their positions are on the two boundary curves: for instance the phi_lu
survivor (0.1, 1.3) sits against the curve x_1 = (16 − 12 x_2)/(7 x_2 − 4), which
at x_2 = 1.3 gives x_1 = 0.0784, so the point is 0.0216 outside, which is 0.65 of
a spacing.

nothing in the derivation was changed to produce these numbers. the closed forms
of section 2.4 were fixed before any grid was filtered, and the agreement with
a1-b's independently measured extents, x_1 in [0, 4/3] and x_2 in [0.8, 4/3] for
phi_lu, both in [0, 4/3] for phi_ls, both in [0, 1] for phi_cw, was a consequence
and not an input.


## 4. completeness, and what closes the set from the other side

sufficiency alone would only say the derived set is contained in the efficient
set. the reverse containment is example 3.9 statement 1, which is a necessary
condition: if x̄ is a weak optimal solution then there are weights w ⩾ 0, not all
zero, satisfying (15) at x̄. its only hypothesis is differentiability of the image
coordinates, which holds everywhere for p1.

so for x̄ in the interior of the box, reading example 3.9 as an interior condition
per section 1.4:

    x̄ weakly optimal  ⇒  (15) holds at x̄ for some w ⩾ 0, w ≠ 0
                      ⇒  x̄ is in X_phi, or x̄ is on one of the two singular lines.

and definition 3.1's implication chain, transcribed in a0 c10, gives optimal ⇒
weak optimal, so the same containment holds for the optimal set. combining with
section 2.6:

    **X_phi ⊆ optimal set ⊆ weak optimal set ⊆ X_phi ∪ (the singular lines)**

which pins the efficient set to within the two lines of measure zero that section
2.6 already flagged as not closing. for phi_lu there are no singular lines and the
sandwich collapses:

    **under phi_lu the optimal set and the weak optimal set both equal X_lu
    exactly, among interior points.**

the necessity direction is the one place the interiority reading is load-bearing,
and it is why every derived set being strictly interior to the box, section 2.5,
matters beyond tidiness.


## 5. the containment check

docs/part1/a_close_containment.md proves, from the criterion that phi_B = M phi_A with M
entrywise non-negative and invertible makes phi_A-dominance imply phi_B-dominance,
that ND_lu and ND_cw are both contained in ND_ls, exactly and for every problem.
this document did not use that result anywhere in the derivation, per the standing
constraint in that document and s-11; it is used here only as an independent test
on the derived closed forms. a derivation violating it would have a bug.

from the closed forms of section 2.4, by inspection:

    X_lu inside X_ls. X_lu's defining inequality 7 x_1 x_2 − 4 x_1 + 12 x_2 ⩽ 16
        is X_ls's. X_lu also carries 4 x_1 − x_1 x_2 − 20 x_2 + 16 ⩽ 0, which
        forces x_2 ⩾ 4/5 > 0, and x_1 ⩽ 4/3 follows from the two together. so
        every point of X_lu satisfies all three of X_ls's constraints.
    X_cw inside X_ls. on [0, 1]^2 the form 7 x_1 x_2 − 4 x_1 + 12 x_2 is largest
        at (1, 1), where it is 7 − 4 + 12 = 15 ⩽ 16, and 1 ⩽ 4/3.

measured on 200000 uniform points of the box:

    lu inside ls:  0 violations of 15606 points in X_lu
    cw inside ls:  0 violations of 49664 points in X_cw
    lu inside cw:  9456 violations of 15606
    cw inside lu: 43514 violations of 49664

both containments hold on the derived sets, and phi_lu against phi_cw is nested in
neither direction, with substantial violation counts both ways. that is corollary
1, corollary 2 and corollary 3 of docs/part1/a_close_containment.md reproduced from an
entirely independent route: that document argues from the map between the two
image spaces and never looks at F, while this one derives each set from [1]'s
optimality conditions applied to p1 and never uses the map. the two agree.

this also confirms, on p1, the reason CONTEXT.md section 10 e3 takes the
sensitivity signal from the phi_lu against phi_cw pair: it is the pair where the
sets genuinely cross. a1-b's grid measurement of the same pair puts the
intersection at 42.6 per cent of phi_lu and 20.4 per cent of phi_cw, which is the
same picture from the grid that the closed forms give here.


## 6. a witness bearing on s-02, offered and not resolving it

s-02 asks whether example 3.9's phrase "w_i ⩾ 0 not equal zero for all i" in
statements 1 and 2 means non-negative and not all zero, reading one, or strictly
positive, reading two. a0 recorded the ambiguity and declined to settle it, noting
only that reading two would make statement 3 redundant, an argument from the
structure of the example rather than from its text.

p1 supplies a witness against reading two, and it is stated here because the brief
requires any b1 result turning on a zero weight to carry the ambiguity explicitly.

take phi_lu and x̄ = (4/3, 1). it is interior to the box. condition (15) at x̄ is
the linear system A w = 0 with

    A = [ [ 8/3, 8/3, 0, 4/3 ], [ −1/2, 1/2, 0, 0 ] ]

and on the simplex grid at denominator 100 exactly one weight vector satisfies it,
w = (0, 0, 1, 0), which has three zero components; none with every component
strictly positive does. meanwhile x̄ is the unique global minimiser of g_3 =
c_2 − r_2, whose hessian diag(3/2, 2) is positive definite, so example 3.8
statement 3 makes x̄ an optimal solution, hence a weak optimal solution by
definition 3.1's implication chain. a search over 2.2 million points of the box,
including 200000 concentrated within 1e−4 of x̄, found nothing dominating it.

so x̄ is weakly optimal and satisfies (15) only with a weight vector having zero
components. under reading two, example 3.9 statement 1 would assert the existence
of a strictly positive w satisfying (15) at x̄, and there is none. reading two
therefore makes statement 1 false for this F, and reading one is the one under
which the published statement holds here.

this is evidence, not a resolution. it is one instance, it rests on this project's
reading of example 3.8 statement 3 and of the implication chain, and s-02 is a
question for the authors about their own sentence. s-02 stays open and is now
carried to the supervisors with this witness attached. nothing in section 2 or 3
depends on the answer: every optimality conclusion above is drawn from example
3.8, whose weight condition is unambiguous, and example 3.9 statement 2 is used
only as a cross-check. the one place reading two would bite is the necessity
direction of section 4, which would then be unavailable and would leave the
derived sets proved to be contained in the efficient set but not proved to
exhaust it.


## 7. p0

r-04 predicted that example 3.9 could not reach p0's anchor under phi_lu. it
cannot, and section 1.5 widens the finding: the differentiability hypothesis fails
at x = 0 under all three phi, and phi-convexity fails under two of them. what
follows states, per phi, what can and cannot be derived with the published results
as they stand. no route around a failed hypothesis is invented.

### 7.1 what fails, per phi

    hypothesis                             phi_lu        phi_ls        phi_cw
    image coordinates differentiable at 0  no            no            no
    image coordinates differentiable, x≠0  yes           yes           yes
    F phi-convex, theorem 3.3              no            no            yes
    S convex                               yes           yes           yes

    example 3.9 statement 1 at x = 0       unavailable   unavailable   unavailable
    example 3.9 statements 2, 3 at x = 0   unavailable   unavailable   unavailable
    example 3.9 statements 2, 3 at x ≠ 0   unavailable   unavailable   available
    example 3.8 statements 1, 2, 3         available     available     available
    example 3.8 statement 4                unavailable   unavailable   available

example 3.8 statements 1, 2 and 3 require no differentiability and no convexity,
a0 c13, so they survive everywhere. statement 4 is the only one needing
phi-convexity and it survives under phi_cw alone.

### 7.2 what example 3.8 does reach

under each of the three phi, the scalarised problem (14) has x = 0 as its unique
minimiser for suitable weights, so **example 3.8 statement 3 makes x = 0 an
optimal solution for (1MIOP_φ) under all three phi**. witnesses, on the simplex
and verified on a 2000001-point grid of [−1, 1]:

    phi_lu  w = (0, 1/2, 0, 1/2), objective (1/2)|x| + (1/2)x^2, argmin {0}, unique
            w = (0.1, 0.4, 0.1, 0.4), objective 0.3|x| + 0.4x^2, argmin {0}, unique,
                and every w_i > 0, so example 3.8 statement 2 gives the same
                conclusion independently
    phi_ls  w = (0, 1/2, 0, 1/2), objective |x| + (1/2)x^2, argmin {0}, unique
            w = (0.1, 0.4, 0.1, 0.4), objective 0.7|x| + 0.4x^2, argmin {0}, unique,
                every w_i > 0
    phi_cw  w = (0, 1/2, 1/4, 1/4), objective (1/2)|x| + (1/4)x^2, argmin {0}, unique
            w = (0.1, 0.4, 0.25, 0.25), objective 0.4|x| + 0.25x^2, argmin {0},
                unique, every w_i > 0

so the published anchor is recovered, and by a route that needs neither the
differentiability that fails at x = 0 nor the convexity that fails under phi_lu
and phi_ls. that is r-04's mitigation working as recorded, and it is the check on
the procedure that CONTEXT.md section 10 b1 asks for before the procedure is
trusted on p1.

what the paper asserts is that x = 0 is "a strict minimum" under phi_lu, [1] line
754, v-19. what example 3.8 statement 3 delivers is an **optimal solution** in the
sense of definition 3.1(2). those are not stated by [1] to be the same thing, and
p-06 is precisely the question of whether [1] maps its phrase onto one of
definition 3.1's three names. **this derivation does not resolve p-06 and does not
attempt to.** what it can say is recorded in 7.4.

### 7.3 what the optimality conditions cannot reach, and what definition 3.1 gives

**the efficient sets themselves do not come from the optimality conditions for p0
under any phi.** the reasons, per phi:

    phi_lu and phi_ls. F is not phi-convex, so example 3.9 statements 2 and 3 and
        example 3.8 statement 4 are all unavailable, and those are the only
        published results that would characterise the set rather than certify one
        point. example 3.9 statement 1 is available at x ≠ 0 and is a necessary
        condition only; it is not enough to determine the set, and at x = 0 it is
        unavailable too.
    phi_cw. F is phi-convex and everything except differentiability at 0 holds, so
        example 3.9 statements 1, 2 and 3 and example 3.8 statement 4 are all
        available at x ≠ 0. but they are **vacuous** here. Λ_1^T f = (f_1 + f̄_1)/2
        = 0 is identically constant, so (15) holds at every x in R with
        w = (1, 0, 0, 0), and example 3.9 statement 2 then says every point of S is
        a weak optimal solution. that is a true statement and not a defect, since
        no point can be strictly smaller in a constant coordinate, but it carries
        no information about the set. example 3.8 statement 4 is vacuous for the
        same reason: it asserts that an optimal x̄ minimises some MOP_φ(w), and
        w = (1, 0, 0, 0) makes every x a minimiser, so the conclusion excludes
        nothing.

what does determine the sets is **definition 3.1 applied directly**, with the
order relations (3), (6) and (7). that is [1]'s own definition applied to an
explicit F, not a new condition, and a0 c15 names it as one of the two routes open
to b1. by hand, and confirmed on an exactly antisymmetric 4001-point grid of
[−1, 1], the grid being built by mirroring [0, 1] because definition 3.1(1)
compares x with −x and np.linspace(−1, 1, n) is not bitwise antisymmetric:

    phi   optimal, 3.1(2)     weak optimal, 3.1(3)   strong or strict, 3.1(1)
    lu    the whole box       the whole box          {0}
    ls    the whole box       the whole box          {0}
    cw    {0}                 the whole box          {0}

the arguments, which the grid confirms rather than replaces:

    phi_lu. x dominates y only if −|x| ⩽ −|y| and |x| ⩽ |y|, that is |x| ⩾ |y| and
        |x| ⩽ |y|, so |x| = |y|, and then all four image coordinates are equal and
        no component is strict. no point dominates any other, so the optimal set is
        all of S. for x̄ ≠ 0 the point −x̄ has F(−x̄) = F(x̄) componentwise, so
        F(−x̄) ≦_φ F(x̄) and x̄ is not a strong or strict optimal solution; at
        x̄ = 0 there is no such partner and |x| ⩽ 0 forces x = 0, so 0 is.
    phi_ls. the same argument with B_1^T f = 2|x| in place of |x|.
    phi_cw. x dominates y exactly when |x| < |y|, the first coordinate being
        constant and the other three all minimised at 0, so the optimal set is
        {0}, and it is the strong or strict optimal set too.

### 7.4 p0's status, stated plainly

the anchor is derivable and the sets are not, under the optimality conditions.
more precisely:

    what can be derived from the published optimality conditions: that x = 0 is an
    optimal solution for (1MIOP_φ) under all three phi, by example 3.8 statement 3
    and, with strictly positive weights, statement 2. that is the whole of it.

    what cannot: the efficient set under any phi. under phi_lu and phi_ls the
    hypothesis of every set-characterising statement fails, F not being phi-convex.
    under phi_cw every hypothesis holds away from x = 0 and the statements are
    vacuous, the first image coordinate being identically zero.

    what definition 3.1 gives directly, which is [1]'s own definition and not a new
    condition: the table in 7.3.

**so p0 is not a fixture in the sense b2 needs.** under phi_lu and phi_ls its
optimal set is the entire decision box, so a reference front there is the image of
the whole box and igd against it measures nothing about a solver's ability to find
an efficient set. under phi_cw the optimal set is the single point {0}, which is a
reference front of one point and is the published anchor itself. what p0 supports
is a smoke test: does a solver find x = 0, which every phi agrees is optimal and
which under phi_cw is the entire answer. that is a useful gate and it is what
CONTEXT.md section 10 c3 can ask of p0. p1 is the fixture.

on p-06, which is not resolved here. what this derivation can say: at x = 0 under
phi_lu, definition 3.1(1) is satisfied, verified directly from the definition and
from the relation ≦_φ of equation (3), and so are 3.1(2) and 3.1(3) by the
implication chain. so the paper's phrase "a strict minimum" describes a point at
which all three of definition 3.1's concepts hold, and no reading of the phrase
among the three is contradicted by the problem. what this derivation cannot say:
which of the three [1] meant. that is a question about the authors' sentence, a0
found no sentence of [1] joining the two vocabularies, and no result of [1] in
scope concludes definition 3.1(1) at all, theorem 3.1 covering the optimal and
weak cases only and examples 3.8 and 3.9 concluding only optimality and weak
optimality. **p-06 stays open and this document does not narrow it.**

one further note, recorded because it bounds what the direct route rests on. r-02
records that [9] of [1], where the relations ≦_{φ_i}, ≤_{φ_i} and <_{φ_i} on C are
defined, is not in scope. section 7.3 uses them only through equation (3), which
states ≦_{φ_i} fully as the componentwise order on the image pair, and through
(6) and (7), which build ≤_φ and <_φ from it. reading (6)'s per-objective strict
relation as "both image coordinates ⩽ with at least one strict" makes ≤_φ the
ordinary pareto relation on the 2m coordinates, which is what the project uses
everywhere and what pymoo implements. that reading is not transcribed from [9] and
is recorded here as the one place p0's direct derivation reaches past (3).


## 8. what b2 takes from this

    the map x(w), section 2.2, for all three phi on p1. it is a closed-form
        rational function of the weight vector and needs no root-finding.
    the closed-form regions X_lu, X_ls and X_cw, section 2.4, for sampling the set
        directly and for testing membership of a candidate point.
    the witnessing weights: every point of the derived set carries the w that
        produced it, which is what CONTEXT.md section 10 b2's first test needs.
    the singular weight set, section 2.3, which b2 must exclude from a weight
        sample or handle as a line rather than a point. a dirichlet or uniform
        sample of the simplex hits it with probability zero, but a structured
        sample over a lattice of weights hits it exactly, as section 2.4's
        denominator-40 grid did, 2 of 12341 for phi_ls and phi_cw.
    the boundary caveat of section 2.6: the two singular segments are in the
        closure of the derived set and the published conditions do not certify
        them as optimal. b2 should sample the open set, which is what x(w) over
        non-singular weights produces on its own.
    for p0, nothing that is a reference front. section 7.4.

CONTEXT.md section 10 b2's second test, that no point of a dense random sample
dominates any point of the reference front, is exactly the test section 3.1 ran
here and passed with 0 of 20000 under every phi, so it is expected to pass in b2
by construction. that is the test that catches a wrong derivation and it is worth
keeping for the same reason it passed here.


## 9. open items this session raises or touches

    s-01, equation (16)'s inconsistent weight subscripts. untouched. (16) was not
        used; (15) was expanded from the definitions of Λ_i and B_i, as a0
        instructed. the row costs nothing until the memoria cites (16).
    s-02, example 3.9's weight phrase. **evidence added**, section 6: p1 supplies
        a point at which reading two would make statement 1 false. the row stays
        open and now carries a witness. no result of this session depends on the
        answer, because every optimality conclusion is drawn from example 3.8.
    s-03, the printed definition of efficient solution for problem (12). touched
        and not settled. the derived sets of section 2 are the same under both
        readings, because the two differ only on distinct decision vectors sharing
        an image, and section 2.6's route through example 3.8 statement 3 produces
        points that are unique minimisers of a strictly convex function and
        therefore have no image-sharing partner. p0 under phi_lu and phi_ls is the
        opposite case and is where the reading bites: every x and −x share an
        image there, which is exactly why the optimal set is the whole box and the
        strong or strict set is {0}. the row is for b2 as recorded.
    s-08, the band rather than a curve, and whether b1 produces a map. **answered
        as expected**: section 2.2 is the map, section 2.4 the region, and no
        bounding box was needed.
    s-11, the containment. untouched and not used. section 5 tested the derived
        forms against it as an independent check and they agree; that is a check on
        this derivation, not evidence for the containment, and nothing here is
        built on it.
    p-05, [10]'s theorem numbering. **widened in fact and unchanged in status**.
        section 1.3 needed the midpoint-radius regularity criterion and cites it as
        "theorem 34" from the literature/ summary with the number unverified. the
        paper is still wanted.
        [**closed in lit-review, 2026-09-05, and this paragraph is left as written
        because it is a record of b1's state.** [10] is in papers/ and the number
        is right: theorem 34, printed page 13, verbatim as section 1.3 quotes it.
        one wording correction and none to the result: section 1.3's gloss of
        abs-differentiability is [10]'s **proposition 32, printed page 12**, not
        its definition 30, and proposition 32's second sentence covers
        **non-negative** radii including their zeros, which is wider than the
        strictly-positive-radius condition section 1.3 leans on and is what part 2
        needs. docs/part2/lit_review.md sections 3.1, 3.2 and 3.4.]
    p-06, the "strict minimum". untouched, section 7.4 states what the derivation
        can and cannot say.
    r-02, the relations on C defined in [1]'s own [9]. touched by section 7.3's
        direct route, which reads (6)'s per-objective strict relation at the level
        of R^2. recorded at the end of section 7.4.
    r-04, example 3.9's hypotheses failing at p0's anchor. **realised and
        mitigated**. the failure is confirmed and is wider than the row states,
        holding under all three phi and not only phi_lu, and the mitigation the row
        names, example 3.8, reaches the anchor under all three. the row can retire
        with that reasoning.

no source read in this session refutes anything in CONTEXT.md, so CONTEXT.md is
unchanged.


## 10. summary table

per problem and per phi, with "closes" meaning the derivation reaches a
characterisation of the efficient set from the published results as they stand.

    problem  phi   convexity  regularity     x(w)        singular w   interior  closes
    p1       lu    yes        yes, trivial   section 2.2  none         yes       yes, fully
    p1       ls    yes        yes, trivial   section 2.2  two rays     yes       yes, up to
                                                                                two segments
    p1       cw    yes        yes, trivial   section 2.2  two rays     yes       yes, up to
                                                                                two segments
    p0       lu    no         fails at 0     n/a          n/a          n/a       no, anchor only
    p0       ls    no         fails at 0     n/a          n/a          n/a       no, anchor only
    p0       cw    yes        fails at 0     n/a          n/a          n/a       no, conditions
                                                                                vacuous

the one phi for which the conditions do not close in the sense the brief asks
about, that is where a hypothesis fails outright, is **p0 under phi_lu and under
phi_ls**, where theorem 3.3 refuses phi-convexity and every set-characterising
statement of examples 3.8 and 3.9 goes with it. **p0 under phi_cw** closes on
hypotheses and fails on content, the conditions holding and saying nothing. **p1
closes under all three phi**, with the single reservation of section 2.6, the two
singular segments on which the published conditions give weak optimality and no
optimality verdict.
