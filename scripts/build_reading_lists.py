"""Rebuild checked-in reading lists and BibTeX from curated survey records."""
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[1]


def outputs():
    papers = json.loads((ROOT / 'data/papers.json').read_text())
    sections = json.loads((ROOT / 'data/sections.json').read_text())
    readme = (ROOT / 'README.md').read_text()
    prefix = readme.split('## Reading Lists')[0]
    prefix = re.sub(r'This initial collection contains.*?See \[coverage and provenance\]\(docs/coverage.md\)\.', 'The collection contains **120 distinct bibliography records** from the August 2026 survey snapshot, including background work and software. Reading lists follow the actual numbered subsections; the same paper can appear wherever it is cited or discussed. See [coverage and provenance](docs/coverage.md) and the [citation audit](docs/citation-audit.md).', prefix)
    prefix = prefix.replace('| 2 | Definition and boundaries | [Scope](#scope) |', '| 1–2 | Background and boundary cases | [Reading list](#background-and-boundary-cases) |')
    prefix = prefix.replace('engines, proxies, query pruning, and fused scoring in Section 6.', 'engines, proxies, and query pruning in Section 6; fused scoring kernels in Section 11.2.')
    text = prefix + '## Reading Lists\n\n'
    text += 'Download [references.bib](references.bib) for the cited literature; use [survey.bib](survey.bib) to cite the survey itself. **Cited** denotes an explicit author–year citation (including table citations); **mentioned** denotes a named discussion whose citation is supplied elsewhere. Parent-section entries cover introductory text; subsections without a new citation or named reference are retained in the outline.\n\n'
    for sec in sections:
        sid = sec['id']
        if sid == '1':
            text += '<a id="background-and-boundary-cases"></a>\n\n### Background and boundary cases — §§1–2\n\nPoly-encoders, ME-BERT, MVR, and MLR illustrate the wider multi-vector family. DPR, ANCE, and Contriever supply single-vector baselines. Their inclusion is background context, not a classification as core late interaction. Canonical methods cited in the introduction are listed separately below.\n\n'
        level = '###' if '.' not in sid else '####'
        text += f'<a id="section-{sid}"></a>\n\n{level} §{sid} {sec["title"]}\n\n'
        selected = [p for p in papers if sid in p['discussed_in_sections']]
        if not selected:
            text += 'No additional explicit citation or identified named-paper discussion in this subsection; see the surrounding subsections.\n\n'
        for category, label in [('late-interaction-and-extensions', 'Late-interaction methods, systems, analyses, and extensions'), ('background-and-boundary', 'Background and boundary cases'), ('software', 'Software and infrastructure')]:
            group = [p for p in selected if p['category'] == category]
            if not group:
                continue
            text += f'**{label}**\n\n| Work / paper | Survey citation | Evidence |\n| --- | --- | --- |\n'
            for p in group:
                title = p['title'].replace('|', '\\|')
                name = p['name'].replace('|', '\\|')
                label = title if name.casefold() == title.casefold() else f'{name} — {title}'
                evidence = 'Cited' if sid in p['cited_in_sections'] else 'Mentioned'
                text += f'| [{label}]({p["url"]}) | {" / ".join(p["source_citations"])} · `{p["citation_key"]}` | {evidence} |\n'
            text += '\n'
    text += '## Citation' + readme.split('## Citation', 1)[1]
    text = text.replace('The initial release follows the survey\'s component-based organization.', 'The reading lists follow the survey\'s numbered subsections with many-to-many paper placement.')
    bib = '% Literature cited by the survey; cite the survey itself using survey.bib.\n% Author initials and publication years follow the surveyed reference version.\n\n'
    for p in papers:
        def esc(value):
            return value.replace('&', r'\&').replace('%', r'\%').replace('_', r'\_').replace('⋆', r'$\star$')
        fields = {'title': '{' + esc(p['title']) + '}', 'author': ' and '.join('{' + a + '}' if ',' not in a else a for a in p['authors'])}
        if p['year']:
            fields['year'] = str(p['year'])
        fields['url'] = p['url']
        source = p['source_reference']
        venue = source.split(', in:', 1)[1] if ', in:' in source else p.get('reference_venue_or_version', '')
        venue = re.split(r'URL:|doi:|arXiv:', venue)[0].strip(' .,')
        if venue:
            fields['howpublished'] = esc(venue)
        fields['note'] = 'Survey citation: ' + '; '.join(p['source_citations'])
        bib += '@misc{' + p['citation_key'] + ',\n' + ',\n'.join('  ' + k + ' = {' + v + '}' for k, v in fields.items()) + '\n}\n\n'
    return {'README.md': text, 'references.bib': bib}


if __name__ == '__main__':
    for path, content in outputs().items():
        (ROOT / path).write_text(content)
