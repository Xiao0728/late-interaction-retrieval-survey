# Contributing

Suggestions, corrections, and paper additions are welcome through issues or pull requests.

## Adding a paper

Provide the exact title, authors, year, primary paper URL, venue or preprint status, and all relevant survey subsections. Include one sentence explaining the intervention and, when available, a link to the authors' code or model. Mark the entry as **survey-covered** or **post-survey addition**, supported by a section reference or publication date.

Place each work in every subsection where it is cited or substantively discussed. Keep one literature record with many-to-many subsection mappings. Separate explicit citations from named mentions, and keep background/boundary work and software labeled. Do not infer actual discussion locations solely from technical similarity.

Prefer DOI landing pages, ACL Anthology, publisher proceedings, OpenReview, or arXiv. Do not infer a DOI or code URL from a naming pattern. A preprint and its conference version should normally share one entry; an extended journal study may have a separate entry when its contribution warrants it.

Update `data/papers.json` and `data/citation-occurrences.json` with source evidence; preserve source aliases when deduplicating. Update `data/sections.json` if the manuscript outline changes. Run `python scripts/build_reading_lists.py` and `python scripts/validate_references.py` to regenerate and check `README.md` and `references.bib`. Keep `survey.bib` reserved for citing the survey. Add a note to `CHANGELOG.md` for substantive changes. The validator checks the curated evidence; a new manuscript requires a fresh body citation audit.

## Claims and measurements

Describe mechanisms concretely. Avoid universal claims such as "best", "lossless", or "exact" unless the paper establishes the stated conditions. Do not combine latency or effectiveness from incompatible datasets, candidate depths, hardware, or scoring protocols into one leaderboard.

Keep original model scoring, approximate retrieval, and final reranking separate. For compression results, distinguish vector payload from complete index storage.

## Corrections

Identify the affected entry and provide the primary source supporting the correction. For a broken link, supply the replacement and explain whether it refers to the same version.

## Rights

Link to papers and code rather than uploading third-party PDFs or assets without permission. This repository does not change the licenses of linked materials.
