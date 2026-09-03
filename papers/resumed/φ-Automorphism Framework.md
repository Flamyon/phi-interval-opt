# [1] Costa et al. 2024 — φ-Automorphism Framework

---

## 1. Core claim

The paper introduces a unified framework for multiobjective interval optimization built on a family of preference order relations on intervals, each parameterized by a bijection φ on ℝ²ᵐ. The main contribution is showing that previously disparate interval order relations (LU, LS, CW) used across the literature are all special cases of a single φ-indexed family. The paper also proves that solving a φ-multiobjective interval optimization problem is equivalent to solving a classical real-valued multiobjective optimization problem, which means standard tools (scalarization, KKT conditions) apply directly.

---

## 2. What is φ (automorphism)?

φ is a bijection — a one-to-one and onto function — from ℝ²ᵐ to ℝ²ᵐ. The paper works with a specific family of such bijections called **𝒜ᵐ**, where each φ decomposes as a product of m independent 2×2 linear maps, one per interval component.

Concretely, each component automorphism φᵢ : ℝ² → ℝ² acts on a pair (lower bound, upper bound) of a single interval and produces a new pair of real numbers via a linear transformation:

```
φᵢ(x₂ᵢ₋₁, x₂ᵢ) = (λ₂ᵢ₋₁ · x₂ᵢ₋₁ + λ₂ᵢ · x₂ᵢ,  β₂ᵢ₋₁ · x₂ᵢ₋₁ + β₂ᵢ · x₂ᵢ)
```

where λ and β are real constants chosen by the decision maker, subject to the condition λ₂ᵢ₋₁β₂ᵢ ≠ λ₂ᵢβ₂ᵢ₋₁ (i.e., the 2×2 matrix is invertible).

**Operationally:** applying φ to an interval [a, ā] means computing two linear combinations of its lower and upper bounds and treating the result as a pair of real numbers. φ is a **re-encoding** of the interval into ℝ². Different choices of the λ and β coefficients encode different semantic views of what matters about an interval — for example, just its endpoints, its center and width, or its lower bound and spread.

---

## 3. The family of interval orders ≤_φ

**Definition (from the paper, Eq. 3):**

For φ ∈ 𝒜ᵐ, the preference order relation ≦_φ on (𝒦_C)ᵐ (m-tuples of closed bounded intervals) is:

```
(A₁, …, Aₘ) ≦_φ (B₁, …, Bₘ)
  ⟺  φ̄ᵢ(Aᵢ) ≦ φ̄ᵢ(Bᵢ)  for all i ∈ {1, …, m}
```

where φ̄ᵢ([a, ā]) = φᵢ(a, ā) ∈ ℝ², and ≦ on ℝ² means componentwise (both coordinates of the image are ≤).

**Plain sentence:** A compares as ≤_φ to B if and only if, after re-encoding each interval pair through φ, the resulting real vectors satisfy the standard componentwise order in ℝ².

---

## 4. Concrete φ examples

The paper names four explicit φ instances, all in 𝒜ᵐ (applied identically across all m components).

---

### Example 2.2 — LU order (lower-upper, identity)

- **Produces:** LU-convexity / LU-preference order (type-I Pareto in Wu 2009 [31])
- **Formula:**
  ```
  φᵢ(x₂ᵢ₋₁, x₂ᵢ) = (x₂ᵢ₋₁, x₂ᵢ)
  with λ₂ᵢ₋₁=1, λ₂ᵢ=0, β₂ᵢ₋₁=0, β₂ᵢ=1
  ```
- **Induced order:** [a, ā] ≦_φ [b, b̄]  ⟺  a ≤ b  AND  ā ≤ b̄
  (compare lower bounds and upper bounds separately)

---

### Example 2.3 — LS order (lower-spread)

- **Produces:** LS-convexity / LS-Pareto (coincides with Singh et al. 2016 [26])
- **Formula:**
  ```
  φᵢ(x₂ᵢ₋₁, x₂ᵢ) = (x₂ᵢ₋₁, x₂ᵢ − x₂ᵢ₋₁)
  with λ₂ᵢ₋₁=1, λ₂ᵢ=0, β₂ᵢ₋₁=−1, β₂ᵢ=1
  ```
- **Induced order:** [a, ā] ≦_φ [b, b̄]  ⟺  a ≤ b  AND  (ā − a) ≤ (b̄ − b)
  (compare lower bound and interval width)

---

### Example 2.4 — CW order (center-width)

- **Produces:** CW-convexity / type-II Pareto (coincides with Wu 2009 [31])
- **Formula:**
  ```
  φᵢ(x₂ᵢ₋₁, x₂ᵢ) = ((x₂ᵢ₋₁ + x₂ᵢ)/2,  (x₂ᵢ − x₂ᵢ₋₁)/2)
  with λ₂ᵢ₋₁=½, λ₂ᵢ=½, β₂ᵢ₋₁=−½, β₂ᵢ=½
  ```
- **Induced order:** [a, ā] ≦_φ [b, b̄]  ⟺  center(A) ≤ center(B)  AND  half-width(A) ≤ half-width(B)

---

### Example 2.1 — Car purchase (four-component mixed φ)

- **Produces:** A custom mixed order for comparing 4-tuples of intervals encoding purchase price, fuel economy, sale price, and year of production
- Each φᵢ is chosen differently to reflect the distinct semantics of each component:
  - φ₁: upper bound and average (for purchase price)
  - φ₂: spread and negated upper bound (for fuel economy)
  - φ₃: half-spread and negated upper bound (for sale price)
  - φ₄: negated both bounds (for year of production — older is worse)
- **Significance:** illustrates that φ need not be uniform across components; different interval components can be ordered by different criteria simultaneously.

---

## 5. What changes when you change φ?

The paper claims — and proves (Theorems 3.1, 3.2) — that the set of optimal solutions to a φ-multiobjective interval optimization problem depends directly on φ. Specifically:

- An optimal solution x̄ for problem (1MIOP_φ) is **exactly** an efficient solution of the transformed real-valued problem (MOP_φ), which minimizes the vector (φ̄ ∘ F)(x). Changing φ changes the objectives of this real-valued problem, and therefore changes which points are Pareto-efficient.

- The paper gives an explicit example (Proposition 5.1) where an optimal solution under φ (LU order, Example 2.2) is also optimal under ψ (LS order, Example 2.3), showing a one-directional inclusion relationship between solution sets for these two specific φ choices.

- More broadly, the paper establishes that every previously published interval order (LU, LS, CW) yields a different problem formulation and potentially different solution set — all are special cases of this framework.

**What the paper does NOT provide:** a general characterization of how solution sets differ across arbitrary φ₁ vs φ₂. Only specific inclusions and equivalences for the named examples are established.

---

## 6. Connection to multiobjective optimization

The paper proves that every φ-interval optimization problem reduces exactly to a classical real-valued multiobjective problem. The key construction is the composition:

```
φ̄ ∘ F : S → ℝ²ᵐ
```

which converts an interval-valued objective F into a 2m-dimensional real vector objective. The paper states:

> "solving (1MIOP_φ) and (2MIOP_φ) is equivalent to solving a classical multiobjective optimization problem"

**Mechanically:** each interval Fᵢ(x) = [f_i(x), f̄ᵢ(x)] is mapped by φᵢ to a pair of real-valued objectives:

```
(λ₂ᵢ₋₁ · f_i + λ₂ᵢ · f̄ᵢ,   β₂ᵢ₋₁ · f_i + β₂ᵢ · f̄ᵢ)
```

The interval comparison ≦_φ becomes componentwise dominance in ℝ²ᵐ, so standard Pareto optimality applies. Concretely:

| φ choice | Real objectives produced |
|----------|--------------------------|
| LU (Ex 2.2) | Minimize lower bound AND upper bound separately |
| LS (Ex 2.3) | Minimize lower bound AND interval width |
| CW (Ex 2.4) | Minimize center AND half-width |

The choice of φ determines which linear combinations of (f_i, f̄ᵢ) become the actual real-valued objectives fed to the optimizer.

---

## 7. What this paper does NOT do

The paper is explicitly theoretical. It does not:

- Implement any algorithm or run any numerical experiments
- Apply NSGA-II, PSO, or any evolutionary or swarm algorithm
- Analyze or compare Pareto fronts computationally across different φ choices
- Give conditions under which one φ yields a strictly larger or smaller Pareto front than another (beyond the single special case in Proposition 5.1)
- Prove general sensitivity results: how solutions change continuously as λ and β parameters are varied
- Address how to choose φ optimally or appropriately for a given application
- Handle non-convex problems (optimality conditions rely on φ-convexity assumptions throughout)
- Provide any portfolio optimization or financial application (all examples are abstract or generic)
- Prove anything about computational complexity or convergence of solvers under different φ

---

## 8. Citation summary

Costa et al. (2024) established a unified framework of φ-parameterized preference orders on intervals, proving that classical interval orders (LU, LS, CW) are special cases and that every φ-multiobjective interval optimization problem reduces exactly to a standard real-valued multiobjective problem, enabling direct application of KKT conditions and scalarization [Costa, Osuna-Gómez, Chalco-Cano, *Fuzzy Sets and Systems* 477 (2024) 108812].

---

## 9. Flags

| Issue | Detail |
|-------|--------|
| φ̄ vs φ notation | The paper uses both φ : ℝ²ᵐ → ℝ²ᵐ and φ̄ : (𝒦_C)ᵐ → ℝ²ᵐ. φ̄ is the "lift" of φ that acts on tuples of intervals by treating (lower, upper) as coordinates. Not confusing once understood, but the overloaded notation requires careful tracking. |
| 𝒜ᵐ vs general bijections | The paper distinguishes between arbitrary bijections φ (Definition 2.1) and the specific class 𝒜ᵐ of product automorphisms. Most results use 𝒜ᵐ, but this distinction is not always clearly flagged in theorem statements. |
| Proposition 5.1 (solution set inclusion) | The proof shows LU-optimal implies LS-optimal for fuzzy problems. The paper does not state whether the converse holds or whether this is a strict inclusion. The gap is not flagged by the authors. |
| Section 4 (fuzzy intervals) | Extension to fuzzy intervals adds substantial notation (α-level sets, membership functions). The core logic mirrors the interval case exactly, but tracking the α-parameterization through proofs requires sustained attention. |
| Appendix proofs | Proofs of Theorems 5.2 and 5.3 are structurally identical to Theorems 3.1 and 3.2, as the authors note. No parsing issues. |

