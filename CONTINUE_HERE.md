# Continue Eden Comms

## EC-R6 reliability checkpoint (2026-11-25)

Visual Review 5 runtime artwork remains at 542145f0389d8b32113bb9850bee7a9daa330081 (internal 10034). PR #206 merged d0bee9788f60a7eaa64303113b02e92c0f60c1bc after CI #582; post-icon Preview run 45590660687 not yet confirmed complete. PR #207 merged 4ff686a4468d97f1707b8d4a655c6b0bd5a1b794 after CI #584; real JVM loopback accept/read cancellation and stale listener release tests passed. Main Android run 45591364629 and signing 45591364667 passed: [internal 10036](https://github.com/EdenP-Development/Eden-Comms/actions/runs/45591364667/artifacts/15011227339), APK SHA-256 11dd8964f5020b6a719671a4702b6b4235498f38831c297d6e208a8553e41fa4. PR #208 merged d6d6399462a458a0496415030c354553d6bfed2e after CI #586; partial LAN metadata loss and stalled writer forced-close tests passed. Main follow-up pending. EC-R6C branch adds Bluetooth old opened-link role/reason cross-product and Wi-Fi Direct cancelled permission outcome coverage. CI pending. No runtime changes, no physical evidence from these tests. Next EC-R7 actual message delivery audit, EC-R8 audio lifecycle, EC-R9 resource ownership and EC-R10 consolidated QA. Owner physical artwork approval, 54 physical cases, independent security review and release gates remain open. No publishing.


## Current checkpoint — Visual Review 5 and Beta 1 reliability (2026-11-25)

This checkpoint supersedes earlier visual status below. PR #205 merged at 542145f0389d8b32113bb9850bee7a9daa330081 after CI #580. Main Android run 45586732879 and private signing run 45586732727 passed. [Internal 10034](https://github.com/EdenP-Development/Eden-Comms/actions/runs/45586732727/artifacts/15008313812), expires Dec 2; APK SHA-256 7d4a3617a0f620e5849e40a269160a2d99aaac705972f17192b5b13265dbbcde. Same pinned internal signer. Central registry updated ab0f78913de1cc3b561225a95276e26026ccffac. Owner approved the original matte product icon concept and three-second skippable EPS splash; native derivative icon is merged but physical artwork acceptance remains open. Owner cannot currently upload screenshots; do not block other engineering on visual feedback.

Pre-icon integrated Preview run 45582913336 at e94265f6a587c0ec1719bca43163789347c9b7a4 passed and captured 28 screenshots (artifact 15007657884). No qualitative screenshot inspection or post-icon emulator pass claimed. Add icon resource paths to Preview trigger so subsequent icon changes get integrated checks. Next reliability work: review production boundary, stale callbacks, teardown, retries and test coverage by transport; prefer targeted fixes over feature expansion. All 54 physical cases and independent security review remain NOT RUN; no public functional beta or publication authorized. Use harmless test content only.


## Visual Review 3 owner acceptance and follow-up (2026-11-25)
Owner reviewed internal 10028 and explicitly said “The splash was perfect and skipable.” EPS artwork, nominal 3000ms and tap skip accepted; central EPS guide and BRAND_IDENTITY updated (central commit 54e1fd762a77d27a6ab093ccf3c79fceca4c50c6). This is startup-specific acceptance, not all UI or release approval. Seven screenshots show compact Home, four appearance variants, Settings and startup; remaining developer observations are lower Help row clipped at viewport, old opaque emblem, redundant history help, system bar color discontinuity. No icon replacement yet. Integrated run 45575256247 exposed actual split semantics: clickable checkable ancestor and named non-checkable child. Driver now searches contained named descendants, validates unique actual checked state, and has regression fixture; emulator retry pending. Next finish compact spacing/privacy cleanup and startup bar polish without changing accepted timing; independent security and physical communications gates remain open.

## Owner physical Visual Review 2 — 2026-11-25
Seven owner screenshots of signed candidate from 79711c005975e17f17ac0b14eda19e0a06cb00bd show Home in four palettes and Field Green Settings light/dark. Owner explicitly says splash is definitely too fast. No final visual approval. Pilot nominal 3000ms (250 fade in / 2500 hold / 250 fade out), exact same pinned publisher artwork/background, skip/reduced motion/lifecycle/offline behavior preserved. This is a proposed EPS timing revision requiring physical acceptance before central standard promotion. Screenshots also show tall stacked communication cards, partially visible Settings above large reserved scroll cue, old opaque green emblem in light theme, help text amber despite violet icon, dense privacy explanations. These are developer observations, not additional explicit owner complaints. Next compact Home with accessible horizontal stacked tiles, smaller scroll cue, consistent help accent, privacy hierarchy. Icon remains deferred; no final artwork acceptance. PR #195 locator repair merged bb81dd02bed2b249de9b328aefa2d0535380698 after CI #556; integrated emulator retry unverified. Prior candidate signing passed; no new signed APK yet. Physical two-phone/security/release gates remain open.

## VIS-07 checkpoint (2026-11-25)
VIS-06 merged at 2a862ae56a847f1c8eeb5e3692e0950909dab47b after CI #552. All first-pass Home, Settings, connection and conversation refinements are on main. Icon deferred by owner; concept C needs heavier, centered, dimensional artwork. VIS-07 expands disconnected emulator driver to four appearance combinations (Settings/Home/chooser captures), explicit dark switch state checks, and Settings/privacy reachability at 200% font. No fabricated connection, preference injection, microphone or QR activation. Static test and emulator execution pending; screenshots do not prove physical layout or security. No new APK approved. Next verify CI and integrated preview results, inspect screenshot evidence where available, repair failures, then signed internal Visual Review 2. Physical 54 cases and independent security gates remain open.

## VIS-01 — active visual refinement checkpoint (2026-11-25)

PR #187 merged at e1684a707a6269073fbf997868b45459380fcc1b; CI #534 passed. Owner screenshots from internal 10015 showed palette switching, but visual approval withheld: EPS appeared amber-only, light mode brown, old shield/attribution and tall layout need refinement. Owner selected Modular Comms concept C as icon direction only; final asset unapproved. Startup physical acceptance not established. Active branch feature/eps-vis01-color-roles adds shared supportingAccent/actionFill/actionContent roles, palette provider in main and five nearby Compose activities, violet supporting accents, gold/dark main Home action in both EPS modes, corrected EPS header attribution, selected contrast checks. Field Green palette retained; no communication authority changed. CI pending.

Cross-project references inspected: SudokuTogether main GameTheme.kt (central typography, shapes, color roles), docs/GRIDMATES_BETA12_THEME_PILOT_REVIEW_2026-11-16.md (contrast matrix and independent state tokens), docs/GRIDMATES_BETA2_OWNER_PHONE_VISUAL_FEEDBACK_2026-11-17.md (physical feedback/approval boundaries), CompactPlayLayoutTest.kt and NearbyVisualAuditTest.kt (native deterministic presentation fixtures, 200% font/landscape). Adapt techniques, not game aesthetics. For Comms, fixtures must be test-only, synthetic, incapable of granting trust or transport admission; no production demo authorization. Existing disconnected emulator QA is not physical session evidence. Other repo discovery incomplete; no claim of inspection.

Next: verify VIS-01, develop Modular Comms icon candidates and compact Home, Settings, pairing and conversation layouts; consolidate signed Visual Review 2. Preserve exact EPS publisher PNG and startup timings, app IDs/signing/local data, release flags. Physical 54-case and independent security gates remain open. No publication. See EPS_VISUAL_REFINEMENT_PLAN.md.


## Current checkpoint — EPS Visual Review 2 (2026-11-25)

Owner physically reviewed internal 10015 (source c673600b0eff13134ee6546c4ab6d742f2fff190). EPS/Field Green light and dark screens observed; visual acceptance NOT granted. Owner selected concept C, Modular Comms, as the product-icon direction, not final artwork. Preserve fixed EPS publisher startup art, existing launcher until replacement accepted, app IDs/signing/data and security gates. See docs/EPS_VISUAL_REVIEW_1_FEEDBACK.md and docs/EPS_VISUAL_REFINEMENT_PLAN.md. Next VIS-01 semantic color roles and compact Home design, VIS-02 icon candidates; consolidate visual review rather than small APK churn.

Verified baseline: PR #186 merged; CI #532, exact artwork SHA-256 d144934346d77a6e04c1475dae361fc57cb28a95d7033a799bf6e2f256548516, 426 Python checks passed. Main CI 45556205473, private signing 45556203782, disconnected Preview emulator 45556203668 all passed. [Internal 10015](https://github.com/EdenP-Development/Eden-Comms/actions/runs/45556203782/artifacts/14994963791), [Preview 200022](https://github.com/EdenP-Development/Eden-Comms/actions/runs/45556203668/artifacts/14996375061). Startup physical approval, persistence, accessibility, physical 54-case acceptance, independent security and release engineering remain open. No public release.


## Beta 1 readiness — LAN permission parity (proposed)

PR #179 merged at 86e6159465448955c036e0e2310b8217acedfc98; main Android CI 45543701081 and internal signing 45543701160 passed. [Internal artifact](https://github.com/EdenP-Development/Eden-Comms/actions/runs/45543701160/artifacts/14991150076), expires December 2. LAN branch rechecks microphone permission on both granted capture paths and at live PCM/tap burst admission, retaining the atomic cancellation gate. Updated legacy assertions and added source regressions. Exact-head CI pending. See [consolidated readiness checklist](docs/BETA_1_READINESS_CHECKLIST.md) for all engineering/product tasks, draft quick start and feedback template. Professional distribution preferred; no selection or publication yet. Physical 54-case matrix, independent security review and non-debug release engineering remain open. Next finish reliability audit and integrated quality review; no feature expansion. Rollback via reviewed revert.

## Beta 1 target — November 24, 2026

Owner has set first downloadable Android Beta 1 (probably itch.io) as the goal. See [Beta 1 release plan](docs/BETA_1_RELEASE_PLAN.md). EC-R3 #177 merged at 5ebe39e7cff4e5acce46fca62502ca879989db20 after three stale permission assertions corrected; CI #511 and main Android CI 45536101859 and private signing 45536101963 succeeded. Next EC-R4 lifecycle/recovery audit, then EC-R5, consolidated physical matrix and independent security review. Public functional beta remains NO-SHIP until charter gates pass; debug APK is internal QA only. No public distribution authorized. Scope frozen to existing local one-to-one core; no runtime change in this planning pass.

## 2026-11-24 — verified private signing and integrated QA readiness

PR #172 standardized two organization secrets; CI #496 failed two stale source assertions, corrected in #497 (412/412). PR #173 enabled automatic owner-main signing while retaining protected environment, exact repo/ref/actor, certificate pin and no PR signing secrets. Both merged; product runtime unchanged.

Two fresh automatic builds passed:
- A: 10001, source 46a372e782212e70fc50f9e7038f2dbdcb3f62fe, [signing](https://github.com/EdenP-Development/Eden-Comms/actions/runs/45529175721), [Android CI](https://github.com/EdenP-Development/Eden-Comms/actions/runs/45529175761), APK SHA-256 5c32d58369f4a473c999f0e094d04d703dfbb188ca1f71fb8bf68eb46484aed3.
- B: 10002, source 20eac5ae75cab2c89ffc290517ec014b43f20293, [signing](https://github.com/EdenP-Development/Eden-Comms/actions/runs/45529515834), [Android CI](https://github.com/EdenP-Development/Eden-Comms/actions/runs/45529515883), APK SHA-256 ff8d0f02a5a22bb78a42e7b03fe05d8de9fd5a3b250da0eb5ce41b1d331e6c52. [Artifact](https://github.com/EdenP-Development/Eden-Comms/actions/runs/45529515834/artifacts/14983823881) expires December 2.

Both package com.edenpractical.comms and certificate dad2159585f8bc804c47de056bf8a2c2f546ad25893cb64e0448eb0cf8676d06 verified by CI. Static upgrade prerequisites met; physical install-over and independent owner backup recovery NOT VERIFIED. Never uninstall old incompatible installs without consent. Issue #27 remains open. Preview separate; 200017 disconnected emulator 14 scenes passed (run 45494041287); owner visual review and real two-phone 18×3 matrix NOT RUN. Release flags remain false; no independent security approval.

Next: integrated acceptance preparation, then prioritize observed failures rather than speculative feature micro-patches. Preserve design Bible and privacy charter. Rollback: revert focused QA/documentation changes via reviewed PR; never rotate signer for build failures.

## Prior signing checkpoint

PRs #172 and #173 merged. Exact source 46a372e782212e70fc50f9e7038f2dbdcb3f62fe passed independent Android CI (run 45529175761) and automatic owner-main private signing (run 45529175721). All 412 Python tests passed. Private internal package com.edenpractical.comms, version 10001 / 0.2.12-internal-10001, certificate SHA-256 dad2159585f8bc804c47de056bf8a2c2f546ad25893cb64e0448eb0cf8676d06, APK SHA-256 5c32d58369f4a473c999f0e094d04d703dfbb188ca1f71fb8bf68eb46484aed3. [Signed artifact](https://github.com/EdenP-Development/Eden-Comms/actions/runs/45529175721/artifacts/14983613375). Central registry updated. Two organization secrets reported configured by owner; real signing verified, independent backup recovery and physical upgrade unverified. No manual dispatch needed for owner main pushes. Public Preview stays separate. Production release flags remain false. Next: consolidate integrated feature/UI acceptance and prepare the single two-phone test matrix; avoid speculative micro-patches. Issue #27 remains open pending second compatible build and physical preservation. Older original-package disposable debug installs may be incompatible; do not uninstall without informed consent.

**Historical transfer receipt:** [EdenP post-transfer build/signing record](docs/EDENP_POST_TRANSFER_VERIFICATION_2026_11_24.md)
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
