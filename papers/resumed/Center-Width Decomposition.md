# [9] Ishibuchi & Tanaka 1990 — Center-Width Decomposition

**Source:** Ishibuchi, H. & Tanaka, H. (1990). "Multiobjective programming in optimization of the interval objective function." *European Journal of Operational Research*, 48, 219–225.

---

## 1. Core Claim

The paper addresses the mathematical programming problem where objective function coefficients are uncertain and represented as closed intervals rather than fixed values. The central contribution is converting a single-objective interval optimization problem into a real-valued multiobjective problem by using order relations on intervals defined via their left limit, right limit, center, and width. Solutions to the interval problem are then defined as the Pareto optimal (nondominated) solutions of the resulting multiobjective problem, which can be solved with standard methods.

---

## 2. The Interval Order Relations Defined

The paper defines four order relations in total: two for maximization problems (Section 3.1) and two for minimization problems (Section 3.2). It also introduces two auxiliary combined relations in Section 4 to simplify definitions.

---

### 2.1 Order Relations for Maximization Problems

**Relation 1: ≤_LR (left-right order for maximization)**

- **Formal definition:** Given A = [a_L, a_R] and B = [b_L, b_R]:
  - A ≤_LR B  iff  a_L ≤ b_L  and  a_R ≤ b_R  (Definition 3.1, eq. 3.1)
  - A <_LR B  iff  A ≤_LR B  and  A ≠ B  (eq. 3.2)
- **Plain-language meaning:** Interval A is "no better than" interval B for profit when both the minimum possible profit (left limit) and the maximum possible profit (right limit) of A are at most those of B. The decision maker prefers higher minimum and higher maximum profit.
- **Properties stated:** It is a partial order (transitive, reflexive, antisymmetric). If A ≤_LR B, then a_C ≤ b_C (centers are ordered too). Reduces to ordinary ≤ when intervals are degenerate (a_L = a_R).
- **Limitation noted by authors:** Many interval pairs cannot be compared under ≤_LR. Example given: A = [100, 200], B = [160, 180] — neither A ≤_LR B nor B ≤_LR A holds, yet B is intuitively preferable (higher minimum, less spread). This motivates Relation 2.
- **Correspondence to φ:** The paper does not use φ-automorphism language. This relation corresponds to requiring dominance in both endpoints simultaneously — it is the most conservative (lexicographic in both limits).

---

**Relation 2: ≤_CW (center-width order for maximization)**

- **Formal definition:** Given A = ⟨a_C, a_W⟩ and B = ⟨b_C, b_W⟩:
  - A ≤_CW B  iff  a_C ≤ b_C  and  a_W ≥ b_W  (Definition 3.2, eq. 3.3)
  - A <_CW B  iff  A ≤_CW B  and  A ≠ B  (eq. 3.4)
- **Plain-language meaning:** For profit maximization, A is "no better than" B when B has a higher or equal expected value (center) AND lower or equal uncertainty (width). The decision maker prefers higher expected profit and less uncertainty. Note the asymmetry: center must go up, width must go down.
- **Properties stated:** Also a partial order. If A ≤_CW B, then a_L ≤ b_L (left limits are also ordered). Reduces to ordinary ≤ when both widths are zero.
- **Key result (Proposition 3.1):** ≤_LR and ≤_CW never conflict. If A ≤_LR B and B ≤_CW A simultaneously, then A = B. They are consistent partial orders.
- **Correspondence to φ:** This is the relation that the center-width decomposition directly implements. The center is the "expected value" interpretation of an interval; the width is "uncertainty."

---

### 2.2 Order Relations for Minimization Problems

**Relation 3: ≤*_LR (left-right order for minimization)**

- **Formal definition:** Given A = [a_L, a_R] and B = [b_L, b_R]:
  - A ≤*_LR B  iff  a_L ≤ b_L  and  a_R ≤ b_R  (Definition 3.3, eq. 3.9)
  - A <*_LR B  iff  A ≤*_LR B  and  A ≠ B  (eq. 3.10)
- **Plain-language meaning:** For cost minimization, A is preferred to B when both the minimum cost and the maximum cost of A are at most those of B (lower is better in both limits). The authors explicitly note this is the same formal relation as ≤_LR — the difference is interpretational, not mathematical.
- **Correspondence to φ:** Identical to ≤_LR structurally.

---

**Relation 4: ≤*_CW (center-width order for minimization)**

- **Formal definition:** Given A = ⟨a_C, a_W⟩ and B = ⟨b_C, b_W⟩:
  - A ≤*_CW B  iff  a_C ≤ b_C  and  a_W ≤ b_W  (Definition 3.4, eq. 3.11)
  - A <*_CW B  iff  A ≤*_CW B  and  A ≠ B  (eq. 3.12)
- **Plain-language meaning:** For cost minimization, A is preferred to B when A has a lower or equal expected cost (center) AND lower or equal uncertainty (width). Both center and width go in the same direction (down), unlike ≤_CW where they go in opposite directions.
- **Critical distinction:** ≤*_CW ≠ ≤_CW. For profit, you want width to decrease (less risk around a high center is better). For cost, you also want width to decrease (less cost uncertainty is better), but center should also decrease. The directions of both components differ from the maximization case.
- **Properties:** Also a partial order. If A ≤*_CW B, then a_R ≤ b_R (right limits ordered). Reduces to ordinary ≤ when widths are zero.
- **Key result (Proposition 3.2):** ≤*_LR and ≤*_CW never conflict (same logic as Proposition 3.1).

---

### 2.3 Auxiliary Combined Relations (Section 4)

**Relation 5: ≤_LC (combined for maximization)**

- **Formal definition:**
  - A ≤_LC B  iff  a_L ≤ b_L  and  a_C ≤ b_C  (eq. 4.1)
  - A <_LC B  iff  A ≤_LC B  and  A ≠ B  (eq. 4.2)
- **Purpose:** Simplifies the solution definition. Proposition 4.1 shows:
  - A ≤_LC B  iff  A ≤_LR B  or  A ≤_CW B
  - A <_LC B  iff  A <_LR B  or  A <_CW B
- So ≤_LC is the union of ≤_LR and ≤_CW. A solution x is nondominated if no x' satisfies Z(x) <_LC Z(x').

**Relation 6: ≤*_RC (combined for minimization)**

- **Formal definition:**
  - A ≤*_RC B  iff  a_R ≤ b_R  and  a_C ≤ b_C  (eq. 4.15)
  - A <*_RC B  iff  A ≤*_RC B  and  A ≠ B  (eq. 4.16)
- **Purpose:** Same unification role for minimization. Proposition 4.2 shows:
  - A ≤*_RC B  iff  A ≤*_LR B  or  A ≤*_CW B

---

## 3. The Center-Width Transformation (The Key Method)

Given an interval objective function Z(x) = A_1 x_1 + A_2 x_2 + ... + A_n x_n where each A_i = ⟨a_{Ci}, a_{Wi}⟩:

**Center:**
```
f_C(x) = z_C(x) = a_{C1} x_1 + a_{C2} x_2 + ... + a_{Cn} x_n     (eq. 4.12)
```

**Width (left limit, for x ≥ 0):**
```
f_L(x) = z_L(x) = (a_{C1} x_1 + ... + a_{Cn} x_n) - (a_{W1} x_1 + ... + a_{Wn} x_n)
        = z_C(x) - (a_{W1} x_1 + ... + a_{Wn} x_n)               (eq. 4.13, for x ≥ 0)
```

The general form without assuming x ≥ 0 is:
```
z_L(x) = (a_{C1} x_1 + ... + a_{Cn} x_n) - (a_{W1}|x_1| + ... + a_{Wn}|x_n|)  (eq. 4.11)
```

**How it transforms the problem:** The single interval-valued objective Z(x) is replaced by two real-valued objectives:
- z_L(x): the left limit of Z(x) — interpreted as the worst-case profit
- z_C(x): the center of Z(x) — interpreted as the average/expected profit

Both must be maximized simultaneously. The Pareto front of this real two-objective problem is exactly the solution set of the interval problem (Definition 4.2).

For minimization, the analogous pair is:
- z_R(x): the right limit — worst-case cost
- z_C(x): the center — average cost

Both minimized simultaneously (eq. 4.21).

**Python function:**

```python
def interval_to_objectives(x, centers, widths, mode="maximize"):
    """
    Transform an interval objective Z(x) = sum_i A_i x_i into two real objectives.

    Parameters
    ----------
    x       : list or array of decision variable values (assumed >= 0)
    centers : list of a_{Ci}, the center of each interval coefficient A_i
    widths  : list of a_{Wi}, the width of each interval coefficient A_i
    mode    : "maximize" returns (z_L, z_C) to maximize
              "minimize" returns (z_R, z_C) to minimize

    Returns
    -------
    Two real-valued objectives as a tuple.
    """
    z_C = sum(centers[i] * x[i] for i in range(len(x)))           # eq. 4.12
    uncertainty_term = sum(widths[i] * abs(x[i]) for i in range(len(x)))

    if mode == "maximize":
        z_L = z_C - uncertainty_term                               # eq. 4.11 / 4.13
        return z_L, z_C
    elif mode == "minimize":
        z_R = z_C + uncertainty_term                               # eq. 4.19 / 4.20
        return z_R, z_C
    else:
        raise ValueError("mode must be 'maximize' or 'minimize'")


def reconstruct_interval(x, centers, widths):
    """
    Reconstruct the full interval Z(x) = [z_L, z_R] = <z_C, z_W>.
    """
    z_C = sum(centers[i] * x[i] for i in range(len(x)))
    z_W = sum(widths[i] * abs(x[i]) for i in range(len(x)))
    z_L = z_C - z_W
    z_R = z_C + z_W
    return z_L, z_R, z_C, z_W
```

---

## 4. The Multiobjective Formulation

**Original interval problem (maximization, eq. 1.1):**
```
max Z(x) = A_1 x_1 + A_2 x_2 + ... + A_n x_n
subject to: x ∈ S ⊆ R^n
```
where each A_i is a closed interval.

**Transformed multiobjective problem (eq. 4.14):**
```
max  ( z_L(x),  z_C(x) )
subject to: x ∈ S ⊆ R^n
```
where:
- z_L(x) = sum_i a_{Ci} x_i  -  sum_i a_{Wi} |x_i|   [eq. 4.11; simplified to eq. 4.13 for x ≥ 0]
- z_C(x) = sum_i a_{Ci} x_i                            [eq. 4.12]
- Constraints are unchanged from the original problem S.

**Solution definition (Definition 4.2):** x ∈ S is a solution of the interval problem if and only if there is no x' ∈ S such that Z(x) <_LC Z(x'). Equivalently: x is Pareto optimal in the two-objective real problem.

**For minimization (eq. 4.21):**
```
min  ( z_R(x),  z_C(x) )
subject to: x ∈ S ⊆ R^n
```
where:
- z_R(x) = sum_i a_{Ci} x_i  +  sum_i a_{Wi} |x_i|   [eq. 4.19; simplified to eq. 4.20 for x ≥ 0]
- z_C(x) = sum_i a_{Ci} x_i                            [eq. 4.12]

**Key observation:** z_C(x) appears in both objectives of the maximization formulation (eq. 4.14) and also in both objectives of the minimization formulation (eq. 4.21). The two objectives are not independent — they share the center term and differ only in the sign of the uncertainty term.

**Symmetry property (Proposition 4.3):** Maximizing Z(x) and minimizing -Z(x) yield the same solution set. This mirrors the standard max/min equivalence in ordinary programming.

---

## 5. What the Paper Proves or Shows Empirically

### Theoretical Results

**Proposition 3.1:** If A ≤_LR B and B ≤_CW A simultaneously, then A = B. Proved analytically from the definitions. Consequence: the two maximization order relations are consistent (they never produce contradictory preference rankings).

**Proposition 3.2:** Same result for the minimization order relations ≤*_LR and ≤*_CW. Proof omitted (stated to follow the same argument as Proposition 3.1).

**Proposition 4.1:** A ≤_LC B  iff  A ≤_LR B  or  A ≤_CW B. Proved in full. Consequence: the combined relation ≤_LC unifies the two maximization orders, allowing Definition 4.1 to be simplified to Definition 4.2.

**Proposition 4.2:** Analogous result for minimization: A ≤*_RC B  iff  A ≤*_LR B  or  A ≤*_CW B. Proof stated to follow from Proposition 4.1's argument.

**Proposition 4.3:** The solution sets of max Z(x) and min -Z(x) coincide (in the interval sense). Proved via eq. 4.23–4.26 by showing Z(x) <_LC Z(x')  iff  -Z(x') <*_RC -Z(x).

### Numerical Experiments

**Example 1 — Binary product-mix problem (Problem 1, Section 5):**
- 6 binary decision variables, 1 resource constraint (eq. 5.4–5.6)
- Interval coefficients given as [a_L, a_R] pairs
- Solved by full enumeration (problem is small)
- Two Pareto optimal solutions found:
  - x^a = (0,1,0,1,1,0): Z(x^a) = [1850, 2215] = ⟨2032.5, 182.5⟩ — high minimum profit, low expected value
  - x^b = (0,1,0,1,0,1): Z(x^b) = [1695, 2515] = ⟨2105, 410⟩ — high expected value, low minimum profit
- Conclusion: the two solutions are incomparable under the order relations; the choice between them is left to the decision maker. This illustrates the irreducible subjectivity in interval comparison.

**Example 2 — Continuous LP with interval objective (Problem 2, Section 5):**
- 3 continuous variables (x ≥ 0), 3 resource constraints (eq. 5.12–5.16)
- Multiobjective problem MP2 solved via the weighted-sum (scalarization) method [LP2]:
  - max  w·z_L(x) + (1-w)·z_C(x)  subject to the same constraints (eq. 5.20)
  - w varied from 0 to 1
- Three Pareto optimal solutions identified:
  - x^a = (0, 1.13, 3.45): Z(x^a) = [51.4, 126.2] = ⟨88.8, 37.4⟩
  - x^b = (3.48, 0, 1.39): Z(x^b) = [66.1, 100.8] = ⟨83.4, 17.3⟩
  - x^c = (4.57, 0, 0):   Z(x^c) = [68.5, 77.6]  = ⟨73.0, 4.57⟩
- The trade-off is explicit: x^a has the highest expected value but highest uncertainty; x^c has the lowest uncertainty but lowest expected value. Again, final selection is decision-maker-dependent.

---

## 6. What You Implement from This Paper

The following are the direct implementation targets for the computational project:

| Item | What to implement | Equation(s) |
|---|---|---|
| **Interval representation** | Store each interval coefficient A_i as (center, width) pair | eq. 2.3, 2.4 |
| **z_C(x) — center objective** | Dot product of centers with x | eq. 4.12 |
| **z_L(x) — left limit objective** | z_C(x) minus weighted widths (for maximization; assume x ≥ 0) | eq. 4.13 |
| **z_R(x) — right limit objective** | z_C(x) plus weighted widths (for minimization; assume x ≥ 0) | eq. 4.20 |
| **Maximization formulation** | Two-objective problem: max(z_L, z_C) | eq. 4.14 |
| **Minimization formulation** | Two-objective problem: min(z_R, z_C) | eq. 4.21 |
| **Pareto front = solution set** | Use pymoo's NSGA-II to find the Pareto front of the two-objective real problem | Definition 4.2 / 4.4 |
| **Interval reconstruction** | From (center, width) pairs, recover [z_L, z_R] for reporting | eq. 2.1, 2.2 |

**What you do NOT need to implement from this paper:**
- The order relations themselves (≤_LR, ≤_CW, etc.) — pymoo handles Pareto dominance automatically on the real objectives; the order relations are the theoretical justification, not an algorithmic component.
- The enumeration method used in Example 1 — NSGA-II replaces this.
- The weighted-sum scalarization (LP2) — NSGA-II finds the full Pareto front without scalarization.

---

## 7. Limitations Stated by the Authors

The paper is terse and the authors are largely silent on limitations. What can be extracted:

1. **Order relations are partial, not total.** Both ≤_LR and ≤_CW are partial orders. Many interval pairs remain incomparable. The solution set is therefore a set of Pareto-optimal alternatives, not a single optimal solution. Final selection among Pareto solutions requires additional preference information from the decision maker (explicitly stated in the conclusion of Example 1).

2. **Constraints are assumed real-valued.** The paper only handles interval coefficients in the objective function. Constraints are assumed to have fixed (deterministic) coefficients. The paper makes no claim about handling interval-valued constraints.

3. **Linear objective only.** The formulation max Z(x) = sum_i A_i x_i is linear in x. No extension to nonlinear interval objectives is discussed.

4. **Sign assumption.** The simplified forms of z_L (eq. 4.13) and z_R (eq. 4.20) — which drop the absolute value — require x ≥ 0. The paper notes this assumption explicitly. For problems where x may take negative values, the full forms with |x_i| (eq. 4.11, 4.19) must be used.

5. **No computational complexity analysis.** The paper provides no discussion of how the method scales with problem size. The numerical examples are small (6 variables, 3 variables).

6. **Weighted-sum scalarization is used for continuous LP, without justification of completeness.** In Example 2, the Pareto front is traced by varying w in LP2, but no proof is given that this recovers all Pareto-optimal solutions (weighted-sum methods miss non-convex parts of the Pareto front).

---

## 8. Python Sketch

```python
def center_width_from_bounds(a_L, a_R):
    """Convert [a_L, a_R] representation to (center, width). Eq. 2.3, 2.4."""
    a_C = 0.5 * (a_R + a_L)
    a_W = 0.5 * (a_R - a_L)
    return a_C, a_W


def interval_objectives_maximize(x, centers, widths):
    """
    Eq. 4.13 and 4.12. Assumes x >= 0.
    Returns (z_L, z_C) — both to be maximized.
    """
    z_C = sum(c * xi for c, xi in zip(centers, x))
    z_L = z_C - sum(w * xi for w, xi in zip(widths, x))
    return z_L, z_C


def interval_objectives_minimize(x, centers, widths):
    """
    Eq. 4.20 and 4.12. Assumes x >= 0.
    Returns (z_R, z_C) — both to be minimized.
    """
    z_C = sum(c * xi for c, xi in zip(centers, x))
    z_R = z_C + sum(w * xi for w, xi in zip(widths, x))
    return z_R, z_C


# --- pymoo integration sketch ---
# In pymoo, the problem's _evaluate method computes objectives for a batch of solutions.
# For maximization, negate objectives (pymoo minimizes by convention).

class IntervalObjectiveProblem:
    """
    Wraps the Ishibuchi-Tanaka decomposition for use with pymoo's NSGA-II.
    n_obj = 2 (z_L and z_C, both negated for minimization in pymoo).
    """

    def __init__(self, centers, widths, constraints_fn):
        self.centers = centers
        self.widths = widths
        self.constraints_fn = constraints_fn

    def evaluate(self, x):
        z_L, z_C = interval_objectives_maximize(x, self.centers, self.widths)
        # pymoo minimizes; negate to convert maximization to minimization
        return [-z_L, -z_C]

    def get_constraints(self, x):
        return self.constraints_fn(x)
```

---

## 9. Flags

**Ambiguities and potential issues encountered:**

1. **MP2 header in Example 2 (p. 225, eq. 5.17):** The paper writes `max. (z_L(x), z_C(x))` with subscript L in the first objective, consistent with the general formulation. However, the subscript on the first objective in the printed text appears to read `z_C` in some scans of this paper (likely a typo in the original or a scan artifact). Based on the definitions in Section 4.1, the first objective for maximization must be z_L(x) per eq. 4.14 — not a second copy of z_C. The numerical equations 5.18 and 5.19 confirm: 5.18 uses the left-limit coefficients (1000, 750, ...) and 5.19 uses the center coefficients (1070, 785, ...), matching eq. 4.13 and 4.12 respectively.

2. **No explicit φ-automorphism language.** The paper predates the φ-automorphism framework your supervisors are using. The order relations here (≤_LR, ≤_CW) are defined directly on intervals without reference to automorphisms. You will need to map these to φ-orders explicitly when connecting to your supervisors' framework. The ≤_CW relation (comparing via center and width) is the natural candidate for a "standard" φ corresponding to identity, while ≤_LR compares endpoints directly.

3. **The two objectives z_L and z_C are not independent.** Since z_L = z_C - uncertainty_term, the two objectives share z_C entirely. This means the Pareto front of the two-objective problem has a specific geometric structure (it is not a generic two-objective problem). Whether this causes numerical issues in NSGA-II is not discussed by the authors and worth monitoring in your experiments.

4. **Weighted-sum completeness gap (Example 2).** The paper uses the weighted-sum method to sweep the Pareto front in Example 2. This method is not guaranteed to find all Pareto-optimal solutions if the Pareto front is non-convex. Since NSGA-II is your implementation method, this is not a concern for you — NSGA-II handles non-convex fronts — but it is worth noting that the paper's own numerical method has this limitation.

5. **Section 6 conclusion contains a minor inconsistency.** The conclusion states the maximization multiobjective objectives are "to maximize the left limit and the center." This is correct per eq. 4.14. However, it then says "the minimization problem... objectives are to minimize the right limit and the center." This is also consistent with eq. 4.21. No contradiction, but the asymmetry (left limit for max, right limit for min) is worth flagging explicitly: the paper uses the worst-case limit in both cases — worst-case profit is the left limit; worst-case cost is the right limit.
