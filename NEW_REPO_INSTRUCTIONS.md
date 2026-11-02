# Instructions for new repositories

When the owner points you to this document, apply these defaults to the requested
repository. Inspect its existing instructions and work first. The owner's current
request takes precedence; preserve stronger existing privacy and protection rules.
Implement the requested product, not merely a plan, and continue through authorized
validation and delivery. Ask only for information or authority actually missing.

## Approved public Git identity

The owner-approved pseudonymous identity is exactly:

```text
infoe-bots <349551173+infoe-labs@users.noreply.github.com>
```

Use it for **both author and committer** in repositories to which the owner applies
this document. This document supplies explicit identity approval: do not ask again
for the name/email simply because a new repository lacks local configuration.
Do not infer identity from OS accounts, global Git settings, GitHub authentication,
hostnames, home directories or another repository. A conflicting existing local
identity must be reconciled with the owner before replacement.

On a new, unconfigured destination, configure **repository-local** settings:

```sh
git config --local user.name 'infoe-bots'
git config --local user.email '349551173+infoe-labs@users.noreply.github.com'
git config --local user.useConfigOnly true
git config --local commit.gpgsign false
git config --local tag.gpgsign false
```

Do not change global Git configuration. Leave existing approved signing intact;
the signing-disable defaults above apply when no approved signing identity exists.
Use UTC for new commit timestamps, e.g. `TZ=UTC git commit ...`. Before committing,
check `git var GIT_AUTHOR_IDENT` and `git var GIT_COMMITTER_IDENT`: environment
variables can override local settings. Verify the actual resulting commit too.
Never add personal signoffs or co-author trailers.

For verified GitHub-generated merges, the public service committer
`GitHub` with its public service noreply email is acceptable; the author must still be exactly the
approved `infoe-bots` identity above. Never use the service identity for local
commits. Audit server commit metadata and keep local hook exceptions narrow
(prefer explicitly audited commit SHAs over an unrestricted service allowlist).

For GitHub-generated merges, local settings are insufficient. Explicitly select
the approved noreply email, verify the proposed public author/committer identities,
and immediately audit the resulting commit. If GitHub would use another identity,
resolve that before merging; do not silently broaden a local allowlist. Never
impersonate a reviewer or approve your own PR.

## Public-repository privacy

Treat tracked files, Git history, PR text, CI logs, artifacts and releases as public.
Keep personal identities, private emails, machine usernames, hostnames, IP addresses,
physical locations, absolute machine paths, tokens, credentials and user content
out of them. Required upstream license notices must retain their legal attribution.
Use synthetic fixtures. Report generic errors instead of logging user payloads or
raw exceptions. Keep environment files, secrets, generated output and local test
artifacts ignored. Do not include local machine details in commit/PR descriptions.

Install or adapt privacy checks locally under `.git/hooks`; never track their
implementation, private denylists, identity policy files or credentials. Verify
`core.hooksPath` and executable permissions. Hooks must validate pending/outgoing
author and committer identities and scan staged/outgoing content and messages for
private data and secrets. Do not copy another repository's `.git` directory.
Never bypass hooks with `--no-verify`, equivalent options or temporary disabling.
If a hook rejects content, fix the content; do not weaken the check to publish it.

Before **every commit and push**:

1. Inspect the staged diff and filenames; check identity, secrets and machine data.
2. Run the intended hooks normally and verify exact author/committer metadata.
3. Audit every outgoing commit and its tracked content, not only the latest diff.
4. After publication or merge, verify the actual remote commit metadata and checks.

Do not repair a published identity leak by silently rewriting history. Stop further
publication, notify the owner without repeating private details, and coordinate
cleanup and credential revocation where relevant.

## Repository setup and delivery

- Inspect `AGENTS.md`, README, working tree, branch, origin and existing remote
  history. Preserve the owner's changes. Verify the destination and visibility
  with `gh repo view`; authentication identity is not a Git author identity.
- Write a project-specific `AGENTS.md` retaining this privacy/identity policy,
  required checks, storage rules and repository delivery conventions. Write an
  accurate README covering actual behavior, limitations and deployment.
- Prepare and validate a concrete result before seeking a final approval that is
  actually required. Do not ask again for actions already authorized by the owner.
- A request to build locally alone does not authorize public publication. A request
  to push/deploy an **empty** destination authorizes the one-time initial `main`
  bootstrap needed to establish CI, unless the owner says otherwise. Audit it with
  the same privacy hooks and approved identity. Never force-push over existing work.
- After bootstrap, use feature branches and PRs. Existing repositories use PRs from
  the outset. Honor required checks/reviews/conversations and never bypass protection,
  force a merge, fabricate statuses, or weaken rules to land a change.
- Use `gh` to inspect server settings; a source copy does not copy repository rules,
  hooks, permissions, environments or Pages configuration. Preserve stronger rules.
- Establish protected `main`: required PRs, required passing `build` check with the
  observed GitHub App ID, strict/up-to-date checks, resolved conversations, linear
  history, admin enforcement, and no force pushes or branch deletion. Require zero
  separate approving reviews for a solo-maintainer repo unless an independent
  reviewer or existing policy requires more. No bypass actors or locked-branch trick.
- Set Actions default token permission to read-only and disallow Actions from creating
  or approving PRs. Enable squash merges and automatic feature-branch deletion where
  appropriate. Never replace stronger existing settings with a weaker template.
- If GitHub permissions/plan restrictions prevent protection, report the exact gap;
  do not claim it is configured. Protection is checked by reading settings, not by
  attempting a forbidden direct push.
- For multiline PR bodies, use a temporary file with `gh pr create --body-file`.
  Keep public descriptions free of local paths, identities and conversational debris.

## Required new-repository setup checklist

This is the normal baseline when repository setup/publication is authorized.
Configure it on GitHub, then read it back; copying workflow files is insufficient.
Preserve any stronger existing rules and explain permission/plan blockers.

| Setting | Required baseline |
| --- | --- |
| Default branch | `main` |
| Ordinary changes | Feature branch → pull request → passing checks → merge |
| Direct pushes to `main` | Blocked, including administrators; only the explicitly authorized empty-repository bootstrap is exceptional |
| Required status check | Stable `build` check, bound to the GitHub App ID observed on the actual run |
| Up-to-date branches | Required before merge |
| PR conversations | All resolved before merge |
| Review count | Zero separate approvals for solo-maintainer repos; retain stronger existing requirements or require independent review when available |
| Stale approvals | Dismiss when new commits are pushed |
| Admin enforcement | Enabled; no bot/admin bypass actors |
| Force pushes / deleting `main` | Both blocked |
| History | Linear; squash merges enabled, merge commits/rebase merges disabled unless a stronger established policy says otherwise |
| Merged feature branches | Automatically deleted |
| Actions default token | Read-only; Actions cannot create or approve PRs |
| PR CI | Runs without production secrets or deployment permissions |
| Production deployment | Trusted `main` only; environment permits only `main` |
| Pages build source | GitHub Actions for Pages projects |
| Public site URL | Prominent clickable link immediately below the README title |
| Local Git metadata | Exact approved author and committer; UTC timestamps |
| Local privacy hooks | Installed, executable, active, and excluded from tracked source |

For an empty repository, audit/push the authorized bootstrap, observe its real
`build` check and App ID, then establish protection promptly. Every subsequent
change uses a PR, even a one-line README change. Do not temporarily remove
protection or use an administrator bypass because a change is small or CI fails.
Do not "test" protection by trying a real forbidden push.

Read back branch protection/rulesets, merge settings, Actions defaults and deployment
environment policies through `gh`. A successful API request alone is not verification
of every intended setting. Check that the required job actually runs on PRs and does
not remain pending due to conditional/path filtering. Use a real authorized PR to
verify that checks are enforced; never fabricate a status or approve your own work.
Include completed server-setting checks and any exceptions in the delivery report.

## Local-first application defaults

Privacy is a product requirement. Default to no telemetry, analytics, remote logging,
cloud processing, accounts, sync, external fonts or runtime CDN dependencies. Do not
send user content to services without explicit product authorization. Audit library
network activity and logging, and document actual data flows rather than unsupported
privacy claims. Bundle required workers, fonts, models and WASM assets locally when
an offline/local-only product is requested. Evaluate licensing and maintenance.

Prefer in-memory processing. Add persistence deliberately, with clear consent for
sensitive documents. Treat IndexedDB, localStorage, service-worker caches and offline
queues as retained data. Document what is stored, retention/expiry, deletion, quota
failures and recovery. Do not silently introduce alternative storage behavior.

Scope storage and caches by **app ID + deployment base + feature + data version**.
Use explicit migrations/deletion plans. Never clear all origin storage/caches or
unregister unrelated service workers. Namespaces prevent collisions, not same-origin
access; separate origins are necessary for security isolation. Do not promise that
browser storage is encrypted, durable or a backup. Cache only approved public app
assets; keep user documents, authenticated responses and APIs out of shell caches.

## Reusing the PWA foundation

For a new static/offline web app, inspect the local `pwa-base-layer` project under
`~/git/` and read its `AGENTS.md`, README, `docs/REUSE.md`, `docs/STORAGE.md` and
`docs/REPOSITORY_SETUP.md`. Reuse appropriate tracked source/assets as a foundation;
reconcile destination files rather than overwriting existing work.

Do not copy `.git`, local hooks, `.env*`, secrets, dependencies, `dist`, browser traces
or test artifacts. Give the product a unique non-personal app ID, package name,
branding and icons. Replace demo product behavior and storage namespaces. Preserve
license notices. The base is copied source, not a runtime network dependency.

Prefer React, strict TypeScript for product code, Vite, locally compiled Tailwind
and reusable UI components. Separate reusable browser/storage code from product UI.
Use the repository's Node version and npm lockfile. Install a suitable Node runtime
locally if needed; do not change unrelated system configuration or pretend an
unsupported runtime was tested.

Preserve responsive layouts, keyboard access, light/dark themes, reduced-motion
support, safe-area spacing, Android installation, iOS home-screen guidance, Apple
metadata, touch icons and standalone launch. Avoid unsupported capabilities and
placeholder controls that look functional. Explain technical limitations honestly.

## CI/CD and GitHub Pages

When static hosting/publication is requested:

1. Use a static architecture; configure manifest URLs, asset URLs, worker scope and
   storage scope from one validated base path. Repository Pages normally uses
   `/REPOSITORY/`; custom-domain sites normally use `/`. Do not hardcode a machine path.
2. Commit reproducible dependency locks and scripts for generated public assets.
   Pin third-party Actions to verified full commit SHAs. Use finite job timeouts,
   read-only checkout credentials, concurrency controls and minimal permissions.
3. Run lint, type checking, meaningful unit tests, production build and browser
   workflow tests on PRs. Keep a stable required `build` job. Do not skip mandatory
   checks using path filters. Test a non-root deployment path and offline reload.
4. Build PRs with read-only permissions, no production secrets and no deployment.
   Never use `pull_request_target` to execute untrusted PR code. Deploy only trusted
   `main`, with Pages/OIDC write permissions confined to the deployment job.
5. Configure GitHub Pages through the API/UI to build from GitHub Actions. Confirm
   the deployment environment permits only the intended production branch. A YAML
   workflow alone does not configure hosting or protections.
6. Push only within the owner's authorization, wait for **remote** checks, inspect
   failures, fix them through the appropriate branch/PR flow and finish deployment.
   A passing local build does not prove GitHub Actions or the live site works.
7. Put a prominent **Live site** / **GitHub Pages** Markdown link immediately below
   the README title, before badges, descriptions or setup instructions. Use the
   verified deployment URL, update it if hosting changes, and clearly label it
   pending until its deployment is live. Do not bury it in the deployment section.
8. Verify the actual deployed site, manifest, worker scope, assets and an offline
   reload/recovery in a clean browser context. Use synthetic data. Do not describe
   browser emulation as real Android/iOS installation testing.

## Completion report

State the concrete result, relevant tests, commit/PR and live URL when published,
and remaining material limitations or manual checks. Report identity and protection
verification without exposing private configuration. Do not call a site deployed
until its deployment succeeds and its public URL has been checked. Do not end at a
plan when implementation and delivery were requested and are authorized.
