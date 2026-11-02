# Repository setup checklist

- Record the reviewed infoe-labs/new-repo standards commit and inspect local rules.
- Confirm owner, name, visibility and publication authorization.
- Apply the approved exact local author/committer identity; reconcile conflicts.
- Install and verify local, untracked privacy hooks. Audit all outgoing content.
- Adapt AGENTS.md, README, PR template, ignore rules and project-required CI.
- Only an authorized empty-repo bootstrap may establish main directly.
- Observe the real stable build check and App ID; preserve existing required checks.
- Require PRs, strict checks, conversation resolution, stale-review dismissal,
  linear history and admin enforcement; prohibit deletion/force-push and bypasses.
- Keep stronger review/signature/restriction policies; solo default is zero approvals.
- Enable squash merges and feature-branch deletion; Actions default read-only,
  with PR creation/approval disabled. Verify settings by reading them back.
- For Pages, configure Actions hosting and main-only deployment/environment;
  verify the live URL and put its link immediately below the README title.
- Verify remote CI and metadata; register the repo and any explicit exceptions.

Use NEW_REPO_INSTRUCTIONS.md for the complete baseline. Templates alone do not
configure GitHub server settings, credentials, hooks, environments or hosting.
