# [12–15] Analysis of Four Interval Optimization Papers 

Prepared as a template/comparison reference for the PI3 project ("Interval Optimization Techniques based on Computational Intelligence" — φ-automorphism order relations + NSGA-II/PSO Pareto sensitivity study). These papers are read for method and reporting structure, not for citation of theory.

Papers covered:
1. **[Şerban, Costea, Ferrara]** — *Portfolio Optimization Using Interval Analysis* (file 15)
2. **[Şerban 2025]** — *A Multi-Period Optimization Framework for Portfolio Selection Using Interval Analysis*, Mathematics/MDPI (file 14)
3. **[Wen, Wang, Cui, Cai, Chen 2026]** — *A Two-Stage Evolutionary Algorithm for Uncertain Constrained Multi-Objective Problems with Interval-Valued Objective* (TS-ICMOEA), Information Sciences (file 13)
4. **[Cui, Qu, Zhang, Jin, Cai, Zhang, Chen 2024]** — *An Adaptive Interval Many-Objective Evolutionary Algorithm with Information Entropy Dominance* (IMEA-IED), Swarm and Evolutionary Computation (file 12, bundled in the same upload as file 13)

Straight assessment up front: only papers 3 and 4 are real computational templates for what this project needs (NSGA-II/PSO + interval dominance + Pareto sensitivity). Papers 1 and 2 are LP-based, single-objective, and don't use an evolutionary algorithm at all — they're useful for problem-formulation language and portfolio constraint structure, not for algorithm design.

---

# Paper 1: Portfolio Optimization Using Interval Analysis (Şerban, Costea, Ferrara)

## 1. Problem formulation
Real-world problem: a single-period portfolio allocation problem for an investor with capital to distribute across n risky assets, where asset returns are estimated as intervals from historical data.

- **Decision variables:** x_j = proportion of total capital invested in asset j, j = 1,…,n.
- **Objectives:** exactly one. Maximize interval-valued portfolio return: max [r̃(x)] = [Σ x_j r_j^L, Σ x_j r_j^U]. There is no second explicit objective — risk enters only as a constraint, not as a competing objective. This is not a multi-objective problem in the pymoo/NSGA-II sense.
- **Constraints (exactly as stated):**
  - Σ x_j = 1
  - risk tolerance: mean-deviation interval of the portfolio w(x) ≤ [w^L, w^U] (component-wise upper bound on the risk interval)
  - 0 ≤ x_j ≤ u_j for j = 1,…,n (box constraints, no short selling, per-asset cap)

## 2. How intervals enter the problem
Intervals appear in two places: (1) the objective — each asset's average return is represented as [min(r_a, r_h), max(r_a, r_h)], where r_a is the arithmetic mean of historical returns and r_h is a "historical mean return tendency" computed over a rolling window τ; (2) the risk constraint — the mean-absolute-deviation of the portfolio return is computed as an interval by taking min/max over historical deviations. The intervals represent estimation uncertainty in the true (unobservable) expected return and risk, not measurement noise or randomness with a known distribution — that's the explicit motivation given for choosing interval over stochastic/fuzzy modeling. Decision variables x_j are ordinary real numbers, not intervals.

## 3. How they handle interval comparison/ordering
They do not perform pairwise dominance comparison of interval-valued solutions at all. Section 2.3 lists several classical interval inequality definitions (component-wise ≤, the Ishibuchi & Tanaka 1990 median-based order ⪯ where [x]⪯[y] iff m[x]≤m[y], plus two more variants), but these are presented as background, not actually invoked in the solution algorithm. The actual solution method sidesteps interval comparison entirely by reducing the interval program to two deterministic linear programs — a "best" case (safest possible constraints, most favorable coefficients) and a "worst" case (strictest constraints, least favorable coefficients) — solved independently, then blended.

## 4. Algorithm used
Classical Simplex algorithm, applied twice (once per LP: PPL(1) "best" and PPL(2) "worst"). This is off-the-shelf LP, not a metaheuristic, not NSGA-II or PSO. The final portfolio is x⁰ = λx⁽¹⁾ + (1−λ)x⁽²⁾ for λ ∈ [0,1], a simple linear interpolation — not a Pareto front.

## 5. Results reported
A single case study: two Romanian-exchange stocks (TGN = Transgaz, FP = Fondul Proprietatea), 124 trading days of closing prices (Apr–Sep 2014), τ = 10-day window for the trend component. Computed interval returns: r̃₁ = [0.0632, 0.1847], r̃₂ = [0.0068, 0.1110]. Risk tolerance set to [0.02, 0.06], upper allocation bound u_j = 0.8 for both assets. Solving PPL(1) and PPL(2) gives x⁽¹⁾ = (0.28, 0.72) and x⁽²⁾ = (0.22, 0.78). No convergence metrics, no comparison against any other method, no sensitivity analysis on λ, no repeated trials — it's a single deterministic numeric example, described as illustrating the method rather than validating it.

## 6. What you can take directly from this paper
- The two-stage "best-case LP / worst-case LP, then λ-blend" decomposition is a clean, minimal illustration of the general idea behind φ-based transformation — useful as an intuition-building baseline before moving to NSGA-II/PSO with automorphism-based order relations.
- The interval-return construction recipe (arithmetic mean + trend/momentum mean, taking min/max as the bounds) is a reusable, simple way to turn a historical return series into an interval without inventing new machinery.
- The minimal case-study reporting format (parameter table → one results table → short interpretation) is a reasonable template for a first, very small computational sanity check, before scaling up to the full NSGA-II/PSO experiments.

## 7. Gaps or weaknesses
- Not multi-objective: risk is a constraint, not a second objective, so there's no Pareto front to speak of — this paper cannot directly demonstrate "does the front change under different φ."
- No evolutionary algorithm at all; nothing here transfers to a pymoo NSGA-II/PSO pipeline except the return-construction idea.
- Only two assets, one time period, no sensitivity analysis, no benchmarking against alternative interval order relations — this is exactly the gap the current project is meant to fill.
- The paper's own literature discussion criticizes an earlier semi-absolute-deviation model (Jong 2012) for "shortcomings from computational point of view" without giving any number or experiment to back that claim up.

## 8. Template value
**2/5.** Useful only for the return-construction recipe and as a minimal conceptual warm-up; it is not a usable computational template for an NSGA-II/PSO + φ-order-relation pipeline.

## 9. Flags
- The claim about Jong (2012)'s "shortcomings from computational point of view" is asserted, not demonstrated.
- Several equations in the extracted text show OCR corruption (garbled symbols, e.g. the interval-order definitions in Section 2.3 use a non-standard "Ա" glyph that is presumably meant to render as a specific relation symbol). Don't trust the extracted equation formatting for implementation — go back to the original PDF before coding anything from this paper.

---

# Paper 2: A Multi-Period Optimization Framework for Portfolio Selection Using Interval Analysis (Şerban, 2025)

## 1. Problem formulation
Real-world problem: multi-period portfolio rebalancing over T discrete periods for n assets (case study: four cryptocurrencies — BTC, ETH, SOL, BNB), maximizing terminal wealth subject to per-period return, risk, liquidity, and diversification requirements, with transaction costs charged on rebalancing.

- **Decision variables:** x_{t,i} = proportion of wealth allocated to asset i at period t, for i = 1,…,n and t = 1,…,T.
- **Objectives:** exactly one — maximize terminal wealth W_T (interval-valued), computed as a product across periods of (interval return − interval transaction cost) terms, scaled by initial wealth W₀. Again, single-objective; risk/liquidity/diversification are constraints, not objectives.
- **Constraints (as numbered in the paper, Eqs. 9–14):**
  - (9) portfolio return interval at period t ≥ minimum required return interval [R_t]
  - (10) portfolio risk interval (interval covariance-based) ≤ maximum tolerated risk interval [δ_t]
  - (11) portfolio turnover/liquidity interval ≥ minimum required interval [I_t]
  - (12) Shannon-entropy diversification measure H(x_t) = −Σ x_{t,i} ln x_{t,i} ≥ threshold e_t
  - (13) Σ_i x_{t,i} = 1 for each period t
  - (14) x_{t,i} ≥ 0 (no short selling), for all i, t

## 2. How intervals enter the problem
Intervals appear only in the parameters, not in the decision variables: expected return [r_{t,i}], covariance [δ_{i,k,t}], and turnover/liquidity [I_{t,i}] are all interval-valued per asset per period. These flow through into interval-valued portfolio return, risk, turnover, and terminal wealth. They are stated to represent market volatility and estimation uncertainty, explicitly framed as more appropriate than probabilistic models for "volatile markets such as cryptocurrencies" where historical data may be "limited, inconsistent, or unstable." Transaction cost and entropy are treated as real (non-interval) quantities.

## 3. How they handle interval comparison/ordering
Same three-stage best/worst/blend structure as Paper 1, extended to the multi-period, multi-constraint setting:
- **Stage 1:** solve for the "best" solution x⁽¹⁾ using the most favorable bound of each interval (upper return bound, lower risk bound, etc.) subject to the constraints evaluated at their most permissive bounds.
- **Stage 2:** solve for the "worst" solution x⁽²⁾ using the opposite (least favorable) bounds.
- **Stage 3:** blend, x⁽⁰⁾ = λx⁽¹⁾ + (1−λ)x⁽²⁾, λ ∈ [0,1].
There is no pairwise interval-dominance comparator and no explicit φ-automorphism language; λ functions as a scalar risk-attitude weight, not a general order-relation parameter. The case study additionally frames three named strategies — pessimistic (lower return bound / upper risk bound), optimistic (upper return bound / lower risk bound), mixed (average of bounds) — which is a slightly different but related three-way bracketing of the same idea.

## 4. Algorithm used
**Not clearly specified.** The paper describes three conceptual stages (find best bound, find worst bound, blend) but never names the numerical method used to solve the resulting constrained nonlinear optimization at each stage — no simplex, no NSGA-II, no PSO, no solver library is mentioned. The text just says the interval objective is "solved using conventional techniques" after being converted to a "single-valued nonlinear optimization problem." This is a real gap in the paper, not just an omission on my part.

## 5. Results reported
Case study on four cryptocurrencies over three monthly periods (Jan–Mar 2025), with **simulated** (explicitly stated, not real historical) interval input data for return/risk/turnover, given in a table per asset per period. Parameters: W₀ = 1000 (unit currency), transaction cost 0.2% per asset, entropy threshold e_t = 0.9 for all t. Final terminal wealth intervals by strategy: pessimistic [1085.32, 1163.77], mixed [1123.89, 1245.16], optimistic [1167.42, 1323.55]. Discussion: pessimistic strategy produces narrower, more conservative allocations; optimistic produces wider, higher-expected-return allocations; entropy diversification is credited with keeping allocations spread across all four assets, especially in the pessimistic/mixed cases. No comparison against any other algorithm, no repeated-trial statistics, no convergence behavior shown, and — importantly — no real market data used to validate the numbers.

## 6. What you can take directly from this paper
- The four-constraint-type structure (return floor, risk ceiling, liquidity floor, diversification floor via entropy) is directly reusable as a richer constraint set for a portfolio-optimization test problem in pymoo, beyond the simpler return/risk-only setup of Paper 1.
- The Shannon-entropy diversification constraint (H(x) = −Σ x_i ln x_i) is a ready-made, well-defined additional term that could be used either as a constraint or turned into an explicit second/third objective in a true multi-objective formulation.
- The three-strategy (pessimistic/mixed/optimistic) presentation format, mapped to different bound choices, is a reasonable way to present the *outcome* of a sensitivity study — though note it is not the same thing as varying an order relation φ; it's varying which bound of the interval is treated as "true."
- The literature framing (why intervals over stochastic/fuzzy for volatile/limited-data markets) is directly reusable prose for a project introduction.

## 7. Gaps or weaknesses
- Still single-objective with constraints, not a genuine multi-objective Pareto problem — same structural limitation as Paper 1, just with more constraints.
- The core solution algorithm is unspecified ("conventional techniques") — this cannot be replicated as-is; you'd have to choose your own solver for the described stages.
- Input data for the case study is explicitly simulated, not real market data, and results are not validated against any ground truth or benchmark — treat the reported terminal-wealth numbers as illustrative only, not evidence the method works on real markets.
- No exploration of different φ/order-relation choices; λ is a fixed scalar blend weight, not a family of order relations, so this paper does not actually test the "does the solution change under different comparison rule" question central to this project.
- No NSGA-II/PSO, no pymoo-style dominance handling, nothing on Pareto front sensitivity.

## 8. Template value
**3/5.** Solid for constraint-structure ideas (especially the entropy diversification term) and for framing/motivation language; weak as an algorithmic template because the actual solver is unspecified and the method isn't evolutionary or genuinely multi-objective.

## 9. Flags
- "Solved using conventional techniques" is a vague, unsupported methodological claim — there is no way to verify or reproduce the optimization step from the paper's text alone.
- The case-study data is explicitly simulated (stated directly in the text: "calibrated using a simulated price series"), so the headline terminal-wealth results in Table 2 are not empirically validated against real crypto market behavior — worth flagging clearly if this paper is cited anywhere as evidence the model "works."
- Some of the extracted formula text (e.g., the terminal wealth recursion, Eq. 5–6) has inconsistent subscripts (t vs. j mixed) likely from OCR/PDF extraction — re-derive from the original PDF rather than trusting the extracted LaTeX-like text.

---

# Paper 3: A Two-Stage Evolutionary Algorithm for Uncertain Constrained Multi-Objective Problems with Interval-Valued Objective (TS-ICMOEA)

## 1. Problem formulation
This is a generic algorithmic paper, not a finance application — the "real-world problem" is a class of benchmark problems (interval constrained multi-objective optimization problems, ICMOPs), built by injecting interval uncertainty into standard test suites (LIRCMOP1-4, DC-DTLZ1/DTLZ3).

- **Decision variables:** x = (x_1,…,x_q) ∈ R^q, a generic q-dimensional real decision vector (no domain-specific meaning; these are the standard decision variables of the underlying WFG/DTLZ-style benchmark functions).
- **Objectives:** Z interval-valued objectives, F(x,c) = (f_1(x,c),…,f_Z(x,c))ᵀ, each f_z(x,c) an interval determined by an uncertain parameter c. Genuinely multi-objective (2 to 15 objectives tested).
- **Constraints (exactly as stated):**
  - g_j(x) ≤ 0, for j = 1,…,m (inequality)
  - h_j(x) = 0, for j = m+1,…,n (equality)
  - Constraint violation degree CV_j(x) = max{g_j(x), 0} for inequality, max{|h_j(x)| − ε, 0} for equality (ε = 0.0001 tolerance); overall CV(x) = Σ_j CV_j(x). A solution is feasible iff CV(x) = 0.

## 2. How intervals enter the problem
Intervals are injected purely synthetically, on top of deterministic benchmark objectives, using a perturbation factor: η_z = |sin(10 · 2^(z-1)π Σ_d x_d)/4|, then f_z(x,c_z) = [f_z(x) − c_z, f_z(x) + c_z] with c_z built from η_z. So this represents artificial, controlled uncertainty for algorithm stress-testing, not a physically-derived quantity (no market, sensor, or measurement noise interpretation is given, or needed, in this paper). Decision variables and constraints remain deterministic/real; only the objective values are interval-valued.

## 3. How they handle interval comparison/ordering
This is the substantive part of the paper. Two mechanisms:
- **Interval probability / interval dominance (Definitions 3–4, following Liu et al. 2020):** for two interval objective values I and J, take R = [R̲, R̄] as the smallest and second-smallest of the pooled bound set; P(I<J) = d(J,R) / (d(I,R) + d(J,R)) where d is Euclidean distance in the (lower, upper) bound plane. If P(I<J) > 0.5 then I < J, if < 0.5 then I > J, if = 0.5 they're equal. Solution x_i is said to dominate x_j (denoted x_i ≺_P x_j) if P(I<J) ≥ 0.5 on every objective and > 0.5 on at least one — a probabilistic generalization of Pareto dominance.
- **Two-level balanced dominance sorting (their own contribution, Stage 1 of the algorithm):** first level = standard interval non-dominated sorting on the raw objective intervals (Eq. 9). When too many individuals tie at the same rank (common in high-dimensional objective spaces), a second-level ranking kicks in on a bi-objective model: min(CI(x), CV(x)), where CI(x) is a "convergence indicator" — the sum, over objectives, of interval distance between x's objective values and the population's per-objective ideal interval (Eq. 11) — and CV(x) is constraint violation. This second-level model is itself solved via ordinary Pareto non-dominated sorting on (CI, CV). Interval crowding distance (Definition 5) is used as a final tiebreaker.
- **Stage 2 feasibility handling:** switches between two subprocesses based on the feasible ratio φ = |S_F| / |Q_t| (fraction of the combined population that is feasible): if φ < 0.5, prioritize feasible solutions plus the lowest-CV infeasible ones; if φ ≥ 0.5, apply a constrained-dominance-principle-style sort (interval dominance + interval crowding distance) restricted to feasible solutions.

## 4. Algorithm used
**TS-ICMOEA**, a modified NSGA-II-style genetic algorithm (simulated binary crossover + polynomial mutation for offspring generation), with a custom two-stage environmental selection replacing standard non-dominated sorting: Stage 1 (generations t ≤ μ·T_max, μ tuned to 0.5) does global search via the two-level balanced dominance sorting above; Stage 2 (t > μ·T_max) does feasibility-guided selection via the two cooperative subprocesses. This is a substantially modified algorithm, not off-the-shelf; stated worst-case time complexity O(M N²).

## 5. Results reported
Benchmarks: InLIRCMOP1-4 (2 objectives, disconnected/irregular feasible regions) and InDC1/InDC2/InDC3-DTLZ1 and -DTLZ3 (2 to 15 objectives, three types of constraint structures). Compared against DI-μMOGA, three weight variants of IMOEA-DS, INSGA-II, and IP-ICA-MOEA (bi-objective only). Metrics: **IIGD** (Interval Inverted Generational Distance — average distance between the constrained-PF and the algorithm's obtained front, computed on interval midpoints) and **Feasible Rate** (fraction of final population that is feasible). Stage-control factor μ tuned across 0.3/0.5/0.7 with Wilcoxon rank-sum testing; μ = 0.5 selected as best on balance. Main findings: TS-ICMOEA achieves the best or statistically tied-best IIGD on most InLIRCMOP and InDC1/InDC2-DTLZ1 problems, and is the only algorithm to sustain near-100% feasible rate across almost all problems as the number of objectives scales up to 15 (competitors frequently return "NaN" — no feasible solutions found — at higher dimensions). Boxplots of IIGD across 30 independent runs (Figs. 2, 3, and Table 8, described but not reproduced here) show TS-ICMOEA with the lowest median and shortest interquartile box on most problems, indicating both accuracy and run-to-run stability. It is not universally best — on InDC1-DTLZ3 and InDC2-DTLZ3 at very high objective counts, decomposition-based IMOEA/D-family methods sometimes edge it out, and on InDC3-DTLZ1 with 8+ objectives every compared algorithm, including TS-ICMOEA, fails to find any feasible solution (reported as NaN across the board) — the paper acknowledges this honestly rather than hiding it.

## 6. What you can take directly from this paper
- This is the most directly transferable of the four papers to a pymoo NSGA-II pipeline: it demonstrates exactly the pattern of "swap a custom interval dominance comparator into an otherwise-standard NSGA-II-style selection loop," which maps directly onto the φ-automorphism substitution this project is built around.
- The interval-probability dominance definition (Definitions 3–4) is a complete, well-specified, ready-to-implement alternative order relation — a good second or third φ-family option beyond Ishibuchi-Tanaka median order.
- The reporting structure — IIGD table with mean (std) per problem/objective-count, a Wilcoxon +/−/= summary row, feasible-rate table, and boxplots per problem across independent runs — is close to a ready-made template for reporting how NSGA-II's Pareto front changes under different φ choices.
- The disturbance-factor formula (η_z = |sin(10·2^(z-1)π Σx_d)/4|, then interval widening by c_z = λη_z f_z(x)) is a standard, reusable way to convert any deterministic benchmark problem (e.g. from pymoo's built-in test suite) into an interval-valued one for controlled sensitivity experiments.

## 7. Gaps or weaknesses
- No finance or portfolio application whatsoever — this is a pure algorithm-benchmarking paper. Bridging it to the interval-portfolio-optimization domain is entirely left to the reader.
- Only tests a genetic-algorithm family (NSGA-II style); no PSO comparison at all.
- Despite being adjacent to the exact question this project asks, the paper never runs the experiment of holding the algorithm fixed and swapping the order relation itself (their own two-level scheme vs. plain interval-probability dominance vs. component-wise ≤, etc.) to see how much the resulting front changes — that specific ablation is conspicuously absent, which is somewhat surprising given how close the machinery is to enabling it directly.

## 8. Template value
**5/5.** This is the best structural match to the project's actual computational plan (custom interval dominance + NSGA-II-style algorithm + Pareto-front comparison across problems), and its reporting format is close to directly reusable.

## 9. Flags
- Several equations in the extracted text show visible OCR/formatting corruption (garbled subscripts and superscripts, especially around the crowding-distance and association-distance formulas, Eqs. 5, 8, 21–22) — don't code from the extracted text; verify against the original PDF figures/equations first.
- The result that all compared algorithms (including TS-ICMOEA) fail entirely on InDC3-DTLZ1 above 8 objectives is reported plainly as a limitation, not glossed over — worth noting as a point of intellectual honesty in the paper, and a useful reminder that "our method wins everywhere" claims should always be checked against exactly this kind of caveat.

---

# Paper 4: An Adaptive Interval Many-Objective Evolutionary Algorithm with Information Entropy Dominance (IMEA-IED)

## 1. Problem formulation
Generic interval many-objective optimization problem (IMaOP, defined as more than 3 objectives), plus one practical application taken from prior work: workflow migration optimization for mobile devices and edge servers.

- **Decision variables:** x = (x_1,…,x_n) ∈ R^n, generic (for the edge-computing case, these would be migration/allocation decisions, but the paper does not spell out that decision-variable meaning in the excerpted text — it's inherited from the cited prior model, IMaOWMUE).
- **Objectives:** m interval-valued objectives, m > 3 by definition of "many-objective." In the benchmark experiments, m ∈ {5, 8, 10, 15}. In the practical application: 4 named objectives — migration delay, maximum completion time, energy consumption, load balancing.
- **Constraints:** the paper's own core model (Eq. 1) is stated as unconstrained (x ⊆ Rⁿ only); no g_j/h_j formalism is given in this paper, unlike Paper 3. Constraint handling is not part of this paper's contribution.

## 2. How intervals enter the problem
Intervals appear as interval-valued parameter vectors C_i = (C_i1,…,C_ih), C_ih = [C̲_ih, C̄_ih], substituted into each objective function f_i(x, C_i). In the benchmark experiments, intervals are again synthetically injected using the identical disturbance-factor recipe as Paper 3 (same formula, same citation chain). In the practical edge-computing application, intervals are stated to represent uncertain network bandwidth and server computing power — i.e., genuine operational uncertainty, not synthetic perturbation, though this application is inherited from prior work rather than newly modeled here.

## 3. How they handle interval comparison/ordering
This paper's central contribution is precisely this question, and it is the most directly relevant of the four papers to the project's core research question. It:
1. Reviews four existing interval dominance methods (IDMs), each given as an explicit formula:
   - **IDM1** (maximal interval confidence): P(a≤b) = d(b,β)/(d(a,β)+d(b,β)), where β is a constructed "ideal interval" between a and b.
   - **IDM2** (conditional interval confidence): same as IDM1 but adds a correction term when midpoints of a and b tie and the lower-bound gap exceeds a's width, to reward convergence potential.
   - **IDM3** (interval confidence level): P(a≤b) = max{1 − max[(a̲−b̲)/((ā−a̲)+(b̄−b̲)), 0], 0}, compared against a threshold γ ∈ [1/2, 1].
   - **IDM4** (improved interval confidence level): adds a relative-difference correction term ΔP(a,b) = (m(b)−m(a)) − (a̲−b̲) to IDM3, to balance average convergence level against convergence potential.
2. Demonstrates with a worked example (their Fig. 3, two small populations "Group A" and "Group B" with the same pair of intervals but different overall population statistics) that IDM1/IDM2 always favor narrower intervals (better uncertainty) while IDM3/IDM4 always favor smaller lower bounds (better convergence) — and that neither fixed choice is right in every population context.
3. Proposes their own **adaptive, information-entropy-based method**: per objective, compute convergence entropy H_ck (Shannon entropy of the normalized midpoints across the population) and uncertainty entropy H_wk (Shannon entropy of the normalized widths). If H_ck < H_wk (midpoints are more "unstable"/informative across the population), use a convergence-weighted confidence P_c (an IDM3 variant weighted by the midpoint gap Δm); if H_ck > H_wk, use an uncertainty-weighted confidence P_w (weighted by the width gap Δw); if equal, fall back to plain IDM3. The switch is recomputed every generation, per objective, from the current population statistics — this is the "adaptive" part.

## 4. Algorithm used
**IMEA-IED**, a modified NSGA-III-style algorithm: standard genetic operators, non-dominated sorting using the information-entropy interval dominance method above, then — when the last front overflows the population budget — an "adaptive niche selection strategy" built on NSGA-III reference vectors with two additions: (a) a crowding-distance-increment (CDI) method to break ties in niche count between subpopulations, and (b) an adaptive reference-vector update (AUV) method that temporarily relocates a reference vector toward an unassociated region when its subpopulation has no candidate solutions, to actively search unexplored parts of the objective space. Built on the NSGA-III skeleton but substantially modified in both the dominance rule and the niche selection.

## 5. Results reported
Benchmarks: InWFG1-9 and InDTLZ1-6 (same interval-injection recipe as Paper 3), tested at 5, 8, 10, and 15 objectives (60 total problem/dimension combinations), compared against 7 competitor algorithms (IMOEA, SetGA, DI-μMOGA, InMaOEA, IMOEA/D, EG-IMOEA, IMOEA/D-AWN). Four metrics: **IIGD**, **Spread** (distribution uniformity, smaller better), **Imprecision** (perimeter of the hyper-cube spanned by the interval solution set, i.e. total uncertainty, smaller better), and **Runtime**. Two ablation studies, directly relevant to this project's methodology:
- **IDM ablation:** compares "convergence-only" (fixed), "uncertainty-only" (fixed), plain IDM3 ("without" adaptation), and the full adaptive method ("with IED"). Result: convergence-only wins on IIGD but loses badly on Imprecision; uncertainty-only wins on Imprecision but loses on IIGD; the adaptive method is the only one that ranks well on *both* metrics simultaneously (average rank table, their Table 10, plus a Wilcoxon win/loss count in Fig. 7).
- **Niche-strategy ablation:** compares CDI-only, AUV-only, neither (plain NSGA-III niching), and full IMEA-IED. Full method gets the best average rank on both IIGD and Spread (their Table 12, Fig. 8).
Main finding: IMEA-IED achieves the best or near-best IIGD on most problems, with the advantage growing as the number of objectives increases; it dominates on Imprecision except where SetGA directly optimizes an imprecision-like quantity as part of its own transformation; it has the shortest runtime among the non-decomposition (dominance-based) competitors. On the practical edge-computing application (their Table 13) it gets the best hypervolume, best Spread, best runtime, and second-best Imprecision (behind SetGA).

## 6. What you can take directly from this paper
- This is the paper most directly structured around the project's actual research question — its two ablation studies are essentially a working blueprint: hold the algorithm (NSGA-III-style) fixed, vary only the interval comparison rule, and report how the resulting Pareto front changes on standardized metrics (IIGD, Imprecision/Spread). This project's Step 5 ("analyze Pareto front sensitivity to φ") can be modeled almost directly on Tables 10 and 12 here, substituting φ-automorphism-based order relations for their entropy-adaptive one.
- IDM1–IDM4 are four fully specified, ready-to-implement alternative interval order relations — a solid starting menu of comparator functions to slot into pymoo's dominance logic as fixed-φ baselines, before or alongside any automorphism-based order relation supplied by the supervisors.
- The identical disturbance-factor benchmark-construction recipe (shared with Paper 3) reinforces that this is a standard, low-risk way to build interval test problems from any deterministic benchmark suite pymoo already ships with.
- The ranking-table + Wilcoxon-win/loss-count format (Tables 10–12, Fig. 7–8) is a compact, defensible way to summarize a sensitivity study across many test problems without needing to show every individual result.

## 7. Gaps or weaknesses
- No finance/portfolio application (only edge computing, and that's inherited from prior work, not newly modeled here) — same bridging work needed as with Paper 3.
- No PSO comparison — only genetic-algorithm and decomposition-family methods.
- Despite defining midpoint/width-based entropy terms, the paper never frames its dominance rule in terms of gH-difference or center-width decomposition in the gH-calculus sense that this project's supervisors use — the mathematical vocabulary doesn't line up directly, even though the underlying quantities (midpoint, width) are the same.
- No stated code or data availability.

## 8. Template value
**5/5.** The single most directly reusable paper of the four for this project's core question: it is essentially a worked example of "vary the order relation, hold the algorithm fixed, measure Pareto front sensitivity," with a ready reporting format.

## 9. Flags
- The symbols H_ck and H_wk are defined per-objective (Eqs. 15–18) but the narrative text around Fig. 6 sometimes refers to "H_c" and "H_w" without the objective index, which reads as if it were a single global quantity — check Section 3.2 carefully before reimplementing to make sure you're computing entropy per-objective, not pooled across objectives.
- Several formulas in the extracted text show garbled/uncertain rendering (e.g. the "𝑃(𝑎 ≤ 𝑏) 𝛥= max{...}" expressions for IDM3/IDM4 and the entropy-weighted P_c/P_w formulas) — verify against the original PDF before coding; do not trust the OCR-derived formatting for anything you plan to implement.
- The claim that all algorithms fail on some high-dimensional DTLZ variant belongs to Paper 3, not this one — don't conflate the two papers' limitation statements when writing up notes later.

---

# Overall comparison for this project

| | Paper 1 (Portfolio LP) | Paper 2 (Multi-period) | Paper 3 (TS-ICMOEA) | Paper 4 (IMEA-IED) |
|---|---|---|---|---|
| Domain | Finance (2 assets) | Finance (4 crypto) | Generic benchmarks | Generic benchmarks + edge computing |
| Multi-objective? | No (1 obj + constraints) | No (1 obj + constraints) | Yes (2–15 obj) | Yes (5–15 obj) |
| Algorithm | Simplex (LP) | Unspecified | Modified NSGA-II | Modified NSGA-III |
| Interval-order treatment | Best/worst bound blend | Best/worst bound blend | Interval probability + custom two-level sort | 4 known IDMs + novel entropy-adaptive IDM |
| Tests sensitivity to order relation? | No | No | No (despite having the pieces) | Yes — this is its central contribution |
| Template value | 2/5 | 3/5 | 5/5 | 5/5 |

Bottom line: papers 1 and 2 give usable finance-domain constraint structures and return/risk construction recipes but nothing algorithmic. Papers 3 and 4 give the actual computational machinery — custom interval dominance rules slotted into an NSGA-style loop, benchmark construction via disturbance factors, and (paper 4 especially) a ready ablation-study format for exactly the "does changing the order relation change the solution" question this project is asking. Neither 3 nor 4 runs that ablation on a finance problem, so combining paper 1/2's portfolio formulation with paper 3/4's methodology is where the actual novelty of this PI3 project would sit.
