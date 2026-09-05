# phi-interval-opt: session log

moved out of PROGRESS.md section 8 in session repo-clean, 2026-09-02, unchanged
and in order. it is **canonical**: PROGRESS.md section 8 holds no entries at all
since docs-clean, which removed the copy of the last three it used to keep rather
than leave the same text in two files, and points here instead.

moved again to docs/part1/ in docs-clean, 2026-09-05, still unchanged. **every
entry names paths as they were on the day it was written and none was rewritten
in the move**, the log being append-only: an entry that says
docs/a0_framework.md means what is now docs/part1/a0_framework.md, and CONTEXT.md
section 12 carries the whole old-to-new mapping. entries also name
docs/row_history.md, which the repo-clean-b entry records as deleted and which
the mapping does not cover for that reason. part 2's entries go in
docs/part2/session_log.md and not here.

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

2026-09-02 | repo-clean-c | CONTEXT.md sections 5 and 11, PROGRESS.md | third and
    last housekeeping pass. **nothing under src/ or tests/ was opened, and no
    phi, problem, derivation, solver, dominance relation, tolerance or measured
    number was touched. no new claim was added anywhere.** the two proposals
    repo-clean-b flagged and did not act on are now taken. first, **CONTEXT.md
    section 5's two tolerance-rejection paragraphs become one line each**
    pointing at docs/a4b_dominance_tolerance.md, the measurement at parts 1.5
    and 1.6 and pymoo's no-op epsilon at part 3; the rule itself, one dominance
    relation and no tolerance, and the exactness-by-evaluation-order paragraph
    are unchanged, and both arguments survive in full in the deliverable that
    measured them. second, **section 11's three anecdotes become three clauses**,
    one on each rule's own line: a1's three unwritten width variants, c2's
    reproducibility grid never overflowing mopso's archive, and c3-e's
    uncommitted session, which was already a clause and is only tightened. the
    full stories are in docs/session_log.md at c2-b and at c-close and, for the
    first, in docs/a1_uncertainty_model.md section 1 rather than in the log.
    section 5 goes 79 lines to 70 and section 11's evidence rules 25 to 20.
    third, two corrections to PROGRESS.md against the files themselves: the
    header said docs/verified.md holds v-01 to v-46 where it holds v-01 to v-57,
    which is what the same header's highest-numbers line already said; and
    **r-15 is added to the phase d dependency list**, its trigger naming d2
    filtering large sets repeatedly and its mitigation ruling out pymoo's
    NonDominatedSorting as a speed-up, so the list d2 must respect is six rows
    and not four. fourth, **the narrative check is still owed and still could
    not be done**: docs/project_narrative.md did not arrive with this session's
    brief either and is not in the repository, so nothing in it has been checked
    against anything, while CONTEXT.md section 12 has named it since repo-clean.
    that entry is the one thing in the docs/ inventory that does not correspond
    to a file. the fast run is 293 passed and 501 deselected in 94.51s and the
    full run is 782 passed and 12 xfailed in 879.49s, the same counts as
    repo-clean-b at a longer wall time | the research chat, on d2 and on
    docs/project_narrative.md. phase d is not blocked

2026-09-02 | d2 | new src/metrics_decision.py and tests/test_metrics_decision.py;
    CONTEXT.md line 10; PROGRESS.md | the decision-space metrics, the ones
    comparable across phi, and the instrument CONTEXT.md section 10 e3 takes its
    headline number from. compute_hausdorff returns both directed distances and
    the symmetric one and they are read apart, a-to-b asking whether what was
    found is correct and b-to-a whether what exists was found; compute_coverage
    is asymmetric and is one call per direction; compute_overlap is the
    delta-neighbourhood intersection over the union, which is 2|A|/(|A|+|B|)
    whenever A is contained in B and is therefore pinned on two of the three
    pairs; cross_evaluate filters set_a's image under a second phi through
    src/random_search.py's non_dominated_indices and phi_image, neither
    reimplemented, **one filter call per call and not one per pair**, r-15, whose
    cost the module states at the sizes e1 will use, 586 to 2256 rows against
    v-57's 66 s at n = 25000. **delta has no default**, for the reason
    include_singular_segments has none, s-12, and it is refused if negative or
    not finite; no comparison anywhere rounds, snaps or admits an epsilon, d-02.
    compare_phi_on_one_sample is built on filter_one_sample_under_every_phi and
    not on the solver runs, c-close's amendment to section 10 e3: the sample is a
    pure function of the box, the budget and the seed, so the three sets differ
    only through the order, and c3-f measured that a difference read off nsga-ii
    output is confounded with nsga-ii's own phi-conditional coverage. **every
    returned pair carries a status field**, check or finding, so a table built
    from the return value cannot present either phi_ls pair as a measured
    difference: the note names r-06's containment, r-11's rounding artefact with
    its one point of 1565 and s-11's status, and the violation count is None on
    the phi_lu against phi_cw pair so that a zero there cannot be read as
    agreement. 28 tests: the three set-geometry functions on identical, disjoint
    and strictly nested sets by hand, both directed distances against an explicit
    pair loop, coverage asymmetric on a constructed case, coverage and overlap
    non-decreasing over nine deltas, b2's efficient set at distance zero from
    itself under both flag settings and bounded by a subsample's fill distance
    computed by loop, the containment as a unit test of cross_evaluate with
    s-11's status cited in place, the three index sets shown to index one array,
    the labelling, no mutation, and the shape and delta refusals. **one
    documentation correction**: CONTEXT.md's line 10, "nothing has been built
    yet. this is subpart zero.", is deleted as false by three phases and nothing
    replaces it; the before and after are in the session reply. **the narrative
    check owed since repo-clean is done**, docs/project_narrative.md having
    arrived in the repository committed by hand: eighteen items reported in the
    session reply, four wrong, seven overstated, one unsourceable and six caveats
    the deliverables carry and the narrative drops, and **nothing in that file
    was corrected**. the fast run is 321 passed and 501 deselected in 77.25s and
    the full run is 810 passed and 12 xfailed in 752.17s, the twelve being the
    strict xfails c3-c left | the research chat, on d2 and on the narrative
    report. next is e1

2026-09-02 | d2-b | docs/project_narrative.md, CONTEXT.md section 11,
    PROGRESS.md; new tag phase-b-complete | the narrative corrected against d2's
    audit of it, and the two gaps that audit exposed. **nothing under src/ or
    tests/ was opened, and no phi, problem, derivation, solver, dominance
    relation, tolerance or measured number was touched. no new claim was added to
    the narrative: every correction names the deliverable it came from.** three
    jobs. first, **all eighteen audit items are applied to
    docs/project_narrative.md**, which goes 332 lines to 502. the four the
    research chat ruled on: the phi_wu paragraph is kept and relabelled
    pre-repository history, the third phi being (f_r, half-width) with
    lambda = (0, 1) and beta = (-1/2, 1/2), removed before the seed commit, whose
    own CONTEXT.md section 4 already names the correct three, and named as the
    origin of section 11's leave-it-out rule; the five exclusions become
    docs/c3_validation.md section 5.5's own five, saturation, wasted slots, the
    pullback, anisotropy and alignment, the pullback being the one the narrative
    had dropped and the one that rules out nsga-ii simply being worse, image-space
    percentiles 0.1 to 4.9 under phi_lu against 17 to 86 and 31 to 71 under the
    two failing phi; region size leaves the exclusion list with the
    double-counting sentence, which had no source, and is replaced by what 5.5
    measures, region shape as about half the effect acting on the comparator, a
    uniform draw covering X_lu 40 per cent worse for its area, and the other half
    nsga-ii's own, excluded as a general effect by the random-search control at
    matched cardinality and not by argument; and map distortion is scoped, phi_lu
    and phi_cw differing by a similarity so that no distortion claim separates
    those two, while B is not one, condition number exactly the golden ratio
    squared, so phi_ls is genuinely sheared, with 5.4's actual exclusion beside
    it, the scaled jacobian ordering being the reverse of what a distortion story
    needs. the other fourteen as reported: the phase-b tag, saturation at
    generation three or four on p1 and dtlz2 but 13 to 21 on zdt1 with two dips,
    46 or 47 of 50 generations and not on zdt1, X_cw and X_ls with their box
    constraints and their excluded open segments, the 1/8 prediction exact in
    probability and not accurate to two decimals, the containment's narrower
    constraint after c2's amendment, the parameterized path needing no
    confirmation, and the six dropped caveats, a1's floating-point counterpart,
    r-11, r-12, r-13, the tolerance's 0.95 quantile with the 0.005 to 0.039
    margin, the full minimum path with a5, e2 and e3 off it, and the 794 tests
    with twelve failing on purpose. **the corrected file was then re-audited
    against the same deliverables**: it introduced no new unsourceable statement,
    and it corrected five things the first audit had not caught, the curve
    argument attributed to a1-b where it is a1 part 3's, "four sessions" of
    explanation where c3-d, c3-e and c3-f are three, the archive resize and its
    factor of 16 quoted without the budget 20000 they were measured at, the
    control's percentiles as 13 to 63 where c3-f measures 12.7 to 63.2, and the
    tolerance as 12 to 15 per cent of the box side where section 2.3 gives 12.0,
    14.6 and 11.6. second, **phase b is tagged**: phase-b-complete, annotated, on
    dbd32c3, b2's commit, phase b being b1 and b2 with no addendum session and no
    close-out session, so the commit that closed it is not ambiguous;
    docs/phase_b_summary.md, written after the fact in repo-clean-b, is its
    summary, and PROGRESS.md section 2 now says so. third, **CONTEXT.md section
    11's scratchpad rule is extended to documents**, that a document written
    outside the repository is not a document of this project until it is committed
    and checked against the deliverables and that section 12 does not name a file
    that does not exist; the before and after are in the session reply, and
    PROGRESS.md's file inventory now lists docs/project_narrative.md, which
    existed on disk and was missing from it. the fast run is 321 passed and 501
    deselected in 115.12s and the full run is 810 passed and 12 xfailed in 1171.68s,
    the same counts as d2 at a longer wall time, the twelve being the strict
    xfails c3-c left | the research chat, on d2-b and on the corrected narrative.
    next is e1

2026-09-02 | b2-b | src/reference_fronts.py; tests/test_reference_fronts.py and
    the four call sites in tests/test_validation.py, tests/test_runners.py,
    tests/test_random_search.py and tests/test_metrics_decision.py; new
    docs/b2b_reference_density.md; CONTEXT.md section 10 d1; PROGRESS.md | r-13's
    mitigation, built before d1 rather than deferred with it. **sampling_mode has
    no default**, for the reason include_singular_segments has none: dirichlet is
    the draw as b2 built it and farthest_point is the same draw at ten times the
    size subsampled to n_points by greedy farthest-point selection in objective
    space, and the two are two reference objects. the selection is in objective
    space because that is where igd averages; it is made at the derivation's own
    parameters, delta translating the image and moving no distance in it, so the
    caller's delta does not move which rows are kept; the singular segment is a
    linspace on a one-dimensional set and is not selected. **the derivation is
    untouched**: every kept point is still x(w) at a drawn w, the kept front is a
    subsequence of the oversample and a test walks it through, and b1 section 2.4's
    inequalities are still nowhere in src/. the factor ten is measured and not
    chosen, the coefficient of variation of the nearest-neighbour spacing of a
    1000-point front falling from 0.74, 1.13 and 1.42 at factor 1 to 0.12, 0.16 and
    0.20 at ten and 0.11, 0.11 and 0.12 at forty, ten taking at least 94 per cent
    of the available reduction at a quarter of forty's cost. **the bias is
    decision-relevant and r-13 is not retired**: on one fixed random-search front
    igd differs by 5.07 to 30.41 per cent between the two references and still by
    5.07, 12.73 and 26.20 at 20000 reference points, where r-12's flag difference
    on the same front falls from 4.30 to 0.55; the allocation minimising igd puts
    25 points of 200 more in the oversampled half under the dirichlet reference
    than under the corrected one, under every phi and both flags; 31 of 32 mirror
    pairs under phi_ls and phi_cw are ranked in opposite orders by the two
    references, with the density-free fill distance agreeing with the corrected
    one; and one pair of equal fill distance, 0.080595 against 0.080788 under
    phi_lu, is preferred one way by 22 per cent and the other by 3. everything was
    measured under both settings of the flag, r-12. 55 tests added, the mode
    parametrised into every b2 test that can afford it, the mode's own two being
    the subsequence check and the nearest-neighbour spread comparison, which is
    asserted as a comparison and never against a number; the 20000-point extreme
    test stays in the dirichlet mode, the selection costing 189 s at that size, and
    a companion test asserts the same convergence for the other mode at 200 and
    2000. the four call sites outside b2 state dirichlet explicitly with the reason
    at each, so docs/c3_validation.md's numbers are unchanged. the fast run is 370
    passed and 507 deselected in 166.42s and the full run is 865 passed and 12
    xfailed in 1268.75s | the research chat, on b2-b; then d1 if it is built, or
    e1

2026-09-03 | d1 | new src/metrics_objective.py and tests/test_metrics_objective.py;
    CONTEXT.md section 10 b2 and section 10 d1; docs/verified.md; PROGRESS.md |
    the three objective-space metrics and the truncation that makes them
    comparable across solvers. **they never rank phi**: each phi maps the same
    problem into a different space on a different scale, so the restriction is in
    the module head and in CONTEXT.md section 10 d1, and the metrics comparable
    across phi remain d2's. **pymoo's indicators where pymoo has one, not
    reimplemented**: compute_hv is pymoo.indicators.hv.HV and compute_igd is
    pymoo.indicators.igd.IGD, both left unnormalised so the reference this module
    is handed is the one the indicator is given. what they do that their names
    would not say is measured and reported rather than worked around, v-59:
    moocore's hypervolume clips at the reference point rather than refusing, the
    rows (0, 1) and (3, 0.5) against (2, 2) giving 2.0, so a row beyond the point
    is discarded silently; pymoo's igd averages over the reference points and not
    over the front, 0.0 against 7.0710678118654755 on the transposed call, which
    is the direction r-13 is about. **pymoo has no indicator for the spread this
    project means**: its SpacingIndicator is a spread of nearest-neighbour
    cityblock distances normalised by n, 0.649519052838329 where the same
    quantity normalised by n - 1 is 0.75, and no paper in scope defines it, so
    compute_spread is M_3^* of [2] definition 6 equation (19), printed page 181,
    read from the rendered page as a5 read zdt1, v-58: the euclidean norm of the
    per-column ranges, larger being wider. its limitation is asserted and not
    hidden, that it reads the extremes of each column and nothing between them,
    and whether d1 should also carry [2]'s distribution metric M_2^*, which needs
    a neighbourhood parameter the fixed signature has no room for, is left to the
    research chat. **every reference is an argument and none is built inside a
    metric**: derive_reference_point takes the rule by name,
    reference_front_nadir or reference_front_nadir_plus_range_tenth, and returns
    the rule beside the point; igd_reference returns the front with the mode, the
    flag, the seed and the size on the record, r-13 and s-12; and no parameter of
    any of the six entry points has a default, asserted by inspect over all of
    them and not by reading. **r-16 is code and no longer a recommendation**:
    truncate_to_common_cardinality is the one uniform random subsample at a
    stated seed, bitwise reproducible and a subsequence of its input, and
    common_cardinality takes the smallest front over the whole comparison and not
    per phi. **b2-b's headline is a regression test at reduced size**: 400
    reference points against 2000 and a 60-point mirror pair allocated 45 against
    15 in place of 200 and 150 against 50. the fill distance against an
    independent covering draw and the corrected reference both prefer the
    sparse-favouring front under phi_ls, 0.345423 against 0.462182, and under
    phi_cw, 0.212935 against 0.280172, while the drawn reference prefers the
    other; under phi_lu the oversampled half is also the half the front needs
    more points in and all three agree, which is section 6.3's 31 of 32 and its
    16 of 16, reproduced. v-52's cardinality effect is reproduced the same way,
    igd 0.1101, 0.0735, 0.0534 and 0.0306 and hypervolume 4.3008, 4.5243, 4.6390
    and 4.7228 at 25, 50, 100 and 290 rows of one fixed random-search front.
    **CONTEXT.md section 10 b2's signature line was wrong on both entry points**,
    missing include_singular_segments and sampling_mode on efficient_set and on
    reference_front, and is corrected with a note that neither has a default.
    b2-b and d2 move to done, their review evidenced by this session's prompt,
    which reads b2-b's correction as the reference d1 must use and d2's shape as
    settled. 52 tests added, all in the fast run. the fast run is 422 passed and
    507 deselected in 129.68s and the full run is 917 passed and 12 xfailed in
    922.89s | the research chat, on d1; then d3 or e1
2026-09-03 | d3 | new src/reporting.py and tests/test_reporting.py; CONTEXT.md
    sections 10 e1 and 10 e3; PROGRESS.md | the last instrument before the
    experiments, and the point at which a restriction that holds in the code has
    to still hold in the artefact. **the two blocks are the content and not the
    layout**: the objective-space metrics and the decision-space ones are written
    with different columns and each under the restriction it is read subject to,
    in the file itself and not in a caption, because a reader holding the csv
    alone has neither module in front of them. the objective block says that these
    compare solvers under one fixed phi and never rank phi and that all three move
    with the cardinality; the decision block says that these are the ones the
    decision space makes comparable across phi and that a row whose status is
    check has one direction fixed by a containment before any solver ran. **a row
    lacking a required field is refused with the field named and nothing is
    written**, which is one test per field per block, sixteen and seventeen of
    them: the seed count, the budget, the cardinality and a median with an
    interquartile range everywhere; the reference size, the sampling mode,
    include_singular_segments and the hypervolume reference point with the rule
    that produced it on an objective row, r-12, r-13 and s-12; delta, the scale of
    the decision box, the pair's status and d2's note and violation count on a
    decision row, r-06 and r-11. a blank cell is refused as a missing one, a field
    the block has no column for is refused because the value would not reach the
    file at all, and a metric is refused in the wrong block, so a hypervolume
    cannot be written under a line saying the numbers below it are comparable
    across phi. **the labels are not re-declared**: check and finding are imported
    from d2, the two reference-point rules from d1 and the two sampling modes from
    b2, so a table cannot state a name the module producing the number does not
    have. **the artefact is evidence and not a picture of one**: values are
    written with repr, which is the shortest text that reads back as the same
    double, read_metrics_table reads a table back to the values that were written
    and the same results written twice give the same bytes.
    containment_violations is the one field that may be empty, and its emptiness
    is d2's None, the pair no containment covers, so a zero cannot be read there
    as agreement. **every figure carries the budget, the seed count and the
    cardinality of each series inside the figure**, in the legend entry and never
    in a filename; plot_fronts takes its column pairs as an argument and chooses
    none of its own; plot_decision_sets draws b1 section 2.4's closed-form region
    behind the recovered sets where the problem is p1, in one grey with a line
    style per phi so that a region never takes a series colour, and the three
    boundaries are transcribed from b1 and checked in the tests against b1's own
    inequalities from the other side, as tests/test_reference_fronts.py checks
    b2's sampled points. no metric is computed in the module and no pixel is
    asserted in its tests. **plot_convergence is not built and nothing was added
    to c2**: src/runners.py returns a SearchResult of the seed, the budget, the
    final front and its decision vectors, pymoo's history is not requested from
    minimize, and adding the recording is a change to c2 and was not this
    session's; the module carries no stub that would look like one. **d1's two
    pymoo findings are filed where they will be needed**, both with before and
    after blocks in the session reply: CONTEXT.md section 10 e1 now requires e1 to
    assert that the hypervolume reference point dominates every front it scores
    and to fail rather than let moocore clip, v-59's rows (0, 1) and (3, 0.5)
    against the point (2, 2) giving 2.0, which is the first row's box alone; and
    CONTEXT.md section 10 e3 now requires e3 to state that the igd it reports is
    pymoo's coverage direction, the average over the reference points, and not
    [2]'s M_1^*, definition 6 equation (17), the average over the front, v-59's
    0.0 against the transposed call's 7.0710678118654755. **d1 moves to done**,
    its review evidenced by this session's prompt, which reads d1 as amended, asks
    d3 to render what d1 and d2 produce and asks for those two findings to be
    recorded. 66 tests added, all in the fast run. the fast run is 488 passed and
    507 deselected in 105.85s and the full run is 983 passed and 12 xfailed in
    586.75s | the research chat, on d3; then e1

2026-09-04 | plan-after-meeting | new docs/plan_after_meeting.md; CONTEXT.md
    sections 2, 3, 4, 6, 8, 9, 10 a5, 10 e1, 10 e3, 10 f1 to f4, 10 g1 to g4, 11
    and 12; PROGRESS.md; docs/answered.md | **planning only, no code, no
    experiment, no new module**, and nothing was implemented: no phi was added to
    the registry, a5's width functions were not changed and the newton method was
    not touched. the session after the supervisors' meeting of 2026-09-04.
    **the single claim, defended**: the choice of order relation is not a
    modelling detail, and moving between two of the framework's own named orders
    replaces most of the optimal set, calibrated exactly on p1 at 10.3 per cent of
    the union shared, reproduced on standard benchmarks and persisting on problems
    that are interval-valued at source. every other finding got a disposition and
    none is left floating.
    **the arc is the plan's spine**: read the framework, build a controlled
    problem answerable exactly, validate the measurement against that known
    answer, extend it to standard benchmarks, apply it to problems interval-valued
    at source. p1 is the calibration and not a toy, being the only place the
    measurement can be checked at all; the interval-native problems are the ending
    and not a fallback.
    **a defect not raised at the meeting**: a5 shares one width function across a
    problem's objectives, so the transformed problem's effective column count is
    **phi-dependent**, four against three on zdt1 and six against four on dtlz2,
    which confounds the study's headline pair with the transformed dimension.
    r-20, d-05, a5-b, and it precedes e2. **nothing already built is re-run.**
    **the phi search got a stopping condition** in the framework's own terms: the
    containment criterion, which in centre and half-width coordinates says any phi
    with four non-negative coefficients is a refinement of example 2.4 and carries
    nothing new, so a new order must carry a sign change. applied to [9], now in
    papers/: definitions 3.1 and 3.3 are example 2.2, definition 3.4 is example
    2.4 with a_w the half-width, equation (4.1)'s order is **excluded as a check**
    with M = [[1, 0], [1/2, 1/2]] against example 2.2, which [9]'s own proposition
    4.1 independently confirms, and definition 3.2's width-seeking order is
    **admitted** and nested with none of the three. the recommendation is neither:
    it is b1-b, the closed form along the path from example 2.4 to example 2.2 on
    p1, one session and no runs, which strengthens the calibration where a fourth
    phi would extend the exploration.
    **the prediction was corrected before it was registered**, x-01. the draft was
    already proved by b1 section 2.4 and by v-54, and two facts in it were wrong:
    delta is 1/8 since d-01, and the condition is a strict subset with a unique
    minimiser and not an interior one. the general form reproduces v-54's 1/2 and
    1/8 exactly, and analytically from the a5 forms it is **refuted for zdt1**,
    whose separable f_1 = x_1 gives example 2.2 a free-set column too, and
    **confirmed for dtlz2**, whose only free-set column under example 2.2 omits a
    variable the efficient set does not constrain. m-1 and m-2 are fixed now.
    **scope**: eleven CONTEXT.md scope statements superseded with before and after
    blocks, the four paper-level exclusions of section 9 lifted, the evidence rule
    restated and strengthened rather than relaxed. r-03 retires, s-05 is moot,
    s-08 is answered, and p-01, p-02, p-04, p-05 and p-06 all become answerable
    because [1], [7], [8], [9] and [10] are now on disk.
    **the calendar**: e1 next, f1 beside it, a5-b, e2, f2, e3, f3, then g1, g2, g3
    and g4, with delivery on 25 september and a cut order that drops stages from
    the end and never from the middle. two email-today items, the memoria's length
    and its language, both blocking g3. no test was run and none was changed; the
    suite is unchanged at 995 | the research chat, on this plan; then e1

2026-09-04 | e1 | new experiments/run_tier0.py, tests/test_run_tier0.py and
    docs/e1_tier0_run.md; new results/tier0/, holding 36 raw npz files with their
    manifest, twelve csv artefacts and eighteen figures; tests/conftest.py, which
    now puts experiments/ on the path; FASES.md, a1 corrected and an e1 entry
    added; CONTEXT.md section 10 g3; PROGRESS.md | **the calibration measured.**
    all three solvers, all three phi, p0 and p1, at seeds 11 to 15, at budget 5000
    with the whole grid repeated at 20000 as the convergence check: 36
    configurations, 180 runs, 5554 s of wall clock. three tables, all through d3's
    save_metrics_table. **the record is generated**: every number in it is read
    back out of a file the run wrote and the file and the key are named beside it,
    so the number-provenance rule of CONTEXT.md section 10 e1 holds by
    construction rather than by care, and --record-only rebuilds the record from
    the artefacts with nothing of the run in memory.
    **the instrument's error, which is what p1 exists to give.** on the pair
    nested in neither direction and at delta zero, the exact 0.394710 measures
    0.555932 at budget 5000 and 0.504177 at 20000; the exact 0.122571 measures
    0.221859 and 0.182152; the exact overlap 0.187054 measures 0.315349 and
    0.265889. every one moves toward its exact value when the budget is
    quadrupled, and the residual at 20000 is the count-for-measure bias and the
    recovered-for-derived overhang together. the containment shows in the
    measurement exactly: coverage of X_lu in X_ls and of X_cw in X_ls is 1.000000
    at both deltas and both budgets.
    **three things the plan and the schema did not meet on, decided here and
    written into the record.** d2's compute_overlap is the two covered counts over
    the two cardinalities and tends to twice the shared measure over the sum, not
    to the shared measure over the union: 0.187054 against 0.103177 on the
    headline pair, so table 1 carries d2's convention and exact_regions_p1.csv
    carries both under separate keys, and plan section b1's identification of the
    two is wrong. the noise floor is a row and not a column, labelled a check,
    d3's decision block having no column for it. and **the tolerance is not needed
    on the instrument that carries the result**: the three sets of one comparison
    are index sets over one array, so at delta zero the coverage is the exact
    shared count, and every pair is reported at delta zero as well as at one
    twentieth of the box diameter. the sweep says the second is far too generous
    at two variables, coverage of X_lu in X_cw running 0.556, 0.625, 0.726, 0.931,
    0.997, 1.000 across box fractions 0, 0.01, 0.02, 0.05, 0.1 and 0.2; it was
    fixed before the run and was not tuned after it.
    **no hypervolume is scored on p0**, one image column being constant under
    every phi, so no point can strictly dominate a row and every box has zero
    thickness; on p1 the point is derived once per phi across both budgets and
    every front was asserted to lie strictly inside it before being scored, and
    none was refused.
    **m-1 and m-2 computed and not read**, x-01 being e3's to read. two
    corrections recorded: FASES.md's a1 entry said the distinct-width variant was
    measured and discarded when a1-b measured and adopted it, and d-07 closes the
    two email-blocking items of plan section h3. 18 tests added. the full run is
    1001 passed and 12 xfailed in 739.10s | the research chat, on e1; then e3, and
    a5-b before e2

2026-09-04 | a5-b | src/problems_tier1.py; tests/test_problems_tier1.py;
    docs/a1_uncertainty_model.md, appendix a5-b; CONTEXT.md sections 10 a5, 10 e2
    and 10 g1; FASES.md; PROGRESS.md | **the tier 1 width defect corrected, and
    e2 unblocked.** every objective of zdt1 and dtlz2 shared one width function,
    so under examples 2.3 and 2.4 the image carried duplicate columns and the
    transformed problem had three effective objectives where zdt1 has four and
    four where dtlz2 has six, with none of it under example 2.2. the redundancy
    was phi-dependent and the study's headline pair is exactly those two orders.
    each objective now has its own driver, zdt1 r_1 on x_30 and r_2 on x_29,
    dtlz2 r_1, r_2 and r_3 on x_12, x_11 and x_10, **with the functional form of
    every half-width unchanged**: the drivers were chosen so that a1 part 4's
    argument applies to each verbatim, x_29 and x_30 entering zdt1's g linearly
    with the same slope 9/29 and x_10, x_11 and x_12 entering dtlz2's g
    quadratically with the same interior optimum. no variable carrying a centre
    may drive a width, which excludes x_1 on zdt1 and x_1 and x_2 on dtlz2.
    **non-coincidence is checked as a property and not as a count.** the 2m image
    columns are linear combinations of the 2m base functions with pairwise
    distinct coefficient vectors, and that follows from [1]'s determinant
    condition alone, so it holds for every admissible phi and not only the three
    in the registry; coincidence would therefore require a linear dependence among
    the base functions, and one full-rank witness matrix at written-out points
    rules it out, at smallest-to-largest singular value ratios of 8.4e-03 and
    4.1e-03. **the certificate is shown to have power**: rebuilt on a5's shared
    width it returns rank 3 and rank 4, which are exactly the effective column
    counts the defect predicts.
    **a1 part 4's slice sweep was re-run and both forms pass**, on all four of
    a1's conditions at every level: three distinct sets, none the crisp set,
    phi_lu not collapsed onto phi_ls, none saturating. no form was adjusted at any
    point. the slice gained one axis per new driver, which the change forces since
    a1's slice pins x_29, x_10 and x_11, so a middle arm was run -- a5's shared
    width on the new slice -- to isolate the form change from the slice change.
    **the harness is a1's**: a1's script was a throwaway and is not in the
    repository, and at side 61 on a1's own slice it reproduces every fraction of
    both published tables exactly, which is what makes this a re-run. the
    correction's signature is visible in the middle arm: on one slice, giving each
    objective its own driver raises zdt1's phi_ls fraction from 0.0468 to 0.3745
    and its phi_cw from 0.0356 to 0.2844 while phi_lu barely moves, which is the
    duplicate column being removed and is as phi-dependent as the defect was.
    **two decisions from the research chat recorded and applied**, d-08 and d-09:
    delta zero is the headline value everywhere and a positive delta appears only
    where two different samples are compared; and the overlap reported is jaccard,
    named jaccard, computed alongside dice rather than by changing compute_overlap.
    **x-01's outcome recorded without waiting for e3**: m-2 confirmed, m-1
    withdrawn as an instrument for conflating protection with being a good point,
    and the 1/8 measurement inconclusive at five seeds and re-registered as x-02 at
    twenty. 12 tests added. the fast run is 515 passed and 514 deselected in
    265.56s and the full run is 1017 passed and 12 xfailed in 1376.97s | the
    research chat, on a5-b; then e2

## the review chain, moved out of PROGRESS.md section 1 in e1

the current-subpart entry of PROGRESS.md section 1 had accumulated the
review evidence of every subpart before it, which is history and not
current state, so CONTEXT.md section 11 says to move it rather than to
shorten the row. it is moved here unchanged, and PROGRESS.md section 1 now
carries the current subpart alone.

    c3-f is done, its review evidenced by c-close's prompt,
    which accepts its decomposition and asks for the close-out.
    c3-c is
    done, its review evidenced by c3-d's prompt, which accepts
    its corrections and asks one diagnostic question about
    section 5; c3-d is done, its review evidenced by c3-e's
    prompt; c3-e ran and **never committed**, its session
    ending before it wrote, and its measurements are recorded
    for the first time in docs/c3_validation.md sections 5.2
    to 5.4 by c3-f, which also carries its own review of them
    in its prompt. c1 is done, its
    review evidenced by c2's prompt; c2 is done, its review evidenced by c2-b's
    prompt, which reverses one of its choices; c2-b is
    done, its review evidenced by c3's prompt, which quotes
    its findings into CONTEXT.md sections 10 c2, 10 d1 and 11;
    c3 is done, corrected in c3-b, its review evidenced by
    c3-b's prompt, which reverses its forward assertion; and
    c3-b is done, its review evidenced by c3-c's prompt, which
    corrects three things c3-b left: the missing proposition
    behind the forward floor, the sampled quality measure, and
    the tolerance; and c3-c is done, its review evidenced by
    c3-d's prompt. b1 and b2 are done and
    phase b is complete and, since d2-b, tagged
    phase-b-complete at b2's commit, its close-out
    docs/phase_b_summary.md. phase a is complete: a0, a0-b,
    a1, a1-b, a2, a3, a3-b, a4, a4-b, a5 and a-close are all
    done and docs/phase_a_summary.md is the close-out
    document

2026-09-05 | e2 | new experiments/run_tier1.py, tests/test_run_tier1.py and
    docs/e2_tier1_results.md; results/tier1/; PROGRESS.md; docs/session_log.md;
    docs/answered.md; FASES.md | **the tier 1 run.** all three solvers, all three
    phi, zdt1_interval and dtlz2_interval, the five imprecision levels of
    src/problems_tier1.py, five seeds, at budget 5000 with one convergence check
    per problem at 20000 at that module's own default level: 108 configurations,
    540 runs, 4243 seconds. ten metrics tables, one per level and kind, 72 figures
    and the record generated, so that every number in it is read back out of a
    file the run wrote.
    **there is no table 1 and the record says so rather than leaving it out**: it
    is exact and p1 only and the two benchmarks have no closed form. what stands
    in its place is e1's instrument error, read back out of results/tier0/ and not
    typed: the exact coverage of X_lu in X_cw is 0.394710 and the measurement
    gives 0.555932 at budget 5000 and 0.504177 at 20000, a relative bias of 0.408
    and 0.277. **the instrument overstates agreement**, so every measured coverage
    here is an upper bound on true sharing and a lower bound on how far the two
    orders differ, and the benchmark numbers understate the difference by a factor
    measured once on the calibration problem.
    **the headline pair on the benchmarks**, example 2.2 against example 2.4, at
    delta zero and budget 5000: on zdt1 the coverage of X_lu in X_cw runs 0.846,
    0.722, 0.660 and 0.545 across eps 0.05 to 0.50 and the reverse 0.088 to 0.160,
    with jaccard 0.087 to 0.133; on dtlz2 0.898 to 0.684 and 0.138 to 0.372, with
    jaccard 0.136 to 0.322. coverage leads and any overlap is named, d-09, and
    dice is printed beside jaccard because e1's artefacts use it.
    **the noise floor is exactly zero on both benchmarks, at every level, under
    every phi**, and that is a measurement and not an omission: two independent
    uniform samples share no point, and at thirty and at twelve variables a ball
    of one twentieth of the box diameter contains none of the other sample's
    points. the floor was swept to find where it stops being zero and it is a
    step and never an informative intermediate value: on zdt1 zero to a fifth of
    the box diameter and 0.438 to 0.896 at three tenths, on dtlz2 0.0026 to 0.0066
    at a tenth and 0.734 to 0.952 at a fifth. **so at tier 1 dimensions the floor
    of docs/plan_after_meeting.md section b1 cannot discriminate**, and the reason
    is the dimension and not the problems.
    **the delta sweep is flat**, which is the same fact from the other side: the
    headline coverage does not move at all from delta zero to a tenth of the box
    diameter on either problem, against p1 where the same range took it from 0.556
    to 0.997. d-08's dimension argument, measured rather than argued.
    **a5-b's correction checked at the run and not inherited**: the effective
    column count is 2m under every phi at every positive level on both problems,
    and at eps = 0 it is m under example 2.2 and m + 1 under the other two, which
    is what makes that level a baseline. no containment violation anywhere, r-11.
    **the rank-1 size against the population size, per configuration**, read
    through a pymoo callback that leaves the front bit-identical: nsga-ii
    saturates in every seed in all fifteen dtlz2 configurations and in twelve of
    fifteen on zdt1, mopso in twelve and in five. at eps = 0.10 nsga-ii first
    fills the slots at generation 2 to 4 on dtlz2 and 4 to 17 on zdt1, which is
    c3-d's ordering on a5-b's new forms.
    **m-2 at twenty seeds, x-02's count, computed and not read**: the median
    overhang is strictly positive on zdt1 under all three phi and on dtlz2 under
    examples 2.3 and 2.4, and exactly zero on dtlz2 under example 2.2. it is
    reported against two structures, x-01's registered one and section f3's own
    domination argument re-run on a5-b's forms, because a5-b moved which variable
    each half-width reads. **m-1 is not computed**, being withdrawn at x-01's
    outcome line. x-02's own p1 constant is not e2's and stays open.
    **r-20 retires**, its mitigation measured; **r-22 opens**, a1's slice
    fractions being grid-resolution dependent by a factor of three.
    45 tests added. the fast run is 555 passed and 519 deselected, and the full run
    is 1062 passed and 12 xfailed in 1544.19s, the twelve being c3's finding held
    in strict xfail | the research chat, on e2; then e3, with f1 and f2 beside it
2026-09-05 | e3 | new docs/e3_synthesis.md; PROGRESS.md sections 1, 2, 8 and 9;
    docs/session_log.md; FASES.md | **part 1 answered.** no experiment, no module
    and no re-run: every number is read out of a file experiments/run_tier0.py or
    experiments/run_tier1.py wrote and the file is named beside it. one number is
    derived and says so, p1's measured jaccard, from e1's dice by e2's own
    identity.
    **the comparison neither run made, which is the claim.** e1 has the exact
    numbers and no benchmarks; e2 has the benchmarks and no exact numbers. on one
    page: p1's exact jaccard on the headline pair is 0.103177 and the same
    instrument measures 0.187190 at budget 5000, a factor of 1.81, so the
    benchmarks' 0.087 to 0.133 on zdt1 and 0.136 to 0.322 on dtlz2 are upper
    bounds and the orders share less at thirty and twelve variables than the
    tables print.
    **the sign of the instrument's bias is measured to transfer and is not
    assumed**, which neither run said. if the bias were a finite-sample artefact
    rather than a property of p1, the benchmarks would have to show the same
    budget response with no exact value to fall toward. they do: quadrupling the
    budget lowers all three statistics on p1, dtlz2 and zdt1, nine of nine, by 9
    to 23 per cent against p1's 9 to 18, and on p1 that direction is known to be
    toward the truth. **the magnitude does not transfer and no correction factor
    is applied to any benchmark number anywhere.**
    **the epsilon dependence, and the half of it e2 did not have.** the coverage
    of X_lu in X_cw falls from 0.846 to 0.545 on zdt1 and 0.898 to 0.684 on dtlz2,
    so more of phi_lu's answer would be rejected under phi_cw as the imprecision
    grows; the jaccard moves the other way, and both follow from the cardinality
    column. |X_cw| is 257 on zdt1 and 1813 on dtlz2 at **every** positive level,
    because eps enters example 2.4's image only as a positive scalar on the width
    columns and a positive rescaling leaves the pareto relation unchanged, so the
    whole eps dependence of the headline pair is X_lu's. **it was predicted**, in
    docs/a1_uncertainty_model.md part 4 where the five levels were chosen, and
    confirmed here on the run's cardinality column and not on a slice fraction,
    r-22.
    **the shape, which the magnitude hides.** p1's two sets are non-nested both
    ways, 0.394710 and 0.122571; at tier 1 X_lu sits largely inside a much larger
    X_cw, 0.846 against 0.088 at zdt1 eps 0.05. same magnitude of disagreement,
    different geometry, and reporting one jaccard column would imply otherwise.
    the normalised symmetric hausdorff distance is the one statistic stable across
    two, twelve and thirty variables, 0.29 to 0.39 on the headline pair, and it is
    **uncalibrated**: exact_regions_p1.csv carries no hausdorff. neither the
    benchmark's structure nor the dimension between 12 and 30 explains the
    geometry; the width driver's alignment with a centre is what is left and one
    variant run would decide it, recorded as open.
    **the noise floor is withdrawn as measured and not omitted**, and the reason
    is structural rather than tier 1's: two independent samples share no point at
    delta zero in continuous space at any dimension, so the construction always
    needed delta > 0, and e2's sweep shows delta > 0 is a step function at these
    dimensions with no operating point. **what replaces it is in the tables**: the
    headline coverage is one sample filtered three ways, so its across-seed
    interquartile range is its complete sampling variability. the criterion is
    that the IQR be small relative to the distance from 1.0, applied per problem,
    level and pair at a stated threshold. **the eight cells in the direction that
    carries the claim all pass, ratios 0.007 to 0.037; four of the eight in the
    other direction fail, every failure on a median near 1.0 with a small X_lu,
    the worst being zdt1 eps 0.05 whose IQR is as wide as its whole distance from
    1.0 on 26 points.** so the memoria's sentence is the reverse direction: 63 to
    91 per cent of X_cw lies outside X_lu at every level on both benchmarks.
    **x-01 closed with a final outcome line.** the dtlz2 clause is confirmed and
    by a sharper comparison than it asked for: under example 2.4, on one sample
    and one seed set, the column whose free set is {x_2} measures exactly 0.000000
    with zero IQR over twenty seeds while the three eleven-variable free-set
    columns measure 0.737 to 0.843, so the condition discriminates column by
    column **inside one phi**. the zdt1 clause is **untestable**: it was registered
    against a5's forms and a5-b moved r_2 onto x_29, so section f3's own
    domination argument no longer applies to that variable and pins one fewer;
    not scored confirmed, since a registered prediction is about a named object
    and the object changed, and not scored refuted, since under a5-b's structure
    positivity holds a fortiori. zdt1 could not have decided it either way in any
    case, every phi there having a measure-zero free-set projection. m-1 stays
    withdrawn.
    **x-02 stays open** and e3 says so rather than inventing a verdict: it is a p1
    measurement, e2 ran tier 1 only, and e3 makes no run.
    **the solver question, answered apart and never mixed into the phi
    comparison.** every one of nsga-ii's twenty-four positive-imprecision
    configurations saturates rank 1 in every seed on both benchmarks under all
    three phi; the only three that do not are the crisp baseline. so those fronts
    are spread results and not convergence results, and at tier 1 there is no
    convergence measurement at all, no reference front existing and therefore no
    igd. the generation at which pressure is lost is ordered and monotone,
    phi_lu holding longest under both population solvers on both problems and
    falling as eps rises, which is c3-d's ordering on a5-b's new forms. at equal
    cardinality nsga-ii leads the hypervolume in five of six cells, read within a
    row only. **e1's tier 0 objective block answers no solver question**, being at
    full cardinality where r-16's effect exceeds the differences, and the two
    objective blocks may not be placed side by side. the coverage deficit is
    reported at its measured size with the phi-neutral control halving it, and the
    containment is used only to withhold two pairs from the evidence, which is the
    conservative direction and does not move the headline if s-11 refutes it.
    **the claim tested clause by clause.** the p1 clauses are strongly supported
    and exact; the benchmark clause is supported in its asymmetric form and not
    its symmetric one; the interval-native clause is not supported by e1 and e2
    and cannot be before f1. the attack that cannot be argued away is that the
    uncertainty model was selected for separation, a1 part 4 having rejected the
    linear half-width because it collapses two phi onto each other and a third
    onto the crisp order. **the recommended claim is conditional on the width
    being non-monotone in a driver the centres do not share, with a1's rejected
    form as the measured negative arm**, which is longer, falsifiable on a new
    problem and stronger. three figures named for g2, one of which exists.
    **noted for the history**: commit 8718150, "test runs", landed
    experiments/run_tier1.py and tests/test_run_tier1.py from outside a session on
    2026-09-05, and e2's commit 50e69bc then landed the record and results/tier1/.
    e2 is one subpart across two commits and the earlier one carries no session
    message | g1, which now has both prerequisites; g2 beside it, and f1

2026-09-05 | part1-close | new docs/part1/part1_closing.md | **the closing
    document for part 1**, landed by commit 1d2aa88 without a session log entry;
    docs-clean records it here rather than absorbing it silently, on CONTEXT.md
    section 11's rule for a session that did not write its own line. no
    experiment, no module, no re-run, no new claim and no new number: every
    figure is read out of an e1, e2 or e3 artefact and the file is named beside
    it. it is the canonical part 1 record and the document g1 lifts part 1 from.
    two statements live only there and bind g1 and g3: section 3.5's caption for
    e1's tier 0 objective block, deliberately not in the generated e1 record, and
    section 3.4's prohibition on generalising the dtlz2 column result | docs-clean,
    then g1
2026-09-05 | docs-clean | fifteen docs/ files moved to docs/part1/; new
    docs/part2/README.md; CONTEXT.md sections 10 f1, 10 g1, 10 g3, 11 and 12;
    PROGRESS.md header and section 8; FASES.md; docs/answered.md;
    docs/project_narrative.md; docs/part1/part1_closing.md,
    docs/part1/e3_synthesis.md and the three phase summaries, headers only;
    experiments/run_tier0.py and run_tier1.py | **documentation reorganised, no
    code, no run and no new claim.** part 1's record is docs/part1/: the phase
    summaries, a0 to c3, e1 to e3, part1_closing and the session log. docs/ keeps
    only what spans the whole project, verified, answered, supervisor_questions,
    project_narrative, plan_after_meeting and meeting_2026_09_04. docs/part2/ is
    created with a README naming what belongs there.
    **306 path references rewritten** and none dangles: 304 citations of a moved
    file plus the two --record output defaults in experiments/. 299 are live; the
    other 7 were inside the PROGRESS.md section 8 text this session removed as a
    duplicate, and their originals stand unchanged in this file. two sets were
    left unrewritten deliberately and both are covered by CONTEXT.md section 12's
    mapping: this file, which is append-only and whose entries name paths as they
    were written, 49 of them; and the comments under src/ and tests/, 89, which
    this session was told not to touch. **both generated records were rebuilt
    from their artefacts after the repointing and reproduce byte for byte**.
    **four overlaps decided, not listed.** the session log is canonical and
    PROGRESS.md section 8 now holds no entries, its copy of a5-b, e2 and e3
    removed rather than kept in two files, 212 lines. the three phase summaries
    and docs/project_narrative.md serve different readers and both are kept, each
    naming the other, the summary winning on a difference; that file's last
    section, written on 2026-09-02, is superseded by PROGRESS.md and
    part1_closing and is kept unedited as history with a header saying so.
    part1_closing is the settled record and e3_synthesis the working synthesis
    with the full reasoning, each header naming the other and which is which.
    docs/answered.md is canonical for a row's disposition and the deliverable for
    the derivation, with a header index naming the deliverable behind each of the
    eleven rows. nothing was reworded, renumbered or dropped.
    no test was added, changed or deleted and nothing under src/ or tests/ was
    touched. the fast run is 555 passed and 519 deselected in 154.38s and the full
    run is 1062 passed and 12 xfailed in 1250.08s, both counts identical to e2's
    | g1, which lifts part 1 from docs/part1/part1_closing.md
