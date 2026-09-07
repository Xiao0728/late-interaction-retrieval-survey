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
    prefix = re.sub(r'The collection contains.*?\[citation audit\]\(docs/citation-audit.md\)\.', 'The collection contains **120 distinct bibliography records** from the August 2026 survey snapshot, including background work and software. Papers are grouped by survey chapter; a work may appear in multiple relevant chapters. Background and boundary cases are collected at the end. See [coverage and provenance](docs/coverage.md).', prefix)
    text = prefix + '## Reading Lists\n\n'
    text += 'Download [references.bib](references.bib) for the literature, or [survey.bib](survey.bib) to cite the survey.\n\n'
    display = json.loads((ROOT / 'data/reading-list-display.json').read_text())

    def table(group):
        result = '| Work | Year / venue or version | Paper | Main contribution / relevance |\n| --- | --- | --- | --- |\n'
        for paper in sorted(group, key=lambda p: (p['year'] or 0, p['name'].casefold())):
            extra = display.get(paper['citation_key'], {})
            def cell(value):
                return str(value).replace('|', r'\|').replace('\n', ' ')
            name = cell(extra.get('name', paper['name']))
            venue = extra.get('venue', paper.get('reference_venue_or_version', ''))
            date = str(paper['year'] or 'n.d.') + (' · ' + venue if venue else '')
            role = extra.get('role', paper.get('role', ''))
            result += f"| {name} | {cell(date)} | [{cell(paper['title'])}]({paper['url']}) | {cell(role)} |\n"
        return result + '\n'

    for chapter in range(3, 12):
        heading = next(sec['title'] for sec in sections if sec['id'] == str(chapter))
        text += f'<a id="section-{chapter}"></a>\n\n### Section {chapter}: {heading}\n\n'
        group = [p for p in papers if p['category'] != 'background-and-boundary' and any(s.split('.')[0] == str(chapter) for s in p['discussed_in_sections'])]
        text += table(group)
    text += '<a id="background-and-boundary-cases"></a>\n\n### Background and Boundary Cases\n\n'
    text += 'These works provide background, wider multi-vector designs, comparison methods, and evaluation context. Poly-encoders, ME-BERT, MVR, and MLR illustrate the wider multi-vector family; DPR, ANCE, and Contriever are single-vector baselines. COIL and XTR remain in their substantive chapters because the survey discusses their modified forms of late interaction in detail.\n\n'
    text += table([p for p in papers if p['category'] == 'background-and-boundary'])
    text += '## Citation' + readme.split('## Citation', 1)[1]
    text = text.replace("The reading lists follow the survey's numbered subsections with many-to-many paper placement.", "The reading lists follow the survey's chapters, with background and boundary cases collected separately.")
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
