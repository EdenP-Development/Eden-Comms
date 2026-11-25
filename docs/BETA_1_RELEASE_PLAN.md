# Eden Comms — Beta 1 release plan

Owner direction, November 24, 2026: target a first downloadable Android beta, professional software distribution preferred over itch.io; storefront selection deferred until release readiness. Evaluate Android stores, testing tracks and direct Eden Practical Solutions distribution. Keep Spudacus gaming distribution separate. This is a target, not release authorization. The [Privacy and Security Charter](PRIVACY_SECURITY_CHARTER.md) remains normative, including STOP/NO-SHIP on unreviewed cryptography and absent security evidence. Do not publish the debuggable internal QA APK as a public beta or flip production flags to make a build work.

## Scope freeze

Nearby one-to-one text and short PTT on same Wi-Fi, Bluetooth Classic and Wi-Fi Direct; fresh QR identity exchange, separate bilateral approval, explicit disconnect, session-only default, optional local encrypted history and separate peer memory. No accounts, mandatory Internet, cloud relay, advertising, group messaging, attachments or background reconnect. If a transport cannot pass acceptance, defer it explicitly with owner approval rather than presenting it as functional.

## Remaining work and release gates

| Gate | Required evidence | State |
|---|---|---|
| EC-R1/R2/R3 | Merged source and exact-source CI, signed internal QA | Complete automated verification; physical open |
| EC-R4 reliability | Review callback fences, permission/lifecycle teardown, disconnect, timeout, radio changes and retry; regression tests for demonstrated defects | Open |
| EC-R5 integrated quality | Fresh install, compact/landscape/large font/accessibility, clean user journey, truthful copy | Open |
| Physical functionality | C01-C18 on each transport, both phones, swap roles where practical; record failures and retest fixes | NOT RUN |
| Security/privacy | Independent protocol/crypto review, tampering and spoofing negatives, local network capture with WAN on/off, backup/restore and retention review; no open high/critical defects | NOT RUN / NO-SHIP |
| Release engineering | Review non-debug beta variant, package/signing continuity, minimal permissions, dependency/license/SBOM, checksum, changelog, rollback, secure backup recovery | Open |
| Publication | Owner approves exact tested release candidate and itch page, accurate limitations and supported devices, issue/report route | Not authorized |

Do not waive security gates by calling the app beta. Private/internal evaluation with harmless test content is separate from public distribution. If public functional beta is blocked, discuss a clearly disconnected public preview or continued controlled QA, not a disguised debug release.

## Workflow

Finish EC-R4 and EC-R5 against real source. Freeze feature scope and consolidate one two-phone session using [acceptance matrix](TWO_PHONE_ACCEPTANCE_MATRIX.md); prioritize safety failures over cosmetics. Maintain [handoff](CURRENT_HANDOFF.md), [work log](WORK_LOG.md) and central registry. Record exact candidate SHA and actual evidence, not a speculative percentage or calendar promise. Prepare itch copy/assets only after scope and candidate are known. No automatic public publishing.
