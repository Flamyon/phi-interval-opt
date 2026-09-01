# c1: random search, the "referencia base" of slide 17. it is the control the
# whole comparison rests on and it is not a competitor to beat.
#
# why this module matters more than its size suggests. it is the only point in
# the design where the effect of the order is separable from the effect of the
# search. one uniform sample of the decision box can be filtered under each phi
# in turn, and the three resulting fronts then differ only through phi, because
# the search that produced the candidates was identical. in nsga-ii and mopso,
# c2, phi drives the search as well as the ordering: the population that survives
# generation one is already phi's, so every later candidate is phi's too, and a
# difference between two runs is a difference of orders and of trajectories at
# once, with no way to say how much of it is which. that is what
# filter_one_sample_under_every_phi is for, and it lives here rather than in each
# experiment so that every later comparison is filtering the same sample.
# sample_decision_space is separated from run_random_search for the same reason
# and takes no phi at all: the sample is a pure function of the box, the budget
# and the seed, so two runs under two phi at one seed search identically by
# construction and not by care at the call site.
#
# what a uniform sample of a large box is not. docs/a1_uncertainty_model.md
# part 2 and r-08: such a sample contains almost nothing near the efficient set
# of a 30-variable problem, so a separation measured on one is not evidence that
# two orders differ where it matters. that is a statement about the diagnostic a1
# was running and not about this module's job, which is to be the control at a
# stated budget; but it is why nothing here is called an efficient set and why
# every returned object is named for the run that produced it.
#
# the return contract, which c2 will use unchanged. one SearchResult per seed,
# carrying the front as (k, 2m) and the matching decision vectors as (k, n_vars),
# so analysis code treats all three solvers identically. the decision vectors are
# not optional: CONTEXT.md section 5 step 5 puts every metric comparable across
# phi in the decision space.
#
# phi arrives by name and not as a function. CONTEXT.md section 10 c1 writes the
# argument phi_fn, and d-02 has since made that impossible: a phi record carries
# two routes and the one to use is fixed by the problem's declared
# representation, so a bare callable cannot be paired with a problem and would
# have to be paired by the caller, which is the crossing a3-b removed. the record
# is looked up in phi_registry and the route taken by name, exactly as
# src/reference_fronts.py does it.
#
# no tolerance anywhere, per d-02 and CONTEXT.md section 5: non_dominated_indices
# is the ordinary pareto relation on doubles, with no rounding and no epsilon.
# it is the project's one implementation. tests/test_phi_transforms.py and
# tests/test_problems_tier1.py carry local copies which were local by design
# because this module did not exist; they could now import this one and that is a
# separate decision, not taken here.

from collections import namedtuple

import numpy as np

from phi_transforms import phi_registry

# one seed's run. n_evals is carried rather than inferred because it is the
# budget the run is compared at, CONTEXT.md section 10 c1, and a front of k rows
# says nothing about the budget that produced it.
SearchResult = namedtuple("SearchResult", ("seed", "n_evals", "front", "decision_vectors"))

# one sample and the non-dominated index set it gives under each phi. the sample
# is returned with the sets and not discarded: an index set indexing an array the
# caller no longer holds is not the isolation this function exists to provide,
# and index sets over one array are also the only form in which the containments
# of docs/a_close_containment.md can be checked, an intersection of value tuples
# being a different and weaker statement.
OneSample = namedtuple("OneSample", ("decision_vectors", "indices"))


# a uniform sample of the decision box, deliberately taking no phi
def sample_decision_space(bounds, n_evals, seed):
    lower, upper = bounds
    lower = np.asarray(lower, dtype=float)
    upper = np.asarray(upper, dtype=float)
    count = int(n_evals)
    if count < 1:
        raise ValueError("n_evals must be at least 1; got {}".format(n_evals))
    # the bounds come from the problem and are never the unit box by default,
    # CONTEXT.md section 10 c2: p0's is [-1, 1] and p1's is [-0.5, 1.5]^2.
    generator = np.random.default_rng(seed)
    return generator.uniform(lower, upper, size=(count, lower.size))


# the project's one dominance relation: the rows dominated by no other row
def non_dominated_indices(rows, block=256):
    # the ordinary pareto relation on doubles, CONTEXT.md section 5. row j
    # dominates row i when j is no worse in every column and strictly better in
    # at least one, so i is kept exactly when no j does both. two identical rows
    # dominate each other in neither direction and are both kept, which is what
    # makes duplicates and ties survive rather than being resolved by a rounding
    # step. the blocking is memory and not meaning: the comparison is against the
    # whole array either way.
    array = np.asarray(rows, dtype=float)
    keep = np.ones(len(array), dtype=bool)
    for start in range(0, len(array), block):
        chunk = array[start:start + block]
        not_worse = np.all(array[None, :, :] <= chunk[:, None, :], axis=2)
        strictly_better = np.any(array[None, :, :] < chunk[:, None, :], axis=2)
        keep[start:start + block] = ~np.any(not_worse & strictly_better, axis=1)
    return np.flatnonzero(keep)


# the 2m columns of the transformed real problem, phi applied to each objective
def phi_image(problem, pairs, record):
    # the pairing convention of src/problems_tier0.py: the problem names the
    # representation its intervals are computed in and the record is asked for
    # that route by name, so no endpoint is ever rebuilt from a centre and a
    # radius. the pairs are passed in already evaluated so that one evaluation
    # can feed every phi, which is filter_one_sample_under_every_phi's whole
    # point. the column order is (Lambda_1^T f, B_1^T f, Lambda_2^T f, ...), the
    # order src/reference_fronts.py returns and every metric assumes.
    route = getattr(record, "of_" + problem.representation)
    columns = []
    for pair in pairs:
        first, second = route(*pair)
        columns.append(first)
        columns.append(second)
    return np.stack(columns, axis=-1)


# raises unless phi is one of the three named examples of [1] the registry holds
def require_phi(phi_name):
    if phi_name not in phi_registry:
        raise ValueError(
            "unknown phi {!r}; src/phi_transforms.py implements {} and nothing "
            "else, those being the named examples 2.2, 2.3 and 2.4 of [1]"
            .format(phi_name, sorted(phi_registry)))


# raises unless seeds is a non-empty list of seeds rather than a single seed
def require_seeds(seeds):
    # CONTEXT.md section 10 c2: one run per configuration gives no variance, and
    # without variance no difference between phi can be called real. a scalar
    # seed is therefore refused here and not quietly wrapped in a list.
    if isinstance(seeds, (str, bytes)) or not hasattr(seeds, "__len__"):
        raise ValueError(
            "seeds must be a list of seeds and never a scalar; got {!r}. one run "
            "per configuration gives no variance".format(seeds))
    if len(seeds) < 1:
        raise ValueError("seeds must hold at least one seed; got an empty {}"
                         .format(type(seeds).__name__))


# one seed of random search: draw the sample, evaluate, transform, filter
def search_once(problem, record, params, n_evals, seed):
    x = sample_decision_space(problem.bounds(), n_evals, seed)
    image = phi_image(problem, problem.evaluate(x, params), record)
    keep = non_dominated_indices(image)
    return SearchResult(seed=seed, n_evals=int(n_evals), front=image[keep],
                        decision_vectors=x[keep])


# random search under one phi at a stated budget, one result per seed
def run_random_search(problem, phi_name, params, n_evals, seeds):
    require_phi(phi_name)
    require_seeds(seeds)
    record = phi_registry[phi_name]
    return [search_once(problem, record, params, n_evals, seed) for seed in seeds]


# one sample, evaluated once, filtered under every phi in the registry
def filter_one_sample_under_every_phi(problem, params, n_evals, seed):
    # the isolation described at the head of this module. the sample is drawn
    # once and the problem is evaluated once, so the three index sets index one
    # array and differ only through phi. the evaluation is shared as well as the
    # sample, which costs nothing and removes the last way the three could drift
    # apart: phi is applied to the pairs the problem returned, not to three
    # separate evaluations of it.
    x = sample_decision_space(problem.bounds(), n_evals, seed)
    pairs = problem.evaluate(x, params)
    indices = {name: non_dominated_indices(phi_image(problem, pairs, record))
               for name, record in phi_registry.items()}
    return OneSample(decision_vectors=x, indices=indices)
