# Contribution and PR guidelines

Read AGENTS.md and NEW_REPO_INSTRUCTIONS.md. Inspect existing work and preserve it.
Use feature branches and PRs after the authorized empty-repo bootstrap. Keep each
PR focused; describe the concrete problem, resulting behavior, validation, and
material limitations. Use synthetic fixtures and omit machine data and secrets.

Run project-required checks. Keep a stable `build` check on every PR, bound to its
observed GitHub App ID, without path filters. Preserve existing required checks.
Keep main up to date, conversations resolved, history linear and administrators
subject to protections. Require zero separate approvals for a solo maintainer;
retain stronger existing requirements. Dismiss stale reviews. Never self-approve,
fabricate statuses, bypass protection or force-push shared history.

Use squash merges and delete merged branches. Keep Actions defaults read-only and
Actions PR creation/approval disabled. Keep PR checks separate from production
permissions; production deploys only from trusted main with matching environment
branch restrictions. Pin third-party Actions to verified full commit SHAs.

Before every commit/push, inspect staged and outgoing content and metadata with
active local privacy hooks. Use the exact approved public identity and UTC.
Verify server commit identity after publication. See the canonical instructions
for bootstrap, merge identity, privacy, PWA reuse and complete setup requirements.

For any Pages site, place a clickable **Live site** link immediately below the
README title, before badges or description. Use the Pages API URL and verify it
responds successfully; clearly mark a deployment pending until live. Keep the
registry URL current. Do not add a fictitious Pages URL to non-site projects.

Roll shared standards out through one focused PR per repo. Preserve stronger
protections, local product policies, release rulesets and checks. Read settings
back after changes. Record permission or plan blockers instead of bypassing them.
