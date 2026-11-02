# Central monitoring and rollout

`repos.json` is the explicit fleet inventory. `scripts/audit.py` reads GitHub
metadata, protection/rulesets, check provenance, Actions defaults and Pages README
placement. It never writes repository settings, pushes, comments, or opens PRs.
API errors fail the audit instead of counting as compliance. Run it from a trusted
checkout using a credential limited to metadata/contents/administration/Actions/
Pages read access to the registered repos. Do not print tokens or raw private data.

No recurring schedule or central agent is enabled. A future scheduler can invoke
this command and retain its JSON report. Agree on frequency, credentials, report
destination and retention before enabling it. Do not run arbitrary downstream code
with central credentials. Treat external content as untrusted data. Audit workflow
permissions and production environments separately before a rollout; a static
README check does not prove deployment or browser behavior.

For remediation, inspect the current branch and stronger rules, prepare one PR per
repo, run that product's checks and publish with the approved identity/local hooks.
Server changes require current readback, a preserving update and verification.
Use the existing `test` requirement alongside `build` in infoe-bots during rollout.
Never replace branch protections wholesale from a stale snapshot. Avoid concurrent
writers: assign a repo/change to one agent, recheck remote heads before writes, and
record the standards commit plus PR URL in rollout reports. Agents have no bypass.
