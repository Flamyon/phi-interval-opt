# f7: I-VU2, the interchange derived, and the boundary of the transformation approach

session f7, 2026-09-06. **paper and pencil with symbolic verification. no module,
no run, no code beyond the algebra, nothing from [16] implemented, and nothing
added under src/ or tests/.** every script was a throwaway in the session
scratchpad and used exact rational arithmetic from `fractions`, the standard
library, sympy not being in the venv and CONTEXT.md section 11 not permitting a
dependency added for one session -- the same constraint b1, f2 and f5 worked
under. this is docs/part1/b1_phi_efficient_sets.md's method applied to the one
problem in [16]'s appendix A whose boundary functions interchange and which is not
disqualified on other grounds, docs/part2/f5_boundary_interchange.md section 5.

sources read in this session:

    papers/Newton Method for Multiobjective Optimization Problems of
        Interval-Valued Maps.pdf, [16]: appendix A problem 2, printed page 28;
        section 2.1's operations display and definitions 2.1 and 2.2, printed
        page 4; the gH-gradient, printed pages 5 and 6; definitions 2.16 to 2.19
        and proposition 2.1, printed page 7; Table 3, printed page 23; Figure 3,
        printed page 24; the conclusion's validity condition, printed page 27.
    papers/1-New preference order relationships and their application to
        multiobjective interval and fuzzy interval optimization problems.pdf, [1]:
        the order relations (3), (6) and (7), printed pages 3 and 4; definition
        2.2, proposition 2.3, corollary 2.1 and remark 2.2, printed page 5;
        definition 3.1, printed page 6; **examples 3.4 to 3.7, printed pages 7 and
        8**, which are what settles part 1; theorem 3.3, printed page 9; examples
        3.8 and 3.9 with condition (15), printed page 10.
    docs/part2/f5_boundary_interchange.md, all of it, sections 4 and 5 in
        particular.
    docs/part2/f2_ibk1_derivation.md, as the model, in full.
    docs/part1/b1_phi_efficient_sets.md sections 0, 1.2, 1.5, 2.1 to 2.6, for the
        method and for p0's failure.
    docs/part1/part1_closing.md sections 3.4, 5.1, 6.1 and 7.2.
    docs/part1/a_close_containment.md section 1, for the containment criterion.
    docs/part1/a0_framework.md c10, c12, c13, c14.
    src/interval_math.py and src/phi_transforms.py, for the arithmetic the
        verification runs through.

every theorem, example, definition and equation below is cited by number and
printed page. **no condition is invented, extended or weakened anywhere in what
follows**, and where a published result is applied to a restricted feasible set
that is said in the place it is done, with the one set-theoretic lemma that makes
the restriction legitimate written out in section 3.3.


## 0. the headline, in five lines, three of which are negatives

**s-14 is settled from the printed text and it is settled in the direction b1
read it.** [1] defines both a global and a pointwise phi-convexity in its
definition 2.2, printed page 5, uses the pointwise one four times in examples 3.4
to 3.7, printed pages 7 and 8, and uses the global one in example 3.9, printed
page 10. the distinction is the paper's own and example 3.9 chose the global side
of it. section 1.

**and the answer changes nothing on I-VU2**, which is not what f5 expected. under
the pointwise reading F is phi_lu-convex and phi_ls-convex at exactly one point of
the box, the origin -- and the origin is the one point where example 3.9's
*differentiability* hypothesis fails independently. so **under either reading,
example 3.9's statements 2 and 3 are unavailable at every point of I-VU2's box
under phi_lu and phi_ls.** section 1.6.

**the derivation closes under phi_lu and does not close under phi_ls or phi_cw**,
and the reason is not the crossing. it is a **singular weight ray** -- `w`
proportional to `(1, 3, 0, 0)` under phi_ls and to `(1, 5, 0, 0)` under phi_cw --
on which the scalarised objective is *constant* on the quadrant where the whole
answer lives, so condition (15) holds at every point of it and example 3.8
statement 4 cannot bound the optimal set below that quadrant. **that is
docs/part1/b1_phi_efficient_sets.md section 2.3's phenomenon exactly, on a
published problem**, and s-12's gap recurring. sections 3.5 and 3.8.

**the crossing's own failure is in the necessary condition and it is exhibited
rather than asserted.** the candidate set condition (15) produces on the open
quadrants is the open segment `{(t, t/2) : −4 < t < 0}`; the origin is its limit
point and is not in it, because at the origin the first expression of (15) is
undefined under all three phi. **the origin is nevertheless a strong optimal
solution under all three phi, by definition 3.1(1) of [1] printed page 6, proved
directly in section 5 with no differentiability and no convexity.** a point whose
efficiency is provable while the machinery for finding it does not apply is the
statement this session exists to make.

**and I-VU2 fails criterion 3 of the part 2 gate, exactly rather than by sample.**
the three phi-efficient sets are **equal**, to each other and to the crisp
centre problem's, and the reason is the interchange itself: on the quadrant where
the answer lives the crossing turns `r_1 = ¼(|x_1|+|x_2|)` into
`r_1 = (1 − c_1)/5`, an exact affine function of the centre with **negative**
slope, which is part1_closing section 6.1's degeneracy in its saturating form.
**f5 recorded G_1 as non-degenerate, and on the box it is; where the answer is, it
is not.** section 6.


## 1. s-14, settled

### 1.1 the two notions [1] defines, and the page they are on

**definition 2.2 of [1], printed page 5**, transcribed here from the paper:

> **Definition 2.2.** Let ≦_φ be the preference order relation given by (3) and
> let F : S ⊆ ℝⁿ → (C)^m be a multi-interval-valued function. F is said to be
> **φ-convex** if
>
>     F(tx + (1−t)y) ≦_φ t ⊡ F(x) ⊞ (1−t) ⊡ F(y)                          (8)
>
> for all x, y ∈ S and t ∈ (0,1). If there exists x* ∈ S such that
>
>     F(tx* + (1−t)y) ≦_φ t ⊡ F(x*) ⊞ (1−t) ⊡ F(y)                        (9)
>
> for all y ∈ S and t ∈ (0,1), then F is said to be **φ-convex at x***

so the two notions are **(8), quantified over both arguments and therefore over
the whole of S**, and **(9), quantified over one argument with the other pinned at
x***. they are given in one numbered definition, one display apart, and the paper
names them differently: "φ-convex" and "φ-convex at x*".

the two characterisations follow. **theorem 3.3, [1] printed page 9**, a0 c12,
v-12, characterises the global one:

> **Theorem 3.3.** ... Then F is φ-convex if and only if Λ_i^T f and B_i^T f are
> convex for all i ∈ {1, …, m}, where f = (f_1, f̄_1, …, f_m, f̄_m).

and **remark 2.2, [1] printed page 5**, a0 c12, v-13, characterises the pointwise
one, defining "convex at x*" for a real-valued function first:

> **Remark 2.2.** A real-valued function g : S ⊆ ℝⁿ → ℝ is said to be **convex at
> x*** ∈ S if g(tx* + (1−t)y) ⩽ t g(x*) + (1−t) g(y) for all y ∈ S and for all
> t ∈ (0,1). Consequently, given a multi-interval-valued function
> F : S ⊆ ℝⁿ → (C)^m, ... it follows that F is φ-convex at x* if and only if the
> real-valued functions [λ_{2i−1} f_i + λ_{2i} f̄_i] and [β_{2i−1} f_i + β_{2i} f̄_i]
> are convex at x* for all i ∈ {1, …, m}.

### 1.2 example 3.9 as printed

**[1] printed page 10**, transcribed from the paper, the hypotheses in bold being
the two this section is about:

> **Example 3.9 (Necessary and sufficient optimality conditions).** Given
> F : S ⊆ ℝⁿ → (C)^m such that F(x) = (F_1(x), …, F_m(x)) with
> F_i(x) = [f_i(x), f̄_i(x)] for all i ∈ {1, …, m}, **let Λ_i^T f, B_i^T f be
> differentiable for all i ∈ {1, …, m}** and 𝟎 = (0, …, 0) ∈ ℝⁿ. Thus,
>
> 1. If x̄ ∈ S is a weak optimal solution for (1MIOP_φ), then there are
>    w_1, …, w_2m ∈ ℝ, with w_i ⩾ 0 not equal zero for all i ∈ {1, …, 2m}, such
>    that (15).
> 2. If x̄ ∈ S, S is convex, **F is φ-convex** and there are w_1, …, w_2m ∈ ℝ,
>    with w_i ⩾ 0 not equal zero for all i ∈ {1, …, 2m}, such that (15) holds,
>    then x̄ is a weak optimal solution for (1MIOP_φ).
> 3. If x̄ ∈ S, S is convex, **F is φ-convex** and there are w_1, …, w_2m ∈ ℝ,
>    with w_i > 0 for all i ∈ {1, …, 2m}, such that (15) holds, then x̄ is an
>    optimal solution for (1MIOP_φ).

**"F is φ-convex", unqualified, is definition 2.2's (8).** the phrase "at x̄" does
not appear in either statement, and the preamble's differentiability carries no
"at x̄" either.

### 1.3 the paper's own contrast, and it is four sentences long

this would be a thin argument if [1] never used the pointwise form. **it uses it
four times, in the immediately preceding subsection, in statements of exactly the
same shape.** [1] section 3.1, "Optimality conditions for multiobjective interval
optimization problems with preference ordering relation", printed pages 7 and 8:

    example 3.4, printed page 7, part I of theorem 4.2 in [1]'s [31]
        "... where f_i, f̄_i : S → ℝ are **continuously differentiable at x̄** for
         all i ∈ {1, …, m}. **If F is φ-convex at x̄** and if there exist
         w_1, …, w_2m ∈ ℝ with w_i > 0 ... then x̄ is an optimal solution for
         (1MIOP_φ)."
    example 3.5, printed page 7, part II of the same theorem: same two phrases,
        verbatim, with phi_cw's coordinates in the stationarity condition.
    example 3.6, printed page 7, part III: same two phrases, verbatim.
    example 3.7, printed pages 7 and 8, theorem 4.3 in [1]'s [26]: same two
        phrases, verbatim, with phi_ls's coordinates.

so within four printed pages [1] writes "continuously differentiable **at x̄**" and
"F is φ-convex **at x̄**" four times each, and then writes "differentiable" and
"F is φ-convex" in example 3.9. **the two forms are both in the paper's active
vocabulary and example 3.9 uses the unqualified one.**

### 1.4 the verdict

**s-14 is answered, and it is answered against the weakening.** as printed,
example 3.9 statements 2 and 3 require **global** phi-convexity on S, definition
2.2's (8), characterised by theorem 3.3, which is what
docs/part1/b1_phi_efficient_sets.md section 1.2 and
docs/part2/f2_ibk1_derivation.md section 1.3 assumed and what
docs/part2/f5_boundary_interchange.md section 4.1 assumed. **b1's reading is the
printed one and it does not need defending.**

**this session does not weaken it and does not use the pointwise form anywhere**,
CONTEXT.md section 6's stopping rule. the elementary observation that the
pointwise hypothesis would suffice for statements 2 and 3 -- convexity at x̄ plus
stationarity at x̄ gives global minimality of the weighted sum on S by one limit --
is **not used below and is not asserted as the paper's meaning**. what remains for
the authors, and it is narrower than f5's s-14, is whether the omission of "at x̄"
in example 3.9 is deliberate given that the four preceding examples carry it.
**the project does not need the answer**, and section 1.6 is why.

### 1.5 the same question applies to the differentiability, and f5 did not ask it

example 3.9's preamble reads "let Λ_i^T f, B_i^T f **be differentiable** for all
i", unqualified, where examples 3.4 to 3.7 read "**continuously differentiable at
x̄**". **so the preamble is global on S too**, on exactly the reading of section
1.3. that hypothesis is a hypothesis of the whole example, statement 1 included.

**this matters more than the convexity does on I-VU2**, and it is why part 3 below
is organised the way it is. under the printed reading:

    **example 3.9 is unavailable on S = [−4, 4]² under all three phi**, because
        `|x_1|` and `|x_2|` enter every phi's image coordinates through the
        half-width and are not differentiable on the two axes, section 3.1.
        under phi_lu and phi_ls statements 2 and 3 are unavailable a second time,
        on the convexity.
    **it is available on each closed quadrant**, where the same functions are
        affine, and that is a legitimate application of the example to a
        different feasible set rather than a weakening of it. section 3.3 states
        the one lemma that makes the restriction useful and proves it.

### 1.6 what the answer costs on I-VU2, and why it costs nothing

f5 framed s-14 as deciding "whether one crossing point anywhere in the box costs
phi_lu and phi_ls their sufficiency over the whole box, or only on the locus".
**on I-VU2 the two readings give the same verdict**, and that is a fact about this
problem rather than a general one.

under the pointwise reading, statements 2 and 3 would be available at x̄ exactly
where F is phi-convex at x̄. for I-VU2, with `ℓ(t) := min(t, 3t/2)` the coefficient
function of section 2.3:

    **F is phi_lu-convex at x̄ and phi_ls-convex at x̄ if and only if x̄ = (0,0).**
        ℓ is positively homogeneous and ℓ(0) = 0, so at x̄ = 0 both sides of
        remark 2.2's inequality are `(1−t)(ℓ(y_1) + ℓ(y_2))` and it holds with
        equality. at any x̄ with x̄_1 ≠ 0, take `y = (−4, x̄_2)` if
        `x̄_1 > 0` and `y = (4, x̄_2)` otherwise, so that the second coordinate
        contributes the same term to both sides and cancels. at
        `t = 4/(|x̄_1| + 4)` the convex combination has first coordinate 0, where
        `ℓ = 0`, while the right-hand side's first-coordinate term is
        `−2|x̄_1|/(|x̄_1| + 4) < 0`. so the inequality fails. same construction in
        the second coordinate when `x̄_2 ≠ 0`.
    **F is phi_cw-convex at every x̄**, and globally, section 3.1.

and at x̄ = (0,0) the preamble's differentiability fails under all three phi and
condition (15) is not even well formed, section 4.1. **so the point the pointwise
reading would have bought is the one point where the rest of the example has
already failed.**

measured, as a check on the argument rather than a substitute for it, on 20000
random rational chords per point in exact rational arithmetic, a positive count
being a violation of remark 2.2's inequality:

    phi   x*        violations per image coordinate      phi-convex at x*
    lu    (0,0)     0, 0, 0, 0                           yes
    lu    (1,1)     15024, 0, 0, 0                       no
    lu    (−1,−1)   15036, 0, 0, 0                       no
    lu    (0,−1)    9903, 0, 0, 0                        no
    lu    (−2,−1)   14921, 0, 0, 0                       no
    ls    (0,0)     0, 0, 0, 0                           yes
    ls    (1,1)     15084, 0, 0, 0                       no
    ls    (−1,−1)   14948, 0, 0, 0                       no
    ls    (0,−1)    9984, 0, 0, 0                        no
    ls    (−2,−1)   14974, 0, 0, 0                       no
    cw    every point tested                             yes

the single violating coordinate is `Λ_1^T f = G̲_1` in every row, which is
docs/part1/b1_phi_efficient_sets.md section 1.5's p0 table with `−|x|` replaced by
a two-variable version of itself.

**conclusion for the memoria, and it is one sentence.** on I-VU2 the global reading
costs phi_lu and phi_ls example 3.9's sufficiency on the whole box and the
pointwise reading costs them all of it but one point, at which the example has
already failed on differentiability; so **the derivation below is written under the
printed global reading and would be unchanged under the other one.**


## 2. the problem as it is

### 2.1 the statement

problem 2 of appendix A, **[16] printed page 28**, transcribed from the paper this
session and matching docs/part2/lit_review.md section 1.8 and f5 section 3.5:

>     G_1(x_1, x_2) := [1, 1.5] ⊙ x_1 ⊕ [1, 1.5] ⊙ x_2 ⊕ [1, 1],
>     G_2(x_1, x_2) := [1, 1.5] ⊙ x_1²  ⊕  [2, 3] ⊙ x_2²  ⊖_gH  [1, 1],
>     lb^T = (−4, −4) and ub^T = (4, 4).

so `n = 2`, `m = 2`, `2m = 4` image columns, and `S` is the box `[−4, 4]²`.
**there is no printed solution point, no printed gH-gradient and no printed
Hessian for I-VU2 anywhere in [16]**, unlike I-BK1; section 7 says what that costs.

### 2.2 the product applied correctly

⊙ is item (iii) of the operations display of **[16] section 2.1, printed page 4**,
the locator f6 corrected: `S ⊙ T` is the minimum and the maximum over the four
endpoint products. `multiply_by_real` in `src/interval_math.py` is that operation
at `T = [h, h]`, f6, and for one interval coefficient on a real function it gives,
with `m = (a+b)/2` and `w = (b−a)/2`,

    [a, b] ⊙ h  =  [ m h − w|h| ,  m h + w|h| ]

so the centre of a Minkowski sum of such terms stays as smooth as the `h_j` are and
**the half-width picks up an absolute value per sign-changing term**, which is
f5 section 4.1's line.

⊖_gH is definition 2.1 of [16], printed page 4, and `gh_difference` in
`src/interval_math.py`; against a degenerate `[1,1]` it is a real shift of the
centre leaving the half-width alone.

I-VU2's coefficients are `[1, 3/2]` on `x_1`, `x_2` and `x_1²`, `[2, 3]` on `x_2²`,
and the degenerate `[1,1]` twice. so

    c_1 = (5/4)(x_1 + x_2) + 1          r_1 = ¼(|x_1| + |x_2|)
    c_2 = (5/4)x_1² + (5/2)x_2² − 1     r_2 = ¼x_1² + ½x_2²

and, writing `v := x_1 + x_2`, `s := |x_1| + |x_2|` and **`U := x_1² + 2x_2²`**,

    **c_1 = (5/4)v + 1,  r_1 = s/4,  c_2 = (5/4)U − 1,  r_2 = U/4**

    **G̲_1 = (5/4)v − s/4 + 1     Ḡ_1 = (5/4)v + s/4 + 1**
    **G̲_2 = U − 1               Ḡ_2 = (3/2)U − 1**

**the whole of objective 2 is one scalar `U` dressed four ways.** `[1, 3/2]` on
`x_1²` and `[2, 3]` on `x_2²` have the same ratio of second coefficient to first,
`2/1 = 3/1.5 = 2`, so all four of objective 2's boundary and image functions are
*increasing affine functions of the single quantity `U`*. that one fact drives
sections 3.4, 6.1 and 6.4 and is stronger than the degeneracy f5 recorded.

verified against the project's own arithmetic: Moore's product and the Minkowski
sum built up in exact rationals term by term, against the closed forms above, at
4000 random rational points of the box, and the same through
`src/interval_math.py` in floating point:

    endpoints, Moore's product against the closed form: 0 mismatches of 4000
    src/interval_math.py against the closed form: max abs diff 1.421e-14

### 2.3 the endpoint functions piecewise, and the crossing locus

per coordinate, `[1, 3/2] ⊙ x_j` has lower endpoint `ℓ(x_j)` and upper endpoint
`u(x_j)` with

    ℓ(t) = min(t, (3/2)t) =  t     for t ⩾ 0,   (3/2)t  for t < 0
    u(t) = max(t, (3/2)t) = (3/2)t for t ⩾ 0,    t      for t < 0

so `G̲_1 = ℓ(x_1) + ℓ(x_2) + 1` and `Ḡ_1 = u(x_1) + u(x_2) + 1`, and written out
over the four closed quadrants:

    quadrant           G̲_1                       Ḡ_1
    x_1 ⩾ 0, x_2 ⩾ 0   x_1 + x_2 + 1              (3/2)(x_1 + x_2) + 1
    x_1 ⩾ 0, x_2 ⩽ 0   x_1 + (3/2)x_2 + 1         (3/2)x_1 + x_2 + 1
    x_1 ⩽ 0, x_2 ⩾ 0   (3/2)x_1 + x_2 + 1         x_1 + (3/2)x_2 + 1
    x_1 ⩽ 0, x_2 ⩽ 0   (3/2)(x_1 + x_2) + 1       x_1 + x_2 + 1

**the boundary functions interchange on `x_1 = 0` and on `x_2 = 0`.** on
`x_1 > 0` the lower endpoint of the first term comes from the coefficient `a = 1`
and on `x_1 < 0` from `b = 3/2`; the expression that gives the lower endpoint is
not fixed, which is [16]'s own reservation, printed page 27:

> Since G̲_i and Ḡ_i may interchange their position, it is very difficult to
> express the IVM G_i by G_i(x) := [G̲_i(x), Ḡ_i(x)] for all
> x ∈ {x ∈ ℝⁿ : lb ⩽ x ⩽ ub}.

**the crossing locus is the two lines `x_1 = 0` and `x_2 = 0`**, both running
through the interior of the box and meeting at the origin, which is interior. it
has codimension one, which is the general case and not a feature of this problem.
`G_2` has no interchange: `x_1²` and `x_2²` are non-negative, so the two coefficient
products never swap and both boundary functions are polynomials.

### 2.4 the well-ordering, and what the fixed order would have returned

`G̲_i ⩽ Ḡ_i` everywhere, `r_1 ⩾ 0` and `r_2 ⩾ 0` by construction, so the
`f_l ⩽ f_u` guard f6 put at the `Problem` boundary passes on I-VU2 at every point.
**under the fixed-order reading the project used before f6 it would not.** measured
in exact rationals at the same 4000 random points:

    ill ordered under Moore's product:            0 of 4000
    ill ordered under the fixed-order reading:  2071 of 4000

which is every sampled point with `x_1 + x_2 < 0`. **I-VU2 is the first problem the
project has looked at that would have exercised r-23**, and f6's fix is a
precondition of this session rather than an improvement to it; without it the
derivation below would have been of a different object on half its box.

### 2.5 f5's degeneracy check, confirmed and sharpened

**part1_closing section 6.1's condition** is a half-width that is an exact function
of its centre. f5 section 3.2 computes `ρ_j = w_j / m_j` per term from the printed
coefficients and calls the objective degenerate when `ρ` is one number across the
terms. for I-VU2 both objectives have `ρ_j = 1/5` on every term -- `¼ ÷ 5/4` on
`x_1`, `x_2` and `x_1²`, and `½ ÷ 5/2` on `x_2²` -- so under constant signs both
would be degenerate.

**`G_2` is degenerate, and neither constant nor proportional but affine:**

    **r_2 = (c_2 + 1)/5**,   slope 1/5 ∈ (0,1), positive

exactly as f5's ⊖gH table records it. `r_2` is not constant, `U` ranging over
`[0, 48]` on the box, and it is not proportional to `c_2`, the `⊖gH [1,1]` shifting
the centre by −1 and leaving the half-width alone.

**`G_1` is not degenerate on the box, and f5 is right about that** -- `x = (1,−1)`
and `x = (0,0)` both have `c_1 = 1` and have `r_1 = ½` and `r_1 = 0`, an exact
two-point witness that `r_1` is not a function of `c_1`. **and that is the wrong
statement for this problem, which is the sharpening this session adds.** on each of
the two aligned quadrants `s = ±v` and

    on x_1 ⩾ 0, x_2 ⩾ 0:   r_1 = v/4 = (c_1 − 1)/5     slope **+1/5**
    on x_1 ⩽ 0, x_2 ⩽ 0:   r_1 = −v/4 = (1 − c_1)/5    slope **−1/5**

so **`G_1` is degenerate on each aligned quadrant and non-degenerate only because
the two slopes disagree.** section 3 shows that the whole answer lives in the
quadrant where the slope is negative, and f5 section 3.2's own column algebra says
what a negative slope costs: phi_ls's and phi_cw's two columns of that objective
then move oppositely in `c`, so **no two points with distinct `c_1` are comparable
on objective 1 at all**. that is the saturation
docs/part1/a1_uncertainty_model.md part 4 measured on the linear zdt1 half-width,
occurring here because of the interchange and not because of a coefficient choice.
sections 3.5 and 6 are its consequences.

**correction recorded, and it does not reverse f5's verdict.** f5 section 3.5's
"`G_1` is **not** degenerate" is true of the box and false of the region the
efficient set occupies; f5's own degeneracy table row for `G_1`, computed under
constant signs, is exactly right on the first quadrant and has the wrong sign on
the third.

### 2.6 `G_2` is phi-blind, and what that costs the comparison

by section 2.2 all six image columns of objective 2, across the three phi, are
strictly increasing affine functions of `U`:

    phi_lu   G̲_2 = U − 1            Ḡ_2 = (3/2)U − 1
    phi_ls   G̲_2 = U − 1            2r_2 = U/2
    phi_cw   c_2 = (5/4)U − 1        r_2 = U/4

so **objective 2 orders any two points identically under all three phi**, and any
difference between the three efficient sets has to come from objective 1 alone.
that is f5 section 5.3's stated cost of choosing I-VU2 and it is confirmed here in
a stronger form than f5 stated it: not merely "phi-blind", but *a single scalar*,
so objective 2 contributes exactly one real number to the comparison at each point.

**what it costs.** half the problem carries no information about the choice of
order, and section 6 shows that the other half loses its information too, on the
region that matters, for the reason of section 2.5. the two costs compound and the
result is that **I-VU2 cannot separate the three orders at all**. that has to be
in the memoria as a property of the problem and not discovered in a table.

### 2.7 the image coordinates, piecewise, with their Hessians

with `Λ_i^T f = λ_{2i−1} f_i + λ_{2i} f̄_i` and `B_i^T f = β_{2i−1} f_i + β_{2i} f̄_i`
from theorem 3.3's proof, [1] printed page 9, and the three registry members as
a0 c6, c7 and c8:

    phi_lu, example 2.2 of [1], lambda = (1, 0), beta = (0, 1)
      g_1 = G̲_1 = (5/4)v − s/4 + 1      g_2 = Ḡ_1 = (5/4)v + s/4 + 1
      g_3 = G̲_2 = U − 1                 g_4 = Ḡ_2 = (3/2)U − 1

    phi_ls, example 2.3, lambda = (1, 0), beta = (−1, 1)
      g_1 = G̲_1, as above               g_2 = 2r_1 = s/2
      g_3 = G̲_2 = U − 1                 g_4 = 2r_2 = U/2

    phi_cw, example 2.4, lambda = (1/2, 1/2), beta = (−1/2, 1/2)
      g_1 = c_1 = (5/4)v + 1            g_2 = r_1 = s/4
      g_3 = c_2 = (5/4)U − 1            g_4 = r_2 = U/4

verified against `src/phi_transforms.py` at the same 4000 points, the endpoints
coming from `src/interval_math.py`: max abs diff `1.421e-14`, `1.066e-14` and
`7.105e-15` for phi_lu, phi_ls and phi_cw.

**piecewise, on the closed quadrant `Q_σ` with `σ = (σ_1, σ_2) ∈ {+,−}²`**, where
`|x_j| = σ_j x_j`, every one of the twelve is an affine function plus a diagonal
quadratic in `U`, and the Hessians are constant on each quadrant:

    phi   coordinate   on Q_σ                                    Hessian on Q_σ
    lu    g_1 = G̲_1   Σ_j (5/4 − σ_j/4) x_j + 1                 0
    lu    g_2 = Ḡ_1   Σ_j (5/4 + σ_j/4) x_j + 1                 0
    lu    g_3 = G̲_2   U − 1                                     diag(2, 4)
    lu    g_4 = Ḡ_2   (3/2)U − 1                                diag(3, 6)
    ls    g_1 = G̲_1   as above                                  0
    ls    g_2 = 2r_1   Σ_j (σ_j/2) x_j                           0
    ls    g_3 = G̲_2   U − 1                                     diag(2, 4)
    ls    g_4 = 2r_2   U/2                                       diag(1, 2)
    cw    g_1 = c_1    (5/4)(x_1 + x_2) + 1                      0
    cw    g_2 = r_1    Σ_j (σ_j/4) x_j                           0
    cw    g_3 = c_2    (5/4)U − 1                                diag(5/2, 5)
    cw    g_4 = r_2    U/4                                       diag(1/2, 1)

**two structural facts, and everything below is one of their consequences.**

    **every objective-1 column is affine on each quadrant**, so it contributes a
        constant gradient to condition (15) and no curvature at all. that is what
        makes a singular weight possible, section 3.5.
    **every objective-2 Hessian is `κ·diag(2, 4)` for a positive `κ`**, the second
        diagonal entry exactly twice the first, because both endpoints of both
        coefficients share the ratio 2. so `Σ_k w_k H_k = diag(2κ, 4κ)` for every
        weight vector under every phi, and the candidate curve is the same one
        under all three orders, section 3.4.


## 3. the derivation

### 3.1 the hypotheses on the box, per phi

**theorem 3.3, [1] printed page 9, on S = [−4,4]².** `ℓ` is a minimum of two linear
functions, hence concave with a strict kink at 0, so `G̲_1 = ℓ(x_1) + ℓ(x_2) + 1` is
concave and not convex; `u` is a maximum of two linear functions, so `Ḡ_1` is
convex; `s` is convex, `c_1` is affine, and `U` is a positive definite quadratic
form so `G̲_2`, `Ḡ_2`, `2r_2`, `c_2` and `r_2` are convex. hence

    phi   coordinate   convex on S                verdict by theorem 3.3
    lu    G̲_1         **no**, concave            **F is not phi_lu-convex**
    lu    Ḡ_1         yes
    lu    G̲_2, Ḡ_2   yes
    ls    G̲_1         **no**, concave            **F is not phi_ls-convex**
    ls    2r_1         yes
    ls    G̲_2, 2r_2   yes
    cw    c_1          yes, affine                **F is phi_cw-convex**
    cw    r_1          yes
    cw    c_2, r_2     yes

measured on 40000 random rational chords per phi, a positive count being a
violation of the convexity inequality:

    phi_lu  violations per column: 29958, 0, 0, 0   ->  F is NOT phi_lu-convex
    phi_ls  violations per column: 29937, 0, 0, 0   ->  F is NOT phi_ls-convex
    phi_cw  violations per column:     0, 0, 0, 0   ->  F is phi_cw-convex

**this is f5 section 4.1's predicted split and it is confirmed**: phi_cw keeps
theorem 3.3 where phi_lu and phi_ls lose it, because under phi_cw the coordinate
that carries the interchange is the half-width, which is a *sum of absolute
values* and therefore convex, while under the other two it is the lower endpoint,
which is a *sum of minima* and therefore concave. **section 3.8 shows that keeping
it does not help.**

**example 3.9's differentiability preamble, on S.** `|x_1|` and `|x_2|` have no
derivative where their argument vanishes and the gradient of the argument is
non-zero. every phi carries them:

    phi_lu   G̲_1 and Ḡ_1 both non-differentiable on x_1 = 0 and on x_2 = 0
    phi_ls   G̲_1 and 2r_1 both non-differentiable on the same two lines
    phi_cw   c_1 is affine and smooth; **r_1 is not differentiable** on either line

so the preamble fails on the two axes under all three phi. **since every φ_i is
invertible**, [1]'s admissibility condition being a non-zero determinant, v-02,
**differentiability of the two image coordinates is equivalent to differentiability
of the two boundary functions for every admissible φ**, a0 c14, so no choice of
order removes it. that is the same argument b1 section 1.5 makes for p0 and
disagreement d-b records.

**by section 1.5 the preamble is a hypothesis on S, so example 3.9 as printed is
unavailable on the whole box under all three phi.** it is available on each closed
quadrant, section 3.3.

**example 3.8, [1] printed page 10**, a0 c13. statements 1, 2 and 3 carry **no
hypothesis at all** beyond the standing weight condition -- no convexity, no
differentiability -- and statement 4 needs `S` convex and `F` phi-convex. so
statements 1, 2 and 3 are available on the whole box under all three phi, and
statement 4 is available on the whole box under **phi_cw only**, by the table
above. **that asymmetry is what the derivation runs on.**

### 3.2 regularity, by [10] proposition 32 and theorem 34

**proposition 32**, [10] printed page 12, and **theorem 34**, [10] printed page 13,
both transcribed in docs/part2/lit_review.md section 3.2 and used in
docs/part2/f2_ibk1_derivation.md section 1.4:

> **Proposition 32.** If f : K ⊆ ℝⁿ → ℝ is such that its absolute value |f| is
> Fréchet differentiable at x⁽⁰⁾ ∈ K ..., then f is abs-differentiable at x⁽⁰⁾ ...
> In particular, if f : K ⊆ ℝⁿ → ℝ⁺ ∪ {0} is differentiable then it is also
> abs-differentiable.
>
> **Theorem 34.** The IV-function 𝙵(x) = (f̂(x); f̃(x)) is Fréchet gH-differentiable
> at x⁽⁰⁾ ∈ K if and only if f̂ and f̃ are (respectively) Fréchet differentiable and
> abs-differentiable at x⁽⁰⁾.

    objective 2: `c_2` and `r_2` are polynomials, `r_2 = U/4 ⩾ 0` with equality
        only at the origin. proposition 32's second sentence covers the zero, so
        `r_2` is abs-differentiable everywhere and by theorem 34 **`G_2` is
        gH-differentiable at every point of ℝ²**. this is f2 section 1.4's payoff
        recurring: under a1's strict-positivity rule there would have been a hole
        at the origin, which is a point of every answer below.
    objective 1: `c_1` is affine and differentiable everywhere; `r_1 = s/4 ⩾ 0`
        and `|r_1| = r_1` has **no** classical derivative on `x_1 = 0` or
        `x_2 = 0`. **proposition 32 does not apply there** -- its hypothesis is
        differentiability of `f`, which is what fails -- and by theorem 34
        **`G_1` is gH-differentiable exactly off the two axes**.

so **F is Fréchet gH-differentiable on `[−4,4]² ∖ (the two axes)` and at no point
of the axes**, which is the same locus example 3.9's own hypothesis fails on and
reaches it by a different route. as on I-BK1 the [10] reading is not load-bearing
for the hypothesis check -- example 3.9 states differentiability of the image
coordinates and that is decided by inspection -- and it is what licenses calling F
gH-differentiable, which is the language [16] states its own problem in.

### 3.3 the restriction to a quadrant, and the one lemma it needs

**what is done.** for each closed quadrant `Q_σ = {x ∈ S : σ_j x_j ⩾ 0}` the
problem `(1MIOP_φ)` with feasible set `Q_σ` is an instance of [1]'s own
formulation, definition 3.1 being stated for an arbitrary `S ⊆ ℝⁿ`. on `Q_σ` all
twelve image coordinates agree with polynomials of degree at most two, section 2.7,
so they are differentiable; `Q_σ` is convex; and every one of them is convex there,
the objective-1 columns being affine and the objective-2 columns positive
semidefinite quadratics. **so all three statements of example 3.9 and all four of
example 3.8 are available on `Q_σ`, under all three phi, with no hypothesis
weakened.**

**what that is worth, and it is only worth this.** conclusions drawn on `Q_σ` are
about `(1MIOP_φ)` with feasible set `Q_σ`, not about the box. the transfer runs one
way and the lemma is one line.

> **lemma (restriction).** let `Q ⊆ S` and `x̄ ∈ Q`. if `x̄` is a weak optimal
> solution of `(1MIOP_φ)` on `S` then it is a weak optimal solution on `Q`; and if
> it is an optimal solution on `S` it is an optimal solution on `Q`.
>
> *proof.* definition 3.1(3), [1] printed page 6, asks that no `x ∈ S ∖ {x̄}` have
> `F(x) <_φ F(x̄)`. every `x ∈ Q ∖ {x̄}` is such an `x`, so the condition on `Q` is
> implied by the condition on `S`. definition 3.1(2) with `≤_φ` in place of `<_φ`,
> identically. ∎

**so the necessary direction transfers downward and the sufficient direction does
not.** a point of `Q` shown non-candidate on `Q` is non-candidate on `S`; a point
of `Q` shown optimal on `Q` is *not* thereby optimal on `S`. sufficiency on the box
is taken from example 3.8 statements 1 and 3 instead, which need no restriction,
section 3.7.

**and three of the four quadrants are disposed of before any of this**, by a
domination argument that uses definition 3.1 and nothing else -- the analogue of
f2 section 2.5's projection argument.

> **lemma (projection).** for `x ∈ S` write `x⁻ := (min(x_1, 0), min(x_2, 0))`.
> then `x⁻ ∈ S`, and if `x ≠ x⁻` every one of the four image coordinates is
> **strictly** smaller at `x⁻` than at `x`, under all three phi.
>
> *proof.* `ℓ(min(t,0)) ⩽ ℓ(t)` and `u(min(t,0)) ⩽ u(t)`, strictly when `t > 0`,
> since `ℓ(t) = t > 0 = ℓ(0)` and `u(t) = (3/2)t > 0 = u(0)` there; and
> `|min(t,0)| ⩽ |t|` and `min(t,0)² ⩽ t²`, strictly when `t > 0`. every image
> coordinate is a sum of terms of those four kinds with non-negative weights and
> at least one of them strict. ∎

verified in exact rational arithmetic at 14868 random points of `S` outside
`[−4,0]²`: **0 failures, under each of the three phi.**

so **no point of `S ∖ [−4,0]²` is weakly optimal under any phi**, by definition
3.1(3) directly, and the whole answer lies in the closed third quadrant
`Q := [−4, 0]²`. everything below is on `Q`.

### 3.4 condition (15) on the quadrant

condition (15), [1] printed page 10, is stationarity of `Σ_k w_k g_k`, which b1
section 0 confirmed from the definitions of `Λ_i` and `B_i` and a0 c14 records;
the index convention is example 3.8's, `w_1` on `Λ_1^T f`, `w_2` on `B_1^T f`,
`w_3` on `Λ_2^T f`, `w_4` on `B_2^T f`.

on `Q` every image coordinate is `A·x + κ_k U + const` with a constant gradient
`A_k` from objective 1 and a multiple of `∇U = (2x_1, 4x_2)` from objective 2,
section 2.7. so (15) is

    **A_1(w) + 2κ(w) x_1 = 0        A_2(w) + 4κ(w) x_2 = 0**                (f7-1)

with, on `Q`,

    phi_lu   A_1 = A_2 = P_lu := (3/2)w_1 + w_2        κ = w_3 + (3/2)w_4
    phi_ls   A_1 = A_2 = P_ls := (3/2)w_1 − (1/2)w_2   κ = w_3 + (1/2)w_4
    phi_cw   A_1 = A_2 = P_cw := (5/4)w_1 − (1/4)w_2   κ = (5/4)w_3 + (1/4)w_4

**`A_1 = A_2` under all three phi**, because on `Q` both variables carry the same
coefficient in every objective-1 column, and **the two equations differ only by the
factor 2 in the second**, because objective 2's aspect ratio is 2 in every column.
so wherever `κ > 0`,

    **x_1(w) = − P/(2κ),      x_2(w) = − P/(4κ) = x_1(w)/2**

**the candidate curve is `x_2 = x_1/2` under all three phi**, and the three orders
differ only in which `P` they put in the numerator.

verified in exact rational arithmetic on 4000 random non-negative integer weight
vectors per phi, by substituting `x(w)` back into the gradient of `Σ_k w_k g_k`:

    phi_lu: 3914 weights with x(w) in the quadrant, gradient non-zero 0, x_2 ≠ x_1/2 0
    phi_ls: 3231 weights with x(w) in the quadrant, gradient non-zero 0, x_2 ≠ x_1/2 0
    phi_cw: 3324 weights with x(w) in the quadrant, gradient non-zero 0, x_2 ≠ x_1/2 0

exactly zero, not approximately: the arithmetic was rational throughout. the
remaining weights put `x(w)` outside the box and are not candidates.

**and the other three quadrants carry no interior candidate.** on `Q_σ` the
objective-1 coefficient of `x_j` in `G̲_1` is 1 or 3/2 and in `Ḡ_1` is 3/2 or 1, all
strictly positive, and in `2r_1` and `r_1` it is `σ_j/2` and `σ_j/4`. working
(f7-1) out per quadrant, a solution consistent with `σ_j x_j ⩾ 0` and interior
requires `A_j` to vanish, which under every phi forces `w_1 = w_2 = 0` and then
`x = 0`, a corner of the quadrant and a point of the locus. **so the interior of
`Q_++`, `Q_+−` and `Q_−+` contains no candidate under any phi**, which is section
3.3's projection lemma recovered from the stationarity condition.

### 3.5 the singular weight directions, characterised

`Σ_k w_k H_k = diag(2κ, 4κ)` fails to be invertible exactly when `κ(w) = 0`, and
since every objective-2 coefficient is strictly positive that means
**`w_3 = w_4 = 0`**. (f7-1) then reads `A_1(w) = A_2(w) = 0`, a condition on
`(w_1, w_2) ⩾ 0`:

    phi   quadrant   A_1(w) = A_2(w)                  singular and consistent
    lu    Q          (3/2)w_1 + w_2                   **none**: both coefficients
                                                      positive, so A = 0 forces w = 0
    ls    Q          (3/2)w_1 − (1/2)w_2              **the ray w ∝ (1, 3, 0, 0)**
    cw    Q          (5/4)w_1 − (1/4)w_2              **the ray w ∝ (1, 5, 0, 0)**

and on the three other quadrants no phi has one, the enumeration being the same
and the coefficients there all positive.

**on the singular ray (15) holds at every point of `Q`**, both sides of both
equations being identically zero, so the candidate set the necessary condition
produces is the whole quadrant. verified: at `w = (1,3,0,0)` under phi_ls and
`w = (1,5,0,0)` under phi_cw, the scalarised objective `Σ_k w_k g_k` takes
**exactly one value** over 6000 random rational points of `Q` -- it is constant --
and is **strictly larger at every one of 4488 and 4524 sampled points outside `Q`**.

**this is docs/part1/b1_phi_efficient_sets.md section 2.3's phenomenon, on a
problem the project did not construct, and it is worse here.** on p1 the singular
rays were the weight vectors putting all their mass on a single width coordinate
and each produced a *line* of solutions; here the ray mixes two columns of the
same objective and produces a *two-dimensional region*. and the mechanism is
different: on p1 it was a width coordinate depending on one variable, here it is
section 2.5's negative-slope degeneracy, `r_1 = (1 − c_1)/5` on `Q`, which makes
the two combinations the rays name **constant** there:
`c_1 + 5 r_1 = ((5/4)v + 1) + 5(−v/4) = 1` under phi_cw and
`G̲_1 + 3(2r_1) = ((3/2)v + 1) + 3(−v/2) = 1` under phi_ls. **the crossing produced the degeneracy and the degeneracy
produced the singular ray.**

**phi_lu has no singular ray** because its two objective-1 columns are `G̲_1` and
`Ḡ_1`, both *increasing* in `v` on `Q`, so no non-negative combination of them is
constant. that is the whole of the asymmetry in section 3.8.

### 3.6 the candidate set from (15)

collecting sections 3.3 to 3.5, and applying example 3.9 statement 1 on `Q` to a
weak optimal point of the box that lies in `Q` -- legitimate by the restriction
lemma -- with the interiority reading of b1 section 1.4 and f2 section 1.5, which
confines (15) to points interior to the feasible set it is applied on:

    **phi_lu**   candidates in int Q: the open segment
                 **{ (t, t/2) : −4 < t < 0 }**. `t = −P_lu/(2κ)` sweeps
                 `(−∞, 0)` as `P_lu/κ` sweeps `(0, ∞)`, and a candidate has to lie
                 in `S`, which cuts it to `[−4, 0)`; `t = −4` is on a face of the
                 box and outside int S. **the origin is not in it**, `P_lu = 0`
                 forcing `w_1 = w_2 = 0` and with it `κ > 0` and `x = 0`, a point
                 of the locus at which (15) is not defined, section 4.1.
    **phi_ls**   the same open segment from the regular weights, **and the whole
                 of `Q` from the singular ray**. the candidate set is `Q`.
    **phi_cw**   identically: the same segment, and the whole of `Q`.

### 3.7 the scalarised problem, and what example 3.8 gives on the whole box

example 3.8's statements need no restriction, so this is done on `S = [−4,4]²`.
the scalarised objective is **separable**, which is what makes its global minimiser
available in closed form despite the kinks:

    **Σ_k w_k g_k(x) = f(x_1 ; κ) + f(x_2 ; 2κ) + const**,
    with **f(t ; k) = P t + k t² for t ⩽ 0** and **f(t ; k) = N t + k t² for t ⩾ 0**

where `P` is section 3.4's and `N` is its companion on the non-negative side,

    phi_lu   N_lu = w_1 + (3/2)w_2      phi_ls   N_ls = w_1 + (1/2)w_2
    phi_cw   N_cw = (5/4)w_1 + (1/4)w_2

and **`N ⩾ 0` under all three phi**, with `N = 0` only when `w_1 = w_2 = 0`.
verified: 0 mismatches over 12000 random (weight, point) pairs across the three
phi, in exact rationals.

minimising `f(· ; k)` over `[−4, 4]`: for `k > 0` the non-negative branch is
increasing, so the minimum is at `max(−4, −P/(2k))` when `P > 0` and at `0` when
`P ⩽ 0`, and it is **unique** in every case; for `k = 0` it is at `−4` when
`P > 0`, at `0` when `P < 0`, and the whole of `[−4, 0]` when `P = 0` -- the last
being the singular ray of section 3.5, which exists only under phi_ls and phi_cw
and is treated separately below. writing `ρ := max(P, 0)/(2κ) ∈ [0, ∞]`, with
`ρ = ∞` when `κ = 0 < P`, the global minimiser over `S` is therefore

    **( max(−4, −ρ),  max(−4, −ρ/2) )**,  **unique**, in every case except
    `P = κ = 0`

and the union of those, over every weight vector for which the minimiser is
unique, is the **L-shaped curve**

    **E := { (t, t/2) : −4 ⩽ t ⩽ 0 }  ∪  { (−4, s) : −4 ⩽ s ⩽ −2 }**

running from `(0,0)` along `x_2 = x_1/2` to `(−4,−2)` and then down the face
`x_1 = −4` to `(−4,−4)`. the second piece is the range `ρ ∈ [4, 8]`, where `x_1`
has clipped at the face and `x_2` has not.

verified against an exact scan of `801 × 801` rational points, at 900 random weight
vectors across the three phi: **the closed form is beaten by the scan 0 times**,
and every unique argmin lies on `E`, 0 exceptions. **the excluded case `P = κ = 0`
is the singular ray and nothing else**: `P = 0` with `κ = 0` forces `w = 0` under
phi_lu, section 3.5, and under phi_ls and phi_cw it is exactly `w ∝ (1,3,0,0)` and
`w ∝ (1,5,0,0)`, whose set of global minimisers over `S` is the whole of `Q`.

**so, by example 3.8 statement 3, [1] printed page 10** --

> 3. If x̄ ∈ S is the only optimal solution for (MOP_φ(w)), then x̄ ∈ S is an
>    optimal solution for (1MIOP_φ).

-- **every point of `E` is an optimal solution of `(1MIOP_φ)` under all three phi**,
on the whole box, with no convexity and no differentiability used anywhere.
**including the origin**, at `w = (0, 0, w_3, w_4)` with `w_3 + w_4 > 0`, where the
scalarised objective is `κ U + const` and the origin is its unique minimiser;
**and including the whole face piece**, which condition (15) cannot produce because
it carries no constraint multipliers.

and by **example 3.8 statement 1**, which has no hypothesis at all, every global
minimiser of every weighted sum is a weak optimal solution, so under phi_ls and
phi_cw the singular ray's argmin gives **`Q ⊆` the weak optimal set**.

### 3.8 what closes and what does not, per phi

**the necessary direction for the optimal set is example 3.8 statement 4**, [1]
printed page 10, which needs `S` convex and `F` phi-convex and **no
differentiability**:

> 4. If S is convex, F is φ-convex and x̄ ∈ S is an optimal solution for
>    (1MIOP_φ), then there exists w ... with w_i ⩾ 0 ... such that x̄ ∈ S is an
>    optimal solution for (MOP_φ(w)).

    **phi_lu.** unavailable on `S`, F not being phi_lu-convex; **available on `Q`**,
        where every column is affine or a convex quadratic, section 3.3. by the
        projection lemma every optimal solution of the box lies in `Q`, and by the
        restriction lemma it is optimal on `Q`, so it is a global minimiser over
        `Q` of some weighted sum. on `Q` that weighted sum is `P_lu v + κ U + const`
        with `P_lu ⩾ 0` and `κ ⩾ 0` not both zero, whose minimiser over `Q` is
        **unique in every case** -- `P_lu = 0` forces `w_1 = w_2 = 0` and leaves
        `κ U`, minimised only at the origin -- and lies on `E`. so
        **Opt_lu ⊆ E**, and with section 3.7's `E ⊆ Opt_lu`,
        **Opt_lu = E exactly, on the whole box.**
    **phi_ls.** unavailable on `S`, F not being phi_ls-convex. **available on `Q`**
        -- and it gives nothing, because the singular ray's weighted sum is
        constant on `Q`, section 3.5, so its set of global minimisers over `Q` is
        `Q` itself. the bound is **`E ⊆ Opt_ls ⊆ Q`** and no better.
    **phi_cw.** **available on `S` itself**, F being phi_cw-convex, section 3.1 --
        and it gives the same nothing, for the same reason: the singular ray's
        weighted sum is constant on `Q` and strictly larger off it, so its argmin
        over `S` is `Q`. the bound is **`E ⊆ Opt_cw ⊆ Q`**.

and for the weak optimal sets:

    **phi_lu.** example 3.9 statement 1 on `Q`, with the restriction lemma, gives
        `WeakOpt(S) ∩ int Q ∩ int S ⊆ { (t, t/2) }`. so the derivation pins the
        weak optimal set **off the axes and off the faces of the box** and nowhere
        else.
    **phi_ls, phi_cw.** example 3.8 statement 1 at the singular ray gives
        `Q ⊆ WeakOpt`, and the projection lemma gives `WeakOpt ⊆ Q`. so
        **WeakOpt_ls = WeakOpt_cw = Q = [−4,0]² exactly**, derived, on the whole
        box, and the necessary condition is exact and vacuous at once.

**the summary, and the inversion in it is the result.**

    phi   thm 3.3 on S   ex 3.9 on S   singular ray   optimal set        weak optimal set
    lu    **fails**      fails         **none**       **= E, closed**    = E off the axes
                                                                          and faces only
    ls    **fails**      fails         (1,3,0,0)      E ⊆ · ⊆ Q, open    **= Q, closed**
    cw    **holds**      fails         (1,5,0,0)      E ⊆ · ⊆ Q, open    **= Q, closed**

**the order that keeps theorem 3.3 is the one whose derivation does not close, and
the order that loses it is the one whose does.** that is not a paradox: convexity
is a hypothesis of the sufficient statements, and what stops phi_ls and phi_cw is
the *necessary* one, where the singular weight makes the condition hold everywhere.
f5 section 4.1 predicted the convexity split correctly and read it as the damage;
**the damage is elsewhere.**


## 4. the failure, stated precisely

### 4.1 which hypothesis, at which points, under which phi

**the hypothesis that fails is example 3.9's preamble, "let `Λ_i^T f`, `B_i^T f` be
differentiable for all i", [1] printed page 10.**

    **under phi_lu**: `Λ_1^T f = G̲_1` and `B_1^T f = Ḡ_1`, both
        `ℓ(x_1) + ℓ(x_2) + 1` and `u(x_1) + u(x_2) + 1`, non-differentiable at
        every point of `x_1 = 0` and of `x_2 = 0`.
    **under phi_ls**: `Λ_1^T f = G̲_1` and `B_1^T f = 2r_1 = (|x_1| + |x_2|)/2`,
        both non-differentiable on the same two lines.
    **under phi_cw**: `Λ_1^T f = c_1` is affine and smooth, and
        `B_1^T f = r_1 = (|x_1| + |x_2|)/4` is non-differentiable on the same two
        lines.

**so the failure is on the crossing locus, it is on all of it, and it is under all
three phi.** no admissible φ removes it, a0 c14. the objective-2 coordinates are
polynomials and are differentiable everywhere under every phi; **the whole of the
failure sits in objective 1 and is produced by Moore's product on a sign-changing
`h`**, from coefficients that contain no absolute value anywhere.

**and it is not a formality about a hypothesis, because (15) itself is undefined
there.** condition (15) as printed chains three expressions,

>     Σ_i w_{2i−1} ∇Λ_i^T f(x̄) + Σ_i w_{2i} ∇B_i^T f(x̄)
>         = Σ_i ∇[(w_{2i−1} Λ_i^T + w_{2i} B_i^T) f](x̄)
>         = ∇{ Σ_i [(w_{2i−1} Λ_i^T + w_{2i} B_i^T) f] }(x̄) = 𝟎

and **the first expression requires each `∇Λ_i^T f(x̄)` and `∇B_i^T f(x̄)`
separately**. at a point of the locus those do not exist under any of the three
phi, so the first expression has no value and the chain has no meaning -- even at
weight vectors, such as `w = (0,0,w_3,w_4)`, for which the *last* expression is
perfectly well defined, the weighted sum being `κU + const` there. **that is the
exact sense in which the origin is not produced by (15): the equation cannot be
written down at it.**

**under phi_lu and phi_ls a second hypothesis fails, and globally.** by section 3.1
`F` is not phi_lu-convex and not phi_ls-convex on `S`, so example 3.9 statements 2
and 3 are unavailable **at every point of the box**, not only on the locus, and
example 3.8 statement 4 is unavailable with them. by section 1.6 the pointwise
reading of s-14 would restore statements 2 and 3 at the origin alone, where the
differentiability has already failed. **so under phi_lu and phi_ls, example 3.9's
sufficiency is unavailable everywhere on I-VU2 under either reading of s-14.**

### 4.2 what is therefore not derivable

**precisely three things, and no more.**

    **first, the origin is not produced by condition (15), under any phi.** the
        candidate set on the open quadrants is the open segment
        `{(t, t/2) : −4 < t < 0}`, whose closure contains `(0,0)` and which does
        not contain it. **the four quadrant pieces do not glue**: the segment is
        the whole of the third quadrant's contribution and the other three
        quadrants contribute nothing, so (15) approaches the origin from one side
        and never reaches it. that is f5 section 5.3's requirement discharged --
        the gap is exhibited and not asserted.
    **second, the face piece is not produced by condition (15), under any phi.**
        (15) is unconstrained stationarity and carries no constraint multipliers,
        so under the interiority reading of b1 section 1.4 it says nothing at a
        point of a face of the box. `{ (−4, s) : −4 ⩽ s ⩽ −2 }` is an **arc of
        positive length of the answer**, section 3.7, and it lies entirely on the
        face `x_1 = −4`. **on p1 and I-BK1 the interiority reading cost nothing**,
        both derived sets being strictly interior; on I-VU2 it costs an arc, which
        is the risk f5 section 5.1 named for I-SD, arriving on a different problem.
    **third, and this one is not the crossing's, the optimal set is not pinned
        under phi_ls or phi_cw.** the singular ray makes both necessary
        conditions vacuous on `Q` at once -- (15) holds at every point of it,
        section 3.5, and the weighted sum example 3.8 statement 4 produces is
        constant on it, section 3.7 -- so the published route leaves
        `E ⊆ Opt ⊆ Q = [−4,0]²`, a gap of Lebesgue measure `16` against an answer
        of measure zero. **this is s-12 recurring**,
        docs/part1/part1_closing.md section 5.1, on a published problem and in a
        two-dimensional rather than a one-dimensional form.

**and what remains derivable is more than the failure suggests.** the first two
gaps are filled by example 3.8 statement 3, which has no differentiability
hypothesis and no interiority question, and certifies the origin and the whole face
piece as optimal solutions; section 3.7. **the third is not filled by anything
published.** so the honest sentence is: *the condition that finds candidates fails
on the locus and on the faces, and the condition that certifies them does not; and
under two of the three orders the condition that would prove the list complete is
satisfied vacuously.*

### 4.3 the stopping rule, applied

CONTEXT.md section 6 and the brief: a derivation that does not close using the
published results as they stand stops and reports, and is not patched. **it is
applied three times in this document and the three places are named.**

    **example 3.9 is not extended to the locus.** no limiting form of (15), no
        subdifferential, no one-sided derivative and no Clarke gradient appears
        anywhere above. the origin's status comes from definition 3.1 and from
        example 3.8, both of which apply as printed.
    **example 3.9's convexity is not weakened to remark 2.2's pointwise form**,
        section 1.4, even though section 1.6 shows the weakening would change
        nothing here.
    **`Opt_ls` and `Opt_cw` are left as `E ⊆ · ⊆ Q` and are not closed.** section
        6.1 states separately, and marked as such, what is true of them by a direct
        domination argument; **that argument is not offered as a derivation** and
        the derived bound is the one that goes in the memoria's derivation column.

### 4.4 p0 and I-VU2: one condition, and two mechanisms

f5 section 4.4 asks whether this is the condition that made p0 unusable as a
fixture. **it is the same condition and the second half of the answer is sharper
than f5 could make it.**

    **the same.** in both problems the half-width is an absolute value, so both
        image coordinates are kinked; theorem 3.3 fails for phi_lu and phi_ls and
        survives for phi_cw; example 3.9's differentiability fails under all three
        phi; and **the kink sits at a point of the answer** -- p0's published anchor
        `x = 0`, [1] lines 752-755, and I-VU2's origin. b1 section 1.5's p0 table
        and section 1.6's table above are the same table with `−|x|` widened to two
        variables. **r-04 was raised for phi_lu and b1 widened it to all three; this
        session widens it to a problem the project did not construct.**
    **the different, and it is where they come from.** p0 has no ⊙ at all: [1]
        writes `F_1(x) = [−|x|, |x|]` directly and the absolute value is in the
        statement. on I-VU2 it is *produced*, by Moore's product on a sign-changing
        `h`, from coefficients that carry no absolute value. **so the two are one
        condition reached by two mechanisms**, and the second mechanism is the one
        that can appear in a problem nobody wrote to be pathological.
    **and one further difference, which is this session's and not f5's.** on p0 the
        kink costs the derivation a point. **on I-VU2 it also costs the comparison
        the whole problem**, because the same absolute value makes `r_1` an exact
        affine function of `c_1` with negative slope on the quadrant where the
        answer lives, section 2.5, which produces the singular ray of section 3.5
        and the collapse of section 6. **that consequence has no counterpart on
        p0**, whose two objectives are not of that shape, and it is the part of
        the answer that generalises least comfortably: a crossing does not only
        break differentiability, it can *create* part1_closing section 6.1's
        degeneracy locally.
    **and one way in which the appendix-A version is worse.** p0's kink is a single
        point of a one-dimensional box. I-VU2's is two lines through a
        two-dimensional box, and in general the crossing locus has codimension one,
        so the set on which example 3.9 is unavailable is not negligible.


## 5. the origin, without example 3.9

### 5.1 the direct argument, from definition 3.1

**definition 3.1, [1] printed page 6**, a0 c10, with the order relations (3), (6)
and (7) of [1] printed pages 3 and 4:

> **Definition 3.1.** ... x̄ ∈ S is a:
> (1) strong or strict optimal solution for (10) if there does not exist
>     x ∈ S ∖ {x̄} such that F(x) ≦_φ F(x̄).
> (2) optimal solution for (10) if there does not exist x ∈ S ∖ {x̄} such that
>     F(x) ≤_φ F(x̄).
> (3) weak optimal solution for (10) if there does not exist x ∈ S ∖ {x̄} such
>     that F(x) <_φ F(x̄).

and `≦_φ` is componentwise `⩽` on the `2m` image coordinates, (3) with (2) of [1]
printed page 3. **so statement (1) is decided by one inequality per column and
needs no derivative and no convexity.**

**the claim.** `x̄ = (0,0)` is a **strong (strict) optimal solution** of I-VU2 under
all three phi.

**the proof, one column at a time.** at the origin `v = 0`, `s = 0` and `U = 0`, so
the twelve image coordinates take the values

    phi_lu   (G̲_1, Ḡ_1, G̲_2, Ḡ_2) = (1, 1, −1, −1)
    phi_ls   (G̲_1, 2r_1, G̲_2, 2r_2) = (1, 0, −1, 0)
    phi_cw   (c_1, r_1, c_2, r_2) = (1, 0, −1, 0)

suppose `x ≠ 0` had `F(x) ≦_φ F(0)`, that is all four coordinates no larger. it is
enough to read one column per phi:

    **phi_lu**, column 3: `G̲_2(x) = U − 1 ⩽ −1` requires `U ⩽ 0`. `U = x_1² + 2x_2²`
        is a positive definite quadratic form, so `U ⩾ 0` with equality **only** at
        `x = 0`. contradiction. (column 4 does the same on its own.)
    **phi_ls**, column 4: `2r_2(x) = U/2 ⩽ 0`, the same contradiction. (column 3
        does the same.)
    **phi_cw**, column 4: `r_2(x) = U/4 ⩽ 0`, the same contradiction. (column 3
        does the same, `c_2 = (5/4)U − 1 ⩾ −1` with equality only at the origin.)

so no such `x` exists and the origin is a strong optimal solution under all three
phi. **by definition 3.1's own implication chain, printed page 6 -- strong ⇒
optimal ⇒ weak optimal -- it is an optimal and a weak optimal solution too.** ∎

**this is stronger than f5 section 4.3's statement in two ways.** f5 argued
phi_cw-efficiency from `r_1 ⩾ 0` with equality only at the origin, which is true
and needs both objective-1 columns; the argument above uses **one column of
objective 2 per phi** and gives the *strong* concept rather than the ordinary one.
and f5's phi_lu and phi_ls arguments are recovered as the parenthetical cases.
verified on 20000 random rational points of the box: **0 points with all four
columns no larger than the origin's, under each of the three phi.**

**note what the argument does and does not use.** it uses the four numbers above
and the positive definiteness of `U`. it does not use differentiability, convexity,
example 3.9, example 3.8, the weights, the quadrant decomposition or any grid.
**it would be unchanged if the crossing were worse than it is.**

### 5.2 the same point, from example 3.8 statement 3

independently, and this one is a published sufficient condition rather than a
definition: take `w = (0, 0, w_3, w_4)` with `w_3 + w_4 > 0`, admissible under
reading one of s-02, which CONTEXT.md section 6 commits to and which f2 section 5
supplies a second witness for. the scalarised objective is then

    phi_lu   w_3(U − 1) + w_4((3/2)U − 1) = κ U + const,   κ = w_3 + (3/2)w_4 > 0
    phi_ls   κ U + const,  κ = w_3 + (1/2)w_4 > 0
    phi_cw   κ U + const,  κ = (5/4)w_3 + (1/4)w_4 > 0

a positive multiple of a positive definite quadratic form, whose **unique** global
minimiser over `S` is the origin. **example 3.8 statement 3, [1] printed page 10,
then makes the origin an optimal solution of `(1MIOP_φ)` under all three phi**,
and statement 3 requires uniqueness and nothing else -- no convexity of `F`, no
differentiability, no positivity of the weights.

**so the origin is certifiable by a published result, and it is not findable by
the published result the project uses to find candidates.** that is the precise
shape of the boundary and it is worth stating in those words: **example 3.8 has no
smoothness hypothesis and example 3.9 does, and the crossing separates them.**

### 5.3 why this is the sharpest available statement

the deliverable of this session is not "the derivation broke". it is:

    on the four open quadrants the problem is affine-plus-diagonal-quadratic, b1's
        route applies with no hypothesis weakened, and the candidate set is
        derived exactly: the open segment `x_2 = x_1/2`, section 3.6.
    on the two lines `x_1 = 0` and `x_2 = 0` the route is **unavailable and
        provably so**, not merely difficult: (15) cannot be written at a point of
        them under any phi, section 4.1.
    **and the answer contains a point of those lines**, the origin, whose
        efficiency is proved above in nine lines from definition 3.1 and again
        from example 3.8.
    so the closed form the route produces recovers the efficient set **minus** a
        set on which the published conditions have nothing to say, and that set is
        not empty of the answer.
    and the missing point is not an artefact of the box or of a face. it is
        **`G_2`'s own global minimiser**, which is the kind of point every
        biobjective efficient set contains, and it is where both crossing loci
        meet.

**that is [16]'s reservation of printed page 27, instantiated, located and
bounded, on the paper's own test problem.**


## 6. the three sets

### 6.1 what the route establishes, and what is true

**derived**, by section 3.8, with `E` as in section 3.7:

    phi    optimal set (ND)        weak optimal set
    lu     **= E**, exactly        = E off the axes and the box faces; open on them
    ls     E ⊆ · ⊆ [−4,0]²         **= [−4,0]²**, exactly
    cw     E ⊆ · ⊆ [−4,0]²         **= [−4,0]²**, exactly

**true**, by direct domination from definition 3.1 and **not by the published
route**, and marked as such wherever it is used:

    **all three optimal sets equal `E`**, and **`WeakOpt_lu = E`** while
    **`WeakOpt_ls = WeakOpt_cw = [−4,0]²`**.

**the argument, in four steps, each verified in exact rational arithmetic.**

    **(i)** every point outside `[−4,0]²` is strictly dominated by its projection,
        section 3.3's lemma, so all four sets lie in `Q = [−4,0]²`. verified,
        14868 points, 0 failures, per phi.
    **(ii)** on `Q` every image coordinate is a function of the two scalars
        `v = x_1 + x_2` and `U = x_1² + 2x_2²` alone:

            phi_lu   ( (3/2)v + 1,  v + 1,     U − 1,        (3/2)U − 1 )
            phi_ls   ( (3/2)v + 1,  −v/2,      U − 1,        U/2        )
            phi_cw   ( (5/4)v + 1,  −v/4,      (5/4)U − 1,   U/4        )

        verified, 5132 quadrant points, 0 mismatches, per phi. **under phi_lu both
        objective-1 columns increase in `v`; under phi_ls and phi_cw one increases
        and the other decreases**, which is section 2.5's negative slope.
    **(iii)** `u_min(v) := min{ U(y) : y ∈ Q, v(y) = v }` equals `2v²/3` for
        `v ∈ [−6, 0]`, attained only at `(2v/3, v/3)`, and `16 + 2(v+4)²` for
        `v ∈ [−8, −6]`, attained only at `(−4, v+4)`; and it is **strictly
        decreasing in `v`**. verified against an exact scan of 401 points on each
        of 801 level segments: 0 levels beaten, 0 monotonicity violations. the
        set `{ x ∈ Q : U(x) = u_min(v(x)) }` is exactly `E`, verified at 5132
        points, 0 mismatches.
    **(iv)** hence, on `Q`: under **phi_lu**, `y` dominates `x` iff `v(y) ⩽ v(x)`
        and `U(y) ⩽ U(x)` with one strict, so the non-dominated set is
        `{U = u_min(v)} = E`, and the *strictly* dominated points are the same
        ones because `u_min` is continuous. under **phi_ls and phi_cw**, `y`
        dominates `x` iff `v(y) = v(x)` and `U(y) ⩽ U(x)` with one strict -- the
        first two columns move oppositely -- so the non-dominated set is again
        `E`, while **no point of `Q` strictly dominates any other point of `Q`**.
        **nor does any point outside `Q`**, and that needs its own line rather
        than the projection lemma: for `x ∈ Q` and any `y ∈ S`, `s(y) ⩾ |v(y)|`
        always and `s(x) = −v(x)`, so under phi_cw strictness in both objective-1
        columns wants `v(y) < v(x)` and `s(y) < s(x)`, giving
        `−v(y) > −v(x) = s(x) > s(y) ⩾ −v(y)`, a contradiction; under phi_ls,
        writing `t := s(x) − s(y) > 0`, strictness in `G̲_1` gives
        `(5/4)v(y) ⩽ (5/4)v(x) − t/4` while `v(y) ⩾ −s(y) = v(x) + t` gives
        `(5/4)v(y) ⩾ (5/4)v(x) + (5/4)t`, so `(5/4)t ⩽ −t/4` and `t ⩽ 0`. **so
        the weak optimal set is the whole of `Q`**, which is what section 3.8
        derives independently from example 3.8 statement 1.

verified as stated: every off-`E` sampled point is dominated by the exhibited point
`(2v/3, v/3)` or `(−4, v+4)` of its own level, 19986 of 19986 under each phi, 0
failures; no point of a 302-point sweep of `E` is dominated by any of 4000 random
points, under each phi; and under phi_lu every one of 19952 off-`E` quadrant points
is **strictly** dominated by a point of `E` at a slightly smaller `v`, with the
step size taken from the gap `U − u_min(v)` rather than guessed, 0 failures. and
the strictness verdict of (iv) with the dominators drawn from the **whole box**
rather than from `Q`: of 400 sampled points of `[−4,0]²` against 8000 random
points of `[−4,4]²`, **strictly dominated 0 under phi_ls, 0 under phi_cw and 332
under phi_lu**, which is the three weak optimal sets in one line.

### 6.2 the pairwise relations, as far as they can be established

**from the route alone**, section 6.1's first table:

    X_lu = E  and  E ⊆ X_ls,  E ⊆ X_cw     so   **X_lu ⊆ X_ls and X_lu ⊆ X_cw**
    X_ls and X_cw are bounded above by Q and are not pinned, so **no relation
    between X_ls and X_cw is established by the derivation**

**including what is true**, section 6.1's second paragraph:

    **X_lu = X_ls = X_cw = E**, all three equal, all inclusions equalities.

### 6.3 the containment criterion, applied as a check

docs/part1/a_close_containment.md section 1 proves, from the criterion that
`φ_B = M φ_A` with `M` entrywise non-negative and invertible makes `φ_A`-dominance
imply `φ_B`-dominance, that

    corollary 1.  ND_lu(S) ⊆ ND_ls(S)
    corollary 2.  ND_cw(S) ⊆ ND_ls(S)

for every `S` and every `F`, and that the criterion is silent on the pair
(phi_lu, phi_cw) in both directions. **as in b1 section 5 and f2 section 3.2 the
result is not used anywhere in the derivation and is applied here only as an
independent test.**

    **X_lu ⊆ X_ls**   **predicted.** established by the route, section 6.2. **a
                      check on the derivation and not a finding.**
    **X_cw ⊆ X_ls**   **predicted.** holds, with equality, on the true sets; the
                      route does not pin either side, so this one is a check on
                      the direct argument of section 6.1 rather than on the
                      derivation. **not a finding.**
    **X_lu vs X_cw**  **not predicted, in either direction.** established by the
                      route in one direction, `X_lu ⊆ X_cw`, and an equality on
                      the true sets. **this is the finding about I-VU2.**

and the un-predicted pair is worth one line for the memoria because the project now
has three answers to it: **p1's two sets cross**, b1 section 5, neither containing
the other; **I-BK1's nest strictly, `X_cw ⊊ X_lu`**, f2 section 3.1; **I-VU2's are
equal**. three problems, three different answers on the one pair no theorem covers.

### 6.4 criterion 3 fails on I-VU2, exactly

criterion 3 of the part 2 gate, docs/part1/part1_closing.md section 7.2: "the three
phi must give distinct non-trivial sets, none equal to the crisp set and none the
whole box".

    **distinct: no.** all three are `E`, section 6.1.
    **none equal to the crisp set: no.** the crisp centre problem `min (c_1, c_2)`
        has columns `((5/4)v + 1, (5/4)U − 1)`, both increasing in their own
        scalar, so its Pareto set is `{v minimal given U}` -- the same computation
        as section 6.1(iv) -- and is **also `E`**. so all three phi return the
        crisp centre problem's efficient set exactly.
    **none the whole box: yes**, `E` has Lebesgue measure zero in `[−4,4]²`.

**so I-VU2 fails criterion 3, and it fails it exactly rather than by sample**,
which is the reversal docs/part2/lit_review.md section 7.2 argued for and f2
section 3 first exercised: on a problem whose efficient sets are derivable the
derivation answers the criterion, and here the answer is no.

**and the reason is the crossing.** section 2.5: the interchange makes
`r_1 = (1 − c_1)/5` on the quadrant where the whole answer lives, an exact affine
function of the centre with negative slope, so objective 1 is degenerate there in
part1_closing section 6.1's sense; section 2.6: objective 2 is degenerate
everywhere with positive slope and is phi-blind. **both objectives are degenerate
on the region that matters and the three orders have nothing left to disagree
about.** f5 chose I-VU2 knowing `G_2` was blind and recording that as its cost;
what f5 could not see without the derivation is that `G_1` goes blind too, and for
the very reason the problem was chosen.

**this does not retract f5's choice.** the session's deliverable is a statement
about where the transformation's hypotheses fail, section 5.3, and that statement
is delivered. what is retracted is any expectation that I-VU2 could also carry a
cross-phi comparison, and section 8 says what follows for the memoria.

### 6.5 x-01 is not testable on I-VU2

docs/part1/part1_closing.md section 3.4 and the x-01 row of PROGRESS.md section 9:
the protected-minimiser effect is present at a pair (problem, phi) exactly when some
image column has a non-empty free set. **all twelve of I-VU2's image columns depend
on both `x_1` and `x_2`** -- `v`, `s` and `U` all do -- so every free set is empty
and the condition is not triggered. **I-VU2 supplies no test of x-01**, exactly as
I-BK1 supplied none, f3 measuring 0 of 12 columns with a free set there. one line,
recorded so that a later session does not look for the effect here.


## 7. the external check

### 7.1 what [16] gives on I-VU2, and what it does not

**it does not give a solution point.** [16] prints, for I-BK1 alone, Table 1's
iterates with `x⋆` and `G(x⋆)` (printed page 20), equation (25)'s one-parameter
solution curve and Table 2's eleven points (printed pages 20-21), and the
gH-gradients and gH-Hessians (printed page 18). **for I-VU2 it prints none of
these.** what it prints is:

    **Table 3, printed page 23**, "Performance of Algorithm 1": for 100 randomly
        chosen initial points, the min, max, mean, median, mode and standard
        deviation of the iteration count and of the CPU time. the I-VU2 row is
            iterations  (0, 6, 3.8000, 4.0000, 4, 1.7403)
            CPU time    (0.0114, 0.2136, 0.1028, 0.0755, 0.0114, 0.0651)
    **Figure 3(a), printed page 24**: the objective feasible region with the
        locations of `G(x⋆)` for five randomly chosen initial points, as a picture.
        no coordinates are printed and none can be read off a raster figure to any
        useful precision.

**so there is no numerical checkpoint on I-VU2 and this session does not claim
one.** f2's two checkpoints -- equation (25)'s curve, which passed, and Table 1's
`x⋆`, which failed in the paper -- have no analogue here. **the derivation above is
verified against its own algebra and against the project's own modules and is not
verified against a published point, because there is no published point.**

**one weaker thing is available and is worth naming.** the *reading* of I-VU2 --
that ⊙ is Moore's product and that the endpoints are section 2.2's -- is confirmed
only transitively: the same conventions, in the same modules, reproduce [16]'s
printed `G(x⋆)` for I-BK1 to the last printed digit, f2 section 4.2 and f6's
`tests/test_problems_native.py`. **that is a check on the conventions and not on
I-VU2.**

### 7.2 what the paper does give, checked against the derivation

**two things can be checked, and both pass.**

**first, containment in [16]'s own Pareto critical set.** definition 2.18, [16]
printed page 7:

> **Definition 2.18 (Pareto critical point [27]).** A point x⋆ ∈ U is said to be
> Pareto critical point of the MIOP (1) if there does not exist any v ∈ ℝⁿ such
> that ∇_gH G_i(x⋆)^⊤ ⊙ v ≺ 0 for all i = 1, 2, …, m.

with `∇_gH H(x̃)^⊤ ⊙ v := ⊕_j D_j H(x̃) ⊙ v_j`, printed page 6, and `≺` from
definition 2.2, printed page 4. Algorithm 1 converges to a Pareto critical point,
so **every point of the derived efficient set must be Pareto critical** -- a
necessary condition the derivation has to satisfy. from the problem statement,
`D_j G_1 = [1, 3/2]` for both `j`, and `D_1 G_2 = [1,3/2] ⊙ 2x_1`,
`D_2 G_2 = [2,3] ⊙ 2x_2`. working the four sign cases out gives, on the open third
quadrant with `p = −x_1` and `q = −x_2`,

    **a descent direction exists iff `p > (9/2) q` or `q > (9/8) p`**,
    so **the Pareto critical set is the cone `2/9 ⩽ x_2/x_1 ⩽ 9/8`** in the third
    quadrant, and no point outside the closed third quadrant is critical.

checked against a scan of 8000 rational directions at 70 points of the quadrant,
including points on both sides of both boundaries: **70 agreements, 0
disagreements**, and 5 of 5 tested points outside the quadrant found non-critical
by the scan. **the derived efficient ray has `x_2/x_1 = 1/2`, inside `[2/9, 9/8]`,
and the face piece has `x_2/x_1 = |s|/4 ∈ [1/2, 1]`, also inside. so `E` is
contained in [16]'s own Pareto critical set: the check passes.**

**second, Table 3's minimum iteration count of 0.** `E` has Lebesgue measure zero
in `[−4,4]²`, so a uniformly random initial point is efficient with probability
zero; yet at least one of [16]'s 100 random starts terminated at iteration 0.
**that is only consistent if the algorithm's termination set is strictly larger
than the efficient set**, which is exactly what the cone above says: its area
inside the box is `64/9 = 7.1111` against the box's `64`, i.e. **one ninth of the
box**, so about eleven of a hundred uniform starts are expected to be critical
already. the row's mean 3.8 sitting below its median and mode of 4, with a
standard deviation of 1.7403 and a maximum of 6, is the shape a small cluster of
zeros produces. **this is a consistency check and not a verification**: nothing
above pins the number of zeros and the arithmetic would tolerate a range of them.

**what this is not.** it is **not** a second counterexample to [16]'s proposition
2.1 or lemma 2.4(ii), which f2 section 4.3 refuted on I-BK1 and which a-11 records.
both statements require hypotheses I-VU2 fails independently -- proposition 2.1
requires `∇²_gH G_i ≻ 0` for all `i`, and `G_1` is affine so its gH-Hessian is the
degenerate `[0,0]`; lemma 2.4(ii) requires `G` to be `I(ℝ)^m` convex, and `G̲_1` is
concave, section 3.1. **so neither statement applies to I-VU2 and I-VU2 says
nothing about either.** what recurs is only the *mechanism* a-11 identified: the
Pareto critical set of definition 2.18 strictly contains the efficient set, with
positive measure, on a second problem of the appendix.


## 8. what this adds

**for the memoria, in four sentences.** I-VU2 is the only problem in [16]'s
appendix A whose boundary functions interchange and which is not disqualified on
other grounds, so it is the only route the project has to the question the
supervisors raised on 4 September: it tests what p1, the tier 1 benchmarks and
I-BK1 cannot, because in all four of those every interval coefficient multiplies a
function of constant sign and the 2m transformation's validity condition, [16]
printed page 27, is satisfied by construction. **what it establishes is where the
transformation approach stops**: on a published problem, Moore's product on a
sign-changing factor puts an absolute value in the half-width, example 3.9's
differentiability hypothesis fails on a codimension-one locus under every
admissible order, and the answer contains a point of that locus -- the origin,
whose efficiency is provable in nine lines from definition 3.1 and which condition
(15) cannot produce, because at that point (15) cannot be written down.
**a second cost is found that was not anticipated and belongs beside the first**:
the same absolute value makes the half-width an exact affine function of the centre
with negative slope on the region where the efficient set lives, which produces a
singular weight direction under phi_ls and phi_cw, leaves the optimal set unpinned
under both, and collapses all three phi-efficient sets onto one another and onto
the crisp centre problem's, so **I-VU2 fails criterion 3 exactly and carries no
cross-phi comparison at all.**

**the scope, stated so nobody widens it.** this is **one problem**. the statement
is about **where the published hypotheses fail and what is provable anyway**, not
about how often a crossing occurs in practice, not about how much of a typical
efficient set it hides, and not about the Newton method, which is not implemented
anywhere in this project. f5 section 3.3 measured that **five of [16]'s twenty
appendix-A problems interchange**, which bounds the frequency in one published
suite and in no other; and f5 section 4.2's counts of how often a crossing meets
the answer are grid statements on four of those five, of which only I-VU2's is now
exact. **the honest general sentence is the conditional one**: wherever an interval
coefficient multiplies a function that changes sign on the feasible set, the 2m
transformation's differentiability hypothesis fails on the sign-change locus under
every order in [1]'s class, and whether that costs anything depends on whether the
efficient set meets the locus -- which, on the one problem where it has been
settled exactly, it does.


## 9. open items, corrections, and what this session does not close

**answered.**

    **s-14, as f5 proposed it.** [1] settles it from its own text: example 3.9's
        "F is φ-convex" is definition 2.2's global (8), and the paper's examples
        3.4 to 3.7 show the pointwise form is in its active vocabulary and was not
        used here. section 1. **it was never registered as an s-row and this
        session does not register one**; the proposal is answered rather than
        closed, and the residue -- whether the omission of "at x̄" is deliberate --
        is a question for the authors that the project does not need answered,
        section 1.6. **registration or withdrawal is the research chat's, as f5
        left it.**

**corrections to earlier documents, none of which reverses a verdict.**

    **f5 section 3.5 and section 5.3, on `G_1`'s degeneracy.** "`G_1` is not
        degenerate" is true of the box and **false of the third quadrant**, where
        `r_1 = (1 − c_1)/5`, affine in the centre with negative slope. f5's own
        constant-sign table row is right on the first quadrant and has the wrong
        sign on the third. section 2.5. **the consequence is section 6.4's
        criterion-3 failure**, which f5 did not predict and which does not change
        f5's choice, section 5.3's deliverable being the failure statement and not
        a comparison.
    **f5 section 4.1's reading of where the damage falls.** f5 has the convexity
        split right -- phi_cw keeps theorem 3.3, phi_lu and phi_ls lose it -- and
        reads that as what costs the derivation. **on I-VU2 it is not**: phi_lu,
        which loses theorem 3.3, is the only order whose derivation closes, and
        phi_cw, which keeps it, is one of the two that do not. section 3.8.
    **f5 section 4.2's I-VU2 row, refined rather than corrected.** "crossing points
        not dominated: lu 2/242, ls 2/242, cw 2/242" is right about the
        non-dominated (optimal) sets, whose only locus point is the origin under
        all three phi. it does not distinguish weak optimality, and under phi_ls
        and phi_cw **every point of the locus in `[−4,0]²` is weakly optimal**,
        section 6.1. the test measured the right thing and the distinction is
        worth having in the memoria.

**not closed, and deliberately.**

    **`Opt_ls` and `Opt_cw` are not derived.** the published route leaves
        `E ⊆ · ⊆ [−4,0]²` under both, section 3.8, and the singular weight is why.
        section 6.1 says what is true by direct domination and that argument is
        **not** offered as a derivation. **s-12's row is p1's and stays open on
        p1's terms; I-VU2 is a second instance of the same gap**, on a published
        problem and two-dimensional rather than one-dimensional, and whether that
        is worth adding to the row is the research chat's.
    **no external check exists on I-VU2** and none is claimed, section 7.1.
    **the interiority reading costs an arc here**, section 4.2, where on p1 and
        I-BK1 it cost nothing. whether example 3.9 should be read with constraint
        multipliers on a boxed problem is not a question this session opens; it is
        recorded that the reading is now load-bearing on a published problem and
        that f5 section 5.1 predicted it for I-SD.
    **a-6, a-7 and the sixth gate criterion f5 proposed** are untouched.

**s-02, the weight phrase.** this document takes reading one throughout, as b1 and
f2 do, and section 5.2's certification of the origin uses `w = (0,0,w_3,w_4)`,
which reading two would forbid. **that is a third witness of the same kind as f2
section 5's**, and it is offered as evidence and not as a resolution: under reading
two the origin would lose its example 3.8 certificate and would keep the definition
3.1 argument of section 5.1, which uses no weights at all. **nothing above depends
on the answer**, section 5.1 being weight-free.

**no source read in this session refutes anything in CONTEXT.md, so CONTEXT.md is
unchanged by this session.**
