# f5: boundary-function interchange, and the choice of the project's last problem

session f5, 2026-09-06. **no problem added to src/, no derivation, no fix to
evaluation semantics, and no run beyond diagnostics.** the numbers below come
from throwaway scripts in the session scratchpad; nothing was added under src/,
no test was changed and nothing is committed but this document and one session
log line.

the session exists because the supervisors raised, at the meeting of 4 September,
that an interval carried as two fixed boundary functions can be got wrong: which
expression gives the lower endpoint need not be fixed. under coefficient
imprecision an objective is `[a, b] ⊙ h(x)`, definition 2.1(iii) of [16] printed
page 3 defines the product by the minimum and the maximum over the four endpoint
products, and where `h` changes sign the two boundary functions interchange.
[16]'s own conclusion, printed page 27, states the validity condition of the 2m
transformation in exactly those terms and
docs/part2/lit_review.md section 1.7 transcribes it.

sources read in this session:

    src/interval_math.py, src/problems_tier0.py, src/problems_tier1.py and
        src/problems_native.py, in full, for part 1; src/phi_transforms.py for
        what part 1's ill-ordered pair does downstream.
    papers/Newton Method for Multiobjective Optimization Problems of
        Interval-Valued Maps.pdf, [16], **appendix A re-extracted and read in
        full**, printed pages 27 to 31, and the conclusion's validity condition,
        printed page 27.
    docs/part2/lit_review.md sections 1.7 to 1.10 and 6, and section 7.2 and 7.4.
    docs/part1/part1_closing.md section 6.1 and section 7.2.
    docs/part1/b1_phi_efficient_sets.md sections 1.5 and 2.1, for p0's failure and
        for what condition (15) costs at n = 2.
    docs/part1/a0_framework.md c12 and c14, for theorem 3.3 and example 3.9 as
        transcribed.
    docs/part2/f2_ibk1_derivation.md sections 0, 1.2 and 7, and
        docs/part2/part2_closing.md sections 4 and 7.2.


## 0. the headline, and it is part 1's

**the project does not implement Moore's product anywhere.** `src/interval_math.py`
carries six callables — `add`, `scalar_multiply`, `centre`, `half_width`, `width`,
`gh_difference` — and none of them is an interval-by-interval or an
interval-by-function product. the one place in the project where an interval
coefficient multiplies a function of x is `objective_endpoints` in
[problems_native.py:115-118](src/problems_native.py#L115-L118), and it computes the
endpoints **in fixed order**, `(Σ a_j h_j, Σ b_j h_j)`, not as the minimum and the
maximum over the four products.

**that is exactly correct on everything the project has ever run, and it is not
correct in general.** it is correct wherever every `h_j` has constant sign, which
is [16]'s own condition of printed page 27 and which the module's head comment
states as the reason for the form. it is wrong wherever an `h_j` changes sign under
a non-degenerate coefficient interval, and it is wrong **silently**: nothing in
`src/` tests `f_l ≤ f_u`, so an ill-ordered pair is carried into
`src/phi_transforms.py` unchallenged and emerges as a negative width.

so the code is correct-as-documented, unguarded, and not general. no result in
part 1 or part 2 is affected — part 2 below establishes that per problem — but the
choice this session is preparing for is precisely the choice that could put a
sign-changing `h` into that code path, and at that moment the defect stops being
theoretical. **the fix is not made here**; a change to evaluation semantics is its
own session with its own tests.


## 1. the code audit

### 1.1 what is in the four modules

read in full. wherever an interval coefficient multiplies a function of x:

    src/interval_math.py       no such operation exists. the module's six
                               callables are add, scalar_multiply, centre,
                               half_width, width and gh_difference. **there is no
                               multiply, product, moore_product or
                               interval_multiply.** the only min/max in the module
                               is inside gh_difference, which is a different
                               operation ([10] section 2, printed page 3) and is
                               correct.
    src/problems_tier0.py      p0 returns its endpoint functions directly,
                               (−|x|, |x|) and (0, x²), [16] is not involved and
                               no coefficient multiplies anything. p1 returns
                               (centre, half-width) with the half-widths
                               ρx² + δ built as sums of non-negative terms. **no ⊙
                               anywhere.**
    src/problems_tier1.py      both problems return (centre, half-width); the
                               half-widths are eps·((x−½)² + 1/20) and eps·x.
                               **no ⊙ anywhere.**
    src/problems_native.py     `objective_endpoints`, the only site in the project.
                               it computes
                                   (lower_1*first + lower_2*second,
                                    upper_1*first + upper_2*second)
                               which is `(Σ_j a_j h_j, Σ_j b_j h_j)` in fixed
                               order. **this is the fixed-order reading and not
                               definition 2.1(iii).**

one asymmetry worth recording, because it shows the project already knew the
question in its other form. `scalar_multiply` handles a **real scalar** times an
interval with the endpoints swapped entrywise when the scalar is negative, by
`np.where` on the sign, citing [1] section 2 page 2 lines 103-106. the sign case
that is handled is the one the paper writes down as a branch; the sign case that
is not handled is the one that arises from a function of x rather than from a
coefficient.

### 1.2 the test, and its literal output

the audit is not left as a reading. the diagnostic evaluates an expression
`[a, b] ⊙ h(x)` with `h` changing sign **through the project's own
`objective_endpoints`** — only `basis_functions` and the coefficient tuple are
replaced, the arithmetic is the module's — using I-VU2's `G_1`, problem 2 of [16]'s
appendix A, printed page 28: `[1, 1.5] ⊙ x_1 ⊕ [1, 1.5] ⊙ x_2` on `[−4, 4]²`.

    ========================================================================
    A. what primitives exist in src/interval_math.py
    ========================================================================
    callables: ['add', 'centre', 'gh_difference', 'half_width', 'scalar_multiply', 'width']
    a primitive for interval (.) interval, or interval (.) real function: False

    ========================================================================
    B. scalar_multiply, a REAL scalar times an interval: the sign is handled
    ========================================================================
    lam     = [-2. -1.  0.  1.  2.]
    [a_l,a_u] = [1, 3] throughout
    lower   = [-6. -3.  0.  1.  2.]
    upper   = [-2. -1.  0.  3.  6.]
    well ordered (lower <= upper) everywhere: True

    ========================================================================
    C. an interval coefficient times a SIGN-CHANGING function of x,
       through src/problems_native.py's own objective_endpoints
    ========================================================================
    h(x) = x_1, which changes sign at x_1 = 0, interior to [-4, 4]^2
    x_1     = [-2.  -1.  -0.5  0.   0.5  1.   2. ]
    lower   = [-2.  -1.  -0.5  0.   0.5  1.   2. ]
    upper   = [-3.   -1.5  -0.75  0.    0.75  1.5   3.  ]
    well ordered (lower <= upper): [False False False  True  True  True  True]
    WELL ORDERED EVERYWHERE: False

    Moore's product, definition 2.1(iii) of [16] printed page 3, min and max
    over the four endpoint products, computed here for comparison:
    moore lower = [-3.   -1.5  -0.75  0.    0.5   1.    2.  ]
    moore upper = [-2.   -1.   -0.5   0.    0.75  1.5   3.  ]
    code agrees with Moore where h >= 0: True
    code agrees with Moore where h <  0: False

    ========================================================================
    D. what the ill-ordered pair does downstream, through phi_transforms
    ========================================================================
    phi_lu: coord1 = [-2.  -1.  -0.5  0.   0.5  1.   2. ]
            coord2 = [-3.   -1.5  -0.75  0.    0.75  1.5   3.  ]
    phi_ls: coord1 = [-2.  -1.  -0.5  0.   0.5  1.   2. ]
            coord2 = [-1.   -0.5  -0.25  0.    0.25  0.5   1.  ]
    phi_cw: coord1 = [-2.5   -1.25  -0.625  0.     0.625  1.25   2.5  ]
            coord2 = [-0.5   -0.25  -0.125  0.    0.125  0.25   0.5  ]

    phi_ls's second coordinate is the width f_u - f_l. negative entries: 3 of 7
    phi_cw's second coordinate is the half-width. negative entries: 3 of 7

    ========================================================================
    E. I-BK1 itself, the only problem the module actually carries
    ========================================================================
    objective 1: well ordered at all 200000 points: True
    objective 2: well ordered at all 200000 points: True
    min over the sample of (upper - lower), objective 1: 0.000130, objective 2: 0.000075

### 1.3 what the output says, stated plainly

**the returned interval is not well ordered on the negative side of the crossing.**
`lower` exceeds `upper` at every sampled point with `x_1 < 0`, exactly and by the
factor `b/a`. the code agrees with definition 2.1(iii) where `h ≥ 0` and disagrees
where `h < 0`, which is the whole of the claim.

**and the failure does not stop at the pair.** block D pushes the ill-ordered pair
through `phi_registry[...].of_endpoints`, and every phi carries it forward without
complaint. phi_ls's second image coordinate is the width `f_u − f_l` and phi_cw's
is the half-width; both come out **negative** at three of the seven points. a
negative width is not a quantity the framework has a meaning for — [1]'s examples
2.3 and 2.4 read it as the second coordinate of an automorphism of ℝ², which is
defined on any pair, so nothing raises — and it would enter dominance, the
reference-front machinery and every metric as an ordinary number.

**block E is the reason nothing has gone wrong.** I-BK1's four `h_ij` are squares,
so at 200000 uniform points of `[−10, 10]²` both objectives are well ordered and
both widths are strictly positive. that is not luck: it is the condition
`src/problems_native.py`'s head comment names, citing [16] printed page 27 and
lit_review section 1.7, and f2 section 0 checked it before deriving.

### 1.4 the verdict, and what should be registered

**the code is right on everything it has run and is not a general implementation of
definition 2.1(iii).** three things follow, and none of them is done here.

    the operation is missing rather than wrong. there is no primitive to fix;
        `src/interval_math.py` would gain one, `moore_product(a_l, a_u, h)`
        returning `np.minimum` and `np.maximum` over `a_l*h` and `a_u*h`, and
        `objective_endpoints` would call it per term before summing. that is a
        change to evaluation semantics and belongs to its own session.
    the absent guard is the more serious half. **nothing anywhere in `src/`
        asserts `f_l ≤ f_u`.** a cheap and independently useful change is an
        assertion at the `Problem` boundary, which would have turned this session's
        finding into a test failure the first time a sign-changing problem was
        added. it is cheap because every problem in the project passes it, part 2
        below.
    the module comment is currently the only guard, and it is a comment. it names
        the condition correctly and for the right problem; it does not survive
        someone adding a twenty-first problem to the same registry.

proposed for registration by the research chat, not registered here, since this
session commits only this document: **r-23**, the fixed-order product and the
missing well-ordering guard, with this section as its evidence.


## 2. which problems already run could trigger it

per problem and per objective. the question is whether any interval coefficient
multiplies a function that changes sign on that problem's own box.

**p0.** `n = 1`, `m = 2`, box `[−1, 1]`, [1] lines 752-753. **no interval
coefficient exists.** [1] gives the two boundary functions directly,
`F_1 = [−|x|, |x|]` and `F_2 = [0, x²]`, so there is no ⊙ to interchange. the pair
is well ordered by construction, `−|x| ≤ |x|` and `0 ≤ x²`. **p0 nonetheless has
the kink**, because its half-width is written as `|x|`; that is the same symptom
reached by a different route and section 4 returns to it.

**p1.** `n = 2`, `m = 2`, box `[−0.5, 1.5]²`. **no interval coefficient exists**;
`src/problems_tier0.py` returns `(c_i, r_i)` with `r_1 = ρx_2² + δ` and
`r_2 = ρx_1² + δ`. both are sums of a non-negative term and `δ = 1/8 > 0`, so
`r_i ≥ δ` everywhere and the derived endpoints `c ∓ r` are well ordered with a
margin. no function of x is multiplied by anything imprecise.

**zdt1_interval.** `n = 30`, `m = 2`, box `[0, 1]^30`. **no interval coefficient
exists.** `r_i = eps·((x_driver − ½)² + 1/20) ≥ eps/20 ≥ 0`, a product of a
non-negative level and a strictly positive quadratic. at `eps = 0` it is exactly
zero and the interval degenerates to a point, which is the crisp baseline and not
an interchange.

**dtlz2_interval.** `n = 12`, `m = 3`, box `[0, 1]^12`. **no interval coefficient
exists.** `r_i = eps·x_driver` with `x_driver ∈ [0, 1]`, so `r_i ≥ 0` on the box.
the one thing worth naming: `r_i` here is the only half-width in the project that is
non-negative **because of the box** rather than because of its form. `eps·x` is
negative for `x < 0`, so a box change that admitted negative drivers would produce
`f_l > f_u` with no ⊙ involved at all. the unit cube is [3] section vii.b's own and
is not going to move, so this is a note and not a defect.

**I-BK1.** `n = 2`, `m = 2`, box `[−10, 10]²`, [16] printed page 27. **four interval
coefficients, and every one of them multiplies a square.** `h_11 = x_1²`,
`h_12 = x_2²`, `h_21 = (x_1 − 5)²`, `h_22 = (x_2 − 5)²`, all non-negative on the box
and on all of ℝ². each vanishes on an interior line — `x_1 = 0`, `x_2 = 0`,
`x_1 = 5`, `x_2 = 5` — and **touching zero is not a sign change**: the interval
collapses to a point there and the boundary functions coincide rather than
interchanging. `G_1` is degenerate only at the origin and `G_2` only at `(5, 5)`,
both isolated points of the box.

measured, as a check on the argument rather than a substitute for it, at 200000
uniform points of each problem's own box:

    p0                            objective 1 ok, objective 2 ok
    p1  (rho=1/4, delta=1/8)      objective 1 ok, objective 2 ok, half-width >= 0.125
    zdt1_interval  eps=0.0        half-width identically 0
    dtlz2_interval eps=0.0        half-width identically 0
    zdt1_interval  eps=0.5        half-width in [0.025, 0.149998]
    dtlz2_interval eps=0.5        half-width in [9.3e-07, 0.499999]
    ibk1                          objective 1 ok, objective 2 ok

with `f_l ≤ f_u` at all 200000 points of every objective of every problem.

**the conclusion, and it is the one the brief anticipated.** no problem the project
has run can trigger the defect, and that is a fact about which problems were
selected rather than about the method. three of the five were constructed by the
project with a non-negative half-width by design, one is [1]'s own two-line example
with its endpoints written out, and the fifth was chosen — f2 section 0, on
lit_review's reading — partly *because* its `h_ij` are squares.


## 3. all twenty of appendix A, against both criteria

### 3.1 the baseline criterion A measures distance from

stated exactly, because the brief's summary needs one correction before it can be
used as a yardstick. **what has been run and what has been derived are not the same
set.**

    derived in closed form   p0    n=1, m=2, 4 columns. non-smooth. b1 section 1.5:
                                   the derivation does **not** close at the anchor.
                             p1    n=2, m=2, 4 columns. diagonal quadratics,
                                   constant Hessians, project-chosen widths.
                             I-BK1 n=2, m=2, 4 columns. diagonal quadratics,
                                   constant Hessians, published coefficients.
    run but never derived    zdt1_interval  n=30, m=2. square-root centre, quadratic
                                   half-width.
                             dtlz2_interval n=12, m=3. trigonometric centres, linear
                                   half-widths.

so the brief's "everything run so far is n = 2 or 3" holds of the **derivations**,
where the true range is n = 1 or 2, and not of the runs, which reach n = 30. the
consequence for criterion A is that **higher n is underexplored for derivation and
not for evaluation**, and a candidate at n = 3 or 4 buys a first derivation at that
size rather than a first problem at that size.

what is genuinely untouched, in the project's whole history:

    a closed-form derivation at m = 3, hence at 2m = 6 image columns and on a
        five-dimensional weight simplex. **never done.** b1 and f2 both worked a
        three-dimensional simplex into ℝ².
    a closed-form derivation of a non-polynomial objective. **never done.**
    an interval coefficient on a sign-changing function, anywhere, in any problem,
        run or derived. **never, and part 2 above is why.**

### 3.2 two structural facts the ranking needs, and one of them is new

**fact one: the interchange test is about non-degenerate coefficients, and
lit_review's prose does not always separate them.** `[q, q] ⊙ h` is a real scalar
times `h` for any sign of `h`: both endpoint products coincide and the minimum and
the maximum agree with the fixed order. so a sign-changing `h` under a degenerate
coefficient interchanges nothing. this matters for two rows. **I-KW2** carries
`[10, 10] ⊙ ((1/5)x_1 − x_1³ − x_2⁵)exp(...)`, whose factor takes both signs on
`[−3, 0] × [−1, 2]`, and **I-PNR** carries `[10, 10] ⊙ x_1x_2` and `[¼, ¼] ⊙ x_1`,
both sign-changing on `[−2, 2]²`. **neither problem has an interchange**, though
lit_review section 1.9's criterion-2 prose for I-KW2 names "sign-changing factors"
among its reasons. those rows fail on convexity, which is untouched by this
correction; what changes is the reason, and it is recorded so the memoria does not
repeat it.

**fact two, and it is new to this session: part1_closing section 6.1's degeneracy
can be decided exactly from the printed coefficients, and it disqualifies eight of
the twenty.** for `G_i = ⊕_j [a_j, b_j] ⊙ h_j` with every `h_j` of constant sign,

    centre       c_i = Σ_j m_j h_j,     m_j = (a_j + b_j)/2
    half-width   r_i = Σ_j w_j h_j,     w_j = (b_j − a_j)/2

so `r_i` is an exact affine function of `c_i` **iff the vectors `(w_j)` and `(m_j)`
over the non-constant terms are parallel**, i.e. iff `ρ_j := w_j/m_j` is one number
across `j`. constant interval terms shift `c` and `r` and never break parallelism.
part1_closing section 6.1 states the degeneracy as "a half-width that is any exact
function of the centre" and measured it on zdt1 with `f_1 = c_1x_1`,
`c_1 ∈ [1−d, 1+d]`: correlation +1.0000 and phi_cw returning the crisp non-dominated
set exactly. **f2 section 0 ran this check on five problems; it is run here on all
twenty**, in exact rational arithmetic from `fractions`, sympy not being in the venv
and CONTEXT.md section 11 not permitting a dependency added for one session — the
same constraint b1 and f2 worked under.

**what a parallel objective costs, stated precisely rather than by analogy.** with
`r = αc + β` the six image columns of that objective are

    phi_lu   (c − r, c + r) = ((1−α)c − β, (1+α)c + β)
    phi_ls   (c − r, 2r)    = ((1−α)c − β, 2αc + 2β)
    phi_cw   (c, r)         = (c, αc + β)

for `0 < α < 1`, which is what `ρ = (b−a)/(b+a)` always gives for `0 < a < b`, **all
six are strictly increasing in `c`**, so all three phi order that objective exactly
as the crisp centre does and the objective is blind to the choice of order. for
`α < 0` the picture inverts and is no better: phi_ls's and phi_cw's second columns
decrease in `c` while the first increases, so **no two points with distinct `c` are
comparable on that objective at all**, which is the saturation
docs/part1/a1_uncertainty_model.md part 4 measured on the linear zdt1 half-width.
either way the objective carries no information about the comparison the project
exists to make.

**one corollary that decides several rows at a glance: any objective that is a
single interval coefficient times one function is degenerate**, the parallelism
being vacuous at one term. and if that one `h` changes sign, then `c = mh` and
`r = w|h|` give `r = ρ|c|`: a V rather than a ray, still a one-dimensional image,
still degenerate.

the computation, verbatim, over all twenty:

    ==============================================================================
    rho_j = w_j / m_j per non-constant term. equal across terms  =>  r = alpha c + beta
    ==============================================================================
     1 I-BK1      G1   x1^2:1/3, x2^2:1/2                    not parallel -> (c, r) image is two-dimensional
     1 I-BK1      G2   (x1-5)^2:1/2, (x2-5)^2:2/3            not parallel -> (c, r) image is two-dimensional
     2 I-VU2      G1   x1:1/5, x2:1/5                        r = (1/5) c + (-1/5)   AFFINE in the centre
     2 I-VU2      G2   x1^2:1/5, x2^2:1/5                    r = (1/5) c   PROPORTIONAL
     3 I-CH       G1   (x1-1)^2+(x2-2)^2:0                   width IDENTICALLY ZERO on the variable part
     3 I-CH       G2   x1^2-x2:1/5                           r = (1/5) c + (2)   AFFINE in the centre
     5 I-KW2      G1   (1-x1)^2 E:-1/4, poly*E:0, E:1/4      not parallel -> two-dimensional
     5 I-KW2      G2   (1+x2)^2 E:-1/4, poly*E:0, E:1/4      not parallel -> two-dimensional
     6 I-Far1     G1   E1:-1/3, E2:-1/3, E3:1/2, E4:1/3, E5:1/3    not parallel -> two-dimensional
     6 I-Far1     G2   E1:1/3, E2:1/3, E3:-1/3, E4:-1/3, E5:2/3    not parallel -> two-dimensional
     7 I-Hil1     G1   H1:1/3                                r = (1/3) c   PROPORTIONAL
     7 I-Hil1     G2   H2:1/2                                r = (1/2) c   PROPORTIONAL
     8 I-PNR      G1   x1^4+x2^4:1/5, x1^2+x2^2:4/9, x1x2:0, x1:0   not parallel -> two-dimensional
     8 I-PNR      G2   (x1-1)^2:1/3, x2^2:1/5                not parallel -> two-dimensional
     9 I-Deb      G1   x1:1/3                                r = (1/3) c   PROPORTIONAL
    11 I-IKK1     G1   x1^2:0, x2^2:1                        not parallel -> two-dimensional
    11 I-IKK1     G2   (x1-20)^2:0, (x2-20)^2:1              not parallel -> two-dimensional
    11 I-IKK1     G3   x1^2:1, x2^2:0                        not parallel -> two-dimensional
    12 I-VFM1     G1   x1^2:1/3, (x2-1)^2:1/2                not parallel -> two-dimensional
    12 I-VFM1     G2   x1^2:1/2, (x2+1)^2:1/3                not parallel -> two-dimensional
    12 I-VFM1     G3   (x1-1)^2:1/3, x2^2:2/3                not parallel -> two-dimensional
    13 I-MHHM2    G1   (x1-.8)^2:1/5, (x2-.6)^2:1/3          not parallel -> two-dimensional
    13 I-MHHM2    G2   (x1-.85)^2:1/3, (x2-.7)^2:1/5         not parallel -> two-dimensional
    13 I-MHHM2    G3   (x1-.9)^2:1/9, (x2-.6)^2:1/11         not parallel -> two-dimensional
    14 I-Viennet  G1   x1^2+x2^2:1/3, sin(x1^2+x2^2):1/3     r = (1/3) c   PROPORTIONAL
    14 I-Viennet  G2   (3x1-2x2+4)^2:1/3, (x1-x2+1)^2:1/2    not parallel -> two-dimensional
    15 I-AP1      G1   (x1-1)^4+2(x2-2)^4:1/3                r = (1/3) c   PROPORTIONAL
    15 I-AP1      G2   exp((x1+x2)/2):1/3, x1^2+x2^2:1/5     not parallel -> two-dimensional
    15 I-AP1      G3   exp(-x1)+2exp(-x2):1/5                r = (1/5) c   PROPORTIONAL
    16 I-MOP7     G1   (x1-2)^2:1/3, (x2+1)^2:1/3            r = (1/3) c + (-1/3)   AFFINE in the centre
    16 I-MOP7     G2*  (x1+x2-3)^2:5/13, (-x1+x2+2)^2:1/3    not parallel -> two-dimensional
    16 I-MOP7     G3*  (x1+2x2-1)^2:9/16, (-x1+2x2)^2:1/3    not parallel -> two-dimensional
    17 I-VFM2     G1   x1^2:1/3, x2^2:1/2, x3^2:1/3          not parallel -> two-dimensional
    17 I-VFM2     G2   (x1-5)^2:1/2, (x2-5)^2:2/3, (x3-5)^2:3/5   not parallel -> two-dimensional
    19 I-AP4      G1   (x1-1)^4+2(x2-2)^4+3(x3-3)^4:1/2      r = (1/2) c   PROPORTIONAL
    19 I-AP4      G2   exp((x1+x2+x3)/3):1/5, x1^2+x2^2+x3^2:3/7   not parallel -> two-dimensional
    19 I-AP4      G3   3e^-x1+4e^-x2+3e^-x3:1/7              r = (1/7) c   PROPORTIONAL
    20 I-Comet    G1   (1+x3)q1:1/5                          r = (1/5) c   PROPORTIONAL
    20 I-Comet    G2   (1+x3)q2:1/5                          r = (1/5) c   PROPORTIONAL
    20 I-Comet    G3   (1+x3)x1^2:2/3                        r = (2/3) c   PROPORTIONAL

    ==============================================================================
    the (-)gH problems, worked by the midpoint-radius formula
    A (-)gH B = (c_A - c_B ; |r_A - r_B|), [10] section 2 printed page 3
    ==============================================================================
     4 I-FON     G1   r = (1/2)(1 - c)   AFFINE, slope NEGATIVE
     4 I-FON     G2   r = (2/3)(1 - c)   AFFINE, slope NEGATIVE
     2 I-VU2     G2   (-)gH [1,1] is a real shift, r unchanged: r = (1/5)(c + 1)  AFFINE
    18 I-TR1     G1   r = (1/2)|c - (15/2)|   AFFINE IN |c|, WITH A KINK
    18 I-TR1     G2   r = (1/3)|c - (5)|      AFFINE IN |c|, WITH A KINK
    18 I-TR1     G3   r = (1/2)|c - (15)|     AFFINE IN |c|, WITH A KINK
    16 I-MOP7    G2   r = |r_A - 3/2| with r_A not parallel to c_A: two-dimensional, kinked
    16 I-MOP7    G3   r = |r_A - 1|   with r_A not parallel to c_A: two-dimensional, kinked
    17 I-VFM2    G3   r = |0.05 x1^2 - 0.1 x2^2 (- 0.05 x3^2)|: two-dimensional, kinked (a-7)
    14 I-Viennet G3   r = |R/8 - E/10| with R, E independent: two-dimensional, kinked
     9 I-Deb     G2   nested (-)gH under a 1/x1 scale, scope unresolved (a-6): not computed

I-SD's coefficients are irrational and were computed separately in floating point:
`G_1` gives `ρ = (0.200000, 0.101021, 0.101021, 0.500000)` and `G_2` gives
`(0.200000, 0.295059, 0.295059, 0.200000)`. **neither is constant, so neither
objective is degenerate.**

three of the rows above need a word the table cannot carry.

    **I-Viennet G_1 is worse than the table says.** the two terms share `ρ = 1/3`,
        but `sin` changes sign so the half-width picks up an absolute value and
        `r_1 = c_1/3` holds only where `sin ≥ 0`. the real statement is stronger:
        `G_1 = [0.5,1] ⊙ s ⊕ [1,2] ⊙ sin(s)` with `s = x_1² + x_2²` is **a function
        of the single scalar `s` alone**, so its image in the (centre, half-width)
        plane is a one-parameter curve however the signs fall. measured: over
        400000 uniform points of `[−3, 3]²`, the ten sampled pairs agreeing in `s`
        to `1e−9` agree in the centre to `2.0e−09` and in the half-width to
        `6.2e−10`, with `s` spanning `[0.0001, 17.9454]`.
    **I-Hil1, I-Comet G_1 and G_2, and I-CH G_2 are the `r = ρ|c|` form**, their
        single `h` changing sign. one-dimensional image, with a fold at the
        crossing rather than a ray.
    **I-CH G_1's half-width is the constant 1**, its only non-constant term
        carrying the degenerate coefficient `[1, 1]` and its whole interval-valuedness
        sitting in the constant band `[−1, 1]`. that is part1_closing section 6.1's
        opening case — "slide 19's literal tier 1 prescription ... is a constant
        half-width" — **occurring verbatim in a published problem**, and it is why
        lit_review section 1.9 also fails I-CH on criterion 5.

### 3.3 the crossing loci, confirmed over each box

200000 uniform points per box. a term is reported as an interchange only when its
coefficient interval is non-degenerate.

    2  I-VU2   G1 t1   [1, 1.5]      h in [-4, 4]           INTERCHANGE  locus x1 = 0
    2  I-VU2   G1 t2   [1, 1.5]      h in [-4, 4]           INTERCHANGE  locus x2 = 0
    3  I-CH    G2 t1   [2, 3]        h in [-4, 28.94]       INTERCHANGE  locus x2 = x1^2, |x1| <= 2
    5  I-KW2   G1 t2   [10, 10]      h in [-0.81, 0.36]     degenerate coefficient: no interchange
    5  I-KW2   G2 t2   [10, 10]      h in [-0.81, 0.36]     degenerate coefficient: no interchange
    7  I-Hil1  G1 t1   [1, 2]        h in [-0.36, 1.46]     INTERCHANGE  locus 40sin(2pi x1)+25sin(2pi x2) = 45
    7  I-Hil1  G2 t1   [1, 3]        h in [-0.36, 1.46]     INTERCHANGE  locus 40sin(2pi x1)+25sin(2pi x2) = -45
    8  I-PNR   G1 t3   [10, 10]      h in [-3.99, 3.99]     degenerate coefficient: no interchange
    8  I-PNR   G1 t4   [0.25, 0.25]  h in [-2, 2]           degenerate coefficient: no interchange
    14 I-Vien  G1 t2   [1, 2]        h in [-1, 1]           INTERCHANGE  loci x1^2+x2^2 = k pi, k = 1..5
    20 I-Comet G1 t1   [1, 1.5]      h in [-69.25, 273.2]   INTERCHANGE  locus x1^3 x2^2 = 10x1 + 4x2
    20 I-Comet G2 t1   [1, 1.5]      h in [-69.07, 278.3]   INTERCHANGE  locus x1^3 x2^2 = 10x1 - 4x2

every other term of every other problem has an `h` of constant sign on its own box;
the sweep prints `sign change: False` for each and they are not listed.

**so exactly five of the twenty interchange: I-VU2, I-CH, I-Hil1, I-Viennet and
I-Comet.** the ⊖gH kinks, which are a different mechanism producing the same
symptom, were checked in the same sweep and one earlier reading is corrected:

    16 I-MOP7  G2   r_A in [0.025, 4.47e+04], crosses 1.5:  True   kink reached
    16 I-MOP7  G3   r_A in [0.118, 7.65e+04], crosses 1.0:  True   kink reached
    17 I-VFM2  G3   argument in [-9.997, 4.997], crosses 0: True   kink reached
    18 I-TR1   G1   p in [6.62, 328.9],  kink at p = 75:    True   kink reached
    18 I-TR1   G2   p in [8.54, 407.1],  kink at p = 200:   True   kink reached
    18 I-TR1   G3   p in [10.83, 487.6], kink at p = 150:   True   kink reached
    14 I-Vien  G3   R/8 - E/10 changes sign:                False  **kink NOT reached**

**correction to lit_review section 1.8's closing paragraph as applied to
I-Viennet.** that paragraph says a ⊖gH against a non-degenerate interval "acquires a
kink wherever the two half-widths are equal". true in general, and **not reached on
I-Viennet's box**: with `R = 1/(s+1)` and `E = e^{−s}`, `R/8 − E/10` is `0.025` at
`s = 0` and stays positive for all `s ≥ 0`, since `e^{−s}` decays faster than
`1/(s+1)`. so I-Viennet's `G_3` is smooth. **the verdict does not move** — I-Viennet
fails criterion 2 on convexity and its `G_1` is degenerate — but the reason is now
narrower than lit_review implies.

### 3.4 the two criteria, kept apart

**they pull against each other and are not blended.** criterion A rewards distance
from what has been derived; criterion B rewards a route that closes. the appendix
is built so that almost everything scoring well on A scores badly on B, and the
table below is worth reading for that fact alone.

**the cost unit, defined in what b1, f2 and this project have actually spent.**
one **f2-session** is: image coordinates written out, phi-convexity by theorem 3.3
of [1], regularity by [10] proposition 32 then theorem 34, condition (15) of
example 3.9 for the candidate set, example 3.8 statement 3 to lift weak optimality
to optimality, exact-rational symbolic verification from `fractions`, and the
write-up — at `n = 2`, `m = 2`, four image columns with constant diagonal Hessians,
where (15) decouples into two scalar equations. b1 spent one such session on p1 and
f2 one on I-BK1. lit_review section 7.4 prices the **encoding and statistics** —
the closed form as a reference set, the reference-front machinery, the exact
overlaps — at a **second** session, and part2_closing section 7.2 repeats that
price for I-IKK1. costs below are quoted in those two units and the run, which
needs compute, is priced separately at one session wherever it is wanted.

**where m = 3 costs more than the table's "cheap" suggests.** at `m = 2` the weight
simplex is three-dimensional and (15) maps it into ℝ²; at `m = 3` there are six
image coordinates and a **five-dimensional weight simplex**, and the elimination
that turns `x(w)` into a region — f2 section 2.4's collapse onto the single
quantity `ν`, b1 section 2.1's two scalar equations — has two more parameters to
carry. at `m = 3` **and** `n = 3` the map goes from that five-simplex into ℝ³ and
the derived set is a region of a three-dimensional box rather than of a plane.
**derivable in principle, considerably more work in practice**, and nothing in the
project has done either.

    #   name        n  m  2m  functional class            interchange (locus)              6.1 degeneracy                B: derivability            A: what it adds that nothing tests   cost
    1   I-BK1       2  2  4   diagonal quadratic          none (all h are squares)         none, both objectives         DONE, f2                   nothing; it is the baseline          spent
    2   I-VU2       2  2  4   G1 piecewise-linear,        **yes**, G1 on x1=0 and x2=0,    **G2: r = c/5**, phi-blind    closes per open quadrant,  **the interchange, first anywhere**  1 + 1
                                G2 diagonal quadratic       both interior lines                                          **fails at the crossing**
    3   I-CH        2  2  4   quadratic; quadratic-minus  **yes**, G2 on x2=x1²,           **G1: r ≡ 1 constant.**       fails c5 and c2            nothing usable                       —
                                -linear                     |x1|<=2, interior              **G2: r = |c|/5 + 2**
    4   I-FON       2  2  4   Gaussian                    none (exp > 0)                   **both: r affine in c,        fails c2 (convexity)       nothing usable                       —
                                                                                             negative slope**
    5   I-KW2       2  2  4   polynomial x Gaussian       none: the sign-changing factor   none                          fails c2 (no convexity,    non-convexity, untestable            —
                                                            carries [10,10]                                                no constant Hessians)
    6   I-Far1      2  2  4   sum of five Gaussians       none (exp > 0)                   none                          fails c2 (no convexity)    nothing usable                       —
    7   I-Hil1      2  2  4   doubly oscillatory trig     **yes**, both objectives,        **both: r = ρ|c|**            fails c2 outright          nothing usable                       —
                                                            40sin+25sin = ±45
    8   I-PNR       2  2  4   quartic + bilinear cross    none: x1x2 and x1 carry          none                          fails c2 (indefinite       nothing usable                       —
                                                            degenerate coefficients                                        Hessian at the origin)
    9   I-Deb       2  2  4   rational x Gaussian         none                             **G1: r = c/3**              fails c2; a-6 unresolved   nothing usable                       —
    10  I-SD        4  2  4   G1 linear, G2 reciprocal    none (x > 0 on the box)          none, both objectives         **passes**, diagonal-      **n = 4 derived, and the first        1-2 + 1
                                                                                                                          but-not-constant           non-polynomial derivation**
    11  I-IKK1      2  3  6   diagonal quadratic          none                             none, all three               **passes, cheap**          **m = 3 derived; c4 on three         1-2 + 1
                                                                                                                                                      columns; outside the alignment
                                                                                                                                                      regime**
    12  I-VFM1      2  3  6   diagonal quadratic          none                             none, all three               **passes, cheap**          m = 3 derived, and nothing else      1-2 + 1
    13  I-MHHM2     2  3  6   diagonal quadratic          none                             none, all three               **passes, cheap**          m = 3 derived; cleanest c5 in the    1-2 + 1
                                                                                                                                                      appendix; strict interiority
    14  I-Viennet   2  3  6   quad + sin; quad form;      **yes**, G1 on x1²+x2² = kπ,     **G1 is a function of         fails c2 (no convexity)    nothing usable                       —
                                rational − Gaussian         k = 1..5                         s = x1²+x2² alone**
    15  I-AP1       2  3  6   quartic; exp + quadratic;   none                             **G1: r = c/3.**              **c2 not determinable**;   non-polynomial at m = 3, but         3+, may
                                sum of exponentials                                          **G3: r = c/5**              two of three degenerate     two objectives are blind             not close
    16  I-MOP7      2  3  6   quadratic forms, ⊖gH        none                             **G1: r = (c−1)/3**           fails c2 (⊖gH kink,        nothing usable                       —
                                                                                                                          reached in the box)
    17  I-VFM2      3  3  6   diagonal quadratic, ⊖gH     none                             none (G1, G2)                 fails c2 (⊖gH kink on G3,  n = 3 and m = 3, if G3 were fixed    —
                                                                                                                          reached; a-7)
    18  I-TR1       3  3  6   cubic under ⊖gH             none (p > 0)                     **all three: r = ρ|c − k|,    fails c2 (kink reached     nothing usable                       —
                                                                                             kink reached**                on all three)
    19  I-AP4       3  3  6   quartic; exp + quadratic;   none                             **G1: r = c/2.**              **c2 not determinable**;   n = 3, m = 3, non-polynomial, but    3+, may
                                sum of exponentials                                          **G3: r = c/7**              two of three degenerate     two objectives are blind             not close
    20  I-Comet     3  3  6   degree-5 polynomial x       **yes**, G1 and G2,              **all three: r = ρc or        fails c2 (no convexity)    nothing usable                       —
                                (1 + x3)                    x1³x2² = 10x1 ± 4x2              ρ|c|**

**what changed against lit_review section 1.9, and it is a narrowing not a
reversal.** that section left **I-AP1 and I-AP4 as "not determinable"**, on the
ground that all twelve image coordinates are convex but (15) is a coupled nonlinear
system. section 3.2 above adds a verdict it did not have: **two of the three
objectives of each are degenerate in the sense of part1_closing section 6.1** —
`r = c/3` and `r = c/5` on I-AP1, `r = c/2` and `r = c/7` on I-AP4 — because each is
a single interval coefficient on one function. so even if (15) turned out solvable,
**only `G_2` of each would discriminate between the three phi at all**, the other two
reproducing the crisp order under every one of them. together with the `e^{±100}`
range on their boxes, already recorded by lit_review as a reservation, that removes
both from serious consideration and reduces the shortlist to the problems section 5
names. **the three problems lit_review recommended — I-BK1, I-IKK1 and, behind
them, I-SD, I-VFM1 and I-MHHM2 — all survive the new check with no objective
degenerate.**

### 3.5 the twenty, one block each

each block states dimensions and box from [16] appendix A as transcribed in
lit_review section 1.8 and re-read this session from printed pages 27-31; the
functional class; the interchange and its locus; the section 6.1 check; convexity,
differentiability and the Hessians; what it would add; and cost. **judgements marked
"guess" are guesses.**

**1. I-BK1.** `n=2`, `m=2`, `2m=4`, `[−10,10]²`, p.27. diagonal quadratic. no
interchange, every `h` a square. no degeneracy: `ρ = (1/3, 1/2)` and `(1/2, 2/3)`.
all twelve image coordinates convex with constant diagonal Hessians, f2 section 1.2.
**already derived**; it is the baseline criterion A measures against, and a second
problem of its shape would say nothing new — part2_closing section 4.

**2. I-VU2.** `n=2`, `m=2`, `2m=4`, `[−4,4]²`, p.28. `G_1` is affine in `x` under a
sign-changing product, `G_2` a diagonal quadratic with a real shift. **interchange
on `x_1 = 0` and `x_2 = 0`**, two lines through the interior of the box and meeting
at the origin. `G_2` is degenerate, `r_2 = c_2/5` with `0 < 1/5 < 1`, hence
phi-blind. `G_1` is **not** degenerate: `r_1 = ¼(|x_1| + |x_2|)` is not determined by
`c_1 = 1.25(x_1 + x_2) + 1`. the boundary functions, written out and confirmed
numerically against the module's own arithmetic on the `x_1` axis:

    G̲_1 = 1.25(x_1+x_2) − 0.25(|x_1|+|x_2|) + 1      a min of affine pieces, CONCAVE
    Ḡ_1 = 1.25(x_1+x_2) + 0.25(|x_1|+|x_2|) + 1      a max of affine pieces, convex

so **theorem 3.3 fails under phi_lu and phi_ls** (`Λ_1^T f = G̲_1` is concave) and
**holds under phi_cw** (`Λ_1^T f = c_1` is affine, `B_1^T f = ¼(|x_1|+|x_2|)` is
convex); and **example 3.9's differentiability fails on the two axes under all
three**, since each `φ_i` is invertible and differentiability of the image
coordinates is equivalent to differentiability of the endpoint functions, a0 c14.
**this is p0's failure exactly, on a published problem.** section 4 argues that the
crossing meets the answer. cost: the smooth part is four open quadrants, on each of
which the problem is affine-plus-diagonal-quadratic and b1's route closes cheaply,
so **1 f2-session for the quadrant-wise derivation plus the failure statement, and 1
for the encoding**.

**3. I-CH.** `n=2`, `m=2`, `2m=4`, `[−5,5]×[−4,4]`, p.28. **interchange on the
parabola `x_2 = x_1²`, `|x_1| ≤ 2`, interior.** disqualified twice over before the
interchange matters: `G_1`'s half-width is the **constant 1**, its only variable term
carrying `[1,1]`, which is part1_closing section 6.1's opening case in a published
problem and lit_review's only criterion-5 failure; and `G_2` gives `r = |c|/5 + 2`.
**unusable.**

**4. I-FON.** `n=2`, `m=2`, `2m=4`, `[−2,2]²`, p.28. Gaussian. no interchange,
`exp > 0`. **both objectives degenerate**: `[1,1] ⊖gH [1,k] ⊙ E` gives `c = 1 −
(1+k)E/2` and `r = (k−1)E/2`, hence `r = ((k−1)/(k+1))(1 − c)` — affine in the
centre with **negative** slope, `−1/2` and `−2/3`. by section 3.2's column algebra
that is the saturating case: phi_ls's and phi_cw's two columns move oppositely in
`c`, so on each objective no two points with distinct centres are comparable, and
since **both** objectives are of that form the phi_ls and phi_cw efficient sets are
essentially the whole box. fails criterion 2 independently on convexity, `1 − 2E`
being convex only where the Gaussian is concave. **unusable.**

**5. I-KW2.** `n=2`, `m=2`, `2m=4`, `[−3,0]×[−1,2]`, p.28. polynomial times
Gaussian. **no interchange**: the only sign-changing factor carries the degenerate
`[10,10]`, and the three non-degenerate coefficients sit on `(1−x_1)²exp`,
`(1+x_2)²exp` and `exp`, all non-negative on the box. no degeneracy. fails criterion
2 on convexity and constant Hessians, lit_review 1.9, and the a-5 asymmetry does not
touch that. **the reason recorded in lit_review's prose — "sign-changing factors" —
is corrected here; the verdict is not.**

**6. I-Far1.** `n=2`, `m=2`, `2m=4`, `[−1,1]²`, p.28-29. five Gaussians per
objective. no interchange. no degeneracy, `ρ` taking five values per objective and
mixed in sign. fails criterion 2 on convexity. **unusable.**

**7. I-Hil1.** `n=2`, `m=2`, `2m=4`, `[−1,1]²`, p.29. doubly oscillatory
trigonometric. **interchange in both objectives**, `cos θ` vanishing where
`40 sin(2πx_1) + 25 sin(2πx_2) = 45` and `sin θ` where it is `−45`, both attainable
since the amplitude is 65 and both interior. **both objectives degenerate**,
`r = |c|/3` and `r = |c|/2`, each being one coefficient on one function. no
convexity anywhere. **unusable**, and it is the clearest case in the appendix of a
problem that has the crossing and is worthless for testing it.

**8. I-PNR.** `n=2`, `m=2`, `2m=4`, `[−2,2]²`, p.29. quartic plus quadratic plus a
bilinear cross term. **no interchange**: `x_1x_2` and `x_1` change sign but carry
`[10,10]` and `[¼,¼]`. no degeneracy. fails criterion 2: the cross term makes the
Hessian at the origin `[[2,10],[10,2]]`, indefinite, so the centre and both endpoint
coordinates are non-convex; the half-width alone is convex. **the second row whose
lit_review reason is narrowed here and whose verdict is not.**

**9. I-Deb.** `n=2`, `m=2`, `2m=4`, `[1,3]×[−1,1]`, p.29. rational times Gaussian.
no interchange, `x_1 ≥ 1 > 0`. **`G_1` degenerate**, `r = c/3`, one coefficient on
one function — which is also lit_review's criterion-4 row, `x_2` free in objective 1;
the degeneracy is the stronger statement and subsumes it. fails criterion 2. the
scope of the `1/x_1` factor is **a-6, unresolved**, and the verdict holds under both
readings. **unusable.**

**10. I-SD.** `n=4`, `m=2`, `2m=4`, `[1,6]×[√2,6]×[√2,6]×[1,6]`, p.29. `G_1` linear,
`G_2` a sum of reciprocals — **the only non-polynomial objective in the appendix on
which b1's route closes.** no interchange, every `h` strictly positive on the box.
no degeneracy: `ρ = (0.200000, 0.101021, 0.101021, 0.500000)` and
`(0.200000, 0.295059, 0.295059, 0.200000)`, measured, neither constant. all twelve
image coordinates convex, lit_review 1.9; `G_1`'s Hessians are **zero** and `G_2`'s
are diagonal with entries `2λ_j/x_j³`, so (15) decouples into four scalar equations
`a − b/x_j² = 0` with the closed-form root `x_j = √(b/a)`. **what it adds: the first
derivation above `n = 2` and the first of a non-polynomial objective.** two risks
this session can name and not settle. **first, interiority.** condition (15) carries
no constraint multipliers and b1 reads example 3.9 as an interior condition, b1
section 2 and the box note in `src/problems_tier0.py`; on a two-objective problem the
efficient set has each objective's own minimiser as an endpoint, and here `G_1` is
minimised at `lb` and `G_2` at `ub`, **both corners of the box**. so the route can be
expected to recover the relative interior of the efficient set and not its two ends —
a real limitation, and exactly what p1's box `[−0.5, 1.5]²` was chosen to avoid.
**second, the derived set is a three-dimensional region inside a four-dimensional
box**, the image of a three-simplex, which is more work to describe and to sample
than a plane region and lands on the encoding session rather than the derivation.
cost: **1-2 f2-sessions plus 1 encoding**.

**11. I-IKK1.** `n=2`, `m=3`, `2m=6`, `[−50,50]²`, p.29. diagonal quadratic. no
interchange. no degeneracy — and note the shape, `ρ = (0, 1)` per objective, the
`[1,1]` term contributing centre only and the `[0,1]` term contributing centre and
half-width equally. all image coordinates are non-negative-coefficient diagonal
quadratics with constant diagonal Hessians, so (15) decouples into two scalar
equations exactly as on p1 and I-BK1. **interiority is clean**: the three centres are
minimised at `(0,0)`, `(20,20)` and `(0,0)`, all far inside `[−50,50]²`. what it adds
is what part2_closing section 7.2 already argues at length — **the first derivation
at `m = 3`; a third registered test of the protected-minimiser condition on three
columns at once, x-01; and the one candidate outside the half-width alignment
regime**, its half-widths `½x_2²`, `½(x_2−20)²` and `½x_1²` being minimised on lines
rather than at their centres' minimisers, so it separates "adapted against native"
from "these coefficients against those". **no published checkpoint.** cost: **1-2
f2-sessions plus 1 encoding**, the extra half-session being the five-dimensional
weight simplex rather than any new difficulty in the algebra.

**12. I-VFM1.** `n=2`, `m=3`, `2m=6`, `[−2,2]²`, p.29. diagonal quadratic plus two
degenerate constant shifts `[1,1]` and `[2,2]`, which are real translations. no
interchange, no degeneracy, `ρ = (1/3, 1/2)`, `(1/2, 1/3)`, `(1/3, 2/3)`. constant
diagonal Hessians; centres minimised at `(0,1)`, `(0,−1)` and `(1,0)`, all interior.
**passes cheaply and adds only `m = 3`**: it is I-BK1's shape at three objectives and
inside the alignment regime, so a nesting there would repeat part2_closing section
4's observation without separating its two explanations. cost: **1-2 plus 1**.

**13. I-MHHM2.** `n=2`, `m=3`, `2m=6`, `[0,1]²`, p.29-30. diagonal quadratic,
**six coefficient intervals on six squared displacements and nothing else** — no
constant term of any kind, which lit_review section 1.10 calls the cleanest statement
of criterion 5 in the appendix. no interchange, no degeneracy,
`ρ = (1/5, 1/3)`, `(1/3, 1/5)`, `(1/9, 1/11)`. constant diagonal Hessians; the three
centres are minimised at `(0.8, 0.6)`, `(0.85, 0.7)` and `(0.9, 0.6)`, so **the whole
efficient set is confined to a small interior region of the unit square** — the
strictest interiority in the appendix and the least exposure to the face problem
I-SD carries. **inside the alignment regime**, each half-width minimised where its
own centre is. adds `m = 3` and a clean criterion 5, nothing more. cost: **1-2 plus 1**.

**14. I-Viennet.** `n=2`, `m=3`, `2m=6`, `[−3,3]²`, p.30. `G_1` quadratic plus a
sine of the same quadratic, `G_2` a quadratic form in two affine functions, `G_3` a
rational minus a Gaussian under ⊖gH. **interchange in `G_1` on the circles
`x_1²+x_2² = kπ`, `k = 1..5`**, of which `k = 1, 2` lie wholly inside the box and
`k = 3, 4, 5` meet only its corners. **`G_1` is a function of `s = x_1²+x_2²` alone**,
measured above, so its (centre, half-width) image is a one-parameter curve. `G_3`'s
⊖gH kink is **not** reached, correcting lit_review. fails criterion 2 on convexity.
**unusable.**

**15. I-AP1.** `n=2`, `m=3`, `2m=6`, `[−100,100]²`, p.30. quartic; exponential plus
paraboloid; sum of decaying exponentials. no interchange. **`G_1` and `G_3` are
degenerate**, `r = c/3` and `r = c/5`, each one coefficient on one function; only
`G_2` discriminates. all twelve image coordinates convex, so theorem 3.3 applies, but
the Hessians are neither constant nor diagonal — the exponential's is rank-one and
full — so (15) is a coupled system mixing cubics and exponentials and lit_review
could not say whether it is solvable in closed form. **`exp(−x_j)` on a box reaching
`x_j = −100` spans `e^{100}`**, measured here at `5.3e−44` to `2.6e+43` for
`exp((x_1+x_2)/2)`. **cost 3+ sessions with a real chance of not closing, for a
problem two thirds of which is phi-blind.** not recommended.

**16. I-MOP7.** `n=2`, `m=3`, `2m=6`, `[−400,400]²`, p.30. quadratic forms in affine
functions, two of them under ⊖gH against a constant band. no interchange. **`G_1` is
degenerate**, `r = (c−1)/3`, its two variable terms sharing `ρ = 1/3`. `G_2` and
`G_3` are not degenerate but carry ⊖gH kinks that **are** reached, measured above, so
`G̲_2 = min(A̲ − 17, Ā − 20)` is a minimum of two convex functions and theorem 3.3
fails. Hessians constant but full — lit_review's "constant but not diagonal" widening
of the cheap case, which is recorded there as widening the class and **not** as
rescuing this problem. **unusable.**

**17. I-VFM2.** `n=3`, `m=3`, `2m=6`, `[−5,10]³`, p.30. **I-BK1's shape extended to
three variables in `G_1` and `G_2`** — which is the tantalising part — plus a `G_3`
that fails. no interchange. `G_1` and `G_2` are not degenerate,
`ρ = (1/3, 1/2, 1/3)` and `(1/2, 2/3, 3/5)`. `G_3`'s ⊖gH half-width is
`|0.05x_1² − 0.1x_2²|` under one bracketing and
`|0.05x_1² − 0.1x_2² − 0.05x_3²|` under the other, **a-7 unresolved**, and the
argument changes sign on the box under either reading — measured, `[−9.997, 4.997]`
— so it vanishes on a cone interior to the box and is not convex there. **it would be
the appendix's only `n = 3`, `m = 3` problem with a closing route if `G_3` were
sound, and it is not.** using `G_1` and `G_2` alone would be inventing a problem the
paper does not print, which the project does not do. **unusable as printed.**

**18. I-TR1.** `n=3`, `m=3`, `2m=6`, `[1,4]³`, p.30. cubics under ⊖gH against a
constant band. no interchange, `p_i > 0` on the box. **all three objectives
degenerate, and kinked**: `r = ½|c − 15/2|`, `⅓|c − 5|`, `½|c − 15|`, and the kinks
are reached — `p_1 ∈ [6.62, 328.9]` crossing 75, `p_2 ∈ [8.54, 407.1]` crossing 200,
`p_3 ∈ [10.83, 487.6]` crossing 150, all measured. so the (centre, half-width) image
of every objective is a V, and there is nothing left to test. **unusable.**

**19. I-AP4.** `n=3`, `m=3`, `2m=6`, `[−100,100]³`, p.30-31. I-AP1's structure at
`n = 3`. no interchange. **`G_1` and `G_3` degenerate**, `r = c/2` and `r = c/7`.
same non-constant full Hessians, same unsettled solvability, same `e^{±100}` range
(measured, `3.9e−43` to `7.8e+42`). **cost 3+ with a real chance of not closing, for
a problem two thirds of which is phi-blind.** not recommended.

**20. I-Comet.** `n=3`, `m=3`, `2m=6`, `[1,3.5]×[−2,2]×[0,1]`, p.31. a degree-5
polynomial times `(1+x_3)`. **interchange in `G_1` and `G_2`**, on the surfaces
`x_1³x_2² = 10x_1 + 4x_2` and `x_1³x_2² = 10x_1 − 4x_2`, both reached — the factors
run over `[−69.25, 273.2]` and `[−69.07, 278.3]`. **all three objectives degenerate**,
`r = ρc` or `ρ|c|` with `ρ = 1/5, 1/5, 2/3`, every one being a single coefficient on
one function. no convexity. **unusable**, and it is the second problem in the
appendix that has the crossing and cannot test it.


## 4. where the crossing meets the answer

### 4.1 what a crossing does, in the framework's own terms

with `G_i = ⊕_j [a_ij, b_ij] ⊙ h_ij` and any signs, definition 2.1(iii) gives, term
by term, `min(a h, b h) = m h − w|h|` and `max(a h, b h) = m h + w|h|`, so

    G̲_i = c_i − r_i,   Ḡ_i = c_i + r_i,   c_i = Σ_j m_ij h_ij,   r_i = Σ_j w_ij |h_ij|

**the centre stays as smooth as the `h_ij` are; the half-width picks up an absolute
value per sign-changing term.** everything below follows from that one line.

**theorem 3.3, and the damage is asymmetric across the three phi.** the theorem
requires `Λ_i^T f` and `B_i^T f` convex, a0 c12, printed page 9. under phi_lu those
are `G̲_i` and `Ḡ_i`; under phi_ls they are `G̲_i` and `Ḡ_i − G̲_i = 2r_i`; under
phi_cw they are `c_i` and `r_i`.

    **`G̲_i` is a sum of pointwise minima of two smooth functions**, hence generically
        not convex — for affine `h_ij` it is a min of affine pieces and is exactly
        concave. so **phi_lu and phi_ls lose theorem 3.3 at the crossing.**
    **`c_i` is untouched** and `r_i = Σ w_ij|h_ij|` is convex whenever each `|h_ij|`
        is — true for affine `h_ij` and for any convex `h_ij` of one sign, false in
        general. so **phi_cw can keep theorem 3.3 where the other two lose it.**

**that split is p0's table verbatim.** b1 section 1.5 measured it on 200000 midpoint
chords: "F is phi_cw-convex. F is neither phi_lu-convex nor phi_ls-convex", the
single failing coordinate being `Λ_1^T f = −|x|`.

**and the loss is global, not local.** example 3.9 statements 2 and 3 as printed
require "S is convex, F is φ-convex", a0 c14 — theorem 3.3's global form, not
remark 2.2's pointwise one, which example 3.9 does not invoke. so **one crossing
point anywhere in the box costs phi_lu and phi_ls their sufficiency over the whole
box**, not only on the locus. that is why a crossing that misses the efficient set
is still not free: it is free for statement 1 and for phi_cw, and not for phi_lu's
and phi_ls's statements 2 and 3.

**example 3.9's differentiability hypothesis fails on the locus, under all three
phi.** the hypothesis is on `Λ_i^T f` and `B_i^T f` and on nothing else, a0 c14,
printed page 10; and since each `φ_i` is invertible, differentiability of both image
coordinates is equivalent to differentiability of both endpoint functions **for every
admissible φ**, which a0 c14 states in exactly those words. `|h|` has no derivative
where `h = 0` and `∇h ≠ 0`. so on the crossing locus:

    statement 1, the **necessary** condition, is unavailable. a weak optimal solution
        sitting on the locus need not admit weights satisfying (15), so **the derived
        candidate set can miss efficient points**, silently and without any sign in
        the algebra that something was missed.
    statements 2 and 3, the **sufficient** conditions, are unavailable there too, so
        a point of the locus cannot be certified even if a limiting form of (15) held
        at it.

### 4.2 the decisive question, measured rather than guessed

for each of the five interchange problems: points **on** the crossing locus, tested
against a dense grid of the box under each phi. a locus point that no grid point
dominates is a locus point in the efficient set.

    2  I-VU2     crossing points not dominated   lu: 2/242     ls: 2/242     cw: 2/242
    3  I-CH      crossing points not dominated   lu: 0/161     ls: 12/161    cw: 12/161
    7  I-Hil1    crossing points not dominated   lu: 0/133     ls: 0/133     cw: 0/133
    14 I-Viennet crossing points not dominated   lu: 4/400     ls: 205/400   cw: 205/400
    20 I-Comet   crossing points not dominated   lu: 0/780     ls: 780/780   cw: 780/780

    grid sizes: I-VU2 601x601, I-CH 601x481, I-Hil1 601x601,
                I-Viennet 481x481, I-Comet 81x81x41

**a phi-dependence that is a mechanism and not an accident.** under phi_cw the second
image column of objective `i` **is** the half-width `r_i = Σ_j w_ij|h_ij|`, and under
phi_ls it is the full width `2r_i`; both are minimised, locally, exactly where a
sign-changing `h_ij` vanishes. **so under those two orders the crossing locus is the
width column's own minimiser set and the order pulls the efficient set onto it.**
under phi_lu the two columns are `G̲_i` and `Ḡ_i`, neither of which has a minimum on
the locus, and there is no such attraction. the table shows exactly that: `0/161`,
`4/400`, `0/780` under phi_lu against `12/161`, `205/400`, `780/780` under the other
two, on the same points.

**so the honest general answer to the brief's question is: for phi_cw and phi_ls a
crossing generically does meet the answer, and for phi_lu it generically does not.**

**the I-Hil1 row is a limitation of the test and not a result, and it is corrected
here.** `0/133` does not mean the locus misses the efficient set; it means each of
the 133 sampled locus points is dominated by some **other** point of the same locus.
on I-Hil1's locus `cos θ = 0` forces `θ = π/2`, hence `h_2 = amp·sin θ = amp` and the
phi_cw columns `(0, 0, 2·amp, amp)`, so the locus point with the smallest
`amp = 1 + ½cos(2πx_1)` beats every other. the 601×601 grid contains **eight points
lying exactly on the locus**, at `x_1 ∈ {−11/12, −7/12, 1/12, 5/12}` and
`x_2 ∈ {−3/4, 1/4}`, where the trigonometry is exact; re-running the test on those:

    phi_lu: of those 8 exact-locus grid points, NOT dominated: 4
    phi_ls: of those 8 exact-locus grid points, NOT dominated: 4
    phi_cw: of those 8 exact-locus grid points, NOT dominated: 4
      at x = (-7/12, -3/4), (-7/12, 1/4), (5/12, -3/4), (5/12, 1/4)

**so I-Hil1's crossing meets the efficient set too**, at the `amp`-minimising points
of the locus, under all three phi. the general test under-reports whenever the
dominator is itself on the locus, and that is a property of the test.

### 4.3 per candidate

**I-VU2, and this one is exact rather than a grid statement.** the surviving points
are, under all three phi, `x = (0, 0)` and nothing else — the origin, which appears
twice in the sample because it lies on both lines. and it can be proved directly.
under phi_cw the four columns are

    c_1 = 1.25(x_1+x_2) + 1,   r_1 = ¼(|x_1|+|x_2|),
    c_2 = 1.25x_1² + 2.5x_2² − 1,   r_2 = ¼x_1² + ½x_2²

and **three of the four attain their global minimum at the origin**: `r_1 ≥ 0`,
`c_2 ≥ −1`, `r_2 ≥ 0`, each with equality only there. any dominator needs `r_1 ≤ 0`,
which forces `x = 0`. **so the origin is phi_cw-efficient, exactly.** under phi_lu
the objective-2 columns are `G̲_2 = x_1² + 2x_2² − 1` and `Ḡ_2 = 1.5x_1² + 3x_2² − 1`,
both `≥ −1` with equality only at the origin, and the same argument closes; under
phi_ls the columns `2r_1 = ½(|x_1|+|x_2|)`, `G̲_2` and `Ḡ_2 − G̲_2 = ½x_1² + x_2²`
are all globally minimised there. **the origin is efficient under all three.**

**and the origin is where both crossing loci meet.** so for I-VU2 the conditions of
example 3.9 fail at a point of the answer under every phi, and the point at which
they fail is not an artefact of the box or of a face: it is `G_2`'s own global
minimiser, which is the kind of point every biobjective efficient set contains.

**I-CH.** `12/161` under phi_ls and phi_cw, `0/161` under phi_lu, the mechanism above.
worth naming because it is the clearest instance: `G_2`'s half-width is
`½|x_1²−x_2| + 2`, minimised **exactly on the parabola**, so under phi_cw an arc of
the crossing locus is efficient by construction. the problem is disqualified twice
over — constant width on `G_1`, criterion 5 — so this is illustration and not a
candidate.

**I-Viennet.** `205/400` against `4/400`. same mechanism, on the circles
`x_1²+x_2² = kπ`. disqualified on convexity and on `G_1`'s one-dimensional image.

**I-Comet.** `780/780` against `0/780` — every sampled crossing point survives under
phi_ls and phi_cw and none under phi_lu, which is the mechanism in its purest form,
`G_1` and `G_2` each being a single coefficient on one sign-changing function so that
`r = ρ|h|` is minimised on the locus and nowhere else. disqualified: all three
objectives degenerate.

**I-SD, I-IKK1, I-VFM1, I-MHHM2 have no crossing at all**, section 3.3, so part 4's
question does not arise for them and example 3.9's differentiability holds
everywhere on their boxes.

**the limits of section 4.2.** every number there except I-VU2's is a **grid**
statement: a dominator could sit between grid points, which would only lower the
counts, and the sampling artefact just described can lower them spuriously, which is
what I-Hil1 shows. so the counts are evidence for the direction of the answer and
are not the answer. **what cannot be settled without deriving the efficient set** is
the measure of the intersection — whether the locus meets the efficient set in
isolated points, as I-VU2's exact argument gives, or in an arc, as I-CH's and
I-Comet's counts suggest. that distinction decides how much of a derived set would
be missing, and no reading or grid settles it.

### 4.4 is it the condition that made p0 unusable as a fixture

**yes on the image coordinates, no on where the absolute value comes from, and the
distinction is worth keeping.**

    the same. in both cases the half-width is an absolute value, so both image
        coordinates are kinked; theorem 3.3 fails for phi_lu and phi_ls and survives
        for phi_cw; example 3.9's differentiability fails under all three; and
        **the kink sits at a point of the answer.** on p0 that point is the
        published anchor `x = 0`, [1] lines 752-755, which is why r-04 and b1
        section 1.5 record that the anchor "cannot be reached by applying example
        3.9" and why p0 could never serve as a fixture: the only published point it
        has is exactly the point at which the route has nothing to say.
    the different. **p0 has no ⊙ at all.** [1] writes `F_1(x) = [−|x|, |x|]`
        directly, so the absolute value is in the statement of the problem. on
        I-VU2 it is produced by Moore's product on a sign-changing `h`, from
        coefficients that carry no absolute value anywhere. **the same obstruction,
        reached from a published problem that does not look pathological.**
    and one way in which the appendix-A version is **worse**. p0's kink is a single
        point of a one-dimensional box. I-VU2's is two lines through a
        two-dimensional box, and in general the crossing locus has codimension one.
        so the set on which example 3.9 is unavailable is not negligible, and the
        part of the efficient set it can hide is not a point count.

**that is the sentence the supervisors' objection reduces to, and it is checkable
before any run**: the 2m transformation is exactly as valid as [16]'s printed page
27 says it is, and where it is not, the failure is p0's failure — which the project
has already met, already located, and already knows it cannot argue around.


## 5. a shortlist, not a pick

**the choice is not made here.** it goes back to the research chat with this
comparison in front of it. four candidates, spanning the trade-off rather than
converging on one, and **the two criteria are reported separately for each because
no candidate is best on both.**

**one thing to know before reading the four.** the brief asks for "the most derivable
of the sign-changing problems" and, separately, for "a problem where the derivation
is expected to fail at the crossing". **those two slots collapse onto one problem.**
of the five that interchange, I-CH has a constant width and fails criterion 5,
I-Hil1 and I-Comet have every objective degenerate, and I-Viennet's `G_1` is a
function of one scalar. **I-VU2 is the only problem in appendix A that interchanges
and is not disqualified on other grounds**, so it is simultaneously the most
derivable sign-changing problem and the expected-failure candidate. that is not a
convenience; it is what the appendix contains.

### 5.1 I-SD — the most novel that still looks derivable

`n = 4`, `m = 2`, four columns, `[1,6]×[√2,6]×[√2,6]×[1,6]`, [16] p.29.

**criterion A: the highest of any candidate that closes.** it is the **first
derivation above `n = 2`** in the project's history and the **first derivation of a
non-polynomial objective**, `G_2` being a sum of reciprocals. docs/plan_after_meeting.md
section d0.1 states the preference in advance — "an example at `n = 4` and `m = 2` is
preferable to one at `n = 3` and `m = 3` on that ground alone" — and this is the only
problem in the appendix that satisfies it.

**criterion B: closes, by a route the plan did not anticipate.** all twelve image
coordinates convex; `G_1`'s Hessians zero and `G_2`'s diagonal with entries
`2λ_j/x_j³`, so (15) decouples into four scalar equations `a − b/x_j² = 0` with the
closed-form root `x_j = √(b/a)`. lit_review section 1.9 calls this the
"diagonal but not constant" widening of the cheap case.

**what it buys.** two firsts at once, on a problem whose route is closed-form and
whose coefficients are published. it would say that the project's method is not
confined to quadratics with constant Hessians, which is currently the only shape it
has ever derived and the obvious thing for an examiner to ask about.

**what it risks, and section 3.5 names two.** **interiority.** condition (15) carries
no constraint multipliers and b1 reads example 3.9 as an interior condition; on a
biobjective problem the efficient set has each objective's minimiser as an endpoint,
and here `G_1` is minimised at `lb` and `G_2` at `ub`, **both corners of the box**. so
the route can be expected to recover the relative interior of the efficient set and
not its two ends. that is a **stated limitation, not a failure** — it is the same
condition p1's box `[−0.5, 1.5]²` was chosen to avoid — but it must be stated in
advance rather than discovered. **and the encoding is harder than the derivation**:
the derived set is a three-dimensional region inside a four-dimensional box, so the
reference-front machinery has no plane to draw and igd's density question, r-13 and
b2-b, arrives in a form the project has not met. **no published checkpoint.**

**cost: 1-2 f2-sessions for the derivation, 1 for the encoding and statistics**, and
the encoding is the one at risk of overrunning.

### 5.2 I-IKK1 — the strongest result if the derivation closes

`n = 2`, `m = 3`, six columns, `[−50,50]²`, [16] p.29.

**criterion A: moderate on shape, highest of all on what it decides.** it is the
**first derivation at `m = 3`**, hence the first on a five-dimensional weight simplex.
its functional class is what the project has already derived twice, diagonal
quadratics with constant diagonal Hessians, so it adds nothing there.

**criterion B: passes cheaply**, the same decoupling as p1 and I-BK1, and with the
cleanest interiority of the three-objective candidates after I-MHHM2: centres
minimised at `(0,0)`, `(20,20)`, `(0,0)`, far inside the box.

**what it buys, and part2_closing section 7.2 already argues it at length.** it is
**the one candidate outside the half-width alignment regime** — half-widths `½x_2²`,
`½(x_2−20)²`, `½x_1²`, minimised on lines and not at their centres' minimisers, which
is p1's structure and not I-BK1's. so it **separates the two explanations of
part2_closing section 4**: if its three sets cross, part 1's geometry occurs on a
problem nobody adapted and the difference is located in the width structure rather
than in the problem's provenance; if they nest, that is the first evidence for the
other explanation. **either outcome is worth having**, which part2_closing says is
not true of a second problem of I-BK1's shape. and it is a **third registered test of
the protected-minimiser condition, x-01, on three columns at once**, where I-BK1
supplied none — 0 of 12 columns with a free set, measured at f3.

**what it risks.** **no published checkpoint**, so a derivation rests on the project's
own algebra as p1's did, which is exactly the standing weakness a checkpoint on I-BK1
was chosen to remove. and the `m = 3` elimination is real work that nothing in the
project has done: six image coordinates, a five-dimensional weight simplex, and no
guarantee that it collapses onto one scalar as f2's did on I-BK1.

**cost: 1-2 f2-sessions plus 1 encoding**, the same price part2_closing section 7.2
quotes.

### 5.3 I-VU2 — the crossing, and the expected failure

`n = 2`, `m = 2`, four columns, `[−4,4]²`, [16] p.28. **the only sign-changing
candidate in the appendix**, and the only route to the question the supervisors
raised.

**criterion A: it tests the one thing no problem in the project has ever tested**,
at the project's cheapest dimensions. **criterion B: it closes on each open quadrant
and provably fails at the crossing**, and section 4 establishes that the crossing
meets the answer — exactly, not by grid — at the origin under all three phi.

**what it buys, and it is a result and not a failure.** the deliverable is not "the
derivation broke". it is a **precise statement of the boundary of the transformation
approach on a published problem**:

    on each of the four open quadrants the problem is affine-plus-diagonal-quadratic,
        b1's route closes cheaply, and the efficient set is derived exactly there.
    on the two lines `x_1 = 0` and `x_2 = 0` the route is **unavailable and provably
        so**, not merely difficult: `G̲_1 = 1.25(x_1+x_2) − ¼(|x_1|+|x_2|) + 1` is
        concave, so theorem 3.3 fails for phi_lu and phi_ls **globally** by section
        4.1; and example 3.9's differentiability fails on the lines under all three
        phi by a0 c14's invertibility argument.
    **and the answer contains a point of those lines.** the origin is efficient under
        all three phi, proved directly in section 4.3 from three columns attaining
        their global minima there — no derivation needed for that half.
    so the closed form recovers the efficient set **minus** a set on which the
        published conditions have nothing to say, and that set is not empty of the
        answer. **that is the objection of [16]'s printed page 27, instantiated,
        located and bounded, on the paper's own test problem.**

**what would be needed to state the failure precisely rather than merely to hit it.**
five things, and four of them are done in this document: the boundary functions in
closed form (section 3.5); the convexity verdict per phi with theorem 3.3 (section
4.1); the differentiability verdict per phi with a0 c14 (section 4.1); and the proof
that the origin is efficient (section 4.3). **the fifth is the quadrant-wise
derivation**, which is one f2-session, and what it must show is that the four
quadrant pieces do not glue — that the candidate set produced by (15) has the origin
as a limit point and does not contain it, so the gap is exhibited rather than
asserted.

**what it risks.** **`G_2` is phi-blind**, `r_2 = c_2/5` with slope in `(0,1)`, so by
section 3.2 all six of its columns are increasing in `c_2` and objective 2 orders
identically under all three phi. **half the problem carries no information about the
comparison the project exists to make**, and any cross-phi statistic on I-VU2 is
driven by objective 1 alone. that is a real reduction and it must be said in the
memoria rather than discovered in the tables. and the result it produces is a
**negative**: it says where the approach stops, not that it works, so it strengthens
the memoria's honesty and not its headline.

**cost: 1 f2-session plus 1 encoding.** the cheapest of the four, because the
quadrants are the project's own shape and the failure statement is mostly written.

### 5.4 I-MHHM2 — the floor, named so the trade-off has a bottom

`n = 2`, `m = 3`, six columns, `[0,1]²`, [16] p.29-30. **six coefficient intervals on
six squared displacements and nothing else** — no constant term of any kind, the
cleanest statement of criterion 5 in the appendix, and the strictest interiority: the
three centres are minimised at `(0.8,0.6)`, `(0.85,0.7)` and `(0.9,0.6)`, so the whole
efficient set is confined to a small interior region of the unit square, with no
exposure to the face problem I-SD carries.

**criterion A: the lowest of the four.** it adds `m = 3` and nothing else; it is
inside the alignment regime, so it repeats I-BK1's structure at three objectives and
cannot separate part2_closing section 4's two explanations. **criterion B: the
highest of the four** — the cheapest route in the appendix, constant diagonal
Hessians, clean interiority, no ⊖gH, no crossing, no degeneracy.

**it is on the list because a shortlist with no safe option is not a shortlist.** if
the schedule turns out to have room for one session and not two, this is the
candidate that will certainly finish, and it still delivers the first `m = 3`
derivation.

**cost: 1-2 f2-sessions plus 1 encoding.** no published checkpoint.

### 5.5 the trade-off, in one place

    candidate   criterion A, novelty                         criterion B, does it close     cost      risk
    I-SD        **highest**: first n > 2, first              yes, diagonal-but-not-         1-2 + 1   ends of the efficient set on
                non-polynomial                               constant                                 faces; a 3-D set in a 4-D box
    I-IKK1      moderate shape, **highest decision           yes, cheap                     1-2 + 1   no checkpoint; m = 3 elimination
                value**: settles part2_closing section 4                                              never attempted
    I-VU2       **the interchange, untested anywhere**       per quadrant yes,              1 + 1     G_2 phi-blind; the result is a
                                                             **at the crossing no**                   negative
    I-MHHM2     **lowest**: m = 3 and nothing more           yes, cheapest                  1-2 + 1   adds least; repeats the
                                                                                                      alignment regime

**and the two readings of "what the supervisors were asking for" point at different
rows.** if "mathematics generalises" means *the method reaches further than the
shape it was built on*, the row is **I-SD**. if it means *the method's limits are
known and stated*, the row is **I-VU2**, which is what p0 became and is the only
candidate that answers the objection actually raised on 4 September. if it means
*the project's own open question gets closed*, the row is **I-IKK1**. **those are
three different sessions and the document does not choose between them.**


## 6. what this session closes, what it corrects, and what it does not

**closed.**

    **the audit.** the project implements the fixed-order endpoint reading and not
        definition 2.1(iii), it has no interval-product primitive at all, and there
        is no well-ordering guard anywhere in `src/`. tested, not read: section 1.2's
        output. **correct on everything run, silently wrong in general.**
    **which problems already run could trigger it: none**, and per problem with the
        reason, section 2. three were constructed with a non-negative half-width by
        design, p0 has no ⊙, and I-BK1's four `h_ij` are squares.
    **the section 6.1 degeneracy, decided exactly for all twenty**, section 3.2 —
        a check lit_review did not run and f2 ran on five problems. **eight of the
        twenty have at least one objective whose half-width is an exact function of
        its centre**, and on five of those it is every objective.
    **the crossing question, per problem and per phi**, section 4.2, with the
        mechanism that explains the phi-dependence.

**corrections to earlier documents, none of which moves a verdict.**

    **lit_review section 1.9, criterion 2, I-KW2** — and by the same argument I-PNR.
        the reason given includes "sign-changing factors"; those factors carry the
        degenerate coefficients `[10,10]` and `[¼,¼]` and interchange nothing.
        **both problems still fail, on convexity.**
    **lit_review section 1.8's closing paragraph, applied to I-Viennet `G_3`.** the
        ⊖gH kink is **not reached** on `[−3,3]²`: `R/8 − E/10` is `0.025` at `s = 0`
        and stays positive. **I-Viennet still fails**, on convexity and on `G_1`.
    **lit_review section 1.9, I-AP1 and I-AP4.** left as "not determinable"; this
        session adds a verdict on a different ground — **two of the three objectives
        of each are degenerate**, so even a closing derivation would leave two thirds
        of each problem blind to the choice of order. not a correction of a wrong
        reading; a check that was not run.
    **the brief's own baseline.** "everything run so far is n = 2 or 3" holds of the
        **derivations**, where the range is `n = 1` or `2`; the tier 1 benchmarks were
        run at `n = 30` and `n = 12` and never derived. section 3.1. the consequence
        is that higher `n` is underexplored **for derivation** and not for evaluation.

**not closed, and deliberately.**

    **the choice.** four candidates, no pick, by instruction.
    **the fix.** no change to evaluation semantics, per the constraints. section 1.4
        says what the change would be and why it needs its own session with its own
        tests.
    **the measure of the intersection.** section 4.2's counts say the crossing meets
        the answer; they do not say whether it meets it in isolated points or in an
        arc, and that decides how much of a derived set would be missing. **only the
        derivation settles it**, and only on the problem chosen.
    **a-6 and a-7** stay unresolved and neither changes a verdict here, as
        lit_review already recorded.

**proposed for registration by the research chat, and not registered here, this
session committing only this document and one session log line.**

    **r-23.** the fixed-order product in `objective_endpoints` and the absent
        `f_l ≤ f_u` guard, with section 1 as the evidence. two separable pieces: the
        missing Moore primitive, and the missing assertion at the `Problem` boundary
        — **the second is the cheaper and the more valuable**, since every problem in
        the project passes it today and it would convert this session's finding into
        a test failure the first time a sign-changing problem is added.
    **s-14.** whether example 3.9 statements 2 and 3's "F is φ-convex" is the global
        hypothesis of theorem 3.3, as printed and as b1 read it, or may be weakened
        to remark 2.2's pointwise "φ-convex at x̄", which example 3.9 does not invoke.
        **it matters exactly here**: under the global reading one crossing point
        anywhere in the box costs phi_lu and phi_ls their sufficiency over the whole
        box, section 4.1, and under the pointwise reading it costs them only the
        locus.
    **a sixth criterion for the gate of part1_closing section 7.2**, or a
        strengthening of criterion 5. the check of section 3.2 is exact, costs
        minutes, needs only the printed coefficients, and **disqualifies eight of the
        twenty problems** — one of them, I-CH, being the same problem criterion 5
        already fails, which suggests the two are the same condition seen from two
        sides. the gate currently has no criterion that would have caught I-Hil1,
        I-TR1 or I-Comet.
