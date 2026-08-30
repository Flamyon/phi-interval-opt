# phi-interval-opt: progress

state, not specification. the specification is CONTEXT.md and this file never
repeats it. edited by the human only, from session record blocks reviewed in the
research chat.

project started 2026-08-30. nothing has been built.


## 1. where the project stands

    current phase:      a, formulation
    current subpart:    a0
    blocked on:         nothing
    files on disk:      none


## 2. subpart status

status is one of: not started, in progress, awaiting review, done, reopened.

phase a, formulation
    a0  verification pass over [1]          not started
    a1  uncertainty model                   not started
    a2  interval_math.py                    not started
    a3  phi_transforms.py                   not started
    a4  problems_tier0.py                   not started
    a5  problems_tier1.py                   not started

phase b, ground truth
    b1  phi-efficient sets, derivation      not started
    b2  reference_fronts.py                 not started

phase c, solvers
    c1  random_search.py                    not started
    c2  runners.py                          not started
    c3  validation gate                     not started

phase d, analysis
    d1  metrics_objective.py                not started
    d2  metrics_decision.py                 not started
    d3  reporting.py                        not started

phase e, experiments
    e1  tier 0 run                          not started
    e2  tier 1 run                          not started
    e3  results synthesis                   not started

phase f, part 2
    f1  data and interval construction      not started
    f2  optimization under selected phi     not started
    f3  backtest                            not started
    f4  write-up                            not started


## 3. decisions

decisions taken in the research chat and closed. a decision is reopened only with a
reason recorded here as a new entry, never by editing the old one.

format:

    d-nn, date. one sentence stating the decision.
        why: the reason.
        source: the paper, example or file it rests on, or "project judgement".
        affects: the subparts it constrains.

none yet.


## 4. verified facts

claims read from a paper in this project, with their location. a claim moves here
only once it has been checked against the source, and once here it may be relied on
without re-checking. anything not on this list is not established.

format:

    v-nn | claim | paper | location | verified in | date

none yet.


## 5. questions the papers answer

reading tasks with an owner. no working assumption is attached to these, because
the source can settle them and guessing is what this project is avoiding.

format:

    p-nn | question | owner subpart | status | answer once found

none yet.


## 6. questions only the supervisors can answer

each carries the working assumption the project proceeds on. none blocks work. if
an answer differs from the assumption, record it as a decision in section 3 and
list the subparts that have to change.

format:

    s-nn | question | working assumption | asked on | answer

none yet.


## 7. risks

format:

    r-nn | risk | what it would cost | what would trigger it | mitigation

none yet.


## 8. session log

one block per session, appended after review. never edited by the coding agent, and
never edited after it is written; a correction is a new entry.

format:

    date | subpart | files produced | outcome | next

none yet.
