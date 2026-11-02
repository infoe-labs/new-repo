#!/usr/bin/env python3
"""Read-only GitHub governance audit. No third-party dependencies."""
import base64
import json
from pathlib import Path
import subprocess
import sys


def api(path):
    result = subprocess.run(['gh', 'api', path], capture_output=True, text=True)
    if result.returncode:
        raise RuntimeError('GitHub API unavailable: ' + path)
    return json.loads(result.stdout)


def audit(entry):
    repo = entry['repository']
    root = 'repos/' + repo
    findings = []
    def require(condition, message):
        if not condition:
            findings.append(message)
    meta = api(root)
    require(meta['default_branch'] == 'main', 'default branch must be main')
    require(meta['allow_squash_merge'] and meta['delete_branch_on_merge'], 'squash/branch cleanup settings')
    require(not meta['allow_merge_commit'] and not meta['allow_rebase_merge'], 'only squash merges expected')
    actions = api(root + '/actions/permissions/workflow')
    require(actions['default_workflow_permissions'] == 'read' and not actions['can_approve_pull_request_reviews'], 'Actions defaults')
    # Classic protection and rulesets can coexist. Audit rulesets for bypasses,
    # and use the effective branch rules endpoint when classic protection is absent.
    rulesets = api(root + '/rulesets')
    for summary in rulesets:
        if summary['target'] == 'branch' and summary['enforcement'] == 'active':
            ruleset = api(root + '/rulesets/' + str(summary['id']))
            require(not ruleset.get('bypass_actors'), 'active branch ruleset has bypass actors')
    result = subprocess.run(['gh', 'api', root + '/branches/main/protection'], capture_output=True, text=True)
    checks = []
    if result.returncode == 0:
        p = json.loads(result.stdout)
        for key in ['enforce_admins', 'required_linear_history', 'required_conversation_resolution']:
            require(p.get(key, {}).get('enabled'), key)
        for key in ['allow_force_pushes', 'allow_deletions', 'lock_branch']:
            require(not p.get(key, {}).get('enabled'), key)
        review = p.get('required_pull_request_reviews') or {}
        require(bool(review), 'required PRs')
        require(review.get('dismiss_stale_reviews'), 'dismiss stale reviews')
        require(not review.get('bypass_pull_request_allowances'), 'PR bypass allowances')
        status = p.get('required_status_checks') or {}
        require(status.get('strict'), 'strict required checks')
        checks = [(c['context'], c.get('app_id')) for c in status.get('checks', [])]
    elif '404' in result.stderr:
        rules = api(root + '/rules/branches/main')
        types = {r['type']: r for r in rules}
        for key in ['deletion', 'non_fast_forward', 'required_linear_history', 'pull_request', 'required_status_checks']:
            require(key in types, key)
        review = types.get('pull_request', {}).get('parameters', {})
        require(review.get('dismiss_stale_reviews_on_push'), 'dismiss stale reviews')
        require(review.get('required_review_thread_resolution'), 'resolve conversations')
        status = types.get('required_status_checks', {}).get('parameters', {})
        require(status.get('strict_required_status_checks_policy'), 'strict required checks')
        checks = [(c['context'], c.get('integration_id')) for c in status.get('required_status_checks', [])]
    else:
        raise RuntimeError('Protection API unavailable: ' + repo)
    runs = api(root + '/commits/main/check-runs?per_page=100')['check_runs']
    observed = {(r['name'], r['app']['id']) for r in runs}
    for name in entry['required_checks']:
        require(any(c == name and app is not None and (c, app) in observed for c, app in checks), 'required check with observed app: ' + name)
    readme = base64.b64decode(api(root + '/readme')['content']).decode('utf-8')
    # Query Pages even for non-site entries so newly enabled sites cannot escape audit.
    result = subprocess.run(['gh', 'api', root + '/pages'], capture_output=True, text=True)
    if result.returncode == 0:
        pages = json.loads(result.stdout)
        url = pages['html_url']
        require(entry['pages_url'] == url, 'registry Pages URL differs')
        require(pages.get('build_type') == 'workflow', 'Pages source must be Actions')
        lines = [line.strip() for line in readme.splitlines() if line.strip()]
        require(len(lines) > 1 and lines[0].startswith('# ') and '](' + url + ')' in lines[1], 'Pages link immediately below README title')
    elif '404' in result.stderr:
        require(entry['pages_url'] is None, 'registered Pages site unavailable')
    else:
        raise RuntimeError('Pages API unavailable: ' + repo)
    return {'repository': repo, 'findings': findings}


def main():
    registry = json.loads((Path(__file__).resolve().parents[1] / 'repos.json').read_text())
    reports = []
    for entry in registry['repositories']:
        try:
            reports.append(audit(entry))
        except (RuntimeError, KeyError, ValueError) as error:
            reports.append({'repository': entry['repository'], 'findings': [str(error)]})
    print(json.dumps(reports, indent=2))
    return int(any(r['findings'] for r in reports))


if __name__ == '__main__':
    sys.exit(main())
