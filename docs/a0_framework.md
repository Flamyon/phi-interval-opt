# a0: verification pass over [1]

subpart a0 of the phase plan in CONTEXT.md section 8. document, no code.

source read: `papers/new_preference_order_relationships_paper.txt`, the extracted
text of

    [1] T.M. Costa, R. Osuna-Gomez, Y. Chalco-Cano, "New preference order
        relationships and their application to multiobjective interval and fuzzy
        interval optimization problems", Fuzzy Sets and Systems 477 (2024) 108812.

`literature/φ-Automorphism Framework.md` was not consulted, per the session
constraint. no other source was used.

verified on 2026-08-31.


## how to read the locations

every location gives two things:

    the paper's own address: section, definition, theorem, example or equation
    number, and the printed journal page.
    the line range in `papers/new_preference_order_relationships_paper.txt`, so
    the claim can be re-checked without re-deriving where it lives.

printed pages were recovered from the page footers in the extracted text. the
mapping used throughout:

    page 2   lines   47-136        page 7   lines 412-491
    page 3   lines  137-205        page 8   lines 492-574
    page 4   lines  206-275        page 9   lines 575-650
    page 5   lines  276-338        page 10  lines 651-741
    page 6   lines  339-411        page 11  lines 742-825

the pages a0-b needed, continuing the same mapping:

    page 12  lines  826-914        page 18  lines 1334-1413
    page 14  lines  994-1062       page 19  lines 1414-1505
    page 16  lines 1153-1230       page 20  lines 1506-1573
                                   page 22  lines 1661-1685

page 22 has no footer in the extracted text, which ends at line 1685 in the
middle of appendix A. it is page 22 by continuation from the page 21 footer at
line 1660.

a0 cited the conclusion's inclusion-order passage as printed page 19. that was
wrong: the page 19 footer is at line 1505 and the passage begins at line 1509,
so it is on page 20. corrected above and in PROGRESS.md v-23. the line numbers
a0 gave were correct and no other citation in this document is affected, since
every other one is at line 771 or below.

sections 2 and 3, the whole of the interval branch in scope, occupy lines 99 to
771, printed pages 2 to 11.


## notation, and two glyphs the extraction lost

the pdf-to-text extraction drops two symbols wherever they occur, leaving only
their subscript. they are named here so the transcriptions below are readable,
and the loss is reported again under "ambiguities and text corruption".

    the symbol for the class of automorphisms. the text renders "φ ∈ 𝔄_m" as
    "𝜑 ∈ 𝑚" and "𝔄_4" as "4". this document writes `A_m`, and CONTEXT.md writes
    𝔄_m. neither the letter nor its typeface is recoverable from the text.

    the symbol for the second row vector of the automorphism, the one carrying
    the beta coefficients. the text renders "B_i^T f" as "𝑇𝑖 𝑓" and "B_1 = (β_1,
    β_2, 0, …, 0)" as "1 = (𝛽1 , 𝛽2 , 0, … , 0, 0)". this document writes `B_i`,
    matching CONTEXT.md. the letter is not recoverable; the vector's contents are
    fully recoverable and are verified below.

both losses are cosmetic for the project's purposes. neither affects any
coefficient, any hypothesis or any conclusion.


## c1. componentwise action, each component a 2x2 linear map in lambda and beta

    claim in CONTEXT.md section 4: the class of admissible automorphisms acts
    componentwise on endpoint pairs, with each component a 2x2 linear map given by
    coefficients lambda and beta.

verdict: **confirmed**.

location: section 2, the unnumbered paragraph introducing the class, printed
page 3, lines 163-172. the two displays are unnumbered; the numbered equations
(1), (2), (3) sit around them.

transcription, lines 163-172:

> In this sense, `A_m` is used to denote the particular class of automorphisms
> φ_1 × φ_2 × … × φ_m : ℝ^2m → ℝ^2m such that
>
>     (φ_1 × φ_2 × … × φ_m)(x_1, x_2, x_3, x_4, …, x_2m−1, x_2m)
>         = (φ_1(x_1, x_2), φ_2(x_3, x_4), …, φ_m(x_2m−1, x_2m)),
>
> where φ_i : ℝ^2 → ℝ^2 are automorphisms given by
>
>     φ_i(x_2i−1, x_2i) = (λ_2i−1 x_2i−1 + λ_2i x_2i, β_2i−1 x_2i−1 + β_2i x_2i)
>
> for all (x_2i−1, x_2i) ∈ ℝ^2 and for all i ∈ {1, 2, …, m}

the componentwise action is exactly as CONTEXT.md states, on the pair
(x_2i−1, x_2i), which is the endpoint pair of the i-th interval once φ is
composed with F, see c5.


## c2. admissibility is exactly a nonzero determinant

    claim in CONTEXT.md section 4: the admissibility condition is exactly
    lambda_{2i-1}*beta_{2i} != lambda_{2i}*beta_{2i-1}, and nothing further.

verdict: **confirmed**.

location: section 2, same paragraph, printed page 3, lines 171-172. restated in
section 3, printed page 6, lines 398-399.

transcription, lines 171-172, continuing the display above:

> using real numbers (that can be chosen according to a decision) λ_2i−1, λ_2i,
> β_2i−1, β_2i ∈ ℝ with λ_2i−1 β_2i ≠ λ_2i β_2i−1.

restatement, lines 398-399:

> The optimal solution concept for each one of these problems depends on the
> φ ∈ `A_m` that is defined through the values λ_2i−1, λ_2i, β_2i−1, β_2i ∈ ℝ
> with λ_2i−1 β_2i ≠ λ_2i β_2i−1 for all i ∈ {1, …, m}.

"and nothing further" was checked by reading sections 2 and 3 in full. no further
restriction on the coefficients appears anywhere in lines 99-771. the paper calls
φ_i an automorphism of ℝ^2 and the determinant condition is precisely what makes
the stated linear map one; no normalisation, sign or orientation condition is
imposed.


## c3. the coefficients are chosen by a decision maker and carry the semantics

    claim in CONTEXT.md section 4: the paper states that those coefficients may be
    chosen by a decision maker, and that the semantics of the problem are carried
    by them.

verdict: **confirmed**, in two separate places.

location one: section 2, printed page 3, line 171, the parenthetical inside the
sentence quoted under c2: "using real numbers (that can be chosen according to a
decision)".

location two: section 3, printed page 6, lines 397-401, the paragraph
immediately after the implication chain of definition 3.1 and 3.2. this is the
stronger statement and the one CONTEXT.md is paraphrasing.

transcription, lines 397-401:

> Behind each of the problems (1MIOP_φ) and (2MIOP_φ) there exists a semantic
> that is expressed by means of its optimal solution concepts. The optimal
> solution concept for each one of these problems depends on the φ ∈ `A_m` that
> is defined through the values λ_2i−1, λ_2i, β_2i−1, β_2i ∈ ℝ with
> λ_2i−1 β_2i ≠ λ_2i β_2i−1 for all i ∈ {1, …, m}. Consequently, the optimal
> solution concepts for these problems depend on the values λ_2i−1, λ_2i, β_2i−1,
> β_2i ∈ ℝ. Therefore, the semantics related to (1MIOP_φ) and (2MIOP_φ) are
> implicitly expressed by the values λ_2i−1, λ_2i, β_2i−1, β_2i ∈ ℝ which can be
> chosen by a decision maker.

see also section 2, printed page 4, lines 264-267, which says the same of the
order relations themselves: "Semantically, these preference order relations can
be related to the decision maker's preferences".

this is a statement about who chooses. it is not a ranking of φ. see however the
finding recorded at the end of c9, which concerns a comparative statement the
paper makes in its conclusion, outside the scope of c1 to c15.


## c4. the order is componentwise on R^2m and decomposes objective by objective

    claim in CONTEXT.md section 4: the order relation is componentwise on R^(2m)
    and decomposes objective by objective, so phi applies independently to each
    interval objective.

verdict: **confirmed**, with one scoping refinement that CONTEXT.md already
states correctly and which is recorded here so it is not lost.

location: definition 2.1, printed page 2, lines 123-134; equation (2), printed
page 3, lines 175-176; equation (3), printed page 3, lines 179-184.

definition 2.1, transcribed, lines 123-134:

> **Definition 2.1.** Let φ : ℝ^2m → ℝ^2m be a bijection and let ⩽_{ℝ^2m} be an
> order relation on ℝ^2m. The φ, ⩽_{ℝ^2m}-preference order relation ≦^2m_φ on
> (C)^m is defined by
>
>     A ≦^2m_φ B ⇔ φ̄(A) ⩽_{ℝ^2m} φ̄(B),                                  (1)
>
> where A = ([a_1, ā_1], …, [a_m, ā_m]), B = ([b_1, b̄_1], …, [b_m, b̄_m]) ∈ (C)^m
> and φ̄ : (C)^m → ℝ^2m is the injective function given by
>
>     φ̄([a_1, ā_1], …, [a_m, ā_m]) = φ(a_1, ā_1, …, a_m, ā_m).

the refinement: in definition 2.1 the order ⩽_{ℝ^2m} is an arbitrary order
relation on ℝ^2m and φ an arbitrary bijection. componentwise-ness is not part of
definition 2.1. it arrives when the paper specialises to the class `A_m` and
fixes ⩽_{ℝ^2m} to be ≦^2m, at lines 172-176. CONTEXT.md states this correctly
("for the class 𝔄_m the order on R^(2m) is componentwise"); it is recorded here
because a later reader could easily attribute componentwise-ness to definition
2.1 itself.

equation (2), lines 175-176:

>     (x_1, x_2, …, x_2m−1, x_2m) ≦^2m (y_1, y_2, …, y_2m−1, y_2m)
>         ⇔ (x_2i−1, x_2i) ≦ (y_2i−1, y_2i)                                  (2)
>
> for all i ∈ {1, 2, …, m}, where (x_2i−1, x_2i) ≦ (y_2i−1, y_2i) if and only if
> x_2i−1 ⩽ y_2i−1 and x_2i ⩽ y_2i for all i ∈ {1, 2, …, m}.

equation (3), the decomposition, lines 179-184:

>     (A_1, …, A_m) ≦_φ (B_1, …, B_m) ⇔ φ̄(A_1, …, A_m) ≦^2m φ̄(B_1, …, B_m)
>                                     ⇔ φ̄_i(A_i) ≦ φ̄_i(B_i)  ∀ i ∈ {1, …, m}
>                                     ⇔ A_i ≦_{φ_i} B_i       ∀ i ∈ {1, …, m}  (3)
>
> for all (A_1, …, A_m), (B_1, …, B_m) ∈ (C)^m, where ≦_{φ_i} is a preference
> order relation on C given in [9] for all i ∈ {1, …, m}.

one notational point: the paper writes φ̄_i(A_i), the induced map on intervals,
where CONTEXT.md writes phi_i(A_i). the paper defines φ̄_i([a, ā]) = φ_i(a, ā) at
printed page 5, line 311. the two are the same object under that identification;
nothing turns on it.

the strict versions are equation (6), printed page 3, lines 203-223, and equation
(7), lines 227-229. equation (6) is the one that matters for definition 3.1(2):

>     (A_1, …, A_m) ≤_φ (B_1, …, B_m)
>         ⇔ A_i ≦_{φ_i} B_i for all i ∈ {1, …, m}
>           and ∃ k ∈ {1, …, m} such that A_k ≤_{φ_k} B_k                     (6)

equation (7):

>     (A_1, …, A_m) <_φ (B_1, …, B_m) ⇔ A_i <_{φ_i} B_i  ∀ i ∈ {1, …, m}       (7)

≦_φ is a partial order on (C)^m: proposition 2.1, printed page 3, lines 144-145,
for the general definition 2.1 case, and proposition 2.2, printed page 3, lines
187-191, for the class `A_m`.


## c5. m interval objectives become 2m real objectives

    claim in CONTEXT.md section 4: the transformed problem has 2m real objectives
    for m interval objectives.

verdict: **confirmed**.

location: section 3, printed page 8, lines 508-537. equation (12) at line 511,
the composition display at lines 517-532, equation (13) at line 537.

equation (12), lines 511-512, the target form:

>     min (h_1(x), h_2(x), …, h_2m(x))                                       (12)
>     x∈S
>
> where S ⊆ ℝ^n and h_1, h_2, …, h_2m : S → ℝ.

the composition, lines 517-532:

> The composition φ̄∘F : S → ℝ^2m defined by
>
>     (φ̄∘F)(x) = φ̄(F(x)) = φ̄(F_1(x), …, F_m(x))
>              = φ̄([f_1(x), f̄_1(x)], …, [f_m(x), f̄_m(x)])
>              = (φ_1(f_1(x), f̄_1(x)), …, φ_m(f_m(x), f̄_m(x)))
>              = ((λ_1 f_1 + λ_2 f̄_1)(x), (β_1 f_1 + β_2 f̄_1)(x), …,
>                 (λ_2m−1 f_m + λ_2m f̄_m)(x), (β_2m−1 f_m + β_2m f̄_m)(x))
>              = (Λ_1^T f(x), B_1^T f(x), …, Λ_2m^T f(x), B_2m^T f(x)),
>
> where Λ_1 = (λ_1, λ_2, 0, …, 0, 0), Λ_2 = (0, 0, λ_3, λ_4, 0, …, 0),
> Λ_i = (0, 0, …, λ_2i−1, λ_2i, 0 …, 0), …, Λ_m = (0, 0, …, λ_2m−1, λ_2m),
> B_1 = (β_1, β_2, 0, …, 0, 0), B_2 = (0, 0, β_3, β_4, 0, …, 0),
> B_i = (0, 0, …, β_2i−1, β_2i, 0 …, 0), …, B_m = (0, 0, …, β_2m−1, β_2m) ∈ ℝ^2m
> and f(x) = (f_1(x), f̄_1(x), f_2(x), f̄_2(x), …, f_m(x), f̄_m(x)) for all x ∈ S

the final line of that display prints subscript 2m on the last Λ and B where the
definitions that follow it list only Λ_1 … Λ_m and B_1 … B_m. reported under
"ambiguities and text corruption"; it does not affect the count of 2m real
objectives, which is fixed by (12), by the codomain ℝ^2m, and by the 2m scalar
components listed in the two preceding lines of the same display.

equation (13), the transformed problem, line 537:

>     (MOP_φ)  min (φ̄∘F)(x).                                                (13)
>              x∈S

so zdt1 with m = 2 gives a 4-objective real problem and dtlz2 with m = 3 gives a
6-objective real problem, as CONTEXT.md section 5 step 3 states.


## c6. example 2.2 is lambda = (1, 0), beta = (0, 1), giving (f_l, f_u), LU

    claim in CONTEXT.md section 4: example 2.2 is lambda=(1,0), beta=(0,1), giving
    (f_l, f_u), and its convexity notion is LU-convexity.

verdict: **confirmed**, all three parts.

location: example 2.2, section 2, printed page 5, lines 332-336.

transcription:

> **Example 2.2.** For φ = (φ_1 × … × φ_m) ∈ `A_m` such that
>
>     φ_i(x_2i−1, x_2i) = (1 x_2i−1 + 0 x_2i, 0 x_2i−1 + 1 x_2i) = (x_2i−1, x_2i)
>
> for all i ∈ {1, …, m}, consider the preference order relation ≦_φ given by (3).
> Thus, the concept of φ-convexity at x* ∈ S for multi-interval-valued functions
> F : S ⊆ ℝ^n → (C)^m coincides with the concept of LU-convexity at x* given
> in [31].

so λ_2i−1 = 1, λ_2i = 0, β_2i−1 = 0, β_2i = 1. determinant 1·1 − 0·0 = 1 ≠ 0.
composed with F it gives (f_i, f̄_i), the identity on the endpoint pair. the
convexity notion is LU-convexity, attributed to the paper's reference [31], which
the extracted text does not let me resolve; see "ambiguities and text
corruption".


## c7. example 2.3 is lambda = (1, 0), beta = (-1, 1), giving the full width, LS

    claim in CONTEXT.md section 4: example 2.3 is lambda=(1,0), beta=(-1,1),
    giving (f_l, f_u - f_l), the FULL width, and its convexity notion is
    LS-convexity.

verdict: **confirmed**, all three parts, including that the second coordinate is
the full width and carries no factor of one half.

location: example 2.3, section 2, printed page 6, lines 342-346.

transcription:

> **Example 2.3.** For φ = (φ_1 × … × φ_m) ∈ `A_m` such that
>
>     φ_i(x_2i−1, x_2i) = (1 x_2i−1 + 0 x_2i, −1 x_2i−1 + 1 x_2i)
>                       = (x_2i−1, x_2i − x_2i−1)
>
> for all i ∈ {1, …, m}, consider the preference order relation ≦_φ given by (3).
> Thus, the concept of φ-convexity at x* ∈ S for multi-interval-valued functions
> F : S ⊆ ℝ^n → (C)^m coincides with the concept of LS-convexity at x* given
> in [26].

so λ_2i−1 = 1, λ_2i = 0, β_2i−1 = −1, β_2i = 1. determinant 1·1 − 0·(−1) = 1 ≠ 0.
composed with F it gives (f_i, f̄_i − f_i), lower bound and full width. the
convexity notion is LS-convexity, attributed to the paper's reference [26].


## c8. example 2.4 is lambda = (1/2, 1/2), beta = (-1/2, 1/2), centre and half-width, CW

    claim in CONTEXT.md section 4: example 2.4 is lambda=(1/2,1/2),
    beta=(-1/2,1/2), giving centre and HALF-width, and its convexity notion is
    CW-convexity.

verdict: **confirmed**, all three parts, including the factor of one half on the
second coordinate.

location: example 2.4, section 2, printed page 6, lines 348-353.

transcription:

> **Example 2.4.** For φ = (φ_1 × … × φ_m) ∈ `A_m` such that
>
>     φ_i(x_2i−1, x_2i) = ( (1/2) x_2i−1 + (1/2) x_2i, −(1/2) x_2i−1 + (1/2) x_2i )
>                       = ( (x_2i−1 + x_2i)/2, (x_2i − x_2i−1)/2 )
>
> for all i ∈ {1, …, m}, consider the preference order relation ≦_φ given by (3).
> Thus, the concept of φ-convexity at x* ∈ S for multi-interval-valued functions
> F : S ⊆ ℝ^n → (C)^m coincides with the concept of CW-convexity at x* given
> in [31].

so λ_2i−1 = 1/2, λ_2i = 1/2, β_2i−1 = −1/2, β_2i = 1/2. determinant
(1/2)(1/2) − (1/2)(−1/2) = 1/2 ≠ 0. composed with F it gives
((f_i + f̄_i)/2, (f̄_i − f_i)/2), centre and half-width. the convexity notion is
CW-convexity, attributed to the paper's reference [31].

the difference CONTEXT.md insists on is confirmed as real and as printed: the
second coordinate of example 2.3 is x_2i − x_2i−1 and the second coordinate of
example 2.4 is (x_2i − x_2i−1)/2. they differ by a factor of two.


## c9. whether a further named example of phi appears in sections 2 or 3

    claim in CONTEXT.md section 4 and the a0 specification in section 10: sections
    2 and 3 contain no further named example of phi.

verdict: **refuted**. one further named example exists, with explicit
coefficients. two further explicit automorphisms exist that are not named
examples, one inside section 3 and one in the conclusion.

this was checked exhaustively, not by skimming: every line of the extracted text
between line 99 and line 771 that contains a φ with an argument list and an
equals sign was enumerated and read. the complete list of explicit automorphisms
in sections 2 and 3 is: the general form at line 170, example 2.1 at lines
246-252, example 2.2 at line 334, example 2.3 at line 344, example 2.4 at line
350, and −φ at line 590. examples 3.1 to 3.7 introduce no φ of their own; each
names one of examples 2.2, 2.3 or 2.4, tabulated at the end of this section.

### the further named example: example 2.1

location: example 2.1, section 2, printed page 4, lines 234-262. it is the
car-purchase illustration of the introductory discussion at lines 148-161. it is
a φ = φ_1 × φ_2 × φ_3 × φ_4 ∈ `A_4`, that is m = 4, and every coefficient is
given explicitly.

transcription of the coefficients, lines 245-252:

> As criteria of comparison one can use the greatest possible purchase price and
> the average of the possible purchase prices for the first interval component,
> the variation of the possible fuel economy and the maximum of the possible fuel
> economy for the second interval component, the greatest possible sale price and
> the average of the possible sale prices for the third interval component, and
> the oldest and the newest year for the last interval component as follows:
>
>     φ_1(x_1, x_2) = (x_2, (x_1 + x_2)/2),  where λ_1 = 0, λ_2 = 1,
>                                                  β_1 = 1/2 = β_2;
>     φ_2(x_3, x_4) = (x_4 − x_3, −x_4),     where λ_3 = −1, λ_4 = 1,
>                                                  β_3 = 0, β_4 = −1;
>     φ_3(x_5, x_6) = ((x_6 − x_5)/2, −x_6), where λ_5 = −1/2, λ_6 = 1/2,
>                                                  β_5 = 0, β_6 = −1;
>     φ_4(x_7, x_8) = (−x_7, −x_8),          where λ_7 = −1, λ_8 = 0,
>                                                  β_7 = 0, β_8 = −1.

each component is admissible: determinants 0·(1/2) − 1·(1/2) = −1/2,
(−1)(−1) − 1·0 = 1, (−1/2)(−1) − (1/2)(0) = 1/2, (−1)(−1) − 0·0 = 1, all nonzero.

three things about example 2.1 that matter to this project:

    it is the only place in [1] where the components of a single φ carry
    different coefficients from one another. examples 2.2, 2.3 and 2.4 all use
    the same 2x2 map in every component. the class `A_m` permits per-objective
    coefficients and example 2.1 is the paper's demonstration of that.

    it is the only place in sections 2 and 3 where negative coefficients appear,
    and the paper's reason is semantic: components 3 and 4 are quantities the
    buyer wants large, embedded in a minimisation. this is how [1] handles mixed
    minimise-maximise objectives inside a single problem.

    it carries no convexity notion and no optimality condition. examples 2.2, 2.3
    and 2.4 each close with "coincides with the concept of ... convexity at x*
    given in [·]"; example 2.1 does not. it illustrates the order relation, not
    the convexity theory.

it is a named example of a φ, and CONTEXT.md section 4's sentence "they are the
named examples of [1]" is therefore not accurate as written. the correction is
listed under "disagreements with CONTEXT.md". example 2.1 is **not** proposed as
a fourth experiment φ; the session constraint forbids proposing a φ and the
project's committed experiment is unchanged.

### two further explicit automorphisms that are not named examples

first, −φ, defined inside the proof of theorem 3.2, section 3, printed page 9,
lines 588-592:

> Given −φ ∈ `A_m` by
>
>     −φ(a_1, …, a_2m) = ((−λ_1 a_1 − λ_2 a_2, −β_1 a_1 − β_2 a_2), …,
>                         (−λ_2m−1 a_2m−1 − λ_2m a_2m,
>                          −β_2m−1 a_2m−1 − β_2m a_2m)),

this is a construction from an arbitrary φ, used only to state the maximisation
case, not an example with fixed coefficients. it is what CONTEXT.md section 5
step 3 refers to as "theorem 3.2 gives the maximisation case through -phi".

second, and outside the scope of c9 but recorded because it is material: the
**conclusion**, section 6, printed page 20, lines 1513-1515, gives a further
explicit automorphism with fixed coefficients, unnumbered and not called an
example:

> On the other hand, it is well-known that the preference partial order relation
> ≦_{φ_2}, where φ_2 ∈ `A_1` is given by
> φ_2(x_1, x_2) = (λ_1 x_1 + λ_2 x_2, β_1 x_1 + β_2 x_2), with λ_1 = −1,
> λ_2 = 0 = β_1, and β_2 = 1, and which coincides with the inclusion order ⊆,
> provides a structure of quasilinear space for the interval space (see,
> e.g., [23]). Consequently, the use of ≦_{φ_2} would be a better option than the
> use of ≦_{φ_1} in a decision making.

that is φ(x_1, x_2) = (−x_1, x_2), giving (−f_l, f_u); determinant
(−1)(1) − 0·0 = −1 ≠ 0, so admissible. φ_1 in that passage is the automorphism of
example 2.2, named at line 1510.

this passage is a comparative statement about two φ, made by the paper, under an
explicit criterion: whether the interval space equipped with the induced order
satisfies the axioms of an ordered quasilinear interval space, specifically axiom
(q.11) of definition 2.1 in the paper's reference [23], with the counterexample
α = 1, β = −1, x = [−1, 1] given at lines 1512-1513. it is not a statement about
optimisation performance and it does not bear on part 1's measurement design.
it is recorded because CONTEXT.md section 2 characterises the paper's position as
"a statement about who chooses, not a ranking", and that characterisation is
accurate for the section 3 passage it cites but is not the whole of what [1]
says. no CONTEXT.md edit is made for this: it falls outside c1 to c15, and
whether section 2 should be amended is a question for the research chat, raised
in PROGRESS.md.

### which phi each example of section 3 uses

    example 3.1  printed page 6, line 406        example 2.2
    example 3.2  printed page 7, line 415        example 2.3
    example 3.3  printed page 7, line 420        example 2.4
    example 3.4  printed page 7, lines 430-431   example 2.2
    example 3.5  printed page 7, lines 448-449   example 2.4
    example 3.6  printed page 7, lines 464-465   example 2.4
    example 3.7  printed page 7, lines 486-487   example 2.3
    example 3.8  printed page 10, line 682       arbitrary φ
    example 3.9  printed page 10, line 709       arbitrary φ


## c10. definition 3.1, the three solution concepts and the implications

    claim in CONTEXT.md section 6: definition 3.1 gives what optimal, weakly
    optimal and strictly optimal mean for the phi-interval problem.

verdict: **confirmed**. transcribed in full below.

location: definition 3.1, section 3, printed page 6, lines 371-374. the
implication chain is unnumbered, printed page 6, line 394, and sits after
definition 3.2.

the problem it refers to, equation (10), printed page 6, lines 359-361:

>     (1MIOP_φ)  min F(x),                                                   (10)
>                x∈S

with F : S ⊆ ℝ^n → (C)^m, F(x) = (F_1(x), …, F_m(x)), F_i(x) = [f_i(x), f̄_i(x)],
and f_i, f̄_i : S → ℝ with f_i(x) ⩽ f̄_i(x) on S, lines 363-366. the
δ-neighborhood N(x, δ) := {y ∈ S : ‖y − x‖ < δ}, line 369.

transcription, lines 371-374. the paper uses a typographic convention: the bold
parenthetical gives the local version and the text after it gives the global
version. both are printed on one line.

> **Definition 3.1.** Let φ ∈ `A_m` be an automorphism. It is said that x̄ ∈ S is
> a:
>
> (1) (local) strong or strict optimal solution for (10) if there does not exist
>     (**x ∈ N(x̄, δ) ∩ S \ {x̄}**) x ∈ S \ {x̄} such that F(x) ≦_φ F(x̄).
>
> (2) (local) optimal solution for (10) if there does not exist
>     (**x ∈ N(x̄, δ) ∩ S \ {x̄}**) x ∈ S \ {x̄} such that F(x) ≤_φ F(x̄).
>
> (3) (local) weak optimal solution for (10) if there does not exist
>     (**x ∈ N(x̄, δ) ∩ S \ {x̄}**) x ∈ S \ {x̄} such that F(x) <_φ F(x̄).

the three relations ≦_φ, ≤_φ and <_φ are equations (3), (6) and (7), transcribed
under c4.

the implications, printed page 6, lines 391-394:

> The following relations are immediate:
>
>     strong or strict optimal solution ⇒ optimal solution ⇒ weak optimal solution

this display is placed after definition 3.2 and, from its wording and position,
covers both definition 3.1 (minimisation) and definition 3.2 (maximisation).

for completeness, definition 3.2, the maximisation counterpart, printed page 6,
lines 385-389, for problem (11) max_{x∈S} F(x):

> **Definition 3.2.** Let φ ∈ `A_m` be an automorphism. It is said that x̄ ∈ S is
> a:
>
> (1) (local) strong or strict optimal solution for (11) if there does not exist
>     (**x ∈ N(x̄, δ) ∩ S \ {x̄}**) x ∈ S \ {x̄} such that F(x̄) ≦_φ F(x).
>
> (2) (local) optimal solution for (11) if there does not exist
>     (**x ∈ N(x̄, δ) ∩ S \ {x̄}**) x ∈ S \ {x̄} such that F(x̄) ≤_φ F(x).
>
> (3) (local) weak optimal solution for (11) if there does not exist
>     (**x ∈ N(x̄, δ) ∩ S \ {x̄}**) x ∈ S \ {x̄} such that F(x̄) <_φ F(x).

CONTEXT.md section 6 calls the three concepts "optimal, weakly optimal and
strictly optimal". the paper's own names are "strong or strict optimal solution",
"optimal solution" and "weak optimal solution". the naming is compatible; the
paper's names are used in this document and should be used in b1.


## c11. theorem 3.1 and theorem 3.2

    claim in CONTEXT.md section 5 step 3 and section 6: theorem 3.1 states the
    equivalence between the phi-interval problem and min (phi-bar o F)(x).
    theorem 3.2 gives the maximisation case through -phi.

verdict: **confirmed**, both. transcribed in full below.

location: theorem 3.1, section 3, printed page 8, lines 545-546. theorem 3.2,
section 3, printed page 9, lines 584-586.

theorem 3.1, transcribed verbatim:

> **Theorem 3.1.** x̄ ∈ S is an optimal solution (weakly optimal solution) for
> 1MIOP_φ if and only if x̄ ∈ S is an efficient solution (weakly efficient
> solution) for (MOP_φ).

(MOP_φ) is equation (13), min_{x∈S} (φ̄∘F)(x), transcribed under c5. the theorem
covers the optimal and the weak optimal cases; it says nothing about the strong
or strict case of definition 3.1(1), and no separate result in section 3 does.

theorem 3.2, transcribed verbatim:

> **Theorem 3.2.** x̄ ∈ S is an optimal solution (weak optimal solution) for
> (2MIOP_φ) if and only if x̄ ∈ S is an efficient solution (weakly efficient
> solution) for (MOP_{(−φ)}).

(MOP_{(−φ)}) is defined inside the proof, printed page 9, lines 588-595, from the
−φ transcribed under c9:

>     (MOP_{(−φ)})  min (−Λ_1^T f(x), −B_1^T f(x), …, −Λ_m^T f(x), −B_m^T f(x)).
>                   x∈S

the hypotheses of both theorems are only the standing ones of section 3: φ ∈ `A_m`,
S ⊆ ℝ^n, F : S → (C)^m a multi-interval-valued function. no convexity, no
differentiability, no constraint qualification, no compactness. this is what
licenses running ordinary solvers on the transformed problem for any problem in
this project, per CONTEXT.md section 5 step 3.

the efficiency notions used on the right-hand side are defined immediately before
the theorem, printed page 8, lines 514-516:

> Recall that x̄ ∈ S is an efficient solution for (12) if there does not exist
> x ∈ S \ {x̄} such that h_i(x) ⩽ h_i(x̄) for all i ∈ {1, …, 2m}, and x̄ ∈ S is an
> weak efficient solution for (12) if there does not exist x ∈ S \ {x̄} such that
> h_i(x) < h_i(x̄) for all i ∈ {1, …, 2m}.

that printed definition of "efficient solution" does not match the usual one and
does not match definition 3.1(2). reported under "ambiguities and text
corruption"; it matters for b2's test design and is not resolved here.


## c12. theorem 3.3

    claim in CONTEXT.md section 6: theorem 3.3, phi-convexity of F holds exactly
    when the two image coordinates Lambda_i^T f and B_i^T f are convex, for
    every i.

verdict: **confirmed**. transcribed in full below.

location: theorem 3.3, section 3, printed page 9, lines 638-641.

transcription verbatim:

> **Theorem 3.3.** Let F : S ⊆ ℝ^n → (C)^m be a multi-interval-valued function
> given by F(x) = (F_1(x), …, F_m(x)), with F_i(x) = [f_i(x), f̄_i(x)] for all
> i ∈ {1, …, m} and let ≦_φ be the preference order relation given by (3). Then F
> is φ-convex if and only if Λ_i^T f and B_i^T f are convex for all i ∈ {1, …, m},
> where f = (f_1, f̄_1, …, f_i, f̄_i, …, f_m, f̄_m).

from the proof, printed page 9, lines 645-657, the two image coordinates written
out:

>     Λ_i^T f = λ_2i−1 f_i + λ_2i f̄_i
>     B_i^T f = β_2i−1 f_i + β_2i f̄_i

φ-convexity itself is definition 2.2, section 2, printed page 5, lines 283-290:

> **Definition 2.2.** Let ≦_φ be the preference order relation given by (3) and
> let F : S ⊆ ℝ^n → (C)^m be a multi-interval-valued function. F is said to be
> φ-convex if
>
>     F(tx + (1 − t)y) ≦_φ t ⊡ F(x) ⊞ (1 − t) ⊡ F(y)                          (8)
>
> for all x, y ∈ S and t ∈ (0, 1). If there exists x* ∈ S such that
>
>     F(t x* + (1 − t)y) ≦_φ t ⊡ F(x*) ⊞ (1 − t) ⊡ F(y)                       (9)
>
> for all y ∈ S and t ∈ (0, 1), then F is said to be φ-convex at x*

the pointwise counterpart of theorem 3.3, which b1 will need because examples
3.4 to 3.7 assume φ-convexity **at x̄** and not globally, is remark 2.2, section
2, printed page 5, lines 319-327:

> Consequently, given a multi-interval-valued function F : S ⊆ ℝ^n → (C)^m, such
> that F(x) = (F_1(x), …, F_m(x)), with F_i(x) = [f_i(x), f̄_i(x)], then from
> Proposition 2.3, Corollary 2.1 and from definition of the preference order
> given by (3), it follows that F is φ-convex at x* if and only if the
> real-valued functions [λ_2i−1 f_i + λ_2i f̄_i] and [β_2i−1 f_i + β_2i f̄_i] are
> convex at x* for all i ∈ {1, …, m}.

theorem 3.3 and remark 2.2 are the global and pointwise forms of the same
characterisation. CONTEXT.md section 6 and section 10 b1 cite theorem 3.3; remark
2.2 is the one that applies pointwise and is recorded here so b1 has it.

one gap in the printed hypotheses: theorem 3.3 does not restate φ ∈ `A_m`,
although its proof uses "the definition of the automorphisms φ_i ∈ `A`" at line
659 and the conclusion is stated in terms of Λ_i and B_i, which exist only for
that class. reported under "ambiguities and text corruption". it is not a defect
for this project, which only ever uses φ ∈ `A_m`.


## c13. example 3.8, scalarization

    claim in CONTEXT.md section 6: example 3.8, scalarization, four statements
    relating solutions of the weighted scalar problem to solutions of the
    phi-interval problem.

verdict: **confirmed**, four numbered statements. transcribed in full below,
with the exact weight conditions.

location: example 3.8, section 3.1, printed page 10, lines 682-706. equation (14)
at line 685.

transcription verbatim, lines 682-706:

> **Example 3.8** (Scalarization). Associated with (13), consider the weighted
> scalar problem (see [7])
>
>     (MOP_φ(w))  min  Σ_{i=1}^{m} ( w_2i−1 Λ_i^T f(x) + w_2i B_i^T f(x) ),   (14)
>                 x∈S
>
> where w = (w_1, …, w_2m) ∈ ℝ^2m, w_i ⩾ 0 for all i ∈ {1, …, 2m} and
> Σ_{i=1}^{2m} w_i = 1. The relationships between the solutions for (10) and the
> solutions for the scalar problem (14) are as follows.
>
> 1. If x̄ ∈ S is an optimal solution for (MOP_φ(w)), then x̄ ∈ S is a weak
>    optimal solution for (1MIOP_φ).
>
> 2. If x̄ ∈ S is an optimal solution for (MOP_φ(w)) with w_i > 0 for all
>    i ∈ {1, …, 2m}, then x̄ ∈ S is an optimal solution for (1MIOP_φ).
>
> 3. If x̄ ∈ S is the only optimal solution for (MOP_φ(w)), then x̄ ∈ S is an
>    optimal solution for (1MIOP_φ).
>
> 4. If S is convex, F is φ-convex and x̄ ∈ S is an optimal solution for
>    (1MIOP_φ), then there exists w = (w_1, …, w_2m) ∈ ℝ^2m with w_i ⩾ 0 for all
>    i ∈ {1, …, 2m} and Σ_{i=1}^{2m} w_i = 1 such that x̄ ∈ S is an optimal
>    solution for (MOP_φ(w)).

the exact conditions on the weights, statement by statement:

    standing, applying to every w that appears anywhere in the example, from the
    sentence introducing (14): w ∈ ℝ^2m, w_i ⩾ 0 for all i ∈ {1, …, 2m}, and
    Σ_{i=1}^{2m} w_i = 1. the normalisation to one is part of the standing
    condition and is not optional.

    statement 1: the standing condition only. no strict positivity. conclusion is
    weak optimality.

    statement 2: the standing condition, strengthened to w_i > 0 for **all**
    i ∈ {1, …, 2m}. conclusion is optimality.

    statement 3: the standing condition only. the strengthening is on the
    solution, not on the weights: x̄ must be the **only** optimal solution of the
    scalar problem. conclusion is optimality.

    statement 4: the converse. hypotheses are S convex and F φ-convex, plus x̄
    optimal for (1MIOP_φ). the conclusion asserts existence of a w satisfying the
    standing condition, with no strict positivity. so statement 4 does not invert
    statement 2: it returns a w that may have zero components.

note the index convention in (14): the sum runs over i ∈ {1, …, m}, the interval
objectives, and pairs weight w_2i−1 with the lambda coordinate Λ_i^T f and weight
w_2i with the beta coordinate B_i^T f. there are 2m weights for m summands.

note also that example 3.8 requires no differentiability anywhere. it is the
shorter route for any p1 branch where the image coordinates are not smooth, which
is what CONTEXT.md section 10 b1 anticipates.


## c14. example 3.9, necessary and sufficient optimality conditions

    claim in CONTEXT.md section 6: example 3.9, necessary and sufficient
    optimality conditions. its condition (15) is stationarity of the gradient of a
    weighted sum of the image coordinates, with weights nonnegative and not all
    zero. a point that matters for b1: example 3.9 requires Lambda_i^T f and
    B_i^T f to be differentiable. it does not require f_l and f_u to be
    differentiable.

verdict: **partially confirmed**. the differentiability claim is confirmed
exactly. the reading of the weight condition is one of two readings the printed
text admits and the paper does not settle it; reported as an ambiguity, not
resolved. the example has **three** numbered statements, not four.

location: example 3.9, section 3.1, printed page 10, lines 709-730. equation (15)
at lines 715-723. the differentiable-endpoints rewriting, equation (16), printed
pages 10 and 11, lines 732-746.

### hypotheses

transcription verbatim, lines 709-711:

> **Example 3.9** (Necessary and sufficient optimality conditions). Given
> F : S ⊆ ℝ^n → (C)^m such that F(x) = (F_1(x), …, F_m(x)) with
> F_i(x) = [f_i(x), f̄_i(x)] for all i ∈ {1, …, m}, let **Λ_i^T f, B_i^T f be
> differentiable** for all i ∈ {1, …, m} and 0 = (0, …, 0) ∈ ℝ^n. Thus,

the emphasis is added. the differentiability hypothesis is on Λ_i^T f and B_i^T f
and on nothing else. f_i and f̄_i are not required to be differentiable. CONTEXT.md
section 6 states this correctly and it is confirmed verbatim.

which functions are required to be differentiable, stated precisely: the 2m
real-valued functions Λ_i^T f = λ_2i−1 f_i + λ_2i f̄_i and
B_i^T f = β_2i−1 f_i + β_2i f̄_i, for i ∈ {1, …, m}. under the φ of example 2.2
these are f_i and f̄_i themselves, so for φ_lu the hypothesis is exactly
differentiability of the endpoint functions. under examples 2.3 and 2.4 they are
different combinations; but since each φ_i is invertible, differentiability of
both image coordinates is equivalent to differentiability of both endpoint
functions for **every** φ ∈ `A_m`. the hypothesis is therefore not weaker than
endpoint differentiability for any admissible φ. this is recorded because it
bears directly on the correction listed under c15 and on b1.

no constraint qualification appears and S carries no structure in statement 1.
statements 2 and 3 add convexity of S and φ-convexity of F.

### the three numbered statements

transcription verbatim, lines 712-730:

> 1. If x̄ ∈ S is a weak optimal solution for (1MIOP_φ), then there are
>    w_1, …, w_2m ∈ ℝ, with w_i ⩾ 0 not equal zero for all i ∈ {1, …, 2m}, such
>    that (15).
>
> 2. If x̄ ∈ S, S is convex, F is φ-convex and there are w_1, …, w_2m ∈ ℝ, with
>    w_i ⩾ 0 not equal zero for all i ∈ {1, …, 2m}, such that (15) holds, then x̄
>    is a weak optimal solution for (1MIOP_φ).
>
> 3. If x̄ ∈ S, S is convex, F is φ-convex and there are w_1, …, w_2m ∈ ℝ, with
>    w_i > 0 for all i ∈ {1, …, 2m}, such that (15) holds, then x̄ is an optimal
>    solution for (1MIOP_φ).

statements 1 and 2 together are the necessary-and-sufficient pair for **weak**
optimal solutions. statement 3 is sufficient only, for **optimal** solutions;
the paper gives no necessary condition for optimal solutions here. example 3.8
statement 4 is the nearest necessary result and it is a scalarization statement,
not a stationarity one.

the phrase "w_i ⩾ 0 not equal zero for all i ∈ {1, …, 2m}" in statements 1 and 2
is the ambiguity. see "ambiguities and text corruption".

### condition (15), written out in full

transcription verbatim, lines 715-723. the three expressions are chained by
equalities and the condition is that the last equals the zero vector of ℝ^n:

>     Σ_{i=1}^{m} w_2i−1 ∇Λ_i^T f(x̄)  +  Σ_{i=1}^{m} w_2i ∇B_i^T f(x̄)
>
>         = Σ_{i=1}^{m} ∇[ ( w_2i−1 Λ_i^T + w_2i B_i^T ) f ](x̄)
>
>         = ∇{ Σ_{i=1}^{m} [ ( w_2i−1 Λ_i^T + w_2i B_i^T ) f ] }(x̄)
>
>         = 0.                                                              (15)

in words: the gradient, at x̄, of the single real-valued function
Σ_{i=1}^{m} ( w_2i−1 Λ_i^T f + w_2i B_i^T f ) : S → ℝ vanishes. that function is
exactly the objective of the scalar problem (14) of example 3.8. so (15) is
first-order stationarity of the scalarized objective, and the weights of (15) and
the weights of (14) are the same 2m numbers, save that (14) also normalises them
to sum to one and (15) does not.

CONTEXT.md section 6's description, "stationarity of the gradient of a weighted
sum of the image coordinates", is confirmed as an accurate description of (15).

### equation (16), the rewriting when the endpoints are differentiable

transcription, lines 732-746:

> We note that if f_i and f̄_i are differentiable for all i ∈ {1, …, m}, then (15)
> can be rewritten as being
>
>     Σ_{i=1}^{m} ( w_2i−1 λ_2i−1 ∇f_i(x̄) + w_2i−1 λ_2i ∇f̄_i(x̄) )
>   + Σ_{i=1}^{m} ( w_2i   β_2i−1 ∇f_i(x̄) + w_2i   β_2i ∇f̄_i(x̄) )
>
>     = Σ_{i=1}^{m} ( w_2i−1 λ_2i−1 + w_2i−1 β_2i−1 ) ∇f_i(x̄)
>     + Σ_{i=1}^{m} ( w_2i−1 λ_2i   + w_2i−1 β_2i   ) ∇f̄_i(x̄) = 0.          (16)

the two lines of (16) are not consistent with one another: the first carries w_2i
on the beta terms and the second carries w_2i−1 on the same terms. reported under
"ambiguities and text corruption". b1 must not use (16) as printed without
settling this.

note also that (16) is offered as a convenience under an **extra** hypothesis
that example 3.9 does not require, and the paper immediately explains why that
extra hypothesis is unattractive, lines 750-752:

> However, due to the algebraic structure on C, in many cases it is very
> restrictive to require f_i and f̄_i to be differentiable for all i ∈ {1, …, m}.


## c15. the worked function given after example 3.9

    claim in CONTEXT.md section 6: [1] makes exactly this point with a worked
    function whose endpoint functions are non-differentiable at the candidate
    point while the relevant combination is smooth and convex. claim in
    CONTEXT.md section 10 a4: the paper states a conclusion about the point x = 0
    under one specific phi.

verdict on the transcription and on the conclusion and its φ: **confirmed**.
verdict on CONTEXT.md section 6's characterisation of what the worked function
demonstrates: **refuted**. see "disagreements with CONTEXT.md".

location: section 3.1, immediately after equation (16), printed pages 10 and 11,
lines 750-769. it is unnumbered: not an example, not a remark, a continuation of
the paragraph that begins "However, due to the algebraic structure on C".

### the function

transcription verbatim, lines 752-753:

> In fact, consider the interval-valued function F : ℝ → (C)^2, defined by
> F(x) = (F_1(x), F_2(x)), where F_1(x) = [−|x|, |x|] = [f_1(x), f̄_1(x)] and
> F_2(x) = [0, x^2] = [f_2(x), f̄_2(x)].

so n = 1, m = 2, S = ℝ, and

    F_1(x) = [−|x|, |x|]     f_1(x) = −|x|      f̄_1(x) = |x|
    F_2(x) = [0, x^2]        f_2(x) = 0         f̄_2(x) = x^2

both are legitimate: −|x| ⩽ |x| and 0 ⩽ x^2 for all x ∈ ℝ. the paper writes
"interval-valued function" where its own convention at lines 268-272 reserves
that name for m = 1 and calls the m > 1 case multi-interval-valued; here m = 2.
minor wording slip, no consequence.

### the conclusion the paper states, and the phi it is stated under

transcription verbatim, lines 753-755:

> Hence, f_1 and f̄_1 are not differentiable at x = 0, although x = 0 is a strict
> minimum for F considering the order relation ≦_φ with φ given in Example 2.2.

that is the whole of the paper's conclusion about the point. stated precisely:

    the point is x = 0.
    the property asserted is "a strict minimum", which in the vocabulary of
        definition 3.1(1) is a strong or strict optimal solution.
    the φ it is asserted under is the φ of **example 2.2**, that is φ_lu,
        λ = (1, 0), β = (0, 1).
    the paper gives no proof of the assertion and no argument for it.
    the paper says nothing about the efficient set of this F under any φ, and
        nothing at all about it under the φ of examples 2.3 or 2.4.

nothing beyond this is inferred here, per the session constraint and per
CONTEXT.md section 10 a4.

### the computation the paper attaches to it

transcription, lines 756-769:

> On the other hand, we have that Σ_{i=1}^{2} (Λ_i^T f + B_i^T f)
> = (Λ_i^T + B_i^T) f : ℝ → ℝ is given by
> Σ_{i=1}^{2} [ (Λ_i^T + B_i^T) f ](x) = x^2 for all x ∈ ℝ since, for this case,
> Λ_1 = (1, 0, 0, 0), Λ_2 = (0, 0, 1, 0), B_1 = (0, 1, 0, 0), B_2 = (0, 0, 0, 1)
> and f(x) = (−|x|, |x|, 0, x^2). Therefore, Σ_{i=1}^{2} (Λ_i^T f + B_i^T f) is a
> differentiable and convex function and ∇( Σ_{i=1}^{2} (Λ_i^T + B_i^T) f )(0) = 0,
> **which is a version of condition (15)**.

the emphasis is added. the arithmetic checks: Λ_1^T f = −|x|, B_1^T f = |x|,
Λ_2^T f = 0, B_2^T f = x^2, and the sum of the four is x^2, differentiable and
convex on ℝ, with derivative 0 at x = 0. the four vectors listed are exactly
the Λ_i and B_i of the φ of example 2.2 with m = 2, consistent with the
conclusion being stated under that φ.

the phrase the paper uses is "a version of condition (15)", not "condition (15)".
the qualification is load-bearing and is the reason for the refutation recorded
below: this F does **not** satisfy the hypotheses of example 3.9 under the φ of
example 2.2, because Λ_1^T f = −|x| and B_1^T f = |x| are both non-differentiable
at 0. what the passage exhibits is that the **aggregate** function
Σ_i (Λ_i^T f + B_i^T f) can be smooth and convex, with vanishing gradient at the
candidate point, when the individual image coordinates are not. it is a weakening
of (15), offered as motivation for not requiring endpoint differentiability. it
is not an instance of example 3.9.

for a4 and b1: this F is a legitimate p0 and the anchor is exactly as CONTEXT.md
section 10 a4 states, but b1 cannot reach the anchor by applying example 3.9
under φ_lu, because the hypotheses fail at x = 0. b1 must either use example 3.8,
which needs no differentiability, or work from definition 3.1 directly, or record
that the conditions do not close and go to the research chat, per CONTEXT.md
section 10 b1's stopping rule.


## disagreements with CONTEXT.md

three. the paper wins in all three. the corrections applied to CONTEXT.md are
reproduced as before and after blocks in the session reply.

### d-a. CONTEXT.md section 4 calls examples 2.2, 2.3 and 2.4 "the named examples of [1]"

refuted by c9. example 2.1, printed page 4, lines 234-262, is a further named
example of a φ with fully explicit coefficients. the three the project implements
are the three named examples that are each identified with a convexity notion;
they are not the only named examples in the paper.

the correction narrows the sentence and adds a pointer to example 2.1. it does
not change what the project implements, and example 2.1 is not proposed as a
fourth φ.

### d-b. CONTEXT.md section 6 says the worked function illustrates the differentiability distinction

refuted by c15. CONTEXT.md section 6 currently reads, in part: "example 3.9
requires Lambda_i^T f and B_i^T f to be differentiable. it does not require f_l
and f_u to be differentiable. [1] makes exactly this point with a worked function
whose endpoint functions are non-differentiable at the candidate point while the
relevant combination is smooth and convex."

the first two sentences are confirmed verbatim at line 710. the third is refuted
on three counts:

    under the φ of example 2.2, the φ the paper states the conclusion under,
    Λ_i^T f and f_i are the same function and B_i^T f and f̄_i are the same
    function. the worked function cannot separate the two hypotheses because
    under that φ they are not two hypotheses.

    more generally, since every φ_i ∈ `A_m` is invertible, differentiability of
    the pair (Λ_i^T f, B_i^T f) and differentiability of the pair (f_i, f̄_i) are
    equivalent for every admissible φ. the distinction CONTEXT.md draws is not a
    real weakening for any φ in `A_m`, at any point.

    the worked function satisfies neither: Λ_1^T f = −|x| and B_1^T f = |x| are
    both non-differentiable at 0. the paper says only that the aggregate
    Σ_i (Λ_i^T f + B_i^T f) = x^2 is smooth and convex and that its vanishing
    gradient at 0 is "a version of condition (15)", lines 761-769.

this matters for b1 exactly as CONTEXT.md predicted a mistake here would: a b1
that assumed example 3.9 applies at p0's anchor under φ_lu would be applying a
theorem whose hypotheses fail.

the correction rewrites the third sentence to say what the paper says, and adds
the consequence for b1.

### d-c. CONTEXT.md section 11 forbids the agent from editing PROGRESS.md and CONTEXT.md

not a disagreement with the paper. the session brief instructs the agent to
maintain PROGRESS.md and to correct CONTEXT.md against a verified source with the
diff shown, which the existing rule forbids. the rule is updated to match the
instruction, as the session brief's output 3 requires.


## ambiguities and text corruption

reported, not resolved. each says what the text does and does not settle, and
what it would cost the project to guess.

### a-1. equation (16) is internally inconsistent in the weight subscripts

location: printed pages 10 and 11, lines 732-746. verified against the raw
codepoints of lines 737 and 746, not against the rendered view, so this is not an
artefact of how the text displays.

the expanded line, line 737, reads

    Σ_i ( w_2i−1 λ_2i−1 ∇f_i + w_2i−1 λ_2i ∇f̄_i )
  + Σ_i ( w_2i   β_2i−1 ∇f_i + w_2i   β_2i ∇f̄_i )

the collected line, line 746, reads

    Σ_i ( w_2i−1 λ_2i−1 + w_2i−1 β_2i−1 ) ∇f_i
  + Σ_i ( w_2i−1 λ_2i   + w_2i−1 β_2i   ) ∇f̄_i = 0

the beta terms carry w_2i in the first and w_2i−1 in the second. the two lines
are not the same expression unless w_2i−1 = w_2i for every i, which nothing
assumes. the extracted text does not tell me which line is as the authors
intended.

what the text does settle: line 737 is the term-by-term expansion of (15) under
Λ_i^T f = λ_2i−1 f_i + λ_2i f̄_i and B_i^T f = β_2i−1 f_i + β_2i f̄_i, which are
the paper's own definitions at lines 647 and 656. line 746 is not. that is an
observation about internal consistency, not a choice of reading, and it is
recorded as such.

cost of guessing: b1 uses (15) directly and (16) is only a convenience. b1 should
expand (15) itself from the definitions of Λ_i and B_i and not cite (16). if (16)
is ever cited in the memoria, the discrepancy must be raised with the supervisors
first. raised as s-01 in PROGRESS.md.

### a-2. the weight condition in example 3.9 statements 1 and 2

location: printed page 10, lines 713 and 726. the printed phrase is

    "with w_i ⩾ 0 not equal zero for all i ∈ {1, …, 2m}"

two readings:

    reading one: w_i ⩾ 0 for all i, and w ≠ 0, that is the weights are
        nonnegative and not all zero.
    reading two: w_i ⩾ 0 and w_i ≠ 0 for all i, that is w_i > 0 for all i.

the sentence as printed supports either. reading two makes statement 3, which
states w_i > 0 for all i as its distinguishing hypothesis, a strictly weaker
conclusion drawn from an identical hypothesis to statement 2, which would make
statement 3 redundant. that is an argument from the structure of the example, not
from its text, and it is not treated here as settling the question.

CONTEXT.md section 6 commits to reading one. that commitment is not refuted by
the paper and is left standing; it is flagged so it is not mistaken for a
verified fact. raised as s-02 in PROGRESS.md.

cost of guessing: reading two would make example 3.9 statements 1 and 2 unusable
for any b1 candidate set that needs a zero weight, and would make statement 1's
necessary condition much stronger than it appears. any b1 result that depends on
a zero weight in statements 1 or 2 must carry the ambiguity explicitly.

### a-3. the printed definition of "efficient solution" for problem (12)

location: printed page 8, lines 514-516, immediately before theorem 3.1, quoted
in full under c11.

as printed, x̄ is efficient for (12) if there is no x ∈ S \ {x̄} with
h_i(x) ⩽ h_i(x̄) for **all** i, with no requirement that the inequality be strict
anywhere. the usual definition of an efficient, that is Pareto-optimal, solution
requires in addition that h(x) ≠ h(x̄). as printed the paper's condition is the
one usually called strong or strict efficiency.

this is not consistent with definition 3.1(2), which uses ≤_φ and, through
equation (6), does require a component where A_k ≠ B_k. the two differ exactly
on the degenerate case of two distinct decision vectors x ≠ x̄ with
(φ̄∘F)(x) = (φ̄∘F)(x̄): the printed definition of (12) says x̄ is not efficient,
definition 3.1(2) says x̄ may still be optimal. theorem 3.1 asserts the two
notions coincide.

the extracted text does not settle whether this is a typo, a deliberate
convention, or a place where the theorem's "if and only if" is intended modulo
that degenerate case. the weak version at line 516 is the usual one and is not
affected.

cost of guessing: it affects b2's second test, "no point of a dense random sample
dominates any point of the reference front", and the definition of dominance the
solvers and the metrics use. pymoo's non-dominated sorting uses the usual
definition, not the printed one. this must be settled before b2 and it is
recorded so the choice is deliberate. raised as s-03 in PROGRESS.md.

### a-4. the last term of the composition display before equation (13)

location: printed page 8, line 528. the display ends

    = (Λ_1^T f(x), B_1^T f(x), …, Λ_2m^T f(x), B_2m^T f(x))

but the sentence that immediately follows, lines 530-531, defines only Λ_1 … Λ_m
and B_1 … B_m. subscript 2m on the last pair has no referent. the preceding line
of the same display ends with (λ_2m−1 f_m + λ_2m f̄_m, β_2m−1 f_m + β_2m f̄_m),
which is Λ_m and B_m. theorem 3.2's (MOP_{(−φ)}) at line 595 writes Λ_m and B_m.

the extracted text does not settle whether this is the paper's typo or the
extraction's. it changes nothing: the vector has 2m components either way.

### a-5. theorem 3.3 does not restate the hypothesis phi in A_m

location: printed page 9, lines 638-641, quoted under c12. Λ_i and B_i are
defined only for the class `A_m`, at lines 530-531, and the proof invokes "the
definition of the automorphisms φ_i ∈ `A`" at line 659, but the theorem statement
itself asks only that ≦_φ be "the preference order relation given by (3)".
equation (3) is itself stated for the class, at lines 172-184, so the hypothesis
is present transitively. recorded for completeness; no consequence for this
project, which only uses φ ∈ `A_m`.

### a-6. two glyphs are missing throughout the extracted text

the class symbol and the beta row-vector symbol, described under "notation" at
the top of this document. every occurrence in the file is affected. the
consequence: this project cannot state from the paper what letter or typeface
[1] uses for the class of automorphisms or for the second row vector. CONTEXT.md
writes 𝔄_m and B_i; those names are used throughout the project and are
**not** verified against the source. they are names, not content. no coefficient,
hypothesis or conclusion depends on them.

if the pdf is obtained, this is settled in one look. raised as p-01 in
PROGRESS.md.

### a-7. the reference list of [1] is absent from the extracted text

the file ends at line 1685, in the middle of the appendix, with the proof of
proposition 5.1. there is no bibliography. the paper's own citation numbers
therefore cannot be resolved to works. the ones that matter to this project:

    [31]  cited for LU-convexity (example 2.2), CW-convexity (example 2.4), the
          formulation and definition 3.1 and definition 3.2 of [31] (examples 3.1
          and 3.3), theorem 4.2 (examples 3.4, 3.5, 3.6), and type-I and type-II
          Pareto (conclusion, lines 1521-1524).
    [26]  cited for LS-convexity (example 2.3), definition 3.4 of [26] (example
          3.2), theorem 4.3 (example 3.7), and LS-Pareto (conclusion, line 1526).
    [9]   the m = 1 predecessor paper, cited for definition 3.1 in [9],
          proposition 3.1 in [9], and the order relations ≦_{φ_i}, ≤_{φ_i},
          <_{φ_i} on C that equation (3) decomposes into. lines 140-141, 184,
          190, 230, 232, 1519.
    [7]   cited for the scalarization of examples 3.8 and 5.7.
    [23]  cited for the quasilinear space axioms in the conclusion.

consequences for the project:

    CONTEXT.md section 3 states that [9] in the supervisors' numbering, ishibuchi
    and tanaka 1990, "in the framework of [1] it is the automorphism of example
    2.4". [1] attributes example 2.4's CW-convexity to its own [31], which cannot
    be resolved from this text. the provenance claim is therefore **not
    verified** by this session. it is a provenance claim only and CONTEXT.md
    already says the operative definition used by the code is the one in [1], so
    nothing downstream depends on it.

    reference [9] of [1] is the direct predecessor of this framework, the m = 1
    case, and it is where the order relations ≦_{φ_i} on C are actually defined.
    equation (3) of [1] reduces the order to those relations. it is not among the
    five papers of CONTEXT.md section 3. this is recorded as r-02 in PROGRESS.md.

raised as p-01 in PROGRESS.md, together with a-6: obtaining the pdf settles both.

### a-8. definition 3.1 and definition 3.2 interleave two variants on one line

location: printed page 6, lines 371-374 and 385-389. the paper prints the local
variant as a bold parenthetical inside the sentence stating the global variant,
so each numbered item reads "there does not exist (**x ∈ N(x̄, δ) ∩ S \ {x̄}**)
x ∈ S \ {x̄} such that …". the convention is not stated in the text; it is
inferred from the bold typeface surviving the extraction and from the "(local)"
prefix on each item. the reading is not in doubt but it is recorded because the
transcription under c10 depends on it.

everything this project uses is the global variant. definition 3.2's item (1) at
line 387 additionally has its parenthetical displaced to the end of the line by
the extraction; the content is unaffected.


# a0-b addendum

subpart a0 reopened for one verification. document, no code. same source, same
locational conventions, same notation. the page mapping used here is the
extension printed under "how to read the locations".

verified on 2026-08-31.

why this addendum exists: a0 verified c1 to c15 over sections 2 and 3, which
CONTEXT.md section 9 puts in scope, and did not read section 5, which that
section puts out of scope. section 5 contains proposition 5.1, a statement about
two of the three phi this project implements. the scope decision has to be taken
knowing that, so the proposition is read and recorded here. reading it is not
adopting it: see the scope question raised as s-05 in PROGRESS.md.


## c16. proposition 5.1 and remark 5.1

    claim to verify: proposition 5.1 and remark 5.1. exact statement, both
    automorphisms with their coefficients, exact hypotheses, and which direction
    the implication runs and therefore which efficient set contains which.

verdict: **confirmed to exist and transcribed**. it is a statement about the two
**fuzzy** problems (1MFIOP_φ) and (1MFIOP_ψ). it is not stated for the interval
problems; see c17.

location: proposition 5.1, section 5.1, printed page 19, lines 1481-1487. remark
5.1, printed page 19, lines 1489-1494. the proof is deferred to appendix A,
printed page 22, lines 1664-1685.

### the sentence that introduces it

printed page 19, lines 1475-1479, transcribed:

> There exists a semantic meaning behind of each φ-multiobjective fuzzy interval
> problem, that is interpreted by means of its concept of solution, which is
> given by means of an automorphism φ ∈ `A_m`. Consequently, for each φ ∈ `A_m`,
> there exists a semantic meaning for the associated φ-multiobjective fuzzy
> interval problem. However, there exist cases in which it is possible to obtain
> optimality conditions for a φ-multiobjective fuzzy interval problem from the
> optimality conditions for another one as illustrated in the next result.

note the paper's own framing: "there exist cases". it is presented as an
exception, not as a general relation between automorphisms.

### proposition 5.1, transcribed verbatim

lines 1481-1487:

> **Proposition 5.1.** Let (1MFIOP_φ) and (1MFIOP_ψ) be the multiobjective fuzzy
> interval optimization problems such that φ is the automorphism given in
> Example 2.2 and ψ = (ψ_1 × … × ψ_m) ∈ `A_m` the automorphism given in
> Example 2.3, i.e.,
>
>     ψ_i(x_2i−1, x_2i) = (x_2i−1, x_2i − x_2i−1)
>
> for all i ∈ {1, …, m}. If x̄ ∈ S is an optimal solution for (1MFIOP_φ), then x̄
> is also an optimal solution for (1MFIOP_ψ).
>
> **Proof.** See the proof in Appendix A.

### remark 5.1, transcribed verbatim

lines 1489-1494:

> **Remark 5.1.** From Proposition 5.1 each optimal condition for (1MFIOP_φ),
> where φ is the automorphism given in Example 2.2, it is also an optimal
> condition for (1MFIOP_ψ), where ψ = (ψ_1 × … × ψ_m) ∈ `A_m` is the automorphism
> given in Example 2.3, i.e.,
>
>     ψ_i(x_2i−1, x_2i) = (x_2i−1, x_2i − x_2i−1)
>
> for all i ∈ {1, …, m}. Thus, it is possible to obtain optimal conditions for
> (1MFIOP_ψ) by means of the optimal conditions obtained for (1MFIOP_φ).

### the two automorphisms, with coefficients

    φ   example 2.2   λ_2i−1 = 1, λ_2i = 0, β_2i−1 = 0, β_2i = 1
                      φ_i(x_2i−1, x_2i) = (x_2i−1, x_2i)
                      composed with F: (f_l, f_u). LU. this project's phi_lu.
                      verified as v-06.

    ψ   example 2.3   λ_2i−1 = 1, λ_2i = 0, β_2i−1 = −1, β_2i = 1
                      ψ_i(x_2i−1, x_2i) = (x_2i−1, x_2i − x_2i−1)
                      composed with F: (f_l, f_u − f_l), full width. LS.
                      this project's phi_ls. verified as v-07.

proposition 5.1 restates ψ inline only in its collapsed form. the coefficients
themselves are not repeated there; they come from example 2.3, printed page 6,
lines 342-346. the collapsed form printed at lines 1484 and 1492 matches example
2.3's second expression exactly.

example 2.4, the centre and half-width automorphism, this project's phi_cw, does
**not** appear in proposition 5.1 or remark 5.1. no statement anywhere in [1]
relates its solution set to either of the other two.

### exact hypotheses

everything the proposition assumes, and nothing more:

    (1MFIOP_φ) and (1MFIOP_ψ) are the multiobjective fuzzy interval minimization
    problems of equation (23), printed page 16, line 1159, so they share the same
    feasible set S ⊆ ℝ^n and the same objective F̃ : S → (C(ℝ))^m. only the
    automorphism differs between the two problems.

    φ is the automorphism of example 2.2. ψ ∈ `A_m` is the automorphism of
    example 2.3.

    x̄ ∈ S is an optimal solution for (1MFIOP_φ).

there is no convexity hypothesis, no differentiability hypothesis, no constraint
qualification, and no structure on S beyond S ⊆ ℝ^n. in that respect it is like
theorems 3.1 and 3.2 and unlike examples 3.4 to 3.9.

one restriction that does matter: the proposition is stated for the **optimal
solution** concept only, definition 5.1(2), the one built on the strict relation
≤̃_φ. it is not stated for the strong or strict optimal solution of definition
5.1(1), nor for the weak optimal solution of definition 5.1(3). the paper gives
no analogue for either.

no converse is stated. [1] does not claim the reverse implication, and does not
claim the two solution sets are equal.

### direction of the implication, and which set contains which

the implication runs from example 2.2 to example 2.3, that is from LU to LS:

    x̄ optimal for (1MFIOP_φ), φ of example 2.2   ⟹   x̄ optimal for (1MFIOP_ψ),
                                                      ψ of example 2.3

so, writing Opt(·) for the set of optimal solutions of the fuzzy problem under
the named automorphism,

    Opt(example 2.2) ⊆ Opt(example 2.3)

the **example 2.3 solution set is the larger one**, and it contains the example
2.2 solution set. in the project's names, for the fuzzy problems: the phi_ls
solution set contains the phi_lu solution set.

this is a restatement of the printed implication in set language, which is what
the claim asks for. it is not an extension of the result and it says nothing
about the interval problems.

### what the proof does, reported without being relied on

appendix A, printed page 22, lines 1664-1685. it is a proof by contradiction.
assume x̄ optimal for (1MFIOP_φ); suppose it is not optimal for (1MFIOP_ψ); then
there is x ≠ x̄ with, for all α ∈ [0, 1] and all i ∈ {1, …, m},

>     (I)  f_{i,α}(x) ⩽ f_{i,α}(x̄)
>     (II) (f̄_{i,α} − f_{i,α})(x) ⩽ (f̄_{i,α} − f_{i,α})(x̄)

and the proof closes, line 1683, "Thus, from definition of ≤_φ, Definition 3.1,
and from Theorem 5.1, it follows that x̄ is not an optimal solution for
(1MFIOP_φ), which is a contradiction."

two observations, both factual and neither a derivation:

    the argument is carried out on the α-levels [f_{i,α}, f̄_{i,α}], which are
    intervals, and it invokes definition 3.1 and theorem 5.1, which are the
    interval-side objects. that is a description of how the printed proof is
    organised.

    it does not follow from that description that [1] states an interval
    analogue, and this document does not derive one. see c17 and c18.

the printed proof carries two errors, reported under "a0-b ambiguities and text
corruption" below.


## c17. is there an interval-space analogue in sections 2 or 3

    claim to verify: does an interval-space analogue of proposition 5.1 appear
    anywhere in sections 2 or 3? report what is found, or state that nothing is
    found. do not derive the interval case from the fuzzy one.

verdict: **not found**. sections 2 and 3 contain no stated relation between the
solution sets of two different automorphisms, and no analogue of proposition 5.1.
this is the answer, and nothing is derived from the fuzzy case.

how the search was done, so it can be repeated:

    every occurrence of ψ in the entire file was enumerated. there are nine, at
    lines 1481, 1482, 1484, 1485, 1490, 1492, 1664, 1665 and 1685. all nine are
    in section 5 or in appendix A. ψ does not occur anywhere in lines 99 to 771.

    every line in lines 99 to 771 was tested for naming two different examples
    from 2.1 to 2.4 in the same line. none does.

    lines 99 to 771 were swept for comparative and containment vocabulary:
    better, contain, subset, imply, implies, implication, superior, preferable,
    stronger, weaker, every optimal, any optimal. the only two hits are line 156,
    "it is a better representation for the considered components in a purchase of
    car", and line 237, "buying the car A is preferable to buying the car B",
    both descriptive prose inside the car-purchase illustration of example 2.1
    and neither a statement about solution sets.

    the whole file was scanned for any place where "Example 2.2" and
    "Example 2.3" occur within 400 characters of each other. there are exactly
    three: near line 1482 (proposition 5.1), near line 1489 (remark 5.1), and
    near line 1537 (the conclusion, where each is separately matched to a
    formulation in the literature, not to the other).

what sections 2 and 3 do contain instead: every result fixes one automorphism
and relates its problem to something else. examples 3.1, 3.2 and 3.3 relate
(1MIOP_φ) under one φ to a formulation in the literature. examples 3.4 to 3.7
give an optimality condition under one φ. theorems 3.1 and 3.2 relate one
φ-interval problem to one real multiobjective problem. theorem 3.3 characterises
φ-convexity for one φ. examples 3.8 and 3.9 hold for an arbitrary but fixed φ.
none of them puts two automorphisms in relation with each other.

whether the interval analogue is true, and whether it is a corollary of what is
printed, is not settled here. it is not stated, and the session constraint is to
say so and stop. raised as p-03 in PROGRESS.md, and it bears on the scope
question s-05.


## c18. where [1] states the relationship between the fuzzy and interval formulations

    claim to verify: where does [1] state the relationship between the fuzzy
    formulation and the interval formulation? transcribe it. this is what would
    decide whether the interval case is a corollary, and it is the supervisors'
    call.

verdict: **confirmed and located**. it is theorem 5.1. the order-level statement
that underlies it is definition 4.1 and equation (18).

### theorem 5.1, the problem-level relationship

location: theorem 5.1, section 5, printed page 16, lines 1207-1223.

the sentence that introduces it, lines 1207-1209:

> From (18), (19), (20), Definitions 3.1 and 5.1, and from the characterization
> of a fuzzy interval through its α-levels, φ-multiobjective fuzzy interval
> optimization problems can be associated with a family of φ-multiobjective
> interval optimization problems as follows.

theorem 5.1, transcribed verbatim, lines 1211-1223:

> **Theorem 5.1.** Given φ ∈ `A_m`, consider the φ-multiobjective fuzzy interval
> optimization problem (1MFIOP_φ) and the φ-multiobjective interval optimization
> problems (1MIOP_φ) given by
>
>     (1MIOP_φ)  min [F̃]_α(x)                                                (25)
>                x∈S
>
> for each α ∈ [0, 1]. Then
>
>   (i) x̄ ∈ S is a (local) strong or strict optimal solution for (23) if and only
>       if x̄ ∈ S is a (local) strong or strict optimal solution for (25) for all
>       α ∈ [0, 1].
>
>  (ii) x̄ ∈ S is a (local) optimal solution for (23) if and only if x̄ ∈ S is a
>       (local) optimal solution for (25) for all α ∈ [0, 1].
>
> (iii) x̄ ∈ S is a (local) weak optimal solution for (23) if and only if x̄ ∈ S is
>       a (local) weak optimal solution for (25) for all α ∈ [0, 1].

its only hypothesis is φ ∈ `A_m`. equation (23) is the fuzzy problem
min_{x∈S} F̃(x), printed page 16, line 1159. no proof is given in section 5; the
result is stated and then used.

three things about the shape of theorem 5.1 that decide what can and cannot be
read off it, stated without drawing the conclusion:

    it relates one fuzzy problem to a **family** of interval problems, one for
    each α ∈ [0, 1], not to a single interval problem. the interval problems are
    (25), whose objective is the α-level [F̃]_α of the fuzzy objective.

    the equivalence is "for all α ∈ [0, 1]" on the interval side. it is an
    equivalence, so it runs in both directions, but the interval side is a
    universally quantified family and not one problem.

    it covers all three solution concepts of definitions 3.1 and 5.1, unlike
    proposition 5.1, which covers only the optimal solution.

whether proposition 5.1 therefore yields an interval statement, and of what form,
is exactly the question theorem 5.1 would have to be applied to answer. this
document does not apply it. the session constraint is explicit that this is the
supervisors' call and not the agent's, and c17 has already established that [1]
does not state the interval case itself.

### definition 4.1 and equation (18), the order-level relationship

location: definition 4.1, section 4, printed page 12, lines 851-862; equation
(18), printed page 12, lines 865-872; proposition 4.1, lines 875-878.

definition 4.1, transcribed, lines 851-862:

> **Definition 4.1.** The φ, ⩽_{ℝ^2m}-preference order relation ≦̃^2m_φ on
> (F(ℝ))^m is given level-wise by
>
>     (ũ_1, …, ũ_m) ≦̃^2m_φ (ṽ_1, …, ṽ_m)
>         ⇔ ([ũ_1]^α, …, [ũ_m]^α) ≦^2m_φ ([ṽ_1]^α, …, [ṽ_m]^α)
>         ⇔ φ̄([ũ_1]^α, …, [ũ_m]^α) ⩽_{ℝ^2m} φ̄([ṽ_1]^α, …, [ṽ_m]^α)
>
> for all α ∈ [0, 1], where (ũ_1, …, ũ_m), (ṽ_1, …, ṽ_m) ∈ (F(ℝ))^m and ≦^2m_φ is
> the order relation given in (1).

equation (18), the specialisation to the class, lines 865-872:

> The following family of preference order relations, dependent on φ, considering
> φ ∈ `A_m` and ⩽_{ℝ^2m} the order relation on ℝ^2m given by (2), is defined by
>
>     (ũ_1, …, ũ_m) ≦̃_φ (ṽ_1, …, ṽ_m)
>         ⇔ ([ũ_1]^α, …, [ũ_m]^α) ≦_φ ([ṽ_1]^α, …, [ṽ_m]^α)                  (18)
>
> for all α ∈ [0, 1], where (ũ_1, …, ũ_m), (ṽ_1, …, ṽ_m) ∈ (F(ℝ))^m and ≦_φ is
> the order relation given in (3).

so the fuzzy order is defined as the interval order of equation (3) holding at
every α-level. proposition 4.1, lines 875-878, adds that ≦̃_φ is a partial order
relation, "This result follows directly from Proposition 2.2 and from (18)".

the two automorphisms of proposition 5.1 are written out at the level of α-cuts
in examples 4.2 and 4.4, printed page 14. example 4.2, lines 1023-1030, under the
φ of example 2.2, gives ≦̃_φ ⇔ u_{i,α} ⩽ v_{i,α} and ū_{i,α} ⩽ v̄_{i,α}. example
4.4, lines 1045-1053, under the φ of example 2.3, gives ≦̃_φ ⇔ u_{i,α} ⩽ v_{i,α}
and ū_{i,α} − u_{i,α} ⩽ v̄_{i,α} − v_{i,α}. the glyph for the fuzzy-interval space
is dropped by the extraction in the same way as the two glyphs reported in a0;
it is written (F(ℝ))^m here and the extraction leaves "( (ℝ))^m".

### for completeness, theorems 5.2 and 5.3

located at printed page 18, lines 1389-1398. they are the fuzzy counterparts of
theorems 3.1 and 3.2: x̄ is an optimal (weakly optimal) solution for (1MFIOP_φ)
if and only if it is an efficient (weakly efficient) solution for (MOP_{φ,α}) for
all α ∈ [0, 1], and correspondingly for (2MFIOP_φ) and (MOP_{(−φ),α}). they
relate the fuzzy problem to a classical multiobjective problem, not to an
interval problem, so they are not the answer to c18. both defer their proofs to
appendix A.


## c19. the conclusion's "better option" claim, and what it is conditional on

    claim to verify: the conclusion passage on the inclusion-order automorphism.
    transcribe the exact criterion under which the paper says one order "would be
    a better option". confirm or refute that the claim is conditional on that
    criterion rather than general.

verdict: **confirmed conditional**. the claim is not general. it is conditional
on two things stated in the same sentence chain: the case m = 1, and the decision
maker's objective being to use properties of an ordered quasilinear interval
space.

location note first. the session brief cites lines 1532-1535. that is not the
passage: lines 1532-1535 are in the fuzzy paragraph of the conclusion and read
"Thus, ≦̃_φ is a partial order relation on fuzzy-interval space … as shown in
Theorem 5.2, Theorem 5.3 and Examples 5.7 and 5.8." the inclusion-order passage
is at **lines 1503 and 1509-1516**, printed page 20. a0 recorded the same passage
at lines 1513-1515 and cited it as printed page 19; the line numbers were right
and the page was wrong, corrected at the top of this document and in PROGRESS.md
v-23.

### the passage, transcribed verbatim

the conditional opens at line 1503, on printed page 19, and the sentence runs
across the page break into page 20 at line 1509:

> Thus, considering a simple case, where m = 1, if one of the objectives of a
> decision making is to model an interval optimization problem aiming to use
> properties of an ordered quasilinear interval space, then semantically the use
> of the partial interval order ≦_{φ_1}, where φ_1 is given in Example 2.2, it is
> not suitable since the interval space equipped with this order does not satisfy
> the axioms of an ordered quasilinear interval space. To be more precise, the
> interval space equipped with this partial order does not satisfy the axiom
> (q.11) of Definition 2.1 in [23] and, in order to verify this fact one can
> consider X = C, α = 1, β = −1 and x = [−1, 1]. On the other hand, it is
> well-known that the preference partial order relation ≦_{φ_2}, where φ_2 ∈ `A_1`
> is given by φ_2(x_1, x_2) = (λ_1 x_1 + λ_2 x_2, β_1 x_1 + β_2 x_2), with
> λ_1 = −1, λ_2 = 0 = β_1, and β_2 = 1, and which coincides with the inclusion
> order ⊆, provides a structure of quasilinear space for the interval space (see,
> e.g., [23]). Consequently, the use of ≦_{φ_2} would be a better option than the
> use of ≦_{φ_1} in a decision making.

the symbol transcribed as X at line 1512 is dropped by the extraction, which
leaves a blank before "= C".

### the exact criterion, and the grammar that makes the claim conditional

the criterion is: **whether the interval space equipped with the order satisfies
the axioms of an ordered quasilinear interval space**, made precise as axiom
(q.11) of definition 2.1 in the paper's reference [23], with the counterexample
X = C, α = 1, β = −1, x = [−1, 1] showing that the order of example 2.2 fails it.

the claim is conditional, on two counts, both inside the same sentence chain:

    "considering a simple case, **where m = 1**". the passage restricts to one
    interval objective throughout. φ_2 is introduced as an element of `A_1`.

    "**if** one of the objectives of a decision making is to model an interval
    optimization problem aiming to use properties of an ordered quasilinear
    interval space, **then** …". the "Consequently" at line 1515 that carries the
    "better option" wording is drawn from inside that conditional, and from the
    two structural facts stated in between.

so it is refuted that the claim is general. [1] does not say the inclusion order
is a better option than LU as such. it says it is a better option **for a
decision maker whose stated objective is to use quasilinear-space properties**,
in the case m = 1. the criterion is structural, about the algebra of the ordered
space, and not about optimisation performance, solution quality, or any empirical
measure. nothing in the passage compares recovered solution sets.

this confirms rather than disturbs CONTEXT.md section 2. the paper's only
comparative statement about two automorphisms is conditional on a criterion this
project does not use and does not measure. a0's v-23 recorded the criterion but
not the m = 1 restriction; that refinement is added as v-27.


## a0-b: disagreements with CONTEXT.md

**none.** c16 to c19 refute nothing in CONTEXT.md.

the closest thing to a disagreement is not one. CONTEXT.md section 9 excludes
sections 4 and 5 of [1], and gives as its reason that slide 18 offers the fuzzy
branch as an alternative and not a requirement. that reason is about which
problem the project formulates, and c16 to c19 do not touch it. what c16 does is
put a fact in front of the exclusion that was not available when it was written:
section 5 contains a result relating the solution sets of two of the three
automorphisms in the experiment. whether the exclusion still stands is a scope
decision, and the session constraint is explicit that it is not the agent's to
take. raised as s-05 in PROGRESS.md with the working assumption the brief
supplies.

one correction was made, but to a0's own output and not to CONTEXT.md: the
conclusion's inclusion-order passage is on printed page 20, not printed page 19.
corrected in this document and in PROGRESS.md v-23.


## a0-b: ambiguities and text corruption

reported, not resolved, in the same way as a0's a-1 to a-8. numbering continues.

### a-9. the printed proof of proposition 5.1 carries two errors

location: appendix A, printed page 22, lines 1664-1685.

first, line 1665: "then there exists x ∈ S with x ≠ x̄ such that F̃(x) ≤_ψ F̃(x)".
both sides of the relation are F̃(x). the second argument has to be something
other than F̃(x) for the sentence to say anything, and the rest of the proof
compares x against x̄ throughout. the extracted text does not settle what is
printed in the journal.

second, lines 1675-1676: "However, from (I) and (II), it follows that there does
not exist x ∈ S with x ≠ x̄ such that f_{i,α}(x) ⩽ f_{i,α}(x̄) and
f̄_{i,α}(x) ⩽ f̄_{i,α}(x̄) for all α ∈ [0, 1] and for all i ∈ {1, …, m}". the
negation is inconsistent with what the proof concludes eight lines later at line
1683, "it follows that x̄ is not an optimal solution for (1MFIOP_φ), which is a
contradiction": a non-existence at line 1675 would give no contradiction. the
sentence at line 1675 is drawing a consequence from (I) and (II), which are
existence statements about a particular x, so the direction of the printed
negation does not match its own premises either.

neither error is resolved here. what is recorded is that the proof as extracted
does not read correctly and that this project has not verified the proof, only
the statement. the statement of proposition 5.1 at lines 1481-1485 is clean and
is what v-24 records.

cost of guessing: nothing immediate. the project does not use proposition 5.1 as
a result; under the working assumption of s-05 it is a prediction to be checked
empirically. if that ever changes, the proof has to be read from the pdf first.
this is a further reason to obtain the pdf, p-01.

### a-10. proposition 5.1 covers one solution concept and the paper does not say why

location: proposition 5.1, printed page 19, lines 1481-1485.

the proposition is stated for the optimal solution concept of definition 5.1(2)
and for neither of the other two. theorem 5.1, by contrast, is stated for all
three. the paper offers no remark on why the other two are omitted, and no
counterexample showing that they fail. the extracted text does not settle whether
the omission is deliberate or incidental.

not resolved. recorded because a b1 or e3 reading of proposition 5.1 that treated
it as covering weak or strict optimality would be going beyond what is printed.
