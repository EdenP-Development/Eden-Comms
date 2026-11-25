# Beta 1 readiness checklist

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
