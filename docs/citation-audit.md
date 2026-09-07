# Citation reconciliation

This audit uses the authors' August 2026 manuscript snapshot, `Late_Interaction (33).pdf` (59 PDF pages including front matter), previously used to initialize this repository. It does not assert identity with a subsequently replaced SSRN PDF.

The snapshot has **121 bibliography entries, representing 120 distinct works/resources**. All 120 have body citation evidence and a literature record. The previous 76 entries are retained; 44 additional records cover omitted papers, background, benchmarks, and software. These are not 120 core late-interaction methods.

The reconciliation records **261 explicit citation occurrences** (including table citations and the undated Qdrant attribution) and **96 additional named-discussion placements**. Multiple mentions within a subsection do not produce duplicate reading-list rows. Named discussion supplements explicit citations; it is not presented as a fresh author–year citation.

| Layer | File | Evidence |
| --- | --- | --- |
| Body citation / named discussion | [citation-occurrences.json](../data/citation-occurrences.json) | Subsection, citation or method name, extraction line; PDF page for explicit citations |
| Literature record | [papers.json](../data/papers.json) | Stable ID/key, authors, source reference, aliases, category, cited and discussed subsections |
| Export and list | [references.bib](../references.bib), [README](../README.md#reading-lists) | One bibliography entry per work; complete bibliography plus contribution-based chapter selections |

Extraction lines refer to the reviewed text extraction, not universal PDF line numbers. Pages count front matter. Floating tables are associated with the preceding subsection in PDF reading order; named mentions can additionally place a paper in its substantive discussion subsection. A section cross-reference alone does not imply that every paper in the target section is discussed again.

The record-driven author–year scan was checked against an independent scan for unmatched author–year strings. Shorthand years (`2022b,a`, `2021, 2022`), line-broken surnames, and the undated attribution were resolved. “Workshop … ECIR 2026” is an event name, not an additional citation.

## README presentation

The README uses one table per chapter (§§3–11), with background and boundary cases in a final table. The detailed subsection evidence remains in the data files. Chapter tables are selected by substantive contribution using `data/reading-list-selection.json`; they are not exhaustive unions of subsection citations. Every reference has an explicit disposition: selected chapters with a rationale per chapter, the background table, or bibliography-only. Source discussion locations remain separate from editorial topic placement. For example, SaMer and ColChunk are read under representation reduction, and Flash-MaxSim/TileMaxSim under efficient execution, while their actual manuscript locations remain unchanged in the evidence data. COIL and XTR retain their substantive method placements. Display metadata is maintained separately in `data/reading-list-display.json`.

## Corrections

- `Killingback et al., 2026a` and `2026b` identify the same Signed MaxSim paper. Both source aliases resolve to one BibTeX entry, `killingback2026a`. The manuscript itself still needs this duplicate corrected.
- `Kim et al., 2026` (HEAVEN) and `Kim, 2026` (LITTA) remain distinct. Author-count distinctions also disambiguate Lin 2021 and Nogueira 2019.
- In the source-evidence data, SaMer is mapped to §11.1; ColChunk to §10.2; Flash-MaxSim/TileMaxSim to §11.2; POQD to §8.3 and §11.3. LITTA appears in both query-side and multimodal discussions. Introduction mentions are retained separately.
- Background and boundary works include Poly-encoders, ME-BERT, MVR, MLR, DPR, ANCE, Contriever, lexical/sparse baselines, and agentic context. A core method appearing in §1 is not automatically classified as a boundary case.
- Missing surveyed works added include token importance, late-interaction dynamics, Jina-ColBERT-v2, LeapMV, ConstBERT, Light-ColPali/Light-ColQwen2, IGP, DESSERT, ALIGNER, M3-Embedding, Col⋆, PyLate, NevIR, Beneath [MASK], JaColBERTv2.5, Video-ColBERT, HEAVEN, and AGREE.
- Metadata follows the surveyed version; source reference strings preserve original metadata. Initials are preserved rather than guessed full names. Truncated author lists for Ma 2025 and Ni 2022 were completed from ACL Anthology. Name-order normalizations retain the source citation aliases.

## Revalidation

```sh
python scripts/build_reading_lists.py
python scripts/validate_references.py
```

Validation checks evidence-to-record resolution, aliases, exact cited/discussed subsection sets, one-to-one BibTeX keys, separation of the survey citation, and actual rows in each README chapter and the final background/boundary table. It checks README rows against editorial selections, requires a reason for each selected chapter or non-chapter disposition, and retains complete source-to-bibliography checks. Unselected source citations are not treated as missing README rows. Scientific relevance remains an editorial judgment rather than something the script can prove.

This validates the curated snapshot correspondence, not an unseen revised PDF. For a manuscript update, reread its body and bibliography and update the evidence manifest before regenerating. This audit does not independently revalidate every paper's scientific claims or promise continuous external-link availability.
