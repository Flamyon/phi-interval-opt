# c3, the validation gate. this file is not a report on the solvers: it is the
# check that decides whether phase e starts. it runs all three solvers on p1
# under all three phi at the budget r-15 fixed, over a stated seed list, and
# compares the recovered decision vectors against the sets
# docs/b1_phi_efficient_sets.md derived and src/reference_fronts.py encodes.
#
# recovery is measured by hausdorff distance in the decision space and never by
# igd, CONTEXT.md section 10 c3 and r-13: b2 samples through b1's weight map,
# whose density in objective space is the parametrisation's and not the front's,
# and igd averages over reference points, so it weights a densely sampled region
# more heavily. hausdorff is a maximum and is insensitive to that.
#
# both directions are reported and neither is a summary of the other:
#   solver to reference   is what was found correct, that is, does every
#                         recovered point sit near the derived set.
#   reference to solver   was what exists found, that is, is every point of the
#                         derived set near some recovered point.
# a solver that returns one perfect point scores well on the first and badly on
# the second; a solver that scatters over the box scores the reverse. the two are
# reported per solver, per phi, per seed and are never averaged together.
#
# the tolerance and where it comes from, since a number with no derivation is not
# a stated tolerance. both sets in every comparison are finite samples of the same
# two-dimensional region, and each carries its own resolution floor:
#   h_reference   the covering radius of the derived region by b2's reference
#                 sample at reference_points. no distance to that sample can be
#                 read as smaller than this, whatever the solver did.
#   h_design      the covering radius of the derived region by a front of
#                 front_design_size points drawn uniformly from it. this is what
#                 a perfect solver returning a design-sized front achieves in the
#                 reference-to-solver direction, and it is a property of the
#                 region and not of any solver.
# the tolerance is their sum, per phi, with no free multiplier: every term is
# measured, at a size fixed in advance, on the region b1 derived. front_design_size
# is nsga-ii's population, which is the smallest front the design fixes before a
# run rather than reads off one, mopso's archive bound being 200 and random
# search's count being whatever is non-dominated.
# the sum rather than either alone: the forward direction is floored by
# h_reference and the reverse by h_design, and a gate that took one floor for
# both directions would leave no room for the other. the two floors are of the
# same order here, 0.04 to 0.14 against 0.15 to 0.21, so neither term is decoration.
#
# what this tolerance is not. it is not tight. the derived sets are
# two-dimensional regions of substantial area, b1 section 2.4, so a hundred-point
# front cannot cover one to better than about 0.15 in a box of side 2, and the
# gate is coarse for that reason and not by choice. docs/c3_validation.md reports
# the margin of every configuration so that a pass with no margin is visible as
# one.
#
# front cardinality is reported beside every number, r-16, and nothing is
# truncated to a common size. r-16 is about objective-space metrics that move
# with the number of rows; hausdorff is a maximum over two sets and truncating
# either of them here would discard real coverage, which is the d1 addition
# CONTEXT.md section 10 d1 now records.
#
# p0 is a smoke test and not a fixture, b1 section 7.4, and this file treats it as
# one: it checks that a solver finds the published anchor x = 0 and nothing more.
# under phi_lu and phi_ls p0's optimal set is the whole decision box, so finding
# the anchor is a weaker statement than it looks, and docs/c3_validation.md says so.
#
# every test that runs a solver is marked slow. the runs are cached per solver and
# phi, so the grid is executed once and not once per assertion.

import numpy as np
import pytest

from phi_transforms import phi_registry
from problems_tier0 import p0, p0_anchor, p1, p1_default_params
from random_search import non_dominated_indices, phi_image, run_random_search
from reference_fronts import efficient_set
from runners import run_mopso, run_nsga2

phi_names = ("lu", "ls", "cw")
# the budget r-15 fixed for e1 and e2, and the population c2-b timed it at. the
# gate runs at the budget the experiments will run at, because a gate passed at a
# budget nothing else uses says nothing about the runs that follow it.
gate_pop_size = 100
gate_n_gen = 50
gate_n_evals = gate_pop_size * gate_n_gen
# the stated seed list. five rather than one, CONTEXT.md section 10 c2: a single
# run gives no variance and a failure on one seed of five is a different finding
# from a failure on all five, which is what the diagnosis order in the c3 brief
# turns on.
gate_seeds = (11, 12, 13, 14, 15)
# the reference sample size, the one tests/test_runners.py already uses.
reference_points = 1000
# nsga-ii's population, the smallest front size the design fixes in advance.
front_design_size = 100
# the uniform region sample the two floors are measured on, and the draw count
# and seed that make that measurement reproducible.
tolerance_sample_size = 20000
tolerance_draws = 20
tolerance_seed = 20260903
# p0's anchor tolerance, on the same principle as p1's and in one dimension: the
# box is [-1, 1], of length 2, and a design-sized front resolves it to
# 2 / front_design_size. under phi_cw the anchor is the whole optimal set and a
# solver should do far better than this; under phi_lu and phi_ls the whole box is
# optimal and the front merely has to have a point there.
anchor_tolerance = 2.0 / front_design_size

# the three solvers behind one call signature, so no solver is tested less than
# another. random search is the control, CONTEXT.md section 10 c1, and is in the
# grid on the same terms as the other two.
solver_ids = ("random_search", "nsga2", "mopso")
run_cache = {}
tolerance_cache = {}

# b1 section 2.4's closed-form regions, written out here and not imported from
# src/. tests/test_reference_fronts.py carries the same forms for the same
# reason: a region the module also holds would make the check a file agreeing
# with itself. the two copies are the same three inequalities from the same
# section, and c2's precedent for copying a helper between test files rather than
# sharing it is followed here rather than reopened.
four_thirds = 4.0 / 3.0


# whether each point lies in the closed region b1 section 2.4 derived for one phi
def in_region(phi_name, points):
    x_1, x_2 = points[:, 0], points[:, 1]
    ls_form = 7.0 * x_1 * x_2 - 4.0 * x_1 + 12.0 * x_2 - 16.0
    if phi_name == "lu":
        return (x_1 >= 0.0) & (4.0 * x_1 - x_1 * x_2 - 20.0 * x_2 + 16.0 <= 0.0) \
            & (ls_form <= 0.0)
    if phi_name == "ls":
        return (x_1 >= 0.0) & (x_2 >= 0.0) & (x_1 <= four_thirds) \
            & (x_2 <= four_thirds) & (ls_form <= 0.0)
    return (x_1 >= 0.0) & (x_2 >= 0.0) & (x_1 <= 1.0) & (x_2 <= 1.0)


# a uniform sample of one derived region, by rejection from p1's decision box
def region_sample(phi_name, size, seed):
    # uniform on the region and not on b2's weight simplex on purpose. the weight
    # sample is dirichlet at concentration 0.3, src/reference_fronts.py, so its
    # density in the decision space is the parametrisation's; a covering radius
    # measured against it would inherit that density, and the floors here are
    # meant to be properties of the region.
    lower, upper = p1.bounds()
    generator = np.random.default_rng(seed)
    kept = []
    total = 0
    while total < size:
        block = generator.uniform(lower, upper, size=(4 * size, p1.n_vars))
        inside = block[in_region(phi_name, block)]
        kept.append(inside)
        total += len(inside)
    return np.concatenate(kept)[:size]


# the directed hausdorff distance, the largest distance from a point of a to b
def directed_hausdorff(set_a, set_b, block=256):
    # euclidean, in the decision space, which is the space common to every phi,
    # CONTEXT.md section 5 step 5. blocked for memory only: the comparison is
    # against the whole of set_b either way.
    a = np.atleast_2d(np.asarray(set_a, dtype=float))
    b = np.atleast_2d(np.asarray(set_b, dtype=float))
    worst = 0.0
    for start in range(0, len(a), block):
        chunk = a[start:start + block]
        distances = np.sqrt(np.sum((chunk[:, None, :] - b[None, :, :]) ** 2, axis=2))
        worst = max(worst, float(np.max(np.min(distances, axis=1))))
    return worst


# the covering radius of one derived region by a given point set
def covering_radius(phi_name, points, sample):
    return directed_hausdorff(sample, points)


# the two resolution floors and the gate tolerance they sum to, for one phi
def tolerance_terms(phi_name):
    if phi_name not in tolerance_cache:
        sample = region_sample(phi_name, tolerance_sample_size, tolerance_seed)
        reference, _ = efficient_set(p1, phi_name, reference_points, False)
        h_reference = covering_radius(phi_name, reference, sample)
        generator = np.random.default_rng(tolerance_seed)
        radii = [covering_radius(phi_name,
                                 sample[generator.choice(len(sample), front_design_size,
                                                         replace=False)], sample)
                 for _ in range(tolerance_draws)]
        h_design = float(np.mean(radii))
        tolerance_cache[phi_name] = (h_reference, h_design, h_reference + h_design)
    return tolerance_cache[phi_name]


# the gate tolerance for one phi, the sum of the two measured floors
def gate_tolerance(phi_name):
    return tolerance_terms(phi_name)[2]


# one solver's runs on one problem under one phi over the stated seeds, cached
def solver_runs(solver_id, problem, params, phi_name):
    key = (solver_id, problem.name, phi_name)
    if key not in run_cache:
        seeds = list(gate_seeds)
        if solver_id == "random_search":
            runs = run_random_search(problem, phi_name, params, gate_n_evals, seeds)
        elif solver_id == "nsga2":
            runs = run_nsga2(problem, phi_name, params, gate_n_gen, gate_pop_size, seeds)
        else:
            runs = run_mopso(problem, phi_name, params, gate_n_gen, gate_pop_size, seeds)
        run_cache[key] = runs
    return run_cache[key]


# the run of one solver under one phi at one seed
def one_run(solver_id, problem, params, phi_name, seed):
    runs = solver_runs(solver_id, problem, params, phi_name)
    return runs[list(gate_seeds).index(seed)]


# both hausdorff directions and both cardinalities for one recovered set
def recovery(solver_id, phi_name, seed, include_singular):
    run = one_run(solver_id, p1, p1_default_params, phi_name, seed)
    reference, _ = efficient_set(p1, phi_name, reference_points, include_singular)
    recovered = run.decision_vectors
    return {"solver_to_reference": directed_hausdorff(recovered, reference),
            "reference_to_solver": directed_hausdorff(reference, recovered),
            "k_solver": len(recovered), "k_reference": len(reference)}


# how many points of the phi_lu non-dominated set are absent from the phi_ls one
def lu_points_outside_ls(problem, points, params):
    # docs/a_close_containment.md corollary 1 makes ND_lu a subset of ND_ls
    # exactly, in real arithmetic, so this count is zero as an identity and any
    # positive value is a violation of an identity in doubles. it is a diagnostic
    # of the pipeline's arithmetic and never a result about phi, CONTEXT.md
    # section 10 c3. the sets are index sets over one evaluation of one array,
    # which is the form the containment is a statement about; an intersection of
    # value tuples would be a weaker and different claim.
    pairs = problem.evaluate(points, params)
    sets = {name: frozenset(non_dominated_indices(phi_image(problem, pairs, record)).tolist())
            for name, record in phi_registry.items()}
    return len(sets["lu"] - sets["ls"]), len(sets["lu"]), len(sets["ls"])


# the gate proper: both hausdorff directions within the derived tolerance
@pytest.mark.slow
@pytest.mark.parametrize("solver_id", solver_ids)
@pytest.mark.parametrize("phi_name", phi_names)
@pytest.mark.parametrize("seed", gate_seeds)
@pytest.mark.parametrize("include_singular", (False, True))
def test_the_recovered_set_matches_the_derived_set(solver_id, phi_name, seed,
                                                   include_singular):
    # a failure here is a result and phase e waits on it. the message carries the
    # solver, the phi, the seed, the singular flag, both distances, the tolerance
    # and both cardinalities, so that what failed and by how much is readable
    # without rerunning anything.
    measured = recovery(solver_id, phi_name, seed, include_singular)
    tolerance = gate_tolerance(phi_name)
    report = ("{} on p1 under phi_{}, seed {}, include_singular_segments {}: "
              "solver to reference {:.4f}, reference to solver {:.4f}, tolerance "
              "{:.4f}, k_solver {}, k_reference {}"
              .format(solver_id, phi_name, seed, include_singular,
                      measured["solver_to_reference"], measured["reference_to_solver"],
                      tolerance, measured["k_solver"], measured["k_reference"]))
    assert measured["solver_to_reference"] <= tolerance, report
    assert measured["reference_to_solver"] <= tolerance, report


# the published anchor x = 0 is found on p0, which is all p0 is asked
@pytest.mark.slow
@pytest.mark.parametrize("solver_id", solver_ids)
@pytest.mark.parametrize("phi_name", phi_names)
@pytest.mark.parametrize("seed", gate_seeds)
def test_the_published_anchor_is_found_on_p0(solver_id, phi_name, seed):
    # b1 section 7.4: p0 is a smoke test and not a fixture. under phi_lu and
    # phi_ls its optimal set is the whole decision box, so a front containing a
    # point near the origin is a weak statement; under phi_cw the optimal set is
    # the anchor alone and the statement is the whole answer. the check is the
    # same in all three cases and the reading is not, and
    # docs/c3_validation.md carries the distinction.
    run = one_run(solver_id, p0, None, phi_name, seed)
    distance = float(np.min(np.abs(run.decision_vectors[:, 0] - p0_anchor[0])))
    assert distance <= anchor_tolerance, (
        "{} on p0 under phi_{}, seed {}: nearest point to the anchor x = 0 is at "
        "{:.5f}, tolerance {:.5f}, k_solver {}"
        .format(solver_id, phi_name, seed, distance, anchor_tolerance,
                len(run.decision_vectors)))


# the phi_lu non-dominated set has no point outside the phi_ls one, on p1
@pytest.mark.slow
@pytest.mark.parametrize("solver_id", solver_ids)
@pytest.mark.parametrize("phi_name", phi_names)
@pytest.mark.parametrize("seed", gate_seeds)
def test_no_lu_point_falls_outside_the_ls_set_on_p1(solver_id, phi_name, seed):
    run = one_run(solver_id, p1, p1_default_params, phi_name, seed)
    outside, in_lu, in_ls = lu_points_outside_ls(p1, run.decision_vectors,
                                                 p1_default_params)
    assert outside == 0, (
        "{} on p1 under phi_{}, seed {}: {} of {} phi_lu points are absent from "
        "the phi_ls set of {}. this is numerical noise in the pipeline and never "
        "a result about phi".format(solver_id, phi_name, seed, outside, in_lu, in_ls))


# the same count on p0, the other tier 0 problem the diagnostic covers
@pytest.mark.slow
@pytest.mark.parametrize("solver_id", solver_ids)
@pytest.mark.parametrize("phi_name", phi_names)
@pytest.mark.parametrize("seed", gate_seeds)
def test_no_lu_point_falls_outside_the_ls_set_on_p0(solver_id, phi_name, seed):
    run = one_run(solver_id, p0, None, phi_name, seed)
    outside, in_lu, in_ls = lu_points_outside_ls(p0, run.decision_vectors, None)
    assert outside == 0, (
        "{} on p0 under phi_{}, seed {}: {} of {} phi_lu points are absent from "
        "the phi_ls set of {}. this is numerical noise in the pipeline and never "
        "a result about phi".format(solver_id, phi_name, seed, outside, in_lu, in_ls))


# the two settings of include_singular_segments really are two different sets
@pytest.mark.parametrize("phi_name", phi_names)
def test_the_singular_flag_changes_the_reference_set_except_under_lu(phi_name):
    # CONTEXT.md section 11's evidence rule: a test that runs both settings of a
    # flag has to demonstrate the two settings differ, or it is asserting a
    # property it cannot observe. b1 section 2.3 finds no singular ray at all for
    # phi_lu, so there the flag is a no-op and that is what is asserted; for
    # phi_ls and phi_cw the sets differ and the count of differing rows is the
    # evidence that the gate's two settings are two measurements.
    without, _ = efficient_set(p1, phi_name, reference_points, False)
    with_segment, _ = efficient_set(p1, phi_name, reference_points, True)
    assert len(without) == len(with_segment) == reference_points
    differing = int(np.count_nonzero(np.any(without != with_segment, axis=1)))
    if phi_name == "lu":
        assert differing == 0
    else:
        assert differing >= int(np.ceil(np.sqrt(reference_points)))


# the tolerance is the sum of two measured floors and neither term is negligible
@pytest.mark.parametrize("phi_name", phi_names)
def test_the_tolerance_is_the_sum_of_two_measured_floors(phi_name):
    # the derivation asserted rather than described: both terms are positive,
    # both are measured on the region and not on the weight sample, and the
    # tolerance is a fraction of the box side rather than a number of its order.
    # the box is [-0.5, 1.5]^2, of side 2, docs/a1_uncertainty_model.md.
    h_reference, h_design, tolerance = tolerance_terms(phi_name)
    assert h_reference > 0.0 and h_design > 0.0
    assert tolerance == h_reference + h_design
    assert h_reference < h_design
    assert tolerance < 0.25 * 2.0


# every point of the region sample the floors are measured on lies in the region
@pytest.mark.parametrize("phi_name", phi_names)
def test_the_region_sample_lies_in_the_derived_region(phi_name):
    sample = region_sample(phi_name, 2000, tolerance_seed)
    assert len(sample) == 2000
    assert np.all(in_region(phi_name, sample))
    points, _ = efficient_set(p1, phi_name, 500, False)
    assert np.all(in_region(phi_name, points))


# the directed hausdorff distance is a maximum of minima and is not symmetric
def test_directed_hausdorff_is_a_maximum_and_is_directional():
    # the property the whole gate rests on, checked on a case where the two
    # directions are known and different: b contains a, so every point of a is at
    # distance zero from b, while the extra point of b is at distance 3 from a.
    set_a = np.array([[0.0, 0.0], [1.0, 0.0]])
    set_b = np.array([[0.0, 0.0], [1.0, 0.0], [4.0, 0.0]])
    assert directed_hausdorff(set_a, set_b) == 0.0
    assert directed_hausdorff(set_b, set_a) == 3.0
    assert directed_hausdorff(set_a, set_a, block=1) == 0.0
