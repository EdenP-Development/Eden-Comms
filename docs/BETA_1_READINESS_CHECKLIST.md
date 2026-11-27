# Beta 1 readiness checklist

## EC-B04 rights inventory checkpoint (2026-11-27)

PR #221 merged c25dda7ca010aab80e6aa4e3c0fca4ff4e2907fe after CI #616. [Asset rights register](ASSET_RIGHTS_REGISTER.md) records EPS and product artwork, native icons, code and direct dependencies. Initial source inventory only; actual resolved SBOM, notices, creator/terms evidence, trademark review and exact release clearance pending. Next EC-B05 support/security reporting. No runtime or license changes.

## EC-R10 / EC-B01–B03 checkpoint (2026-11-27)

EC-R10 merged #220 at 50b506a71548be32d3c82a513f7f3bef1e7b8b45; main Android 45791275292, private signing 45791275284 and integrated Preview 45791275281 passed. 442 Python checks and 28 disconnected screenshots. [Internal 10049](https://github.com/EdenP-Development/Eden-Comms/actions/runs/45791275284/artifacts/15102478507) expires Dec 3; [Preview evidence](https://github.com/EdenP-Development/Eden-Comms/actions/runs/45791275281/artifacts/15103426213) expires Nov 28. See docs/evidence/internal-10049-receipt.json, docs/DATA_HANDLING_REGISTER.md, docs/drafts/EDEN_COMMS_PRIVACY_POLICY_WORKING_DRAFT.md. Hub PORT-10/BUS-03 templates applied; draft not published. Physical 0/54, owner signer recovery, actual upgrade, independent security, archive byte verification and release rights/data audit remain pending. Next EC-B04 asset/dependency rights inventory, EC-B05 support/privacy reporting, EC-B06 bounded toolkit review, EC-B07 recovery/archive, EC-B08 physical upgrade and acceptance, EC-B09 security review, EC-B10 storefront and EC-B11 exact-artifact authorization. No runtime changes or publication.


## EC-R6–R9 reliability checkpoint (2026-11-26)

Verified merged PRs: #209 fresh pairing CI #588; #210 ACK regression CI #590; #211 LAN write-before-ACK fix CI #592; #212 Bluetooth/Wi-Fi Direct deferred ACK fix CI #597; #213 audio ownership CI #599; #214 expired floor approval fix CI #602; #215 microphone activation/cancellation CI #604; #216 speaker activation/cancellation CI #606; #217 nearby queue teardown CI #608; #218 LAN queued PCM shutdown CI #610, main edf3814ca0576472f5032371a09a9a1af84f7ee2. Post-icon integrated Preview 200037 run 45590660687 succeeded. These are source/CI results, not physical acceptance. EC-R9C adds 100 independent queue turns and LAN shutdown source guard; CI pending. Next EC-R10 consolidated signed internal candidate and integrated QA; confirm artifacts and registry against actual successful runs. Physical 54 cases, physical icon acceptance, audio cancellation latency, independent security review and all release gates remain open. No publishing.


## EC-R6 reliability checkpoint (2026-11-25)

Visual Review 5 runtime artwork remains at 542145f0389d8b32113bb9850bee7a9daa330081 (internal 10034). PR #206 merged d0bee9788f60a7eaa64303113b02e92c0f60c1bc after CI #582; post-icon Preview run 45590660687 not yet confirmed complete. PR #207 merged 4ff686a4468d97f1707b8d4a655c6b0bd5a1b794 after CI #584; real JVM loopback accept/read cancellation and stale listener release tests passed. Main Android run 45591364629 and signing 45591364667 passed: [internal 10036](https://github.com/EdenP-Development/Eden-Comms/actions/runs/45591364667/artifacts/15011227339), APK SHA-256 11dd8964f5020b6a719671a4702b6b4235498f38831c297d6e208a8553e41fa4. PR #208 merged d6d6399462a458a0496415030c354553d6bfed2e after CI #586; partial LAN metadata loss and stalled writer forced-close tests passed. Main follow-up pending. EC-R6C branch adds Bluetooth old opened-link role/reason cross-product and Wi-Fi Direct cancelled permission outcome coverage. CI pending. No runtime changes, no physical evidence from these tests. Next EC-R7 actual message delivery audit, EC-R8 audio lifecycle, EC-R9 resource ownership and EC-R10 consolidated QA. Owner physical artwork approval, 54 physical cases, independent security review and release gates remain open. No publishing.


## Current checkpoint — Visual Review 5 and Beta 1 reliability (2026-11-25)

This checkpoint supersedes earlier visual status below. PR #205 merged at 542145f0389d8b32113bb9850bee7a9daa330081 after CI #580. Main Android run 45586732879 and private signing run 45586732727 passed. [Internal 10034](https://github.com/EdenP-Development/Eden-Comms/actions/runs/45586732727/artifacts/15008313812), expires Dec 2; APK SHA-256 7d4a3617a0f620e5849e40a269160a2d99aaac705972f17192b5b13265dbbcde. Same pinned internal signer. Central registry updated ab0f78913de1cc3b561225a95276e26026ccffac. Owner approved the original matte product icon concept and three-second skippable EPS splash; native derivative icon is merged but physical artwork acceptance remains open. Owner cannot currently upload screenshots; do not block other engineering on visual feedback.

Pre-icon integrated Preview run 45582913336 at e94265f6a587c0ec1719bca43163789347c9b7a4 passed and captured 28 screenshots (artifact 15007657884). No qualitative screenshot inspection or post-icon emulator pass claimed. Add icon resource paths to Preview trigger so subsequent icon changes get integrated checks. Next reliability work: review production boundary, stale callbacks, teardown, retries and test coverage by transport; prefer targeted fixes over feature expansion. All 54 physical cases and independent security review remain NOT RUN; no public functional beta or publication authorized. Use harmless test content only.


## Current checkpoint — EPS Visual Review 2 (2026-11-25)

Owner physically reviewed internal 10015 (source c673600b0eff13134ee6546c4ab6d742f2fff190). EPS/Field Green light and dark screens observed; visual acceptance NOT granted. Owner selected concept C, Modular Comms, as the product-icon direction, not final artwork. Preserve fixed EPS publisher startup art, existing launcher until replacement accepted, app IDs/signing/data and security gates. See docs/EPS_VISUAL_REVIEW_1_FEEDBACK.md and docs/EPS_VISUAL_REFINEMENT_PLAN.md. Next VIS-01 semantic color roles and compact Home design, VIS-02 icon candidates; consolidate visual review rather than small APK churn.

Verified baseline: PR #186 merged; CI #532, exact artwork SHA-256 d144934346d77a6e04c1475dae361fc57cb28a95d7033a799bf6e2f256548516, 426 Python checks passed. Main CI 45556205473, private signing 45556203782, disconnected Preview emulator 45556203668 all passed. [Internal 10015](https://github.com/EdenP-Development/Eden-Comms/actions/runs/45556203782/artifacts/14994963791), [Preview 200022](https://github.com/EdenP-Development/Eden-Comms/actions/runs/45556203668/artifacts/14996375061). Startup physical approval, persistence, accessibility, physical 54-case acceptance, independent security and release engineering remain open. No public release.


Status: internal development, not approved for public distribution. Normative gates: PRIVACY_SECURITY_CHARTER.md and BETA_1_RELEASE_PLAN.md. Owner requests professional software distribution rather than gaming storefront; no storefront selected. Freeze scope to existing nearby one-to-one text and PTT.

| Workstream | Next action / evidence | Status |
|---|---|---|
| Reliability | Finish LAN permission parity; review stale callbacks, radio loss, timeout, teardown and retry for each transport | In progress |
| Integrated UX | Audit actual screens: first launch, permission rationale, QR/approval, Text/Talk, hide/clear, disconnect, recovery; small screens, large fonts, TalkBack | Open |
| Identity | Review existing icon, splash, typography and colors against professional EPS tone; reuse assets before redesign | Open |
| Performance | Record physical battery, audio latency, memory and cleanup observations; no invented benchmarks | Not run |
| Physical QA | Complete 54 cases in TWO_PHONE_ACCEPTANCE_MATRIX.md on same candidate, record device/OS and redacted outcomes; retest failures | Not run |
| Security | Independent crypto/protocol review; spoofing/tamper/backup/retention/WAN traffic evidence, resolve high/critical findings | No-ship |
| Release packaging | Non-debug variant review, signing and install-over evidence, key backup recovery, licenses/SBOM, checksums, rollback | Open |
| User help | Quick start, troubleshooting, limitations, privacy disclosures and support route | Draft below |
| Distribution | Compare professional Android testing/store/direct options when candidate ready; owner approves channel and exact artifact | Deferred |
| Beta feedback | Collect app version, Android version, transport, expected/actual behavior, reproduction; never ask for messages, QR payload, pins or audio | Draft below |

## EC-R5 entry — verified EC-R4 baseline and recovery review

PR #180 merged at 2a690fd160f5a2cf2fef8904052cf6c7672b48c9; main Android CI 45545690005 and signing 45545690006 succeeded. Internal 10009, APK SHA-256 133fcca12730238a2d5857b36b37dd7262a2be3c82b3ca24c0cfbad2e8285a20, same private signer. [Artifact](https://github.com/EdenP-Development/Eden-Comms/actions/runs/45545690006/artifacts/14991567419), expires December 2. Reviewed M6-G recovery audit, actual nearby guidance and LAN continuity/graceful-stop policies: existing explicit fresh pairing, observed cleanup and bounded forced-close behavior should be retained, not rewritten without observed defect. This is a targeted source review, not exhaustive lifecycle or physical evidence. Updated consolidated matrix with current candidate and permission/voice/UX regressions, upgrade 10008 to 10009. All 54 cases remain NOT RUN. Begin integrated UI/quality audit; unresolved recovery behavior to be tested on devices. No public beta or security claims, no runtime/production capability change.

## Draft quick start (internal QA only)

Use two nearby Android phones with the same internal build. Select the same connection method, follow host/join prompts and scan the fresh pairing QR as instructed. Both people must approve before text or voice testing. Use harmless test content only. Talk is limited to three seconds; release to stop. Microphone permission is only needed to speak. Local history is session-only by default; optional saved history and remembered identities are independent choices. Disconnect when done. If interrupted, start a fresh pairing; do not assume old approvals carry over. Never use this unreviewed build for secrets or emergencies.

## Draft feedback template

Build/version; device models and Android versions; transport and host/join role; steps; expected vs actual; reproducibility; whether disconnect and fresh pairing recovered. Redact identifiers and content. Do not submit secrets, QR codes, fingerprints, private messages or recordings.

## Completion rule

A source audit or CI pass is not physical or independent security evidence. Do not mark a workstream complete without recorded evidence. Prioritize functional and safety blockers before cosmetic polish. No public upload without owner approval and charter gates.
