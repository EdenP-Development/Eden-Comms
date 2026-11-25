# Eden Comms — Current development handoff

Updated: **November 24, 2026** (migration preflight; product code unchanged). This is a concise launch point, not a
substitute for GitHub's live status. On resuming, check **main SHA, open PRs
and latest green Android CI** before modifying any files.

## EC-R4 — nearby microphone permission boundary (proposed)

Beta 1 plan #178 merged at f8d086b03dfff82a4dad0dc2e04365af3b53c3f0 after CI #513 passed. Owner clarified professional software storefront preferred over itch.io; no storefront selected and no publication authorized. Source inspection found nearby voice owner's continuation checks cover authenticated session/radio, but not microphone permission at asynchronous grant and frame admission. Add explicit Android permission rechecks at request, grant, capture and PCM submission; clear pressed state on rejected grant. Keep audio receive independent of mic permission. No protocol, key or production capability changes. Source tests added; CI and physical revocation test pending. Rollback via reviewed revert. Next: assess LAN late grants and callback cleanup, then integrated QA. Charter no-ship gates remain.

## Beta 1 target — November 24, 2026

Owner has set first downloadable Android Beta 1 (probably itch.io) as the goal. See [Beta 1 release plan](BETA_1_RELEASE_PLAN.md). EC-R3 #177 merged at 5ebe39e7cff4e5acce46fca62502ca879989db20 after three stale permission assertions corrected; CI #511 and main Android CI 45536101859 and private signing 45536101963 succeeded. Next EC-R4 lifecycle/recovery audit, then EC-R5, consolidated physical matrix and independent security review. Public functional beta remains NO-SHIP until charter gates pass; debug APK is internal QA only. No public distribution authorized. Scope frozen to existing local one-to-one core; no runtime change in this planning pass.

## EC-R3 — explicit microphone permission and voice status (proposed)

EC-R2 #176 merged at 4504e9cde0d981a44a23e47b1893642508f7ac34; independent main CI 45534129525 and signing 45534129376 passed. [Internal build 10005](https://github.com/EdenP-Development/Eden-Comms/actions/runs/45534129376/artifacts/14986995638), expires December 2. EC-R3 adds explicit LAN microphone permission action and resume refresh, distinguishes tap recording from live sending, and exposes existing nearby pending-floor state to the Bluetooth/P2P status label. No change to authentication, wire formats, audio lifecycle or release flags. Nearby remote receiving state still conveyed by existing notice; dedicated receiving indicator deferred until event-lifecycle review. Source checks added; CI and physical QA pending. Rollback via reviewed revert.

## EC-R2 — composer-first LAN privacy disclosure (proposed)

EC-R1 PR #175 merged at be4237d6b98dcd4dac2c6f8c5baef4c50c317ce7 after CI #504 failed two obsolete diagnostics assertions and corrected CI #505 passed. Independent main Android CI 45533091385 and private signing 45533091311 both succeeded; [internal build 10004](https://github.com/EdenP-Development/Eden-Comms/actions/runs/45533091311/artifacts/14984539400) expires December 2. Physical interaction not verified.

This pass moves LAN optional disappearing-text and saved-history controls below the composer, collapsed by default, with current retention label visible. Hide/clear remain directly accessible; collapsing or hiding closes transient menus and history confirmation. Storage choices and existing callbacks unchanged; no authorization, protocol or production capability changes. Remember-peer placement and cross-transport voice guidance remain separate follow-up work. Source regressions added; exact-head CI pending. Rollback via reviewed revert. Physical matrix remains NOT RUN.

## EC-R1 — LAN conversation mode parity (proposed)

Source audit found LAN combines text, privacy and voice on one scrolling surface while Bluetooth/P2P have Text/Talk tabs. This pass adds session-scoped Text default and explicit Talk mode, keyboard dismissal and synchronous cancellation of pending/active microphone when returning to Text. Disconnect remains outside both modes; draft and existing retention/approval behavior remain. No protocol or release changes. Source regression added; Android CI and physical interaction pending. Rollback via revert of this focused PR. Next inspect privacy visibility and voice status parity; real phone acceptance remains deferred to consolidated matrix.

## 2026-11-24 — verified private signing and integrated QA readiness

PR #172 standardized two organization secrets; CI #496 failed two stale source assertions, corrected in #497 (412/412). PR #173 enabled automatic owner-main signing while retaining protected environment, exact repo/ref/actor, certificate pin and no PR signing secrets. Both merged; product runtime unchanged.

Two fresh automatic builds passed:
- A: 10001, source 46a372e782212e70fc50f9e7038f2dbdcb3f62fe, [signing](https://github.com/EdenP-Development/Eden-Comms/actions/runs/45529175721), [Android CI](https://github.com/EdenP-Development/Eden-Comms/actions/runs/45529175761), APK SHA-256 5c32d58369f4a473c999f0e094d04d703dfbb188ca1f71fb8bf68eb46484aed3.
- B: 10002, source 20eac5ae75cab2c89ffc290517ec014b43f20293, [signing](https://github.com/EdenP-Development/Eden-Comms/actions/runs/45529515834), [Android CI](https://github.com/EdenP-Development/Eden-Comms/actions/runs/45529515883), APK SHA-256 ff8d0f02a5a22bb78a42e7b03fe05d8de9fd5a3b250da0eb5ce41b1d331e6c52. [Artifact](https://github.com/EdenP-Development/Eden-Comms/actions/runs/45529515834/artifacts/14983823881) expires December 2.

Both package com.edenpractical.comms and certificate dad2159585f8bc804c47de056bf8a2c2f546ad25893cb64e0448eb0cf8676d06 verified by CI. Static upgrade prerequisites met; physical install-over and independent owner backup recovery NOT VERIFIED. Never uninstall old incompatible installs without consent. Issue #27 remains open. Preview separate; 200017 disconnected emulator 14 scenes passed (run 45494041287); owner visual review and real two-phone 18×3 matrix NOT RUN. Release flags remain false; no independent security approval.

Next: integrated acceptance preparation, then prioritize observed failures rather than speculative feature micro-patches. Preserve design Bible and privacy charter. Rollback: revert focused QA/documentation changes via reviewed PR; never rotate signer for build failures.

## Historical checkpoint — superseded by the receipt above

- Canonical `EdenP-Development/Eden-Comms`, repository ID `1445090231`,
  main `a0952f602fa8482ecdc84a8220d4f5a7673f64f5`.
- [Post-transfer migration PR #169](https://github.com/EdenP-Development/Eden-Comms/pull/169)
  merged with [org main Android CI SUCCESS](https://github.com/EdenP-Development/Eden-Comms/actions/runs/45490751352).
- [Home scroll overlap fix PR #170](https://github.com/EdenP-Development/Eden-Comms/pull/170)
  merged with [independent main CI SUCCESS](https://github.com/EdenP-Development/Eden-Comms/actions/runs/45492143260).
  It uses a measured footer instead of obscuring Connect/Text with a
  floating scroll button.
- [Preview 200016 signed artifact](https://github.com/EdenP-Development/Eden-Comms/actions/runs/45492143156/artifacts/14965554625)
  was built from that exact SHA, certificate `a40da80a59d170caa950cf15c18c454d47a39b26989d8b640ecd745ba71bf5dc`.
  Real emulator visual job **FAILED** at the final landscape Voice/PTT lookup despite capturing 13 real PNGs. The new screenshot confirms the scroll hint no longer obscures Connect; the test swipe instead started inside the footer at 78% of the 720px screen. The emulator driver is being corrected to drag from 64% within actual scroll content; new source QA plus real replay required before any visual PASS.
- [Full migration, app identity and QA receipt](EDENP_POST_TRANSFER_VERIFICATION_2026_11_24.md).
  Only the **public-test Preview** signer has verified continuity.
  Original-package protected internal signer/org secret availability
  and physical update remain unverified. Preserve all existing
  IDs/keys, keep release communication flags disabled.

## Historical Home visual issue #167 investigation

Post-transfer CI produced a verified signed org-hosted Preview 200015
with the unchanged public AOSP certificate. The **separate** emulator
visual QA job must establish whether the existing Home scroll overlay
and landscape Voice/PTT issue is reproducible. A focused Compose fix
has been submitted: the Home scroll cue moves into a reserved footer
below the weighted scrolling viewport, never over the Connect button
or cards. Run PR-head CI and an actual fresh signed Preview/emulator
inspection before claiming the updated UI is visually accepted.
Production communication remains disabled and physical two-phone
acceptance NOT RUN.

## EdenP Development post-transfer state — November 24, 2026

- **Ownership VERIFIED:** `EdenP-Development/Eden-Comms`,
  same immutable GitHub repository ID `1445090231`, original
  `main` source `fb495a27ad2150a16c2aa17671ff55c21bfe6b2c`
  before workflow repairs, 162 branches, all 10 open issues,
  zero open PRs at verification. GitHub connector read/write
  confirmed by creation of the post-transfer integration branch.
- **Workflows updated in integration PR (pending exact CI):**
  Preview both org-only job guards, internal-test exact repo check,
  manually dispatched emulator guard, and corresponding Python
  source contracts. The only authorized signing actor remains
  `PlayerEden` and environment `internal-test` / `main`
  protection stay in place. The original private signer and
  organization restricted-secret availability remain **UNVERIFIED**;
  no private keys generated/rotated.
- [Current integration details](EDENP_DEVELOPMENT_INTEGRATION_2026_11_24.md).
  Next: exact PR-head CI → merge → independent main CI →
  signed **org-hosted** Preview and real emulator evidence.
  Continue existing [issue #167](https://github.com/EdenP-Development/Eden-Comms/issues/167)
  for overlapping Home scroll cue and landscape Voice/PTT reachability
  after organizational verification. No physical two-phone or
  independent crypto acceptance yet.

## Historical pre-transfer checkpoint — November 24, 2026

The owner requested preservation-first integration into
`EdenP-Development`. On the preflight date the repository was still
`PlayerEden/Eden-Comms`, GitHub repo ID `1445090231`,
`main` at `2a19e91f2af15a788920c032bc1eba4e9fbdc2e4`.
No open PRs; existing issue/history and signing identity must be
preserved. The shared EdenP [registry](https://github.com/EdenP-Development/Eden-Development-Standards/blob/main/APP_REGISTRY.json)
has a verified **transfer-pending** non-secret Eden Comms record.

[Read the exact integration inventory and post-transfer plan](EDENP_DEVELOPMENT_INTEGRATION_2026_11_24.md).
Do not update the repository guards or claim org signing/build success
before owner transfer. The public `.preview` development signer is
verified, but original-package internal private signing remains
**unverified**. Do not replace or invent the old key; protect installed
app state. Same UI/transport roadmap, design bible, user-provided
Home screenshots and issue #167 remain the next development work.

## Product direction

Simple local-first one-to-one Android messaging and push-to-talk using
same-network Wi-Fi, Bluetooth Classic or router-free Wi-Fi Direct. No
mandatory account, backend, always-on discovery or cloud. Session-only is
the default. For any future persistent chat or peer record, obtain separate
explicit consent with **30 days maximum** and a simple local erase control.
All transport/crypto code remains unreviewed development software.

## Quality audit and unified design reference — November 10, 2026

- [Consolidated Eden Comms Product & Design Bible](EDEN_COMMS_DESIGN_BIBLE.md)
  defines the current owner-reviewable scope, everyday UX, palette and
  graded acceptance. Earlier UX-01/06/07 proposals are historical where
  they contradict the integrated debug code.
- [Full GitHub and app quality audit](OVERALL_QUALITY_AUDIT_2026_11_10.md)
  records a critical automated visual-driver failure: literal \\n text
  accidentally commented out the Preview `PACKAGE = opts.package`
  assignment, so emulator ADB launched the **ordinary** ID after
  installing the **Preview** APK. Source repair and executable
  package-binding regression are on the audit branch, awaiting CI.
- Owner-provided Home screenshots cover only first-impression UX.
  Signed Preview 200013 build and independent Android main CI passed;
  the same-run integrated emulator screenshot job **failed**. No
  successful full visual QA or three-transport physical acceptance.

## Current sources of truth

- [Delivery roadmap](FULL_FUNCTION_DEVELOPMENT_TEST_ROADMAP_2026_11_07.md)
- [Latest decisions](DECISIONS.md), [Data retention](DATA_RETENTION_AND_EXPIRY.md)
  and [Peer memory](TRUST_RETENTION_AND_HELP_PLAN.md)
- [Recent QA and decisions](WORK_LOG.md)
- [CI runs](https://github.com/EdenP-Development/Eden-Comms/actions)
- [GitHub PRs](https://github.com/EdenP-Development/Eden-Comms/pulls)

## Implemented in source and automated regression (not phone-accepted)

- Android/Compose app and in-person QR pairing.
- LAN: mutual pinned TLS and QR challenge / exporter proof, independent
  approvals, short two-way typed text and peer-app ACK; short debug live PTT
  uses the same approved channel.
- Bluetooth Classic: in-person QR/pinned TLS, bilateral consent and
  real debug TEXT/ACK on one retained RFCOMM socket (F2-Q, PR #146).
- Wi-Fi Direct: temporary Android group, bound TCP interface, checked
  three-QR exchange, same authenticated TLS/consent, debug TEXT/ACK and
  cancellation (F3-C, PR #147). The zero-data reachability probe remains
  distinct from authorization.
- Ephemeral local disappearing timer (1/5/15-minute screen display only).

**Physical device acceptance:** LAN full matrix, live Bluetooth and Wi-Fi
Direct interoperability, Android TLS providers/OEM behavior, two-way audible
PTT and accessibility tests still need the planned consolidated on-device
pass. **Independent security audit** is a separate requirement. Do not
interpret a green JVM/CI run as passing either.

## Completed source checkpoint — F5-A

[PR #148](https://github.com/EdenP-Development/Eden-Comms/pull/148) merged at
`53e581aad2c0cc30426b9674ed603d910d5c4d70`. [Post-merge Android
CI passed](https://github.com/EdenP-Development/Eden-Comms/actions/runs/42582592960).
Opt-in Keystore AES-GCM history of *actual approved LAN text events*,
stored in app `noBackupFilesDir`. Every new session defaults to RAM-only;
1h, 24h, 7d, 14d or 30d are explicit choices. Expiry filtering and
per-peer delete are separate from peer memory. Independent Android storage/
backup/security acceptance remains open; release variant is no-op.

## Completed code checkpoint — F5-B remembered public peer

[PR #149](https://github.com/EdenP-Development/Eden-Comms/pull/149) was merged as
`5364eea23914d95481625bde30590c7c2b3f93fc`.
[Main-branch CI passed](https://github.com/EdenP-Development/Eden-Comms/actions/runs/42585024948).
Separate DEBUG Keystore AES-GCM public fingerprint/expiry cache, explicit
1–30-day consent and per-peer/clear-all deletion. F5-A chat history is
separate. Records are viewed only after fresh verified LAN approval; they
never confer an automatic connection or trust. Production store remains no-op.

## Completed code checkpoint — F5-C verified nearby privacy

[PR #150](https://github.com/EdenP-Development/Eden-Comms/pull/150) merged into
`main` at `9f69de394069fa8ac1c17d5ba459bccefb808e01`.
[Post-merge CI passed 19/19 checks](https://github.com/EdenP-Development/Eden-Comms/actions/runs/42648245844).
One experimental, **debug-only** opt-in history/remember-peer UI now runs
after real approved Bluetooth Classic and Wi-Fi Direct host/join sessions.
Saved peer public fingerprints are not TLS pin authorization, and both
choices reset appropriately. No physical-device/security acceptance.

## Completed code checkpoint — F4-U Bluetooth/P2P voice bursts

[PR #151](https://github.com/EdenP-Development/Eden-Comms/pull/151) merged to
`main` as `48c94f0c9a218363a5cd95d326517332ad41735e`.
[Independent post-merge CI passed 19/19](https://github.com/EdenP-Development/Eden-Comms/actions/runs/42653580697).
The previous DEBUG Bluetooth Classic and Wi-Fi Direct host/join voice option
was a three-second **record-then-send** encrypted voice burst (not real-time).
No physical radio/voice acceptance or cryptographic review.

## Completed code checkpoint — F4-V authenticated live nearby voice

[PR #152](https://github.com/EdenP-Development/Eden-Comms/pull/152)
merged as `ad821579dd5f03d770f9df96e9dac1683bf8ab79`.
[Post-merge CI SUCCESS 19/19](https://github.com/EdenP-Development/Eden-Comms/actions/runs/42658640505).
Bluetooth Classic and Wi-Fi Direct host/join reuse LAN's actual
host-arbitrated encrypted REQUEST/GRANT/DENY/CANCEL/RELEASE floor;
Android foreground mic sends 16kHz mono PCM 20ms frames WHILE held
(max 3s) over the same QR/pinned TLS/dual-approved channel, streaming
to remote AudioTrack. No verified physical radio/OEM behavior or
independent security review; debug only. Previous F4-U whole-clip path
is a regression-only fallback and also requires floor.

## Completed code checkpoint — M6-A unified Connect → Text/Talk

[PR #153](https://github.com/EdenP-Development/Eden-Comms/pull/153)
merged to `main` at `b9166cdc4f2809146c5aeeb8eac4f34397a860a7`.
[Independent postmerge CI passed](https://github.com/EdenP-Development/Eden-Comms/actions/runs/42663929342).
One debug Connect chooser routes to already authenticated Same Wi-Fi LAN,
Bluetooth Classic and Wi-Fi Direct entrypoints. Existing nearby verified
sessions show the shared **Text/Talk/Disconnect** shell and optional
privacy under a disclosure; low-level diagnostics moved to Advanced.
Choosing a radio never authorizes or verifies it, and production switches
are still FALSE. Physical two-phone UX and real OEM/security acceptance OPEN.

## Completed code checkpoint — M6-B tab safety and QA evidence

[PR #154](https://github.com/EdenP-Development/Eden-Comms/pull/154) merged to
`main` as `3d0e2d6e050d7617079fd1929c85da227e6dea9c`.
[Independent main CI passed 19/19](https://github.com/EdenP-Development/Eden-Comms/actions/runs/42669197572).
Nearby Bluetooth and Wi-Fi Direct verified sessions now cancel pending mic floor
or release active AudioRecord when switching Talk → Text or unmounting Talk.
Optional Advanced RAM-only local counters for text, ACK, floor and voice are
copyable with an explicit user tap but retain NO text/audio/peer data.
[18-case x 3-method phone test matrix](TWO_PHONE_ACCEPTANCE_MATRIX.md) is
ready but **NOT RUN** on physical devices.

## Completed source checkpoint — M6-C accessible verified conversation

[PR #155](https://github.com/EdenP-Development/Eden-Comms/pull/155) merged to
`main` at `9c158b1e9dfea6b82350069cb7cd842956cebd9c`.
[Final PR CI passed](https://github.com/EdenP-Development/Eden-Comms/actions/runs/42691177877);
[independent main CI passed](https://github.com/EdenP-Development/Eden-Comms/actions/runs/42691600680).
Verified Bluetooth/P2P Text buttons now consistently stop pending/active
voice before switching from Talk; angular chat cards, screen-reader semantics
and live mic permission refresh are present. Home, Help, Settings and
Privacy & data now truthfully describe three experimental transports, opt-in
local text history and separate peer memory. No emulator/TalkBack/device
acceptance or independent security audit. Production CAN_* remain FALSE.
[Detailed audit](M6_C_USABILITY_ACCESSIBILITY_AUDIT.md).

## Completed source checkpoint — M6-D guided nearby QR setup

[PR #156](https://github.com/EdenP-Development/Eden-Comms/pull/156)
merged to main as `475756467698407848429def12c0ab6fd04145d3`.
[Final PR Android CI passed](https://github.com/EdenP-Development/Eden-Comms/actions/runs/42692297197)
and [independent main CI passed](https://github.com/EdenP-Development/Eden-Comms/actions/runs/42692721109).
Bluetooth's two QR stages and Wi-Fi Direct's three QR stages now
show accurate host/join next actions, accessible status/heading semantics
and a clear NOT YET VERIFIED boundary. No actual phone visual/TalkBack
or two-device acceptance took place. See
[M6-D audit](M6_D_QR_PAIRING_GUIDANCE_AUDIT.md).

## Completed source checkpoint — M6-E text and peer-app ACK clarity

[PR #157](https://github.com/EdenP-Development/Eden-Comms/pull/157) merged
as `6dc2070692a7143c3e76e35599a16ec44a01580d`.
[Exact-final-head PR Android/JVM/Python/security CI SUCCESS](https://github.com/EdenP-Development/Eden-Comms/actions/runs/42696448115);
[independent `main` CI SUCCESS](https://github.com/EdenP-Development/Eden-Comms/actions/runs/42696732161).
Both Bluetooth and Wi-Fi Direct verified debug text use the same
280-Unicode-codepoint draft gate (no UTF-16 truncation), bounded
scrolling and Jump to latest. Queue acceptance, local TLS write,
peer-app ACK and local receive are displayed separately. Failed local
queue attempts preserve the draft and report failure. No emulator,
TalkBack, actual two-phone or independent crypto acceptance.
[M6-E source audit](M6_E_TEXT_COMPOSER_ACK_RECOVERY_AUDIT.md).

## Completed source checkpoint — M6-F keyboard/privacy recovery

[PR #158](https://github.com/EdenP-Development/Eden-Comms/pull/158) merged as
`ef155509e55125be11eef7e75c864c39594d29c6`.
[Exact PR-head Android/JVM/Python/security CI SUCCESS](https://github.com/EdenP-Development/Eden-Comms/actions/runs/42702688134);
[independent merged-main CI SUCCESS](https://github.com/EdenP-Development/Eden-Comms/actions/runs/42702975134).
All three actual Bluetooth/P2P debug conversation pages gained
keyboard/system-bar insets and debug-only `adjustResize`, the shared
verified shell hides keyboard/focus before Talk or Disconnect,
Bluetooth QR/chat requests best-effort screenshot protection,
and stale Bluetooth queue feedback clears on STOPPED/Ready.
No actual Android emulator/phone/TalkBack/privacy or crypto acceptance.
[M6-F source audit](M6_F_NEARBY_IME_CAPTURE_RECOVERY_AUDIT.md).

## Completed source checkpoint — M6-G observed failure recovery

[PR #159](https://github.com/EdenP-Development/Eden-Comms/pull/159)
merged as `bca8156d53806e0deb1d98b68770d198d22d3200`.
[Exact PR-head Android/JVM/Python/security CI SUCCESS](https://github.com/EdenP-Development/Eden-Comms/actions/runs/42705244355);
[independent merged-main CI SUCCESS](https://github.com/EdenP-Development/Eden-Comms/actions/runs/42705668476).
Debug Bluetooth/P2P observed STOPPED, radio, and group-cleanup
states now show separate, concrete instructions without auto-retry.
Fresh explicitly started Wi-Fi Direct host/discovery clears stale
RAM chat/queue/ACK and remains unverified until actual approved
channel Ready. Physical QA/TalkBack, OEM cleanup and external crypto
review still NOT RUN.
[M6-G audit](M6_G_RECOVERY_GUIDANCE_AND_STATE_RESET_AUDIT.md).

## Completed source checkpoint — M6-H one-use P2P three-QR request

[PR #160](https://github.com/EdenP-Development/Eden-Comms/pull/160)
merged as `cbbd61b95e1431392ff435bd182aa8b8324a675d`.
[Exact-final-head PR Android/JVM/Python/security CI SUCCESS](https://github.com/EdenP-Development/Eden-Comms/actions/runs/42707312560);
[independent merged-main CI SUCCESS](https://github.com/EdenP-Development/Eden-Comms/actions/runs/42707691367).
The Wi-Fi Direct QR coordinator now atomically claims a
**single actual constructed pinned TLS request** per successful
three-QR exchange. Duplicates are closed; only the existing
explicit fresh QR exchange resets the use gate. Actual
Bluetooth/P2P/LAN two-phone acceptance, microphone, real Android
error behavior, and independent crypto/privacy review NOT RUN.
[M6-H source audit](M6_H_SINGLE_USE_WIFI_DIRECT_QR_REQUEST_AUDIT.md).

## Completed source checkpoint — M6-I interruption isolation

[PR #161](https://github.com/EdenP-Development/Eden-Comms/pull/161)
merged as `dd0366f966ffe419dda45b78631eb9cb71525725`.
[Exact-final-head PR Android/JVM/Python/security CI SUCCESS](https://github.com/EdenP-Development/Eden-Comms/actions/runs/42725506431);
[independent merged-main CI SUCCESS](https://github.com/EdenP-Development/Eden-Comms/actions/runs/42725798742).
The actual Wi-Fi Direct Join callback failure path now closes only
its original still-pending QR request if the exact radio token,
OS group phase and unpromoted TLS state still match. All six
Join Activity callbacks fence status/voice/optional privacy to
the current controller identity. Physical two-phone tests,
Android emulator and independent security acceptance NOT RUN.
[M6-I source audit](M6_I_P2P_INTERRUPTED_CALLBACK_ISOLATION_AUDIT.md).

## Active integrated application test drop — visual before micro-patches

**Owner direction:** Stop auto-chaining isolated M6 edge-case PRs.
Ship a **single installable full-function development Preview**,
inspect the real Android screens, then prioritize observed
blocking issues. Source implementation of debug LAN, Bluetooth
Classic and Wi-Fi Direct two-way TEXT/peer-app ACK + short
foreground PTT already exists; none is independently accepted
on real phones.

Branch: `feature/integrated-preview-and-emulator-visual-2026-11-09`.
Review [integrated test audit](INTEGRATED_PREVIEW_VISUAL_QA_2026_11_09.md).

- Fixed the stale emulator navigation script: current Home first
  opens a real connection-method chooser. Safe test now goes
  Home → chooser → Same-Wi-Fi idle QR (and returns twice).
  Voice/PTT also routes to chooser rather than the old
  `COMING SOON` page. Help assertion uses real current copy.
- Emulator driver can install either **exact** debug package or
  isolated `com.edenpractical.comms.preview`. Device guard
  still refuses physical devices. Never taps Show/Scan, runs
  radio discovery, creates identity, sends chat or opens mic.
- Installable Preview workflow packages its existing **real**
  public-test-key-signed Android APK and then a **second job
  downloads the exact APK from the same run** into Android 35
  emulator, exercises current UI and publishes sanitized PNGs
  + summary JSON. Merely checking a workflow into source
  does not establish screenshot success.
- Updated included START-HERE instructions for actual
  Connect → three methods → mutual approval → Text/Talk →
  Disconnect, plus honest one-phone/2-phone boundaries.
  Removed stale workflow claim Bluetooth cannot chat.

## Active owner-led visual polish — Home scroll cue (2026-11-10)

The owner has **actually installed the integrated Preview and provided
dark-theme Home screenshots**. Main screen looked good, but the lower
Settings/How it works entries were only reachable by scrolling with
no cue. The next focused source change is a minimal, accessible
viewport-bottom `↓ SCROLL FOR MORE` button on Home when and only
when further content is hidden; tap advances content, first swipe
dismisses the prompt. The rest of the app and fixed TopBar are
untouched. Build/regression and a fresh owner Preview are the only
verification target; real two-phone and independent security QA
remain deferred. Do not turn this into another transport milestone.

## Immediate acceptance priorities — quality audit handoff

1. **Fix verified visual QA break:** run the corrected Preview package
   assignment driver on the real emulator after exact PR-head CI green.
   Squash merge only green source; independently confirm merged-main CI
   and newly triggered signed Preview + actual screenshot job. The owner
   already has a valid Preview 200013 APK, but emulator PNG acceptance
   remains **FAILED / NOT CAPTURED** until observed otherwise.
2. **Owner-led visual polish:** compare real Home, three-method chooser,
   QR setup, chat/Text/Talk, Settings/Privacy, scroll cue, light/dark,
   keyboard, rotation and 200%-font on real screens. Prioritize observed
   UX defects rather than speculative radio micro-fixes.
3. **Physical and release gates remain open:** one consolidated two-phone
   matrix across LAN/Bluetooth/P2P, audited voice/ACK and failure behavior,
   independent protocol/security/storage/backup/accessibility review.
   Production `CAN_*` flags remain FALSE. No sensitive messages.
4. **Document hygiene:** use [Design Bible](EDEN_COMMS_DESIGN_BIBLE.md)
   as the current UX/scope entry and
   [quality audit](OVERALL_QUALITY_AUDIT_2026_11_10.md) as the evidence
   backlog. Old "Coming Soon" milestone documents are historical;
   update GitHub issues with actual source/CI/device review fields
   before closing them.

**Rollback:** revert only the relevant merged PR; do not reset package ID,
signing keys, stored app identity or unrelated features. For F5-A, provide
a user-visible Delete saved history before any schema change; do not claim
that a source rollback erased data already on a handset.
