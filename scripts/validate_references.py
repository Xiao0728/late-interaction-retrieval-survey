"""Validate body evidence -> literature record -> bibliography -> reading list."""
import collections
import json
import re
from build_reading_lists import ROOT, outputs

papers = json.loads((ROOT / 'data/papers.json').read_text())
occurrences = json.loads((ROOT / 'data/citation-occurrences.json').read_text())
sections = {s['id'] for s in json.loads((ROOT / 'data/sections.json').read_text())}
records = {p['citation_key']: p for p in papers}
assert len(records) == len(papers), 'Duplicate citation key'
assert len({p['id'] for p in papers}) == len(papers), 'Duplicate work ID'
cited, discussed = collections.defaultdict(set), collections.defaultdict(set)
for occurrence in occurrences:
    key, section = occurrence['citation_key'], occurrence['section']
    assert key in records, f'Body evidence has no literature record: {key}'
    assert section in sections, f'Unknown subsection: {section}'
    assert occurrence['source_line'] > 0, f'Missing source locator: {key}'
    discussed[key].add(section)
    if occurrence['kind'] == 'explicit-citation':
        cited[key].add(section)
        alias = occurrence['source_citation']
        assert alias in records[key]['source_citations'] or (key == 'qdrantteamnd' and alias == 'Qdrant Team (undated)'), f'Unresolved source citation: {alias}'
        assert occurrence['pdf_page'] > 0
    else:
        assert occurrence['kind'] == 'named-mention' and occurrence['mention']
for key, paper in records.items():
    assert cited[key], f'Record lacks body citation evidence: {key}'
    assert cited[key] == set(paper['cited_in_sections']), f'Citation mapping mismatch: {key}'
    assert discussed[key] == set(paper['discussed_in_sections']), f'Discussion mapping mismatch: {key}'
    assert paper['authors'] and paper['title'] and paper['url'], f'Incomplete metadata: {key}'
keys = re.findall(r'^@\w+\{([^,]+),', (ROOT / 'references.bib').read_text(), re.M)
assert len(keys) == len(set(keys)) and set(keys) == set(records), 'BibTeX records differ'
survey = re.findall(r'^@\w+\{([^,]+),', (ROOT / 'survey.bib').read_text(), re.M)
assert survey == ['wang2026lateinteractionsurvey'], 'survey.bib must cite only the survey'
assert not set(survey) & set(keys), 'Survey citation mixed into literature bibliography'
selection = json.loads((ROOT / 'data/reading-list-selection.json').read_text())
assert set(selection) == set(records), 'Each reference needs an explicit editorial disposition'
for key, decision in selection.items():
    assert set(decision['source_sections']) == discussed[key], f'Stale curation evidence: {key}'
    assert decision['placement'] in {'chapters', 'background', 'bibliography-only'}
    if decision['placement'] == 'chapters':
        assert decision.get('chapters'), f'No selected chapter: {key}'
        for chapter, rationale in decision['chapters'].items():
            assert chapter in {str(i) for i in range(3, 12)} and rationale['reason'].strip()
    else:
        assert not decision.get('chapters') and decision['reason'].strip()
readme = (ROOT / 'README.md').read_text()
for section in [str(i) for i in range(3, 12)] + ['background-and-boundary-cases']:
    anchor = section if section == 'background-and-boundary-cases' else 'section-' + section
    block = readme.split(f'<a id="{anchor}"></a>', 1)[1].split('<a id=', 1)[0].split('## Citation', 1)[0]
    actual = re.findall(r'\]\((https?://[^\s]+)\) \|', block)
    if section == 'background-and-boundary-cases':
        expected = [p['url'] for p in papers if selection[p['citation_key']]['placement'] == 'background']
    else:
        expected = [p['url'] for p in papers if section in selection[p['citation_key']].get('chapters', {})]
    assert len(actual) == len(set(actual)), f'Duplicate paper within chapter: {section}'
    assert set(actual) == set(expected), f'Reading list mismatch: {section}'
assert all(f"]({p['url']})" in readme for p in papers if selection[p['citation_key']]['placement'] != 'bibliography-only'), 'Selected literature omitted from README'
for path, content in outputs().items():
    assert (ROOT / path).read_text() == content, f'Stale generated file: {path}'
print(f'PASS: {len(papers)} literature records; {len(occurrences)} evidence records; {len(sections)} outline entries; survey citation separate.')
