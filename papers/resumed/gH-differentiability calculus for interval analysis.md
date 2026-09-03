# [10] Stefanini et al. 2025 — gH-Differentiability Calculus

> **Source:** Stefanini, L., Arana-Jiménez, M., & Sorini, L. (2025). Fréchet and Gateaux gH-differentiability for interval valued functions of multiple variables. *Information Sciences*, 691, 121601. https://doi.org/10.1016/j.ins.2024.121601

---

## 1. Core claim

The paper introduces a new concept of **gH-linearity** for interval-valued (IV) functions of multiple variables, defined via equivalence classes of a vector space, and uses it as the "target class" for Fréchet-type and Gateaux-type gH-differentiability. This unifies and extends prior definitions of gH-differentiability (notably Stefanini & Arana-Jiménez 2019 and Roy et al. 2024), which either lacked a proper linearity concept or used Minkowski-type combinations of partial derivatives that fail to produce correct directional derivatives in general. The paper also extends these concepts to vector IV-functions (defining the gH-Jacobian) and to second-order differentiability (the gH-Hessian matrix).

---

## 2. What is the gH-difference?

**Definition as stated (Section 2):**

> A ⊖_gH B = C ⟺ (a) A = B ⊕_M C, or (b) B = A ⊕_M (−1)C.

The gH-difference always exists and is given explicitly by:

> A ⊖_gH B = [min{a − b, ā − b̄}, max{a − b, ā − b̄}] = (â − b̂; |ã − b̃|)

where â, b̂ are midpoints and ã, b̃ are radii (half-widths).

**Plain sentence:** The gH-difference of two intervals is always an interval whose midpoint is the difference of midpoints and whose radius is the absolute difference of radii.

**Code-level formula:**

```python
def gH_diff(a_l, a_u, b_l, b_u):
    mid_a = (a_l + a_u) / 2
    rad_a = (a_u - a_l) / 2
    mid_b = (b_l + b_u) / 2
    rad_b = (b_u - b_l) / 2
    result_mid = mid_a - mid_b
    result_rad = abs(rad_a - rad_b)
    return [result_mid - result_rad, result_mid + result_rad]
```

This is equivalent to: `[min(a_l − b_l, a_u − b_u), max(a_l − b_l, a_u − b_u)]`. The two cases from the definition correspond to whether rad_a ≥ rad_b (case a, Hukuhara-type) or rad_a < rad_b (case b, reversed), but the formula handles both uniformly via the absolute value.

---

## 3. What is gH-differentiability?

**Fréchet gH-differentiability (Definition 29):** An IV-function F : K ⊆ ℝⁿ → I(ℝ), written F(x) = (f̂(x); f̃(x)), is Fréchet gH-differentiable at a point x⁽⁰⁾ ∈ K if and only if there exists a continuous **gH-linear** function L_{x⁽⁰⁾} : ℝⁿ → I(ℝ) such that the Hausdorff norm of the double gH-difference `(F(x⁽⁰⁾ + h) ⊖_gH F(x⁽⁰⁾)) ⊖_gH L_{x⁽⁰⁾}(h)`, divided by ‖h‖, goes to zero as ‖h‖ → 0.

In words: F is Fréchet gH-differentiable at x⁽⁰⁾ when there exists a gH-linear IV-function that approximates increments of F (measured via gH-difference) to first order in the Hausdorff metric. The approximating function L must be gH-linear — meaning of the form L(x) = (l̂ᵀx; |w̃ᵀx|) for fixed vectors l̂, w̃ ∈ ℝⁿ — not merely Minkowski-linear.

**Equivalent characterization (Theorem 34):** F = (f̂; f̃) is Fréchet gH-differentiable at x⁽⁰⁾ **if and only if** f̂ is Fréchet differentiable (in the ordinary sense) at x⁽⁰⁾, **and** f̃ is "abs-differentiable" at x⁽⁰⁾ — meaning |f̃| has a classical Fréchet derivative there.

**Gateaux gH-differentiability (Definition 35):** F is Gateaux gH-differentiable at x⁽⁰⁾ if for all directions h ∈ ℝⁿ, the limit of `(F(x⁽⁰⁾ + th) ⊖_gH F(x⁽⁰⁾)) / t` as t → 0 exists and equals a continuous gH-linear function L(h). Fréchet gH-differentiability implies Gateaux gH-differentiability; the converse does not hold.

---

## 4. Why does this matter for optimization?

The paper states that gH-differentiability enables the construction of gradient-based descent directions for IV-functions. Specifically, Section 6.2 states:

> "the existence of descent directions for the ordinary function f̂(x) (the midpoint component of F(x)) is sufficient to the existence of decreasing directions for F(x) (with respect to the partial LU-order)"

The paper explicitly claims that gH-differentiability provides the theoretical basis for obtaining non-dominated solutions to IV-minimization problems, and states that further work is planned on "a related algorithm to obtain non-dominated solutions to IV-minimization problems." It also cites Roy et al. 2024 as having applied gH-differentiability to a gradient-based descent for interval-valued optimization with finance applications — but shows that Roy et al.'s definition is more restrictive and incorrect in general (their expression (36) is not fulfilled by functions that are correctly gH-differentiable under Definition 29).

The paper does **not** itself derive or validate a complete gradient-based optimization algorithm. What it establishes is that the gH-gradient ∇_gH F(x⁽⁰⁾) — a vector of intervals — exists when F is gH-differentiable, and that the gH-differential function (not merely the gradient vector) is needed to correctly compute directional derivatives.

---

## 5. Theorems we keep in mind

| Theorem | Statement | Why it matters |
|---|---|---|
| **Theorem 34** | F = (f̂; f̃) is Fréchet gH-differentiable at x⁽⁰⁾ iff f̂ is Fréchet differentiable and f̃ is abs-differentiable at x⁽⁰⁾. | Gives a computable, component-wise criterion: check two real-valued functions independently. This is the theorem you use to verify gH-differentiability in code. |
| **Theorem 36** | If F is Fréchet gH-differentiable at x⁽⁰⁾, then F is continuous at x⁽⁰⁾. | Standard sanity check: differentiability implies continuity, as in classical analysis. |
| **Theorem 37** | If F is gH-linear, then F is Fréchet gH-differentiable everywhere and its gH-differential is F itself. | Confirms that the class of gH-linear functions is self-consistent; linear IV-functions behave exactly as in classical calculus. |
| **Theorem 44** | If F is Gateaux gH-differentiable at x⁽⁰⁾ and f̃ has all standard partial derivatives there, then the directional gH-derivative equals the gH-differential applied to the direction: ∂_gH F(x⁽⁰⁾; d) = D_gH F(x⁽⁰⁾)(d). | Connects Gateaux derivatives to the differential operator; validates that partial gH-derivatives assemble into the full differential. |
| **Theorem 45** | If F is gH-differentiable at x⁽⁰⁾, then all partial gH-derivatives exist at x⁽⁰⁾ and equal the gH-differential evaluated at canonical directions. | Establishes that gH-differentiability is strictly stronger than existence of partial derivatives, and gives explicit formulas for the gH-gradient components. |
| **Theorem 49** | If F is Fréchet gH-differentiable at x⁽⁰⁾, then the components w̃_j of the gH-differential are determined by the signed one-sided partial derivatives of f̃. | Gives the algorithm for computing the gH-differential from computable quantities (one-sided partial derivatives of the radius function). |
| **Theorem 55** | The gH-tangency function P* is inclusion-minimal among all IV-functions satisfying the first-order tangency condition at x⁽⁰⁾. | Proves that the gH-differential gives the tightest possible first-order interval approximation, justifying its use as the analogue of the classical gradient. |
| **Proposition 46** | A Minkowski combination of n intervals F(x) = Σ x_j A_j is Fréchet gH-differentiable at x⁽⁰⁾ provided x_j⁽⁰⁾ = 0 implies ã_j = 0 for all j. | Identifies precisely where Minkowski-type IV-functions fail to be gH-differentiable (at the origin when intervals have nonzero width), which is the critical obstruction for optimization. |
| **Proposition 59** | F = (f̂; f̃) is LU-convex iff \|αf̃(x) + βf̃(y) − f̃(αx+βy)\| ≤ αf̂(x) + βf̂(x) − f̂(αx+βy); F is inclusion-convex iff the inequality is reversed. | Characterizes both notions of convexity in terms of the component functions; needed for establishing optimality conditions. |

---

## 6. What this paper does NOT do

- **No algorithm implementation.** The paper contains no pseudocode, no numerical optimization routine, and no solver for interval-valued problems.
- **No benchmark testing.** There are no experiments on test functions, no performance comparisons, and no numerical results beyond illustrative analytic examples (Examples 56, 60–62, 67).
- **No connection to NSGA-II or PSO.** These algorithms are not mentioned anywhere in the paper. The paper is purely theoretical calculus.
- **No connection to evolutionary or swarm computation.** The paper does not discuss metaheuristics, population-based methods, or any computational intelligence technique.
- **No automorphism-based ordering (φ-automorphisms).** The ordering framework used in φ-automorphism research is not the subject of this paper; it uses LU-order and inclusion order only.
- **No portfolio optimization or applied finance examples.** The only connection to finance is a citation of Roy et al. 2024, who applied gH-differentiability to a finance problem; the present paper does not itself do this.
- **No treatment of constrained optimization.** KKT conditions are mentioned as future work direction (citing Stefanini & Arana-Jiménez 2019 [45]), but are not derived here.
- **No multiobjective Pareto front analysis.** Pareto fronts and non-dominated solution sets are mentioned in the concluding section as planned future work, not results of this paper.

---

## 7. Citation summary

Stefanini, Arana-Jiménez, and Sorini (2025) established the concept of gH-linearity for interval-valued functions of multiple variables and used it to define rigorous Fréchet and Gateaux gH-differentiability, proving that differentiability reduces to component-wise conditions on the midpoint and radius functions and providing the theoretical basis for gradient-based analysis of interval optimization problems.

---

## 8. Flags

- **Abs-differentiability (Definition 30)** is a non-standard concept introduced in this paper with no prior literature citation. It is defined clearly but may not appear in other sources you read — do not assume other papers use the same term.
- **The vector space 𝒜 and equivalence classes** (Section 3) involve non-standard algebraic machinery (the space 𝒱 of pairs (x, |x|), quotient sets, sign pattern matrices). This is foundational to the paper's definition of gH-linearity but you do not need to implement it — just know that gH-linear functions have the form L(x) = (l̂ᵀx; |w̃ᵀx|).
- **Section 4.3 (convexity)** is self-contained but the connection between convexity and optimization (e.g., sufficient conditions for minima) is deferred to future work. Do not over-cite this section for algorithmic purposes.
- **Figure 2 and Figure 3** are referenced extensively in Example 56 but the figures themselves were not fully interpretable from the PDF rendering. The mathematical conclusions of the example are stated in text and are followable.
- **The gH-Hessian (Section 5.2)** is outlined for the single-variable case first, then generalized. The definition of second-order gH-differentiability (Definition 65) requires understanding the first-order theory fully before it is meaningful — do not cite it in isolation.
- **Roy et al. [36]** is explicitly shown to be incorrect (their expression (36) fails on a concrete example in Remark 43). If your literature review cites Roy et al., note this paper's critique.
