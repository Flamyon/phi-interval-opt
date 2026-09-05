# phase b: what was established, and what it changed

session repo-clean-b, 2026-09-02, written after the fact. phase b of CONTEXT.md
section 8, ground truth, is complete: subparts b1 and b2, with no addendum
session. it is the only phase that closed without a summary, and this document
is that summary and nothing more.

who this is for. a reader who has not followed the sessions: the supervisors, and
the author in october writing the memoria. it repeats no derivation, runs no
measurement and states no new result. every claim below points at the session
deliverable that established it, and where this document and a deliverable could
differ the deliverable wins.

**this document and docs/project_narrative.md cover the same ground and both are
kept**, docs-clean, 2026-09-05. that file is one continuous account of phases a to
c in plain words, written in the research chat rather than at a phase boundary,
with the failures narrated rather than cited; this one is the close-out of a
single phase, organised by subpart, and every claim in it points at the
deliverable that established it. **where the two could differ, this one wins.**
part 1 as a whole is docs/part1/part1_closing.md, which is the settled record and
supersedes neither.

where the detail is, so this document does not become a second copy of it:

    docs/part1/b1_phi_efficient_sets.md  the derivation itself, sections 0 to
                                         10, with the hypotheses, the closed
                                         forms, the exact verification and p0's
                                         status
    src/reference_fronts.py              b2, and its module comment, which states
                                         what the module does and does not encode
    docs/verified.md                     the verified facts, each with its source
    docs/answered.md                     answered questions and retired risks
    PROGRESS.md                          the open p-, s- and r-rows
    docs/part1/session_log.md            b1's and b2's own session records
    docs/part1/phase_a_summary.md        phase a's close-out, on the same model
    docs/part1/phase_c_summary.md        phase c's, which judges its solvers
                                         against what phase b produced


## 1. why phase b exists at all

phase b is step 3 of the methodology of slide 18: know the answer before running
anything that claims to find it. CONTEXT.md section 10 a4 fixes the reason in one
sentence, that the small analytic problems are the only place a phi-efficient set
is available in closed form, so they are the only place a reference front exists,
the only place igd is defined, and the only place the solvers can be validated.

everything phase c measured, and everything phase e will measure on tier 0, is
measured against what phase b derived. that is the whole of its importance and it
is worth stating plainly: if b1's closed forms were wrong, the c3 gate would be
comparing solvers against a fiction and would not know it.


## 2. what b1 derived, and how

the method is the one CONTEXT.md section 10 b1 prescribes and it stays inside the
corpus throughout: write the image coordinates explicitly, check phi-convexity by
theorem 3.3 of [1], check regularity by the criterion of [10], apply example 3.9
to obtain the candidate set and its numbered statements to separate weakly optimal
from optimal, and use example 3.8 where scalarisation is the shorter route.

**the precondition, checked before anything was built on it.** condition (15) is
stationarity of the weighted sum, confirmed against [1] directly before use rather
than assumed from the shape of the formula. b1 section 0.

**the hypotheses close for p1 under all three phi.** all ten image coordinates are
quadratics with constant positive semidefinite hessians, so theorem 3.3 gives
phi-convexity globally under every phi, and regularity is trivial under [10]'s
midpoint-radius criterion, every function involved being a polynomial with a
strictly positive radius. b1 sections 1.2 and 1.3. the citation of [10]'s theorem
number is to a literature/ summary and not to the paper, which is p-05 and is the
one place in phase b where a number is carried unverified; the outcome does not
depend on it.

**the derivation is a closed form and not a search.** (15) is a diagonal linear
system for p1, so the weight-parameterised stationarity map

    x(w) = -(sum_k w_k H_k)^-1 (sum_k w_k b_k)

comes out as an explicit rational function of the weight vector, one per phi, with
no root-finding anywhere. verified exactly on 3000 random weights per phi with the
gradient identically zero. b1 section 2.2.

**the sets themselves are closed-form regions.** eliminating the weights gives
X_lu bounded by two conic arcs, X_ls by one, and X_cw exactly the closed unit
square up to one open edge, all three strictly interior to the decision box. b1
sections 2.4 and 2.5. these are two-dimensional regions and not curves, which is
s-08's answer and is what makes a coverage question askable at all. the closed
forms were verified in both directions in exact rational arithmetic: forward on a
denominator-40 simplex grid, 12341 weight vectors per phi with none landing
outside the stated region, and backwards at 301 random rational points of each
region, none without a witness weight.

**the strength of each conclusion is taken from the shortest published route that
carries it.** optimality comes from example 3.8 statement 3, whose hypothesis is
uniqueness of the scalarised minimiser and which needs no positive weights, rather
than from example 3.9 statement 3, which would deliver optimality only where every
weight is strictly positive. example 3.9 statement 1 closes the set from the other
side. b1 sections 2.6 and 4. this is a choice about which published statement is
cited and not a strengthening of any of them.

**the procedure was validated before it was trusted.** against a4's grid, 0 of
20000 derived points are dominated under any phi; phi_cw is exact at every
resolution, and the phi_lu and phi_ls residue is shown to be the finite grid
rather than the derivation, the excess distance staying at 2.6 grid spacings while
the absolute distance halves with the spacing, and 0 of 289, 0 of 1418 and 0 of
961 in-region points failing under a 24-fold local refinement. b1 sections 3.1 to
3.3.

**one result was reproduced independently.** both containments, ND_lu and ND_cw
inside ND_ls, fall out of the closed forms without using
docs/part1/a_close_containment.md's criterion. b1 section 5. that is a check on both and
neither is asserted by the project; the criterion is s-11.


## 3. what b2 encoded, and the distinction that matters

**src/reference_fronts.py encodes the derivation and not its conclusion.** the
module samples weights and pushes them through b1's map x(w); it does not carry
the inequalities of b1 section 2.4 anywhere in src/. those inequalities live only
in tests/test_reference_fronts.py, as the check that the sampled points land where
the derivation says they should.

that is the distinction, and it is worth being explicit about why it is not
pedantry. the map and the region are two different objects derived from the same
system: the map is what produces a point together with the weight that witnesses
it, and the region is what a point can be tested against. if src/ held the region
too, the membership test would be the module agreeing with itself and would catch
nothing. the same reasoning is why c3-c later duplicated region_excess into
tests/test_validation.py rather than moving it into src/. the encoded object is
the constructive one and the derived conclusion is the independent check on it.

two consequences follow and both are stated in the module:

**every returned point carries its witnessing weight**, which is what CONTEXT.md
section 10 b2's first test needs: condition (15) is checked numerically at every
sampled point with the weight b1 recorded, not with a weight refitted afterwards.

**p0 is refused by both entry points**, with b1 section 7.4's reason. b2 covers p1
and nothing else.

**the weight sample was chosen by measurement.** every extreme of b1 section 2.4
needs a zero weight, so a uniform simplex draw approaches them slowly; b2 draws
dirichlet with concentration 0.3, at which the worst gap from a fine lattice of
the derived region to the sample is 0.034, 0.165 and 0.138 under the three phi
against 0.274, 1.191 and 0.868 at concentration 1. docs/part1/session_log.md, b2.

**the test that catches a wrong derivation** is that no point of a dense random
sample dominates any point of the reference front: 0 of 2000 front points
dominated by 50000 uniform box points, at three seeds, under every phi and under
both settings of the singular flag. it samples randomly and not on a lattice, and
the reason is d-02: on a lattice test set it is not zero, one phi_ls segment point
colliding with an a4 grid point 5.6e-17 away and losing by one rounding step,
which is the dominance relation carrying no tolerance and is not a fault in the
front.


## 4. the two things that did not close, and why neither was patched

CONTEXT.md section 10 b1's stopping rule is that a derivation which does not close
with the published results as they stand stops and goes to the research chat, and
is not patched. it was invoked twice and honoured both times.

**the two singular weight segments, under phi_ls and phi_cw.** on the rays putting
all mass on one width coordinate the scalar problem has a line of minimisers
rather than one, so example 3.8 statement 3 does not apply; example 3.8 statement
2 and example 3.9 statement 3 need every weight strictly positive, which those
rays do not have; and no regular weight reaches the interior of the segments. the
published conditions therefore give weak optimality there and no optimality
verdict either way. b1 section 2.6.

what b2 did about it is nothing, deliberately. efficient_set and reference_front
take include_singular_segments with no default, so a caller has to state which of
the two sets it wants and the value belongs in every table beside the seed and the
point count. **the cost of not knowing was measured rather than argued**: with the
region sample held fixed and the segment added on top, the igd of a fixed test
front moves by -0.63 to +5.36 per cent at 1000 reference points and by -0.11 to
+1.35 per cent at 20000. so the question is priced. it is s-12 to the supervisors
and r-12 in PROGRESS.md, and it is open.

**p0, under every phi.** example 3.9's differentiability hypothesis fails at the
anchor x = 0 under all three phi, p0's first half-width being |x|, and theorem 3.3
refuses phi-convexity under phi_lu and phi_ls as well; under phi_cw the conditions
hold and are vacuous, the first image coordinate being identically zero. b1
sections 1.5 and 7.1. so p0's efficient set is not reachable from the optimality
conditions under any phi.

what was recovered instead is the published anchor and only that: example 3.8
statement 3 makes x = 0 an optimal solution under all three phi, so [1]'s stated
conclusion comes back, and the sets come from definition 3.1 applied directly. b1
sections 7.2 and 7.3. **p0 is therefore a smoke test and not a b2 fixture**, b1
section 7.4, which is why b2 refuses it. this is what retired r-04.


## 5. what phase b means for phase e

**the reference front exists for p1 and for nothing else.** every tier 0 recovery
number in c3, and every igd d1 might compute, is against p1 under three phi. p0
contributes one assertion, that a solver finds the published anchor, and no
metric.

**every tier 0 comparison inherits the singular-segment flag.** it has no default
by design, so e1 states it at the call site and prints it in every table, and where
two solvers land within a few per cent of each other under phi_ls or phi_cw, e1
reports the metric both ways rather than picking one. r-12.

**one of the three phi pairs is not free.** ND_lu and ND_cw both sit inside ND_ls
exactly, which b1 section 5 reproduces from the closed forms, so on the two phi_ls
pairs one direction of every coverage and overlap statistic is fixed before a
solver runs. e3's headline number comes from phi_lu against phi_cw, which is
nested in neither direction. CONTEXT.md section 10 e3, r-06, s-11.

**the region has an area, and that turned out to matter.** because b1 gives the
sets in closed form, c3-f could compute |X_lu| = 0.310533, |X_ls| = 1.513401 and
|X_cw| = 1 and attribute half of r-19's coverage deficit to the shape of the
region rather than to any solver. that half of the phase c finding is a phase b
object. docs/part1/c3_validation.md section 5.5.

**one reference-front risk is still open and is d1's, not b2's.** the sample is
drawn through the weight map, so its density in objective space is the
parametrisation's and not the front's, and igd averages over reference points.
r-13's mitigation is a b2-b before d1, and none at all if d1 is cut. c3 is
unaffected, measuring recovery by a hausdorff distance, which is a maximum.


## 6. what is verified, and what is still open

phase b closes with the derivation done, encoded, and checked from both
directions, and with two things it could not decide and did not pretend to.

    open and phase b's own:
        s-12  are the singular-segment points optimal solutions for (1MIOP_phi)
        r-12  the two reference fronts are two different objects for igd
        r-13  the reference sample's density is the parametrisation's
        p-05  [10]'s theorem number, cited to a summary and not to the paper
    open and touched here:
        s-02  b1 found a witness against the strict reading of example 3.9's
              weight condition, and no b1 result depends on the answer
        s-08  answered as assumed: the band is accepted, and it can retire on the
              supervisors' acknowledgement
        s-11  the containment criterion, which b1 reproduces but does not use
    retired here:
        r-04  p0's hypotheses, realised in b1 and mitigated by example 3.8

nothing in phase b blocks anything. the two open decisions have both been priced,
the segment question in per cent of igd and the p0 question in what p0 is allowed
to be used for, and the project proceeded on stated assumptions in both.
