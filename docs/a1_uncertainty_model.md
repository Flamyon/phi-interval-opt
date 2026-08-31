# a1: uncertainty model decision

subpart a1 of the phase plan in CONTEXT.md section 8. document, no code in src/.

decides, once and for the whole project, how bounded imprecision enters a
problem. slide 19 of `papers/Presentacion_optimizacion_intervalar.txt` allows it
in the coefficients or in the objective; this session picks one and says why.

read for this session: CONTEXT.md in full, PROGRESS.md, docs/a0_framework.md,
and slide 19. the paper was not re-read; a0 and a0-b are relied on for [1].

decided on 2026-08-31.

all diagnostics below were run from a throwaway script in the session scratchpad
under /tmp, numpy only, nothing under src/ and nothing committed. seed 20260831
throughout. dominance is the usual Pareto relation, a dominates b iff a_i <= b_i
for all i and a_j < b_j for some j; note that this is **not** the relation [1]
prints for problem (12), see a0 ambiguity a-3, which is still open as s-03.


## what slide 19 actually says

transcribed from `papers/Presentacion_optimizacion_intervalar.txt`, lines
436-443, slide 19 of 23, "Ejemplos y benchmarks previstos":

> Problemas sencillos de una o dos variables, con imprecisión artificial en los
> coeficientes o en la función objetivo.
> Adaptación intervalar de benchmarks multiobjetivo clásicos (familias ZDT,
> DTLZ), introduciendo incertidumbre acotada ±ε en los objetivos.
> Implementación reproducible en Python (p. ej. numpy, DEAP/pymoo), comparando
> distintos φ sobre el mismo problema base.

two things follow that CONTEXT.md section 5 step 1 does not spell out.

the coefficients-or-objective choice is offered for the **tier 0** problems, the
"problemas sencillos de una o dos variables". for the **tier 1** benchmarks the
slide is more specific: "introduciendo incertidumbre acotada ±ε en los
objetivos", bounded uncertainty ±ε in the objectives.

that literal ±ε, a constant half-width, is exactly the construction part 1 tests
below, and it is degenerate. the slide's tier 1 prescription therefore cannot be
taken literally. the recommendation in this document keeps the slide's form,
imprecision in the objectives, and makes ε a function of the decision vector.
that is the smallest departure from the slide that produces a study with
anything to measure.


## part 1, the degeneracy check

hypothesis under test, from CONTEXT.md section 5 step 1: a constant width
collapses phi_lu, phi_ls and phi_cw to one order, and to the crisp order.

**verdict: confirmed**, in exact arithmetic, on both benchmarks and at both
imprecision levels tested. the three phi and the crisp order return the identical
index set, not merely sets of the same size.

but the first run of this check appeared to refute it, and the reason is a defect
this project has to carry forward. it is reported first because it changes how
the numbers below must be read.

### the floating-point artefact, and why it matters more than the result

the constant-width construction is f -> [f - eps, f + eps]. its width is 2*eps at
every point, exactly. computing that width as `fu - fl` in double precision does
not return 2*eps:

    obj 1: exact 2*eps = 0.1
            min = 0.09999999999999998
            max = 0.10000000000000009
            range = 1.110e-16   std = 4.954e-17
            count exactly equal to 2*eps : 383 / 5000
            number of distinct values    : 5
            |f| range                    : [0.0004, 0.9999]

    obj 2: exact 2*eps = 0.1
            min = 0.09999999999999964
            max = 0.10000000000000009
            range = 4.441e-16   std = 5.366e-17
            count exactly equal to 2*eps : 0 / 5000
            number of distinct values    : 2
            |f| range                    : [2.1476, 6.5051]

the cancellation error is of order machine epsilon times |f|. under phi_lu that
noise is harmless: the two image coordinates are f_l and f_u themselves and no
subtraction happens. under phi_ls and phi_cw the second image coordinate **is**
the width, so the noise becomes the entire content of that coordinate whenever
the true width is constant. the effect on the diagnostic:

    zdt1, n=30, m=2, eps=0.05, phi computed from the endpoint pair (fl, fu):
      |crisp|=16  |phi_lu|=16  |phi_ls|=30  |phi_cw|=30

    the same sample, phi computed from (centre, half-width) with no subtraction:
      |crisp|=16  |phi_lu|=16  |phi_ls|=16  |phi_cw|=16

the endpoint-mode numbers look like a discovery. phi_ls and phi_cw appear to
find nearly twice as many non-dominated points as phi_lu and the crisp order, and
the containment structure is clean and plausible. it is entirely rounding noise.

this is the worst possible failure mode for this project, and it is worth being
explicit about why. the expected symptom of a degenerate construction is that the
three phi **coincide**, which is easy to notice and is what CONTEXT.md section 5
step 1 tells the project to look for. the actual symptom, in floating point, is
that they **differ** — which reads as a positive result. a study that ran the
degenerate construction and reported "phi_ls and phi_cw recover a larger
efficient set than phi_lu" would be reporting arithmetic.

recorded as r-07. it constrains a2 and a3 and is raised for the research chat as
s-06, since the fix is a design decision about the module interface: CONTEXT.md
section 10 a3 specifies `make_phi(lam, beta)` returning "a function of (f_l, f_u)",
which is the interface that forces the cancelling subtraction.

### the literal output, exact arithmetic

    seed = 20260831, sample = 5000 uniform points, 20 centre-bins

    --------------------------------------------------------------------------
    zdt1, n=30, m=2, eps=0.05   [phi evaluated in exact mode]
    --------------------------------------------------------------------------
      width versus centre
        obj 1: width range [0.1, 0.1], span 0
               corr(centre, width) = -0.0000
               median within-centre-bin width spread = 0, as fraction of span = nan
        obj 2: width range [0.1, 0.1], span 0
               corr(centre, width) = +0.0000
               median within-centre-bin width spread = 0, as fraction of span = nan
      non-dominated subsets of the same sample
          |crisp|=16  |phi_lu|=16  |phi_ls|=16  |phi_cw|=16
          identical to phi_lu:  {'phi_ls': True, 'phi_cw': True, 'crisp': True}
      pairwise structure
          pair          |A|    |B|  |A^B|  |A^B|/|A|  |A^B|/|B|
          lu/ls          16     16     16     1.0000     1.0000
          lu/cw          16     16     16     1.0000     1.0000
          ls/cw          16     16     16     1.0000     1.0000
          phi_lu vs crisp: |A|=16 |B|=16 |A^B|=16 identical=True
          phi_ls vs crisp: |A|=16 |B|=16 |A^B|=16 identical=True
          phi_cw vs crisp: |A|=16 |B|=16 |A^B|=16 identical=True

    --------------------------------------------------------------------------
    zdt1, n=30, m=2, eps=0.5   [phi evaluated in exact mode]
    --------------------------------------------------------------------------
      width versus centre
        obj 1: width range [1, 1], span 0
               corr(centre, width) = undefined (width has exactly zero variance)
               median within-centre-bin width spread = 0, as fraction of span = nan
        obj 2: width range [1, 1], span 0
               corr(centre, width) = undefined (width has exactly zero variance)
               median within-centre-bin width spread = 0, as fraction of span = nan
      non-dominated subsets of the same sample
          |crisp|=24  |phi_lu|=24  |phi_ls|=24  |phi_cw|=24
          identical to phi_lu:  {'phi_ls': True, 'phi_cw': True, 'crisp': True}
      pairwise structure
          pair          |A|    |B|  |A^B|  |A^B|/|A|  |A^B|/|B|
          lu/ls          24     24     24     1.0000     1.0000
          lu/cw          24     24     24     1.0000     1.0000
          ls/cw          24     24     24     1.0000     1.0000
          phi_lu vs crisp: |A|=24 |B|=24 |A^B|=24 identical=True
          phi_ls vs crisp: |A|=24 |B|=24 |A^B|=24 identical=True
          phi_cw vs crisp: |A|=24 |B|=24 |A^B|=24 identical=True

    --------------------------------------------------------------------------
    dtlz2, n=12, m=3, eps=0.05   [phi evaluated in exact mode]
    --------------------------------------------------------------------------
      width versus centre
        obj 1: width range [0.1, 0.1], span 0
               corr(centre, width) = -0.0000
               median within-centre-bin width spread = 0, as fraction of span = nan
        obj 2: width range [0.1, 0.1], span 0
               corr(centre, width) = +0.0000
               median within-centre-bin width spread = 0, as fraction of span = nan
        obj 3: width range [0.1, 0.1], span 0
               corr(centre, width) = +0.0000
               median within-centre-bin width spread = 0, as fraction of span = nan
      non-dominated subsets of the same sample
          |crisp|=147  |phi_lu|=147  |phi_ls|=147  |phi_cw|=147
          identical to phi_lu:  {'phi_ls': True, 'phi_cw': True, 'crisp': True}
      pairwise structure
          pair          |A|    |B|  |A^B|  |A^B|/|A|  |A^B|/|B|
          lu/ls         147    147    147     1.0000     1.0000
          lu/cw         147    147    147     1.0000     1.0000
          ls/cw         147    147    147     1.0000     1.0000
          phi_lu vs crisp: |A|=147 |B|=147 |A^B|=147 identical=True
          phi_ls vs crisp: |A|=147 |B|=147 |A^B|=147 identical=True
          phi_cw vs crisp: |A|=147 |B|=147 |A^B|=147 identical=True

the dtlz2 eps=0.5 block is identical in structure, with |crisp| = |phi_lu| =
|phi_ls| = |phi_cw| = 152 and every set identical. the endpoint-mode counterparts
of these four blocks give, respectively, ls and cw sets of 30, 48, 525 and 373
against unchanged lu and crisp sets of 16, 24, 147 and 152.

### reading the lu/ls pair separately, per the session brief

a0-b's r-06 predicted that phi_lu and phi_ls may be nested for structural
reasons, so their coinciding says less than a coincidence involving phi_cw. that
is the right reading here. in every exact-mode block above lu, ls and cw are all
identical to crisp, so the lu/ls coincidence carries no information on its own;
what establishes the degeneracy is that **phi_cw** also coincides with crisp.
phi_cw is the order that resolves a width difference in favour of the narrower
interval, so phi_cw agreeing with the crisp order is the diagnostic fact. the
lu/ls agreement would have happened anyway.

the nesting itself does show up, clearly, once the construction is
non-degenerate: see part 2, where lu is a strict subset of ls with
|lu inter ls|/|lu| = 1.0000 and |lu inter ls|/|ls| = 0.6216. that is r-06's
prediction confirmed empirically on a case where it had room to fail.

### where the reasoning in CONTEXT.md section 5 step 1 needs care

the reasoning is right and the check confirms it. two refinements, neither a
refutation.

first, **correlation is not the right statistic** and CONTEXT.md's a1 spec asks
for it. in the constant-width case the width has zero variance, so the
correlation is undefined; numpy still returns a number because the mean of many
identical doubles is not exactly that double, and the guard for "zero variance"
fired for eps=0.5 and did not fire for eps=0.05. the two statistics that behaved
reliably in every run were the **width span** and the **median within-centre-bin
width spread**. those are reported alongside the correlation throughout this
document and should be what a4 and a5 assert on.

second, and more important, **the condition is necessary and not sufficient**,
which CONTEXT.md does say ("the necessary condition") but the check it prescribes
does not reflect. part 2 gives a construction whose width is fully independent of
its centre by every statistic, and on which phi_cw still reproduces the crisp
efficient set exactly. see "the sample diagnostic is not sufficient" below.


## part 2, the constructions

all runs in exact arithmetic, same seed and sample size, on zdt1 with n=30.

### (a) imprecision in the objective, width driven by other decision variables

F_i(x) = [f_i(x) - r_i(x), f_i(x) + r_i(x)] with r_i a function of the decision
vector. three width drivers were tried. the driver is written d(x) and
r_i = eps * d(x) with eps = 0.25 for both objectives.

    driver = mean(x_2..x_n), n=30: over the box it spans [0,1]; in this uniform
    sample it spans [0.3024, 0.6702] (std 0.0533)

      obj 1: width range [0.151179, 0.33508], span 0.183902
             corr(centre, width) = +0.0176
             median within-centre-bin width spread = 0.144937 (0.7881 of span)
      obj 2: width range [0.151179, 0.33508], span 0.183902
             corr(centre, width) = +0.5822
             median within-centre-bin width spread = 0.0908178 (0.4938 of span)
      |crisp|=16  |phi_lu|=44  |phi_ls|=44  |phi_cw|=16
      identical to phi_lu:  {'phi_ls': True, 'phi_cw': False, 'crisp': False}
          lu/ls          44     44     44     1.0000     1.0000
          lu/cw          44     16     16     0.3636     1.0000
          ls/cw          44     16     16     0.3636     1.0000
          phi_cw vs crisp: |A|=16 |B|=16 |A^B|=16 identical=True

    driver = x_n, n=30: in this uniform sample it spans [0.0001, 1.0000]
    (std 0.2864)

      obj 1: width range [5.68603e-05, 0.499986], span 0.499929
             corr(centre, width) = -0.0111
             median within-centre-bin width spread = 0.497067 (0.9943 of span)
      obj 2: width range [5.68603e-05, 0.499986], span 0.499929
             corr(centre, width) = +0.1027
             median within-centre-bin width spread = 0.496509 (0.9932 of span)
      |crisp|=24  |phi_lu|=138  |phi_ls|=222  |phi_cw|=86
      identical to phi_lu:  {'phi_ls': False, 'phi_cw': False, 'crisp': False}
          lu/ls         138    222    138     1.0000     0.6216
          lu/cw         138     86     43     0.3116     0.5000
          ls/cw         222     86     86     0.3874     1.0000

    driver = mean(x_2..x_n), n=5: sample spans [0.0883, 0.9415] (std 0.1443)

      obj 1: width span 0.426594, corr = -0.0074, within-bin spread 0.8653 of span
      obj 2: width span 0.426594, corr = +0.8971, within-bin spread 0.3075 of span
      |crisp|=10  |phi_lu|=58  |phi_ls|=58  |phi_cw|=10
      identical to phi_lu:  {'phi_ls': True, 'phi_cw': False, 'crisp': True... }
          phi_cw vs crisp: |A|=10 |B|=10 |A^B|=10 identical=True

what this shows. the driver has to have real spread **under the sampling actually
used**, not merely over the box. `mean(x_2..x_n)` with n=30 spans [0,1] over the
box but [0.30, 0.67] under uniform sampling, because the mean of 29 uniforms
concentrates; its standard deviation is 0.053. at that spread phi_cw returns the
crisp non-dominated set exactly. the same driver at n=5 has three times the
spread and still gives phi_cw = crisp. a single dedicated variable, `x_n`,
spans the full range under uniform sampling and separates all three phi.

this is a sampling-design finding as much as a construction finding, and it bears
on c1: random search on a 30-variable problem does not explore an aggregate of
29 variables, so any width built on such an aggregate is close to constant in
practice whatever it is over the box.

on the lu/ls pair, read separately as instructed: for driver = x_n the two are
distinct and **nested**, |lu inter ls|/|lu| = 1.0000 and /|ls| = 0.6216, phi_lu's
set strictly inside phi_ls's. that is the direction a0-b's v-24 records for
proposition 5.1 in the fuzzy case and that r-06 predicted might hold here. it is
an observation on one sample of one problem, not a result; s-05's working
assumption, that proposition 5.1 is a prediction to be checked and not a result
the project claims, is unchanged and is now supported rather than contradicted.

### (b) imprecision in the coefficients

the problem's constants become intervals and the objective bounds follow from
interval arithmetic. for zdt1 the constants are the 1 multiplying x_1 and the 9
inside g. writing f_1 = c_1 x_1 with c_1 in [1-d, 1+d] and the 9 as [9-d9, 9+d9],
and using that h(a, g) = g - sqrt(a g) is decreasing in a and increasing in g on
this box, so f_2^l = h(f_1^u, g^l) and f_2^u = h(f_1^l, g^u):

    zdt1 n=30, m=2, (b) d=0.1, d9=0.9
      obj 1: width range [3.76099e-05, 0.199894], span 0.199856
             corr(centre, width) = +1.0000
             median within-centre-bin width spread = 0.00992622 (0.0497 of span)
      obj 2: width range [0.595954, 1.24243], span 0.646479
             corr(centre, width) = +0.5179
             median within-centre-bin width spread = 0.351544 (0.5438 of span)
      |crisp|=25  |phi_lu|=27  |phi_ls|=27  |phi_cw|=25
          lu/ls          27     27     27     1.0000     1.0000
          lu/cw          27     25     25     0.9259     1.0000
          phi_cw vs crisp: |A|=25 |B|=25 |A^B|=25 identical=True

    zdt1 n=30, m=2, (b) d=0.25, d9=2.25
      obj 1: corr = +1.0000, within-bin spread 0.0497 of span
      obj 2: corr = +0.5454, within-bin spread 0.5184 of span
      |crisp|=18  |phi_lu|=24  |phi_ls|=24  |phi_cw|=18
          lu/cw          24     18     18     0.7500     1.0000
          phi_cw vs crisp: |A|=18 |B|=18 |A^B|=18 identical=True

objective 1 is degenerate and the reason is structural, not a matter of the
parameter values. multiplicative coefficient imprecision on f_1 = c_1 x_1 gives
centre x_1 and half-width d*x_1, so the **half-width is an exact linear function
of the centre**. correlation +1.0000 and a within-bin spread of 0.0497 of the
span, which is exactly the 1/20 bin resolution and therefore the floor of that
statistic, are the signature. this is the second case CONTEXT.md section 5 step 1
names, "a function of the centre alone".

it is not an artefact of zdt1's particular constants. any objective that is a
monomial in the imprecise coefficient has this property, and slide 19's tier 0
problems, "problemas sencillos de una o dos variables", are exactly the place
where objectives are monomials.

the consequence is visible: phi_cw returns the crisp non-dominated set exactly,
at both imprecision levels. under phi_cw the image coordinates of objective 1 are
(centre, half-width) = (x_1, d x_1), the second a monotone function of the first,
so objective 1 contributes one coordinate's worth of information instead of two.

**rejected.**

### (c) proportional imprecision in the objective, as a negative control

f -> [f(1-eps), f(1+eps)], so the half-width is eps times the centre by
construction. included to check that the diagnostic detects a degeneracy that is
not the constant-width one.

    zdt1 n=30, m=2, (c) eps=0.1
      obj 1: width span 0.199938, corr = +1.0000, within-bin spread 0.0497 of span
      obj 2: width span 0.836196, corr = +1.0000, within-bin spread 0.0496 of span
      |crisp|=20  |phi_lu|=20  |phi_ls|=20  |phi_cw|=20
      identical to phi_lu:  {'phi_ls': True, 'phi_cw': True, 'crisp': True}

    zdt1 n=30, m=2, (c) eps=0.25
      obj 1: corr = +1.0000, within-bin spread 0.0497 of span
      obj 2: corr = +1.0000, within-bin spread 0.0496 of span
      |crisp|=17  |phi_lu|=17  |phi_ls|=17  |phi_cw|=17
      identical to phi_lu:  {'phi_ls': True, 'phi_cw': True, 'crisp': True}

the diagnostic works: all three phi collapse to the crisp order, exactly, with a
width that is nowhere near constant, spanning 0.84 and 2.19 respectively. this is
the direct confirmation of the second half of CONTEXT.md section 5 step 1, the
"function of the centre alone" clause, which part 1 alone does not test.

**rejected**, and useful: it is the negative control a4 and a5 should keep as a
test case, because a construction that fails to differ from it is measuring
nothing.

### the sample diagnostic is not sufficient

this is the finding with the most consequence for the rest of the project.

construction (a) with driver = x_n passes every width-versus-centre test: span
0.4999, correlation -0.0111 and +0.1027, within-bin spread 0.9943 and 0.9932 of
the span. on a uniform random sample it separates all three phi, |phi_cw| = 86
against |crisp| = 24. by the check CONTEXT.md section 5 step 1 prescribes, it is
a good construction.

it is not. restricting to the slice where zdt1's efficient set actually lives,
x_2 .. x_{n-1} held at 0 and x_1 and x_n varied on an 81x81 grid:

    ZDT1 slice (x_2..x_29 = 0), eps = 0.25
      r = eps * x_n        (ALIGNED with g's optimum at x_n = 0)
        crisp    |eff|=   81  frac=0.0123  x_n extent [0.000, 0.000]  == crisp
        phi_lu   |eff|= 6561  frac=1.0000  x_n extent [0.000, 1.000]
        phi_ls   |eff|= 6561  frac=1.0000  x_n extent [0.000, 1.000]
        phi_cw   |eff|=   81  frac=0.0123  x_n extent [0.000, 0.000]  == crisp

phi_cw's efficient set on the slice **is** the crisp efficient set, and phi_lu
and phi_ls are the entire slice. the random-sample diagnostic reported separation
where the efficient sets coincide, and reported it because a uniform sample of a
30-dimensional box contains almost nothing near the efficient set.

the reason is alignment. zdt1's g is minimised at x_n = 0 and the half-width
eps*x_n is also minimised at x_n = 0, so under phi_cw, whose second coordinate is
the half-width, nothing trades and x_n is resolved to 0 exactly as the crisp
problem resolves it.

reversing the alignment does not fix it, it breaks the other way:

    ZDT1 slice, r = eps * (1 - x_n)  (ANTI-ALIGNED)
        crisp    |eff|=   81  frac=0.0123
        phi_lu   |eff|= 6561  frac=1.0000
        phi_ls   |eff|= 6561  frac=1.0000
        phi_cw   |eff|= 6561  frac=1.0000

now every phi returns the whole slice, because g is **linear** in x_n and the
width is linear in x_n, so the trade-off between them has no interior resolution
and every value of x_n is non-dominated.

dtlz2 behaves differently and better, because its g is quadratic in x_n with an
interior minimum at 0.5:

    DTLZ2 slice (x_2 = 0.5, x_3..x_11 = 0.5), eps = 0.25
      r = eps * x_n        (g's optimum is interior at x_n = 0.5)
        crisp    |eff|=   81  frac=0.0123  x_n extent [0.500, 0.500]  == crisp
        phi_lu   |eff|= 3133  frac=0.4775  x_n extent [0.000, 1.000]
        phi_ls   |eff|= 4847  frac=0.7388  x_n extent [0.000, 1.000]
        phi_cw   |eff|= 3321  frac=0.5062  x_n extent [0.000, 0.500]

all three distinct, none trivial, none equal to crisp, and phi_cw's band in x_n
is [0, 0.5], bounded strictly between the width's optimum at 0 and g's at 0.5.

**the rule this yields**, and it is the operative content of this session:

> a width driver must (i) be a decision variable the crisp objectives actually
> depend on, (ii) have its width-optimum different from the crisp problem's
> optimum in that variable, and (iii) meet the crisp objective's dependence with
> enough curvature on one side or the other that the trade-off resolves in the
> interior rather than filling the whole range.
>
> and it must be checked on the slice where the efficient set lives, not only on
> a uniform sample of the box.

recorded as r-08. the additional check is proposed for a4 and a5 as s-07.


## recommendation

**construction (a): imprecision in the objective, with a half-width that is a
function of the decision vector.** rejected: (b) coefficient imprecision, and (c)
proportional imprecision. the literal reading of slide 19's tier 1 prescription,
a constant ±eps, is rejected by part 1.

the reasons, in order of weight:

    (b) makes the half-width an exact linear function of the centre for any
    objective that is a monomial in the imprecise coefficient, which is the
    degeneracy CONTEXT.md section 5 step 1 names. it is worst on precisely the
    small one- and two-variable problems slide 19 asks for. phi_cw returned the
    crisp efficient set exactly at both levels tested.

    (a) puts the half-width under independent control. it is the only one of the
    three where the (centre, width) image is genuinely two-dimensional, with
    within-centre-bin width spread above 0.99 of the span for a well-chosen
    driver.

    (a) is also what slide 19 asks for at tier 1, "incertidumbre acotada +-eps en
    los objetivos". the departure is only that eps becomes eps times a function of
    x rather than a constant, which is the minimum change that makes the study
    non-vacuous.

    the crisp problem is recoverable as a limiting case under (a) and is not
    under (b). setting eps = 0 in (a) gives r == 0, F_i = [f_i, f_i], and the
    published benchmark exactly. under (b) the coefficient interval collapsing to
    a point recovers the crisp problem too, but the path to it changes the
    objective values themselves rather than only their width, so the sweep is not
    a sweep in one parameter of one problem.

**these two constructions are not tied and the choice is not brought to the
research chat.** (b) fails a stated condition of CONTEXT.md section 5 step 1 on
its own numbers. what is brought to the research chat is the width-driver rule
above and the two checks it implies, s-06 and s-07.


## part 3, problem p1

### the design rule the six image coordinates impose

writing each interval objective as centre c_i and half-width r_i, so
f_i^l = c_i - r_i and f_i^u = c_i + r_i, the image coordinates required by
theorem 3.3 and example 3.9 of [1] (a0 v-12, v-15) are, per objective:

    phi_lu   Lam^T f = f^l = c - r        B^T f = f^u = c + r
    phi_ls   Lam^T f = f^l = c - r        B^T f = f^u - f^l = 2r
    phi_cw   Lam^T f = (f^l + f^u)/2 = c  B^T f = (f^u - f^l)/2 = r

so the set of functions that must be convex across all three phi is
{c - r, c + r, 2r, c, r}, and since c + r = (c - r) + 2r and c = (c-r) + r, that
set is generated by two:

> **all six image coordinates are convex for all three phi if and only if
> (c - r) is convex and r is convex.**

the cheapest way to satisfy it is to make the half-width **affine**, since an
affine r is convex and c - r is then convex whenever c is. that was the first
design tried and it fails for a different reason, given below, so p1 uses a
convex quadratic r with the curvature bounded so that c - r stays convex.

### four designs that do not work, and why

these are recorded because each fails for a reason that constrains the next
attempt, and because a4 should not rediscover them.

on an 81x81 grid of [0,1]^2 with rho = 0.5, writing p for rho:

    P1-A  c1=x1^2, r1=p*x2 ; c2=(x1-1)^2, r2=p*(1-x2)
           crisp/lu/ls/cw all 6561 of 6561: every phi returns the whole box.
    P1-B  c1=x1^2, r1=p*x2 ; c2=(x1-1)^2+x2^2, r2=p*(1-x2)
           lu 4162, ls 6561, cw 6561: ls and cw return the whole box.
    P1-C  c1=x1^2+x2^2, r1=p*x2 ; c2=(x1-1)^2+x2^2, r2=p*(1-x2)
           lu 1701, ls 6561, cw 6561: ls and cw return the whole box.
    P1-D  c1=x1^2, r1=p*x2 ; c2=(x1-1)^2, r2=p*x2
           lu 6561, ls 6561, cw 81: lu and ls return the whole box.

three obstructions, each established by these runs:

    if the two half-widths are **opposed** in the width variable, one increasing
    and one decreasing, then the width columns alone make every pair of points
    with different x2 incomparable, and phi_ls and phi_cw return the whole box.
    that kills A, B and C.

    if the half-widths are **aligned** and the centres do not respond to the
    width variable, phi_lu and phi_ls return the whole box, because (c-r, c+r)
    conflict in any direction that moves r and leaves c alone. that kills D and A.

    if the centres respond to the width variable **monotonically**, phi_lu and
    phi_ls coincide exactly. a further family, c1 = x1^2+x2^2,
    c2 = (x1-1)^2+x2^2, r = p*x2 with three variants of r2 and rho in {0.5, 0.8},
    gave |lu| = |ls| with identical index sets in all six configurations. a
    second family with the centres *decreasing* in x2, c = x^2+(1-x2)^2 and
    c = x1^2-x2, gave ls and cw the whole box in all eight configurations.

what is left is the one structure that avoids all three: **the centre's optimum
and the half-width's optimum in the width variable must both be interior, and
different**. that requires the half-width to be non-monotone in the width
variable, hence convex quadratic, with curvature small enough to keep c - r
convex.

### p1, proposed

    decision box     x = (x_1, x_2) in [-0.5, 1.5] x [-0.5, 1.5]

    centres          c_1(x) = x_1^2       + (x_2 - 1)^2
                     c_2(x) = (x_1 - 1)^2 + (x_2 - 1)^2

    half-widths      r_1(x) = r_2(x) = rho * x_2^2 + delta
                     with rho = 1/4 and delta = 1/10

    objectives       F_i(x) = [ c_i(x) - r_i(x),  c_i(x) + r_i(x) ],  i = 1, 2

on the box the half-width runs over [0.1000, 0.6625] and is strictly positive
everywhere, so f^l <= f^u holds with strict inequality and no interval ever
degenerates.

**the box is not the unit box, and the reason is example 3.9.** condition (15) of
[1] is unconstrained stationarity, the vanishing of the gradient of a weighted
sum of the image coordinates (a0 v-17); it carries no constraint multipliers,
unlike examples 3.4 to 3.7. so b1 can only apply example 3.9 at points in the
**interior** of the feasible set. the efficient set of this problem has x_1 in
[0, 1], fixed by the two centres' minima at 0 and 1, and x_2 in [0, 4/3], fixed
by the four stationary points listed below. [-0.5, 1.5]^2 is the smallest
symmetric box with a margin on both, and the grid check below confirms every
phi's efficient set is interior to it. on [0,1]^2 the efficient set would touch
three faces and example 3.9 would be unavailable to b1 at those points.

the choice rho = 1/4 is also forced by interiority rather than taste. the
stationary point of c - r in x_2 is at 1/(1 - rho); at rho = 1/2 that is x_2 = 2,
outside any reasonable box, and the grid check at rho = 1/2 returned a phi_lu
efficient set running to the face x_2 = 1.5. at rho = 1/4 it is 4/3, interior.
rho must also stay below 1 for c - r to be convex at all.

### the six image coordinates, written out

for objective 1. objective 2 is identical with x_1 replaced by x_1 - 1
throughout, so the verdicts are the same.

    phi_lu, lambda = (1, 0), beta = (0, 1)

      Lam^T f = 1*f^l + 0*f^u = f^l
              = x_1^2 + (x_2 - 1)^2 - (1/4) x_2^2 - 1/10
              = x_1^2 + (3/4) x_2^2 - 2 x_2 + 9/10
        differentiable: yes, polynomial, C-infinity on R^2.
        convex: yes. Hessian = diag(2, 3/2), constant, min eigenvalue 3/2 > 0.

      B^T f   = 0*f^l + 1*f^u = f^u
              = x_1^2 + (x_2 - 1)^2 + (1/4) x_2^2 + 1/10
              = x_1^2 + (5/4) x_2^2 - 2 x_2 + 11/10
        differentiable: yes, polynomial.
        convex: yes. Hessian = diag(2, 5/2), min eigenvalue 2 > 0.

    phi_ls, lambda = (1, 0), beta = (-1, 1)

      Lam^T f = f^l, as above.
        differentiable: yes.   convex: yes, Hessian diag(2, 3/2).

      B^T f   = -1*f^l + 1*f^u = f^u - f^l = 2 r_1
              = (1/2) x_2^2 + 1/5
        differentiable: yes, polynomial.
        convex: yes. Hessian = diag(0, 1), min eigenvalue 0, positive
        semidefinite. convex but not strictly so, and constant in x_1.

    phi_cw, lambda = (1/2, 1/2), beta = (-1/2, 1/2)

      Lam^T f = (1/2) f^l + (1/2) f^u = c_1
              = x_1^2 + (x_2 - 1)^2
        differentiable: yes, polynomial.
        convex: yes. Hessian = diag(2, 2), min eigenvalue 2 > 0.

      B^T f   = -(1/2) f^l + (1/2) f^u = r_1
              = (1/4) x_2^2 + 1/10
        differentiable: yes, polynomial.
        convex: yes. Hessian = diag(0, 1/2), min eigenvalue 0, positive
        semidefinite. convex but not strictly so, and constant in x_1.

all six are polynomials of degree 2, hence differentiable to every order on the
whole plane, so the differentiability hypothesis of example 3.9 holds on the box
with room to spare. all six have constant positive semidefinite Hessians, so
theorem 3.3's hypothesis holds globally and not merely at a point, which also
gives remark 2.2's pointwise form everywhere (a0 v-12, v-13). that is the
viability check the session brief asks for; **the efficient set itself is not
derived here and is b1's work.**

the verdicts were confirmed numerically as well as by hand, both by the minimum
eigenvalue of the analytic Hessian and by a 20000-chord midpoint convexity test
over the box:

    coordinate                              min eig(Hessian)  max chord violation  convex?
    phi_lu  Lam^T f  = f_l  = c - r                1.5000            -2.12e-06  yes
    phi_lu  B^T f    = f_u  = c + r                2.0000            -2.76e-06  yes
    phi_ls  Lam^T f  = f_l                         1.5000            -2.12e-06  yes
    phi_ls  B^T f    = f_u - f_l = 2r              0.0000            -5.72e-10  yes
    phi_cw  Lam^T f  = (f_l+f_u)/2 = c             2.0000            -2.57e-06  yes
    phi_cw  B^T f    = (f_u-f_l)/2 = r             0.0000            -2.86e-10  yes

a negative chord violation is convexity holding with slack; the two zero-eigenvalue
rows are the width coordinates, which are convex and affine in x_1.

### p1, viability numbers

61x61 grid on [-0.5, 1.5]^2, 3721 points, exact arithmetic.

    half-width range on the box: [0.1000, 0.6625]  (strictly positive: True)

    obj 1: width span 1.1250, corr(centre,width) = -0.4018,
           median within-centre-bin width spread = 1.0872 (0.966 of span)
    obj 2: width span 1.1250, corr(centre,width) = -0.4018,
           median within-centre-bin width spread = 1.0872 (0.966 of span)

    set        |eff|   frac     x1 extent        x2 extent      interior to box?
    crisp         31  0.0083  [ 0.000, 1.000]  [ 1.000, 1.000]      True
    phi_lu       527  0.1416  [ 0.000, 1.000]  [ 0.800, 1.333]      True
    phi_ls      1271  0.3416  [ 0.000, 1.000]  [ 0.000, 1.333]      True
    phi_cw       961  0.2583  [ 0.000, 1.000]  [ 0.000, 1.000]      True

    lu subset of ls: True    |lu|/|ls| = 0.415
    lu/ls: |A|=527  |B|=1271 |A^B|=527 in-A=1.000 in-B=0.415
    lu/cw: |A|=527  |B|=961  |A^B|=217 in-A=0.412 in-B=0.226
    ls/cw: |A|=1271 |B|=961  |A^B|=961 in-A=0.756 in-B=1.000

the width is independent of the centre by the statistic that matters: within a
centre bin the width still ranges over 96.6% of its full span. the correlation is
-0.4018, which is a good illustration of why correlation is the wrong test — a
sizeable correlation coexists here with essentially complete independence in the
sense the study needs.

the four x_2 extents are the four stationary points in x_2 of the four distinct
image coordinates, and they come out of the grid exactly where the coordinates
put them: the half-width r at x_2 = 0, c + r at 1/(1+rho) = 0.8, the centre c at
x_2 = 1, and c - r at 1/(1-rho) = 4/3 = 1.333. each phi's efficient set spans the
interval between the optima of its own two coordinates. that is a consistency
check on the design, not a derivation of the efficient set.

all three phi give distinct, non-trivial efficient sets, none equal to the crisp
set, none the whole box, all strictly interior to the box. phi_lu is a strict
subset of phi_ls, consistent with a0-b r-06 and v-24; phi_cw is not nested with
phi_lu in either direction, sharing 41% of phi_lu and 23% of phi_cw.

### the one requirement of the session brief that p1 does not meet

the brief requires that p1's phi-efficient set be "a curve, not a point". it is
not a curve. under each phi it is a two-dimensional band, the full x_1 interval
[0, 1] crossed with an x_2 interval.

this is not a failure of this particular design and no design will fix it. two
variables and two interval objectives give, through theorem 3.1, a real
multiobjective problem with **four** objectives on a two-dimensional decision
space. for m objectives on an n-dimensional space the efficient set is generically
min(m-1, n)-dimensional, here min(3, 2) = 2. a curve would need the x_2 trade-off
to resolve to a single value for every x_1, and that happens exactly when the
width coordinate and the centre coordinate have the same optimum in x_2, which is
the aligned case shown above to make phi_cw reproduce the crisp order. **a curve
and three distinct phi are not simultaneously available at n = 2, m = 2.**

the band satisfies the purpose the brief gives for the requirement, "so spread
and coverage have something to measure", better than a curve would: it has
positive measure in both decision coordinates, so hausdorff distance and
delta-coverage have two dimensions of structure to pick up rather than one. and
it is tractable for b1, being a product of intervals with x_2 bounds independent
of x_1.

it is nevertheless a departure from a stated requirement of both the session
brief and CONTEXT.md section 10 a4, so CONTEXT.md is corrected and the correction
is in the session reply. it is also listed under "not settled" below, because
whether to accept a two-dimensional efficient set or to change p1's shape is a
judgement the research chat should make rather than this session.


## part 4, tier 1

### the form

both benchmarks keep their published objectives untouched and gain a half-width:

    F_i(x) = [ f_i(x) - r_i(x),  f_i(x) + r_i(x) ]

with f_i the published objective and r_i the half-width below. no coefficient is
disturbed and no objective is rewritten, so this is a modification of how
imprecision enters, not a new benchmark family.

the width driver is x_n, the last decision variable, in both cases. the **form**
of the dependence differs between the two benchmarks and that is deliberate, not
an inconsistency: the rule stated in part 2 is uniform, and it forces different
instances because the two benchmarks' g functions differ in x_n.

    ZDT1     n = 30,  x in [0,1]^30,  m = 2 interval objectives, 4 real

      f_1(x) = x_1
      g(x)   = 1 + 9 * (sum_{i=2}^{n} x_i) / (n - 1)
      f_2(x) = g(x) * (1 - sqrt(f_1(x) / g(x)))

      r_1(x) = r_2(x) = eps * ( (x_n - 1/2)^2 + 1/20 )

      g is *linear* in x_n with slope 9/(n-1) = 0.3103 and its optimum in x_n is
      at the face x_n = 0. a half-width linear in x_n is therefore either aligned
      with it, giving phi_cw = crisp, or opposed to it, giving every phi the whole
      slice; both were measured and both are in part 2. a half-width *quadratic*
      in x_n has its optimum at the interior point x_n = 1/2, different from g's,
      and the trade-off resolves in the interior. the +1/20 keeps it strictly
      positive so no interval degenerates at x_n = 1/2.

    DTLZ2    n = 12,  x in [0,1]^12,  m = 3 interval objectives, 6 real

      g(x)   = sum_{i=m}^{n} (x_i - 1/2)^2
      f_1(x) = (1 + g) cos(x_1 pi/2) cos(x_2 pi/2)
      f_2(x) = (1 + g) cos(x_1 pi/2) sin(x_2 pi/2)
      f_3(x) = (1 + g) sin(x_1 pi/2)

      r_1(x) = r_2(x) = r_3(x) = eps * x_n

      g is already *quadratic* in x_n with an interior optimum at x_n = 1/2, so a
      half-width linear in x_n, optimum at 0, already differs from it and the
      trade-off is bounded. no extra curvature is needed and none should be added:
      a half-width of the form (x_n - 1/2)^2 would put the width's optimum exactly
      on g's and reintroduce the alignment that makes phi_cw reproduce the crisp
      order.

### the crisp limit

eps = 0 gives r_i == 0 for both benchmarks, hence F_i(x) = [f_i(x), f_i(x)], and
the objectives are the published ZDT1 and DTLZ2 unchanged. the published fronts
survive exactly, because nothing but the width has been touched: the centres are
the published f_i at every eps, so the crisp problem is not a limit that is
approached but the exact eps = 0 member of the family.

as CONTEXT.md section 10 a5 already records, the crisp case is a degenerate
baseline and must be labelled one: at eps = 0 the second image coordinate is
identically zero under phi_ls and phi_cw, so half of the transformed objectives
are constant and the three phi coincide with each other and with the crisp order.
part 1 of this document is the general version of that statement. it is not a
data point in the sensitivity study.

### the levels to sweep

    eps in { 0, 0.05, 0.10, 0.25, 0.50 }

the crisp baseline plus four levels, which meets CONTEXT.md section 10 a5's "at
least three levels". the levels were chosen from the slice sweeps below, which
show where each phi's efficient set actually moves.

    ZDT1 slice (x_2..x_29 = 0), r = eps*((x_n-0.5)^2 + 0.05)
       eps    lu frac  ls frac  cw frac  lu==ls cw==crisp  lu x_n ext     cw x_n ext
       0.05    0.1105   0.5281   0.5082  False False   [0.00,0.98]   [0.00,0.50]
       0.10    0.1435   0.5284   0.5082  False False   [0.00,0.98]   [0.00,0.50]
       0.25    0.3701   0.5286   0.5082  False False   [0.00,0.98]   [0.00,0.50]
       0.50    0.4700   0.5286   0.5082  False False   [0.00,0.98]   [0.00,0.50]
       1.00    0.5133   0.5286   0.5082  False False   [0.00,0.98]   [0.00,0.50]

    DTLZ2 slice (x_2 = 0.5, x_3..x_11 = 0.5), r = eps*x_n
       eps    lu frac  ls frac  cw frac  lu==ls cw==crisp  cw x_n extent
       0.02    0.1121   0.5560   0.5082  False   False      [0.000, 0.500]
       0.05    0.1814   0.5907   0.5082  False   False      [0.000, 0.500]
       0.10    0.2706   0.6353   0.5082  False   False      [0.000, 0.500]
       0.25    0.4964   0.7482   0.5082  False   False      [0.000, 0.500]
       0.50    0.8517   0.9258   0.5082  False   False      [0.000, 0.500]

at every level tested, on both benchmarks, all three phi are distinct and phi_cw
differs from the crisp order. phi_lu is the sensitive one: its efficient set
grows from 11% to 51% of the zdt1 slice and from 11% to 85% of the dtlz2 slice.
phi_cw is stable, its x_n band pinned at [0, 0.5] on both. that spread across eps
is what CONTEXT.md section 10 e3 will report as "under which imprecision levels
the difference appears or vanishes", and the levels above are placed to resolve
it: 0.05 and 0.10 in the region where phi_lu is still tight, 0.25 and 0.50 where
it has opened up.

for contrast, the same zdt1 slice with the *rejected* linear half-width r = eps*x_n:

       eps    lu frac  ls frac  cw frac  lu==ls cw==crisp
       0.020   0.1029   0.1029   0.0164  True    True
       0.050   0.1252   0.1252   0.0164  True    True
       0.100   0.2491   0.2491   0.0164  True    True
       0.207   1.0000   1.0000   0.0164  True    True
       0.310   1.0000   1.0000   0.0164  True    True
       0.500   1.0000   1.0000   0.0164  True    True

at every level phi_lu and phi_ls are identical and phi_cw is the crisp order, and
above eps = 0.2 the first two saturate at the whole slice. that is what the
recommended quadratic form avoids, and it is why the two benchmarks get different
half-width forms.


## what this session could not settle

recorded, not resolved.

**u-1. whether a two-dimensional p1 efficient set is acceptable.** the session
brief and CONTEXT.md section 10 a4 both ask for a curve. part 3 shows a curve is
not available at n = 2, m = 2 together with three distinct phi. CONTEXT.md has
been corrected to state the band, but whether to accept it, or to change p1's
shape by some other means, is the research chat's call. raised as s-08.

**u-2. what a3's phi interface should be.** the artefact in part 1 is caused by
computing the width as f_u - f_l. CONTEXT.md section 10 a3 specifies make_phi as
"a function of (f_l, f_u)", which forces that subtraction. carrying
(centre, half_width) instead, or having problems return both representations,
would remove it, but it changes a specified interface and touches a2 as well.
raised as s-06. not decided here because a1 has no mandate over a3's signature.

**u-3. how large the artefact is when the width is not constant.** part 1
measures it only in the degenerate case, where it is total. the relative error in
the computed width is of order machine epsilon times |f| divided by the width, so
it is negligible when the width is a reasonable fraction of the objective value
and unbounded as the width goes to zero. the eps = 0 crisp baseline of the tier 1
sweep sits exactly at that limit. no threshold has been established and none is
guessed. this needs a numerical study in a2 or a3, not a1.

**u-4. whether the width driver rule generalises.** part 2's rule was derived
from two benchmarks and one tier 0 design. it is stated as a rule because it
explains every failure observed in this session, including four p1 candidates and
two zdt1 variants, but it has not been tested outside them. it is a working rule,
not a result.

**u-5. the scale asymmetry of a common absolute half-width.** on zdt1, f_1 ranges
over [0,1] and f_2 over roughly [0,10] under uniform sampling, so a common
absolute half-width is a large relative imprecision on the first objective and a
small one on the second. this follows slide 19's "+-eps en los objetivos" but a
per-objective scaling is an equally defensible reading. it was not tested. raised
as s-09.

**u-6. the dominance relation itself.** everything above uses the usual Pareto
relation. a0's ambiguity a-3 records that [1] prints a different one for problem
(12), and s-03 is still open. if that resolves the other way, every non-dominated
count in this document changes, though the degeneracy conclusions of parts 1 and
2 would not: they rest on the image coordinates being monotone functions of one
another, which no choice of dominance relation affects.
