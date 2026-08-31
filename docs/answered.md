# phi-interval-opt: answered questions and retired risks

moved out of PROGRESS.md in session a1-b, unchanged. a p-row or s-row lands here
once it has an answer, a risk once it is retired. numbering is shared with
PROGRESS.md and never reused.

nothing is deleted here. a row is kept with the reasoning that retired it, so a
later session can see why it stopped being live rather than finding it gone.


## answered questions from section 5, questions the papers answer

none yet. p-05 was narrowed in a3 but is still open and stays in PROGRESS.md.


## answered questions from section 6, questions only the supervisors can answer

none yet. every s-row is still marked "not yet asked" and stays in PROGRESS.md.


## retired risks

r-07 | closed in a3-b, its premise removed rather than mitigated. as raised in a1
    this said that computing an image coordinate as f_u - f_l is unsafe when the
    width is constant or near zero, the cancellation error of order eps|f| being
    the entire content of the second coordinate under phi_ls and phi_cw. a4-b
    measured it: eps|c| exactly, 1.1e-07 at |c| = 1e9, and the shattering of a
    width column's 46 true values into 210 on p1's grid. d-02 removed the
    subtraction instead of covering it. every phi now has a centre-radius route,
    the same phi composed with M = [[1, -1], [1, 1]], and a problem declares which
    route applies to it; p1 returns its centre and half-width and builds no
    endpoint, and p0's endpoints are the paper's own and are exact, -|x| + |x|
    being exactly zero and |x| - (-|x|) exactly 2|x|. the a4 test's rounding step
    was deleted and the same grids return a1-b's counts without it, 31, 460, 1505
    and 961 on the box and 40, 724, 2496 and 1600 on the slice | it would have
    cost a study reporting arithmetic as a phi effect, which a1 showed reads as a
    positive result and not as an error | no longer live | what remains is not a
    risk but a discipline, and it is carried in CONTEXT.md sections 4 and 10
    rather than here: a problem must declare the representation it actually
    computes in. a problem that genuinely computes endpoints may still subtract
    them, and there is no better route for it, but one that computes a centre and
    a half-width and declares "endpoints" would put the error back. the tier 1
    eps = 0 baseline is also improved rather than merely labelled: in centre and
    half-width form its second coordinate is exactly zero and not a cancellation
    residue

r-01 | closed in a4. as raised in a0 this said the source papers were not under
    version control: .gitignore line 1 is "*.txt", so git mv failed and the two
    files were moved with plain mv. a0-b committed both papers and added the
    "!papers/*.txt" exception to .gitignore, so the premise is gone: the exact
    text a0 verified against is now in history and a re-extraction that differed
    from it would show as a diff | it would have cost the recoverability of the
    verified text, silently | no longer live | none needed. r-03, the missing pdf
    of [1], is a different risk and is still open in PROGRESS.md

r-10 | closed in a3, and the entry is kept rather than deleted because the
    reasoning is worth having on record. as raised in a2 this said gh_difference
    was the first piece of code in the project cited to a literature/ summary
    rather than to a paper, [1] containing no gh-difference at all, v-35. that
    premise no longer holds: slide 5 equation (2) of
    papers/Presentacion_optimizacion_intervalar.txt states the same definition,
    is a primary source in papers/, and is now the citation in the code, with the
    summary kept as a secondary that agrees with it, v-39. the risk as stated,
    that an unverified summary formula propagates through every later use, is
    therefore retired | it would have cost every later use of gh_difference, had
    the summary been wrong | no longer live | none needed. what remains is p-05,
    which is a citation-quality question about the definition number in [10] and
    not a correctness risk
