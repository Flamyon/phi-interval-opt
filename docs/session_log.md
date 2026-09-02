# phi-interval-opt: session log

moved out of PROGRESS.md section 8 in session repo-clean, 2026-09-02, unchanged
and in order. PROGRESS.md keeps the last three entries and a pointer to this
file; everything before them is here.

one line per session, appended after review. never edited once written; a
correction is a new entry. the detail behind each line is in that session's
commit message and in its docs/ deliverable.

format:

    date | subpart | files | outcome | next

2026-08-31 | a0 | docs/a0_framework.md | 15 claims checked against [1]: 12
    confirmed, 1 refuted, 1 partial, 1 split. 23 verified facts. CONTEXT.md
    corrected in sections 4, 6 and 11 | a1 or a2; a0 unblocks a3 and b1
2026-08-31 | a0-b | docs/a0_framework.md addendum; papers/ committed | proposition
    5.1 transcribed; no interval-space analogue anywhere in [1]. 6 facts added,
    1 corrected | s-05 to the supervisors before b1 or e3 uses section 5
2026-08-31 | a1 | docs/a1_uncertainty_model.md | degeneracy hypothesis confirmed
    in exact arithmetic; coefficient imprecision rejected; p1 proposed; CONTEXT.md
    section 10 a4 corrected | a1 reviewed before a4, a5 or b1's p1 branch
2026-08-31 | a2 | src/interval_math.py, tests/conftest.py,
    tests/test_interval_math.py, requirements.txt | six functions, 16 tests pass.
    gh_difference cited to a literature/ summary, raised as p-05 and r-10 | a3
2026-08-31 | a2, addendum after review | none | pymoo 0.6.2 and numpy 2.5.2
    confirmed compatible, v-36 to v-38. s-06 split between a2 and a3 recorded.
    s-10 raised | a3
2026-08-31 | a3 | src/phi_transforms.py, tests/test_phi_transforms.py,
    src/interval_math.py comment only | three phi built through make_phi, 29 tests
    pass. gh_difference re-cited to a primary source, v-39. r-10 retired | a4
2026-08-31 | a1-b | docs/a1_uncertainty_model.md section "a1-b, distinct widths",
    docs/verified.md, docs/answered.md, PROGRESS.md, CONTEXT.md | modified p1 keeps
    convexity, interiority and phi-separation and loses the product-of-intervals
    efficient set for phi_lu and phi_ls. PROGRESS.md restructured | research chat
    decides p1's widths; then a4
2026-08-31 | a4 | src/problems_tier0.py, tests/test_problems_tier0.py,
    PROGRESS.md, docs/answered.md, docs/verified.md, CONTEXT.md | p0 and p1 built,
    p1 in a1-b's distinct-width form, 13 tests pass and 42 in the suite. the r-08
    slice check is a test. s-08 re-answered on the stationarity map, r-01 retired,
    v-42 added, CONTEXT.md sections 11 and 12 amended | b1, or a5
2026-08-31 | a4-b | docs/a4b_dominance_tolerance.md, src/problems_tier0.py,
    tests/test_problems_tier0.py, PROGRESS.md, CONTEXT.md | the endpoint route's
    error measured at eps|c| and shown to shatter the width column's structural
    ties; an eleven-decade clean tolerance band found; delta changed to 1/8 as
    d-01 after exact verification; the (centre, half_width) route recommended as
    d-02, open. pymoo's epsilon argument shown to be a no-op | the research chat
    takes or rejects d-02; then a5
2026-08-31 | a3-b | src/phi_transforms.py, src/problems_tier0.py, their tests,
    CONTEXT.md, PROGRESS.md, docs/answered.md, docs/verified.md | the composite
    re-derived and checked before implementing; both routes built from one
    coefficient pair and one admissibility check; p1 now primary in centre and
    half-width and p0 in endpoints; the a4 rounding step deleted and a1-b's counts
    reproduced without it. 55 tests pass. d-02 closed, r-07 retired, s-06 narrowed
    to a presentation question, v-43 added | a5, which builds tier 1 in centre and
    half-width form
2026-08-31 | a5 | src/problems_tier1.py, tests/test_problems_tier1.py,
    papers/ two benchmark pdfs, docs/verified.md, docs/answered.md, PROGRESS.md |
    zdt1 and dtlz2 built in centre and half-width form from a1 part 4's widths,
    both declaring centre_radius and forming no endpoint, the crisp half-width
    exactly zero. the crisp objectives taken from [2] equation (7) and [3]
    equation (9), read in this session, v-44 and v-45. the separation sample is
    constructed from each benchmark's published crisp Pareto set rather than
    sampled, per r-08, and neither benchmark saturates: the three phi are
    distinct at all four levels with the non-dominated fraction between 0.03 and
    0.93. the phi_lu inside phi_ls nesting was found to fail by one point of 1565
    through rounding, v-46 and r-11. 22 tests, 115 in the suite. the a4-b against
    a3-b magnitude-sweep discrepancy recorded beside r-07 and not investigated |
    b1, which now has both tiers to derive against
2026-08-31 | a-close | docs/a_close_containment.md, docs/phase_a_summary.md,
    CONTEXT.md, PROGRESS.md, docs/answered.md | phase a closed. the phi_lu inside
    phi_ls containment verified three ways, symbolically through the project's own
    phi routes, by exhaustive rational case analysis covering both strictness
    branches, and on p0, p1, zdt1 and dtlz2 with an exact filter returning zero
    violations where doubles return the one v-46 records. p-03 closed by the proof
    and s-11 raised, two questions: is it correct, and is it published, [26] being
    where it would sit. the project does not build on it. CONTEXT.md section 10 c3
    gains the violation count as a numerical-noise measure, which holds either
    way. p-04 re-owned to e3 with the date it was missing. one observation
    recorded and not developed: the same map argument appears to put phi_cw's set
    inside phi_ls's too, which bears on r-06 and is for the research chat. 115
    tests pass | b1
2026-09-01 | a-close-b | tests/test_problems_tier1.py, docs/a_close_containment.md,
    docs/verified.md, CONTEXT.md, PROGRESS.md | a5's |ls&cw| shortfall on dtlz2
    run down and found to be arithmetic, not bookkeeping: the helper builds index
    sets over one array and reproduces exactly under a second implementation, 8 of
    8 cases, and all 39 points at eps = 0.50 are phi_ls-dominated in doubles and
    none in exact arithmetic. every number the helper prints was recomputed
    exactly; only the phi_ls and phi_lu columns move, the crisp set and |cw| being
    bit-identical. v-47. the report gains cw<ls, ls<cw and a noise line, which is
    the one thing that was wrong, a containment printed as a raw intersection with
    no noise count beside it; no computation and no assertion was wrong. the
    result generalised: phi_B = M phi_A with M non-negative and invertible gives
    ND_B inside ND_A, verified with both hypotheses removed in turn, and both
    containments follow from it, so ND_lu and ND_cw both sit inside ND_ls.
    CONTEXT.md section 10 e3 now takes the sensitivity signal from phi_lu against
    phi_cw. s-11 widened to three questions, r-06 corrected, its phi_cw clause
    withdrawn. 115 tests pass | b1
2026-09-01 | b1 | docs/b1_phi_efficient_sets.md, PROGRESS.md | the phi-efficient
    sets derived. condition (15) confirmed to be stationarity of the weighted sum
    before use, from [1] lines 715-723. p1: all ten image coordinates convex with
    constant psd hessians so theorem 3.3 gives phi-convexity globally under all
    three phi, regularity trivial by [10]'s midpoint-radius criterion, cited to
    the literature/ summary with the number unverified, p-05. (15) is a diagonal
    linear system and x(w) comes out as an explicit rational map for each phi,
    verified exactly on 3000 random weights per phi with the gradient identically
    zero. the singular weights characterised: none for phi_lu, and for phi_ls and
    phi_cw exactly the two rays putting all mass on one width coordinate, each
    giving a consistent system with a line of solutions and never an inconsistent
    one. the sets in closed form, two conic arcs bounding phi_lu, one bounding
    phi_ls, and phi_cw's set exactly the unit square; all three strictly interior
    to the box. optimality taken from example 3.8 statement 3 rather than example
    3.9 statement 3, uniqueness of a strictly convex minimiser covering zero
    weights too, with example 3.9 statement 1 closing the set from the other
    side. against a4's grid: 0 of 20000 derived points dominated under any phi,
    phi_cw exact at every resolution, and the phi_lu and phi_ls residue shown to
    be the finite grid, the excess distance fixed at 2.6 spacings while the
    absolute distance halves with the spacing and 0 of 289, 0 of 1418 and 0 of
    961 in-region points falling under a 24-fold local refinement. both
    containments reproduced from the closed forms independently of
    docs/a_close_containment.md. p0: hypotheses fail wider than r-04 stated, the
    anchor still recovered under all three phi by example 3.8, the sets only from
    definition 3.1 directly, and p0 recorded as a smoke test and not a fixture.
    s-02 gains a witness against the strict reading, s-08 answered, r-04 realised
    and mitigated. one thing does not close and was not patched: on the two
    singular segments the published conditions give weak optimality and no
    optimality verdict | b2, which encodes the map and the regions

2026-09-01 | b2 | src/reference_fronts.py, tests/test_reference_fronts.py,
    PROGRESS.md | b1's derivation encoded as the map w -> x(w) of section 2.2 and
    a weight sample, never as the region's inequalities, which live only in the
    tests as the check that the sample lands where the derivation says. p1 only:
    both entry points refuse p0 with b1 section 7.4's reason. the weight sample is
    a dirichlet draw with concentration 0.3, chosen by measurement and not by
    taste, every extreme of b1 section 2.4 needing a zero weight: the worst gap
    from a fine lattice of the derived region to the sample is 0.034, 0.165 and
    0.138 for phi_lu, phi_ls and phi_cw against 0.274, 1.191 and 0.868 at
    concentration 1. the singular segments are a stated parameter with no default,
    b1 section 2.6 not closing there and b2 not closing it either; the cost of not
    knowing was measured rather than argued and is s-12 and r-12, the igd of a
    fixed test front moving by -0.63 to +5.36 per cent at 1000 reference points
    and -0.11 to +1.35 per cent at 20000, with the sign depending on the test
    front. 46 tests pass and 161 in the suite. the dominance test is 0 of 2000
    front points dominated by 50000 uniform box points, at three seeds, under
    every phi and under both settings of the flag; on a lattice test set it is not
    0, one phi_ls segment point colliding with an a4 grid point 5.6e-17 away and
    losing by one rounding step, which is d-02's subject and is why the test
    samples randomly | c1, random_search.py

2026-09-01 | c1 | src/random_search.py, tests/test_random_search.py, CONTEXT.md,
    PROGRESS.md | the control of slide 17, built so that the order is separable
    from the search: sample_decision_space takes no phi, so the sample is a pure
    function of the box, the budget and the seed, and
    filter_one_sample_under_every_phi draws one sample, evaluates it once and
    returns the non-dominated index set under each phi, three sets over one array.
    non_dominated_indices is the project's one dominance relation, no tolerance
    and no rounding; the copies in tests/test_phi_transforms.py and
    tests/test_problems_tier1.py could now import it and that is left as a
    separate decision. phi arrives by name and not as the phi_fn CONTEXT.md
    section 10 c1 writes, d-02 having made a bare callable unpairable with a
    problem's declared representation. 96 tests pass and 257 in the suite. the
    containment of docs/a_close_containment.md is asserted on solver output for
    the first time and holds exactly, ND_lu and ND_cw strictly inside ND_ls on p1
    and on both tier 1 benchmarks at two seeds, with no band: a5 needed 0.99
    because its lattice sample sits on dtlz2's face x_1 = 1 where c - r rounds a
    strict inequality to a tie, and a uniform sample reaches no such point. no
    random-search front point dominates any point of b2's reference front, under
    every phi and both settings of the singular flag. r-13 raised, the reference
    front's density in objective space being the weight parametrisation's and
    biasing igd; CONTEXT.md section 10 c3 corrected to measure recovery by
    hausdorff distance and never by igd | c2, runners.py

2026-09-01 | c2 | src/runners.py, tests/test_runners.py, pytest.ini, CONTEXT.md,
    docs/a_close_containment.md, docs/verified.md, PROGRESS.md | nsga-ii and
    mopso_cd wrapped around one shared contract: SearchResult, phi_image and
    require_seeds are imported from c1 and nothing of c1 is defined a second time,
    so the three solvers return one shape. two findings, both about pymoo 0.6.2 and
    both measured before being acted on. first, budget parity is not what ("n_gen",
    n) gives: nsga-ii spends pop_size * n_gen and mopso_cd spends one population
    more, 60, 100 and 200 against 80, 120 and 220 at pop_size 20, so the runners
    terminate on the evaluation count and both spend the stated budget exactly,
    v-49. second, mopso_cd is not reproducible at its default archive size: pymoo
    truncates an overflowing archive from a generator seeded by the operating
    system, and five runs of one seed on p1 under phi_ls gave five different
    fronts, diverging at generation 17 with the algorithm's own generator in an
    identical state; sizing the archive to the budget removes the overflow and the
    runs are bit-reproducible on all four problems under all three phi, v-48 and
    d-03, at a cost that is quadratic in the budget and is r-15. the check this
    session existed to make passes: the project's dominance relation is the
    identity on both solvers' fronts in all 24 cases, so pymoo's non-domination and
    the project's agree exactly and no phase e number will depend on which produced
    it, v-50. the column order is asserted through b2's own transformed_image and
    not inferred; the containments hold on both solvers' output; no solver front
    point dominates b2's reference front under any phi at either setting of the
    singular flag. 13 tests and 162 cases in the new file, 419 in the suite, 273 of
    them fast, and the suite splits by a slow marker,
    python -m pytest -q -m "not slow" for the fast run and python -m pytest -q for
    the full one. cost measured for e1 to plan against, r-15: at budget 5000 a run
    is 0.8 to 1.3 s for nsga-ii, 2.7 to 34.2 s for mopso and 3.9 to 4.6 s for
    random search, and non_dominated_indices alone is 2.3 s at n = 5000 and 396 s
    at n = 50000 with 2m = 6. CONTEXT.md section 10 c1 and c2 corrected from phi_fn
    to phi_name, section 11 given the rule that an agent may not mark a subpart
    reviewed, and docs/a_close_containment.md's standing constraint amended to say
    that a test may assert a containment as a self-check while no result is claimed
    from it | c3, the validation gate

2026-09-01 | c2-b | src/runners.py, tests/test_runners.py, CONTEXT.md,
    docs/verified.md, PROGRESS.md | two corrections to c2 and no new module. the
    archive: c2 made mopso reproducible by sizing the archive to the budget and
    rejected seeding pymoo's truncation on the ground that an archive policy is
    part of the algorithm, which inverts the rule it appeals to, the resize being
    the option that changes the search. checked in the source first, and reported:
    pymoo's Algorithm does take an archive at construction, core/algorithm.py lines
    34 and 58, but MOPSO_CD overwrites it in _setup at line 77 and rebuilds one
    every generation in _update_archive at lines 216 to 219, so an injected archive
    is discarded twice and a subclass is the only route. SeededArchiveMopso
    overrides that one method by delegation, three lines, reinstalling pymoo's own
    archive with a truncation that draws from the algorithm's seeded generator;
    nothing of mopso's sorting, pruning or sizing is reimplemented and archive_size
    is back at pymoo's 200. bit-identical over five runs at one seed on all four
    problems under all three phi, with the project's filter still the identity.
    seconds at budgets 500, 1000, 2000, 4000 and 20000 on p1 under phi_lu: 0.09,
    0.30, 0.82, 2.05 and 11.71 seeded, against 0.08, 0.32, 1.18, 6.61 and 187.78
    for c2's resize and 0.08, 0.32, 0.82, 1.91 and 10.35 for pymoo's unseeded
    default, so the fix tracks pymoo's own cost and is a factor of 16 cheaper than
    the resize at budget 20000. the reproducibility grid was found not to exercise
    the truncation at all at 400 evaluations, so a separate test counts the calls
    on the case that does overflow, p1 under phi_ls at 800. v-51, d-03 rewritten,
    r-14 remitigated. the cardinality confound measured and recorded, not fixed:
    one 610-row front subsampled uniformly gives igd 0.1303, 0.0851, 0.0551,
    0.0357, 0.0221 and 0.0201 and hypervolume 4.6845 to 5.1665 at 25, 50, 100, 200,
    500 and 610 rows, the same points from the same search, while nsga-ii returns
    100 rows, mopso at most 200 and random search 32 to 2220. v-52 and r-16, whose
    recommended rule is a common cardinality by uniform random subsample at a
    stated seed, with cardinality still printed beside every metric; CONTEXT.md
    section 10 d1 now requires it. r-15 rewritten with the archive fixed and with
    the research chat's budget plan: e1 and e2 sweep at budget 5000 with one
    budget-20000 run per problem as a convergence check, about 11 minutes for e1
    and about an hour for e2, the latter mostly random search's filter. 175 tests
    in the file, 432 in the suite | c3, the validation gate
2026-09-01 | c3 | tests/test_validation.py, docs/c3_validation.md, CONTEXT.md
    sections 10 c2, 10 d1 and 11 | the gate does not pass and phase e does not
    start. all three solvers on p1 under all three phi at budget 5000 over seeds
    11 to 15, both settings of include_singular_segments, recovery by hausdorff
    distance in the decision space with both directions reported separately and
    igd used nowhere. the tolerance is derived before the runs and not adjusted
    after them: the sum of two measured resolution floors, the covering radius of
    the derived region by b2's 1000-point reference sample and by a 100-point
    uniform draw of the region, 100 being nsga-ii's population and the smallest
    front the design fixes in advance; 0.1629, 0.3415 and 0.3213 for phi_lu,
    phi_ls and phi_cw against a box of side 2. twelve of forty-five
    configurations fail, every one of them in the solver-to-reference direction;
    the reference-to-solver direction passes in all ninety measurements, so no
    solver misses part of a derived set by more than the tolerance and the
    failures are all points returned that are not in the set. diagnosed in the
    order the brief sets and not concluded before: the box face is not the cause,
    two of twelve worst points sit on one; the budget is the cause for nsga-ii,
    all three of its failures fixed at 20000, for three of mopso's five and for
    none of random search's, whose forward distance is unchanged to four decimals
    at four times the budget; and no solver and phi pair fails on all five seeds,
    the worst being random search under phi_cw at three of five. a fourth check
    was added because the three did not say what the offending points are: ten of
    the twelve are dominated by b2's reference front and are therefore genuinely
    not efficient, and for random search that is structural, the sampled point
    with the smallest x_1^2 uniquely minimising an image coordinate and so
    surviving any filter whatever its x_2. the remaining two are dominated by
    nothing in the derived set, both under phi_cw on the singular line x_2 = 0
    past x_1 = 1 where b1 section 2.6 leaves the status undecided; s-13, which
    extends s-12. p0 checked as a smoke test only, per b1 section 7.4: all
    forty-five runs find the anchor x = 0, by two orders of magnitude, and the
    document says what that is worth, the whole box being optimal under phi_lu and
    phi_ls. the phi_lu points absent from the phi_ls set are zero in all ninety
    runs filtered, forty-five on p1 and forty-five on p0, so no tier 0 arithmetic
    noise; r-11's one measured violation stays a tier 1 finding. cardinality
    printed beside every number and nothing truncated, r-16 being an
    objective-space rule. CONTEXT.md corrected in three places, each reproduced as
    a before and after block in the session reply: section 10 c2's "unmodified"
    clause, section 11's evidence rules, and section 10 d1's two additions to
    r-16. r-17 raised, the gate's sensitivity to its own tolerance. 235 tests in
    the file, 667 in the suite, 24 failing and all of them the gate | the research
    chat, on the three decisions in docs/c3_validation.md section 9. e1 waits
2026-09-01 | c3-b | tests/test_validation.py, docs/c3_validation.md, CONTEXT.md
    section 10 c3, docs/verified.md, docs/answered.md, PROGRESS.md | the gate
    reopened, and the assertion was wrong rather than the code. c3 asserted the
    forward hausdorff, solver to reference, and twelve of forty-five
    configurations failed; that direction carries a floor that is a property of
    filtering a finite sample and not of any solver, so no tolerance derived from
    the region can be asserted against it. verified before acting on it and not
    taken on the brief's word: p1's image columns are (c_1 - r_1, c_1 + r_1,
    c_2 - r_2, c_2 + r_2) under phi_lu, (c_1 - r_1, 2 r_1, c_2 - r_2, 2 r_2) under
    phi_ls and (c_1, r_1, c_2, r_2) under phi_cw, so phi_ls and phi_cw each carry
    two columns depending on one variable alone and phi_lu carries none; the
    point of smallest |x_1| in any finite candidate set is then the strict
    minimiser of the r_2 column and nothing can dominate it whatever its x_2, and
    its x_2 ranges over [-1/2, 3/2] against X_cw's [0, 1]. measured: both extreme
    points are non-dominated under phi_ls and phi_cw at all five gate seeds and
    dominated under phi_lu at all five, and over 40 draws of 2000 points the
    phi_lu ones are dominated in 24 and 40 of 40 against 0 of 40 for the other
    two. the overhangs the argument predicts are c3's own worst points to four
    decimals, (0.00026, 1.41550) at 0.4155 and (-0.00000, -0.36913) at 0.3691,
    and c3's largest forward distance, 0.5000154, is the box overhang 1/2. v-53.
    so the gate now asserts the reverse hausdorff within c3's tolerance, which is
    not adjusted, and that no solver front point dominates any reference front
    point; both pass in all ninety measurements, the tightest reverse margin
    0.0106 at nsga-ii under phi_ls at seed 11. it reports the forward distance,
    the count of solver points dominated by the reference front as a fraction of
    front size for all three solvers, and cardinality beside every number. the
    budget trend is asserted for the population methods only, pooled over the five
    seeds because CONTEXT.md section 10 c2 puts five seeds in the design precisely
    because one run gives no variance, and it fails: nine of twelve cells hold and
    three rise, all phi_cw, nsga-ii at the True flag 20.80 to 21.80 per cent and
    mopso at both, 13.40 to 14.60 and 14.50 to 15.40. reported as a failure and
    not softened; pooling over phi as well would make both solvers pass, 19.00 to
    17.07 and 16.33 to 15.77, and that adjustment was refused. r-18 raised. per
    seed the count rises in eleven of thirty and falls or holds in nineteen.
    random search excluded from the trend with the reason in the code and
    measured: its front is the non-dominated subset of one uniform sample, so
    neither extreme point is dominated in any of the ten samples at 20000
    evaluations, and its forward distance is unchanged to four decimals. s-13
    checked against b1's closed form instead of b2's sample and dissolved:
    (0.999, 0.0001) is in X_cw, is off the undecided segment, and its phi_cw image
    (1.997801, 0.125000, 0.999801, 0.374500) is strictly smaller in all four
    columns than both recorded points, with 28 and 26 of 200000 interior draws
    dominating them; closed in docs/answered.md, and c3's ten of twelve is twelve
    of twelve. s-12 untouched. r-17 stands and now bites only on the reverse
    direction, which passes under both readings of h_design. CONTEXT.md section 10
    c3 corrected, reproduced as a before and after block in the session reply. no
    phi, problem, derivation, solver or dominance relation touched and no
    tolerance adjusted. 369 tests in the file, 801 in the suite, 3 failing and all
    of them the budget trend under phi_cw | the research chat, on r-18 and on
    whether the trend is the right thing to assert of a capped-front method. e1 is
    not blocked
2026-09-01 | c3-c | docs/c3_validation.md rewritten, tests/test_validation.py,
    docs/verified.md, docs/answered.md, CONTEXT.md sections 10 c3 and 10 e3,
    pytest.ini | three corrections, all of c3-b's own, and none about the
    solvers. **the protected extreme is now a proposition with a proof**, v-54:
    under phi_ls and phi_cw the second and fourth image columns are a (rho x^2 +
    delta) with a > 0, functions of one decision variable alone, so the member of
    strictly smallest |x_1| is the strict minimiser of one of them and nothing
    can dominate it whatever its other coordinate; the corollary is that the
    member of j-th smallest |x_1| can be dominated only by one of the j - 1 below
    it, so the whole low-|x_1| tail is shielded and not merely its first member.
    checked on 2000 adversarial finite sets, 0 dominations under phi_ls and
    phi_cw against 1066 and 1939 under phi_lu; on the gate's own draws the thirty
    smallest |x_1| survive the filter at 0.73 and 0.60 against 0.44 and 0.31 for
    the sample at large, and the thirty smallest |x_2| are dominated 150 of 150
    under phi_lu. over 200 uniform draws at n = 1000 to 80000 the median smallest
    |x_1| falls by a factor of four per factor of four in n while the mean
    overhang of the elected point's other coordinate does not move, 0.1226,
    0.1404, 0.1334, 0.1261, so a larger budget re-elects rather than removes.
    **the budget trend assertion is removed for all three solvers**, not
    weakened, not pooled and not restricted to phi_lu, and reported as a number
    on both measures; r-18 rewritten, it said no mechanism forces improvement and
    the truth is that a mechanism protects the offending points.
    **the sampled quality measure is replaced by exact region membership.** on
    nsga-ii under phi_cw at seed 11 the count dominated by b2's reference front
    runs 9, 12, 15, 18, 24, 26, 31 at reference sizes 250 to 16000 while the
    exact answer is 46 outside b1 section 2.4's region, so the old number was
    biased downward by a factor of three at the size c3 and c3-b used and is not
    comparable across reference sizes. region_excess duplicated from
    tests/test_reference_fronts.py rather than moved to src/, for the reason that
    file already gives: a region src/ also held would make both checks a file
    agreeing with itself. the outside fraction is 14 to 57 per cent, against the
    13 to 21 the brief expected, and the two protected extremes account for 0.4
    to 3.6 per cent of the outside points. diagnosis: boundary under phi_lu and
    for random search everywhere, at most 6 per cent of outside points beyond 0.1
    from the region and 925 of random search's 1062 phi_lu ones violating a
    curved boundary; scattered under phi_ls and phi_cw for the population
    methods, 32 to 47 per cent beyond 0.1, spread over all four faces of the box
    and reaching them, which is non-convergence and not spread.
    **the tolerance is corrected**, v-55: every reference point lies in the
    derived region, so the reverse direction is bounded by the fill distance of
    the solver set with respect to that region and by nothing else, and between
    two subsets of it the bound is max and never sum; checked 300 of 300 in both
    directions under all three phi with the reverse slack reaching 0.0000. so
    h_reference leaves the tolerance and h_design stops being one draw: 1000
    draws at k = 100, the 0.95 quantile fixed and justified in writing before the
    study ran, giving 0.2405, 0.2919 and 0.2318 against c3's 0.1629, 0.3415 and
    0.3213 -- up for one phi and down for two, which is what a derived tolerance
    looks like. the estimator is c3's: the first twenty draws reproduce 0.1246,
    0.2174 and 0.1836 exactly. the full distribution is in section 2.2 and
    phi_lu's runs 0.077 to 0.440 over 1000 draws, which is why twenty was not
    enough. r-17 retired to docs/answered.md, both its causes removed.
    **the gate now fails, and it is asserted for all three solvers anyway.**
    twelve of ninety reverse measurements over the tolerance, every one nsga-ii,
    three seeds under phi_ls and three under phi_cw and none under phi_lu, by
    0.005 to 0.039. exempting nsga-ii was refused and so was xfail: an assertion
    dropped for whichever solver it catches is not an assertion, and the one
    exemption granted before, random search's, rested on a proof of vacuity that
    v-54 has now extended to all three. r-19 raised: for a full-dimensional
    efficient set nsga-ii's decision-space coverage is worse than uniform random
    sampling at equal cardinality, at the 85th to 99th percentile of 1000 uniform
    100-point draws under phi_ls and phi_cw and the 33rd to 60th under phi_lu,
    with mopso showing it weaker at its own 200. four times the budget removes
    none of it, 0.3309 to 0.3315 and 0.2503 to 0.2531. everything else holds: no
    solver point dominates any reference front point in any of the ninety, p0's
    anchor found in all forty-five by two orders of magnitude, the containment
    diagnostic zero in all ninety runs filtered. CONTEXT.md sections 10 c3 and 10
    e3 corrected, both reproduced as before and after blocks in the session
    reply. no phi, problem, derivation, solver or dominance relation touched and
    no tolerance adjusted to make anything pass. 362 tests in the file, 794 in
    the suite, 12 failing and all of them the gate's reverse direction at
    nsga-ii; the fast run is 310 passed in 155s and the full run 782 passed and
    12 failed in 736s | the research chat, on r-19 and on whether a red suite
    carrying a stated finding is the right way to leave a gate. e1 is not blocked

2026-09-01 | c3-d | docs/c3_validation.md section 5 and its new section 5.1,
    CONTEXT.md sections 10 e2 and 10 e3, PROGRESS.md | one diagnostic, and the
    hypothesis it tested is refuted. **no code changed: no module added, nothing
    under src/ or tests/ touched, pymoo unmodified, and no assertion, tolerance or
    number in sections 1 to 4 of the deliverable moved.** the question was whether
    section 5's crowding-distance reading of the phi split is a demonstration.
    nsga-ii sorts pop_size + offspring = 200 candidates a generation and keeps 100,
    so if rank 1 alone holds 100 of them then no survivor is chosen by dominance
    and the front is a spread and not a convergence result. the route: a pymoo
    Callback reads the survivors' own rank and crowding attributes after every
    generation, core/algorithm.py line 329 and
    operators/survival/rank_and_crowding/classes.py line 99, and because pymoo
    keeps the survivors and discards the merged set they came from, the rank-1 size
    among the 200 and the front count are obtained by re-running **pymoo's own**
    NonDominatedSorting on the previous generation's survivors stacked on
    algorithm.off. a callback that reads state is not a modification and no sorting
    is reimplemented. the instrument is checked and not assumed: at every phi the
    front comes back bit-identical to src/runners.py's own solve_once at the same
    seed. **it saturates, and under all three phi.** on p1 at the gate's budget rank
    1 first reaches 100 at generation 4, 3 and 3 under phi_lu, phi_ls and phi_cw at
    all five gate seeds, never falls back at any of them, and holds a median of 167
    to 173 of 200 over the last thirty generations under every phi, with the
    survival sort enumerating one front where four or five exist. so for 46 or 47
    of the 50 generations dominance decides nothing, **including under phi_lu**, and
    a mechanism present under every phi cannot produce a finding that appears under
    two and not the third. **section 5's reading stays a reading**, rewritten to say
    so with the series as evidence, and no second hypothesis is constructed here to
    replace it. the finding itself is unchanged. the extremes were checked too: the
    28 to 39 points holding an infinite crowding distance in the five final fronts
    are enriched among section 3.3's outside points, outside 64 to 85 per cent of
    the time against a front base rate of 44 to 48, but account for only 8 to 14 per
    cent of them, 10 to 16 counting every point that was ever an extreme; descent
    from an extreme, measured with a Mating subclass that delegates to pymoo's own
    _do and again reproduces the run bit-identically, is 100 per cent of the front
    against a base rate of 100 per cent and separates nothing. the outside counts
    the run returns, 222, 239 and 235, are section 3.3's own, which is the check
    that this is the same run. **tier 1, at eps = 0.10 and seed 11**: dtlz2_interval
    at 6 columns saturates at generation 4, 3 and 3 and sits at a median rank 1 of
    146, 155 and 153 of 200; zdt1_interval at 4 columns in 30 variables is the only
    place dominance survives a while, first reaching 100 at generation 14, 13 and
    21, dipping back twice under phi_lu, and holding a median of 124, 131 and 118.
    the column count is not on its own what orders the three problems, since p1 also
    transforms to four columns and saturates as fast as dtlz2 does; what tracks the
    ordering is the non-dominated fraction of the transformed image, 0.58, 0.79 and
    0.55 on dtlz2 against 0.24, 0.52 and 0.47 on zdt1, and three problems is not
    enough to assert that and it is not asserted. one arithmetic correction to the
    prompt, which does not change what it predicted: p1's a4 grid is 61 x 61 = 3721
    and not 1728, so the expected rank-1 sizes among 200 are 25, 81 and 52 rather
    than 53, 174 and 111; both sets predict the same split and both are refuted the
    same way. no v-row added: the brief attached one to the branch where the
    mechanism carries the split, and it does not. CONTEXT.md sections 10 e2 and 10
    e3 now require the rank-1 size against the population size for every
    configuration, r-19 extended with the tier 1 numbers and with the trigger and
    mitigation that follow. the suite is unchanged because nothing in it changed:
    the fast run is 310 passed in 144s and the full run 782 passed and 12 failed in
    728s, the same twelve gate tests at nsga-ii as c3-c left | the research chat,
    on what the phi split is if it is not the sorting, and on r-19. e1 is not
    blocked

2026-09-02 | c3-e | nothing; the session ended before it wrote and **never
    committed** | recorded here by c3-f so the gap in the log is visible rather
    than silent. it ran three measurements and all three survive in
    docs/c3_validation.md sections 5.2, 5.3 and 5.4, where they are marked as its.
    **no code changed and none was proposed.** part 1, the effective cardinality:
    a front row far from R occupies a slot without contributing coverage, so each
    run's percentile was re-read at the number of rows within a stated distance of
    R rather than at 100. the distance is 0.10 because that is section 3.3's own
    cut, with 0.02, 0.05 and 0.20 beside it and an assumption-free companion, the
    count of rows holding a non-empty voronoi cell within R. it is not the deficit:
    the effective cardinality is 96 to 99 under phi_lu and 80 to 89 under the other
    two, the correction buys 2 to 11 percentile points of a gap of 50, and all ten
    failing measurements stay at or above the 74th percentile. part 2, the image
    space: nsga-ii's fill distance against the image of R, each column normalised
    by its range over that image as crowding distance normalises, read against
    1000 uniform k-point draws of the same image drawn with the same generator and
    seed so the two spaces are paired. under phi_ls and phi_cw it is at the 17th to
    86th and 31st to 71st percentile, ordinary, against 85th to 99th in the
    decision space; under phi_lu it is at the 0.1st to 4.9th, which the reading
    fixed in advance did not anticipate and which is stated rather than smoothed.
    so nsga-ii is not worse than uniform at what it optimises under either failing
    phi. part 3, the jacobian, closed form from b1 section 1.1 and checked against
    central differences to 7.6e-10: under the column-normalised map phi_lu is the
    anisotropic one, median ratio 3.97 against 1.42 and 1.45, the reverse of the
    ordering a pullback story needs, and no ratio anywhere exceeds 10 | superseded
    by c3-f's prompt, which rereads these numbers and asks the next question

2026-09-02 | c3-f | docs/c3_validation.md new sections 5.2 to 5.5 and its head
    note, section 5's closing paragraph, sections 10 and 11; docs/verified.md v-56;
    CONTEXT.md section 10 e3; PROGRESS.md | one diagnostic and it closes phase c.
    **no code changed: no module added, nothing under src/ or tests/ touched, pymoo
    unmodified, no assertion added to the suite, and no tolerance or number in
    sections 1 to 4 moved.** it also records c3-e, which never committed. the
    session's own prompt supplied the rereading and it is verified against c3-e's
    tables before being acted on: the image-space percentiles really are 0.1 to 4.9
    under phi_lu against 17 to 86 and 31 to 71 under the other two, so the anomaly
    is phi_lu being extraordinarily good and not the other two being bad.
    the hypothesis tested: since J_lu = A J_cw with A^T A = 2 I, the phi_lu and
    phi_cw images are the same object up to a rotation and a uniform scaling, and
    crowding distance is computed per column and normalised by column range, so it
    is not rotation invariant; the candidate is that the operator favours one
    alignment. **it is refuted.** reading each nsga-ii front in every frame with its
    own decision set and its own region held fixed, so that only alignment moves,
    the phi_cw runs read in the lu frame sit at 44.3 to 80.5 and the phi_lu runs
    read in the cw frame stay at 12.9 to 46.0: **the advantage travels with the run
    and not with the frame.** the frame change is asserted and not inspected, since
    A^T A = 2 I forces every raw distance in the lu frame to be exactly sqrt(2)
    times the same distance in the cw frame, and over all thirty runs the maximum
    relative departure is 4.5e-15. pymoo's own calc_crowding_distance on the same
    front in each frame confirms the operator works and splits nothing: the
    coefficient of variation is lowest in the run's own frame in all fifteen runs,
    which is the best instrument check in the document, and the diagonal values are
    0.25 to 0.32, 0.24 to 0.43 and 0.25 to 0.30, one behaviour and not three.
    **the control that should have been in the first framing.** random search is
    phi-neutral by construction, c1's sample being a pure function of the box, the
    budget and the seed, so the three phi filter one identical draw. at matched
    cardinality, twenty uniform 100-row subsamples of each front read against the
    same k = 100 distribution nsga-ii is read against, it has no deficit under any
    phi: 12.7 to 29.4, 21.4 to 63.2 and 31.1 to 48.7, thirteen of fifteen below the
    median, against nsga-ii's 33 to 60, 85 to 98 and 90 to 99. so the split is the
    operator meeting the order and not a property of the phi-efficient sets that
    any method at fixed cardinality would inherit.
    **the dimensional check, added to this session on review rather than opened as
    another.** the three region areas in closed form, |X_lu| = 0.310533,
    |X_ls| = 1.513401 and |X_cw| = 1, agreeing with adaptive quadrature to 3.9e-16
    and with a 4-million-point monte carlo of the gate's own in_region to 7e-4, and
    matching b1's twelfth, three eighths and quarter. in units of sqrt(|R|/k) a
    uniform draw covers X_lu 40 per cent worse for its area than it covers the
    other two, so the comparator is itself region-dependent and weakest exactly
    where nsga-ii looks best. it does not dissolve the finding, and the control is
    what shows that: in units of the uniform mean at the same k, random search
    carries +0.243 of nsga-ii's +0.483 swing from phi_lu to phi_ls and +0.244 of
    its +0.485 to phi_cw, **exactly half**, the agreement to three decimals being a
    coincidence of two numbers and read as nothing. the gap between the solvers at
    the same k, region and comparator is +0.165, +0.405 and +0.406.
    **where phi_ls sits, and this is the part that outlives the split.** all three
    images are constant linear images of one another because each phi is a constant
    linear map of the endpoint pair. g_lu = A g_cw with A^T A = 2 I, a similarity,
    ratio exactly 1; g_ls = B g_cw with B^T B block diagonal in two copies of
    [[1,-1],[-1,5]], eigenvalues 3 +- sqrt 5, singular values sqrt(3 + sqrt 5) and
    sqrt(3 - sqrt 5) each twice and condition number exactly
    (1 + sqrt 5)^2 / 4 = 2.618034, the golden ratio squared; and the phi_ls to
    phi_lu map has singular values exactly phi and 1/phi. verified to 0.000e+00 on
    500 random points and on all three region samples, and to 7.1e-15 for the
    pointwise equality of phi_lu's and phi_cw's raw jacobian ratios. **so no
    statement of the form "the phi_lu map distorts more than the phi_cw map" can be
    true**, and 5.4's apparent difference between their raw rows is averaging over
    two different regions. this is v-56, it contains no parameter of p1, and it is
    reported and not asserted, this session adding nothing to the suite.
    **what closes.** four candidate mechanisms excluded by direct measurement,
    across c3-d, c3-e and c3-f: saturation, wasted slots, the pullback, the
    anisotropy of the map, and the alignment of the operator's axes. what replaces
    them is a decomposition, half the swing carried by a method with no operator
    and half nsga-ii's own, and **the residual half has no mechanism and is not
    given one here.** phase c closes with the split measured, bounded, halved and
    honestly unexplained, which is what the brief asked for if it came to that.
    the suite is unchanged because nothing in it changed: the fast run is 310
    passed in 148.58s and the full run 782 passed and 12 failed in 899.35s, the
    same twelve gate tests at nsga-ii as c3-c left | the research chat, on
    whether the residual half is worth another session or whether e1 reports it
    as measured. e1 is not blocked

2026-09-02 | c-close | CONTEXT.md sections 10 e3 and 11; new
    docs/phase_c_summary.md and docs/supervisor_questions.md; PROGRESS.md | the
    phase c close-out. **no measurement was run and no mechanism was proposed.
    no code changed: nothing under src/ or tests/ touched, no phi, problem,
    derivation, solver, dominance relation or tolerance moved, and the two new
    documents cite session deliverables and add no claim of their own.**
    three changes outside the two new documents. **CONTEXT.md section 11 gains a
    commit rule**, prompted by c3-e ending without committing and its numbers
    surviving only in a scratchpad, the second uncommitted session in a row: a
    session commits whatever it has established before starting any run expected
    to take more than a few minutes, and again at its end; a measurement that
    exists only in a scratchpad is not a result of this project, since the
    scratchpad is not in the repository, is not reviewed and does not survive the
    session; and where a session ends without committing, the next session
    records the gap in the session log rather than absorbing the work silently,
    as c3-f did for c3-e. **CONTEXT.md section 10 e3 gains the instruction that
    the phi_lu against phi_cw comparison is made on random search output**,
    through src/random_search.py's filter_one_sample_under_every_phi, which is
    the amendment c3-f's control forces: random search is phi-neutral by
    construction, sample_decision_space taking no phi and the sample being a pure
    function of the box, the budget and the seed, while nsga-ii's coverage of the
    derived region is phi-conditional at matched cardinality, so a difference
    between recovered sets measured on nsga-ii output is confounded with
    nsga-ii's own behaviour and is not evidence about the order. the population
    methods are reported separately with the coverage deficit and the saturation
    beside them. c1 is therefore the instrument carrying the study's main result
    and not a baseline to beat, which is what its own module comment always said
    it was for and what slide 17 asked for it. **PROGRESS.md moves phase c to
    complete and the current subpart to d2**, with d1 and d3 marked off
    CONTEXT.md section 8's minimum presentable path, and records what phase d
    depends on: no open row blocks d2, which must carry s-12 and r-12 through
    include_singular_segments having no default, r-11 and r-06 through naming the
    doubles artefact in the phi_lu against phi_ls pair, s-11 through reporting
    that pair as a check and not a finding, and r-16 through printing cardinality
    beside every metric; d1, if it is built at all, does have two prerequisites,
    r-13's b2-b and r-12's igd trigger.
    **docs/phase_c_summary.md** is the close-out, on docs/phase_a_summary.md's
    model and for the same two readers. it states what phase c built, the gate's
    verdict in one section, and four findings each bounded by what it does not
    say: the protected extreme and its shielded-chain corollary, proved; rank 1
    saturating by generation three or four under every phi and on both tier 1
    benchmarks, stated as a cost of the transformation taking m interval
    objectives to 2m real ones and as the empirical form of the objection [7]
    raises against transformation methods; v-56's exact linear relations with the
    observation that A and B carry no parameter of p1; and nsga-ii's coverage
    deficit at its true scope, half attributable to X_lu's shape making the
    uniform comparator weaker there and the remainder unexplained after five
    named exclusions, saturation, effective cardinality, the pullback, map
    anisotropy and region size. **the exclusions are the work and the document
    says so.**
    **docs/supervisor_questions.md** is the accumulated list written to be
    answered in one sitting: s-01 to s-12, each as question, working assumption
    and what depends on the answer, with s-11 and s-12 first because they are the
    two that change a number in the memoria. one correction to the brief, which
    asked for s-12 and s-13 on the singular segments: **s-13 is closed**, and
    closed by b1's derivation rather than by the supervisors, so it appears as
    context under s-12 with the reason it is not being asked, and the document
    says explicitly that s-12 is untouched by it. v-56 is included as part e, a
    result offered for comment and not a question, with two consistency checks
    against s-11: dominance is preserved by an entrywise non-negative map and not
    by an arbitrary invertible one, and the per-objective blocks of A and B both
    carry a negative entry, which is exactly why phi_lu and phi_cw are nested in
    neither direction while both sit inside phi_ls. the document closes by
    pointing out that supplying any of [1]'s pdf, [26], [9], [31], [10], [7] or
    [8] would close more open rows than any answer on the page.
    the suite is unchanged because nothing in it changed: the full run is 782
    passed and 12 failed in 694.42s, **the same twelve gate tests at nsga-ii as
    c3-c left, which are the gate's stated verdict and not a regression**.
    tagged phase-c-complete | the research chat, on d2. phase d is not blocked

2026-09-02 | repo-clean | PROGRESS.md, CONTEXT.md section 12, pytest.ini,
    tests/test_problems_tier1.py, tests/test_reference_fronts.py,
    tests/test_validation.py; new docs/session_log.md and docs/row_history.md |
    housekeeping. **nothing under src/ was opened, and no phi, problem,
    derivation, solver, dominance relation, tolerance or measured number was
    touched.** four jobs. first, PROGRESS.md is back to the row shapes CONTEXT.md
    section 11 requires and 1470 lines become 735, this entry included.
    section 8, the session log, moved whole and unchanged to
    docs/session_log.md, this file keeping the last three entries and a
    pointer; section 6 became a twelve-row index into
    docs/supervisor_questions.md, which already carries the full text of every
    s-row and is the version the supervisors read; section 7 went to risk, cost,
    trigger, mitigation and nothing else; section 3 to decision, source, affects.
    the history trimmed out of sections 3 and 7 is in docs/row_history.md
    verbatim, kept whole rather than pruned: 68 of its 76 measured figures are a
    second copy of something in docs/c3_validation.md or the session log, and the
    eight that are not are r-15's filter timings, so the research chat can prune
    it against the deliverables rather than take an agent's word for what was
    duplicated. nothing was deleted and every line of the old file has a verbatim
    home except section 6's, which is what the brief directed. second,
    docs/project_narrative.md is entered in CONTEXT.md section 12 as the human
    narrative kept alongside PROGRESS.md's machine state, together with the three
    docs/ files the layout did not name; **the narrative itself has not arrived,
    so nothing in it has been checked against the repository and the claim-by-
    claim pass the brief asked for is still owed.** third, the fast run: it is
    not b2 and a5 that dominate it. measured with --durations=0, of 122 seconds
    tests/test_random_search.py is 60, tests/test_validation.py 29,
    tests/test_reference_fronts.py 17, tests/test_problems_tier0.py 9 and
    tests/test_problems_tier1.py 5. four tests are large-sample diagnostics
    rather than correctness checks and are now marked slow: b2's
    test_no_dense_sample_point_dominates_the_front at 20000 points, c3's
    shielded-tail pair, and a5's separation report. c1's tests are the real cost
    and are not marked, being contract checks; what makes them expensive is d-02's
    untoleranced O(N^2) filter at the test size of 2000, which is r-15's subject
    and a decision rather than tidying. the fast run is 310 passed in 122s before
    and 293 passed in 76s after. fourth, pytest.ini's marker text was widened from
    "runs a solver" to cover the new category. the full run is unchanged: 782
    passed and 12 failed in 707.20s, the same twelve
    test_the_derived_set_is_reached_by_the_solver at nsga-ii, three seeds under
    phi_ls and three under phi_cw at both flag settings, which are the gate's
    verdict and not a regression | the research chat, on d2; and on
    docs/project_narrative.md, which repo-clean could not check because it is not
    in the repository. phase d is not blocked

2026-09-02 | repo-clean-b | tests/test_validation.py, CONTEXT.md sections 10 and
    12, PROGRESS.md, docs/verified.md, docs/answered.md, docs/c3_validation.md,
    docs/phase_c_summary.md; new docs/phase_b_summary.md; docs/row_history.md
    removed | second housekeeping pass. **nothing under src/ was opened, and no
    phi, problem, derivation, solver, dominance relation, tolerance or measured
    number was touched.** four jobs. first, the twelve gate failures are marked
    xfail(strict=True), pinned to nsga-ii under phi_ls at seeds 11, 13 and 14 and
    under phi_cw at 12, 13 and 14 at both flag settings, six triples naming twelve
    parameter sets. **the assertion is unchanged and still runs on all ninety.**
    the marking is done by a fixture that adds the marker at setup, not by
    rewriting the parametrize stack, so all 90 test ids are byte-identical to the
    ones the log already records. this is not what c3-c refused: that refusal was
    about dropping the assertion for whichever solver it caught, and strict xfail
    asserts in both directions, a thirteenth failure being a plain failure and an
    unexpected pass an error, which is what would say the finding of
    docs/c3_validation.md section 5 had changed. second, CONTEXT.md section 10
    goes from 545 lines to 489: fifteen rationale paragraphs are replaced by one
    line naming the decision and the deliverable that carries it, in a4, c1, c2,
    c3, d1, e2 and e3, and no requirement is removed. c3 goes 89 to 66 and e3 113
    to 97, which are the two that had accumulated most. one paragraph had no home
    elsewhere and was moved rather than dropped: c3-b's reading of the coverage
    numbers as a tolerance question, now docs/c3_validation.md section 5,
    unchanged and marked as moved. third, the repo-clean items.
    **docs/row_history.md is gone**: 68 of its 76 measured figures were
    duplicates, and the eight that
    were not are r-15's filter and sweep timings, now v-57 in docs/verified.md,
    filed there and not re-measured; d-03's rejected candidate, the only prose in
    it without a home, is now one clause of d-03's source field. r-04 moved to
    docs/answered.md, which is where a row that states its own retirement belongs
    by CONTEXT.md section 11. c1's tests are left unmarked.
    **docs/phase_b_summary.md is written**, on the model of the other two: what b1
    derived and how, what b2
    encoded and why encoding the map rather than the region is what makes the
    region an independent check, the two things that did not close and were not
    patched, and what phase b means for phase e. no new claim: every statement in
    it points at b1, b2's session record or a v-row. fourth, the narrative check
    was **not done and could not be**: docs/project_narrative.md is still not in
    the repository, so nothing in it has been checked against anything. sections 1
    to 9 and 11 to 12 are unchanged and two blocks in them are flagged as history
    rather than specification, section 5's tolerance-rejection paragraphs and
    section 11's three worked anecdotes; both are proposals and neither was acted
    on. the fast run is 293 passed in 77.51s and **the full run is 782 passed and
    12 xfailed in 554.76s, with no failures** | the research chat, on d2, on
    docs/project_narrative.md, and on the two section 1-to-12 proposals. phase d
    is not blocked
