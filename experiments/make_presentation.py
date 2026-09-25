# make_presentation.py: every number and every data figure of the presentation,
# generated from results/ and never typed into the .tex.
#
# what this script is. presentation/presentacion.tex carries no literal number of
# the project's: it \input's the fragments this script writes under
# results/figures/presentation/fragments/, and it \includegraphics the figures
# this script draws under results/figures/presentation/. re-running the script
# regenerates both from the same csv files, so a number on a slide can always be
# traced to a file and a key, the rule of docs/plan_after_meeting.md section a2.
#
# where each number comes from. every fragment carries a latex comment naming the
# file and the key it was read from. the sources, slide by slide:
#     slide 5      docs/part1/a1_uncertainty_model.md (correlation under the
#                  proportional width), read by regular expression
#     slide 6      src/problems_tier0.py (p1's rho, delta and box)
#     slide 7      results/tier0/exact_regions_p1.csv
#     slide 10     results/tier0/instrument_error_p1.csv at budget 5000 and
#                  results/tier0/table_2_measured.csv at budget 20000, against
#                  results/tier0/exact_regions_p1.csv
#     slides 11-12 results/tier1/table_2_measured_eps_*.csv, decision block,
#                  pair (lu, cw), status finding, budget 5000, delta 0
#     slide 13     src/problems_native.py (I-BK1's printed coefficients)
#     slide 14     results/part2/exact_regions_ibk1.csv, and the nu of equation
#                  (25) from docs/part2/f2_ibk1_derivation.md section 4.1
#     slide 15     the coefficients of I-VU2 as [16] prints them and
#                  docs/part2/f7_ivu2_derivation.md transcribes them
#     slide 16     docs/part2/f2_ibk1_derivation.md section 4.2 (the four
#                  inequalities, re-computed here in exact rationals and asserted
#                  equal), results/part2/dominators_summary.csv
#     slide 17     results/part2/instrument_error_ibk1.csv (the range of the
#                  jaccard factors on I-BK1)
#     reserve      docs/explicacion_proyecto.md part 10 (the two counts of trap
#                  10.3 and 10.5), results/tier1/rank_one_summary.csv
#
# what this script checks before writing anything. the eight benchmark values of
# slide 11 fall in [0.628, 0.912]; the areas of the two drawn figures, integrated
# on the drawing grid, agree with the csv areas; the four inequalities of slide 16
# re-computed from the problem statement agree with the derivation's table to six
# decimals; and the containment-fixed coverages of the reserve slide are exactly
# 1 with zero range in every file they appear in. a failed check stops the script,
# so a stale fragment is never written over a good one.
#
# usage, from the repository root, with the repository's .venv:
#     .venv/bin/python experiments/make_presentation.py
# no arguments; idempotent.

import csv
import re
import sys
from fractions import Fraction
from pathlib import Path

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import Rectangle  # noqa: E402

repository = Path(__file__).resolve().parent.parent
source_directory = repository / "src"
if str(source_directory) not in sys.path:
    sys.path.insert(0, str(source_directory))

from problems_tier0 import p1_default_params, p1_lower, p1_upper  # noqa: E402
from problems_native import ibk1_coefficients, ibk1_lower, ibk1_upper, ibk1_shift  # noqa: E402
from problems_tier1 import (zdt1_n_vars, zdt1_n_obj, zdt1_width_drivers, evaluate_zdt1,  # noqa: E402
                            dtlz2_n_vars, dtlz2_n_obj, dtlz2_width_drivers, evaluate_dtlz2)

results = repository / "results"
out_dir = results / "figures" / "presentation"
fragments_dir = out_dir / "fragments"
out_dir.mkdir(parents=True, exist_ok=True)
fragments_dir.mkdir(parents=True, exist_ok=True)

# the three colours, one per order, the same in every figure and in the .tex
# (presentation/presentacion.tex defines the same three hex values once). none of
# the three reads as "good" or "bad": no green, no red. the intersection is
# hatched, never a fourth colour.
colour = {"lu": "#2A6FB0", "ls": "#C98A2B", "cw": "#7A4FA3"}
label = {"lu": r"$X_{lu}$ (Ejemplo 2.2)", "ls": r"$X_{ls}$ (Ejemplo 2.3)", "cw": r"$X_{cw}$ (Ejemplo 2.4)"}
tex_label = {"lu": r"$\phi_{lu}$", "ls": r"$\phi_{ls}$", "cw": r"$\phi_{cw}$"}

plt.rcParams.update({
    "font.size": 13, "axes.titlesize": 13, "legend.fontsize": 12,
    "axes.spines.top": False, "axes.spines.right": False,
    "savefig.dpi": 200, "figure.dpi": 100,
})


# ---------------------------------------------------------------- helpers

def read_rows(path):
    # the tables written by src/reporting.py carry comment lines and two blocks
    # with different headers; this returns the rows of the decision block as
    # dictionaries keyed by that block's header.
    rows, header, in_decision, has_blocks = [], None, False, False
    with open(path, newline="") as handle:
        for raw in csv.reader(handle):
            if not raw or raw[0].startswith("#"):
                continue
            if raw[0] == "block":
                has_blocks, in_decision, header = True, raw[1] == "decision_space", None
                continue
            if header is None:
                header = raw
                continue
            if in_decision or not has_blocks:
                rows.append(dict(zip(header, raw)))
    return rows


def read_simple(path):
    with open(path, newline="") as handle:
        return list(csv.DictReader(row for row in handle if not row.startswith("#")))


def pct(x, nd=1):
    return f"{100.0 * x:.{nd}f}"


def signed_pct(x, nd=1):
    return f"{'+' if x >= 0 else '−'}{abs(100.0 * x):.{nd}f}"


def f3(x):
    return f"{x:.3f}"


def f2(x):
    return f"{x:.2f}"


def tfrac(x):
    fr = Fraction(x).limit_denominator(1000)
    assert abs(float(fr) - x) < 1e-9, (x, fr)
    sign = "-" if fr < 0 else ""
    fr = abs(fr)
    if fr.denominator == 1:
        return f"{sign}{fr.numerator}"
    return rf"{sign}\tfrac{{{fr.numerator}}}{{{fr.denominator}}}"


def mfrac(x):
    # matplotlib's mathtext has \frac and not \tfrac; same fraction, for figures
    return tfrac(x).replace(r"\tfrac", r"\frac")


def jaccard_from_dice(d):
    # src/metrics_decision.py's compute_overlap returns dice; the identity is
    # jaccard = dice / (2 - dice), and it is written here as everywhere it is used.
    return d / (2.0 - d)


def from_doc(path, pattern, cast=str):
    text = (repository / path).read_text(encoding="utf-8")
    match = re.search(pattern, text)
    if match is None:
        raise SystemExit(f"could not read {pattern!r} from {path}")
    return cast(match.group(1))


macros = []          # (name, value, source comment)
pending = []         # anything the script could not trace, for the README


def macro(name, value, source):
    assert re.fullmatch(r"[A-Za-z]+", name), name
    macros.append((name, value, source))


# ---------------------------------------------------------------- slide 6: p1

rho, delta = Fraction(p1_default_params["rho"]), Fraction(p1_default_params["delta"])
macro("pRho", tfrac(float(rho)), "src/problems_tier0.py p1_default_params rho")
macro("pOffset", tfrac(float(delta)), "src/problems_tier0.py p1_default_params, the constant term of the half-width")
macro("pBoxLo", tfrac(float(p1_lower[0])), "src/problems_tier0.py p1_lower")
macro("pBoxHi", tfrac(float(p1_upper[0])), "src/problems_tier0.py p1_upper")

# ---------------------------------------------------------------- slide 7: p1 exact regions

exact_p1 = {(r["quantity"], r["phi_a"], r["phi_b"]): float(r["value"]) for r in read_simple(results / "tier0/exact_regions_p1.csv")}
area_p1 = {phi: exact_p1[("area", phi, "")] for phi in ("lu", "ls", "cw")}
cov_lu_in_cw = exact_p1[("coverage_a_in_b", "lu", "cw")]
cov_cw_in_lu = exact_p1[("coverage_b_in_a", "lu", "cw")]
union_share = exact_p1[("overlap_union_share", "lu", "cw")]
src7 = "results/tier0/exact_regions_p1.csv"
macro("pAreaLu", f3(area_p1["lu"]), f"{src7} area,lu")
macro("pAreaLs", f3(area_p1["ls"]), f"{src7} area,ls")
macro("pAreaCw", f3(area_p1["cw"]), f"{src7} area,cw")
macro("pUnionShare", pct(union_share), f"{src7} overlap_union_share,lu,cw (in %)")
macro("pLuOutsideCw", pct(1.0 - cov_lu_in_cw), f"{src7} 1 - coverage_a_in_b,lu,cw (in %)")
macro("pCwOutsideLu", pct(1.0 - cov_cw_in_lu), f"{src7} 1 - coverage_b_in_a,lu,cw (in %)")
macro("pCovLuCwExact", f3(cov_lu_in_cw), f"{src7} coverage_a_in_b,lu,cw")
macro("pCovCwLuExact", f3(cov_cw_in_lu), f"{src7} coverage_b_in_a,lu,cw")
macro("pJacExact", f3(union_share), f"{src7} overlap_union_share,lu,cw")


def p1_masks(n=2401):
    # the three closed forms of docs/part1/b1_phi_efficient_sets.md section 2.4,
    # evaluated as masks on a fine grid of the decision box. the curve
    # 7 x1 x2 - 4 x1 + 12 x2 - 16 = 0 bounds X_ls and X_lu above; the curve
    # 4 x1 - x1 x2 - 20 x2 + 16 = 0 bounds X_lu below.
    lo, hi = float(p1_lower[0]), float(p1_upper[0])
    axis = np.linspace(lo, hi, n)
    x1, x2 = np.meshgrid(axis, axis)
    upper_arc = 7 * x1 * x2 - 4 * x1 + 12 * x2 - 16 <= 0
    lower_arc = 4 * x1 - x1 * x2 - 20 * x2 + 16 <= 0
    masks = {
        "cw": (x1 >= 0) & (x1 <= 1) & (x2 >= 0) & (x2 <= 1),
        "ls": (x1 >= 0) & (x1 <= 4 / 3) & (x2 >= 0) & (x2 <= 4 / 3) & upper_arc,
        "lu": (x1 >= 0) & upper_arc & lower_arc,
    }
    cell = (axis[1] - axis[0]) ** 2
    return axis, masks, cell


# the two anchors of p1's centres: c_1 is the squared distance to (0, 1) and c_2
# the squared distance to (1, 1), which is what makes the crisp problem readable
# as "get close to two places at once".
p1_anchor_a, p1_anchor_b = (0.0, 1.0), (1.0, 1.0)


def crisp_front_is_the_segment():
    # the efficient set of the problem without uncertainty, checked rather than
    # asserted from the algebra: the non-dominated subset of a fine grid of the
    # box is exactly x_2 = 1 with x_1 in [0, 1], the segment joining the two
    # anchors. squaring is strictly increasing, so minimising the two squared
    # distances and minimising the two distances have the same efficient set.
    n = 601
    axis = np.linspace(float(p1_lower[0]), float(p1_upper[0]), n)
    x1, x2 = np.meshgrid(axis, axis)
    c1 = (x1 - p1_anchor_a[0]) ** 2 + (x2 - p1_anchor_a[1]) ** 2
    c2 = (x1 - p1_anchor_b[0]) ** 2 + (x2 - p1_anchor_b[1]) ** 2
    pts = np.column_stack([x1.ravel(), x2.ravel()])
    values = np.column_stack([c1.ravel(), c2.ravel()])
    order = np.lexsort((values[:, 1], values[:, 0]))
    best, keep = np.inf, np.zeros(len(values), bool)
    for i in order:
        if values[i, 1] < best - 1e-12:
            keep[i] = True
            best = values[i, 1]
    front = pts[keep]
    assert np.allclose(front[:, 1], p1_anchor_a[1]), "the crisp front left x_2 = 1"
    assert abs(front[:, 0].min() - p1_anchor_a[0]) < 1e-9, front[:, 0].min()
    assert abs(front[:, 0].max() - p1_anchor_b[0]) < 1e-9, front[:, 0].max()
    return len(front)


def draw_crisp():
    # the slide before the big picture: two objectives that are both "get closer
    # to this point", and the answer without uncertainty, which is the segment.
    crisp_front_is_the_segment()
    lo, hi = float(p1_lower[0]), float(p1_upper[0])
    fig = plt.figure(figsize=(11.0, 5.4))
    ax = fig.add_axes([0.05, 0.10, 0.50, 0.86])
    ax.add_patch(Rectangle((lo, lo), hi - lo, hi - lo, fill=False, lw=1.0, ec="#9a9a9a"))
    # level curves: how far you are from each anchor
    for radius in (0.25, 0.5, 0.75, 1.0, 1.25):
        ax.add_patch(plt.Circle(p1_anchor_a, radius, fill=False, ec="#3A3A3A", lw=0.6, alpha=0.35, ls=(0, (4, 3))))
        ax.add_patch(plt.Circle(p1_anchor_b, radius, fill=False, ec="#8A5A2B", lw=0.6, alpha=0.35, ls=(0, (1, 2))))
    # a point outside the segment, and the move that improves both at once
    outside = (0.62, 0.45)
    ax.annotate("", xy=(0.62, 0.97), xytext=outside,
                arrowprops=dict(arrowstyle="-|>", color="#B03A2E", lw=2.0))
    ax.plot(*outside, "o", color="#B03A2E", ms=7)
    ax.text(outside[0] - 0.09, outside[1] - 0.06, "desde aquí te acercas\na los dos a la vez",
            fontsize=12.5, color="#B03A2E", va="top", ha="right")
    # the answer
    ax.plot([p1_anchor_a[0], p1_anchor_b[0]], [p1_anchor_a[1], p1_anchor_b[1]],
            "-", color="#111111", lw=4.5, solid_capstyle="round", zorder=4)
    for anchor, colour_, name in ((p1_anchor_a, "#3A3A3A", "objetivo 1"), (p1_anchor_b, "#8A5A2B", "objetivo 2")):
        ax.plot(*anchor, "o", color=colour_, ms=13, zorder=5)
    a_label = f"({p1_anchor_a[0]:g}, {p1_anchor_a[1]:g})"
    b_label = f"({p1_anchor_b[0]:g}, {p1_anchor_b[1]:g})"
    ax.annotate(f"objetivo 1:\nacercarse a {a_label}", p1_anchor_a, textcoords="offset points",
                xytext=(-16, 22), ha="center", fontsize=13, color="#3A3A3A")
    ax.annotate(f"objetivo 2:\nacercarse a {b_label}", p1_anchor_b, textcoords="offset points",
                xytext=(22, 22), ha="center", fontsize=13, color="#8A5A2B")
    ax.set_xlim(lo - 0.08, hi + 0.08)
    ax.set_ylim(lo - 0.08, hi + 0.08)
    ax.set_aspect("equal")
    ax.set_xlabel(r"$x_1$")
    ax.set_ylabel(r"$x_2$", rotation=0, labelpad=12)
    ax.set_xticks([-0.5, 0, 0.5, 1, 1.5])
    ax.set_yticks([-0.5, 0, 0.5, 1, 1.5])
    fig.text(0.575, 0.70, "No se puede estar\nen los dos sitios a la vez.",
             fontsize=18, color="#111111", va="top")
    fig.text(0.575, 0.44, "Sin incertidumbre, la respuesta\nes el segmento que los une.",
             fontsize=18, color="#111111", va="top", fontweight="bold")
    for ext in ("pdf", "png"):
        fig.savefig(out_dir / f"p1_crisp.{ext}")
    plt.close(fig)


def draw_p1():
    axis, masks, cell = p1_masks()
    for phi in ("lu", "ls", "cw"):
        drawn = masks[phi].sum() * cell
        assert abs(drawn - area_p1[phi]) < 3e-3, (phi, drawn, area_p1[phi])
    lo, hi = float(p1_lower[0]), float(p1_upper[0])

    fig = plt.figure(figsize=(11.6, 5.4))
    ax = fig.add_axes([0.04, 0.10, 0.46, 0.87])
    # the decision box
    ax.add_patch(Rectangle((lo, lo), hi - lo, hi - lo, fill=False, lw=1.0, ec="#9a9a9a", ls="-"))
    ax.text(lo + 0.03, lo + 0.04, r"caja de decisión $[-\frac{1}{2}, \frac{3}{2}]^2$", fontsize=10, color="#6a6a6a")

    # X_ls: square [0,4/3]^2 clipped by the upper arc x1 = (16 - 12 x2)/(7 x2 - 4), x2 in [1, 4/3]
    t = np.linspace(1.0, 4 / 3, 300)
    arc_up = (16 - 12 * t) / (7 * t - 4)
    xs = np.concatenate([[0, 4 / 3, 4 / 3], arc_up, [0]])
    ys = np.concatenate([[0, 0, 1], t, [0]])
    ax.fill(xs, ys, fc=colour["ls"], alpha=0.22, ec=colour["ls"], lw=2.2, ls="--", label=label["ls"] + f", área {f3(area_p1['ls'])}")
    # X_cw: the unit square
    ax.fill([0, 1, 1, 0], [0, 0, 1, 1], fc=colour["cw"], alpha=0.22, ec=colour["cw"], lw=2.2, ls=":", label=label["cw"] + f", área {f3(area_p1['cw'])}")
    # X_lu: lens between the lower arc x1 = (20 x2 - 16)/(4 - x2), x2 in [4/5, 1], and the upper arc
    s = np.linspace(4 / 5, 1.0, 300)
    arc_lo = (20 * s - 16) / (4 - s)
    xs = np.concatenate([arc_lo, arc_up, [0]])
    ys = np.concatenate([s, t, [4 / 5]])
    ax.fill(xs, ys, fc=colour["lu"], alpha=0.30, ec=colour["lu"], lw=2.2, ls="-", label=label["lu"] + f", área {f3(area_p1['lu'])}")
    # X_lu ∩ X_cw, hatched: the lens below x2 = 1 and left of x1 = 1; the lower arc meets x1 = 1 at x2 = 20/21
    s_cut = np.linspace(4 / 5, 20 / 21, 200)
    xs = np.concatenate([(20 * s_cut - 16) / (4 - s_cut), [1, 0, 0]])
    ys = np.concatenate([s_cut, [1, 1, 4 / 5]])
    ax.fill(xs, ys, fc="none", ec="#333333", hatch="////", lw=0.0,
            label=r"$X_{lu} \cap X_{cw}$, " + f"{pct(union_share)} % de la unión")

    # el segmento del problema sin incertidumbre, de la diapositiva anterior
    ax.plot([p1_anchor_a[0], p1_anchor_b[0]], [p1_anchor_a[1], p1_anchor_b[1]],
            "-", color="#111111", lw=3.0, solid_capstyle="round", zorder=4,
            label="sin incertidumbre: el segmento")
    for (px, py, txt, dx, dy) in [(0, 4 / 5, r"$(0, \frac{4}{5})$", 0.04, -0.09),
                                  (4 / 3, 1, r"$(\frac{4}{3}, 1)$", 0.03, 0.04),
                                  (0, 4 / 3, r"$(0, \frac{4}{3})$", 0.04, 0.03)]:
        ax.plot(px, py, "o", color="#222222", ms=6, zorder=5)
        ax.text(px + dx, py + dy, txt, fontsize=11)

    ax.set_xlim(lo - 0.08, hi + 0.08)
    ax.set_ylim(lo - 0.08, hi + 0.08)
    ax.set_aspect("equal")
    ax.set_xlabel(r"$x_1$")
    ax.set_ylabel(r"$x_2$", rotation=0, labelpad=12)
    ax.set_xticks([-0.5, 0, 0.5, 1, 1.5])
    ax.set_yticks([-0.5, 0, 0.5, 1, 1.5])
    handles, labels = ax.get_legend_handles_labels()
    order = [2, 1, 0, 4, 3]
    fig.legend([handles[i] for i in order], [labels[i] for i in order], loc="center left",
               bbox_to_anchor=(0.51, 0.76), frameon=False, fontsize=14.5, handlelength=2.4)
    fig.text(0.53, 0.34, f"El {pct(1 - cov_lu_in_cw)}\u2009% de $X_{{lu}}$ queda fuera de $X_{{cw}}$.\n"
                          f"El {pct(1 - cov_cw_in_lu)}\u2009% de $X_{{cw}}$ queda fuera de $X_{{lu}}$.\n\n"
                          "Cada uno tiene una zona\na la que el otro no llega.",
             fontsize=15, color="#333333", va="top")
    for ext in ("pdf", "png"):
        fig.savefig(out_dir / f"p1_regiones.{ext}")
    plt.close(fig)


# ---------------------------------------------------------------- slide 10: instrument error on p1

instrument_rows = read_simple(results / "tier0/instrument_error_p1.csv")
measured_p1 = read_rows(results / "tier0/table_2_measured.csv")


def p1_measured(metric, n_evals, source):
    rows = [r for r in source if r["problem"] == "p1" and r["phi_a"] == "lu" and r["phi_b"] == "cw"
            and r["metric"] == metric and int(r["n_evals"]) == n_evals and float(r["delta"]) == 0.0]
    assert len(rows) == 1, (metric, n_evals, len(rows))
    return rows[0]


src10 = "results/tier0/instrument_error_p1.csv (lu,cw; delta 0.0; n_evals 5000)"
src10b = "results/tier0/table_2_measured.csv decision block (lu,cw; delta 0.0; n_evals 20000)"
instrument_table = []
instrument_bars = []   # (nombre, exacto, medido, clave) para la figura de la 10
for metric, name, exact in (("coverage_a_in_b", r"cobertura$(lu \to cw)$", cov_lu_in_cw),
                            ("coverage_b_in_a", r"cobertura$(cw \to lu)$", cov_cw_in_lu),
                            ("overlap", "Jaccard", union_share)):
    r5 = p1_measured(metric, 5000, instrument_rows)
    r20 = p1_measured(metric, 20000, measured_p1)
    assert abs(float(r5["exact"]) - (exact if metric != "overlap" else exact_p1[("overlap_d2_convention", "lu", "cw")])) < 1e-12
    m5, m20 = float(r5["measured_median"]), float(r20["median"])
    if metric == "overlap":
        m5, m20 = jaccard_from_dice(m5), jaccard_from_dice(m20)
        err5, err20 = rf"$\times${m5 / exact:.2f}", rf"$\times${m20 / exact:.2f}"
        key = "Jac"
    else:
        err5, err20 = signed_pct(m5 / exact - 1) + r"\,\%", signed_pct(m20 / exact - 1) + r"\,\%"
        key = "CovLuCw" if metric == "coverage_a_in_b" else "CovCwLu"
    instrument_table.append((name, f3(exact), f3(m5), err5))
    instrument_bars.append((name, exact, m5, key))
    macro(f"p{key}Meas", f3(m5), f"{src10} measured_median, metric {metric}" + (" via jaccard = dice/(2-dice)" if metric == "overlap" else ""))
    macro(f"p{key}Err", err5, f"{src10} measured/exact, metric {metric}")
    macro(f"p{key}ErrLarge", err20, f"{src10b} median/exact, metric {metric}")
    if metric == "overlap":
        macro("pJacFactorPlain", f"{m5 / exact:.2f}", f"{src10} jaccard measured/exact")
        macro("pJacFactorLargePlain", f"{m20 / exact:.2f}", f"{src10b} jaccard measured/exact")

with open(fragments_dir / "tabla_instrumento.tex", "w", encoding="utf-8") as handle:
    handle.write("% generated by experiments/make_presentation.py\n")
    handle.write(f"% source: {src10}; exact values from {src7}; jaccard = dice/(2-dice)\n")
    handle.write(r"\begin{tabular}{lrrr}" + "\n" + r"\toprule" + "\n")
    handle.write(r"par $\phi_{lu}$ frente a $\phi_{cw}$, p1 & exacto & medido & error \\" + "\n" + r"\midrule" + "\n")
    for name, ex, me, er in instrument_table:
        bold = r"\textbf{%s}" % er if er.startswith("$") else er
        handle.write(f"{name} & {ex} & {me} & {bold} \\\\\n")
    handle.write(r"\bottomrule" + "\n" + r"\end{tabular}" + "\n")

def draw_instrument():
    # slide 10 as a picture instead of a table: exact against measured, three
    # rows, with the jaccard factor called out. neutral greys, since neither bar
    # is an order and nothing here is good or bad.
    fig, ax = plt.subplots(figsize=(10.4, 4.1))
    # las filas, dichas en palabras: qué compara cada una de las tres
    spelled = {"CovLuCw": "de $X_{lu}$, cuánto está\ndentro de $X_{cw}$",
               "CovCwLu": "de $X_{cw}$, cuánto está\ndentro de $X_{lu}$",
               "Jac": "Jaccard: de todo lo que ocupan\nentre los dos, cuánto comparten"}
    names = [spelled[key] for *_, key in instrument_bars]
    y = np.arange(len(instrument_bars))[::-1]
    exact_v = [e for _, e, _, _ in instrument_bars]
    meas_v = [m for _, _, m, _ in instrument_bars]
    ax.barh(y + 0.19, exact_v, height=0.34, color="#3A3A3A", label="la verdad, analíticamente")
    ax.barh(y - 0.19, meas_v, height=0.34, color="#FFFFFF", edgecolor="#3A3A3A", hatch="////",
            label="medido con 5000 puntos al azar")
    for yy, e, m in zip(y, exact_v, meas_v):
        ax.text(e + 0.008, yy + 0.19, f3(e), va="center", fontsize=13)
        ax.text(m + 0.008, yy - 0.19, f3(m), va="center", fontsize=13)
    ax.set_yticks(y)
    ax.set_yticklabels(names, fontsize=12.5)
    ax.set_xlim(0, max(meas_v) * 1.28)
    ax.set_xticks([])
    ax.spines["left"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.tick_params(left=False)
    factor = meas_v[-1] / exact_v[-1]
    ax.text(max(meas_v) * 1.02, y[-1] - 0.05, f"$\\times${factor:.2f}", color="#B03A2E", fontsize=26,
            fontweight="bold", va="center")
    ax.legend(frameon=False, loc="lower right", bbox_to_anchor=(1.0, -0.20), ncol=2, fontsize=13)
    ax.set_title(r"$X_{lu}$ (Ejemplo 2.2) frente a $X_{cw}$ (Ejemplo 2.4), sobre p1",
                 fontsize=14, color="#333333", pad=14)
    fig.tight_layout()
    for ext in ("pdf", "png"):
        fig.savefig(out_dir / f"instrumento.{ext}")
    plt.close(fig)


# ---------------------------------------------------------------- slides 11-12: benchmarks

bench = {}   # (problem, eps) -> dict(cov_cw_in_lu, card_lu, card_cw, iqr)
for eps in ("0.05", "0.1", "0.25", "0.5"):
    rows = read_rows(results / f"tier1/table_2_measured_eps_{eps}.csv")
    for problem in ("zdt1_interval", "dtlz2_interval"):
        hit = [r for r in rows if r["problem"] == problem and r["phi_a"] == "lu" and r["phi_b"] == "cw"
               and r["status"] == "finding" and r["metric"] == "coverage_b_in_a"
               and int(r["n_evals"]) == 5000 and float(r["delta"]) == 0.0]
        assert len(hit) == 1, (eps, problem, len(hit))
        r = hit[0]
        bench[(problem, float(eps))] = dict(cov=float(r["median"]), card_lu=int(r["cardinality_a"]),
                                            card_cw=int(r["cardinality_b"]), iqr=float(r["iqr"]))
# the sanity row: at eps = 0 everything is 1
rows0 = read_rows(results / "tier1/table_2_measured_eps_0.0.csv")
for r in rows0:
    if r["phi_a"] == "lu" and r["phi_b"] == "cw" and r["metric"].startswith("coverage") and int(r["n_evals"]) == 5000 and float(r["delta"]) == 0.0:
        assert float(r["median"]) == 1.0 and float(r["iqr"]) == 0.0, r

outside = {k: 1.0 - v["cov"] for k, v in bench.items()}
b_min, b_max = min(outside.values()), max(outside.values())
assert 0.628 <= b_min and b_max <= 0.912, (b_min, b_max)
src11 = "results/tier1/table_2_measured_eps_{0.05,0.1,0.25,0.5}.csv decision block, lu,cw, finding, coverage_b_in_a, n_evals 5000, delta 0.0"
macro("bMinPct", pct(b_min), f"{src11}: min over the eight cells of 1 - median (in %)")
macro("bMaxPct", pct(b_max), f"{src11}: max over the eight cells of 1 - median (in %)")
macro("bMinInt", str(int(round(100 * b_min))), f"{src11}: min, rounded to the integer")
macro("bMaxInt", str(int(round(100 * b_max))), f"{src11}: max, rounded to the integer")
macro("bZdtVars", str(zdt1_n_vars), "src/problems_tier1.py zdt1_n_vars")
macro("bDtlzVars", str(dtlz2_n_vars), "src/problems_tier1.py dtlz2_n_vars")
problem_name = {"zdt1_interval": f"ZDT1 ({zdt1_n_vars} variables)", "dtlz2_interval": f"DTLZ2 ({dtlz2_n_vars} variables)"}
eps_levels = (0.05, 0.1, 0.25, 0.5)

with open(fragments_dir / "tabla_benchmarks.tex", "w", encoding="utf-8") as handle:
    handle.write("% generated by experiments/make_presentation.py\n")
    handle.write(f"% source: {src11}; columns median, cardinality_a (|X_lu|), cardinality_b (|X_cw|)\n")
    handle.write(r"\begin{tabular}{lrrr}" + "\n" + r"\toprule" + "\n")
    handle.write(r"$\varepsilon$ & $1 - \mathrm{cob}(cw \to lu)$ & $|X_{lu}|$ & $|X_{cw}|$ \\" + "\n" + r"\midrule" + "\n")
    for problem in ("zdt1_interval", "dtlz2_interval"):
        handle.write(r"\multicolumn{4}{l}{\textbf{" + problem_name[problem] + r"}} \\" + "\n")
        for eps in eps_levels:
            b = bench[(problem, eps)]
            handle.write(f"{eps:.2f} & {pct(1 - b['cov'])}\\,\\% & {b['card_lu']} & {b['card_cw']} \\\\\n")
        if problem == "zdt1_interval":
            handle.write(r"\addlinespace" + "\n")
    handle.write(r"\bottomrule" + "\n" + r"\end{tabular}" + "\n")

for problem, key in (("zdt1_interval", "Zdt"), ("dtlz2_interval", "Dtlz")):
    cws = {bench[(problem, e)]["card_cw"] for e in eps_levels}
    assert len(cws) == 1, (problem, cws)
    macro(f"c{key}CardCw", str(cws.pop()), f"{src11}: cardinality_b, constant over the four eps")
    macro(f"c{key}CardLu", r"\,\to\,".join(str(bench[(problem, e)]["card_lu"]) for e in eps_levels), f"{src11}: cardinality_a over eps 0.05, 0.1, 0.25, 0.5")


def draw_benchmarks():
    # slide 11 as a picture instead of a table: the fraction of one order's
    # efficient set that lies outside the other's, at every imprecision level,
    # with the sanity point at eps = 0 drawn hollow because it is not a level.
    fig, ax = plt.subplots(figsize=(10.0, 4.4))
    ax.axhspan(100 * b_min, 100 * b_max, color="#3A3A3A", alpha=0.08, zorder=0)
    marks = {"zdt1_interval": "o", "dtlz2_interval": "s"}
    shades = {"zdt1_interval": "#3A3A3A", "dtlz2_interval": "#7A7A7A"}
    offsets = {"zdt1_interval": 12, "dtlz2_interval": -20}
    for problem in ("zdt1_interval", "dtlz2_interval"):
        xs = np.arange(1, len(eps_levels) + 1)
        ys = [100 * outside[(problem, e)] for e in eps_levels]
        ax.plot(xs, ys, marks[problem] + "-", color=shades[problem], lw=2.2, ms=10,
                label=problem_name[problem])
        ax.plot([0], [0], marks[problem], color=shades[problem], ms=10, mfc="white")
        for x, v in zip(xs, ys):
            ax.annotate(f"{v:.1f}", (x, v), textcoords="offset points", xytext=(0, offsets[problem]),
                        ha="center", fontsize=12.5, color=shades[problem])
    ax.text(len(eps_levels) + 0.18, 100 * (b_min + b_max) / 2, f"{pct(b_min)}\u2013{pct(b_max)}\u2009%",
            fontsize=20, color="#3A3A3A", va="center", ha="left")
    ax.annotate("sin incertidumbre:\nlos tres órdenes\ncoinciden", (0, 0),
                textcoords="offset points", xytext=(12, 18), fontsize=12, color="#6A6A6A",
                arrowprops=dict(arrowstyle="-", color="#9A9A9A", lw=1.0))
    ax.set_xticks(range(len(eps_levels) + 1))
    ax.set_xticklabels(["0"] + [f"{e:.2f}" for e in eps_levels])
    ax.set_xlabel(r"nivel de imprecisión $\varepsilon$", fontsize=14)
    ax.set_ylabel("% de una respuesta que\ndesaparece con el otro orden", fontsize=14)
    ax.set_ylim(-8, 104)
    ax.set_xlim(-0.35, len(eps_levels) + 1.15)
    ax.legend(frameon=False, loc="lower right", bbox_to_anchor=(0.86, 0.02), fontsize=13)
    fig.tight_layout()
    for ext in ("pdf", "png"):
        fig.savefig(out_dir / f"benchmarks.{ext}")
    plt.close(fig)


def draw_cardinalities():
    fig, axes = plt.subplots(1, 2, figsize=(9.4, 4.8))
    positions = np.arange(len(eps_levels))
    for ax, problem in zip(axes, ("zdt1_interval", "dtlz2_interval")):
        lu = [bench[(problem, e)]["card_lu"] for e in eps_levels]
        cw = [bench[(problem, e)]["card_cw"] for e in eps_levels]
        ax.plot(positions, cw, "-o", color=colour["cw"], lw=2.4, ms=8, label=r"$|X_{cw}|$")
        ax.plot(positions, lu, "-o", color=colour["lu"], lw=2.4, ms=8, label=r"$|X_{lu}|$")
        top = max(cw) * 1.22
        for p, v in zip(positions, cw):
            ax.annotate(str(v), (p, v), textcoords="offset points", xytext=(0, 9), ha="center", color=colour["cw"], fontsize=11)
        for p, v in zip(positions, lu):
            ax.annotate(str(v), (p, v), textcoords="offset points", xytext=(0, -17), ha="center", color=colour["lu"], fontsize=11)
        ax.set_xticks(positions)
        ax.set_xticklabels([f"{e:.2f}" for e in eps_levels])
        ax.set_xlabel(r"nivel de imprecisión $\varepsilon$")
        ax.set_ylim(0, top)
        ax.set_title(problem_name[problem])
        ax.legend(frameon=False, loc="center left", bbox_to_anchor=(0.02, 0.55))
    axes[0].set_ylabel("tamaño del conjunto eficiente\n(de una muestra de 5000 puntos)")
    fig.tight_layout()
    for ext in ("pdf", "png"):
        fig.savefig(out_dir / f"tamanos_eps.{ext}")
    plt.close(fig)


# ---------------------------------------------------------------- the two benchmarks, stated

# the two published problems, written from src/problems_tier1.py so that the
# slide states what the code evaluates. the constants are read from the module
# and not typed: the number of variables, which variable drives each half-width,
# and the two half-width forms.
zdt1_drivers = ", ".join(f"x_{{{d + 1}}}" for d in zdt1_width_drivers)
dtlz2_drivers = ", ".join(f"x_{{{d + 1}}}" for d in dtlz2_width_drivers)
macro("ZdtName", "ZDT1", "src/problems_tier1.py zdt1_interval")
macro("ZdtSize", f"{zdt1_n_vars} variables, {zdt1_n_obj} objetivos", "src/problems_tier1.py zdt1_n_vars, zdt1_n_obj")
macro("ZdtF", r"f_1 = x_1, \qquad f_2 = g\,\Bigl(1 - \sqrt{f_1/g}\,\Bigr)",
      "src/problems_tier1.py evaluate_zdt1, [2] equations (6) and (7)")
macro("ZdtG", rf"g = 1 + \dfrac{{9}}{{{zdt1_n_vars - 1}}}\sum_{{i \geq 2}} x_i",
      "src/problems_tier1.py evaluate_zdt1, g with m - 1 = zdt1_n_vars - 1")
macro("ZdtR", r"r_i = \varepsilon\,\bigl( (\marca{x_d} - \tfrac{1}{2})^2 + \tfrac{1}{20} \bigr)",
      "src/problems_tier1.py zdt1_half_width")
macro("ZdtDrivers", zdt1_drivers, "src/problems_tier1.py zdt1_width_drivers, as 1-based names")
macro("DtlzName", "DTLZ2", "src/problems_tier1.py dtlz2_interval")
macro("DtlzSize", f"{dtlz2_n_vars} variables, {dtlz2_n_obj} objetivos", "src/problems_tier1.py dtlz2_n_vars, dtlz2_n_obj")
macro("DtlzFone", r"f_1 = (1+g)\cos\tfrac{\pi x_1}{2}\cos\tfrac{\pi x_2}{2}",
      "src/problems_tier1.py evaluate_dtlz2, [3] equation (9) at M = 3")
macro("DtlzFtwo", r"f_2 = (1+g)\cos\tfrac{\pi x_1}{2}\sin\tfrac{\pi x_2}{2}",
      "src/problems_tier1.py evaluate_dtlz2, [3] equation (9) at M = 3")
macro("DtlzFthree", r"f_3 = (1+g)\sin\tfrac{\pi x_1}{2}",
      "src/problems_tier1.py evaluate_dtlz2, [3] equation (9) at M = 3")
macro("DtlzG", rf"g = \sum_{{i \geq {dtlz2_n_obj}}} (x_i - \tfrac{{1}}{{2}})^2",
      "src/problems_tier1.py evaluate_dtlz2, g over the tail")
macro("DtlzR", r"r_i = \varepsilon\,\marca{x_d}", "src/problems_tier1.py dtlz2_half_width")
macro("DtlzDrivers", dtlz2_drivers, "src/problems_tier1.py dtlz2_width_drivers, as 1-based names")


def draw_benchmark_fronts():
    # the answer of each benchmark without uncertainty, drawn from the code: the
    # points are evaluated with the module's own evaluate_* at eps = 0 on the
    # decision vectors the two papers give for their efficient sets, and the
    # script checks that a large uniform sample of the box dominates none of them.
    from mpl_toolkits.mplot3d import Axes3D  # noqa: F401

    rng = np.random.default_rng(20260924)

    t = np.linspace(0.0, 1.0, 300)
    zdt = np.zeros((len(t), zdt1_n_vars))
    zdt[:, 0] = t
    (zc1, _), (zc2, _) = evaluate_zdt1(zdt)
    sample = rng.random((20000, zdt1_n_vars))
    (sc1, _), (sc2, _) = evaluate_zdt1(sample)
    dominated = ((sc1[:, None] <= zc1[None, :]) & (sc2[:, None] <= zc2[None, :]) &
                 ((sc1[:, None] < zc1[None, :]) | (sc2[:, None] < zc2[None, :]))).any()
    assert not dominated, "a uniform sample dominated a point of zdt1's stated front"

    grid = np.linspace(0.0, 1.0, 40)
    a1, a2 = np.meshgrid(grid, grid)
    dtlz = np.full((a1.size, dtlz2_n_vars), 0.5)
    dtlz[:, 0], dtlz[:, 1] = a1.ravel(), a2.ravel()
    (d1, _), (d2, _), (d3, _) = evaluate_dtlz2(dtlz)
    radius = np.sqrt(d1 ** 2 + d2 ** 2 + d3 ** 2)
    assert np.allclose(radius, 1.0), "dtlz2's stated front left the unit sphere"

    fig = plt.figure(figsize=(3.6, 3.2))
    left = fig.add_subplot(1, 1, 1)
    left.plot(zc1, zc2, "-", color="#111111", lw=3.5)
    left.set_xlabel("$f_1$", fontsize=13)
    left.set_ylabel("$f_2$", rotation=0, labelpad=10, fontsize=13)
    left.set_xlim(-0.05, 1.08)
    left.set_ylim(-0.05, 1.08)
    left.set_xticks([0, 1])
    left.set_yticks([0, 1])
    fig.tight_layout()
    for ext in ("pdf", "png"):
        fig.savefig(out_dir / f"zdt1_frente.{ext}")
    plt.close(fig)

    fig = plt.figure(figsize=(3.6, 3.2))
    right = fig.add_subplot(1, 1, 1, projection="3d")
    right.plot_surface(d1.reshape(a1.shape), d2.reshape(a1.shape), d3.reshape(a1.shape),
                       color="#555555", alpha=0.55, linewidth=0, antialiased=True, shade=True)
    right.set_xlabel("$f_1$", labelpad=-12, fontsize=13)
    right.set_ylabel("$f_2$", labelpad=-12, fontsize=13)
    right.set_zlabel("$f_3$", labelpad=-12, fontsize=13)
    for axis in (right.xaxis, right.yaxis, right.zaxis):
        axis.set_ticks([])
        axis.pane.set_visible(False)
    right.grid(False)
    right.set_xlim(0, 1); right.set_ylim(0, 1); right.set_zlim(0, 1)
    right.set_box_aspect((1, 1, 1))
    right.view_init(elev=24, azim=38)
    fig.tight_layout()
    for ext in ("pdf", "png"):
        fig.savefig(out_dir / f"dtlz2_frente.{ext}")
    plt.close(fig)


# ---------------------------------------------------------------- slide 13: I-BK1, the problem and its non-degeneracy

# the coefficients as src/problems_native.py holds them, which are the paper's
# printed decimals; exact rationals for the two ratios of the degeneracy test.
ibk1_exact = [[(Fraction(str(a)), Fraction(str(b))) for (a, b) in objective] for objective in ibk1_coefficients]


def interval_tex(a, b):
    def dec(v):
        return f"{float(v):g}"
    # \coef is defined in presentation/presentacion.tex: it is what highlights the
    # brackets on the coefficients, the point of slide 13
    return f"\\coef{{[{dec(a)}, {dec(b)}]}}"


shift = int(ibk1_shift)
macro("IBKone", f"G_1 = {interval_tex(*ibk1_exact[0][0])}\\, x_1^2 + {interval_tex(*ibk1_exact[0][1])}\\, x_2^2",
      "src/problems_native.py ibk1_coefficients[0]")
macro("IBKtwo", f"G_2 = {interval_tex(*ibk1_exact[1][0])}\\, (x_1 - {shift})^2 + {interval_tex(*ibk1_exact[1][1])}\\, (x_2 - {shift})^2",
      "src/problems_native.py ibk1_coefficients[1], ibk1_shift")
macro("IBKbox", f"[{int(ibk1_lower[0])}, {int(ibk1_upper[0])}]^2", "src/problems_native.py ibk1_lower, ibk1_upper")
# degeneracy test of docs/part2/f5_boundary_interchange.md section 3.2: the ratio
# (b - a)/(a + b) per term; an objective is order-blind iff it is the same in every term
ratios = [[(b - a) / (a + b) for (a, b) in objective] for objective in ibk1_exact]
for i, objective in enumerate(ratios):
    assert objective[0] != objective[1], ("I-BK1 objective would be degenerate", i)
macro("IBKratiosOne", " frente a ".join(tfrac(float(v)) for v in ratios[0]), "computed from ibk1_coefficients[0]: (b-a)/(a+b) per term")
macro("IBKratiosTwo", " frente a ".join(tfrac(float(v)) for v in ratios[1]), "computed from ibk1_coefficients[1]: (b-a)/(a+b) per term")

# ---------------------------------------------------------------- slide 14: I-BK1 exact regions, the wedges

exact_ibk1 = {(r["quantity"], r["phi_a"], r["phi_b"]): float(r["value"]) for r in read_simple(results / "part2/exact_regions_ibk1.csv")}
src14 = "results/part2/exact_regions_ibk1.csv"
band = {phi: (exact_ibk1[("band_lower", phi, "")], exact_ibk1[("band_upper", phi, "")]) for phi in ("lu", "ls", "cw")}
area_ibk1 = {phi: exact_ibk1[("area", phi, "")] for phi in ("lu", "ls", "cw")}
for phi in ("lu", "ls", "cw"):
    macro(f"iArea{phi.capitalize()}", f3(area_ibk1[phi]), f"{src14} area,{phi}")
    macro(f"iBand{phi.capitalize()}Lo", tfrac(band[phi][0]), f"{src14} band_lower,{phi}")
    macro(f"iBand{phi.capitalize()}Hi", tfrac(band[phi][1]), f"{src14} band_upper,{phi}")
# strict nesting, asserted rather than assumed
assert band["ls"][0] < band["lu"][0] < band["cw"][0] < band["cw"][1] < band["lu"][1] < band["ls"][1]
ends = sorted([(band[p][0], p) for p in band] + [(band[p][1], p) for p in band])
macro("iOrderedEnds", " < ".join(tfrac(v) for v, _ in ends), f"{src14} the six band ends, sorted")
cov_ls_in_cw = exact_ibk1[("coverage_a_in_b", "ls", "cw")]
macro("iLsOutsideCw", pct(1.0 - cov_ls_in_cw), f"{src14} 1 - coverage_a_in_b,ls,cw (in %)")
macro("iCovLsCw", f3(cov_ls_in_cw), f"{src14} coverage_a_in_b,ls,cw")
nu_curve = from_doc("docs/part2/f2_ibk1_derivation.md", r"ν = V/U = a c / b² = .*?= (\d+/\d+) =")
macro("iNuCurve", tfrac(float(Fraction(nu_curve))), "docs/part2/f2_ibk1_derivation.md section 4.1, nu of equation (25)'s curve")
crit_ratio = from_doc("docs/part2/f2_ibk1_derivation.md", r"the critical set is ([\d.]+) times X_lu", float)
macro("iCritRatio", f2(crit_ratio), "docs/part2/f2_ibk1_derivation.md section 4.3, critical set measure over X_lu's")


# I-BK1 without uncertainty: the problem of the two centres. its efficient set is
# a single curve of constant nu, and the value is recomputed here from the printed
# coefficients and checked against the one the derivation states.
ibk1_centres = [[(a + b) / 2 for (a, b) in objective] for objective in ibk1_exact]
ibk1_nu_crisp = (ibk1_centres[0][0] * ibk1_centres[1][1]) / (ibk1_centres[0][1] * ibk1_centres[1][0])
_stated = Fraction(from_doc("docs/part2/f2_ibk1_derivation.md",
                            r"the centres \(c_1, c_2\)\s+(\d+/\d+)"))
assert ibk1_nu_crisp == _stated, (ibk1_nu_crisp, _stated)
assert band["ls"][0] < ibk1_nu_crisp < band["ls"][1], "the crisp curve left the widest wedge"
macro("iNuCrisp", tfrac(float(ibk1_nu_crisp)),
      "computed from src/problems_native.py's coefficients and checked against "
      "docs/part2/f2_ibk1_derivation.md section 3.3")


def nu_curve_points(k, n=600):
    # nu = x2 (5 - x1) / (x1 (5 - x2)) = k  <=>  x2 = 5 k x1 / (5 + (k - 1) x1)
    x1 = np.linspace(0, shift, n)
    return x1, shift * k * x1 / (shift + (k - 1) * x1)


def draw_ibk1_crisp():
    # the slide that states the published problem: where each objective pulls, the
    # fact that a level of an interval objective is a band and not a curve, and the
    # answer without uncertainty, which is one curve.
    fig = plt.figure(figsize=(5.6, 5.0))
    ax = fig.add_axes([0.11, 0.11, 0.86, 0.86])
    grid = np.linspace(0, shift, 700)
    gx, gy = np.meshgrid(grid, grid)
    anchors = ((0.0, 0.0), (float(shift), float(shift)))
    shades = ("#3A3A3A", "#8A5A2B")
    for objective, (anchor, shade) in enumerate(zip(anchors, shades)):
        (lo_1, hi_1), (lo_2, hi_2) = [(float(a), float(b)) for (a, b) in ibk1_exact[objective]]
        u, v = (gx - anchor[0]) ** 2, (gy - anchor[1]) ** 2
        low, high = lo_1 * u + lo_2 * v, hi_1 * u + hi_2 * v
        level = 2.0
        # where this objective's interval could take exactly this value: a band,
        # because the objective is not a number but an interval
        band_here = (low <= level) & (level <= high)
        ax.contourf(gx, gy, band_here.astype(float), levels=[0.5, 1.5],
                    colors=[shade], alpha=0.22)
        ax.contour(gx, gy, high - level, levels=[0.0], colors=[shade], linewidths=1.0, alpha=0.7)
        ax.contour(gx, gy, low - level, levels=[0.0], colors=[shade], linewidths=1.0, alpha=0.7)
    cx, cy = nu_curve_points(float(ibk1_nu_crisp))
    ax.plot(cx, cy, "-", color="#111111", lw=4.0, solid_capstyle="round", zorder=5)
    for anchor, shade in zip(anchors, shades):
        ax.plot(*anchor, "o", color=shade, ms=13, zorder=6)
    # a los lados de la diagonal, para no pisar la curva ni los puntos
    ax.annotate("$G_1$ tira aquí", anchors[0], textcoords="offset points",
                xytext=(30, -4), ha="left", va="center", fontsize=12, color=shades[0])
    ax.annotate("$G_2$ tira aquí", anchors[1], textcoords="offset points",
                xytext=(-30, 4), ha="right", va="center", fontsize=12, color=shades[1])
    ax.set_xlim(-0.25, shift + 0.25)
    ax.set_ylim(-0.25, shift + 0.25)
    ax.set_aspect("equal")
    ax.set_xlabel(r"$x_1$")
    ax.set_ylabel(r"$x_2$", rotation=0, labelpad=12)
    for ext in ("pdf", "png"):
        fig.savefig(out_dir / f"ibk1_crisp.{ext}")
    plt.close(fig)


def draw_ibk1():
    n = 2001
    axis = np.linspace(0, shift, n)
    x1, x2 = np.meshgrid(axis, axis)
    with np.errstate(divide="ignore", invalid="ignore"):
        nu = x2 * (shift - x1) / (x1 * (shift - x2))
    cell = (axis[1] - axis[0]) ** 2
    for phi in ("lu", "ls", "cw"):
        mask = (nu >= band[phi][0]) & (nu <= band[phi][1])
        drawn = np.nansum(mask) * cell
        assert abs(drawn - area_ibk1[phi]) < 1.5e-2, (phi, drawn, area_ibk1[phi])

    fig = plt.figure(figsize=(11.6, 5.2))
    ax = fig.add_axes([0.05, 0.12, 0.42, 0.84])
    styles = {"ls": "--", "lu": "-", "cw": ":"}
    for phi, alpha in (("ls", 0.20), ("lu", 0.26), ("cw", 0.34)):
        lo_x, lo_y = nu_curve_points(band[phi][0])
        hi_x, hi_y = nu_curve_points(band[phi][1])
        xs = np.concatenate([lo_x, hi_x[::-1]])
        ys = np.concatenate([lo_y, hi_y[::-1]])
        ax.fill(xs, ys, fc=colour[phi], alpha=alpha, ec=colour[phi], lw=2.2, ls=styles[phi],
                label=label[phi] + rf": $\nu \in [{mfrac(band[phi][0])}, {mfrac(band[phi][1])}]$, área {f3(area_ibk1[phi])}")
    cx, cy = nu_curve_points(float(Fraction(nu_curve)))
    ax.plot(cx, cy, color="#777777", lw=0.9, ls=(0, (1, 2)),
            label=rf"la curva que [16] publica, $\nu = {mfrac(float(Fraction(nu_curve)))}$")
    kx, ky = nu_curve_points(float(ibk1_nu_crisp))
    ax.plot(kx, ky, color="#111111", lw=2.6, solid_capstyle="round", zorder=5,
            label=rf"sin incertidumbre: una curva, $\nu = {mfrac(float(ibk1_nu_crisp))}$")
    ax.plot([0, shift], [0, shift], "o", color="#222222", ms=6, zorder=5)
    ax.text(0.15, 0.10, "(0, 0)", fontsize=10, va="bottom")
    ax.text(shift - 0.15, shift + 0.06, f"({shift}, {shift})", fontsize=10, ha="right")
    ax.set_xlim(-0.15, shift + 0.15)
    ax.set_ylim(-0.15, shift + 0.15)
    ax.set_aspect("equal")
    ax.set_xlabel(r"$x_1$")
    ax.set_ylabel(r"$x_2$", rotation=0, labelpad=12)
    ax.set_title(rf"$\nu = x_2(5-x_1)\,/\,x_1(5-x_2)$ en la región $[0, {shift}]^2$", fontsize=12)

    # the whole box, small, with the region marked
    inset = fig.add_axes([0.53, 0.62, 0.14, 0.30])
    lo, hi = float(ibk1_lower[0]), float(ibk1_upper[0])
    inset.add_patch(Rectangle((lo, lo), hi - lo, hi - lo, fill=False, lw=1.0, ec="#9a9a9a"))
    inset.add_patch(Rectangle((0, 0), shift, shift, fc="#dddddd", ec="#555555", lw=1.0))
    inset.set_xlim(lo - 1, hi + 1)
    inset.set_ylim(lo - 1, hi + 1)
    inset.set_aspect("equal")
    inset.set_xticks([lo, 0, hi])
    inset.set_yticks([lo, 0, hi])
    inset.tick_params(labelsize=8)
    inset.set_title(rf"caja de decisión $[{int(lo)}, {int(hi)}]^2$", fontsize=11)

    # the number line of the six band ends
    line = fig.add_axes([0.52, 0.32, 0.46, 0.18])
    line.set_xlim(0.35, 2.15)
    line.set_ylim(-1.4, 1.6)
    line.axhline(0, color="#444444", lw=1.2)
    for phi, height in (("ls", 1.05), ("lu", 0.70), ("cw", 0.35)):
        a, b = band[phi]
        line.plot([a, b], [height, height], color=colour[phi], lw=3.0, solid_capstyle="butt")
        line.text(b + 0.03, height, tex_label[phi], color=colour[phi], va="center", fontsize=13)
    for v, phi in ends:
        line.plot([v, v], [-0.12, 0.12], color=colour[phi], lw=2.0)
        line.text(v, -0.35, f"${mfrac(v)}$", ha="center", va="top", fontsize=13, color=colour[phi])
    line.axis("off")
    line.set_title(r"los seis extremos de $\nu$, ordenados", fontsize=12)

    handles, labels = ax.get_legend_handles_labels()
    fig.legend(handles, labels, loc="lower left", bbox_to_anchor=(0.50, 0.01), frameon=False, fontsize=12.5, handlelength=2.4)
    for ext in ("pdf", "png"):
        fig.savefig(out_dir / f"ibk1_cunas.{ext}")
    plt.close(fig)


# ---------------------------------------------------------------- slide 15: I-VU2, the problem as printed

# problem 2 of appendix A of [16], printed page 28, as docs/part2/f7_ivu2_derivation.md
# transcribes it. it is not in src/ because it was not run, and this is the one
# place the presentation states it.
ivu2 = {
    "G1": "G_1 = \\coef{[1, 1.5]}\\, \\marca{x_1} + \\coef{[1, 1.5]}\\, \\marca{x_2} + \\coef{[1, 1]}",
    "G2": "G_2 = \\coef{[1, 1.5]}\\, x_1^2 + \\coef{[2, 3]}\\, x_2^2 - \\coef{[1, 1]}",
    "box": "[-4, 4]^2",
}
macro("IVUone", ivu2["G1"], "[16] appendix A problem 2, as docs/part2/f7_ivu2_derivation.md transcribes it")
macro("IVUtwo", ivu2["G2"], "[16] appendix A problem 2, as docs/part2/f7_ivu2_derivation.md transcribes it")
macro("IVUbox", ivu2["box"], "[16] appendix A problem 2, as docs/part2/f7_ivu2_derivation.md transcribes it")

# ---------------------------------------------------------------- slide 16: the counterexample

derivation = (repository / "docs/part2/f2_ibk1_derivation.md").read_text(encoding="utf-8")
section = derivation.split("### 4.2")[1].split("### 4.3")[0]
x_star = tuple(Fraction(v) for v in re.search(r"x⋆ = \(([\d.]+), ([\d.]+)\)", section).groups())
y_point = tuple(Fraction(v) for v in re.search(r"y = \(([\d.]+), ([\d.]+)\)", section).groups())
table_rows = re.findall(r"G_(\d) (lower|upper)\s+([\d.]+)\s+([\d.]+)\s+\+([\d.]+)\s+yes", section)
assert len(table_rows) == 4, table_rows


def g_ibk1(x):
    # the four endpoint functions of I-BK1 from the printed coefficients: all four
    # h are squares, so the moore product is the fixed-order one, [16] page 27.
    x1, x2 = x
    h = [(x1 ** 2, x2 ** 2), ((x1 - shift) ** 2, (x2 - shift) ** 2)]
    out = []
    for objective in range(2):
        (a1, b1), (a2, b2) = ibk1_exact[objective]
        h1, h2 = h[objective]
        out.append((a1 * h1 + a2 * h2, b1 * h1 + b2 * h2))
    return out


g_y, g_star = g_ibk1(y_point), g_ibk1(x_star)
counter_rows = []
for (obj, end, gy_doc, gs_doc, margin_doc) in table_rows:
    i, j = int(obj) - 1, 0 if end == "lower" else 1
    gy, gs = float(g_y[i][j]), float(g_star[i][j])
    assert abs(gy - float(gy_doc)) < 1.5e-6, (obj, end, gy, gy_doc)
    assert abs(gs - float(gs_doc)) < 1.5e-6, (obj, end, gs, gs_doc)
    assert gy < gs
    name = f"$G_{obj}$ " + ("inferior" if end == "lower" else "superior")
    counter_rows.append((name, gy_doc, gs_doc, margin_doc))
min_margin = min(float(m) for *_, m in table_rows)
src16 = "docs/part2/f2_ibk1_derivation.md section 4.2 (re-computed here in exact rationals from src/problems_native.py's coefficients and asserted equal)"
macro("dXstar", f"({float(x_star[0]):.6f}, {float(x_star[1]):.6f})", "[16] Table 1 page 20, as " + src16)
macro("dY", f"({float(y_point[0]):.4f}, {float(y_point[1]):.4f})", src16)
macro("dMinMargin", f3(min_margin), f"{src16}: the smallest of the four margins")
with open(fragments_dir / "tabla_contraejemplo.tex", "w", encoding="utf-8") as handle:
    handle.write("% generated by experiments/make_presentation.py\n")
    handle.write(f"% source: {src16}\n")
    handle.write(r"\begin{tabular}{lrrr}" + "\n" + r"\toprule" + "\n")
    handle.write(r"coordenada & $G(y)$ & $G(x^\star)$ de [16] & margen \\" + "\n" + r"\midrule" + "\n")
    for name, gy, gs, margin in counter_rows:
        handle.write(f"{name} & {gy} & {gs} & +{margin} \\\\\n")
    handle.write(r"\bottomrule" + "\n" + r"\end{tabular}" + "\n")

def draw_counterexample():
    # slide 16 as a picture: four coordinates, our point against the printed one,
    # all four strictly smaller. the numbers are the ones the table carries.
    fig, ax = plt.subplots(figsize=(9.6, 4.2))
    y = np.arange(len(counter_rows))[::-1]
    names = [n.replace("$", "") for n, *_ in counter_rows]
    gy = [float(v) for _, v, _, _ in counter_rows]
    gs = [float(v) for _, _, v, _ in counter_rows]
    ax.barh(y + 0.19, gs, height=0.34, color="#9A9A9A", label=r"$G(x^\star)$, el punto que [16] publica")
    ax.barh(y - 0.19, gy, height=0.34, color="#B03A2E", label=r"$G(y)$, otro punto de su propia caja")
    for yy, a, b in zip(y, gy, gs):
        ax.text(b + 0.08, yy + 0.19, f"{b:.6f}", va="center", fontsize=12.5, color="#5A5A5A")
        ax.text(a + 0.08, yy - 0.19, f"{a:.6f}", va="center", fontsize=12.5, color="#B03A2E")
    ax.set_yticks(y)
    ax.set_yticklabels(names, fontsize=14)
    ax.set_xlim(0, max(gs) * 1.30)
    ax.set_xticks([])
    for side in ("left", "bottom"):
        ax.spines[side].set_visible(False)
    ax.tick_params(left=False)
    ax.text(max(gs) * 0.72, y[0] + 0.55, "las cuatro, estrictamente menores",
            fontsize=15, color="#B03A2E", fontweight="bold")
    ax.legend(frameon=False, loc="lower right", bbox_to_anchor=(1.0, -0.16), fontsize=12.5)
    fig.tight_layout()
    for ext in ("pdf", "png"):
        fig.savefig(out_dir / f"contraejemplo.{ext}")
    plt.close(fig)


dominators = read_simple(results / "part2/dominators_summary.csv")
n_config = len(dominators)
n_with = sum(1 for r in dominators if int(r["seeds_with_a_dominator"]) == int(r["n_seeds"]))
widest = max(float(r["widest_margin_over_seeds"]) for r in dominators)
src16b = "results/part2/dominators_summary.csv"
macro("dConfigs", str(n_config), f"{src16b}: number of rows (solver x phi x budget)")
macro("dConfigsWithDominator", str(n_with), f"{src16b}: rows with seeds_with_a_dominator == n_seeds")
macro("dWidestMargin", f3(widest), f"{src16b}: max of widest_margin_over_seeds")
assert n_with == n_config

# ---------------------------------------------------------------- slide 17: the range of the I-BK1 jaccard factors

ibk1_error = read_simple(results / "part2/instrument_error_ibk1.csv")
factors = []
for r in ibk1_error:
    if r["metric"] == "overlap" and float(r["delta"]) == 0.0:
        factors.append(jaccard_from_dice(float(r["measured_median"])) / jaccard_from_dice(float(r["exact"])))
assert len(factors) == 3
src17 = "results/part2/instrument_error_ibk1.csv, metric overlap, delta 0.0, jaccard = dice/(2-dice), measured/exact over the three pairs"
macro("iJacFactorMin", f"{min(factors):.2f}", src17 + " (min)")
macro("iJacFactorMax", f"{max(factors):.2f}", src17 + " (max)")

# ---------------------------------------------------------------- slide 5: the constant-width degeneration, measured

corr = from_doc("docs/part1/a1_uncertainty_model.md", r"correlation (\+1\.0000) and a within-bin spread")
macro("aCorrProportional", corr, "docs/part1/a1_uncertainty_model.md part 1, the proportional width, corr(centre, width)")

# ---------------------------------------------------------------- reserve R1: two counts from part 10

macro("rWidthValuesTrue", from_doc("docs/explicacion_proyecto.md", r"toma\s+\*\*(\d+)\*\* valores distintos"), "docs/explicacion_proyecto.md section 10.3")
macro("rWidthValuesSeen", from_doc("docs/explicacion_proyecto.md", r"valores distintos en una rejilla sale con \*\*(\d+)\*\*"), "docs/explicacion_proyecto.md section 10.3")
macro("rGridPoints", from_doc("docs/explicacion_proyecto.md", r"bit a bit en los (\d+) puntos"), "docs/explicacion_proyecto.md section 10.5")

# ---------------------------------------------------------------- reserve R2: the containment-fixed coverages

fixed = []
for path in [results / "tier0/instrument_error_p1.csv", results / "part2/instrument_error_ibk1.csv"]:
    for r in read_simple(path):
        if r["status"] == "check" and float(r["delta"]) == 0.0 and r["metric"].startswith("coverage") and float(r["exact"]) == 1.0:
            fixed.append((float(r["measured_median"]), float(r["measured_q1"]), float(r["measured_q3"])) if "measured_q1" in r else (float(r["measured_median"]),) * 3)
for eps in ("0.0", "0.05", "0.1", "0.25", "0.5"):
    for r in read_rows(results / f"tier1/table_2_measured_eps_{eps}.csv"):
        if r["status"] == "check" and float(r["delta"]) == 0.0 and r["metric"].startswith("coverage"):
            pair = (r["phi_a"], r["phi_b"], r["metric"])
            if pair in (("lu", "ls", "coverage_a_in_b"), ("ls", "cw", "coverage_b_in_a")):
                fixed.append((float(r["median"]), float(r["q1"]), float(r["q3"])))
assert fixed and all(m == 1.0 and q1 == 1.0 and q3 == 1.0 for m, q1, q3 in fixed), fixed
macro("rFixedCoverage", "1.000000", "instrument_error_p1.csv, instrument_error_ibk1.csv, table_2_measured_eps_*.csv: every check row with a containment-fixed direction")
macro("rFixedRange", "0", "same rows: q3 - q1")
macro("rFixedRows", str(len(fixed)), "same rows: how many were checked")

# ---------------------------------------------------------------- reserve R3: rank-one saturation

rank_rows = read_simple(results / "tier1/rank_one_summary.csv")
nsga = [r for r in rank_rows if r["solver"] == "nsga2" and float(r["eps"]) > 0 and int(r["n_evals"]) == 5000]
assert len(nsga) == 24 and all(r["saturates_in_every_seed"] == "True" for r in nsga)
generations = {(r["problem"], r["phi"], float(r["eps"])): int(float(r["first_saturated_generation"])) for r in nsga}
n_generations = {int(r["n_generations"]) for r in nsga}
assert len(n_generations) == 1
macro("rSatConfigs", str(len(nsga)), "results/tier1/rank_one_summary.csv: nsga2 rows with eps > 0 at n_evals 5000")
macro("rGenerations", str(n_generations.pop()), "results/tier1/rank_one_summary.csv: n_generations")
with open(fragments_dir / "tabla_saturacion.tex", "w", encoding="utf-8") as handle:
    handle.write("% generated by experiments/make_presentation.py\n")
    handle.write("% source: results/tier1/rank_one_summary.csv, solver nsga2, n_evals 5000, first_saturated_generation\n")
    handle.write(r"\begin{tabular}{llrrrr}" + "\n" + r"\toprule" + "\n")
    handle.write(r"problema & orden & $\varepsilon = 0.05$ & $0.10$ & $0.25$ & $0.50$ \\" + "\n" + r"\midrule" + "\n")
    for problem in ("zdt1_interval", "dtlz2_interval"):
        for i, phi in enumerate(("lu", "ls", "cw")):
            first = problem_name[problem] if i == 0 else ""
            cells = " & ".join(str(generations[(problem, phi, e)]) for e in eps_levels)
            handle.write(f"{first} & {tex_label[phi]} & {cells} \\\\\n")
        if problem == "zdt1_interval":
            handle.write(r"\addlinespace" + "\n")
    handle.write(r"\bottomrule" + "\n" + r"\end{tabular}" + "\n")

# ---------------------------------------------------------------- the speaker notes
# presentation/guion.txt is the spoken script, one block per slide separated by a
# blank gap, and it is the single place it lives: this turns it into
# \notaI ... \notaXVIII so that presentacion.tex's \note{} commands and the
# printed script cannot drift apart.

def latex_escape(text):
    for a, b in (("\\", r"\textbackslash{}"), ("&", r"\&"), ("%", r"\%"), ("$", r"\$"),
                 ("#", r"\#"), ("_", r"\_"), ("{", r"\{"), ("}", r"\}"), ("~", r"\textasciitilde{}"),
                 ("^", r"\textasciicircum{}")):
        text = text.replace(a, b)
    return text


def roman(n):
    numerals = [(10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
    out = ""
    for value, sign in numerals:
        while n >= value:
            out += sign
            n -= value
    return out


guion = (repository / "presentation/guion.txt").read_text(encoding="utf-8")
blocks = [b.strip() for b in re.split(r"\n\s*\n\s*\n+", guion) if b.strip()]
assert len(blocks) == 15, f"guion.txt has {len(blocks)} blocks, expected 15 (14 slides + the closing)"
with open(fragments_dir / "notas.tex", "w", encoding="utf-8") as handle:
    handle.write("% generated by experiments/make_presentation.py from presentation/guion.txt\n")
    handle.write("% one command per slide, in order; presentacion.tex uses them inside \\note{}.\n")
    # beamer prints all of a frame's \note commands on one note page and silently
    # truncates what does not fit, so the length is checked here instead: a block
    # over the budget stops the script and names itself, and the fix is to shorten
    # it in guion.txt rather than to discover the missing half on the day.
    note_budget = 1700
    too_long = [(i, len(" ".join(b.split()))) for i, b in enumerate(blocks, start=1)
                if len(" ".join(b.split())) > note_budget]
    assert not too_long, ("these guion.txt blocks do not fit on one note page "
                          f"(budget {note_budget} characters): {too_long}")
    for i, block in enumerate(blocks, start=1):
        body = " ".join(latex_escape(line.strip()) for line in block.splitlines() if line.strip())
        handle.write(f"\\newcommand{{\\Nota{roman(i)}}}{{\\note{{{body}}}}}\n")

# ---------------------------------------------------------------- write the macros and draw

with open(fragments_dir / "numbers.tex", "w", encoding="utf-8") as handle:
    handle.write("% generated by experiments/make_presentation.py; do not edit.\n")
    handle.write("% one \\newcommand per number, each with the file and key it was read from.\n")
    for name, value, source in macros:
        handle.write(f"% {name}: {source}\n")
        handle.write(f"\\newcommand{{\\{name}}}{{{value}}}\n")

draw_crisp()
draw_benchmark_fronts()
draw_p1()
draw_instrument()
draw_benchmarks()
draw_cardinalities()
draw_ibk1_crisp()
draw_ibk1()
draw_counterexample()

with open(out_dir / "PROVENANCE.md", "w", encoding="utf-8") as handle:
    handle.write("# Provenance of every generated number\n\n")
    handle.write("Written by `experiments/make_presentation.py`. One row per macro in `fragments/numbers.tex`.\n\n")
    handle.write("| macro | value | source |\n|---|---|---|\n")
    for name, value, source in macros:
        handle.write(f"| `\\{name}` | `{value}` | {source} |\n")
    handle.write("\n## Tables\n\n")
    handle.write(f"- `fragments/tabla_instrumento.tex` — {src10}; exact from {src7}\n")
    handle.write(f"- `fragments/tabla_benchmarks.tex` — {src11}\n")
    handle.write(f"- `fragments/tabla_contraejemplo.tex` — {src16}\n")
    handle.write("- `fragments/tabla_saturacion.tex` — results/tier1/rank_one_summary.csv\n")
    handle.write("\n## Figures\n\n")
    handle.write(f"- `p1_crisp.{{pdf,png}}` — p1 without uncertainty: the two anchors of its centres and the segment between them, which the script re-derives as the non-dominated subset of a 601x601 grid of the box\n")
    handle.write("- `p1_regiones.{pdf,png}` — the three closed forms of docs/part1/b1_phi_efficient_sets.md section 2.4 as masks; areas checked against results/tier0/exact_regions_p1.csv\n")
    handle.write("- `tamanos_eps.{pdf,png}` — cardinality_a and cardinality_b of the slide-11 rows\n")
    handle.write(f"- `instrumento.{{pdf,png}}` — the same three rows as the instrument table, drawn: {src10}\n")
    handle.write("- `zdt1_frente.{pdf,png}` and `dtlz2_frente.{pdf,png}` — the answer of each benchmark without uncertainty, evaluated with src/problems_tier1.py's own functions on the decision vectors the two papers state, with a 20000-point sample checked to dominate none of them\n")
    handle.write(f"- `benchmarks.{{pdf,png}}` — the eight cells of slide 11 drawn, plus the eps = 0 sanity point: {src11}\n")
    handle.write(f"- `contraejemplo.{{pdf,png}}` — the four inequalities drawn: {src16}\n")
    handle.write("- `ibk1_crisp.{pdf,png}` — I-BK1 stated: where each objective pulls, the band a level of an interval objective occupies, and the curve of constant nu that is its efficient set without uncertainty\n")
    handle.write("- `ibk1_cunas.{pdf,png}` — the bands of results/part2/exact_regions_ibk1.csv drawn between the hyperbolas nu = const; areas checked against the same file\n")

print(f"wrote {len(macros)} macros, {len(blocks)} notes, 4 tables and 10 figures under {out_dir.relative_to(repository)}")
