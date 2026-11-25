# Continue Eden Comms

## Latest checkpoint — automatic private internal signing verified

PRs #172 and #173 merged. Exact source 46a372e782212e70fc50f9e7038f2dbdcb3f62fe passed independent Android CI (run 45529175761) and automatic owner-main private signing (run 45529175721). All 412 Python tests passed. Private internal package com.edenpractical.comms, version 10001 / 0.2.12-internal-10001, certificate SHA-256 dad2159585f8bc804c47de056bf8a2c2f546ad25893cb64e0448eb0cf8676d06, APK SHA-256 5c32d58369f4a473c999f0e094d04d703dfbb188ca1f71fb8bf68eb46484aed3. [Signed artifact](https://github.com/EdenP-Development/Eden-Comms/actions/runs/45529175721/artifacts/14983613375). Central registry updated. Two organization secrets reported configured by owner; real signing verified, independent backup recovery and physical upgrade unverified. No manual dispatch needed for owner main pushes. Public Preview stays separate. Production release flags remain false. Next: consolidate integrated feature/UI acceptance and prepare the single two-phone test matrix; avoid speculative micro-patches. Issue #27 remains open pending second compatible build and physical preservation. Older original-package disposable debug installs may be incompatible; do not uninstall without informed consent.

**Latest verified technical receipt:** [EdenP post-transfer build/signing record](docs/EDENP_POST_TRANSFER_VERIFICATION_2026_11_24.md)
— migrated repo `EdenP-Development/Eden-Comms`, current main
`a0952f602fa8482ecdc84a8220d4f5a7673f64f5`,
org Android CI **SUCCESS**, org-hosted public-key Preview **200016**
built with unchanged signing certificate. Private original-package
signing and actual two-phone acceptance **UNVERIFIED**. Visual issue
[#167](https://github.com/EdenP-Development/Eden-Comms/issues/167)
is the next owner-led QA checkpoint.

**EdenP Development organization transfer verified November 24, 2026.**
Current canonical repository: [EdenP-Development/Eden-Comms](https://github.com/EdenP-Development/Eden-Comms).
The same GitHub repository ID, 162 historical branches, issues and main
source history were preserved. [Transfer evidence and signing boundaries](docs/EDENP_DEVELOPMENT_INTEGRATION_2026_11_24.md).
Shared standards: https://github.com/EdenP-Development/Eden-Development-Standards.
Do not mistake public-test Preview signing for private production signing.

**Canonical source:** `main` of `EdenP-Development/Eden-Comms`. Read this page before
coding in a new chat; use live GitHub commit and CI state, not the last chat's
claims or a local temporary workspace.

**Before coding or changing product direction:** read the
[consolidated Product & Design Bible](docs/EDEN_COMMS_DESIGN_BIBLE.md)
and [full repository quality audit](docs/OVERALL_QUALITY_AUDIT_2026_11_10.md).
The Bible is a working UX/product reference; the Privacy and Security
Charter is still normative and cannot be overridden by styling decisions.

1. [Current handoff](docs/CURRENT_HANDOFF.md) — what is really integrated,
   blocked, deferred and the **next** task.
2. [Current work log](docs/WORK_LOG.md) — chronological **who/what/where/why**,
   exact PR/commit, tests, failures, rollback and the next action.
3. [Full core delivery roadmap](docs/FULL_FUNCTION_DEVELOPMENT_TEST_ROADMAP_2026_11_07.md)
   and [product decisions](docs/DECISIONS.md).
4. [Security/privacy contract](docs/PRIVACY_SECURITY_CHARTER.md),
   [local retention policy](docs/DATA_RETENTION_AND_EXPIRY.md),
   [peer trust policy](docs/TRUST_RETENTION_AND_HELP_PLAN.md).
5. [GitHub Actions](https://github.com/EdenP-Development/Eden-Comms/actions)
   and [pull requests](https://github.com/EdenP-Development/Eden-Comms/pulls).

## Development operating agreement

The owner's current instruction is **implement the useful core functions in
source, run CI after meaningful passes, and do ONE consolidated real-phone
test later**. Do not create a stream of Preview APK teasers or repeatedly
request a two-phone test. Use a focused branch/PR, preserve release guards,
and merge only after the exact final head SHA passes Android CI.

Keep three separate statuses for every transport: **source integrated**,
**automated checks passed**, **physical and independent security acceptance**.
These are never interchangeable. Release `CAN_CONNECT`, `CAN_SEND_MESSAGES`
and `CAN_TRANSMIT_VOICE` remain **false**. The app must not be described as
a production encrypted messenger or suitable for secrets/emergencies yet.

Every sizable PR updates the **current handoff** and appends one concise
**work log entry** documenting intent, decisions, files, test evidence,
remaining gaps, and rollback. Don't duplicate a full history in the README.
Preserve source/QA receipts in GitHub for future chat continuity.

Inspired by the owner’s `SudokuTogether/CONTINUE_HERE.md` and
`GridMates-Word-Search/docs/START_HERE.md` workflow; no game runtime,
keys, assets or unrelated code is copied.
