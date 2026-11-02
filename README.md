# new-repo

Shared repository standards and agent starter kit for infoe-labs.

Start with [NEW_REPO_INSTRUCTIONS.md](NEW_REPO_INSTRUCTIONS.md), then adapt the
[templates](templates/) to the product. This repository has no Pages site.

- [Contribution and PR guidelines](CONTRIBUTING.md)
- [Repository registry](repos.json)
- [Central monitoring and rollout](docs/MONITORING.md)
- [New repository checklist](templates/REPOSITORY_SETUP.md)

Run `python3 scripts/validate.py` for local validation. Run
`python3 scripts/audit.py` with authenticated GitHub CLI for a read-only fleet
report; it exits nonzero for drift or unavailable settings. No extra packages.

The registry includes only the six named repositories and this standards repo.
Add new repos through a PR. Standards are applied through reviewed downstream PRs;
updating this repository does not silently overwrite product-specific instructions.
