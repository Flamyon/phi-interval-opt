# phi-interval-opt: the history trimmed out of PROGRESS.md's rows

moved here in session repo-clean, 2026-09-02. nothing below is new, nothing is
reworded and nothing is reinterpreted: this is PROGRESS.md sections 3 and 7 as
they stood before that session reshaped them to the four-field row that
CONTEXT.md section 11 requires, copied verbatim and in order.

why the file exists. CONTEXT.md section 11 says a row that has accumulated a
history is a filing mistake and that the fix is to move the history, never to
shorten the row. most of what follows is a second copy of material that already
sits in the deliverable that produced it, and the session reply that created this
file says, row by row, which parts those are and which parts are unique to
PROGRESS.md. it is kept whole rather than pruned so that the research chat can
prune it against the deliverables rather than take an agent's word for what was
duplicated.

the live rows are in PROGRESS.md sections 3 and 7.


## section 3 as it stood, decisions

decisions taken in the research chat and closed. a decision is reopened only with
a reason recorded here as a new entry, never by editing the old one.

format:

    d-nn, date. one sentence stating the decision.
        why: the reason.
        source: the paper, example or file it rests on, or "project judgement".
        affects: the subparts it constrains.
        status: closed, or proposed and awaiting the research chat.

d-01, 2026-08-31. p1's default delta becomes 1/8, replacing a1-b's 1/10.
    why: 1/10 was p1's only non-dyadic constant. at 1/8 the endpoint route is
    exact on a dyadic sample, 4225 of 4225 points bitwise and the width column
    carrying its true 49 distinct values against 150 at 1/10.
    source: docs/a4b_dominance_tolerance.md part 2, which verifies in exact
    integer arithmetic that delta enters every image coordinate as an additive
    constant, that no gradient or hessian moves, and that all three efficient
    index sets are identical.
    affects: a4, done; b1 and b2 inherit the new constant; a1-b's tables were
    measured at 1/10 and their efficient sets are unchanged by this.
    status: closed.

d-02, 2026-08-31, taken in the research chat and built in a3-b. every phi image is
    computed from the representation the problem declares, and one untoleranced
    dominance relation is used everywhere.
    why: it is the only option measured that needs no tolerance parameter, is
    stable over twelve decades of magnitude, and reaches inside pymoo rather than
    patching its output. the framing that made it cheap is that it is an
    evaluation-order change and not an interface change: (f_l, f_u) = M (c, r)
    with M = [[1, -1], [1, 1]] and det M = 2, so composing with phi gives the same
    phi in other coordinates and the composite determinant is 2 det phi, leaving
    admissibility exactly where [1] states it, on lam and beta.
    source: docs/a4b_dominance_tolerance.md for the measurements; the composite
    was re-derived and checked in a3-b before being implemented, on 2000 random
    rational coefficient sets, and is in CONTEXT.md section 4.
    affects: a3 gained make_phi_of_centre_radius and a paired registry, make_phi
    itself unchanged; a4 gained Problem.representation, p0 declaring "endpoints"
    and p1 "centre_radius"; a5 builds tier 1 in centre and half-width form from
    the start; c1, c2, d2 and b2 compare with no tolerance. the a4 test's rounding
    step is gone and the same grids return a1-b's counts without it.
    status: closed.

d-03, 2026-09-01, proposed in c2, reversed in c2-b before it was taken, and
    awaiting the research chat in the c2-b form. mopso_cd's archive truncation is
    drawn from the algorithm's own seeded generator, at pymoo's default
    archive_size of 200.
    why: reproducibility, which is not otherwise available. pymoo 0.6.2 adds every
    infill to the algorithm's archive, core/algorithm.py line 249, and an archive
    that passes max_size truncates itself with RandomTruncation, which is called
    with no random_state and draws from np.random.default_rng(None), a generator
    seeded from the operating system that neither minimize(seed=s) nor
    numpy.random.seed reaches. at the default size, five runs of one seed on p1
    under phi_ls gave five different fronts. nsga-ii is unaffected, holding no
    archive.
    why this form and not c2's: c2 proposed sizing the archive to the whole budget
    so the truncation was never reached, and rejected seeding it on the ground that
    an archive policy is part of the algorithm and CONTEXT.md section 10 c2 says
    pymoo is unmodified. that inverts the rule it appeals to. the archive is
    mopso's leader pool, drawn from by binary tournament in
    _select_diverse_leaders, so taking it from 200 to the 6295 rows c2 measured at
    budget 20000 changes what the search does; seeding the truncation draws the
    same uniform sample, without replacement, of the same count from the same
    archive of the same size, and changes only which generator it comes from. the
    option c2 chose modifies the behaviour and the option c2 rejected preserves it.
    the archive cannot be injected instead: pymoo's Algorithm does accept an
    archive at construction, core/algorithm.py lines 34 and 58, but MOPSO_CD
    overwrites it in _setup at line 77 and builds a fresh one every generation in
    _update_archive at lines 216 to 219, so the only place the truncation can be
    fixed is the archive _update_archive installs. src/runners.py's
    SeededArchiveMopso overrides that one method by delegation, in three lines,
    reinstalling the archive pymoo just built with a seeded truncation; no sorting,
    pruning, size or ordering of pymoo's is reimplemented. v-51.
    what it costs, measured on p1 under phi_lu at pop_size 100, seconds at budgets
    500, 1000, 2000, 4000 and 20000: seeded truncation at archive 200 gives 0.09,
    0.30, 0.82, 2.05 and 11.71; c2's resize gives 0.08, 0.32, 1.18, 6.61 and
    187.78; pymoo's unseeded default gives 0.08, 0.32, 0.82, 1.91 and 10.35. so the
    seeded form tracks pymoo's own default and is a factor of 16 cheaper than c2's
    resize at budget 20000, and it is what removes r-15's trigger.
    the candidate rejected, written out so it can be re-examined: archive_size =
    pop_size * n_gen, which cannot overflow because the archive holds at most one
    entry per evaluation. it is reproducible and it is correct; it is rejected for
    changing the leader pool and for costing roughly quadratically in the budget.
    source: project diagnostic, v-48 and v-51, with the pymoo 0.6.2 source read in
    c2 and c2-b.
    affects: c2, rebuilt this way in c2-b; c3, e1 and e2, which no longer pay the
    resize's cost; r-14 and r-15. if it is taken, CONTEXT.md section 10 c2's
    "nsga-ii and mopso from pymoo, unmodified" needs a clause for the one override,
    and only the research chat can write it: the agent's licence to edit CONTEXT.md
    is for corrections against a source, section 11, and this is a decision.
    status: proposed.


## section 7 as it stood, risks

format: r-nn | risk / cost / trigger / mitigation

r-02 | [9] of [1], where the order relations on C that (3) decomposes are defined,
    is not among the five papers in scope.
    cost: b1 has no source for a property of those relations beyond (3).
    trigger: b1 needing such a property.
    mitigation: (3) states the relation fully in terms of phi_i and the order on
    R^2, so nothing is missing today; research chat if b1 needs more.

r-03 | the pdf of [1] is not in the repository and the extracted text lacks its
    reference list and two glyphs.
    cost: section 3's provenance claims and [1]'s own citations cannot be resolved.
    trigger: already realised in a0.
    mitigation: obtain the pdf; p-01 and p-02.

r-04 | example 3.9's hypotheses fail at p0's anchor x = 0, and b1 found the
    failure wider than this row stated: the differentiability hypothesis fails
    under all three phi, p0's first half-width being |x|, and theorem 3.3 refuses
    phi-convexity under phi_lu and phi_ls as well.
    cost: realised. p0's efficient set is not reachable from the optimality
    conditions under any phi, and under phi_cw they hold and are vacuous, the
    first image coordinate being identically zero.
    trigger: fired in b1.
    mitigation: the one this row named worked for the anchor. example 3.8
    statement 3 makes x = 0 an optimal solution under all three phi, so the
    published conclusion is recovered and the procedure is validated before p1.
    the sets come from definition 3.1 applied directly. the consequence is that
    p0 is a smoke test and not a b2 fixture, docs/b1_phi_efficient_sets.md
    section 7.4, and the row retires with that reasoning.

r-05 | example 2.1 shows the class permits different coefficients per objective,
    which none of the three implemented phi use.
    cost: nothing for the experiment; a reviewer may ask why one 2x2 map is fixed
    across all objectives when the framework does not require it.
    trigger: memoria review.
    mitigation: the answer is in docs/a0_framework.md c9 and CONTEXT.md section 4.

r-06 | corrected in a-close-b, the conditional removed and the phi_cw clause
    withdrawn. as raised in a0-b this read "if an interval analogue of
    proposition 5.1 holds, the phi_lu and phi_ls efficient sets are nested rather
    than merely different", and closed "the phi_cw comparisons are unaffected,
    v-25". the first half is no longer conditional and the second half is false.
    both ND_lu and ND_cw are contained in ND_ls, exactly, for every problem, so
    two of the three pairs are nested and only phi_lu against phi_cw is not.
    cost: "the sets differ" would present a containment as a free finding on two
    pairs and not one, and one direction of delta-coverage and of overlap is
    trivially complete on both. the phi_ls against phi_cw pair is the one the
    old wording would have let through unlabelled.
    trigger: e1 or e2 producing the decision-space metrics for either phi_ls
    pair, which is r-11's trigger as well.
    mitigation: report both phi_ls pairs as checks on the containment with it
    named, never as independent findings, and take the sensitivity signal from
    phi_lu against phi_cw, which is nested in neither direction. CONTEXT.md
    section 10 e3 now states this and states that it stands on s-11.

r-08 | a construction can pass every width-versus-centre statistic on a uniform
    sample and still give phi_cw the crisp efficient set, a uniform sample of a
    large box containing almost nothing near that set.
    cost: tier 1 would measure nothing while appearing to measure something, and
    the failure would surface only at e3.
    trigger: already realised for zdt1 with half-width eps*x_n, a1 part 2.
    mitigation: a1's width driver rule plus the slice check of s-07, built as a
    test in a4 and repeated in a5.

r-09 | a1's width driver rule was derived from two benchmarks and one tier 0
    design and has not been tested outside them.
    cost: a tier 1 or portfolio problem built on it could still be degenerate in a
    way not yet seen.
    trigger: f1 constructing interval returns, a different kind of problem.
    mitigation: treat it as a working rule and not a result, and run the full a1
    diagnostic including the slice check on every new problem before use.

r-11 | the phi_lu inside phi_ls nesting is a theorem in real arithmetic and
    fails by rounding in doubles, c + r and (c - r) + 2r not being the same
    double. a5 measured one violation, dtlz2 at eps = 0.50, one point of 1565,
    where the centre (1 + g) cos(x_1 pi/2) is 6.1e-17 against a half-width of 0.5.
    cost: d2's delta-coverage and any cross-evaluation of phi_lu against phi_ls
    will show a handful of points on the wrong side of a containment that is
    exact, and a table reporting them as a finding would be reporting arithmetic.
    trigger: e1 or e2 producing the phi_lu against phi_ls decision-space metrics,
    which is r-06's trigger as well.
    mitigation: v-46 states the exact result and the measured size of the
    artefact, and a5's test asserts the containment as a band and not as an
    equality; d2 reports the pair as a check on r-06 with the artefact named.
    this is not r-07: no endpoint is built and no round trip is performed, the
    cancellation is inside phi's own first coordinate c - r, and no representation
    a problem can declare removes it.

r-12 | the reference front with the singular segments and the one without are two
    different objects, so an igd computed against one is not comparable with an
    igd computed against the other, and s-12 says the published conditions do not
    decide which is the right one.
    cost: measured, and small rather than negligible. holding the region sample
    fixed and adding the segment on top, the igd of a fixed test front moves by
    -0.63 to +5.36 per cent at 1000 reference points, -0.27 to +2.62 per cent at
    5000 and -0.11 to +1.35 per cent at 20000, the negative figures being the a4
    61 x 61 grid's non-dominated set and the positive ones a 400-point uniform
    sample's. so the choice cannot flip a comparison that is not already inside a
    few per cent at the densities e1 will use, and it can flip one that is.
    trigger: d1 computing igd and e1 tabling it, under phi_ls or phi_cw. phi_lu
    has no singular ray at all, b1 section 2.3, so the flag is a no-op there and
    the risk does not touch it.
    mitigation: include_singular_segments has no default, so the value is stated
    at the call site; it is recorded in every table beside the seed and the point
    count; and where two solvers land within a few per cent of each other under
    phi_ls or phi_cw, e1 reports the metric both ways rather than picking one.

r-13 | b2's reference front is sampled through b1's weight map, so it covers the
    derived region well but its density in objective space is the
    parametrisation's and not the front's, and igd is an average over reference
    points, so a denser region is weighted more heavily.
    cost: igd in d1 is biased by the parametrisation rather than by the solvers.
    trigger: d1 computing igd.
    mitigation: oversample through the map and subsample by farthest-point
    selection in objective space, which changes which points are kept and not the
    derivation; to be done in a b2-b before d1, and not at all if d1 is cut.
    c3 is unaffected and says so: CONTEXT.md section 10 c3 measures recovery by
    hausdorff distance in decision space, which is a maximum and insensitive to
    reference-front density.

r-14 | pymoo 0.6.2 reaches a generator no seeding call controls. any algorithm
    holding an archive truncates it with RandomTruncation once it passes max_size,
    and that call passes no random_state, so it draws from
    np.random.default_rng(None). v-48.
    cost: a run that is not bit-reproducible while appearing to be seeded, which
    would put unreproducible numbers in every table that used it. realised on
    mopso_cd at its default archive size, five runs of one seed giving five
    different fronts.
    trigger: any use of a pymoo algorithm with a bounded archive. mopso_cd today;
    a future d1 indicator or a phase f solver that carries one tomorrow.
    mitigation: d-03, in its c2-b form, draws that truncation from the algorithm's
    own seeded generator, so the archive keeps pymoo's size and behaviour and the
    generator is the only thing that changes. tests/test_runners.py asserts bitwise
    reproducibility for both solvers on every problem and every phi, and separately
    asserts that the truncation is actually reached on the one case that overflows
    at test size, p1 under phi_ls at 800 evaluations, since a reproducibility test
    that never enters the branch proves nothing about it. the general guard is that
    reproducibility is asserted for any new solver rather than assumed from a seed
    argument.

r-15 | a sweep's cost is set by mopso's archive and by the project's dominance
    filter, which is O(N^2 m) with (block x N x 2m) boolean temporaries. the
    archive half is fixed in c2-b, d-03; the filter half stands.
    cost: measured on one seed, pop_size 100, uncontended, with the c2-b archive.
    per run at budget 5000 over p1, zdt1 and dtlz2 under all three phi: nsga-ii
    0.33 to 0.50 s, mopso 1.13 to 3.21 s, random search 1.69 to 2.06 s. c2's
    figures for the same table, 2.7 to 34.2 s for mopso, were the resize's and were
    measured with three processes running; both changes matter and the resize's is
    the larger. at budget 20000 on p1 under phi_lu: nsga-ii about 2 s, mopso 11.71
    s, random search 46 to 54 s, the last being the filter and not the search.
    random_search.non_dominated_indices alone, uniform rows: n = 5000 takes 2.27 s
    at 2m = 4 and 2.40 s at 2m = 6; n = 25000 takes 66.19 s and 78.06 s; n = 50000
    takes 381.04 s and 396.01 s. peak resident memory over those six is 44, 49, 94,
    88, 119 and 144 MiB against a 33 MiB baseline, so time and not memory is the
    constraint.
    the plan the research chat has set, recorded here in c2-b: e1 and e2 both run
    their full sweeps at budget 5000, with a single budget-20000 run per problem as
    a convergence check. re-estimated against the numbers above, ten seeds: e1's
    sweep, two tier 0 problems by three phi by three solvers, is about 5 minutes,
    its convergence checks about 6, so about 11 minutes in total. e2's sweep, two
    tier 1 problems by five imprecision levels by three phi by three solvers, is
    about 25 minutes and its convergence checks about 30, so about an hour, of
    which the checks are mostly random search's filter at n = 20000 and not the
    solvers.
    trigger: e1 or e2 departing from that plan, and d1 or d2 filtering large sets
    repeatedly.
    mitigation: the budget and the seed count are stated in the plan above rather
    than discovered while a sweep runs. one reduction exists for the filter half
    and is not taken here, being a decision rather than tuning: pymoo's own
    NonDominatedSorting is O(N^2) with a better constant and v-50 measures it
    agreeing with the project's filter row for row, so the two could be used
    interchangeably where speed matters, against CONTEXT.md section 5's rule that
    the project has one implementation and not two.

r-16 | every objective-space metric moves with the number of rows a solver
    returns, and the three solvers return very different numbers: at budget 5000 on
    p1, nsga-ii returns exactly its population of 100, mopso its archive of at most
    200, and random search whatever is non-dominated, 32 to 2220 across the
    problems and phi c2 timed. igd averages, over reference points, the distance to
    the nearest front point, so a larger front scores better whether or not it
    searched better.
    cost: measured in c2-b, and larger than the differences e1 would be trying to
    detect. one fixed front, random search on p1 under phi_lu at budget 5000, 610
    rows, against b2's 1000-point reference front with include_singular_segments
    False, subsampled uniformly at random, ten draws per size, mean over the draws:
    igd is 0.1303 at k = 25, 0.0851 at 50, 0.0551 at 100, 0.0357 at 200, 0.0221 at
    500 and 0.0201 at the full 610; hypervolume against the fixed reference point
    (1.5892, 2.334, 1.174, 1.3731), the componentwise maximum of the union plus a
    tenth of each range, is 4.6845, 4.9176, 5.0433, 5.1084, 5.1595 and 5.1665 over
    the same sizes. these are the same points from the same search: the igd
    improves by a factor of 6.5 from k = 25 to the full front and by 2.7 from k =
    100 to it, and the hypervolume by 10.3 per cent, on cardinality alone. the
    spread of igd over the ten draws is 0.1013 to 0.2260 at k = 25 and 0.0217 to
    0.0223 at k = 500, so small common sizes also add noise.
    trigger: d1 computing hypervolume, igd or spread for more than one solver, and
    e1 or e3 tabling them side by side.
    mitigation: two candidate rules, and d1 implements one; c2-b measured them and
    does not build either. first, report every metric at a common truncated
    cardinality with the selection rule stated in advance. second, report
    cardinality beside every metric and never compare across solvers without it.
    the recommendation is the first, with the truncation a uniform random
    subsample at a stated seed and the common size the smallest front in the
    comparison: the confound is bigger than the signal, a factor of 2.7 in igd
    between 100 and 610 rows of one search, so the second rule leaves the reader
    discounting an effect larger than the one being reported, and a uniform
    subsample is the only selection that does not itself optimise one of the
    metrics, a crowding-distance selection being a spread rule reported beside
    spread. the second rule is kept as well and not instead: cardinality belongs in
    the table whichever way the metric is computed.

r-19 | nsga-ii's decision-space coverage of a full-dimensional efficient set is
    worse than uniform random sampling of that set at equal cardinality, under
    the two phi whose image carries a column depending on one decision variable
    alone and not under the third. this is what the c3 gate's twelve failures
    say, docs/c3_validation.md section 5, and it is a finding rather than a
    defect: nsga-ii returns no point that beats the derivation anywhere. it
    returns exactly 100 rows, which is the cardinality the tolerance's
    distribution is measured at, so the comparison needs no correction. its fill
    distance with respect to the derived region sits at the 85th to the 99th
    percentile of 1000 uniform 100-point draws under phi_ls and phi_cw, worse
    than the uniform mean in all ten measurements, and at the 33rd to the 60th
    under phi_lu, which is where a uniform draw itself sits. mopso shows the same
    tendency weaker at its own cardinality of 200, four of five above the uniform
    mean under phi_ls and two of five under phi_cw. the reading offered, and it
    is a reading and not a demonstration, is that nsga-ii spreads by crowding
    distance in the four-column image space and the coverage is measured in the
    two-dimensional decision space, and under phi_ls and phi_cw two of those four
    columns are functions of a single decision variable.
    the reading was put to a direct measurement in c3-d and does not become a
    demonstration. nsga-ii sorts 200 candidates a generation and keeps 100, and if
    rank 1 alone holds 100 of them then no survivor is chosen by dominance. it
    does: on p1 rank 1 first reaches 100 at generation 4, 3 and 3 under phi_lu,
    phi_ls and phi_cw, at every one of the five gate seeds, never falls back in
    any of them, and sits at a median of 167 to 173 of 200 over the last thirty
    generations under all three phi, with the survival sort enumerating one front
    where three to five exist. **the mechanism is present under phi_lu too**, so it cannot be
    what makes the coverage finding appear under two phi and not the third, and
    the crowding-distance reading stays a reading. the extreme points that hold an
    infinite crowding distance, 28 to 39 over the five final fronts, are enriched
    among the outside points of docs/c3_validation.md section 3.3, outside 64 to
    85 per cent of the time against a front base rate of 44 to 48, and account for
    8 to 14 per cent of them; descent from an extreme is 100 per cent of the front
    against a base rate of 100 per cent and separates nothing.
    the tier 1 numbers, at eps = 0.10 and seed 11 at the same budget, and this is
    where it matters more. dtlz2_interval transforms to 6 columns and saturates at
    generation 4, 3 and 3, then sits at a median rank 1 of 146, 155 and 153 of 200
    with three or four fronts in the sort. zdt1_interval transforms to 4 columns
    in 30 variables and is the one configuration where dominance survives a while:
    rank 1 first reaches 100 at generation 14, 13 and 21, dips back below it twice
    under phi_lu, and its median over the last thirty generations is 124, 131 and
    118. the column count is not on its own what orders the three problems, since
    p1 also transforms to four columns and saturates as fast as dtlz2 does; what
    tracks the ordering is the non-dominated fraction of the transformed image on
    a5's separation samples, 0.58, 0.79 and 0.55 on dtlz2 against 0.24, 0.52 and
    0.47 on zdt1, and three problems is not enough to assert that and it is not
    asserted.
    cost: measured, and it is a cost to the comparison and not to the pipeline.
    twelve of the gate's ninety reverse measurements fail, by 0.005 to 0.039 in a
    box of side 2, and the suite is red in twelve tests by decision,
    docs/c3_validation.md section 4.1. four times the budget removes none of it:
    at 20000 evaluations nsga-ii's worst reverse distance is 0.3315 against
    0.3309 under phi_ls and 0.2531 against 0.2503 under phi_cw.
    trigger: e3 reading any spread statistic, d1's compute_spread included, since
    that statistic is computed in the objective space where nsga-ii sorts while
    the finding is in the decision space where the result lives; e1 reporting
    a decision-space coverage or hausdorff number for nsga-ii without the
    cardinality-matched uniform draw beside it; and e1 or e2 reporting any
    population-method front without the rank-1 size against the population size,
    since a front produced under saturation is a spread and not a convergence
    result.
    mitigation: partial and stated. e1 and e3 report nsga-ii's coverage as
    measured, against a uniform draw of its own cardinality, which is the cheap
    option and the one c3-c takes, and e2 and e3 report the rank-1 size against
    the population size for every configuration, which is what c3-d adds. what is
    not decided is whether a decision-space diversity operator belongs in the
    comparison at all; that would be a change to c2 and is out of scope for a
    gate. CONTEXT.md sections 10 e2 and 10 e3 now require both to be reported.
    **halved in c3-e and c3-f, and still open.** four candidate mechanisms are
    now excluded by direct measurement, docs/c3_validation.md sections 5.2 to 5.5.
    wasted front slots: reading each run's percentile at its effective cardinality
    rather than at 100, where effective means within 0.10 of R, which is section
    3.3's own cut, moves it by 2 to 11 points of a gap of 50 and leaves all ten
    failing measurements at or above the 74th percentile. the pullback: measured in
    the 2m image space with each column normalised by its range over the image of
    R, which is what crowding distance does, nsga-ii is at the 17th to 86th and
    31st to 71st percentile under phi_ls and phi_cw, ordinary, and at the 0.1st to
    4.9th under phi_lu, exceptional, so it is not worse than uniform at what it
    optimises under either failing phi. the anisotropy of the map: under the
    column-normalised jacobian phi_lu is the anisotropic one, median singular-value
    ratio 3.97 against 1.42 and 1.45, which is the reverse of the required
    ordering, and the apparent phi_lu against phi_cw difference is an artefact of
    averaging over two different regions since v-56 makes those two maps similar.
    and the alignment of the crowding distance's axes: reading a front in another
    phi's frame with its own decision set and its own region held fixed does not
    transfer the advantage, phi_cw runs read in the lu frame sitting at 44 to 81
    against the phi_lu runs' 0.1 to 4.9, while pymoo's own crowding distance is
    equalised best in the run's own frame in all fifteen runs and to the same
    degree under every phi.
    what replaces them is a decomposition and not a mechanism, and it comes from
    the control that should have been in the first framing. random search is
    phi-neutral by construction, c1's sample being a pure function of the box, the
    budget and the seed, so the three phi filter one identical draw. at matched
    cardinality, twenty uniform 100-row subsamples of each random-search front read
    against the same k = 100 distribution, it has no deficit under any phi: 13 to
    29, 21 to 63 and 31 to 49, thirteen of the fifteen below the median, against
    nsga-ii's 33 to 60, 85 to 98 and 90 to 99. in units of the uniform mean at the
    same k it carries **exactly half** the swing from phi_lu to each of the other
    two, +0.243 of +0.483 and +0.244 of +0.485, the two halves agreeing to three
    decimals being a coincidence of two numbers and read as nothing. the control's
    half is region shape acting on the comparator, which the closed-form areas make
    concrete: |X_lu| = 0.310533, |X_ls| = 1.513401 and |X_cw| = 1, and in units of
    sqrt(|R|/k) a uniform draw covers X_lu 40 per cent worse for its area than it
    covers the other two, X_lu being a thin curved sliver and the others fat.
    **so half of r-19 is not about nsga-ii at all, and half is nsga-ii's own and
    still has no mechanism.** what is open is unchanged in kind and half the size.

r-18 | rewritten in c3-c. as raised in c3-b this said the gate's budget trend
    failed under phi_cw for both population methods and that no mechanism in
    either algorithm forces the worst member of a capped front to improve with
    budget. the truth is stronger, and it is v-54: a mechanism protects the
    offending points. under phi_ls and phi_cw the member of strictly smallest
    |x_1| is the strict minimiser of a column that depends on |x_1| alone, so
    nothing can dominate it whatever its other coordinate is, and the whole
    low-|x_1| tail is shielded by the same argument one rank at a time. a larger
    budget elects a new such member of smaller |x_1| at an x_2 that is no better
    placed: measured over 200 uniform draws at four sizes, the median smallest
    |x_1| falls by a factor of four for every factor of four in the budget while
    the mean overhang of the elected point's other coordinate does not move at
    all, 0.1226, 0.1404, 0.1334 and 0.1261. **so no monotone trend in budget is a
    property either population method has under phi_ls or phi_cw**, and c3-b's
    assertion had no mechanism behind it rather than merely lacking one.
    c3-c removes the assertion for all three solvers. not weakened, not pooled
    differently and not restricted to phi_lu: phi_lu is exactly the phi where the
    mechanism is absent, so a trend asserted there and nowhere else would be an
    assertion selected by the measurement that is supposed to judge it.
    cost: measured, and the numbers are unchanged from c3-b's, which is the check
    that this is a change of what is asserted and not of what is measured. on the
    exact measure four times the budget lowers the outside fraction for both
    population methods under phi_lu, by 2.2 and 2.1 points, and does not lower it
    under phi_ls or phi_cw for nsga-ii, 47.8 to 48.4 and 47.0 to 53.8, nor
    materially for mopso.
    trigger: any statement in e1 or the memoria that more budget buys a better
    front, and r-15's plan of a 5000 sweep with one 20000 check per problem,
    which is not contradicted but must be read as a check and never as a trend.
    what remains open under the number is the reporting question, what a
    capped-front method's budget response should be reported as at all.
    mitigation: docs/c3_validation.md section 6 reports the trend as a number on
    both measures for all three solvers, with section 1 beside it.

r-17 | retired in c3-c, r-10 in a3, r-01 in a4 and r-07 in a3-b. all four are
    in docs/answered.md with the reasoning that retired them.

