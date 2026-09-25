# Provenance of every generated number

Written by `experiments/make_presentation.py`. One row per macro in `fragments/numbers.tex`.

| macro | value | source |
|---|---|---|
| `\pRho` | `\tfrac{1}{4}` | src/problems_tier0.py p1_default_params rho |
| `\pOffset` | `\tfrac{1}{8}` | src/problems_tier0.py p1_default_params, the constant term of the half-width |
| `\pBoxLo` | `-\tfrac{1}{2}` | src/problems_tier0.py p1_lower |
| `\pBoxHi` | `\tfrac{3}{2}` | src/problems_tier0.py p1_upper |
| `\pAreaLu` | `0.311` | results/tier0/exact_regions_p1.csv area,lu |
| `\pAreaLs` | `1.513` | results/tier0/exact_regions_p1.csv area,ls |
| `\pAreaCw` | `1.000` | results/tier0/exact_regions_p1.csv area,cw |
| `\pUnionShare` | `10.3` | results/tier0/exact_regions_p1.csv overlap_union_share,lu,cw (in %) |
| `\pLuOutsideCw` | `60.5` | results/tier0/exact_regions_p1.csv 1 - coverage_a_in_b,lu,cw (in %) |
| `\pCwOutsideLu` | `87.7` | results/tier0/exact_regions_p1.csv 1 - coverage_b_in_a,lu,cw (in %) |
| `\pCovLuCwExact` | `0.395` | results/tier0/exact_regions_p1.csv coverage_a_in_b,lu,cw |
| `\pCovCwLuExact` | `0.123` | results/tier0/exact_regions_p1.csv coverage_b_in_a,lu,cw |
| `\pJacExact` | `0.103` | results/tier0/exact_regions_p1.csv overlap_union_share,lu,cw |
| `\pCovLuCwMeas` | `0.556` | results/tier0/instrument_error_p1.csv (lu,cw; delta 0.0; n_evals 5000) measured_median, metric coverage_a_in_b |
| `\pCovLuCwErr` | `+40.8\,\%` | results/tier0/instrument_error_p1.csv (lu,cw; delta 0.0; n_evals 5000) measured/exact, metric coverage_a_in_b |
| `\pCovLuCwErrLarge` | `+27.7\,\%` | results/tier0/table_2_measured.csv decision block (lu,cw; delta 0.0; n_evals 20000) median/exact, metric coverage_a_in_b |
| `\pCovCwLuMeas` | `0.222` | results/tier0/instrument_error_p1.csv (lu,cw; delta 0.0; n_evals 5000) measured_median, metric coverage_b_in_a |
| `\pCovCwLuErr` | `+81.0\,\%` | results/tier0/instrument_error_p1.csv (lu,cw; delta 0.0; n_evals 5000) measured/exact, metric coverage_b_in_a |
| `\pCovCwLuErrLarge` | `+48.6\,\%` | results/tier0/table_2_measured.csv decision block (lu,cw; delta 0.0; n_evals 20000) median/exact, metric coverage_b_in_a |
| `\pJacMeas` | `0.187` | results/tier0/instrument_error_p1.csv (lu,cw; delta 0.0; n_evals 5000) measured_median, metric overlap via jaccard = dice/(2-dice) |
| `\pJacErr` | `$\times$1.81` | results/tier0/instrument_error_p1.csv (lu,cw; delta 0.0; n_evals 5000) measured/exact, metric overlap |
| `\pJacErrLarge` | `$\times$1.49` | results/tier0/table_2_measured.csv decision block (lu,cw; delta 0.0; n_evals 20000) median/exact, metric overlap |
| `\pJacFactorPlain` | `1.81` | results/tier0/instrument_error_p1.csv (lu,cw; delta 0.0; n_evals 5000) jaccard measured/exact |
| `\pJacFactorLargePlain` | `1.49` | results/tier0/table_2_measured.csv decision block (lu,cw; delta 0.0; n_evals 20000) jaccard measured/exact |
| `\bMinPct` | `62.8` | results/tier1/table_2_measured_eps_{0.05,0.1,0.25,0.5}.csv decision block, lu,cw, finding, coverage_b_in_a, n_evals 5000, delta 0.0: min over the eight cells of 1 - median (in %) |
| `\bMaxPct` | `91.2` | results/tier1/table_2_measured_eps_{0.05,0.1,0.25,0.5}.csv decision block, lu,cw, finding, coverage_b_in_a, n_evals 5000, delta 0.0: max over the eight cells of 1 - median (in %) |
| `\bMinInt` | `63` | results/tier1/table_2_measured_eps_{0.05,0.1,0.25,0.5}.csv decision block, lu,cw, finding, coverage_b_in_a, n_evals 5000, delta 0.0: min, rounded to the integer |
| `\bMaxInt` | `91` | results/tier1/table_2_measured_eps_{0.05,0.1,0.25,0.5}.csv decision block, lu,cw, finding, coverage_b_in_a, n_evals 5000, delta 0.0: max, rounded to the integer |
| `\bZdtVars` | `30` | src/problems_tier1.py zdt1_n_vars |
| `\bDtlzVars` | `12` | src/problems_tier1.py dtlz2_n_vars |
| `\cZdtCardCw` | `257` | results/tier1/table_2_measured_eps_{0.05,0.1,0.25,0.5}.csv decision block, lu,cw, finding, coverage_b_in_a, n_evals 5000, delta 0.0: cardinality_b, constant over the four eps |
| `\cZdtCardLu` | `26\,\to\,36\,\to\,53\,\to\,68` | results/tier1/table_2_measured_eps_{0.05,0.1,0.25,0.5}.csv decision block, lu,cw, finding, coverage_b_in_a, n_evals 5000, delta 0.0: cardinality_a over eps 0.05, 0.1, 0.25, 0.5 |
| `\cDtlzCardCw` | `1813` | results/tier1/table_2_measured_eps_{0.05,0.1,0.25,0.5}.csv decision block, lu,cw, finding, coverage_b_in_a, n_evals 5000, delta 0.0: cardinality_b, constant over the four eps |
| `\cDtlzCardLu` | `278\,\to\,351\,\to\,575\,\to\,980` | results/tier1/table_2_measured_eps_{0.05,0.1,0.25,0.5}.csv decision block, lu,cw, finding, coverage_b_in_a, n_evals 5000, delta 0.0: cardinality_a over eps 0.05, 0.1, 0.25, 0.5 |
| `\ZdtName` | `ZDT1` | src/problems_tier1.py zdt1_interval |
| `\ZdtSize` | `30 variables, 2 objetivos` | src/problems_tier1.py zdt1_n_vars, zdt1_n_obj |
| `\ZdtF` | `f_1 = x_1, \qquad f_2 = g\,\Bigl(1 - \sqrt{f_1/g}\,\Bigr)` | src/problems_tier1.py evaluate_zdt1, [2] equations (6) and (7) |
| `\ZdtG` | `g = 1 + \dfrac{9}{29}\sum_{i \geq 2} x_i` | src/problems_tier1.py evaluate_zdt1, g with m - 1 = zdt1_n_vars - 1 |
| `\ZdtR` | `r_i = \varepsilon\,\bigl( (\marca{x_d} - \tfrac{1}{2})^2 + \tfrac{1}{20} \bigr)` | src/problems_tier1.py zdt1_half_width |
| `\ZdtDrivers` | `x_{30}, x_{29}` | src/problems_tier1.py zdt1_width_drivers, as 1-based names |
| `\DtlzName` | `DTLZ2` | src/problems_tier1.py dtlz2_interval |
| `\DtlzSize` | `12 variables, 3 objetivos` | src/problems_tier1.py dtlz2_n_vars, dtlz2_n_obj |
| `\DtlzFone` | `f_1 = (1+g)\cos\tfrac{\pi x_1}{2}\cos\tfrac{\pi x_2}{2}` | src/problems_tier1.py evaluate_dtlz2, [3] equation (9) at M = 3 |
| `\DtlzFtwo` | `f_2 = (1+g)\cos\tfrac{\pi x_1}{2}\sin\tfrac{\pi x_2}{2}` | src/problems_tier1.py evaluate_dtlz2, [3] equation (9) at M = 3 |
| `\DtlzFthree` | `f_3 = (1+g)\sin\tfrac{\pi x_1}{2}` | src/problems_tier1.py evaluate_dtlz2, [3] equation (9) at M = 3 |
| `\DtlzG` | `g = \sum_{i \geq 3} (x_i - \tfrac{1}{2})^2` | src/problems_tier1.py evaluate_dtlz2, g over the tail |
| `\DtlzR` | `r_i = \varepsilon\,\marca{x_d}` | src/problems_tier1.py dtlz2_half_width |
| `\DtlzDrivers` | `x_{12}, x_{11}, x_{10}` | src/problems_tier1.py dtlz2_width_drivers, as 1-based names |
| `\IBKone` | `G_1 = \coef{[0.1, 0.2]}\, x_1^2 + \coef{[0.1, 0.3]}\, x_2^2` | src/problems_native.py ibk1_coefficients[0] |
| `\IBKtwo` | `G_2 = \coef{[0.1, 0.3]}\, (x_1 - 5)^2 + \coef{[0.1, 0.5]}\, (x_2 - 5)^2` | src/problems_native.py ibk1_coefficients[1], ibk1_shift |
| `\IBKbox` | `[-10, 10]^2` | src/problems_native.py ibk1_lower, ibk1_upper |
| `\IBKratiosOne` | `\tfrac{1}{3} frente a \tfrac{1}{2}` | computed from ibk1_coefficients[0]: (b-a)/(a+b) per term |
| `\IBKratiosTwo` | `\tfrac{1}{2} frente a \tfrac{2}{3}` | computed from ibk1_coefficients[1]: (b-a)/(a+b) per term |
| `\iAreaLu` | `3.790` | results/part2/exact_regions_ibk1.csv area,lu |
| `\iBandLuLo` | `\tfrac{2}{3}` | results/part2/exact_regions_ibk1.csv band_lower,lu |
| `\iBandLuHi` | `\tfrac{5}{3}` | results/part2/exact_regions_ibk1.csv band_upper,lu |
| `\iAreaLs` | `5.685` | results/part2/exact_regions_ibk1.csv area,ls |
| `\iBandLsLo` | `\tfrac{1}{2}` | results/part2/exact_regions_ibk1.csv band_lower,ls |
| `\iBandLsHi` | `2` | results/part2/exact_regions_ibk1.csv band_upper,ls |
| `\iAreaCw` | `2.876` | results/part2/exact_regions_ibk1.csv area,cw |
| `\iBandCwLo` | `\tfrac{3}{4}` | results/part2/exact_regions_ibk1.csv band_lower,cw |
| `\iBandCwHi` | `\tfrac{3}{2}` | results/part2/exact_regions_ibk1.csv band_upper,cw |
| `\iOrderedEnds` | `\tfrac{1}{2} < \tfrac{2}{3} < \tfrac{3}{4} < \tfrac{3}{2} < \tfrac{5}{3} < 2` | results/part2/exact_regions_ibk1.csv the six band ends, sorted |
| `\iLsOutsideCw` | `49.4` | results/part2/exact_regions_ibk1.csv 1 - coverage_a_in_b,ls,cw (in %) |
| `\iCovLsCw` | `0.506` | results/part2/exact_regions_ibk1.csv coverage_a_in_b,ls,cw |
| `\iNuCurve` | `\tfrac{162}{169}` | docs/part2/f2_ibk1_derivation.md section 4.1, nu of equation (25)'s curve |
| `\iCritRatio` | `4.24` | docs/part2/f2_ibk1_derivation.md section 4.3, critical set measure over X_lu's |
| `\iNuCrisp` | `\tfrac{9}{8}` | computed from src/problems_native.py's coefficients and checked against docs/part2/f2_ibk1_derivation.md section 3.3 |
| `\IVUone` | `G_1 = \coef{[1, 1.5]}\, \marca{x_1} + \coef{[1, 1.5]}\, \marca{x_2} + \coef{[1, 1]}` | [16] appendix A problem 2, as docs/part2/f7_ivu2_derivation.md transcribes it |
| `\IVUtwo` | `G_2 = \coef{[1, 1.5]}\, x_1^2 + \coef{[2, 3]}\, x_2^2 - \coef{[1, 1]}` | [16] appendix A problem 2, as docs/part2/f7_ivu2_derivation.md transcribes it |
| `\IVUbox` | `[-4, 4]^2` | [16] appendix A problem 2, as docs/part2/f7_ivu2_derivation.md transcribes it |
| `\dXstar` | `(3.914930, 1.428474)` | [16] Table 1 page 20, as docs/part2/f2_ibk1_derivation.md section 4.2 (re-computed here in exact rationals from src/problems_native.py's coefficients and asserted equal) |
| `\dY` | `(2.8975, 2.3975)` | docs/part2/f2_ibk1_derivation.md section 4.2 (re-computed here in exact rationals from src/problems_native.py's coefficients and asserted equal) |
| `\dMinMargin` | `0.274` | docs/part2/f2_ibk1_derivation.md section 4.2 (re-computed here in exact rationals from src/problems_native.py's coefficients and asserted equal): the smallest of the four margins |
| `\dConfigs` | `18` | results/part2/dominators_summary.csv: number of rows (solver x phi x budget) |
| `\dConfigsWithDominator` | `18` | results/part2/dominators_summary.csv: rows with seeds_with_a_dominator == n_seeds |
| `\dWidestMargin` | `0.270` | results/part2/dominators_summary.csv: max of widest_margin_over_seeds |
| `\iJacFactorMin` | `1.01` | results/part2/instrument_error_ibk1.csv, metric overlap, delta 0.0, jaccard = dice/(2-dice), measured/exact over the three pairs (min) |
| `\iJacFactorMax` | `1.48` | results/part2/instrument_error_ibk1.csv, metric overlap, delta 0.0, jaccard = dice/(2-dice), measured/exact over the three pairs (max) |
| `\aCorrProportional` | `+1.0000` | docs/part1/a1_uncertainty_model.md part 1, the proportional width, corr(centre, width) |
| `\rWidthValuesTrue` | `46` | docs/explicacion_proyecto.md section 10.3 |
| `\rWidthValuesSeen` | `210` | docs/explicacion_proyecto.md section 10.3 |
| `\rGridPoints` | `40401` | docs/explicacion_proyecto.md section 10.5 |
| `\rFixedCoverage` | `1.000000` | instrument_error_p1.csv, instrument_error_ibk1.csv, table_2_measured_eps_*.csv: every check row with a containment-fixed direction |
| `\rFixedRange` | `0` | same rows: q3 - q1 |
| `\rFixedRows` | `28` | same rows: how many were checked |
| `\rSatConfigs` | `24` | results/tier1/rank_one_summary.csv: nsga2 rows with eps > 0 at n_evals 5000 |
| `\rGenerations` | `50` | results/tier1/rank_one_summary.csv: n_generations |

## Tables

- `fragments/tabla_instrumento.tex` — results/tier0/instrument_error_p1.csv (lu,cw; delta 0.0; n_evals 5000); exact from results/tier0/exact_regions_p1.csv
- `fragments/tabla_benchmarks.tex` — results/tier1/table_2_measured_eps_{0.05,0.1,0.25,0.5}.csv decision block, lu,cw, finding, coverage_b_in_a, n_evals 5000, delta 0.0
- `fragments/tabla_contraejemplo.tex` — docs/part2/f2_ibk1_derivation.md section 4.2 (re-computed here in exact rationals from src/problems_native.py's coefficients and asserted equal)
- `fragments/tabla_saturacion.tex` — results/tier1/rank_one_summary.csv

## Figures

- `p1_crisp.{pdf,png}` — p1 without uncertainty: the two anchors of its centres and the segment between them, which the script re-derives as the non-dominated subset of a 601x601 grid of the box
- `p1_regiones.{pdf,png}` — the three closed forms of docs/part1/b1_phi_efficient_sets.md section 2.4 as masks; areas checked against results/tier0/exact_regions_p1.csv
- `tamanos_eps.{pdf,png}` — cardinality_a and cardinality_b of the slide-11 rows
- `instrumento.{pdf,png}` — the same three rows as the instrument table, drawn: results/tier0/instrument_error_p1.csv (lu,cw; delta 0.0; n_evals 5000)
- `zdt1_frente.{pdf,png}` and `dtlz2_frente.{pdf,png}` — the answer of each benchmark without uncertainty, evaluated with src/problems_tier1.py's own functions on the decision vectors the two papers state, with a 20000-point sample checked to dominate none of them
- `benchmarks.{pdf,png}` — the eight cells of slide 11 drawn, plus the eps = 0 sanity point: results/tier1/table_2_measured_eps_{0.05,0.1,0.25,0.5}.csv decision block, lu,cw, finding, coverage_b_in_a, n_evals 5000, delta 0.0
- `contraejemplo.{pdf,png}` — the four inequalities drawn: docs/part2/f2_ibk1_derivation.md section 4.2 (re-computed here in exact rationals from src/problems_native.py's coefficients and asserted equal)
- `ibk1_crisp.{pdf,png}` — I-BK1 stated: where each objective pulls, the band a level of an interval objective occupies, and the curve of constant nu that is its efficient set without uncertainty
- `ibk1_cunas.{pdf,png}` — the bands of results/part2/exact_regions_ibk1.csv drawn between the hyperbolas nu = const; areas checked against the same file
