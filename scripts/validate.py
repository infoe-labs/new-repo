#!/usr/bin/env python3
"""Validate the starter kit without network access."""
import ast
import json
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
registry = json.loads((root / 'repos.json').read_text())
assert registry['schema_version'] == 1
seen = set()
for repo in registry['repositories']:
    assert re.fullmatch(r'infoe-labs/[a-z0-9-]+', repo['repository'])
    assert repo['repository'] not in seen
    seen.add(repo['repository'])
    assert repo['default_branch'] == 'main'
    assert 'build' in repo['required_checks']
    assert repo['pages_url'] is None or repo['pages_url'].startswith('https://')
for name in ['AGENTS.md', 'CONTRIBUTING.md', 'NEW_REPO_INSTRUCTIONS.md', '.github/pull_request_template.md', 'templates/AGENTS.md', 'templates/README.md', 'templates/REPOSITORY_SETUP.md', 'docs/MONITORING.md']:
    assert (root / name).is_file(), name
for script in (root / 'scripts').glob('*.py'):
    ast.parse(script.read_text())
print('Starter kit validation passed')
