# Eden Comms — EdenP Development integration preflight and handoff

**Verified November 24, 2026.** This is a live repository inventory and a
post-transfer checklist, **not** a declaration that migration or signing
verification has already succeeded.

**Current verification superseding the initial preflight:**
[Signed org-hosted Android and app-identity receipts](EDENP_POST_TRANSFER_VERIFICATION_2026_11_24.md).
This original pre-transfer inventory is retained for history.
Actual organizational transfer, exact PR/main Android checks, and
public-test Preview signing have been verified; private original-key
secrets and the physical two-phone matrix remain unverified.

## November 24 follow-up — actual transfer VERIFIED

**Current, authoritative repository:** [EdenP-Development/Eden-Comms](https://github.com/EdenP-Development/Eden-Comms).
The owner completed the transfer. Live GitHub returned immutable repo ID
`1445090231`, the preserved `main` SHA
`fb495a27ad2150a16c2aa17671ff55c21bfe6b2c`, **162** existing
branches across two pages, zero open PRs on entry, and all **10**
open issues including [#167](https://github.com/EdenP-Development/Eden-Comms/issues/167).
Read/write/admin permissions were verified on the transferred repo by
a successful branch creation and commit.

The detailed pre-transfer inventory **below remains historical evidence**,
not current ownership instructions. A post-transfer integration PR now
updates exact owner checks (two Preview jobs, manually signed
`internal-test` and manual emulator), the existing local signing-helper
repository target and their Python security regression tests. It retains
the actual signing actor `PlayerEden`, `main`-only restrictions, protected
environment and pinned public Preview signer. Active README, design bible,
handoff, Preview guide and signing docs point to the org repo.

**Verification gates at this checkpoint:** exact PR-head Android/JVM/Python
and post-merge main CI pending; *new org-hosted Preview APK* pending;
protected original-package private signer and restricted org secret
availability **UNVERIFIED**; 18×3 physical two-phone matrix and independent
security review **NOT RUN**. No app IDs, secrets, signer identities,
hardware features, assets or Design Bible policies have been replaced.

After successful CI, update this note with exact run IDs and modify
only Eden Comms's entry in the [live central registry](https://github.com/EdenP-Development/Eden-Development-Standards/blob/main/APP_REGISTRY.json).
Other projects' records may change concurrently. Next substantive UI
work remains issue #167.

## Organization and repository

- **Current owner:** `PlayerEden`; current repo:
  [PlayerEden/Eden-Comms](https://github.com/PlayerEden/Eden-Comms).
  **Stable GitHub repository ID:** `1445090231`.
- **Target owner/repository:** `EdenP-Development/Eden-Comms`.
  That target repo **does not yet exist** as of this preflight.
- **Owner-only action:** in
  [repository settings](https://github.com/PlayerEden/Eden-Comms/settings)
  → General → Danger Zone → Transfer ownership, select
  `EdenP-Development`. Preserve the name `Eden-Comms`.
- GitHub connector currently verified **read/write/admin** on the old
  repository and the shared standards hub; **post-transfer access is
  not yet verified**. Do not use old-owner redirects as proof of new-owner
  permission.
- Default branch: `main` at preflight
  `2a19e91f2af15a788920c032bc1eba4e9fbdc2e4`.
  **161 branches** appeared on the first two pages (most are historical
  milestone branches), **0 open PRs**, **10 open issues**, including
  [#167](https://github.com/PlayerEden/Eden-Comms/issues/167) on
  scroll cue overlap / landscape Voice navigation. Do **not** delete or
  recreate historical branches, GitHub issues, PRs, milestones, comments,
  repo history or app design resources merely to standardize.
- There are **no recorded GitHub Releases** for this repo. No verified
  itch.io publication; public owner-testing has been via sideloadable
  Preview development APKs.

## Shared standards — verified live source

The canonical headquarters is
[EdenP-Development/Eden-Development-Standards](https://github.com/EdenP-Development/Eden-Development-Standards).
Read README, APP_REGISTRY.json, ORGANIZATION_TRANSITION,
SIGNING_KEY_MANAGEMENT, RELEASE_POLICY, SAVE_PRESERVATION,
DISASTER_RECOVERY, RELEASE_CHECKLIST and the three `templates/`
references before future release or signing changes. These establish
incremental migration, protected secrets, rollback, backups, accepted
identities, and no automatic publication.

The shared `APP_REGISTRY.json` was updated November 24 with the
**verified public-only Eden Comms inventory** at the *old owner* path;
no other apps' entries were intentionally modified. On real transfer,
re-read the **latest** registry and update only Eden Comms's
`repository`, `migration`, URLs and verified statuses using current
file SHA; protect concurrent updates by other development chats.

## Android channels — preserve and distinguish

| Channel | Package ID | Signer / update status | Version |
|---|---|---|---|
| Public-key test **Preview**, sideload-only | `com.edenpractical.comms.preview` | Public AOSP test certificate SHA-256 `a40da80a59d170caa950cf15c18c454d47a39b26989d8b640ecd745ba71bf5dc`; a PUBLIC test key, **not** private beta or production signing | Last built `0.2.12-preview-200014`, code `200014` |
| Ordinary ephemeral debug APK | `com.edenpractical.comms` | Android CI disposable debug signing; **no presumed install-over continuity** | Source baseline `0.2.12-approval-review-only`, code `11` |
| Dedicated signed **internal-test** (not activated/verified) | `com.edenpractical.comms` | Existing protected manual workflow, five referenced `EC_INTERNAL_*` credentials; actual availability/original certificate unknown; do not assume original-installed compatibility | Would allocate `10000 + run_number` |
| Production (not shipped) | `com.edenpractical.comms` | No accepted release signer/identity evidence | All release communication capabilities remain **FALSE** |

**Last verified Preview:** [CI build job success, 200014](https://github.com/PlayerEden/Eden-Comms/actions/runs/42969199330),
source `2a19e91f2af15a788920c032bc1eba4e9fbdc2e4`,
APK SHA-256
`d8ed947ee0c79904014e40ede3ee04e4ab1803af4c95ffabd3c012f93e1ca7f8`.
CI verified exact certificate and source via `aapt`/`apksigner`.
The same-run **emulator job failed at the final landscape Voice tile
assertion after capturing 13 real disconnected-screen PNGs**; do not
label the overall Preview workflow green. Actions artifact retention
is short; artifact unavailability after expiry is **not** key loss.

**Never** replace this public Preview signer with Sudoku's private
beta signer; never move the original `com.edenpractical.comms` APK to
the public test signer or replace an unknown original internal key.
Two original-package APKs with different certificates are not
compatible updates. Do not tell a tester to uninstall to solve a
signature mismatch; that can erase device identity/local settings.

## Signing setup / custody after transfer

Existing manual internal-test workflow:
`.github/workflows/android-internal-test-apk.yml`,
`environment: internal-test`, only `workflow_dispatch` on `main`,
guarded by original owner repo + `GITHUB_ACTOR=PlayerEden`.

It references five **credential names only**:
`EC_INTERNAL_KEYSTORE_BASE64`,
`EC_INTERNAL_KEYSTORE_PASSWORD`,
`EC_INTERNAL_KEY_ALIAS`,
`EC_INTERNAL_KEY_PASSWORD`,
`EC_INTERNAL_CERT_SHA256`.
**No successful original-key preflight has been found or verified.**
The public registry may list these non-secret names but cannot claim
that they exist, can be read, or match a certificate.

After ownership transfer, inspect the target repo's Actions settings
and `internal-test` environment. Prefer existing original private
material, if any, and verify its public certificate before choosing
new credentials. If owner later chooses a **new** persistent internal
QA channel, keep its key separate from both public Preview and future
production. Use org-level Actions secrets restricted to
`EdenP-Development/Eden-Comms`, with the existing private-key workflow
and public fingerprint pin. Never display or commit private keystores,
passphrases, or backup locations. Have the owner privately maintain two
recoverable encrypted copies. Org secret availability alone does not
establish custody or successful signing.

**Do not dispatch or claim verified protected signing until** source
guards, org secret permissions, actual cert pin, package/version and
signed APK have all passed. User action is required only for transfer,
private credential entry, and physical acceptance/creative review.

## GitHub Actions — five existing workflows

1. `android-debug.yml`: main/PR debug Android/Gradle/JVM/Python
   checks, disposable signer smoke test, APK/privacy evidence.
2. `offline-preview-apk.yml`: main/manual, separate publicly
   test-signed Preview and **same APK** Android emulator visual QA.
3. `android-internal-test-apk.yml`: manual protected original-package
   private-signing path, currently unverified.
4. `m4-ui07-manual-emulator.yml`: manual emulator inspection.
5. `manage-qa-artifact-storage.yml`: opt-in artifact housekeeping;
   test retention should not remove accepted release backups.

**Transfer blockers in source:** `offline-preview-apk.yml` checks
`github.repository == 'PlayerEden/Eden-Comms'` in two jobs;
`android-internal-test-apk.yml` checks old `GITHUB_REPOSITORY`
and `GITHUB_ACTOR`; `m4-ui07-manual-emulator.yml` checks old
`GITHUB_REPOSITORY`. Associated Python guard tests assert the old
owner string (including
`scripts/tests/test_m4_ui07_manual_emulator.py`).
These checks must be updated **after** the transfer together with
their security tests; do not remove repo, main, protected environment
or user/signer guards just to make the workflow green.

## Post-transfer technical sequence — no feature restart

1. Verify `EdenP-Development/Eden-Comms` exists and **repository ID
   remains `1445090231`**; verify `main` history SHA and
   current branch count, all issues including #167, PR history and
   branch/issue continuity, and GitHub connector **read/write**.
2. On a short branch, update the hardcoded exact-owner guards in the
   three protected/preview/emulator workflows and related Python
   assertions. Retain protected environment, main-only/manual-only
   restrictions, least-privilege permissions and preview key pin.
   Update only **current** docs/links: `README.md`,
   `CONTINUE_HERE.md`, `docs/CURRENT_HANDOFF.md`,
   `docs/TEST_BUILD_QUICKSTART.md`, signing guide and Design Bible
   if owner path occurs. Leave dated historical PR/audit notes for
   provenance, with a new dated migration note instead.
3. Exact PR-head Android/JVM/Python/security CI green, merge safely,
   independent merged-main green. **Actually trigger/verify the real
   Preview workflow** from org main, collect version/package/signer
   and valid artifact. Verify emulator screenshots separately; do
   not confuse their failure with a bad APK package.
4. Check org-scoped restricted secret availability **without printing
   values**. Do not generate or replace a private original-package
   signer until key custody is understood. If available, owner
   manually dispatches protected `internal-test` job on main and
   the result must match original pinned certificate. If not,
   document pending, not failed compatibility.
5. Re-read live shared registry and update this project's source,
   owner, CI, confirmed signer/QA statuses **without overwriting**
   GridMates, Sector Rebound or other app records. Update this
   document, current handoff and work log with exact receipts.
6. Resume the existing roadmap at
   [issue #167](https://github.com/PlayerEden/Eden-Comms/issues/167):
   Home scroll cue overlaps Connect on landscape/compact and visual
   harness cannot find Voice/PTT in landscape. Fix observed UX,
   rerun real screenshots, then complete **one consolidated two-phone
   LAN/Bluetooth/Wi-Fi Direct text/ACK/PTT matrix** and independent
   security/storage review before any production unlock.

## Product assets, design and release boundaries

- [Design Bible](EDEN_COMMS_DESIGN_BIBLE.md):
  grounded graphite/sage, native Compose, restrained vectors,
  understandable Connect → Verify → Text/Talk → Disconnect.
  Keep this **project-specific**, not a GridMates visual skin.
- [Visual asset kit](VISUAL_ASSET_KIT_V1.md), current Android resource
  files, [decisions](DECISIONS.md), [work log](WORK_LOG.md) and
  [quality audit](OVERALL_QUALITY_AUDIT_2026_11_10.md) remain untouched.
  Asset provenance and icon continuity must survive transfer.
- Security/privacy authoritative docs:
  [charter](PRIVACY_SECURITY_CHARTER.md),
  [retention](DATA_RETENTION_AND_EXPIRY.md), and
  [two-phone matrix](TWO_PHONE_ACCEPTANCE_MATRIX.md).
  Do not replace disclosures with a generic shared privacy template.
- **No public itch.io build is verified for this app.**
  Focus on a functional and visually reviewable local testing APK;
  Google Play/legal/commercial features remain long-term.
  Do not publish, reset identities, redistribute existing signing
  material or enable release `CAN_CONNECT/CAN_SEND_MESSAGES/
  CAN_TRANSMIT_VOICE` for organizational neatness.

**Next action when the owner transfers:** verify live target repository
first; follow steps above, log exact post-transfer commits, CI and
signing claims. This audit is intentionally **transfer-pending**.
