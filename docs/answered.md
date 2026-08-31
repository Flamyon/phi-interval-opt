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
