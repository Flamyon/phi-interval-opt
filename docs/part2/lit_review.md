# lit-review: the reading pass that bears on part 2

session lit-review, 2026-09-05. **no code, no module, no implementation, no run,
and no phi added to the registry.** every statement below is read out of a pdf in
`papers/` and is located by the paper's own address — printed page, and
definition, theorem, proposition, equation, table or problem number. nothing is
derived, nothing is implemented, and every place the extraction does not settle a
reading is reported in section 6 and left unresolved.

written in the style of docs/part1/a0_framework.md: numbered claims, each located,
verdicts stated, ambiguities separated from findings.

**what this session was asked to decide.** docs/part1/part1_closing.md section 7.1
records clause c5 — "and it persists on problems that are interval-valued at
source" — as **not supported and not supportable by e1 and e2**. section 7.2
states a five-criterion gate an interval-native problem must pass. section 7.3
states what a second calibration point would remove. this session exists to find
out whether any of that is reachable from the corpus now on disk. the answer is
section 7.

sources read, in the order the session read them:

    [16] T. Mondal, D. Ghosh, D. S. Kim, "Newton Method for Multiobjective
         Optimization Problems of Interval-Valued Maps". arXiv:2603.06000v1
         [math.OC], 6 March 2026, 33 pages.
         `papers/Newton Method for Multiobjective Optimization Problems of
         Interval-Valued Maps.pdf`
    [9]  H. Ishibuchi, H. Tanaka, "Multiobjective programming in optimization of
         the interval objective function". European Journal of Operational
         Research 48 (1990) 219-225.
         `papers/9-Multiobjective programming in optimization of the interval
         objective function .pdf`
    [7]  Z. Cui, C. Qu, Z. Zhang, Y. Jin, J. Cai, W. Zhang, J. Chen, "An adaptive
         interval many-objective evolutionary algorithm with information entropy
         dominance". Swarm and Evolutionary Computation 91 (2024) 101749.
    [8]  Z. jingbo, Z. zhixia, C. xingjuan, C. jianghui, C. jinjun, "An interval
         evolutionary algorithm based on dynamic relation adjustment strategy for
         many-objective problems". Swarm and Evolutionary Computation 93 (2025)
         101853.
    [13] J. Wen, Q. Wang, Z. Cui, J. Cai, J. Chen, "A two-stage evolutionary
         algorithm for uncertain constrained multi-objective problems with
         interval-valued objective". Information Sciences 741 (2026) 123217.
    [10] L. Stefanini, M. Arana-Jiménez, L. Sorini, "Fréchet and Gateaux
         gH-differentiability for interval valued functions of multiple
         variables". Information Sciences 691 (2025) 121601, 31 pages.

**not read, by the session's own constraint.** [14] and [15], the portfolio
papers. they are recorded in section 5.3 as what CONTEXT.md section 3 already says
they are — the citation for the memoria's future-work paragraph — and no claim
below depends on them. [1] itself was not re-opened: where this document needs
[1], it cites docs/part1/a0_framework.md, which verified [1] against the paper on
2026-08-31, and says so at the point of use.


## 0. how to re-check any claim, and the page convention

each pdf was read through

    pdftotext -layout <file> <file>.txt

which is deterministic, so any line quoted below can be recovered in one command.
the extracted text is **not committed**: docs/part1/a0_framework.md's convention of
citing line numbers into a committed `.txt` is not followed here, because the
extraction is a derived artefact and the paper's own numbering is a stabler
address. every claim below therefore carries a printed page and a paper-internal
number, and nothing carries a line number.

printed pages were recovered from the page footers, which survive the extraction
in all six papers.

    [16]  the footer is the bare page number; printed page = pdf page, 1 to 33.
    [9]   the footer is the running head with the page number, 219 to 225.
    [7]   printed page = pdf page, 1 to 16.
    [8]   printed page = pdf page, 1 to 16.
    [13]  printed page = pdf page, 1 to 16.
    [10]  Elsevier article-number pagination: the footer is the bare page number,
          printed page = pdf page, 1 to 31. the running head carries only
          "Information Sciences 691 (2025) 121601".

where a numbered item straddles a page break, both pages are given.


## 1. [16], the source of part 2's problems

### 1.1 what the paper is, and the citation the memoria needs

**it is an arXiv preprint and not a journal article.** the stamp on page 1 reads
`arXiv:2603.06000v1 [math.OC] 6 Mar 2026`. there is no journal name, volume or
doi anywhere in it. CONTEXT.md section 3 gives it as "mondal, ghosh and kim,
'newton method for multiobjective optimization problems of interval-valued maps'"
with no venue, which is correct as far as it goes; **the memoria must cite it as a
preprint with its arXiv identifier unless a published version is found before the
memoria is written.** recorded so nobody supplies a venue from memory.

authors and affiliations, page 1: Tapas Mondal and Debdas Ghosh, Department of
Mathematical Sciences, Indian Institute of Technology (BHU), Varanasi; Do Sang
Kim, Department of Applied Mathematics, Pukyong National University, Busan.

**the source appendix A cites for its test problems**, appendix A's opening
sentence, printed page 27, transcribed:

> In this section, we provide a set of test problems for MIOPs refer to [27]. For
> each test problem, we provide the expression of the objective functions and the
> lower and upper bounds of the variables.

[27] in [16]'s own numbering, from the reference list on printed page 32:

> [27] Mondal, T., Ghosh, D.: Steepest descent method for multiobjective
>      optimization problems of interval-valued maps. Numer. Algorithms (2025).
>      https://doi.org/10.1007/s11075-025-02205-7

so the twenty problems are, on [16]'s own attribution, from Mondal and Ghosh's
steepest-descent paper and not original to [16]. **the memoria must cite both**:
[16] as the source the project read, and Mondal–Ghosh 2025 as the source [16]
credits. the phrase "refer to [27]" is ambiguous between "taken from" and
"compare"; see section 6, ambiguity a-3.

### 1.2 the problem class, and what makes it interval-valued at source

location: section 2.2, printed page 7. the problem is equation (1):

> Let U ⊆ ℝⁿ be an open set and G : U → I(ℝ)^m be a multiobjective IVM given by
> G := (G_1, G_2, …, G_m)^⊤, where G_i : U → I(ℝ) is a twice gH-continuously
> differentiable and locally strongly convex IVM given by G_i := [G̲_i, Ḡ_i] for
> all i = 1, 2, …, m. We consider to solve the following MIOP in this study:
>
>     (1)   min G(x)
>           x∈U

the paper's standing assumption, same page, stated immediately before Lemma 2.4:

> Unless explicitly mentioned, we assume that ∇²_gH G_i(x) is positive definite
> for all x ∈ U and for all i = 1, 2, …, m, i.e.,
>
>     v^⊤ ⊙ ∇²_gH G_i(x) ⊙ v ≻ 0 for all nonzero v ∈ ℝⁿ, for all x ∈ U, and for
>     all i = 1, 2, …, m.

**claim 1.1. every problem of appendix A is stated as a sum of interval
coefficients multiplying real functions, and the intervals are coefficient
imprecision, not a band added around a crisp problem.**

verdict: **confirmed, with three named exceptions and one qualification.**

the common shape, read off the twenty problem statements on printed pages 27 to
31, is

    G_i(x) = ⊕_j [a_ij, b_ij] ⊙ h_ij(x)

with h_ij real-valued and [a_ij, b_ij] a numeric interval printed in the problem
statement. this is imprecision in the coefficients, which is criterion 5's
passing construction and is the construction docs/part1/a1_uncertainty_model.md
records slide 19 offering first. the preliminary observation of
docs/plan_after_meeting.md section d1, offered there without page numbers, is
**confirmed against the paper**.

the exceptions, each a constant interval term rather than a coefficient:

    problem 3 (I-CH), page 28. **both** objectives are a degenerate interval
        coefficient times a crisp function, plus a constant interval band:
        G_1 = [1,1] ⊙ ((x_1−1)² + (x_2−2)²) ⊕ [−1,1] and
        G_2 = [2,3] ⊙ (x_1² − x_2) ⊕ [−2,2]. G_1 is f(x) ± 1 exactly, which is
        the form criterion 5 names as failing.
    problem 8 (I-PNR), page 29. constant interval terms ⊕[20,24] on G_1 and
        ⊕[0,2] on G_2, **alongside** genuine coefficient intervals
        [1,1.5], [1,2.6], [1,2], [1,1.5].
    problems 14 (I-Viennet, ⊕[15,16]), 16 (I-MOP7, ⊕[2,3], ⊖gH[17,20],
        ⊖gH[13,15]) and 18 (I-TR1, [15,30]⊖gH …), pages 30. same: a constant
        interval term beside genuine coefficient intervals.

the qualification: degenerate intervals [k,k] appear throughout (problems 2, 3,
5, 8, 11, 12) and are real constants, not bands. they do not offend criterion 5.

**only problem 3 (I-CH) fails criterion 5.** in the others the problem is
interval-valued without the constant term, so the interval-valuedness is at
source.

**claim 1.2. I-CH is the constant-width degeneracy, published.**

verdict: **confirmed, and recorded because it is worth a sentence in the
memoria.** I-CH's G_1 has centre (x_1−1)² + (x_2−2)² and half-width **1, a
constant**. docs/part1/part1_closing.md section 6.1 records the constant-width
degeneracy as the methodological result that would have made the study vacuous
had a1 not caught it. I-CH is that degeneracy occurring in a published test
problem, which is independent evidence that the trap is a real one and not an
artefact of the project's own design process. it is recorded and **not** used: it
fails criterion 5 and is out.

### 1.3 the efficiency concepts, and their relation to [1] definition 3.1

this is the one thing the session was told to read the method section for.

location: definitions 2.16, 2.17 and 2.18, printed page 7. transcribed verbatim:

> **Definition 2.16 (Weakly Pareto optimal point [27]).** An x⋆ ∈ U is said to be
> a weakly Pareto optimal point of the MIOP (1) if there does not exist any other
> x ∈ U such that G_i(x) ≺ G_i(x⋆) for all i = 1, 2, …, m.
>
> **Definition 2.17 (Pareto optimal point [27]).** An x⋆ ∈ U is said to be a
> Pareto optimal point of the MIOP (1) if there does not exist any other x ∈ U
> such that G_i(x) ⪯ G_i(x⋆) for all i = 1, 2, …, m.
>
> **Definition 2.18 (Pareto critical point [27]).** A point x⋆ ∈ U is said to be
> Pareto critical point of the MIOP (1) if there does not exist any v ∈ ℝⁿ such
> that ∇_gH G_i(x⋆)^⊤ ⊙ v ≺ 0 for all i = 1, 2, …, m.

the relations ⪯ and ≺ are definition 2.2, printed page 4, transcribed in section
1.4 below. in words: A ⪯ B means both endpoints of A are ≤ the corresponding
endpoints of B; A ≺ B means the same with at least one endpoint strict.

**claim 1.3. definition 2.17 is exactly [1] definition 3.1(1), the strong or
strict optimal solution, and not [1] definition 3.1(2), the optimal solution.**

verdict: **confirmed**, by comparison with the transcription in
docs/part1/a0_framework.md section c10, [1] definition 3.1, printed page 6 of [1].

[1] definition 3.1(1) reads "x̄ ∈ S is a strong or strict optimal solution for (10)
if there does not exist x ∈ S \ {x̄} such that F(x) ≦_φ F(x̄)", with ≦_φ the
componentwise-weak relation of [1] equation (3). definition 2.17 of [16] reads
"there does not exist any other x ∈ U such that G_i(x) ⪯ G_i(x⋆) for all i", with
⪯ componentwise-weak on the endpoint pair. under φ = φ_lu the two are the same
sentence.

**claim 1.4. definition 2.16 is none of [1]'s three concepts. it sits strictly
between definition 3.1(2) and definition 3.1(3).**

verdict: **confirmed.** definition 2.16 forbids an x that is strict in **every**
objective; [1] definition 3.1(2) forbids an x that is weak in every objective and
strict in **at least one**, [1] equation (6); [1] definition 3.1(3) forbids an x
that is strict in both endpoints of every objective, [1] equation (7). so

    [1] 3.1(1) ⊆ [1] 3.1(2) ⊆ [16] 2.16 ⊆ [1] 3.1(3)

as sets of points, both inclusions being immediate from the definitions and
neither being an equality in general.

**why this matters and what it costs.** the project's phi-efficient set is [1]
definition 3.1(2)'s. a solution [16] calls weakly Pareto optimal is therefore not
a point in a set the project computes, and **a table that put [16]'s weak points
beside the project's phi-efficient sets would be comparing two different objects.**
[16]'s Pareto optimal points, definition 2.17, are usable directly: by [1]'s own
implication chain, printed page 6 of [1], a strong or strict optimal solution is
an optimal solution, so every point of definition 2.17 is a point of [1]
definition 3.1(2). **the published checkpoint of section 1.6 is a definition 2.17
point and is therefore usable.**

### 1.4 the paper's own order relation, located, and the containment criterion applied

location: definition 2.2, printed page 4, attributed to [16]'s own reference [4],
Chauhan, Ghosh, Ramík and Debnath, Soft Computing 25(23) (2021) 14629-14643.
transcribed verbatim, items (i) and (ii):

> **Definition 2.2 (Dominance relation of intervals [4]).** Consider a pair of
> elements S := [s̲, s̄] and T := [t̲, t̄] from I(ℝ).
>
> (i) If s̲ ≥ t̲ and s̄ ≥ t̄, then we say that T dominates S, and represent it by
>     S ⪰ T.
> (ii) If either s̲ > t̲ and s̄ ≥ t̄ or s̲ ≥ t̲ and s̄ > t̄, then we say that T
>     strictly dominates S, and express it by S ≻ T.

**claim 1.5. [16]'s order relation is φ_lu, example 2.2 of [1], already in the
registry. it is a check and not a finding, and it is not even a new candidate.**

verdict: **confirmed.**

the criterion, docs/part1/a_close_containment.md and docs/plan_after_meeting.md
section c1: if φ_B = M φ_A with M entrywise non-negative and invertible then
φ_A-dominance implies φ_B-dominance and ND_B ⊆ ND_A.

definition 2.2's T ⪯ S is t̲ ≤ s̲ and t̄ ≤ s̄, which is componentwise ≤ on the
endpoint pair (f_l, f_u). that is the map λ = (1,0), β = (0,1), which
docs/part1/a0_framework.md section c6 verifies is example 2.2 of [1]. in centre
and half-width coordinates it is [[1,−1],[1,1]] = φ_lu. **M against φ_lu is the
identity**, entrywise non-negative and invertible in both directions, so the
containment is an equality and the relation is the registry member itself.

consequence for part 2, stated plainly: **the paper's own solution concept
coincides with one of the project's three orders and with no other.** every point
[16] publishes is a φ_lu point. that is what makes its published points usable as
checkpoints, and it is also why running the other two phi on its problems is a
measurement the paper itself does not make.

### 1.5 the method, in one paragraph, recorded as out of scope

docs/plan_after_meeting.md section d4 and CONTEXT.md section 1: this project takes
existing solvers and measures what changes when the order changes, and does not
invent an algorithm. **[16]'s method is not this project's subject, nothing below
plans an implementation of it, and this paragraph exists only so that a later
reader does not have to open the paper to know what was skipped.** algorithm 1,
printed page 15, computes a Pareto critical point of (1). at a point x it builds
the interval-valued model g^i_x(v) := ∇_gH G_i(x)^⊤ ⊙ v ⊕ ½ ⊙ v^⊤ ⊙ ∇²_gH G_i(x)
⊙ v, equation (2), printed page 8; takes the upper boundary function ḡ^i_x,
equation (5), printed pages 8-9, because remark 3.1 on printed page 9 shows the
lower one does not imply interval dominance; defines the Newton direction as the
minimiser of max_i ḡ^i_x(v), equations (6) to (8), printed page 9; reformulates
that nonsmooth problem as the smooth constrained subproblem (10) on printed page
10 by splitting |v| into an auxiliary vector u with −u ≤ v ≤ u; and takes an
Armijo-like step, conditions (15). theorem 3.1 is the descent result, theorem 3.2
the existence of the step length, proposition 3.1 the scaling independence, and
theorem 4.1 the convergence of the sequence to a Pareto critical point; all four
are listed in the conclusion, printed page 27. **out of scope, and no session
between here and 25 september has room for it.**

### 1.6 the worked example, and the two published checkpoints

**claim 1.6. [16] publishes, for I-BK1, one solver-generated point and an
eleven-point closed-form curve, and this session reproduced the closed form
exactly.**

verdict: **confirmed**, and this is the single most useful thing the reading found
after the gate itself.

**checkpoint one, Table 1, printed page 20.** twelve iterations of algorithm 1 on
I-BK1 from x⁰ = (9.9862, −7.4332)^⊤, with x^k, G(x^k) and ξ(x^k) at each. the last
row, k = 12:

    x* = (3.914930, 1.428474)
    G(x*) = ([1.736722, 3.677497], [1.393317, 6.731112])
    ξ(x*) = −2.8154e−07

the gH-gradients and gH-Hessians the paper prints for I-BK1 on printed page 18,

    ∇_gH G_1 = ([0.2,0.4]⊙x_1, [0.2,0.6]⊙x_2)^⊤,
    ∇_gH G_2 = ([0.2,0.6]⊙(x_1−5), [0.2,1]⊙(x_2−5))^⊤,
    ∇²_gH G_1 = diag([0.2,0.4], [0.2,0.6]),
    ∇²_gH G_2 = diag([0.2,0.6], [0.2,1]),

are **exactly the derivatives of the boundary functions this session read off the
problem statement in section 1.8**, which is an independent confirmation that the
boundary-function reading of ⊙ is the paper's own.

**checkpoint two, equations (24) and (25) and Table 2, printed page 21.** the
paper scalarises I-BK1 by weighted sum, equation (23) on printed page 20, then by
Bhurjee and Panda's parametric method with weight function w(t_1,t_2,t_3,t_4) :=
t_2 + t_3, giving

>     (24)  min over x_1,x_2 of
>           (1−α)[0.15 x_1² + 0.21667 x_2²] + α[0.21667 (x_1−5)² + 0.3 (x_2−5)²]
>
>     (25)  x_1 := 2.1667α / (0.3 + 0.13334α)   and
>           x_2 := 3α / (0.43334 + 0.16666α),   α ∈ [0,1]

**this session checked (24) and (25) by hand and both are exact.** the four
coefficients of (24) are the w-weighted means of the interval-coefficient
parameters over [0,1]⁴: 0.1 + 0.1·½ = 0.15, 0.1 + 0.2·(7/12) = 13/60 = 0.21667
twice, and 0.1 + 0.4·½ = 0.3, the weight 7/12 being ∫t_2(t_2+t_3)dt = ⅓ + ¼. and
setting the gradient of (24) to zero gives x_1 = 1.08335α/(0.15 + 0.06667α) =
2.1667α/(0.3 + 0.13334α) and x_2 = 1.5α/(0.21667 + 0.08333α) = 3α/(0.43334 +
0.16666α), which is (25) as printed. Table 2 lists the eleven points at α = 0,
0.1, …, 1 with their interval objective values.

**what the two checkpoints are worth to part 2.** any implementation the project
writes for I-BK1 can be checked against a published point and against a published
one-parameter curve **before** any phi-efficient set is derived. no other problem
in appendix A has either. p1, the project's own calibration problem, has neither:
its correctness rests entirely on the project's own derivation. this is the first
external check available to the project at all.

**the paper's own argument that x* is Pareto optimal is invalid, and the
checkpoint survives anyway.** printed pages 21-22:

> As the points x generated by the weighted sum scalarization method (see Table 2)
> and the point x⋆ = (3.914930, 1.428474)^⊤ generated by Algorithm 1 (see Table 1)
> are nondominated each others, the point x⋆ = (3.914930, 1.428474)^⊤ is also a
> Pareto optimal point for the MIOP I-BK1.

being non-dominated by eleven particular points does not establish Pareto
optimality. **but proposition 2.1, printed page 7, supplies it independently**:
if U is convex, G ∈ C²_gH, ∇²_gH G_i(x) ≻ 0 everywhere, and x⋆ is Pareto critical,
then x⋆ is Pareto optimal. I-BK1's gH-Hessians are diag([0.2,0.4],[0.2,0.6]) and
diag([0.2,0.6],[0.2,1]), so v^⊤ ⊙ ∇²_gH G_i ⊙ v has both endpoints strictly
positive for v ≠ 0 and the hypothesis holds. the checkpoint stands on
proposition 2.1 and the Table 2 argument is redundant. recorded as ambiguity a-4
because it is a printed gap and the memoria must not repeat it.

### 1.7 the paper's own objection to the 2m transformation

this was not asked for and it is the most directly useful thing in [16] outside
appendix A, so it is recorded here and used in section 4.4.

location: section 1.2, "Motivation and Work Done", printed page 3, and repeated
almost verbatim in section 5, printed page 20. transcribed from printed page 3:

> However, in [32, 33], authors transformed an MIOP into a real-valued
> multiobjective optimization problem considering each objective function as a sum
> of the lower and upper boundary functions of each IVM and further applied the
> Newton and quasi-Newton methods for real-valued multiobjective optimization,
> **which essentially captures very tiny part of the entire set of efficient
> solutions. One can trivially find that almost entire part of the efficient
> solutions cannot be captured by the methods in [32,33].**

[32] and [33] are Upadhayay, Pandey and Liao, J. Ind. Manag. Optim. 20(4) (2024)
1633-1661, and Upadhayay, Pandey, Pan and Zeng, J. Comput. Appl. Math. 438 (2024)
115550, from the reference list on printed page 32.

and a second, more careful statement in the conclusion, section 7, printed page 27:

> In [6], it is shown that a single-objective interval optimization problem is
> equivalent to a biobjective optimization problem. So, one may think the MIOP (1)
> is equivalent to a conventional real-valued multiobjective optimization problem
> with 2m objective functions. However, this approach is possible if all the IVM
> G_i is convex, have an explicit form in terms of lower and upper boundary
> functions G̲_i and Ḡ_i, respectively such that for all x ∈ {x ∈ ℝⁿ : lb ≤ x ≤ ub}
> and for all i = 1, 2, …, m,
>
>     G_i(x) := [G̲_i(x), Ḡ_i(x)], ∇_gH G_i(x) := [∇G̲_i(x), ∇Ḡ_i(x)], and
>     ∇²_gH G_i(x) := [∇²G̲_i(x), ∇²Ḡ_i(x)].
>
> Since G̲_i and Ḡ_i may interchange their position, it is very difficult to
> express the IVM G_i by G_i(x) := [G̲_i(x), Ḡ_i(x)] for all x ∈ {x ∈ ℝⁿ : lb ≤ x
> ≤ ub}. In addition, the relations ∇_gH G_i(x) := [∇G̲_i(x), ∇Ḡ_i(x)] and
> ∇²_gH G_i(x) := [∇²G̲_i(x), ∇²Ḡ_i(x)] are not true in general.

**two distinct objections, and only the second is technical.** the first is a
claim about how much of the efficient set the *sum* f_l + f_u recovers, and the
sum is a scalarization, not the 2m transformation the project uses; **it is not an
objection to the project's construction and must not be quoted as if it were.**
the second is a genuine and precise condition on the 2m transformation: it is
valid where the lower and upper boundary functions do not interchange, i.e. where
the sign of each h_ij is constant. **the project's construction satisfies that
condition on p1 and on the tier 1 problems by design**, and section 1.8 below
records, per appendix-A problem, whether it satisfies it — which is the same
question as whether the boundary functions are smooth.

### 1.8 appendix A: the twenty problems, transcribed

printed pages 27 to 31. twenty problems, numbered 1 to 20, named I-BK1 through
I-Comet, matching the twenty rows of Table 3 on printed page 23 in the same order.
the problem is stated on printed page 27 as

>     min over lb ≤ x ≤ ub, x ∈ U ⊆ ℝⁿ, of (G_1(x), G_2(x), …, G_m(x))^⊤.

**dimensions.** ten biobjective (problems 1-10) and ten triobjective (11-20).
n = 2 in seventeen of them, n = 3 in problems 17 to 20, and n = 4 in problem 10.
so the transformed problem's 2m column count is **4 for problems 1-10 and 6 for
problems 11-20**, and no problem in the appendix exceeds six columns.

    #   name         n   m   2m   box
    1   I-BK1        2   2   4    [−10,10]²                                p.27
    2   I-VU2        2   2   4    [−4,4]²                                  p.28
    3   I-CH         2   2   4    [−5,5]×[−4,4]                            p.28
    4   I-FON        2   2   4    [−2,2]²                                  p.28
    5   I-KW2        2   2   4    [−3,0]×[−1,2]                            p.28
    6   I-Far1       2   2   4    [−1,1]²                                  p.28-29
    7   I-Hil1       2   2   4    [−1,1]²                                  p.29
    8   I-PNR        2   2   4    [−2,2]²                                  p.29
    9   I-Deb        2   2   4    [1,3]×[−1,1]                             p.29
    10  I-SD         4   2   4    [1,6]×[√2,6]×[√2,6]×[1,6]                p.29
    11  I-IKK1       2   3   6    [−50,50]²                                p.29
    12  I-VFM1       2   3   6    [−2,2]²                                  p.29
    13  I-MHHM2      2   3   6    [0,1]²                                   p.29-30
    14  I-Viennet    2   3   6    [−3,3]²                                  p.30
    15  I-AP1        2   3   6    [−100,100]²                              p.30
    16  I-MOP7       2   3   6    [−400,400]²                              p.30
    17  I-VFM2       3   3   6    [−5,10]³                                 p.30
    18  I-TR1        3   3   6    [1,4]³                                   p.30
    19  I-AP4        3   3   6    [−100,100]³                              p.30-31
    20  I-Comet      3   3   6    [1,3.5]×[−2,2]×[0,1]                     p.31

**the objectives, in the paper's own notation.** transcribed one block per
problem. ⊙ is Moore's scalar-interval product, definition 2.1(iii) of [16] page 3;
⊕ is Minkowski addition; ⊖gH is the gH-difference, definition 2.1 page 4.

    problem 1, I-BK1, p.27
        G_1 = [0.1,0.2] ⊙ x_1²  ⊕  [0.1,0.3] ⊙ x_2²
        G_2 = [0.1,0.3] ⊙ (x_1−5)²  ⊕  [0.1,0.5] ⊙ (x_2−5)²
        lb = (−10,−10), ub = (10,10)

    problem 2, I-VU2, p.28
        G_1 = [1,1.5] ⊙ x_1  ⊕  [1,1.5] ⊙ x_2  ⊕  [1,1]
        G_2 = [1,1.5] ⊙ x_1²  ⊕  [2,3] ⊙ x_2²  ⊖gH  [1,1]
        lb = (−4,−4), ub = (4,4)

    problem 3, I-CH, p.28
        G_1 = [1,1] ⊙ ((x_1−1)² + (x_2−2)²)  ⊕  [−1,1]
        G_2 = [2,3] ⊙ (x_1² − x_2)  ⊕  [−2,2]
        lb = (−5,−4), ub = (5,4)

    problem 4, I-FON, p.28
        G_1 = [1,1]  ⊖gH  [1,3] ⊙ exp(−(x_1 − 1/√2)² − (x_2 − 1/√2)²)
        G_2 = [1,1]  ⊖gH  [1,5] ⊙ exp(−(x_1 + 1/√2)² − (x_2 + 1/√2)²)
        lb = (−2,−2), ub = (2,2)

    problem 5, I-KW2, p.28
        G_1 = [−5,−3] ⊙ (1−x_1)² exp(−x_1² − (x_2+1)²)
              ⊕ [10,10] ⊙ ((1/5)x_1 − x_1³ − x_2⁵) exp(−x_1² − x_2²)
              ⊕ [3,5] ⊙ exp(−(x_1+2)² − x_2²)
              ⊖gH [1/2,1/2] ⊙ (2x_1 + x_2)
        G_2 = [−5,−3] ⊙ (1+x_2)² ⊙ exp(−x_2² − (1−x_2)²)
              ⊕ [10,10] ⊙ (−(1/5)x_2 + x_2³ + x_1⁵) exp(−x_1² − x_2²)
              ⊕ [3,5] ⊙ exp(−(2−x_2)² − x_1²)
        lb = (−3,−1), ub = (0,2)
        [see ambiguity a-5: G_2's first and third terms are not the mirror of
         G_1's and this session does not resolve it]

    problem 6, I-Far1, p.28-29
        G_1 = [−2,−1] ⊙ exp(15 − (x_1−0.1)² − x_2²)
              ⊕ [−2,−1] ⊙ exp(20 − (x_1−0.6)² − (x_2−0.6)²)
              ⊕ [1,3] ⊙ exp(20 − (x_1+0.6)² − (x_2−0.6)²)
              ⊕ [1,2] ⊙ exp(20 − (x_1−0.6)² − (x_2+0.6)²)
              ⊕ [1,2] ⊙ exp(20 − (x_1+0.6)² − (x_2+0.6)²)
        G_2 = [2,4] ⊙ exp(20 − x_1² − x_2²)
              ⊕ [1,2] ⊙ exp(20 − (x_1−0.4)² − (x_2−0.6)²)
              ⊕ [−2,−1] ⊙ exp(20 − (x_1+0.5)² − (x_2−0.7)²)
              ⊕ [−2,−1] ⊙ exp(20 − (x_1−0.5)² − (x_2+0.7)²)
              ⊕ [1,5] ⊙ exp(20 − (x_1+0.4)² − (x_2+0.8)²)
        lb = (−1,−1), ub = (1,1)

    problem 7, I-Hil1, p.29
        G_1 = [1,2] ⊙ (1 + ½cos(2πx_1)) cos((2π/360)(45 + 40 sin(2πx_1)
                                                        + 25 sin(2πx_2)))
        G_2 = [1,3] ⊙ (1 + ½cos(2πx_1)) sin((2π/360)(45 + 40 sin(2πx_1)
                                                        + 25 sin(2πx_2)))
        lb = (−1,−1), ub = (1,1)

    problem 8, I-PNR, p.29
        G_1 = [1,1.5] ⊙ (x_1⁴ + x_2⁴)  ⊕  [1,2.6] ⊙ (x_1² + x_2²)
              ⊕ [10,10] ⊙ x_1x_2  ⊕  [¼,¼] ⊙ x_1  ⊕  [20,24]
        G_2 = [1,2] ⊙ (x_1−1)²  ⊕  [1,1.5] ⊙ x_2²  ⊕  [0,2]
        lb = (−2,−2), ub = (2,2)

    problem 9, I-Deb, p.29
        G_1 = [1,2] ⊙ x_1
        G_2 = (1/x_1) ⊙ ( [2,2]  ⊖gH  [1,3] ⊙ exp(−((x_2−0.2)/0.004)²)
                                 ⊖gH  [0.8,1.5] ⊙ exp(−((x_2−0.6)/0.4)²) )
        lb = (1,−1), ub = (3,1)
        [see ambiguity a-6: the scope of the 1/x_1 factor is not settled by the
         extraction]

    problem 10, I-SD, p.29
        G_1 = [2,3] ⊙ x_1 ⊕ [√2,√3] ⊙ x_2 ⊕ [√2,√3] ⊙ x_3 ⊕ [1,3] ⊙ x_4
        G_2 = [2,3] ⊙ (1/x_1) ⊕ [2√2,3√3] ⊙ (1/x_2)
              ⊕ [2√2,3√3] ⊙ (1/x_3) ⊕ [2,3] ⊙ (1/x_4)
        lb = (1, √2, √2, 1), ub = (6,6,6,6)

    problem 11, I-IKK1, p.29
        G_1 = [1,1] ⊙ x_1²  ⊕  [0,1] ⊙ x_2²
        G_2 = [1,1] ⊙ (x_1−20)²  ⊕  [0,1] ⊙ (x_2−20)²
        G_3 = [0,1] ⊙ x_1²  ⊕  [1,1] ⊙ x_2²
        lb = (−50,−50), ub = (50,50)

    problem 12, I-VFM1, p.29
        G_1 = [1,2] ⊙ x_1²  ⊕  [1,3] ⊙ (x_2−1)²
        G_2 = [1,3] ⊙ x_1²  ⊕  [1,2] ⊙ (x_2+1)²  ⊕  [1,1]
        G_3 = [1,2] ⊙ (x_1−1)²  ⊕  [1,5] ⊙ x_2²  ⊕  [2,2]
        lb = (−2,−2), ub = (2,2)

    problem 13, I-MHHM2, p.29-30
        G_1 = [2,3] ⊙ (x_1−0.8)²  ⊕  [1,2] ⊙ (x_2−0.6)²
        G_2 = [1,2] ⊙ (x_1−0.85)²  ⊕  [1,1.5] ⊙ (x_2−0.7)²
        G_3 = [2,2.5] ⊙ (x_1−0.9)²  ⊕  [1,1.2] ⊙ (x_2−0.6)²
        lb = (0,0), ub = (1,1)

    problem 14, I-Viennet, p.30
        G_1 = [0.5,1] ⊙ (x_1²+x_2²)  ⊕  [1,2] ⊙ sin(x_1²+x_2²)
        G_2 = [⅛,¼] ⊙ (3x_1−2x_2+4)²  ⊕  [1/27,1/9] ⊙ (x_1−x_2+1)²  ⊕  [15,16]
        G_3 = [¼,½] ⊙ (1/(x_1²+x_2²+1))  ⊖gH  [0.9,1.1] ⊙ exp(−x_1²−x_2²)
        lb = (−3,−3), ub = (3,3)

    problem 15, I-AP1, p.30
        G_1 = [¼,½] ⊙ ((x_1−1)⁴ + 2(x_2−2)⁴)
        G_2 = [1,2] ⊙ exp((x_1+x_2)/2)  ⊕  [1,1.5] ⊙ (x_1²+x_2²)
        G_3 = [⅓,½] ⊙ (exp(−x_1) + 2exp(−x_2))
        lb = (−100,−100), ub = (100,100)

    problem 16, I-MOP7, p.30
        G_1 = [¼,½] ⊙ (x_1−2)²  ⊕  [1/26,1/13] ⊙ (x_2+1)²  ⊕  [2,3]
        G_2 = [1/9,¼] ⊙ (x_1+x_2−3)²  ⊕  [1/16,⅛] ⊙ (−x_1+x_2+2)²  ⊖gH  [17,20]
        G_3 = [1/25,1/7] ⊙ (x_1+2x_2−1)²  ⊕  [1/34,1/17] ⊙ (−x_1+2x_2)²
              ⊖gH  [13,15]
        lb = (−400,−400), ub = (400,400)

    problem 17, I-VFM2, p.30
        G_1 = [0.1,0.2] ⊙ x_1² ⊕ [0.1,0.3] ⊙ x_2² ⊕ [0.1,0.2] ⊙ x_3²
        G_2 = [0.1,0.3] ⊙ (x_1−5)² ⊕ [0.1,0.5] ⊙ (x_2−5)²
              ⊕ [0.1,0.4] ⊙ (x_3−5)²
        G_3 = [0.1,0.2] ⊙ x_1²  ⊖gH  [0.1,0.3] ⊙ x_2²  ⊕  [0.1,0.2] ⊙ x_3²
        lb = (−5,−5,−5), ub = (10,10,10)
        [see ambiguity a-7: G_3's bracketing is not settled and ⊖gH does not
         associate with ⊕]

    problem 18, I-TR1, p.30
        G_1 = [15,30] ⊖gH [0.1,0.3] ⊙ (x_1³ + x_1²(1+x_2+x_3) + x_2³ + x_3³)
        G_2 = [25,45] ⊖gH [0.1,0.2] ⊙ (x_1³ + 2x_2³ + x_2²(2+x_1+x_3) + x_3³)
        G_3 = [30,60] ⊖gH [0.1,0.3] ⊙ (x_1³ + x_2³ + 3x_3³ + x_3²(3+x_1+x_2))
        lb = (1,1,1), ub = (4,4,4)

    problem 19, I-AP4, p.30-31
        G_1 = [1/9,⅓] ⊙ ((x_1−1)⁴ + 2(x_2−2)⁴ + 3(x_3−3)⁴)
        G_2 = [2,3] ⊙ exp((x_1+x_2+x_3)/3)  ⊕  [2,5] ⊙ (x_1²+x_2²+x_3²)
        G_3 = [¼,⅓] ⊙ (3exp(−x_1) + 4exp(−x_2) + 3exp(−x_3))
        lb = (−100,−100,−100), ub = (100,100,100)

    problem 20, I-Comet, p.31
        G_1 = [1,1.5] ⊙ (1+x_3) ⊙ (x_1³x_2² − 10x_1 − 4x_2)
        G_2 = [1,1.5] ⊙ (1+x_3) ⊙ (x_1³x_2² − 10x_1 + 4x_2)
        G_3 = [0.2,1] ⊙ (1+x_3) ⊙ x_1²
        lb = (1,−2,0), ub = (3.5,2,1)

**one structural fact that governs everything in section 1.9.** where every h_ij
has constant sign on the box, ⊙ does not interchange the boundary functions and
the four image coordinates under the three phi are fixed smooth combinations of
the h_ij. where an h_ij changes sign, the boundary functions interchange on the
zero set and the image coordinates acquire a kink there. **and where a ⊖gH is
taken against a non-degenerate interval, the resulting half-width is an absolute
value and acquires a kink wherever the two half-widths are equal**, by the
midpoint-radius formula A ⊖gH B = (â − b̂ ; |ã − b̃|), [10] section 2, printed
page 3. both facts are recorded per problem below.

### 1.9 the gate of part1_closing section 7.2, applied to each problem

**criterion 3 is marked "not determinable from the paper" for all twenty**, as
docs/plan_after_meeting.md section d1 instructs. it needs a sample near the
efficient set and the paper supplies none. **not determinable is not a pass**, so
**no problem in appendix A passes the gate on the reading alone**, and that is
stated first so no row below can be misread as an admission.

what the reading can settle is criteria 1, 2, 4 and 5. verdicts, then the table.

**criterion 2, stated once for the whole appendix.** the route is b1's, per
docs/plan_after_meeting.md section d0.2: image coordinates written out,
phi-convexity by theorem 3.3 of [1], regularity by [10], condition (15) of example
3.9 of [1] for the candidate set, and example 3.8 statement 3 to lift weak
optimality to optimality. the route closes when the image coordinates are
differentiable and convex and the stationarity system is solvable. it closes
**cheaply** when the objectives are quadratic with constant diagonal Hessians,
because (15) then decouples into n scalar equations exactly as it does for p1.

**a widening of the cheap case that the reading found.** the plan's condition is
"quadratic with constant diagonal Hessians". the appendix supplies two shapes that
are not that and on which (15) is still solvable in closed form:

    diagonal but not constant. I-SD's G_2 is a sum of λ_j/x_j with x_j > 0 on the
        box. the Hessian is diagonal with entries 2λ_j/x_j³, so (15) still
        decouples into n scalar equations, each of the form a − b/x_j² = 0 with
        the closed-form root x_j = √(b/a). the route closes and is cheap.
    constant but not diagonal. I-MOP7's G_2 and G_3 are sums of squares of affine
        functions, so the Hessians are constant and full. (15) does not decouple
        but it is a 2×2 linear system in x with the weights carried as symbols,
        which is closed form at n = 2. **this does not rescue I-MOP7**, which
        fails criterion 2 on a different ground, but it is recorded because it
        widens the cheap case for any future problem.

**criterion 2, per problem.**

    1  I-BK1      **passes, cheaply.** every h_ij is a square, so no sign change
                  and no interchange. boundary functions
                  G̲_1 = 0.1x_1²+0.1x_2², Ḡ_1 = 0.2x_1²+0.3x_2²,
                  G̲_2 = 0.1(x_1−5)²+0.1(x_2−5)², Ḡ_2 = 0.3(x_1−5)²+0.5(x_2−5)².
                  centres 0.15x_1²+0.2x_2² and 0.2(x_1−5)²+0.3(x_2−5)²;
                  half-widths 0.05x_1²+0.1x_2² and 0.1(x_1−5)²+0.2(x_2−5)².
                  **all twelve image coordinates under the three phi are
                  non-negative-coefficient diagonal quadratics**: convex, and with
                  constant diagonal Hessians. this is p1's shape exactly.
    2  I-VU2      **fails.** G_1's half-width is 0.25(|x_1| + |x_2|), because
                  [1,1.5] ⊙ x has half-width 0.25|x| and x_1, x_2 change sign on
                  [−4,4]². a sum of two absolute values is not the absolute value
                  of any linear function, so it is not abs-differentiable at
                  x_1 = 0 or x_2 = 0 in the sense of [10] definition 30, and by
                  [10] theorem 34 G_1 is not Fréchet gH-differentiable there. the
                  axes are interior to the box.
    3  I-CH       **not reached**: fails criterion 5 outright, section 1.9's table.
                  recorded for completeness: G_1's half-width is the constant 1
                  and G_2's is 0.5|x_1²−x_2|, which has a kink on a parabola
                  interior to the box.
    4  I-FON      **fails.** [1,1] ⊖gH [1,3]⊙E with E = exp(−…) > 0 gives centre
                  1 − 2E and half-width E, both smooth, so gH-differentiability
                  holds; but E is a Gaussian bump, so 1 − 2E is convex only where
                  E is concave. theorem 3.3's phi-convexity fails on the box.
                  Hessians not constant.
    5  I-KW2      **fails.** products of polynomials and Gaussians with
                  sign-changing factors and negative coefficient intervals. no
                  convexity, no constant Hessians.
    6  I-Far1     **fails.** sums of five Gaussians with negative coefficient
                  intervals. no convexity.
    7  I-Hil1     **fails.** the trigonometric factor takes both signs on the box
                  — the cosine argument ranges over roughly [−0.35, 1.92] radians
                  — so the boundary functions interchange. no convexity.
    8  I-PNR      **fails.** G_1's boundary functions carry the cross term
                  10x_1x_2, whose Hessian contribution [[0,10],[10,0]] makes the
                  full Hessian at the origin [[2,10],[10,2]], indefinite. the
                  centre and both endpoint coordinates are non-convex. the
                  half-width 0.25(x_1⁴+x_2⁴) + 0.8(x_1²+x_2²) + 2 **is** convex,
                  and the quartic makes all Hessians non-constant.
    9  I-Deb      **fails.** gH-differences of Gaussians divided by x_1. not
                  convex, Hessians not constant.
    10 I-SD       **passes, by the diagonal-but-not-constant route.** every h is
                  positive on the box, so no interchange. G_1's four image
                  coordinates are linear with positive coefficients (the [√2,√3]
                  pair gives half-width ((√3−√2)/2)(x_2+x_3) ≥ 0, and the phi_ls
                  column 2r is likewise positive-coefficient linear); G_2's are
                  positive combinations of 1/x_j, convex on x > 0, with
                  3√3 > 2√2 keeping the phi_ls column positive. **all twelve
                  image coordinates are convex**; Hessians diagonal, zero for G_1
                  and 2λ/x³ for G_2. (15) decouples into four scalar equations
                  with closed-form roots.
    11 I-IKK1     **passes, cheaply.** [0,1]⊙x² has centre 0.5x² and half-width
                  0.5x²; [1,1]⊙x² is the real x². all image coordinates are
                  non-negative-coefficient diagonal quadratics. convex, constant
                  diagonal Hessians.
    12 I-VFM1     **passes, cheaply.** same shape as I-BK1 at m = 3, plus the
                  degenerate constants [1,1] and [2,2] which are real shifts.
    13 I-MHHM2    **passes, cheaply.** same shape, and with **no constant terms at
                  all** — six coefficient intervals on six squared displacements,
                  nothing else.
    14 I-Viennet  **fails.** sin, a rational term and a Gaussian. no convexity.
    15 I-AP1      **not determinable.** every h is positive and convex — a
                  positive-coefficient quartic, exp((x_1+x_2)/2) plus a
                  paraboloid, and a sum of decaying exponentials — so **all twelve
                  image coordinates are convex** and theorem 3.3 applies. but the
                  Hessians are neither constant nor diagonal (the exponential's
                  Hessian is rank-one and full), so (15) is a coupled nonlinear
                  system mixing cubics and exponentials and **this session cannot
                  say whether it is solvable in closed form.** not a pass.
    16 I-MOP7     **fails, on the ⊖gH.** G_1 alone is a convex diagonal quadratic.
                  but G_2 = A ⊖gH [17,20] with A's half-width
                  (5/72)(x_1+x_2−3)² + (1/32)(−x_1+x_2+2)², so G_2's half-width is
                  |that − 1.5|, which is zero on an ellipse **interior to the
                  box** (it is 0.75 at the origin and 0 at (2.5, 0.5), both below
                  1.5, and grows without bound) and is not convex there. equally,
                  G̲_2 = min(A̲ − 17, Ā − 20) is a minimum of two convex functions.
                  same for G_3 with [13,15]. theorem 3.3 fails.
    17 I-VFM2     **fails, on the ⊖gH.** G_1 and G_2 are I-BK1's shape extended to
                  three variables and are fine. G_3's half-width is
                  |0.05x_1² − 0.1x_2²| under one bracketing and
                  |0.05x_1² − 0.1x_2² − 0.05x_3²| under the other, ambiguity a-7;
                  both vanish on a cone interior to [−5,10]³ and neither is
                  convex. **the ambiguity does not change the verdict.**
    18 I-TR1      **fails, on the ⊖gH.** G_1's half-width is |7.5 − 0.1p| with
                  p = x_1³ + x_1²(1+x_2+x_3) + x_2³ + x_3³, which runs from 6 at
                  (1,1,1) to 336 at (4,4,4) and so crosses 75 inside the box.
                  not convex there. same for G_2 and G_3.
    19 I-AP4      **not determinable**, for I-AP1's reason at n = 3. all twelve
                  image coordinates convex; Hessians neither constant nor
                  diagonal; solvability of (15) in closed form not settled.
    20 I-Comet    **fails.** x_1³x_2² − 10x_1 − 4x_2 runs from −10 at (1,0,·) to
                  128.5 at (3.5,2,·), so the boundary functions interchange.
                  no convexity.

**criterion 4, the width driver, per problem.** the question is whether any image
column under any of the three phi is a function of a strict subset of the decision
variables. four problems have one, and one of them has three.

    9  I-Deb.     G_1 = [1,2]⊙x_1 with x_1 ∈ [1,3] > 0, so **both** of objective
                  1's columns under every phi — centre 1.5x_1, half-width 0.5x_1,
                  lower x_1, upper 2x_1, spread x_1 — are functions of x_1 alone.
                  **x_2 is free in objective 1.** fails criterion 2, so recorded
                  and not usable.
    11 I-IKK1.    **the richest case in the appendix.** under phi_cw the three
                  half-widths are 0.5x_2², 0.5(x_2−20)² and 0.5x_1²: each a
                  function of **one** variable, and not the same one across
                  objectives. under phi_ls the second column of each objective is
                  the same function doubled. under phi_lu the three lower columns
                  are x_1², (x_1−20)² and x_2², again each a function of one
                  variable. **three of six columns are single-variable functions
                  under every phi.** passes criterion 2 cheaply.
    20 I-Comet.   G_3 = [0.2,1]⊙(1+x_3)x_1², so both of objective 3's columns
                  under every phi are functions of (x_1, x_3) only. **x_2 is free
                  in objective 3.** fails criterion 2.
    all others.   every image column depends on every decision variable. verified
                  by inspection of the transcriptions in section 1.8.

criterion 4 is **not a disqualification**: docs/part1/part1_closing.md section 7.2
records it as section 3.4's protected-minimiser condition, and an example that has
it is a third registered test of the mechanism. **I-IKK1 is that example, and it
tests the mechanism on three columns at once rather than one.**

**criterion 5, per problem.** section 1.1 claim 1.1 settles it: nineteen pass,
**I-CH fails** because both its objectives are a crisp function plus a constant
band. the constant interval terms in I-PNR, I-Viennet, I-MOP7 and I-TR1 are
recorded beside genuine coefficient intervals and do not carry the
interval-valuedness on their own.

**criterion 1, per problem.** n ≤ 4 and 2m ≤ 6 everywhere. all twenty pass on
dimension. two are recorded with a reservation that is **not** a criterion-1
failure and belongs to the run rather than the reading: **I-AP1 and I-AP4 carry
exp(−x_j) on a box reaching x_j = −100**, so the objective spans a factor of e¹⁰⁰
and any sampled statistic on them would be dominated by floating-point range. and
**I-MOP7's box is [−400,400]²**, over which its quadratics span nine orders of
magnitude. recorded, not scored.

**the table. twenty rows, one line each.**

    #   name        c1 dim  c2 closed form   c3 sep  c4 driver     c5 source  verdict
    1   I-BK1       pass    **pass, cheap**  n/d     none          pass       4 of 4 readable; c3 open
    2   I-VU2       pass    fail (kink)      n/d     none          pass       fails c2
    3   I-CH        pass    fail             n/d     none          **fail**   fails c5, and c2
    4   I-FON       pass    fail (convex)    n/d     none          pass       fails c2
    5   I-KW2       pass    fail             n/d     none          pass       fails c2
    6   I-Far1      pass    fail             n/d     none          pass       fails c2
    7   I-Hil1      pass    fail             n/d     none          pass       fails c2
    8   I-PNR       pass    fail (convex)    n/d     none          pass       fails c2
    9   I-Deb       pass    fail             n/d     **x_2 free**  pass       fails c2
    10  I-SD        pass    **pass, diag**   n/d     none          pass       4 of 4 readable; c3 open
    11  I-IKK1      pass    **pass, cheap**  n/d     **3 columns** pass       4 of 4 readable; c3 open
    12  I-VFM1      pass    **pass, cheap**  n/d     none          pass       4 of 4 readable; c3 open
    13  I-MHHM2     pass    **pass, cheap**  n/d     none          pass       4 of 4 readable; c3 open
    14  I-Viennet   pass    fail             n/d     none          pass       fails c2
    15  I-AP1       pass    n/d (solvable?)  n/d     none          pass       c2 and c3 open
    16  I-MOP7      pass    fail (⊖gH)       n/d     none          pass       fails c2
    17  I-VFM2      pass    fail (⊖gH)       n/d     none          pass       fails c2
    18  I-TR1       pass    fail (⊖gH)       n/d     none          pass       fails c2
    19  I-AP4       pass    n/d (solvable?)  n/d     none          pass       c2 and c3 open
    20  I-Comet     pass    fail             n/d     **x_2 free**  pass       fails c2

    n/d = not determinable from the paper. not a pass.

**the verdict, stated as the gate requires it.** **no example passes the gate**,
because criterion 3 cannot be answered by reading and not determinable is not a
pass. **five examples pass every criterion a reading can settle** — I-BK1, I-SD,
I-IKK1, I-VFM1 and I-MHHM2 — and on four of those five the closed-form route
closes cheaply on the plan's own condition. that is the strongest verdict the
reading could have produced short of a pass, and section 7 says what it costs to
convert it.

### 1.10 the five candidates, compared, and one risk the reading cannot settle

    I-BK1     n=2, m=2, 4 columns. p1's exact shape: diagonal quadratic centres,
              diagonal quadratic half-widths, constant diagonal Hessians. **the
              only problem in the appendix with published checkpoints** — Table 1's
              point and equation (25)'s closed-form curve, section 1.6. no
              constant terms. box [−10,10]².
    I-SD      n=4, m=2, 4 columns. the shape docs/plan_after_meeting.md section
              d0.1 explicitly prefers ("an example at n = 4 and m = 2 is
              preferable to one at n = 3 and m = 3 on that ground alone"). route
              closes by the diagonal-but-not-constant case. irrational bounds
              √2 on two variables. no constant terms.
    I-IKK1    n=2, m=3, 6 columns. **the only criterion-4 example that also
              passes criterion 2.** three of six columns are single-variable
              functions. constant Hessians, diagonal, cheap. box [−50,50]².
    I-VFM1    n=2, m=3, 6 columns. cheapest route, no criterion-4 complication,
              two degenerate constant shifts.
    I-MHHM2   n=2, m=3, 6 columns. cheapest route, **no constant terms of any
              kind**, box [0,1]², six coefficient intervals and nothing else.
              the cleanest statement of criterion 5 in the appendix.

**the risk, and it is criterion 3 restated in structural terms.**
docs/part1/a1_uncertainty_model.md part 4 records that under a half-width whose
driver is aligned with the centres' own optimum, phi_lu and phi_ls give identical
sets and phi_cw gives the crisp order. **on I-BK1, I-VFM1 and I-MHHM2 every
objective's half-width is minimised at exactly the point its centre is minimised
at** — on I-BK1, r_1 and c_1 both at the origin and r_2 and c_2 both at (5,5); on
I-MHHM2, r_i and c_i both at the paper's printed displacement centre. that is the
alignment regime. it does **not** follow that the orders coincide — the ratio
r_1/c_1 on I-BK1 is 1/3 on the x_1 term and 1/2 on the x_2 term, so the half-width
is not a multiple of the centre and the four phi_cw columns are not two plus two
redundant ones — **but it is the direction in which the risk lies, and reading
cannot settle it.** that is exactly why criterion 3 is marked not determinable and
why section 7's first step is the one that answers it.

**I-IKK1 is the one candidate not in that regime.** its half-widths 0.5x_2²,
0.5(x_2−20)² and 0.5x_1² are minimised on *lines*, not points, so no half-width's
minimiser coincides with its centre's. that is a different structure from p1's and
from the other four, and it is why section 7 recommends it second and for a
different purpose.


## 2. [9], Ishibuchi and Tanaka: six order relations, and p-02

### 2.1 the paper's a_w is the half-width, confirmed three times

**claim 2.1. [9] writes "width" and means half-width, and the paper settles this
itself in three independent places.**

verdict: **confirmed**, and this closes the reading half of p-02.

first, **by definition**. section 2, printed page 220, equations (2.2) and (2.4):

>     A = (a_c, a_w) = {a : a_c − a_w ⩽ a ⩽ a_c + a_w, a ∈ ℝ},        (2.2)
>
>     a_c = ½(a_R + a_L),                                            (2.3)
>     a_w = ½(a_R − a_L).                                            (2.4)

equation (2.4) is unambiguous. the paper's own prose calls a_w "the width of A",
which is the source of the whole question; **the formula is the half-width and the
prose is loose.**

second, **in a proof**. the proof of proposition 4.1, printed page 222, equation
(4.6), uses

>     a_R = a_L + 2a_w ⩽ b_L + 2b_w = b_R.                           (4.6)

this is the equation docs/plan_after_meeting.md section c2 cites and it is exactly
where the plan said it was.

third, **numerically, in the paper's own worked example**. example 1, printed page
224, equations (5.10) and (5.11):

>     Z(x_a) = [1850, 2215] = (2032.5, 182.5),                       (5.10)
>     Z(x_b) = [1695, 2515] = (2105, 410).                           (5.11)

(2215 − 1850)/2 = 182.5 and (2515 − 1695)/2 = 410. both check. the full widths
would be 365 and 820.

**so the a_w-is-the-half-width reading is the paper's own, three times over, and
it is not an inference the project has to defend.** p-02's substantive half, which
docs/plan_after_meeting.md section c2 answered while surveying papers/, is
confirmed with printed page numbers, which is what the row was waiting for.

### 2.2 the order relations, all six of them, each located

docs/plan_after_meeting.md section c2 says [9] "holds four order relations and a
fifth". **the reading finds six**: four in section 3 and two in section 4, the
second of which the plan did not anticipate.

    #  relation   definition   equations      page  sense    condition on A ⩽ B
    1  ⩽_LR       Def. 3.1     (3.1),(3.2)    221   max      a_L ⩽ b_L and a_R ⩽ b_R
    2  ⩽_cw       Def. 3.2     (3.3),(3.4)    221   max      a_c ⩽ b_c and a_w ⩾ b_w
    3  ⩽*_LR      Def. 3.3     (3.9),(3.10)   222   min      a_L ⩽ b_L and a_R ⩽ b_R
    4  ⩽*_cw      Def. 3.4     (3.11),(3.12)  222   min      a_c ⩽ b_c and a_w ⩽ b_w
    5  ⩽_LC       (unnumbered) (4.1),(4.2)    222   max      a_L ⩽ b_L and a_c ⩽ b_c
    6  ⩽*_LC      (unnumbered) (4.15),(4.16)  223   min      a_R ⩽ b_R and a_c ⩽ b_c

transcribed, in the paper's own words.

> **Definition 3.1.** Let us define the order relation ⩽_LR between A = [a_L, a_R]
> and B = [b_L, b_R] as
>
>     A ⩽_LR B  iff  a_L ⩽ b_L and a_R ⩽ b_R,                        (3.1)
>     A <_LR B  iff  A ⩽_LR B and A ≠ B.                             (3.2)

printed page 221, with the paper's gloss: "This order relation represents the
decision maker's preference for the alternative with the higher minimum profit and
maximum profit."

> **Definition 3.2.** Let us define the order relation ⩽_cw between A = (a_c, a_w)
> and B = (b_c, b_w) as
>
>     A ⩽_cw B  iff  a_c ⩽ b_c and a_w ⩾ b_w,                        (3.3)
>     A <_cw B  iff  A ⩽_cw B and A ≠ B.                             (3.4)

printed page 221, with the gloss: "this order relation represents the decision
maker's preference for the alternative with the higher expected value and less
uncertainty."

> **Definition 3.3.** Let us define the order relation ⩽*_LR between A = [a_L, a_R]
> and B = [b_L, b_R] as
>
>     A ⩽*_LR B  iff  a_L ⩽ b_L and a_R ⩽ b_R,                       (3.9)
>     A <*_LR B  iff  A ⩽*_LR B and A ≠ B.                          (3.10)

printed page 222. the paper states in the following sentence: "It should be noted
that ⩽*_LR by Definition 3.3 is the same order relation as ⩽_LR by Definition
3.1." the two differ only in reading direction — profits versus costs.

> **Definition 3.4.** Let us define the order relation ⩽*_cw between A = (a_c, a_w)
> and B = (b_c, b_w) as
>
>     A ⩽*_cw B  iff  a_c ⩽ b_c and a_w ⩽ b_w,                      (3.11)
>     A <*_cw B  iff  A ⩽*_cw B and A ≠ B.                          (3.12)

printed page 222, with the gloss: "The order relation ⩽*_cw represents the decision
maker's preference for the alternative with the lower expected cost and less
uncertainty." and the paper's own warning immediately before it: "It should be
noted that the order relation ⩽*_cw by Definition 3.4 is different from ⩽_cw by
Definition 3.2."

> [the fifth]  A ⩽_LC B  iff  a_L ⩽ b_L and a_c ⩽ b_c,               (4.1)
>              A <_LC B  iff  A ⩽_LC B and A ≠ B.                    (4.2)

printed page 222, in section 4.1, introduced with "In order to simplify this
definition, first we define the order relation ⩽_LC as". **it carries no
definition number**, which is why the plan called it "a fifth" rather than naming
it; it is located by equation number only.

> [the sixth]  A ⩽*_LC B  iff  a_R ⩽ b_R and a_c ⩽ b_c,             (4.15)
>              A <*_LC B  iff  A ⩽*_LC B and A ≠ B.                 (4.16)

printed page 223, in section 4.2, introduced with "For the minimization problem,
the order relation ⩽*_LC is defined as". **also unnumbered.** this is the one the
plan did not anticipate, and section 2.4 below is why it matters.

**two propositions on the section-3 relations, recorded for completeness.**
proposition 3.1, equations (3.5)-(3.8), printed page 221: if A ⩽_LR B and
B ⩽_cw A both hold then A = B, i.e. the maximisation pair never conflict.
proposition 3.2, equation (3.13), printed page 222: the same for the minimisation
pair ⩽*_LR and ⩽*_cw, with the proof omitted as similar.

**the reformulations the orders are for.** definition 4.2, printed page 223: x is
a solution of (1.1) iff there is no x′ with Z(x) <_LC Z(x′); and the solution set
is the Pareto set of max (Z_L(x), Z_c(x)), equation (4.14), printed page 223.
definition 4.4, printed page 223: x is a solution of (1.3) iff there is no x′ with
Z(x′) <*_LC Z(x); the solution set is the Pareto set of min (Z_R(x), Z_c(x)),
equation (4.21), printed page 223. **[9] therefore reduces its own m = 1 problem
to a two-objective real problem, which is the m = 1 case of [1]'s 2m
transformation and is where that construction comes from.**

### 2.3 automorphism status and the containment criterion, applied against the registry

the registry, in centre and half-width coordinates, from
docs/plan_after_meeting.md section c1:

    phi_lu = [[1, −1], [1, 1]]     phi_ls = [[1, −1], [0, 2]]     phi_cw = I

admissibility in [1] is a nonzero determinant and nothing else,
docs/part1/a0_framework.md section c2. **all six relations of [9] are induced by a
linear map on the endpoint pair and all six have nonzero determinant, so all six
lie in 𝔄_1.** the matrices below are the row pairs in centre and half-width
coordinates.

    ⩽_LR   / ⩽*_LR   rows (c−w, c+w)  =  [[1,−1],[1,1]]   det  2
    ⩽_cw            rows (c, −w)      =  [[1, 0],[0,−1]]  det −1
    ⩽*_cw           rows (c, w)       =  [[1, 0],[0, 1]]  det  1
    ⩽_LC            rows (c−w, c)     =  [[1,−1],[1, 0]]  det  1
    ⩽*_LC           rows (c+w, c)     =  [[1, 1],[1, 0]]  det −1

the containment criterion, applied. M is computed as φ_B φ_A^{−1}; M entrywise
non-negative and invertible gives φ_A-dominance ⟹ φ_B-dominance and ND_B ⊆ ND_A.

**⩽*_LR, definition 3.3.** M against phi_lu is the identity. **it is φ_lu**,
example 2.2 of [1]. **already in the registry; a check, and not even a candidate.**

**⩽*_cw, definition 3.4.** M against phi_cw is the identity. **it is φ_cw**,
example 2.4 of [1], **in the same coefficients**. this is the substantive half of
p-02, confirmed against printed pages 222 and 220. **already in the registry; a
check.**

**⩽_LC, equations (4.1)-(4.2).** against phi_lu, M = [[1,−1],[1,0]] · ½[[1,1],
[−1,1]] = [[1, 0],[½, ½]]. entrywise non-negative, det ½ ≠ 0. **direction:
phi_lu-dominance ⟹ ⩽_LC-dominance, so ND_LC ⊆ ND_lu.** against phi_ls,
M = [[1,−1],[1,0]] · [[1,½],[0,½]] = [[1, 0],[1, ½]]. entrywise non-negative,
det ½ ≠ 0. **ND_LC ⊆ ND_ls.** against phi_cw, M = [[1,−1],[1,0]] and its inverse
[[0,1],[−1,1]] both carry a negative entry, so the criterion gives nothing in
either direction. **verdict: excluded as a check, nested inside two of the three
registry members.** the coefficients on (f_l, f_u) are λ = (1,0), β = (½,½) with
determinant ½, which is what docs/plan_after_meeting.md section c2 records; the
computation above is the same fact in centre–half-width coordinates and the two
agree.

**⩽*_LC, equations (4.15)-(4.16). this is new to the project.** against phi_cw,
M = [[1,1],[1,0]]. entrywise non-negative, det −1 ≠ 0. **ND_LC* ⊆ ND_cw.** against
phi_lu, M = [[1,1],[1,0]] · ½[[1,1],[−1,1]] = [[0, 1],[½, ½]]. entrywise
non-negative, det −½ ≠ 0. **ND_LC* ⊆ ND_lu.** **verdict: admissible, and excluded
as a check** — nested inside phi_cw and phi_lu both. section 2.4 shows the paper
proves the same thing independently.

**⩽_cw, definition 3.2, the maximisation order preferring the higher centre and
the *wider* interval.** in centre–half-width coordinates it is [[1,0],[0,−1]].
against phi_cw, M = [[1,0],[0,−1]], negative entry; the inverse is itself, also
negative. against phi_lu, M = ½[[1,1],[1,−1]], negative entry; the reverse
M′ = [[1,1],[1,−1]], negative. against phi_ls, M = [[1,½],[0,−½]], negative; the
reverse M′ = [[1,1],[0,−2]], negative. **verdict: admissible, and nested with none
of the three. it would be a finding and not a check**, and the sign change is
exactly what docs/plan_after_meeting.md section c1 predicts a genuinely new order
must carry.

**it is not added to the registry.** the session's constraint forbids it, and the
plan's own reservation stands: ⩽_cw's second image coordinate is −r, concave
wherever r is convex, so theorem 3.3's phi-convexity fails for every problem the
project has, and [1] covers minimisation in theorem 3.1 and maximisation in
theorem 3.2 through −φ but not a mixed sense. **recorded as the one genuine
candidate the now-open literature adds, and nothing more.**

### 2.4 proposition 4.1, transcribed, and its minimisation twin

**claim 2.2. [9]'s propositions 4.1 and 4.2 confirm the containment criterion
independently, on two cases neither was built for.**

verdict: **confirmed.** docs/plan_after_meeting.md section c2 records proposition
4.1 as "the first independent check the criterion has had". **the reading finds a
second, proposition 4.2, which the plan did not have.**

proposition 4.1, printed page 222, transcribed in full with its proof, which spans
printed pages 222 and 223:

> **Proposition 4.1.** It follows that
>
>     A ⩽_LC B  iff  A ⩽_LR B  or  A ⩽_cw B,                          (4.3)
>     A <_LC B  iff  A <_LR B  or  A <_cw B.                          (4.4)
>
> **Proof.** Since (4.4) is easily obtained from (4.3), we only prove (4.3).
>
> First we show that if A ⩽_LC B then A ⩽_LR B or A ⩽_cw B. From A ⩽_LC B,
>
>     a_L ⩽ b_L,   a_c ⩽ b_c                                          (4.5)
>
> hold. If we assume that a_w ⩾ b_w, then A ⩽_cw B holds from (4.5). On the
> contrary, if we assume that a_w ⩽ b_w, then A ⩽_LR B holds from (4.5) and the
> following inequality:
>
>     a_R = a_L + 2a_w ⩽ b_L + 2b_w = b_R.                            (4.6)
>
> Therefore, it was shown that if A ⩽_LC B then A ⩽_LR B or A ⩽_cw B.
>
> Next we show that if A ⩽_LR B then A ⩽_LC B. From A ⩽_LR B,
>
>     a_L ⩽ b_L,   a_R ⩽ b_R                                          (4.7)
>
> hold. From (4.7),
>
>     a_c = ½(a_R + a_L) ⩽ ½(b_R + b_L) = b_c                         (4.8)
>
> holds. Therefore A ⩽_LC B holds from (4.7) and (4.8).
>
> Last we show that if A ⩽_cw B then A ⩽_LC B. From A ⩽_cw B,
>
>     a_c ⩽ b_c,   a_w ⩾ b_w                                          (4.9)
>
> hold. From (4.9),
>
>     a_L = a_c − a_w ⩽ b_c − b_w = b_L                              (4.10)
>
> holds. Therefore A ⩽_LC B holds from (4.9) and (4.10).  □

and its twin, proposition 4.2, printed page 223, transcribed:

> **Proposition 4.2.** It follows that
>
>     A ⩽*_LC B  iff  A ⩽*_LR B  or  A ⩽*_cw B,                      (4.17)
>     A <*_LC B  iff  A <*_LR B  or  A <*_cw B.                      (4.18)

with the paper's note immediately before it: "Then the following proposition can
be proven in a similar way as the proof of Proposition 4.1."

**why the two propositions are checks of the criterion and not restatements of
it.** each says that a relation is the **union** of two others. a union dominates
at least as often as either component, so its non-dominated set is contained in
each component's. the containment criterion, applied to the same three relations
without knowing the proposition, returns the same two containments and no others.
**the criterion and the published proposition agree in both cases, and the
minimisation case is the one that matters to this project**, because the project
minimises and because ⩽*_LR and ⩽*_cw are exactly φ_lu and φ_cw. **so proposition
4.2 says, in a 1990 paper, that ND_{LC*} ⊆ ND_lu ∩ ND_cw — which is the criterion's
prediction, published, on the project's own two registry members.**

docs/part1/a_close_containment.md section 6 records s-11, whether any of the
containment is published. **this is not an answer to s-11** — s-11 asks about the
containments *between* φ_lu, φ_ls and φ_cw, and proposition 4.2 is about a fourth
relation's containment in two of them. it is a check on the criterion's
correctness, not on the project's own containments. recorded so the distinction is
not lost.

### 2.5 what this section closes

**p-02 is closed.** the row asked whether [9] states the centre-width comparison in
example 2.4's coefficients. **it does**: definition 3.4, equations (3.11) and
(3.12), printed page 222, a_c ⩽ b_c and a_w ⩽ b_w for minimisation, with a_w the
half-width by the paper's own equation (2.4) on printed page 220, by equation (4.6)
in the proof of proposition 4.1 on printed page 222, and numerically by equations
(5.10) and (5.11) on printed page 224. **the printed page numbers the evidence
rule requires are now recorded, which is what the row was waiting for.** the row's
second clause, that the closing session should also record definitions 3.1, 3.2,
3.3 and equation (4.1), is discharged by section 2.2 above, which records those and
two more.


## 3. [10], and p-05

### 3.1 the regularity criterion: theorem 34, confirmed exactly

**claim 3.1. b1's "theorem 34" is the paper's theorem 34, verbatim.**

verdict: **confirmed.** docs/part1/b1_phi_efficient_sets.md section 1.3 cites the
criterion as "Theorem 34" from `literature/gH-differentiability calculus for
interval analysis.md` with the number unverified, [10] not having been on disk.
**the number is right and so is the statement.**

location: theorem 34, section 4, printed page 13. transcribed verbatim:

> **Theorem 34.** The IV-function 𝙵 : K ⊆ ℝⁿ → I(ℝ), 𝙵(x) = (f̂(x); f̃(x)) is
> Fréchet gH-differentiable at a point x⁽⁰⁾ ∈ K, if and only if, f̂ and f̃ are
> (respectively) Fréchet differentiable and abs-differentiable at x⁽⁰⁾.

b1 quoted it as "F = (f̂; f̃) is Fréchet gH-differentiable at x⁽⁰⁾ iff f̂ is Fréchet
differentiable and f̃ is abs-differentiable at x⁽⁰⁾". **the same statement, and the
summary's number was correct.**

the supporting definitions, both located:

    **Definition 29**, Fréchet gH-differentiability, equation (24), printed page
        11. the definition theorem 34 characterises.
    **Definition 30**, Fréchet absolute differentiability, equation (28), printed
        pages 11-12. b1 cited this as "definition 30 of the same summary" and the
        number is correct. the definition: f is abs-differentiable at x⁽⁰⁾ iff
        there is a continuous linear w_{x⁽⁰⁾} : ℝⁿ → ℝ with
        lim_{‖h‖→0} ( ||f(x⁽⁰⁾+h)| − |f(x⁽⁰⁾)|| − |w_{x⁽⁰⁾}(h)| ) / ‖h‖ = 0.

**b1's paraphrase of definition 30 is not quite the paper's.** b1 wrote
"abs-differentiability of f̃ at x⁽⁰⁾ meaning that |f̃| has a classical Fréchet
derivative there". that is **sufficient but not necessary**: it is [10]'s
**proposition 32**, not its definition 30. the difference does not affect b1's
conclusion, and section 3.2 shows it strengthens it. recorded so the memoria
quotes the definition and not the paraphrase.

### 3.2 proposition 32, which b1 did not have and which part 2 needs

location: proposition 32, printed page 12. transcribed verbatim:

> **Proposition 32.** If f : K ⊆ ℝⁿ → ℝ is such that its absolute value
> |f| : K ⊆ ℝⁿ → ℝ is Fréchet differentiable at x⁽⁰⁾ ∈ K with differential function
> D|f|(x⁽⁰⁾), then f is abs-differentiable at x⁽⁰⁾ with the same differential (i.e.,
> D_abs f(x⁽⁰⁾) = D|f|(x⁽⁰⁾)).
>
> In particular, **if f : K ⊆ ℝⁿ → ℝ⁺ ∪ {0} is differentiable then it is also
> abs-differentiable.**

**the second sentence is what part 2 needs and it is stronger than the condition
a1 imposed.** docs/part1/a1_uncertainty_model.md required p1's radius to be
**strictly** positive, and docs/part1/b1_phi_efficient_sets.md section 1.3 leans on
that ("every function involved being a polynomial with a strictly positive
radius"). **proposition 32 covers non-negative radii including their zeros.** that
matters directly: **I-BK1's half-widths vanish** — 0.05x_1² + 0.1x_2² is zero at
the origin and 0.1(x_1−5)² + 0.2(x_2−5)² at (5,5), both interior to the box — and
under a1's strict-positivity rule that would have looked like a problem. **it is
not one.** proposition 32 gives abs-differentiability there and theorem 34 gives
Fréchet gH-differentiability. the same applies to I-IKK1, I-VFM1 and I-MHHM2.

so the regularity leg of b1's route on any of the five candidates is:
**[10] proposition 32, printed page 12, then [10] theorem 34, printed page 13.**
both numbered, both now verified against the paper.

**remark 33, printed page 12, recorded because it is the negative test.**

> A useful fact is that for a function f(·) to be abs-differentiable it is
> necessary that left and right partial derivatives need to exist and have the same
> absolute value; in particular, if there exists j such that
> |∂f(x⁽⁰⁾)/∂x_j^−| ≠ |∂f(x⁽⁰⁾)/∂x_j^+|, then f cannot be abs-differentiable at x⁽⁰⁾.

and its companion sentence on the same page: "It does not seem possible to
establish general sufficient conditions for abs-differentiability of f, similar to
the well known one based on the class of C⁽¹⁾ functions." **there is no C¹
sufficient condition; proposition 32's non-negativity condition is what there is.**

remark 33 is also why section 1.9's verdict on I-MOP7, I-VFM2 and I-TR1 is a
criterion-2 failure on **convexity** and not on differentiability: their half-widths
are of the form |q(x) − k| with q smooth, whose one-sided partials at the kink have
equal absolute value, so they **are** abs-differentiable there and gH-differentiable
by theorem 34. **it is theorem 3.3 of [1] that fails on them, not [10].**

### 3.3 the gH-difference is not under a numbered definition in [10]

**claim 3.2. p-05's first half has a negative answer: [10] states the
gH-difference in an unnumbered display, not under a numbered definition, and not
under an equation number either.**

verdict: **confirmed.**

location: section 2, "Preliminaries on intervals", printed page 3, between the
Minkowski operations (equations (4) and (5), printed page 2) and Remark 3. the
display, transcribed:

>     The gH-difference of two intervals 𝙰 and 𝙱 is the following:
>
>         𝙰 ⊖_gH 𝙱 = 𝙲  ⟺  (a) 𝙰 = 𝙱 ⊕_M 𝙲,   or  (b) 𝙱 = 𝙰 ⊕_M (−1)𝙲.
>
>     The gH-difference of two intervals always exists and is given by
>
>         𝙰 ⊖_gH 𝙱 = [min{a̲ − b̲, ā − b̄}, max{a̲ − b̲, ā − b̄}]
>                  = (â − b̂ ; |ã − b̃|).

**neither display carries a number.** the surrounding numbered items are equations
(4) and (5) before it and equation (6), the Pompeiu-Hausdorff distance, after it.

**consequence for the memoria.** p-05 asked "under which numbered definition does
[10] state the gh-difference". **there is none.** the memoria must cite it by page
— [10], section 2, printed page 3 — or cite [10]'s own source for it, Stefanini
2008, which is [10]'s reference and is also [16]'s reference [31], "A
generalization of Hukuhara difference", Advances in Soft Computing 48, pages
203-210, Springer 2008. **[16] does state it under a number**: definition 2.1,
printed page 4, attributed to that same Stefanini 2008. **so if the memoria wants a
numbered citation for the gH-difference, [16] definition 2.1 is the one available
in the corpus, and [10] is the citation for the midpoint-radius form.**

the second, midpoint-radius form (â − b̂ ; |ã − b̃|) is the one section 1.8 uses to
locate the kinks in I-MOP7, I-VFM2, I-TR1 and I-Viennet. it is on printed page 3 of
[10] and it is unnumbered there.

### 3.4 what this section closes

**p-05 is closed, in both halves, one positively and one negatively.**

    the regularity criterion. **theorem 34, printed page 13 of [10]**, verbatim as
        b1 quoted it, with the number confirmed. the supporting definitions are
        definition 29, printed page 11, and definition 30, printed pages 11-12.
        and **proposition 32, printed page 12**, supplies the sufficient condition
        b1 actually used and widens it to non-negative radii with zeros.
    the gH-difference's definition number. **[10] has none.** it is an unnumbered
        display in section 2, printed page 3. the memoria cites it by page, or
        cites [16] definition 2.1, printed page 4, which does number it.

**this removes the one unverified number in b1's derivation.**
docs/part1/part1_closing.md section 7.4 lists p-05 as "the one unverified number in
b1's derivation"; it is now verified, and b1's section 1.3 can drop its
qualification. **the citation in b1 is not wrong and needs no correction to its
conclusion** — only the paraphrase of definition 30 noted in section 3.1 should be
replaced by proposition 32, which is what b1 was actually using.


## 4. [7], [8] and [13]: the objection, and why none of their relations enters 𝔄_m

### 4.1 the objection, transcribed, from all three

docs/part1/part1_closing.md's memoria has to state the objection accurately before
answering it, so this is transcription and not summary. **the three papers do not
make the same objection**, and the differences matter.

**[7], Cui et al. 2024.** the taxonomy is set up on printed page 1, right column,
section 1:

> At present, some interval evolutionary algorithms have been proposed to address
> IMOPs and IMaOPs. These methods can be categorized into two types. The first type
> converts the interval optimization problems to deterministic optimization
> problems.

and the objection is on printed page 2, left column, at the end of that paragraph,
transcribed in full:

> Bhunia et al. transform IMOP into a single-objective optimization problem using
> interval order relations and interval metrics [32]. Guo et al. proposed a
> knowledge-guided MOEA/D using interval midpoints [33]. Gong et al. integrated the
> midpoint and width of intervals to transform the interval objective into a
> precision objective, then applied an evolutionary algorithm to solve the
> transformed optimization problem [34]. SetGA proposed by Gong et al. [35] uses an
> indirect method to convert IMaOPs into a bi-objective MOP with objectives of
> hypervolume and uncertainty and then uses a set-based genetic algorithm to solve
> the MOP. These methods fall under the category of indirect methods [12].
> **Obviously, such methods lose interval information, which has a negative impact
> on the accuracy of the original problem.**

and the positive claim for the alternative, immediately following, printed page 2,
left column:

> Our study focuses on the second type approach, which constructs interval
> dominance methods and performance metrics to address interval optimization
> problems directly. **This methodology yields an interval Pareto front (PF)
> without compromising the inherent interval characteristics of the problem.**

**the sentence is asserted and not argued.** "Obviously" is the whole of the
support; no measurement, no example and no reference is given for it in that
paragraph. **that is worth saying in the memoria, plainly and without polemic**,
because the project's answer is a measurement and the objection is not.

**[8], Zhang et al. 2025.** two statements, and the first is the more precise one.
printed page 1, right column, section 1:

> Recently, transformation techniques (i.e. sampling [15], weighting [16], and
> mapping [17]) have been employed in IMaOEAs to convert the IMaOPs into MaOPs, and
> then existing deterministic optimization methods can be utilized to solve IMaOPs
> [18]. **However, when the span of the interval is too large, the application of
> transformation techniques may inadvertently disrupt the inherent conflict
> relationship between objectives**; hence, it is imperative to develop specific
> strategies (i.e. interval ordinal [19], reference intervals [20] and interval
> confidence level [21]) that can evaluate the intervals individual advantages and
> disadvantages intuitively […]

and printed page 3, left column, section 2:

> The advantage of the above methods is that the interval is reformulated in the
> form of sets, thereby streamlining the solution process. **Nevertheless, these
> methods may result in a loss of the inherent conflict relationship between
> objectives in IMaOPs, leading to inaccuracies in the final outcome [38].**

**[8]'s objection is stronger, more specific and conditional**, and it is the one
the memoria should answer. it names a mechanism — the conflict relationship between
objectives is disrupted — and a condition under which it bites: **when the span of
the interval is too large.**

**[13], Wen et al. 2026.** printed page 2, section 1:

> Currently, two common research methods have been employed for addressing ICMOPs.
> The first method is based on indirect conversion ideas [22]. By introducing
> certain decision parameters into an evaluation model, ICMOPs can be transformed
> into a deterministic multi-objective or single objective constrained optimization
> problem with real number parameters [23]. […] **Although these indirect
> transformation methods are relatively easy to solve, they tend to introduce
> instability in key interval information, resulting in slow convergence and
> unreliable feasible solutions [27].**

**[13]'s objection is about the solver's behaviour**, not the problem's structure:
slow convergence and unreliable feasible solutions. it is the weakest of the three
as an objection to the construction and the most specific as a claim about runs.

**a fourth, from [16], and it is not the same objection.** section 1.7 above
records [16]'s two statements. **the first is about the scalarization f_l + f_u and
not about the 2m transformation, and must not be quoted as if it were.** the second,
in the conclusion on printed page 27, is the technical one and is the only one of
the four that names a checkable condition on the construction itself: the
transformation is valid where the boundary functions do not interchange.

### 4.2 the dominance relations of [7], [8] and [13], located, and why none is an automorphism

**claim 4.1. none of the three papers' dominance relations lies in 𝔄_m, and the
reason is different in each case.**

verdict: **confirmed.** docs/plan_after_meeting.md section c2's table records them
as "not excluded by the criterion but by admissibility: they are not automorphisms
of the plane". **the reading confirms that and supplies the three distinct
reasons**, which is what the memoria needs, since "not an automorphism" without a
reason reads as a definition rather than an argument.

what an 𝔄_m order is, so that each exclusion can be stated against it. by [1]
definition 2.1 and equations (2) and (3), docs/part1/a0_framework.md sections c1 and
c4: a φ-order assigns to each interval A a **fixed pair of real numbers** φ̄(A),
depending on A alone, by a **linear** map of the endpoint pair, and compares two
intervals by componentwise ⩽ on those pairs. three consequences follow and each is
one of the exclusions below: the assignment depends on A alone and not on what A is
compared with; the map is linear; and componentwise ⩽ is transitive and
antisymmetric, so a φ-order is a partial order.

**[7], the information entropy dominance, IED.** located: section 3.2, equations
(15) to (19), printed page 5, with the four prior methods IDM1 to IDM4 at equations
(4) to (9), printed page 3, and the multiobjective aggregation at equation (10),
printed page 3.

the mechanism, printed page 5: for each objective k, the population's convergence
entropy H_ck and uncertainty entropy H_wk are computed over all N individuals,
equations (15) to (18); if H_ck < H_wk the comparison uses the convergence-based
confidence level P_c of equation (19), if H_ck > H_wk it uses the uncertainty-based
one, and if they are equal it falls back on IDM3.

**the exclusion, and it is decisive before linearity is even reached. the relation
is a function of the whole population, not of the two intervals.** H_ck and H_wk are
sums over all N individuals at generation t. **so "a dominates b" is not a
statement about a and b**; the same pair can be ordered one way in one generation
and the other way in the next with no change to either interval. no assignment
φ̄(A) depending on A alone can reproduce that, so IED is not in 𝔄_m for any φ, and
the question of which φ does not arise. two further reasons, recorded but not
needed: equation (19)'s confidence level is a ratio with a `max` clamp, not linear
in the endpoints; and the rule "P > γ ⟹ a dominates b" with γ ∈ [½,1) is a
thresholded probability, hence intransitive in general.

**[8], IP-dominance and DIP-dominance.** located: definition 2 and equation (4)
with Remark 1, printed page 5; definition 3 and equation (6), with the uncertainty
measure at equation (5) and the decay function at equations (7) and (8), printed
page 6.

**the per-objective relation is φ_lu.** Remark 1, printed page 5, transcribed:

> the notation "<_IN" and "‖_IN" are "less than" and "incomparable" in the interval
> sense. f(x_i, u) <_IN f(x_j, u) means that f̲(x_i, u) is no more than f̲(x_j, u),
> and f̄(x_i, u) is no more than f̄(x_j, u), and f(x_i, u) ≠ f(x_j, u).

that is ⩽ on both endpoints with A ≠ B — **exactly [9]'s <_LR, equation (3.2), and
exactly example 2.2 of [1], φ_lu.** the interval order [8] uses *is* a registry
member.

**the exclusion is in the aggregation across objectives, not in the interval
order.** definition 2, equation (4), printed page 5, requires for domination that
for **all** p, either f_p(x_i) <_IN f_p(x_j) **or the two are incomparable**, and
that for some q the strict relation holds. **the "or incomparable" disjunct is what
leaves 𝔄_m.** componentwise ⩽ on ℝ^2m admits no such disjunct: incomparability in
one objective would block domination, and here it permits it. the effect is to
dominate *more* often than φ_lu-dominance, so ND_IP ⊆ ND_lu — the containment
direction the criterion would give if the criterion applied, which it does not,
because the relation is not induced by any φ. **this is worth a sentence in the
memoria: [8]'s departure from the framework is not a different interval order but a
different multiobjective aggregation.**

DIP-dominance, definition 3 and equation (6), printed page 6, adds a second
exclusion of [7]'s kind: it requires U_i < U_j **and** U_i < U_t, where U is the
interval diagonal distance, equation (5), and U_t = −U_max e^{αt} + 2, equation
(7), **depends on the iteration index t and on the population's U_max**. again not
a relation on pairs of intervals. the paper proves DIP-dominance irreflexive,
asymmetric and transitive, Properties 1 to 3 on printed page 6, which is a partial
order **at fixed t**, and it is a different partial order at each t.

**[13], interval-probability dominance.** located: definition 3, equations (4) to
(6), printed page 3; definition 4, equation (7), printed page 4.

definition 3, printed page 3, transcribed:

> **Definition 3. Interval probability:** For two interval-valued objectives
> I = [f̲_z(x_i,c), f̄_z(x_i,c)] and J = [f̲_z(x_j,c), f̄_z(x_j,c)], if given a
> minimal interval value between I and J as R = [R̲, R̄], where R̲ and R̄ are the
> smallest and second smallest of U = [f̲_z(x_i,c), f̄_z(x_i,c), f̲_z(x_j,c),
> f̄_z(x_j,c)], respectively. Then the probability of I less than J is defined as
> Eq. (4):
>
>     P(I < J) = d(J, R) / ( d(I, R) + d(J, R) )                       (4)

with d the Euclidean distance between endpoint pairs, equations (5) and (6).

**the exclusion: the reference interval R is built from the four endpoints of *both*
intervals**, so I's score depends on J. an 𝔄_m order assigns φ̄(I) from I alone.
that is the same structural exclusion as [7]'s, arrived at differently: [7]'s score
depends on the population, [13]'s on the comparison partner. and, as with [7], the
score is a ratio of Euclidean distances — not linear — and definition 4's rule
P ⩾ ½ is a thresholded probability, intransitive in general.

**[13]'s second-level ranking is not a dominance relation at all** and is recorded
separately: equations (9) and (10), printed page 5, and the convergence indicator
CI at equation (11), printed page 6. it re-ranks the last front by the bi-objective
problem min (CI(x), CV(x)) with CI the interval distance to a **population-derived**
ideal individual γ. population-dependent again.

### 4.3 what [13] confirms that part 1 measured, and it was not looked for

**claim 4.2. the direct-interval literature states the selection-pressure loss that
docs/part1/part1_closing.md section 4.3 measured, and states it as a motivation for
its own design.**

verdict: **confirmed**, in two of the three papers.

[13], printed page 5, section 3.1, transcribed:

> In addition, as the number of objectives to be considered in ICMOPs increases,
> **relying solely on the interval dominance sorting method as the single ranking
> criterion may lead to insufficient selection pressure and poor search
> efficiency.** To address this issue and better distinguish non-dominated
> individuals in a higher dimensional objective search space, a novel two-level
> balanced dominance sorting scheme is adopted, providing a stronger driving force
> to guide the population to converge rapidly.

[8], printed page 1, right column, transcribed:

> With respect to the IMaOPs, each uncertain objective is characterized by two
> parameters: an upper bound value and a lower bound value. An interval individual
> is dominant only if both the upper and lower bounds are smaller than other
> individuals; hence, as the number [of objectives increases …]

and printed page 5, immediately after definition 2:

> However, the satisfaction condition of IP-dominance is slack, that is, **even if
> the objective does not rise to a high dimension, the number of non-dominated
> solutions will greatly increase, which brings difficulties to environment
> selection**; thus, individual uncertainty is considered in this paper.

**this is the same phenomenon docs/part1/part1_closing.md section 4.3 measures as
the loss of selection pressure under the 2m transformation, reported by the papers
that raise the objection, about their own direct methods.** [8] says explicitly
that the count of non-dominated solutions blows up **"even if the objective does
not rise to a high dimension"** and that its own IP-dominance suffers from it — and
IP-dominance's per-objective relation is φ_lu, section 4.2.

**what this licenses and what it does not.** it licenses one sentence in the
memoria: the saturation the project measured is not an artefact of the
transformation, because the direct-interval literature reports the same
difficulty and treats it as the motivation for adding a second criterion.
**it does not license a claim that the two are the same quantity**: the project
measured a rank-1 saturation fraction under a specific transformation at a
specific population size, and [8] and [13] make a qualitative statement with no
number. the memoria must state it as a convergent observation and not as a
corroborating measurement.

### 4.4 [13]'s own comparison uses a midpoint-width weighting the criterion excludes

recorded because it is directly usable and was not looked for.

[13], printed page 9, section 4.2, on the peer algorithm IMOEA-DS:

> Furthermore, for the solution method IMOEA-DS with the conversion idea, the
> interval-valued objective is transformed into deterministic ones by **linear
> weighting of its midpoint and width**. Different weight values indicate different
> emphasis on the converted optimization problem. Set the weight of midpoints to α,
> and the weight of widths to β. In the light of this information we set the weight
> with three cases: IMOEA-DS-1 (α=0.3, β=0.7), IMOEA-DS-2 (α=0.5, β=0.5), and
> IMOEA-DS-3 (α=0.7, β=0.3).

**every one of those three is a non-negative combination of centre and half-width,
and docs/plan_after_meeting.md section c1 says exactly what that means**: in centre
and half-width coordinates any φ whose four coefficients are non-negative is a
refinement of example 2.4 and carries no new information about the order. so
IMOEA-DS-1, -2 and -3 are, in the framework's terms, three points in the positive
orthant, each of whose non-dominated sets is nested inside φ_cw's. **the paper runs
them as three distinct competitors and reports three distinct result columns**,
Table 3 onward.

**this is not a criticism of [13] and the memoria must not present it as one** —
[13] is comparing solvers, not orders, and the three weightings are its
reproduction of a peer method's parameter settings. it is recorded because it is a
concrete, published instance of the construction the containment criterion is for,
and because it shows the criterion has something to say about the comparison
literature and not only about the project's own candidate orders.


## 5. the three papers not read for content

### 5.1 [12] is a duplicate of [7]. confirmed.

CONTEXT.md section 3 records "papers/12-*.pdf is the same paper as [7], same title,
journal, volume and article number". **confirmed, and by a stronger test than
metadata.**

    same title, authors, journal, volume, year and article number: "An adaptive
        interval many-objective evolutionary algorithm with information entropy
        dominance", Cui, Qu, Zhang, Jin, Cai, Zhang and Chen, Swarm and
        Evolutionary Computation 91 (2024) 101749. `papers/12-*.pdf` has a
        truncated filename, ending at "with", and is otherwise the same document.
    same extracted text. `pdftotext -layout` gives 1246 lines from each and the
        two are **identical after whitespace is removed**.
    different files on disk. the md5 sums differ — 48cccf92… for
        `papers/7-*.pdf` and 033b9319… for `papers/12-*.pdf` — so they are two
        downloads of one article and not two copies of one file.

**it is one source and the project has always had it once.** nothing in
docs/part1/ or docs/plan_after_meeting.md treats [12] as a second source, so no
document needs correcting; the row is closed by confirmation.

### 5.2 [14] and [15], recorded and deliberately not read

`papers/14-A Multi-Period Optimization Framework for Portfolio Selection Using
Interval Analysis.pdf` and `papers/15-PORTFOLIO OPTIMIZATION USING INTERVAL
ANALYSIS.pdf`.

CONTEXT.md section 3 records them as Serban 2025 and Serban, Costea and Ferrara,
portfolio selection under interval analysis, and says "the portfolio application is
future work, section 2, and these are what the memoria's future-work section cites
so that it names a study rather than gestures at one. nothing in the project's
results depends on them."

**that record is correct and this session did not open either file.** they are the
citation for one paragraph of the memoria's future-work section, they are not
sources for part 2, and the meeting of 2026-09-04 moved the portfolio out of scope.
**recorded, and moved on.**

one connection worth a line, from [16] and not from them. [16]'s section 6, printed
page 26, applies its algorithm to a two-asset portfolio problem with
d_1 = [2,3], d_2 = [4,6], σ_11 = [1,2], σ_12 = [−1,0], σ_22 = [2,3], reducing under
x_1 + x_2 = 1 to the one-variable problem (28), min ([3x_1−6, 2x_1−4],
[5x_1²−6x_1+2, 5x_1²−6x_1+3]) on x_1 ∈ [0,1], with five solutions in Table 4. **it
is a one-variable, two-objective interval-native portfolio problem with a published
solution table**, and if the memoria's future-work paragraph wants an example
rather than a citation, that is the cheapest one in the corpus. **not scheduled and
not recommended for part 2**; recorded for the future-work paragraph only.


## 6. ambiguities, reported and not resolved

**a-1. [16] is a preprint with no venue.** arXiv:2603.06000v1, 6 March 2026. no
journal, volume or doi appears anywhere in the 33 pages. **the memoria must cite it
as a preprint unless a published version is found.** not resolved: this session did
not search for one.

**a-2. [16]'s Table 3 row for I-TR1 is not computed from 100 initial points, and
every other row is.** printed page 22 states the protocol: "Taking 100 randomly
chosen initial points, we compute Min, Max, Mean, Median, Mode, and Std. Dev." the
I-TR1 iteration row on printed page 23 is (10, 15, 12.3333, 12.0000, 10, 2.5166).
**12.3333 × 3 = 37 exactly, and the three values {10, 12, 15} reproduce the min,
max, mean and median as printed and give sample standard deviation 2.5166, matching
to all four printed digits.** so the row is computed from three runs. **not
resolved**: this session does not know whether the protocol or the row is wrong, and
it does not matter to part 2, since the project does not use Table 3. recorded
because a reader who cites Table 3 should know.

**a-3. appendix A's attribution is ambiguous.** "we provide a set of test problems
for MIOPs refer to [27]", printed page 27. "refer to" could mean "taken from [27]"
or "see also [27]". **the memoria's citation depends on which**, and this session
does not resolve it. the safe form is to cite [16] for the statements the project
read and [27] for the problems' origin, naming both.

**a-4. [16]'s argument that x⋆ is Pareto optimal for I-BK1 is invalid as printed.**
printed pages 21-22, transcribed in section 1.6. mutual non-domination with eleven
particular points does not establish Pareto optimality. **proposition 2.1, printed
page 7, independently supplies the conclusion** and its hypothesis holds for I-BK1,
so the checkpoint stands. **not resolved**: this session does not know whether the
authors intended proposition 2.1 and wrote the wrong justification. the memoria must
not repeat the printed argument.

**a-5. problem 5 (I-KW2)'s two objectives are not mirror images and the printed
asymmetry may be a typographical error.** printed page 28. G_1's first term is
(1−x_1)² exp(−x_1² − (x_2+1)²) and its third is exp(−(x_1+2)² − x_2²). G_2's first
term is (1+x_2)² ⊙ exp(−x_2² − (1−x_2)²), whose **exponent involves only x_2**, and
its third is exp(−(2−x_2)² − x_1²). the shape of the problem — a mirrored pair built
from the standard two-variable "peaks" function — suggests G_2's first term should
carry (1−x_1)² or (1−x_1) in the exponent. **not resolved. the paper wins and it is
transcribed as printed.** the problem fails criterion 2 either way, so the ambiguity
does not affect any verdict in section 1.9.

**a-6. problem 9 (I-Deb)'s 1/x_1 factor has an ambiguous scope in the extraction.**
printed page 29. the extracted text reads "G_2(x_1,x_2) := (1/x_1) ⊙ [2,2] ⊖gH
[1,3] ⊙ exp(…) ⊖gH [0.8,1.5] ⊙ exp(…)", which is consistent with 1/x_1 multiplying
the whole bracket or only [2,2]. the paper prints a large bracket that the
extraction flattens. **the standard Deb two-objective problem has the factor outside
the whole bracket** and section 1.8 transcribes it that way with this note attached.
**not resolved** — the reading is inferred from the standard form and not from the
extracted text. the problem fails criterion 2 under either reading.

**a-7. problem 17 (I-VFM2)'s G_3 has an ambiguous bracketing, and ⊖gH does not
associate.** printed page 30, printed as "[0.1,0.2] ⊙ x_1² ⊖gH [0.1,0.3] ⊙ x_2² ⊕
[0.1,0.2] ⊙ x_3²". [10] notes on printed page 3 that gH-addition is commutative but
not associative, and the same holds for mixing ⊖gH with ⊕. the two readings give
half-widths |0.05x_1² − 0.1x_2²| + 0.05x_3² and |0.05x_1² − 0.1x_2² − 0.05x_3²|,
which are different functions. **not resolved.** section 1.9's criterion-2 verdict
for I-VFM2 is a failure under both readings and does not depend on it.

**a-8. [9]'s definition 3.4 paragraph names the wrong relation once.** printed page
222: "The order relation ⩽*_cw represents the decision maker's preference for the
alternative with the lower expected cost and less uncertainty, that is: **if
A ⩽_cw B, then A is preferred to B.**" the sentence is about ⩽*_cw and the symbol
printed in the final clause is ⩽_cw, which definition 3.2 gives a different meaning
two pages earlier and which the paper itself warns about in the sentence
immediately preceding. **the extraction reproduces the paper's own inconsistency;
this session does not resolve it** and reads it as ⩽*_cw from context. nothing in
section 2.3 depends on the reading.

**a-9. [1]'s own reference [9] was not resolved and this session did not open [1].**
docs/part1/a0_framework.md section a-7 records that [1]'s equation (3) decomposes
its order into relations "≦_{φ_i}, ≤_{φ_i}, <_{φ_i} on C given in [9]", where [9]
is **[1]'s own internal reference number** and the extracted text of [1] carried no
bibliography. **whether [1]'s [9] is Ishibuchi and Tanaka 1990 — the project's [9],
read in section 2 above — is still p-01 and is still open.** the pdf of [1] is on
disk and carries its reference list, so it is answerable in one look, but the
session's reading list did not include re-opening [1] and this document does not
guess. **section 2.3's containment computations do not depend on it**: they rest on
docs/part1/a0_framework.md section c6's verification that example 2.2 of [1] is
λ = (1,0), β = (0,1), which was read from [1] itself.

**a-10. [1]'s per-component strict relation ≤_{φ_i} was not transcribed and section
1.3's claim 1.4 uses it.** claim 1.4 places [16] definition 2.16 strictly between
[1] definition 3.1(2) and 3.1(3). the placement uses [1] equations (6) and (7) as
docs/part1/a0_framework.md section c4 transcribes them, which give the aggregation
across objectives but state the per-component ≤_{φ_i} only by name, referring it to
[1]'s [9]. **the inclusion chain in claim 1.4 is correct under the natural reading
of ≤_{φ_i} — componentwise ⩽ with A ≠ B, which is what [9] definitions 3.1 and 3.4
give at equations (3.2) and (3.12) — and this session did not verify that [1] adopts
that reading.** it is a-9 in another form and closes with it.


## 7. what part 2 should be, on the evidence read

### 7.1 the three questions the session was asked, answered directly

**is clause c5 reachable?** **yes, and the obstacle is a measurement and not a
reading.** criterion 5 — the criterion that is the whole reason part 2 exists —
**passes on nineteen of twenty problems**, and the nineteen are interval-valued in
the construction docs/part1/a1_uncertainty_model.md records slide 19 offering
first: imprecision in the coefficients, ⊕_j [a_ij, b_ij] ⊙ h_ij(x), the paper's own
and attributed to Mondal and Ghosh 2025. **r-21's worry, that the gate might pass no
example of [16], is not what happened.** five problems pass every criterion a
reading can settle. what stands between them and clause c5 is criterion 3,
phi-separation, which cannot be answered by reading and is marked so for all
twenty. **c5 stays marked unsupported in every document until criterion 3 is
answered**, and section 7.2 says how it is answered.

**is a second calibration point available?** **yes, and on four problems rather than
one.** docs/plan_after_meeting.md section d3 makes the optional derivation session
conditional on "an example whose objectives are quadratic with constant hessians,
where the derivation is the same linear system as p1's". **I-BK1, I-IKK1, I-VFM1 and
I-MHHM2 are all that**, and I-BK1's is p1's shape term for term: diagonal quadratic
centres, diagonal quadratic half-widths, constant diagonal Hessians, all twelve
image coordinates convex. **the condition d3 set is met and the branch d3 warns
against — "if f1 passes only an example with exponentials, trigonometric terms or
gh-differences in it, the derivation is not attempted" — is not the branch we are
on.** the derivation is the same linear system as p1's.

**is the fallback of section d2 what part 2 becomes?** **no, and its text is still
owed.** d2's fallback is "part 2 becomes the reading result — what the twenty
problems are, why each does or does not serve, and what a study using them would
need". **sections 1.8, 1.9 and 6 of this document are that**, already written, and
they are owed to the memoria whatever else happens. **but they are a section of
part 2 and not the whole of it**, because the gate did not fail — it returned four
of four on five examples with one criterion out of reach of reading. **f2 and f3
run.** the loss d2 prices — the third clause removed from the claim, the answer to
[7]'s objection reverting to an argument — is not incurred.

### 7.2 the shape of the work, and one order the reading forces

not a list of subparts. the shape, in four movements, and the second is a decision
the reading forces on the plan.

**one. the derivation, on I-BK1.** closed-form φ-efficient sets for all three phi
by b1's route: image coordinates written out, phi-convexity by theorem 3.3 of [1],
regularity by **[10] proposition 32 then [10] theorem 34**, printed pages 12 and 13
— both now numbered and verified, section 3 — condition (15) of example 3.9 of [1]
for the candidate set, and example 3.8 statement 3 to lift weak optimality to
optimality. condition (15) decouples into two scalar equations because the Hessians
are constant and diagonal. **it is the b1 template with different numbers.**

**why I-BK1 and not one of the other four.** it is the only problem in appendix A
with published checkpoints: Table 1's point x⋆ = (3.914930, 1.428474) on printed
page 20, and equations (24) and (25)'s closed-form one-parameter curve with Table
2's eleven points on printed page 21, which this session verified by hand, section
1.6. **the project has never had an external check on any derivation.** p1's
correctness rests entirely on the project's own algebra, which is the standing
weakness d3 names. I-BK1 gives a published point to land on and a published curve
to sit beside. I-MHHM2 is cleaner as a statement of criterion 5 — six coefficient
intervals and nothing else — and has neither.

**two. criterion 3 is answered by the derivation, not before it. this reverses the
plan's order and the reversal should be recorded as a decision.**
docs/plan_after_meeting.md section d1 anticipates criterion 3 being answered by
"a1's diagnostic, run on the union bounding box of the three efficient sets", i.e.
by a sample, and treats it as a gate on the derivation. **on a problem whose
efficient sets are derivable, the derivation answers criterion 3 exactly rather than
by sample** — the three sets are compared in Lebesgue measure, which is what
`exact_regions_p1.csv` did for p1 and is strictly better evidence than any
diagnostic. **so the derivation comes first and the gate's last criterion is
answered as its output.** the cost of being wrong is one session: if the three phi
coincide on I-BK1 the derivation says so exactly, and that is itself a publishable
negative — a published interval-native problem on which the choice of order does not
matter — and it points at I-IKK1, which is not in the alignment regime, section
1.10.

**the risk this reversal accepts, stated so it is not discovered later.** section
1.10 records that on I-BK1, I-VFM1 and I-MHHM2 each objective's half-width is
minimised where its centre is, which is the alignment regime
docs/part1/a1_uncertainty_model.md part 4 records as the one where the orders
collapse. **I-BK1's half-width is not a multiple of its centre** — the ratio is 1/3
on the x_1 term and 1/2 on the x_2 term — so the collapse is not forced, but the
reading cannot say more than that.

**three. the second calibration point, which is the point of the whole exercise.**
with the closed forms, measure on I-BK1 exactly what part 1 measured on p1:
the pairwise overlap fractions in Lebesgue measure, the containments, and the
instrument's error factor when the project's solvers are run against the exact
answer. **that is what docs/part1/part1_closing.md section 7.3 says a second
calibration point would remove**, and it removes all three of the weaknesses named
there:

    the factor 1.81 is p1's alone and is carried nowhere. a second measured error
        factor says whether the bias is stable across problems or is a property of
        p1's geometry — the difference between a calibrated instrument and a
        calibrated measurement.
    the hausdorff distance is the statistic that travels best across the dimension
        change and is the one with no exact value, because `exact_regions_p1.csv`
        carries none. a second closed form decides whether to promote it.
    the geometry question. **I-BK1's half-width driver is aligned with its centre
        driver on both objectives**, which is p1's regime; a measurement there is a
        second point in the same regime and does **not** settle the geometry
        question. section 7.3's deciding measurement — p1's width design
        transplanted onto zdt1 — stays out of scope and stays in future work.

**four, optional and only if the schedule allows it. I-IKK1, for a different
weakness.** it is the one candidate not in the alignment regime: its half-widths
0.5x_2², 0.5(x_2−20)² and 0.5x_1² are minimised on lines and not at their centres'
minimisers. and it is a criterion-4 example on **three columns at once**, which
docs/part1/part1_closing.md section 3.4 makes a third registered test of the
protected-minimiser condition. **it answers the geometry question's neighbourhood
and the protected-minimiser prediction in one problem, and it passes criterion 2
cheaply.** it is the second recommendation and not the first because it has no
published checkpoint.

### 7.3 what it would let the paper claim that part 1 cannot

clause c5, in a form stronger than the one
docs/part1/part1_closing.md section 7.1 withholds.

part 1's recommended claim is conditional on the uncertainty model and is
calibrated on **one problem the project designed to make the three phi differ**,
which docs/part1/a1_uncertainty_model.md part 3 records as four designs rejected for
making them coincide. **that is the standing objection to p1 and no other work in
the plan removes it.** what the work above would let the paper say instead:

> on a problem published by a third party for a different purpose, with no
> uncertainty added by us, whose intervals are imprecision in the paper's own
> coefficients and whose solution the paper itself computes under one of the three
> orders, the three orders give [different / the same] efficient sets, and the
> difference is exact.

**the words in brackets are the measurement and this session does not fill them
in.** what the reading establishes is that the sentence is *writable* — that a
problem exists on which it can be said, that the derivation route closes on it, and
that the paper's own published points can be used to check the implementation before
the sentence is written. **that is what part 1 could not do at all.**

and a smaller thing the memoria gains either way: **[16] independently states the
condition under which the 2m transformation is valid** — that the boundary functions
do not interchange, section 1.7, printed page 27 — which is a published, checkable
condition on the project's own construction, from a paper that is not defending it.
the memoria can cite it in the methods section rather than arguing for the
construction unaided.

### 7.4 what it costs, in sessions

    **1 session. the derivation on I-BK1.** the b1 template, three phi, condition
        (15) decoupled into two scalar equations, plus a symbolic check. no run.
        this session also answers criterion 3 exactly, section 7.2 movement two,
        and therefore closes the gate.
    **1 session. the reference set and the exact statistics.** b2's encoding of the
        closed form as a reference set, the reference-front machinery for a new
        problem, and the exact overlap and containment numbers. this is where the
        published checkpoints of section 1.6 are used, and it is the session that
        produces the second calibration point.
    **1 session, and this is the one that can be cut. the run.** the project's
        solvers under the three phi on I-BK1, giving the second measured
        instrument-error factor. **it is the only one of the three that needs
        compute**, and cutting it leaves the calibration point intact and loses only
        the answer to the first of section 7.3's three weaknesses.

**three sessions, of which two are paper-and-pencil and one is the only one that
runs anything.** docs/plan_after_meeting.md section d3 priced the optional
derivation at "two sessions beyond f2 and f3"; the reading finds that the derivation
**is** most of f2 and f3 rather than an addition to them, because criterion 3 is
answered by the derivation and not by a separate diagnostic run. **so the estimate
is three sessions total for part 2's substantive arm, not five.**

    optional, and only if the schedule allows it, +2 sessions:
        I-IKK1's derivation and its statistics, for the protected-minimiser
        condition on three columns and for the one candidate outside the alignment
        regime.

    already written and costing nothing further:
        sections 1.8, 1.9 and 6 of this document are d2's fallback text. they go
        into the memoria whatever else happens.


## 8. what this session closes, and what it does not

**closed.**

    **p-02.** [9] states the centre-width comparison in example 2.4's coefficients:
        definition 3.4, equations (3.11) and (3.12), printed page 222, with a_w the
        half-width by equation (2.4) on printed page 220, by equation (4.6) on
        printed page 222, and numerically by equations (5.10) and (5.11) on printed
        page 224. definitions 3.1, 3.2, 3.3 and equations (4.1) and (4.2) are
        recorded in section 2.2, together with a sixth relation at equations (4.15)
        and (4.16) that the row did not anticipate. **printed page numbers recorded
        throughout, which is what the row was waiting for.**
    **p-05, both halves.** the regularity criterion is **theorem 34 of [10], printed
        page 13**, verbatim as b1 quoted it, with **proposition 32, printed page
        12**, supplying the sufficient condition b1 actually used and widening it to
        radii with zeros. the gH-difference has **no numbered definition in [10]**;
        it is an unnumbered display in section 2, printed page 3, and the numbered
        alternative available in the corpus is [16] definition 2.1, printed page 4.
        **the one unverified number in b1's derivation is verified.**
    **[12] is a duplicate of [7].** confirmed by identical extracted text and
        distinct md5 sums: two downloads of one article.
    **[14] and [15] are recorded as the memoria's future-work citation and were not
        read**, per the session's constraint and CONTEXT.md section 3.
    **f1's reading gate has run.** every problem of appendix A is transcribed with
        its n, m, 2m column count, box, objectives and criterion verdicts.

**not closed, and each is stated as owed rather than answered.**

    **criterion 3, for all twenty problems.** not determinable by reading, by
        design. **not determinable is not a pass and no example passes the gate.**
        section 7.2 says how it is answered and by what.
    **clause c5 stays marked unsupported.** it becomes supportable when criterion 3
        is answered on one of the five candidates and not before. **it must not
        appear in any document written before then**, which is
        docs/part1/part1_closing.md section 7.1's instruction and this session does
        not relax it.
    **p-01.** whether [1]'s own internal reference [9] is Ishibuchi and Tanaka 1990
        was not opened, ambiguity a-9. [1]'s pdf carries its reference list and this
        is one look; it was outside this session's reading list. **section 2.3's
        containment computations do not depend on it.**
    **p-06.** untouched. no paper read here bears on whether [1] identifies its
        "strict minimum" with one of definition 3.1's three named concepts.
    **s-11.** untouched in its own terms. **section 2.4's proposition 4.2 is a
        second independent check of the containment criterion and is not an answer
        to s-11**, which asks about the containments between φ_lu, φ_ls and φ_cw
        themselves. the distinction is stated in section 2.4 so it is not lost.
    **p-04.** partly served and not closed. section 4.2 records that [8]'s
        per-objective relation is φ_lu and that [7]'s and [13]'s are
        population- and partner-dependent respectively, but the row asks whether any
        construction in [7] or [8] drives the interval **width from the decision
        vector** rather than by a constant band, and that is a question about their
        benchmark suites, which this session did not read. e3 owns it.

**the four prohibitions of docs/part1/part1_closing.md section 8, checked against
this document.**

*no phi is ranked.* no sentence here says one of the three orders is better.
section 2.3 computes containments, which are statements about set inclusion.
section 1.4 records that [16]'s own relation is φ_lu, which is a statement about
what [16] does. section 7.2 recommends one **problem** and no order, and section
7.2 movement one runs all three phi.

*nothing is claimed from the containment.* section 2.3 uses the criterion to
classify two relations of [9] as checks and one as a finding, and adds none of them
to the registry. section 2.4 states explicitly that proposition 4.2 is a check on
the criterion and not an answer to s-11.

*no slice fraction is quoted as a quantity.* no fraction appears in this document at
all. section 7.3's claim leaves its comparative in brackets precisely because the
number does not exist yet.

*no benchmark number is interpreted without the instrument's error beside it.* the
only measured numbers here are [16]'s own, in Table 1 and Table 2, and they are
recorded as published checkpoints and not interpreted. section 7.2 movement three
makes the instrument's error on a second problem the thing to be measured, which is
the reason it is scheduled.

**one prohibition of this session's own, checked.** *the newton method is not
planned.* section 1.5 records it in one paragraph, marks it out of scope, and
section 7 contains no step that implements, derives from, or depends on it.
