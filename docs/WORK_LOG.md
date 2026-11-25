# Eden Comms — rolling implementation work log

This log complements the engineering details in `docs/F*_*.md` and
GitHub PR/CI history. New chats should read its **latest entry** and the
[handoff](CURRENT_HANDOFF.md) first. Append, don't overwrite.

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

## 2026-11-24 — EdenP post-transfer integration and signed Preview evidence

**Verified, not proposed:** immutable repo ID 1445090231 under
`EdenP-Development/Eden-Comms`, preserved branches/history/issues,
PR #169 org-guard migration and
[Android main CI SUCCESS](https://github.com/EdenP-Development/Eden-Comms/actions/runs/45490751352).
Old-owner guards replaced only after the actual transfer; original
`PlayerEden` private-signing actor restriction retained.

First org-hosted [Preview 200015 signed build succeeded](https://github.com/EdenP-Development/Eden-Comms/actions/runs/45490751311)
with the original public-test certificate; its separate emulator
visual job **FAILED** at landscape Voice/PTT after real Home screenshots.
PR #170 addresses the confirmed scroll-hint overlay through a
measured footer. [Exact PR CI SUCCESS](https://github.com/EdenP-Development/Eden-Comms/actions/runs/45491690934);
[squash-merged main CI SUCCESS](https://github.com/EdenP-Development/Eden-Comms/actions/runs/45492143260).
The subsequent [Preview 200016 build succeeded](https://github.com/EdenP-Development/Eden-Comms/actions/runs/45492143156),
same certificate, exact APK SHA
`0a3e10354328aec1054c06a62c49439dcd4d3ee7846ee8da041b0ed1ee77ee39`.
Actual new emulator check **FAILED** at landscape Voice/PTT label after 13 real screenshots. Reviewing the new landscape screenshot confirmed the scroll cue NO LONGER overlays the Connect button. Its emulator driver, however, starts each swipe at 78% of viewport height, directly on the newly reserved bottom footer. A follow-on source fix moves the test swipe origin to 64% (inside scrolling content) and adds a direct mocked-ADB regression, without changing the app's connection or security code. Full visual PASS still pending.

The central [APP_REGISTRY.json](https://github.com/EdenP-Development/Eden-Development-Standards/blob/main/APP_REGISTRY.json)
was updated from live content by changing **only the Eden Comms**
entry. [Long-lived receipt](EDENP_POST_TRANSFER_VERIFICATION_2026_11_24.md)
records identities, source hashes, testing and rollback boundaries.

**No private signing credential verification** has been represented:
the `EC_INTERNAL_*` protected workflow remains owner-only,
manual/main, existing key availability unknown, no new keys
created or substituted. Physical 18×3 phone QA, actual install-over
and independent protocol/privacy/accessibility review remain open.
Next actual QA step is #167 screenshots and the consolidated
physical matrix, not a new feature scope.

## 2026-11-24 — Owner visual feedback: reserve scroll cue outside Home controls

**Observed:** [Issue #167](https://github.com/EdenP-Development/Eden-Comms/issues/167)
has actual emulator PNGs showing the olive scroll hint covering
`CONNECT NEARBY` at 1280×720 landscape and card text on
720×1280 compact portrait. The same visual run failed the
landscape Voice/PTT locator. Preserve the real scroll-discovery
feature but make it safe and unobtrusive.

**Actual Compose fix:** Within the existing constrained app viewport,
Home now uses a weighted scrollable Column and a **separate measured
footer** for `↓ SCROLL FOR MORE`. The hint is not a Box overlay:
no control can sit behind its tap target. It remains Home-only,
scroll-overflow-only, at least 48dp high, tap to scroll, and disappears
after scrolling. Test source guards were updated to prohibit
`Alignment.BottomCenter` overlay and require the reserved footer.

**QA truth:** Physical owner review, real emulator screenshot pass,
landscape Voice/PTT reachability and 18×3 device connectivity
tests remain **pending** until new actual runs. No network/crypto/
voice/storage/signing or release capability changes.

## 2026-11-24 — EdenP Development transfer confirmed, workflow migration

**Verified actual GitHub ownership:** now `EdenP-Development/Eden-Comms`;
stable repo ID `1445090231`, unchanged pre-migration `main`
`fb495a27ad2150a16c2aa17671ff55c21bfe6b2c`, 162 branches,
10 open issues including real [visual issue #167](https://github.com/EdenP-Development/Eden-Comms/issues/167),
0 open PRs before this integration. GitHub read/write/admin proven by
successful post-transfer branch and source commits.

**Real changes (post-transfer integration PR):** move two Preview
workflow `github.repository` guards, owner-restricted manual
internal-test workflow, manual emulator workflow, private signer
setup helper and its mock tests, to the **org repo path**. Keep
`PlayerEden` as the sole manual protected signing actor, keep
`internal-test` environment, exact `main`, strict original
fingerprint matching, **public AOSP Preview signer and existing
application IDs unchanged**. Add a migration-specific source
regression; update active README, Continue, Design Bible,
Current Handoff, owner Preview guide and signing documentation,
and preserve all dated milestones and assets.

**Open QA gates:** exact PR-head Android/JVM/Python/security CI,
post-merge main CI, new org-hosted signed Preview and actual
emulator checks still **pending**; private original-package
signing secrets/key custody cannot be confirmed from public data,
so no key was generated or rotated. Existing phone install-over,
real two-phone matrix, privacy and independent crypto QA remain
**NOT RUN**. There is **no verified itch public release**.

**Next:** complete PR/main and org-preview evidence, update **only**
Eden Comms's central registry entry on latest live SHA, then
resume issue #167 Home landscape scroll overlay/Voice tile visual
acceptance—not another speculative networking milestone.

## 2026-11-24 — EdenP Development centralized transition preflight

**Owner request:** Transfer Eden Comms into `EdenP-Development`
and shared standards without losing progress, design bible, source
history, signing identity or actual user app data.

**Live audit:** Repo still `PlayerEden/Eden-Comms`, ID `1445090231`,
main `2a19e91f2af15a788920c032bc1eba4e9fbdc2e4`,
161 branches on first two GitHub pages, 0 open PRs, 10 open
issues; no public release verified. Most recent Android main CI
passed; Preview `200014` built and verified with its public
AOSP test certificate and artifact hash; full emulator visual
job failed after 13 scenes, and issue #167 tracks the observed
overlapping Home scroll cue plus landscape Voice navigation.
Actual 18×3 physical matrix and independent security still not run.

**Central standards:** Read live central README, app registry,
organization transition, signing key management, release policy,
save preservation, disaster recovery, release checklist and
shared templates. Updated **only this project's entry** in the
shared `APP_REGISTRY.json` with verified, non-secret package,
cert, version, source and CI evidence; ownership transfer marked
pending. No private keys, passwords or fake release statuses.

**Signing:** Preserved public-test-signed isolated
`com.edenpractical.comms.preview` identity. Original
`com.edenpractical.comms` internal-test/production key custody
and private secret availability are unverified, no key generated
or overwritten. Guarded private signing workflow currently
uses old owner `GITHUB_REPOSITORY`, so updating it before transfer
would break protected builds. See
[preflight and exact post-transfer checklist](EDENP_DEVELOPMENT_INTEGRATION_2026_11_24.md).

**Next:** owner GitHub transfer, connector access/history checks,
update workflow guards + source assertions and current docs,
run actual post-transfer CI/Preview, verify original signer only
if credentials exist and are accessible; resume issue #167 and
one consolidated phone QA. This is an integration preflight,
**not a completed migration**.

## 2026-11-10 — Whole-app / GitHub quality audit and design bible

**Reason:** The owner requested an overall audit, not another feature
iteration, including a check for a forgotten product/design bible.

**Repository baseline:** `main` `359443f3a29ef7cce5442b54e94124dd0eaea72a`.
No open PRs at audit start. The latest merged-main Android/JVM/Python
CI was green and installable Preview 200013 was built, but the
integrated emulator visual job **FAILED** and the single two-phone
acceptance matrix is **NOT RUN**.

**Audit:** 584 repository files, 152 docs; no canonical live product/design
bible despite old Product Vision, Privacy Charter, UX baselines, and
milestone notes. Several dated docs still describe formerly disabled
features and different visual palettes. Nine open GitHub issues
lack source/CI/device/independent review distinctions. Identified
work that is documented as implemented versus actually device-accepted.

**Real source bug found:** `scripts/emulator_visual_qa.py` had literal
`\\n` comment escapes that swallowed the code setting the Preview
package and Activity class; `adb am start` tried the ordinary app
package even though the Preview APK was installed. Restored real
executable assignments and added Python tests that actually invoke
`main()` to prove the chosen package and component, not merely
search the text for a statement.

**Artifacts:** [Design Bible](EDEN_COMMS_DESIGN_BIBLE.md),
[overall audit](OVERALL_QUALITY_AUDIT_2026_11_10.md), updated README,
continuation entrypoint and current handoff. No crypto, radio,
voice, transport, permissions, data storage, signing or production
capability modifications.

**Next:** exact final PR-head Android and Python CI, merge, independent
main CI, and inspect newly captured real emulator PNGs. Fix real
navigation/visual issues; one consolidated physical two-phone
session and independent protocol/security review remain necessary.

## 2026-11-10 — First owner visual feedback: Home needs scroll discoverability

**Evidence:** Owner opened the actual integrated Android Preview on phone
and shared two dark-theme Home screenshots. Home, Connect Nearby, Text
and Voice/PTT tiles are legible, but Settings and How it works sit
below the viewport without a visual indication that the page scrolls.
This is an actual observed usability issue, not a speculative
networking edge case.

**Source fix:** The existing Home Compose vertical scroll uses a retained
`ScrollState` and renders a small olive-accented, 48dp-minimum
`↓ SCROLL FOR MORE` action anchored at the viewport bottom only while
more content exists below and the user is still at the top. Tapping
scrolls 240dp (bounded to actual content); a swipe dismisses it.
It is absent when the page already fits or on any non-Home route.
The fixed header, buttons and communication/security code stay
unchanged. Source regression covers conditional visibility,
bounded action, production flag separation and rebuilding the
installable Preview from changes to the real Home source.

**Acceptance:** Android compile/CI + a fresh signed Preview still required
before calling this visually verified. Phone screenshot feedback
supports the need for this fix, **not** the appearance of the
uninstalled revision. Two-phone/security acceptance still NOT RUN.

## 2026-11-09 — Integrated full-function Preview and real visual QA

**Owner direction:** Prioritize a single usable, inspectable Android app
over repeated small M6 edge-case milestones. Base `main`:
`dd0366f966ffe419dda45b78631eb9cb71525725`
([M6-I PR CI SUCCESS](https://github.com/PlayerEden/Eden-Comms/actions/runs/42725506431),
[main CI SUCCESS](https://github.com/PlayerEden/Eden-Comms/actions/runs/42725798742)).
**Branch:** `feature/integrated-preview-and-emulator-visual-2026-11-09`.

**Finding:** The existing real debug transport source already
implements LAN, Bluetooth and Wi-Fi Direct verified TEXT/ACK,
short live PTT and one explicit Connect route. But no actual
Android emulator visual screenshots had been accepted, and the
M4-UI07 driver incorrectly expected Home → Wi-Fi QR without
the new three-method chooser, a retired `COMING SOON`
Voice route, and stale Help copy. A CI-only source checkpoint
was misleadingly close to being called “done.”

**Implementation:** Updated existing safe emulator driver to
follow Home → three-method chooser → Same-Wi-Fi idle QR and
return correctly, and Voice → chooser with real Help copy.
Bound its package argument strictly to the normal debug or
`.preview` application ID; retain ADB emulator-only guard,
no QR/identities/peer/radio/audio or secret evidence. Added
`integrated-visual` job to existing installable Preview
workflow, downloading **the exact signed Preview APK** from
its own build job, installing it in Pixel 5 Android 35 and
uploading actual PNGs + sanitized summary. Includes
portrait/compact/large-font/landscape/keyboard/screens.
Updated bundled first-use guide to reflect all three
actual paths and no premature message-read/remote-audibility
claims. Added Python integration assertions and
[full audit](INTEGRATED_PREVIEW_VISUAL_QA_2026_11_09.md).

**Verification state:** Exact PR CI, separate main CI, signed
Preview APK artifact, emulator screenshots and owner
on-handset acceptance **pending**. No device screenshot,
real audio, QR camera, text ACK, 2-phone reachability or
independent security assessment has been represented as
completed. Production `CAN_*` remain FALSE.

**Next:** run source CI, merge if green, use automatic main
Preview+visual run to inspect the actual APK. If emulator
navigation fails, repair real test / app and run again.
Offer the single test APK and clear owner first-impression
steps before planning another code mini-milestone.

## 2026-11-09 — M6-I: fence real Wi-Fi Direct delayed callback teardown

**Base:** M6-H `main` `cbbd61b95e1431392ff435bd182aa8b8324a675d`.
[M6-H final PR-head CI SUCCESS](https://github.com/PlayerEden/Eden-Comms/actions/runs/42707312560);
[independent main CI SUCCESS](https://github.com/PlayerEden/Eden-Comms/actions/runs/42707691367).
**Source branch:** `feature/m6-i-p2p-stale-callback-isolation-2026-11-09`.

**Why:** Found two concrete P2P Join interrupted-session races:
late `requestConnectionInfo`/`requestGroupInfo` error callbacks
called an unscoped `endPendingVerified(message)` that closed
whichever pending QR object was currently stored and posted STOPPED,
without proving it belonged to the original Android token or proof.
Meanwhile the Activity's old controller's report/finished/verified
status, consent/text/audio or optional public identity callback
could write over a newly started controller's state.

**What:** `endPendingVerified(token, request, message)` now checks
**same current token + same pending one-use QR request**, actual
GROUP_OBSERVED gate, and no promoted TLS session before it touches
the request or status. All five delayed failure/exception sites
pass the original captured token/request. In the actual Join
Activity, every controller callback verifies exact current owner
before setting Compose status, clearing an old chat, disabling
voice, changing privacy or accepting a public identity. A pure
identity-only `DebugWifiDirectCallbackFence` is shared by owner
and Activity, with JVM cancel/new owner/old proof/late callback
regressions and Python actual-source guardrails.

**Evidence:** [M6-I source audit](M6_I_P2P_INTERRUPTED_CALLBACK_ISOLATION_AUDIT.md);
Kotlin `DebugWifiDirectCallbackFenceTest`;
Python `scripts/tests/test_m6_i_stale_p2p_callbacks.py`.
Exact final PR-head Android/JVM/Python/security CI and independent
merged-main CI pending. **NOT RUN:** actual Android async callback
timing, Wi-Fi Direct two-phone chat, mic/speaker, OEM cleanup,
emulator/keyboard/TalkBack, storage/backup and independent
cryptographic/privacy review.

**Next:** CI gates and merge; during the ONE consolidated phone
test, interrupt connection/group-info and confirm an old callback
cannot close a new one-use proof or corrupt a new authenticated
chat. No auto-retry, approval bypass, radio/socket rewrite,
release `CAN_*` change or extra preview APK.

## 2026-11-09 — M6-H: genuine single-use Wi-Fi Direct QR transport proof

**Base:** M6-G merged `main` `bca8156d53806e0deb1d98b68770d198d22d3200`.
[M6-G final PR CI SUCCESS](https://github.com/PlayerEden/Eden-Comms/actions/runs/42705244355),
[independent merged-main CI SUCCESS](https://github.com/PlayerEden/Eden-Comms/actions/runs/42705668476).
**Branch:** `feature/m6-h-one-use-p2p-qr-transport-2026-11-09`.

**Why:** The actual `DebugWifiDirectQrCoordinator` called its
three-QR proof **one use** but allowed `newVerifiedTransportRequest`
to construct another fresh TLS request from the same QR transcript,
even if a previous real P2P/TLS connection had failed while the OS
group remained active. This violated the intended fresh-proof
per-attempt boundary and contradicted existing recovery copy.

**What:** Debug-only `DebugWifiDirectVerifiedQrUseGate` atomically
claims exactly one *successfully constructed* QR-bound TLS request.
Duplicate concurrent requests are closed; UI readiness becomes false
after one use. An explicit fresh QR exchange resets the gate via
the coordinator's original clear QR route, while socket failure,
expiry, timeout or declined approval does **not** reopen old codes.
This gate grants no trust or connection and leaves the original
Android P2P route selection, mutual pinned TLS, exporter, both user
approvals, final encrypted CONFIRM, existing message/voice owners,
and production release gates untouched. User-facing coordinator
copy says to exchange all three new codes on a failed attempt.

**Evidence:** [M6-H source audit](M6_H_SINGLE_USE_WIFI_DIRECT_QR_REQUEST_AUDIT.md),
new JVM simultaneous 32-claimer and repeated one-use tests,
Python QR/host/join/wipe/release-boundary tests. Exact final-head
Android/JVM/Python/security PR CI and independent main CI pending.
**NOT RUN:** real QR camera, TLS/TCP provider, P2P cleanup,
actual two phones, large font/TalkBack, storage/privacy and
independent cryptographic assessment.

**Next:** resolve CI and merge, then use the **one consolidated**
[two-phone matrix](TWO_PHONE_ACCEPTANCE_MATRIX.md) including
one-use failed/declined/timeout retry checks when hardware is
available; real device success is distinct from automated builds.
No APK teaser or production `CAN_*` unlock. Narrow rollback only
after investigating an actual handset regression, never by
silently restoring stale QR reuse.

## 2026-11-09 — M6-G: observed state recovery, clean explicit restart

**Base:** M6-F merged `main` `ef155509e55125be11eef7e75c864c39594d29c6`.
[M6-F exact PR-head CI SUCCESS](https://github.com/PlayerEden/Eden-Comms/actions/runs/42702688134);
[independent main CI SUCCESS](https://github.com/PlayerEden/Eden-Comms/actions/runs/42702975134).
**Source branch:** `feature/m6-g-failure-recovery-guidance-2026-11-09`.

**Why:** After real Bluetooth/P2P stopped links, failures,
permissions/radio changes, and Android P2P group cleanup, the
developer-facing status could leave ordinary users uncertain
whether a channel was active, whether cleanup completed, and
which fresh verified steps to take. The Wi-Fi Direct chat UI's
prior STOPPED label could persist when starting a new radio attempt.

**What:** Added read-only, accessible `DebugNearbyRecoveryGuide`
and `DebugNearbyRecoveryPanel` in debug source only; Bluetooth
STOPPED/permission guidance, P2P host group CLEANING/STOPPED/
unconfirmed cleanup/verified session ended, and P2P join
discovery/radio/verified session ended. Guidance does **not**
claim group removal before Android confirms it, create one-click
trust/retry or infer a verified peer from a radio signal.
The existing UI owners are unchanged. New **user-initiated**
P2P host/search attempts clear the previous terminal, queue,
draft and ACK view to IDLE; only real approved-channel Ready
enables chat. Added Kotlin/JVM coverage of guide and P2P UI
reset plus Python source/production boundary tests and one-pass
negative device-QA matrix addendum.

**Evidence:** [M6-G audit](M6_G_RECOVERY_GUIDANCE_AND_STATE_RESET_AUDIT.md).
Exact final-head Android/JVM/Python/security CI and separate
main CI pending. **NOT RUN:** emulator/real phone recovery,
Bluetooth/P2P permission/radio/cleanup interoperability,
TalkBack and independent security/privacy/Keystore testing.

**Next:** pass CI before merge, test actual Android behavior
once available, follow the consolidated two-phone matrix.
Production `CAN_CONNECT`, `CAN_SEND_MESSAGES`,
`CAN_TRANSMIT_VOICE` remain FALSE. Roll back this narrow
presentation/ephemeral-state PR if real hardware contradicts
its recovery wording; never weaken QR/TLS/both approvals.

## 2026-11-09 — M6-F: nearby keyboard, capture and reset behavior

**Base:** M6-E `main` `6dc2070692a7143c3e76e35599a16ec44a01580d`.
[M6-E final-head PR CI SUCCESS](https://github.com/PlayerEden/Eden-Comms/actions/runs/42696448115);
[independent main CI SUCCESS](https://github.com/PlayerEden/Eden-Comms/actions/runs/42696732161).
**Source branch:** `feature/m6-f-conversation-ime-privacy-recovery-2026-11-09`.

**Why:** Three real debug nearby conversation pages lacked main app's
IME/system-bar inset handling; entering Talk while TextField held focus
did not explicitly hide software keyboard; Bluetooth's QR/chat screen
lacked Wi-Fi Direct's `FLAG_SECURE`; its STOPPED link callback could
leave a queue status from the previous session.

**What:** Add outer route status/navigation/IME padding before scrolling
on Bluetooth and both P2P host/join, and debug manifest `adjustResize`
only for those 3 screens. Shared verified shell clears focus and hides
IME before Talk/Disconnect without skipping real owner disconnect or
existing Talk → Text floor cancellation. Bluetooth debug Activity
requests screenshot/Recents protection before loading QR identity;
Bluetooth STOPPED and newly approved Ready clear stale queue feedback.

**Evidence:** [M6-F audit](M6_F_NEARBY_IME_CAPTURE_RECOVERY_AUDIT.md);
Python source regressions ensure insets, IME calls, release flags,
`FLAG_SECURE`, session reset and debug-only scope. The older M6-A
source test now asserts the real disconnect wrapper rather than an
unwrapped button. Exact-head Android/Gradle/JVM/Python/security CI and
separate postmerge main CI pending. **NOT RUN:** emulator screenshot/
IME/font tests, actual two-phone LAN/Bluetooth/Wi-Fi Direct, OCR/
TalkBack/accessibility, OEM screenshot protections or independent
security/privacy/storage review.

**Next:** green exact-head and merged-main CI; when emulator is
available, visually test layout/IME on real Android. During the ONE
consolidated device acceptance pass, use the C07/C11/C12/C16 addendum
for Text/Talk, keyboard/200% font and capture without sharing real QR.
No new cloud, auto-approval, storage or release capabilities. Roll back
this narrow M6-F source PR if real device layout regresses.

## 2026-11-09 — M6-E: real text composer/queue/ACK accessibility

**Base:** M6-D `main` `475756467698407848429def12c0ab6fd04145d3`.
[M6-D final-head PR CI SUCCESS](https://github.com/PlayerEden/Eden-Comms/actions/runs/42692297197);
[main CI SUCCESS](https://github.com/PlayerEden/Eden-Comms/actions/runs/42692721109).
**Source branch:** `feature/m6-e-text-composer-ack-recovery-2026-11-09`.

**Why:** Bluetooth/P2P connected chat truncated drafts to 280 UTF-16
units even though the protocol accepts 280 Unicode code points. Large
threads lacked bounded scrolling and PiP/BT queue failures had inconsistent
or hidden feedback. ACK/status could be clearer for novice users.

**What:** Both verified debug text panels now reuse
`DebugTextDraftPolicy` for IME, Send and paste, show character count,
render a bounded scrollable transcript and Jump to latest without stealing
a user's reading position. A pure UI copy helper distinguishes **queued**,
**written here**, **received here** and **other-app ACK**, explicitly
denying human-read or delivery inferences. Host/join Wi-Fi Direct and
Bluetooth send owners display true local queue outcomes; rejected drafts
remain intact. Existing secured network owner and human approval code
are unchanged.

**Evidence:** [M6-E audit](M6_E_TEXT_COMPOSER_ACK_RECOVERY_AUDIT.md),
dedicated Kotlin/JVM copy/code-point checks and Python static source
regressions; earlier F2-Q/F3-C source tests updated for safe Unicode
handling. Exact-head Android/Gradle/JVM/Python security CI and separate
main postmerge CI still need final records. **NOT RUN:** emulator,
TalkBack, IME on phone, Bluetooth/P2P/LAN interoperability, full
two-phone matrix and independent crypto/privacy/storage audit.

**Next:** complete CI gates and merge, do real emulator layout review,
then the single scheduled consolidated two-phone pass when hardware is
available. Retain `CAN_*` FALSE, no Preview APK tease. Rollback M6-E
source-only if real-device UX fails; do not reset identities, keys or data.

## 2026-11-09 — M6-D: truthful nearby QR progress and next-step guidance

**Source:** `feature/m6-d-qr-guidance-and-accessibility-2026-11-09`.
Based on M6-C merged `main` commit `9c158b1e9dfea6b82350069cb7cd842956cebd9c`.
[M6-C final-head CI passed](https://github.com/PlayerEden/Eden-Comms/actions/runs/42691177877),
and [postmerge main CI passed](https://github.com/PlayerEden/Eden-Comms/actions/runs/42691600680).

**Why:** Wi-Fi Direct QR UI said "Step 1" even after moving to its second
or third QR. Bluetooth's phase-specific instructions were scattered
throughout its controls. A first-time user could think setup was stalled or
misread exchanged QR metadata as a trusted connection.

**What:** Both debug QR panels now display stage-specific instructions for
their existing host/join coordinators, a distinct "codes exchanged" cue,
a semantic heading and polite status updates. Retained scanner retry,
cancel, 48/52dp buttons and explicit identity creation. No changes to
radio, TLS, QR, approval, Keystore, persistence, release permissions or
network authority. Dedicated
[static regression](../scripts/tests/test_m6_d_qr_walkthrough.py) and
[M6-D audit](M6_D_QR_PAIRING_GUIDANCE_AUDIT.md) document the boundaries.

**Evidence pending:** exact final PR Android/JVM/Python and security tests,
independent postmerge main CI, visual emulator/manual TalkBack and physical
two-device QA. The 18-case matrix is still NOT RUN. No APK distributed.

**Next:** CI gate and merge; then text/ACK and pairing error accessibility,
actual emulator screenshots, and consolidated physical two-phone tests.
Rollback only the M6-D presentation change if actual UX regresses.

## 2026-11-09 — M6-C: accessibility, visual consistency and privacy disclosure audit

**Code:** PR #155 on `feature/m6-c-accessibility-copy-and-chat-polish-2026-11-09`.
Based on verified M6-B `main` commit `3d0e2d6e050d7617079fd1929c85da227e6dea9c`,
[19/19 main CI passed](https://github.com/PlayerEden/Eden-Comms/actions/runs/42669197572).

**Observed static UX issues and changes:** Corrected inactive Text tab so
it takes the same immediate leave-Talk handler as active tab instead of
relying only on a later disposal callback; old disposal/lifecycle stop
still protects capture. Matched verified chat panels to the shared
angular field utility card (CutCornerShape 7dp + outline); added semantic
headings, TalkBack selected/not-selected tab state and Expanded/Collapsed
local privacy/QA state. Dark appearance Switch now explicitly labeled,
and field section headings are navigable. Restored obsolete `ptt`
navigation opens the real connection chooser, not the disabled mock.

Nearby voice panel checks actual RECORD_AUDIO permission again on
ON_RESUME after OS settings; it NEVER automatically requests permission.
Instructions now match live audio while held and accessible two-activation
stop/cancel; status text uses a polite live region.

**Critical disclosure correctness:** Privacy & data had falsely claimed
Bluetooth/P2P voice unavailable and history/remembered peers LAN-only.
Updated the six sections with actual three-transport experimental
functionality, post-approval opt-in retention, independent public-peer
memory, best-effort deletion, OS permissions, server-free limitations
and pending security/physical QA. Home/Help copy no longer suggests
permanent history impossible; production communication flags remain OFF.

**Evidence:** [M6-C source audit](M6_C_USABILITY_ACCESSIBILITY_AUDIT.md),
expanded JVM PrivacyPreviewContentTest, dedicated Python UX source
regressions and new shell security boundaries. Final-head/merged CI
evidence to be recorded in PR #155 after verification; physical
screenshots, TalkBack, real mic and radios **NOT RUN**. This is source
polish, not certification or a new Preview APK.

**Next:** pass CI, merge, independent main CI. Then refine pairing
walkthrough/recovery and keyboard/TalkBack before manual screenshots
and the consolidated two-phone hardware matrix. Rollback PR #155 only.

## 2026-11-09 — M6-B: Talk tab microphone cleanup and one physical QA plan

**PR/source:** [#154](https://github.com/PlayerEden/Eden-Comms/pull/154),
`feature/m6-b-talk-tab-safety-and-qa-matrix-2026-11-09`, based on
verified M6-A `main` commit `b9166cdc4f2809146c5aeeb8eac4f34397a860a7`.
M6-A [postmerge CI passed](https://github.com/PlayerEden/Eden-Comms/actions/runs/42663929342).

**Why:** The unified Talk tab could be hidden while an AudioRecord turn
was active or an encrypted floor GRANT still pending. A new chat tab does
not itself stop a microphone. Also LAN had a redacted copyable QA report,
but Bluetooth/P2P required guesswork during the planned two-phone test.

**Implementation:** The DEBUG-only verified conversation panel now
calls an explicit `onLeaveTalk` on Talk→Text and Talk unmount.
Bluetooth and Wi-Fi Direct host/join map it to their live owner
`release()`, which cancels a pending floor or stops live capture and
queues its final END/RELEASE. Existing Disconnect and onStop still
disable recording, clear sensitive RAM and close connections.

A shared, debug-only, RAM-only `DebugNearbyQaEvidence` stores only
local event counts and never peeks at `Event.text`, PCM bytes, TLS,
QR, peer pins, IP or credentials. Its optional Advanced panel copies
a compact **local observation only** report to Android clipboard on
explicit tap; clipboard privacy warning is visible. All real
Bluetooth/P2P owners observe only events in their already-verified
session and mark evidence ended on activity stop. Added pure JVM
redaction/session reset tests and Python/security source checks.

[Consolidated two-phone QA matrix](TWO_PHONE_ACCEPTANCE_MATRIX.md):
18 core cases per transport, clear role swap and offline tests, expected
proof for C04 wrong/expired QR, C05 asymmetric approval, C07 text/ACK,
C08–C11 audible voice/talk-floor/tab exit, C12 hard stop, C13–C15
history and remember-peer consent, and C16–C18 accessibility/cleanup/
redacted evidence. **Every physical case remains NOT RUN.** Neither
GitHub CI nor the report can establish audibility, security or OEM QA.

**QA receipt:** PR #154 and GitHub Actions hold the final exact-head
build results. Require a green Android debug/release/JUnit/Python/shell
run before merge and an independent main run after. No preview APK
created or real phone results asserted.

**Next/rollback:** fix CI and merge; run single two-phone matrix only
when the owner is ready; repair observed issues and obtain separate
independent crypto/security review. Revert PR #154 alone for rollback.
No saved history, local key material or production capability changes.

## 2026-11-09 — M6-A: one honest Connect → Text/Talk → Disconnect

**Who/what/why:** The app's Home and connection chooser still described
LAN as the only working debug option, and Bluetooth/Wi-Fi Direct as
future-only, despite F3-C/F2-Q/F4-V real source integration. In-chat
Bluetooth/P2P also buried the useful text/talk behind QR/radio/group
diagnostics. Simplify the visible workflow without inventing a
new transport or taking shortcuts through approval. Implement in
[PR #153](https://github.com/PlayerEden/Eden-Comms/pull/153).

**Changes:** The root Home Connect, Text and Talk routes first select
an actual transport from three clearly labeled debug-only methods:
same-Wi-Fi LAN → existing app-local QR page; Bluetooth Classic →
nonexported debug QR/discovery/connection activity; Wi-Fi Direct →
debug capability/permission preflight followed by Host/Join. All
non-LAN launching is guarded by Android FLAG_DEBUGGABLE and
`NearbyMethodCatalog.select()`; runtime launch failures do not
pretend a connection. Release CAN_* remains false and no main
Bluetooth/location/mic permissions are added. A reusable,
debug-only `DebugVerifiedConversationPanel` creates the same Text
and live Talk tabs, visible Disconnect and independently opened
local privacy settings across existing authenticated Bluetooth/P2P
host/join chats. Its parent renders it ONLY after real post-QR/
pinned TLS/exporter/dual-confirmed CHAT state. Original radio/QR,
authentication/approval and stop handlers still own permissions,
connections and cleanup; low-level controls stay in setup/Advanced.

**QA and acceptance:** New method unit tests and M6-A Python security
contracts, plus updated formerly LAN-only UX source tests and shell
review-only boundary. [PR #153](https://github.com/PlayerEden/Eden-Comms/pull/153)
records exact build evidence AFTER full CI green; do not assert
success before checking the final head. Device screenshot, screen
reader/large fonts, physical two-phone sessions, OEM audio/radio/
backup and external cryptographic review remain OPEN.

**Next/rollback:** Fix exact-head CI, merge and confirm main, then
run one consolidated real-phone test/bugfix pass. Revert PR #153
alone to restore old routing/UI, not F2/F3/F4/F5 security/storage.
Existing session state/keys/history are not migrated or deleted.

## 2026-11-09 — F4-V: live floor-controlled Bluetooth and Wi-Fi Direct

**Source:** [PR #152](https://github.com/PlayerEden/Eden-Comms/pull/152),
`feature/f4-v-floor-controlled-live-nearby-voice-2026-11-09`.
No extra Preview APK or normal-release capability change.

**Why:** F4-U introduced REAL captured microphone audio on both transports,
but sent it only after release, with no collision/floor arbitration.
The user wants the practical walkie-talkie flow before device testing.
Reuse the LAN's already-tested half-duplex policy (host arbitration,
correlated joiner grant, deny, cancel, lease expiry), avoiding another
separate Bluetooth/P2P floor implementation.

**What changed:** The actual current authenticated Bluetooth RFCOMM
and Wi-Fi Direct host/join TLS writer now validates ECFL voice floor
frames alongside text and 640-byte PCM. Floor requests/responses are
bound to the same channel and verified role. User initiates a request
before any microphone capture; the joiner waits with mic OFF until
its own authenticated GRANT, and a released request sends CANCEL.
After GRANT, the existing 16kHz `DebugLanVoiceAudio.startLiveCapture`
sends each 20ms PCM frame as it is captured (not after release) into a
bounded TLS queue. START/END+RELEASE order, maximum 150 frames, host
arbitration, 3s request pending timeout, 9s lease timeout and
fail-close if queue overrun are enforced. Remote playback consumes
ordered live frame callbacks; the old combined clip callback is ignored
in UI, retained only for backward protocol regression. Ephemeral data
is wiped and microphone/speaker stopped on session loss.

**Security boundaries:** No QR/radio discovered peer can grant talk;
both human approvals, exporter/channel binding and the same verified
SSLEngine remain mandatory. No voice persistence or automatic mic
permission. All production CAN_* permissions remain disabled. No claim
of reliable Bluetooth throughput, OEM audio behavior, intelligibility
or independently reviewed security until physical testing.

**QA planned:** Kotlin floor/collision/cancel/replay unit tests,
real two-JDK-TLS-engine authenticated same-channel request/grant and
live 20ms PCM roundtrip, Python source boundary tests, Android debug
and release compile, full CI and independent main check. Exact links
and passing hashes in PR #152 after verification.

**Next/rollback:** Fix PR until exact head green, merge and confirm main;
then unify easy connection flow, consolidated two-phone QA and external
cryptographic review. Revert PR #152 only; do not roll back F4-U and
the separate F5-A/B/C local retention stores unnecessarily.

## 2026-11-09 — F4-U: actual approved Bluetooth and P2P voice bursts

**PR/branch:** [#151](https://github.com/PlayerEden/Eden-Comms/pull/151),
`feature/f4-u-nearby-voice-burst-2026-11-09`. No Preview APK requested
or created.

**Why:** Finish useful cross-transport voice capabilities in source before
one consolidated two-phone test, not another future-only demonstration.
Reuse the existing local 16-kHz mono AudioRecord/AudioTrack driver and
20ms PCM codec without adding a third radio protocol or account.

**What:** Mixed ECBT text/ACK and ECVP START/DATA/END PCM records are
validated and wrapped by the SAME live QR/TLS/exporter/both-approved engine.
The shared approved Bluetooth text channel now queues a single bounded
up-to-3s microphone clip after hold release, sequences at most 150 PCM
frames, reconstructs exact ordered remote bytes in memory, and outputs to
Android speaker. P2P already uses this exact channel; adds guarded voice
offer on both actual P2P host and join controllers. Shared Android UI
asks for microphone permission with an explicit button; inactive links,
loss of permission, activity background or disconnect cancel capture and
playback and wipe unsent PCM. No raw socket, storage, services or
automatic background microphone.

**Limitations:** This first pass is **post-release short voice burst**, not
continuous real-time streaming and not a negotiated half-duplex
REQUEST/GRANT floor; two people talking simultaneously may cause local
speaker/mic contention. Debug only, unreviewed and untested on physical
Bluetooth/P2P devices. Never claim secure/low-latency voice production.

**QA:** Strict mixed-frame Kotlin tests and full real JVM dual-confirmed
TLS interop test (PCM each direction, both text/ACK and PCM on the same
engine) plus security source/shell regression gates. Final PR head CI
and main build links are added in PR discussion after verification;
do not assert success until they actually finish.

**Next:** voice floor arbitration and genuinely live short streaming,
then streamlined connection UI and consolidated two-device and security
acceptance. Rollback PR #151 alone; not linked to peer/history stores.

## 2026-11-09 — F5-C: Bluetooth and Wi-Fi Direct private local options

**Source/PR:** [#150](https://github.com/PlayerEden/Eden-Comms/pull/150)
on `feature/f5-c-authenticated-bluetooth-p2p-privacy-2026-11-09`.
No Preview APK build triggered. Branch is not hardware/security accepted.

**Why:** The user's core-first plan requires the same opt-in history and
public-peer retention decisions on all actual debug chat transports,
without separate half-working demos or copied persistence implementations.

**What changed:** One shared DEBUG privacy owner + UI is invoked only by
post-approval, same-channel Bluetooth Classic or Wi-Fi Direct session
adoption. The original pinned TLS/QR/exporter/commitments and both human
APPROVE/CONFIRM records still gate the connection; metadata never flows
back into TLS/QR, discovery or authorization. The owner uses existing
separate F5-A history and F5-B public-peer encrypted stores, session-only
default, explicit 1h–30d history and 1–30d remembered fingerprint, view and
independent delete, per-session token/async fences and serialized storage
operations for consent/off/expiry ordering.

**QA:** Dedicated Python F5-C source regressions + fail-closed shell guards;
use [GitHub Actions](https://github.com/PlayerEden/Eden-Comms/actions)
for the exact head's Android/JVM/security result. At writing this log
the exact-head result and final merge are **not yet verified**. Prior
F5-A/F5-B unit tests guard expiry, AEAD tampering, and no silent renewal.

**Still missing:** physical Android 12+ Bluetooth/P2P/Keystore checks,
independent cryptographic protocol review, transport voice beyond existing
LAN, simplified cross-transport navigation. Do NOT claim reviewed secure
communication, dependable message persistence or flash erasure.

**Next/rollback:** Fix and verify exact-head CI; merge and check main,
then prioritize real voice + cohesive connection UI. Reverting the PR
doesn't erase ciphertext already stored by a test installation; use
in-app delete/Forget and avoid touching F5-A/B unrelated data.

## 2026-11-09 — F5-B: Remember this phone, separate consent and identity proof

**Who/what/where/why:** The owner wants all core functions implemented
in source before one consolidated phone test. After F5-A local history,
build the independent peer-identity retention decision, not a remembered
contact shortcut around cryptographic or human checks. Source branch
`feature/f5-b-explicit-peer-memory-2026-11-09`, [PR #149](https://github.com/PlayerEden/Eden-Comms/pull/149).

**What changed:** Pure peer-memory 1–30-day policy, 8-peer bound and
clock rollback/expiry fail-closed; separate DEBUG Keystore AES-GCM key,
AAD, ciphertext and no-backup directory holding only the public peer
fingerprint, this phone's public fingerprint, and expiry/integrity metadata.
Only the real LAN **APPROVAL_COMPLETE** callback may display previously
remembered metadata. A separate choice inside active verified LAN chat
lets the user remember 1–30 days, shorten but never silently extend,
forget this peer, or forget all. Session end invalidates callbacks and
resets UI. Identity reset separately purges experimental peer cache and
F5-A history. RELEASE stores are hard no-op.

**Safety / real acceptance:** Saved public key fingerprints are NOT
trusted connections. All future peers must still complete fresh QR/TLS,
session challenge, both approvals and final confirmations. No names,
addresses, phone numbers, message text, voice, backend or auto-reconnect;
no unaudited auth-capability flag changed. Real Android device, backup
rules, clock rollback, identity reset, two-phone P2P/Classic and independent
cryptographic/security review remain outstanding.

**QA receipt:** [PR #149](https://github.com/PlayerEden/Eden-Comms/pull/149)
and [Actions](https://github.com/PlayerEden/Eden-Comms/actions).
Policy unit tests, separate ciphertext sourcing and explicit consent
source gates require final-head green Android CI. Post-merge CI must be
checked separately; don't claim either before seeing the result.

**Next:** Integrate the independent privacy/peer-memory choices into
verified Bluetooth and Wi-Fi Direct sessions (never discovery); then
unify connection UX and plan one meaningful physical-device test.
**Rollback:** revert PR #149 without rolling back existing F5-A history;
running code cannot retroactively clear ciphertext already saved on
previously installed test devices. App Forget controls are provided.

## 2026-11-09 — F5-A: optional encrypted local history + simpler project handoff

**Why:** The owner wants the actual usable core functions implemented in code
before the big two-phone test, and fewer hollow Preview checkpoints. The
Sudoku project uses a one-page `CONTINUE_HERE.md`, exact milestone work
logs, QA receipts and an explicit current handoff. Word Search uses
`docs/START_HERE.md`. Eden Comms had valuable but scattered milestone docs.

**Who/what/where:** Source development in the public
`PlayerEden/Eden-Comms` GitHub repo, branch
`feature/f5-a-opt-in-encrypted-local-history-and-handoff-2026-11-09`.
Introduced F5-A pure retention policy and tests, a DEBUG Android Keystore
AES-GCM history store in `noBackupFilesDir`, a RELEASE no-op store, and
actual LAN confirmed-TLS text callback → opt-in save. A user can select
Session only (default), 1h, 24h, 7d, 14d or 30d, and view/delete records
for the currently reverified peer. The short local disappearing timer
pauses persistence; peer trust is completely separate.

**Safety:** No auto-save, no drafts/voice, no remembered addresses, no
automatic trusted reconnect, no release capability switch, no new cloud.
Expiry filters before display and rollback/corruption fail closed.
Manual deletion is best effort on local app files, not flash/screenshot/
recipient copies. Independent crypto/device/backup verification remains
REQUIRED and no production security claim is made.

**QA source receipt:** [PR #148](https://github.com/PlayerEden/Eden-Comms/pull/148).
New pure JUnit expiration and real AES-GCM tamper/negative tests, alongside
Python security source assertions and shell release/backup gates. Full
PR check history appears in [GitHub Actions](https://github.com/PlayerEden/Eden-Comms/actions).
Prior runs surfaced stale "no history" privacy assertions; after correcting
the UI disclosures and tests, verify the **final head** and post-merge CI
before describing the pass as green. No real-device security acceptance.

**Next:** make final-source Android CI pass, merge the reviewed PR, check
main CI; then tackle F5-B opt-in **peer remembering** with a separate
1–30-day expiry and human/cryptographic reauthentication every time.

**Rollback:** revert the F5-A code PR; this does NOT revoke stored data
from an already installed test app. Provide the in-app delete control.

## 2026-11-09 — F3-C: Wi-Fi Direct authenticated text

**PR:** [#147](https://github.com/PlayerEden/Eden-Comms/pull/147),
main merge `2d40b67987605fee0ff5ebab34c1bd61bdfaf71a`.
**Evidence:** [Post-merge Android CI passed](https://github.com/PlayerEden/Eden-Comms/actions/runs/42572812574).
**Change:** moved live three-QR preparation onto host/join Android radio
screens, bound fresh TCP socket to OS P2P interface, reused exact mutual
TLS/exporter/consent protocol and encrypted TEXT/ACK worker; added
foreground/timeout/cancellation guards. **Not phone/security accepted.**
**Next then:** optional encrypted history and peer retention.

## 2026-11-09 — F2-Q: Bluetooth authenticated text

**PR:** [#146](https://github.com/PlayerEden/Eden-Comms/pull/146),
main merge `e2fd6eea3ee4e67fd14d64e433db4e6e1e1b8096`.
**Evidence:** [Post-merge Android CI passed](https://github.com/PlayerEden/Eden-Comms/actions/runs/42568879327).
**Change:** kept actual reciprocal-QR, mutually pinned TLS 1.3 RFCOMM
socket alive after both confirmations and connected encrypted typed TEXT,
receive and peer-app ACK UI. Added paired JVM tests; no production claim,
no Bluetooth voice, no physical acceptance.
