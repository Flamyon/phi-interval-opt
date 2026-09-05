# phase a: what was established, and what it changed

session a-close, 2026-08-31. phase a of CONTEXT.md section 8, formulation, is
complete: subparts a0 to a5 and the four addendum sessions a0-b, a1-b, a3-b and
a4-b.

who this is for. a reader who has not followed the sessions: the supervisors, and
the author in october writing the memoria. it repeats no derivation and states no
new result. every claim below points at the session deliverable or the paper that
established it, and where the two could differ the paper wins, which is
CONTEXT.md section 11's first rule.

**this document and docs/project_narrative.md cover the same ground and both are
kept**, docs-clean, 2026-09-05. that file is one continuous account of phases a to
c in plain words, written in the research chat rather than at a phase boundary,
with the failures narrated rather than cited; this one is the close-out of a
single phase, organised by subpart, and every claim in it points at the
deliverable that established it. **where the two could differ, this one wins.**
part 1 as a whole is docs/part1/part1_closing.md, which is the settled record and
supersedes neither.

where the detail is, so this document does not become a second copy of it:

    docs/verified.md                      every verified fact, v-01 to v-46,
                                          each with its source and location
    docs/answered.md                      answered questions and retired risks,
                                          with the reasoning that retired them
    PROGRESS.md                           the open p-, s- and r-rows and the
                                          session log
    git log                               one commit per subpart, with its full
                                          session record
    docs/part1/a0_framework.md            the verification pass over [1]
    docs/part1/a1_uncertainty_model.md    the uncertainty model decision
    docs/part1/a4b_dominance_tolerance.md the dominance rule decision
    docs/part1/a_close_containment.md     the phi_lu inside phi_ls containment

the papers, in CONTEXT.md section 3's numbering, which is the supervisors' own:

    [1] costa, osuna-gomez and chalco-cano, "new preference order relationships
        and their application to multiobjective interval and fuzzy interval
        optimization problems", fuzzy sets and systems 477 (2024) 108812.
        papers/new_preference_order_relationships_paper.txt
    [2] zitzler, deb and thiele, "comparison of multiobjective evolutionary
        algorithms: empirical results", evolutionary computation 8(2) (2000)
        173-195. papers/zitzler_deb_thiele_2000_comparison.pdf
    [3] deb, thiele, laumanns and zitzler, "scalable multi-objective optimization
        test problems", congress on evolutionary computation 2002, ieee.
        papers/deb_thiele_laumanns_zitzler_2002_scalable.pdf

and the supervisors' presentation, papers/Presentacion_optimizacion_intervalar.txt,
whose slides 17, 18 and 19 define the work.


## 1. what phase a established, in order

phase a is steps 1 to 3 of the methodology of slide 18: formulate the interval
problem, fix phi, transform to a classical multiobjective problem. it produces no
result about phi. what it produces is the ground the results will stand on: a
verified statement of the framework, a construction of imprecision that is not
degenerate, and code that evaluates both without arithmetic artefacts.

**a0, the verification pass over [1].** docs/part1/a0_framework.md. no code. fifteen
claims about the framework, taken from CONTEXT.md section 4 as the research chat
had read it, were checked against the paper itself: twelve confirmed, one refuted,
one partial and one split. it produced v-01 to v-23, each carrying an equation or
example number and a printed page: the class and its admissibility condition
lambda_2i-1 beta_2i != lambda_2i beta_2i-1 and nothing further (v-01, v-02), the
three named examples with their exact coefficients and the convexity notion each
coincides with (v-06 to v-08), definition 3.1's three solution concepts and their
implication chain (v-09), theorems 3.1 to 3.3 with their exact hypotheses (v-10 to
v-12), examples 3.8 and 3.9 with their numbered statements and condition (15)
(v-14 to v-17), and the worked function after example 3.9 that became problem p0
(v-18 to v-20). the refutation was that a further named example exists, example
2.1, with four different coefficient pairs in its four components and no convexity
notion attached (v-21). CONTEXT.md was corrected in sections 4, 6 and 11.

**a0-b, section 5 read once, deliberately.** docs/part1/a0_framework.md addendum, and
the source papers committed to papers/. CONTEXT.md section 9 puts sections 4 and 5
of [1], the fuzzy branch, out of scope, but section 5 contains proposition 5.1,
which relates two of the three phi this project implements. it was transcribed
rather than assumed: for the fuzzy problems, optimal under example 2.2 implies
optimal under example 2.3, with no convexity, no differentiability and no converse
(v-24). the interval side was searched exhaustively and the search method
recorded: sections 2 and 3 contain no stated relation between the solution sets of
two automorphisms and no interval analogue (v-25, v-26). that is what p-03 asked
and what session a-close closes.

**a1, the uncertainty model.** docs/part1/a1_uncertainty_model.md. no code. decides,
once for the project, how imprecision enters a problem. it rejected imprecision in
the coefficients and took bounded imprecision in the objective with a half-width
driven by a decision variable, and it did so on measurements rather than on
preference (v-30 to v-32, and finding 2 below). it produced the design rule that
every problem is built to, that all six image coordinates are convex under all
three phi exactly when c - r and r are both convex (v-33), the tier 0 problem p1,
and the tier 1 half-widths for both benchmarks.

**a2, interval_math.py.** six functions on numpy endpoint arrays with 16 tests,
tests/conftest.py, and requirements.txt with every version pinned to the venv.
[1]'s own interval arithmetic including the negative-scalar endpoint swap was
transcribed (v-34), and it was established that [1] never defines a centre, a
width, a radius or a gh-difference at all, those quantities existing in the paper
only as image coordinates of examples 2.3 and 2.4 (v-35). an addendum after review
confirmed pymoo 0.6.2 under numpy 2.5.2, the class name MOPSO_CD, and that pymoo
seeds only its own generator (v-36 to v-38).

**a3, phi_transforms.py.** the three named phi built through one constructor over
coefficients, validated against the paper's determinant condition exactly and not
against a tolerance, with 29 tests. gh_difference was re-cited from a literature/
summary to a primary source in papers/, slide 5 equation (2) of the presentation
(v-39, v-40), which retired r-10.

**a1-b, distinct widths for p1.** a1 gave both interval objectives of p1 the same
half-width, which made two of the four transformed columns the same function under
phi_ls and phi_cw. taking r_1 driven by x_2 and r_2 by x_1 removes that. the
modified p1 keeps every property a1 established and loses one, the efficient set
being no longer a product of intervals, which is re-answered as s-08. the same
session moved every verified fact into docs/verified.md and every retired row into
docs/answered.md, which is the filing the rest of phase a used.

**a4, problems_tier0.py.** p0, the worked function [1] gives after example 3.9,
with the published anchor x = 0 carried as a named constant together with the whole
of what the paper states about it and an explicit note that it is an anchor and not
an efficient set. p1 in a1-b's form. 13 tests, 42 in the suite, including the r-08
slice check as an assertion. the reading of the paper's "strict minimum" as
definition 3.1(1) was demoted from a claim to an inference and opened as p-06.

**a4-b, the dominance rule.** docs/part1/a4b_dominance_tolerance.md. measured what
computing a width as f_u - f_l costs, found a clean tolerance band and showed it
disappearing with magnitude, and recommended removing the subtraction instead
(finding 4 below). it changed p1's delta to 1/8 as d-01 after verifying in exact
integer arithmetic that delta enters every image coordinate as an additive
constant and moves no efficient set, and it established that pymoo 0.6.2's epsilon
argument is a no-op, dominance being translation invariant.

**a3-b, the evaluation-order fix.** the composite of phi with the endpoint map was
re-derived and checked in exact rational arithmetic on 2000 random coefficient sets
before anything was implemented (v-43), then both routes were built from one
coefficient pair and one admissibility check. p1 became primary in centre and
half-width form and builds no endpoint; p0 stayed in endpoints, the form [1] states
it in. the rounding step a4's test had needed was deleted and the same grids
returned a1-b's counts without it. 55 tests. d-02 closed, r-07 retired.

**a5, problems_tier1.py.** zdt1 and dtlz2 as interval problems in centre and
half-width form from the start, the crisp objectives read from [2] and [3]
themselves in that session (v-44, v-45). the separation sample is constructed from
each benchmark's published crisp Pareto set rather than sampled, which is finding 3
applied. neither benchmark saturates: the three phi are distinct at all four
positive levels with non-dominated fractions between 0.031 and 0.927. 22 tests, 115
in the suite.

**a-close, this session.** verified the phi_lu inside phi_ls containment
symbolically and numerically and wrote it up in docs/part1/a_close_containment.md, closed
p-03, raised s-11, and recorded in CONTEXT.md section 10 c3 that the validation
gate reports the containment's violation count as a measure of numerical noise.
this document is its other deliverable.


## 2. the four findings that changed the project's direction

these are the four places where phase a's output is different from what phase a set
out to build. each is stated with the evidence that forced it.

### the phi that was not in the paper, and its replacement by example 2.3

before the repository existed, the project carried a phi that had never been
checked against [1]. CONTEXT.md section 10 a0 records it in one sentence, as the
reason a0 exists: a0 "is a check on that reading, not a repeat of it, and it exists
because the project previously carried a phi that no one had ever checked against
the source." the replacement is example 2.3 of [1], lambda = (1, 0),
beta = (-1, 1), giving (f_l, f_u - f_l), the lower endpoint and the **full width**,
verified in a0 as v-07 at page 6, lines 342-346. that is a different order from
example 2.4's ((f_l + f_u)/2, (f_u - f_l)/2), the centre and the **half-width**,
v-08, and the difference is a factor of two in one coordinate.

the correction itself predates the repository and the repository holds no record of
the discarded phi. what phase a added is the verification and the rule. a0 checked
all three examples' coefficients against the printed page rather than against a
summary, established that they are the only named examples carrying a convexity
notion and that example 2.1 is a further named phi carrying none (v-21, v-22), and
CONTEXT.md section 4 now carries the standing instruction that no code and no table
may use one word for the full width and the half-width. the general form of the
lesson is CONTEXT.md section 11's first rule, that a coefficient or a theorem
statement enters the project only from a paper read in this project and recorded
with its location. every subsequent finding in this list was found because that
rule was being followed.

### the constant-epsilon degeneracy

slide 19 says, for the tier 1 benchmarks, "introduciendo incertidumbre acotada
+-epsilon en los objetivos", and the literal reading of that is a constant
half-width. a1 measured it and it is degenerate. on zdt1 with n_vars = 30 and m = 2
and on dtlz2 with n_vars = 12 and m = 3, at eps in {0.05, 0.5}, over 5000 uniform
points, the crisp non-dominated set and the three phi non-dominated sets are not
merely equal in size but identical as index sets, all four of them (v-30). the
reason is structural and is CONTEXT.md section 5 step 1: with the width constant,
the image of the feasible set in the centre-width plane is a curve, every injective
phi maps a curve to a monotone curve, and the three orders coincide.

a1 then showed that the degeneracy is not confined to a constant width. a
half-width that is any exact function of the centre does the same: proportional
imprecision f -> [f(1-eps), f(1+eps)] on zdt1 gives width spans of 0.84 and 2.19,
nowhere near constant, with correlation +1.0000 and all four index sets identical
(v-31). that is why imprecision in the coefficients was rejected: any objective
that is a monomial in an imprecise coefficient has a half-width that is an exact
linear function of its centre, and slide 19's tier 0 problems, "problemas sencillos
de una o dos variables", are exactly where objectives are monomials. measured on
zdt1 with f_1 = c_1 x_1 and c_1 in [1-d, 1+d]: correlation +1.0000 and phi_cw
returning the crisp non-dominated set exactly, at d = 0.10 and d = 0.25 (v-32).

the consequence for the project is that the half-width must be driven by a decision
variable that the centre does not resolve, that the crisp case is a labelled
degenerate baseline and not a data point in the sensitivity study, and that the
proportional construction is kept as a negative control. a3 reproduced the collapse
through the implemented phi and asserted it as a test (v-41).

### the zdt1 width alignment, and why a uniform-sample check is not enough

this is the finding a1 itself calls the one with the most consequence for the rest
of the project, and it is a finding about the diagnostic rather than about a
problem. the natural half-width for zdt1 is eps * x_n. it passes every check
CONTEXT.md section 5 step 1 prescribes: on a uniform sample of the 30-dimensional
box its width span is 0.4999, its correlation with the centre is -0.0111 and
+0.1027, its within-bin spread is 0.9943 and 0.9932 of the span, and the three phi
separate, |phi_cw| = 86 against |crisp| = 24. by the prescribed check it is a good
construction.

it is not. restricted to the slice where zdt1's efficient set actually lives,
x_2 to x_29 held at 0 with x_1 and x_n on an 81 x 81 grid, at eps = 0.25:

    crisp    |eff| =   81   frac 0.0123   x_n extent [0.000, 0.000]
    phi_lu   |eff| = 6561   frac 1.0000   x_n extent [0.000, 1.000]
    phi_ls   |eff| = 6561   frac 1.0000   x_n extent [0.000, 1.000]
    phi_cw   |eff| =   81   frac 0.0123   x_n extent [0.000, 0.000]   == crisp

phi_cw's efficient set on the slice is the crisp efficient set exactly, and phi_lu
and phi_ls are the whole slice. the uniform sample reported separation where the
efficient sets coincide, and it did so because a uniform sample of a
30-dimensional box contains essentially nothing near the efficient set. the cause
is alignment: [2]'s g is minimised at x_n = 0 and eps * x_n is minimised at x_n = 0
too, so under phi_cw nothing trades and x_n resolves exactly as the crisp problem
resolves it. reversing the alignment does not fix it, it breaks the other way,
every phi returning the whole slice, because g is linear in x_n and so is the width
and the trade-off has no interior resolution.

three things follow, and all three are in the code. zdt1's half-width is quadratic,
eps * ((x_n - 1/2)^2 + 1/20), whose optimum is interior at x_n = 1/2 and therefore
different from g's, while dtlz2's stays linear, eps * x_n, because [3]'s g is
already quadratic with an interior optimum; the two benchmarks get different forms
and each carries a1's reason in a comment. the check itself was strengthened: a4
and a5 re-grid the region where the efficient sets actually live and assert
separation there, which is r-08 built as a test, and a5 constructs its separation
sample from each benchmark's published crisp Pareto set rather than sampling the
box. and the question of whether the stronger check is the right one is s-07 to the
supervisors, with the tier 1 forms chosen against the stronger check meanwhile. the
residual is r-09: the rule was derived from two benchmarks and one tier 0 design and
is a working rule, not a result, so every new problem including f1's portfolio
returns runs the full diagnostic before use.

### the endpoint cancellation, and the evaluation-order fix

the second image coordinate of phi_ls and phi_cw is a width, and the obvious way to
reach it is to subtract endpoints. that is what a1 flagged as r-07 and what a4-b
measured. the error is eps|c| and nothing else: on p1's 61 x 61 grid against a
reference computed in integer arithmetic, the width column's maximum absolute error
runs 7.2e-16, 1.1e-13, 1.1e-10 and 1.1e-07 as the centre offset runs 0, 1e3, 1e6
and 1e9, while the same column computed from the centre and the half-width holds
2.2e-16 at all four.

the size of the error is not the finding. the finding is what it does to the
structure of the column: p1's r_1 depends on x_2 alone and takes exactly 46 distinct
values on that grid, and the endpoint route gives it 210 while the centre-radius
route gives it 46. an order built on a column is built on that column's ties, and
the subtraction shatters them.

a4-b then measured the obvious remedy and rejected it. a tolerance does work at
p1's magnitudes, every value from 1e-15 to 1e-04 returning the exact set for all
three phi with no spurious point and none lost, but the band narrows by one decade
per decade of centre magnitude and is gone by |c| = 1e12; and scaling the tolerance
per column by that column's own size is worse than not scaling, because the noise in
a width column is proportional to the centre it was subtracted out of and not to the
width. a tolerance would also have had to be shared by pymoo, and pymoo 0.6.2's
epsilon argument is a no-op, since it computes F - epsilon and dominance is
translation invariant.

so the subtraction was removed instead, as d-02. an interval's endpoint pair and its
centre-half-width pair are related by (f_l, f_u) = M (c, r) with M = [[1, -1],
[1, 1]] and det M = 2, and composing [1]'s phi with M gives the same automorphism
read in the other coordinates, with determinant 2 det phi, so it vanishes exactly
when the paper's admissibility condition fails and never otherwise. that was checked
entry by entry in exact rational arithmetic on 2000 random coefficient sets before
it was implemented (v-43). the consequence is the no-round-trip rule, now at the
interface of both problem modules: a problem declares the representation its
intervals are actually computed in, phi is applied once to that through the matching
route, and the pairing is automatic. p1 and both tier 1 problems declare
centre_radius and form no endpoint anywhere; p0 declares endpoints, the form [1]
states it in, where both routes agree bitwise. the a4 test's rounding step was
deleted and the same grids returned a1-b's counts without it, 31, 460, 1505 and 961
on the box and 40, 724, 2496 and 1600 on the slice. CONTEXT.md section 5 now states
one untoleranced dominance relation for the whole project, and the reason it can:
the arithmetic error a tolerance would have had to cover is not committed in the
first place.


## 3. the current phi, problems and their sources

one table. the centre-radius column is the same automorphism read in the other
coordinates, CONTEXT.md section 4 and v-43, and not a second family.

| object | on endpoints | on (c, r) | source, with location | verified | in |
| --- | --- | --- | --- | --- | --- |
| phi_lu | (f_l, f_u) | (c - r, c + r) | [1] example 2.2, page 5, lines 332-336; lambda = (1, 0), beta = (0, 1); coincides with lu-convexity | v-06 | src/phi_transforms.py |
| phi_ls | (f_l, f_u - f_l), full width | (c - r, 2r) | [1] example 2.3, page 6, lines 342-346; lambda = (1, 0), beta = (-1, 1); coincides with ls-convexity | v-07 | src/phi_transforms.py |
| phi_cw | ((f_l + f_u)/2, (f_u - f_l)/2), half-width | (c, r) | [1] example 2.4, page 6, lines 348-353; lambda = (1/2, 1/2), beta = (-1/2, 1/2); coincides with cw-convexity | v-08 | src/phi_transforms.py |

| problem | n_vars, n_obj | centres | half-widths | box, representation | source | in |
| --- | --- | --- | --- | --- | --- | --- |
| p0 | 1, 2 | F_1 = [-abs(x), abs(x)], F_2 = [0, x^2], stated as endpoints | c_1 = 0, r_1 = abs(x); c_2 = r_2 = x^2 / 2, derived | [-1, 1], endpoints | [1] page 11, lines 752-753, v-18; the anchor x = 0 under phi_lu, v-19 | src/problems_tier0.py |
| p1 | 2, 2 | c_1 = x_1^2 + (x_2 - 1)^2, c_2 = (x_1 - 1)^2 + (x_2 - 1)^2 | r_1 = rho x_2^2 + delta, r_2 = rho x_1^2 + delta, rho = 1/4, delta = 1/8 | [-0.5, 1.5]^2, centre_radius | project design, docs/part1/a1_uncertainty_model.md a1-b; delta by d-01, docs/part1/a4b_dominance_tolerance.md part 2 | src/problems_tier0.py |
| zdt1_interval | 30, 2 | [2]'s T_1: f_1 = x_1, g = 1 + 9 (sum_{i>=2} x_i)/(n_vars - 1), f_2 = g (1 - sqrt(f_1/g)) | r_1 = r_2 = eps ((x_30 - 1/2)^2 + 1/20) | [0, 1]^30, centre_radius | centres [2] definition 4, equation (7), page 177, v-44; half-width docs/part1/a1_uncertainty_model.md part 4 | src/problems_tier1.py |
| dtlz2_interval | 12, 3 | [3]'s DTLZ2 at M = 3, g = sum_{i>=3} (x_i - 1/2)^2 | r_1 = r_2 = r_3 = eps x_12 | [0, 1]^12, centre_radius | centres [3] section vii.b, equation (9), pdf page 4, v-45; half-width docs/part1/a1_uncertainty_model.md part 4 | src/problems_tier1.py |

the imprecision levels for both tier 1 problems are eps in {0, 0.05, 0.10, 0.25,
0.50}, docs/part1/a1_uncertainty_model.md part 4. eps = 0 is a labelled degenerate
baseline, not a data point: there every half-width is exactly zero, being a product
and never a difference, the second image coordinate of phi_ls and phi_cw is
identically zero, and all three phi coincide with the crisp order. p0 has no
imprecision parameter, its intervals being the paper's own.

m interval objectives give 2m real objectives, definition 2.1 of [1] and v-05, so
p0 and p1 are 4-objective real problems, zdt1_interval is 4 and dtlz2_interval is
6. n_obj on a Problem record is m and never 2m; the doubling belongs to
src/phi_transforms.py.


## 4. what is verified, and what is still open

verified. docs/verified.md holds v-01 to v-46, each with its source, its location
in that source, the session that checked it and the date. of those, v-01 to v-29
are claims read from [1], v-34 and v-35 as well, v-39 and v-40 are from the
supervisors' presentation, v-44 and v-45 are from [2] and [3] read in a5, and the
remainder are project derivations and diagnostics, each marked as such in its own
row and most of them asserted in the test suite. anything not on that list is not established, which is CONTEXT.md section
11's rule and is why the list is worth reading before relying on a number found
anywhere else in the repository.

the test suite is the executable half of the same record: 115 tests over the four
src/ modules, including the r-08 slice check on both tiers, the constant-width
collapse, the two-route agreement bitwise on a dyadic sample, and the invariance of
every efficient set as a constant up to 1e9 is added to every centre.

open. PROGRESS.md holds the open rows and this document does not restate them.
section 5 there is the questions the papers answer, p-01, p-02, p-04, p-05 and
p-06, all of which need a paper the repository does not have; p-03 was closed in
a-close. section 6 is the questions only the supervisors can answer, s-01 to s-11,
each carrying the working assumption the project proceeds on, none of them
blocking. section 7 is the live risks, r-02, r-03, r-04, r-05, r-06, r-08, r-09 and
r-11; r-01, r-07 and r-10 are retired and are in docs/answered.md with the reasoning
that retired them.

three of those matter enough to phase b to name here, with a pointer and nothing
more. r-03, the pdf of [1] is not in the repository and the extracted text lacks
its reference list, which is what blocks p-01 and p-02 and what makes s-11's second
question unanswerable inside the project. r-04, example 3.9's hypotheses fail at
p0's anchor under phi_lu, both image coordinates of the first objective being
non-differentiable at 0, so b1's check that the published conclusion is recovered
may not close by the planned route. p-05, [10] is wanted for the numbered statement
of the gh-difference and for the midpoint-radius regularity criterion b1 is
specified to apply.

what phase a does not contain, stated so that no reader looks for it. no efficient
set is derived anywhere in phase a and none is assumed: p0's published anchor is an
anchor and not an efficient set, and what the phi-efficient sets are, under each
phi, is b1's derivation and b2's encoding. no solver has been run on a project
problem. no comparison between phi has been made that is a result rather than a
construction check, and CONTEXT.md section 2 forbids part 1 from ranking phi at
all. the containment of docs/part1/a_close_containment.md is recorded and is not built
on until the supervisors answer s-11.
