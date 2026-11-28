# EC-B11 — Beta 1 exact-artifact authorization
2026-11-27 (execution status reconciled after EC-I08C). Decision: NO-SHIP for public functional beta; internal controlled QA only. This is a preparation checkpoint, not an approval. Apply the [charter](PRIVACY_SECURITY_CHARTER.md), [release plan](BETA_1_RELEASE_PLAN.md) and hub PORT-10 release procedure.

## Current evidence and mandatory gates
| Gate | Evidence / current disposition |
|---|---|
| Scope and identity | Recommended controlled debug internal QA 10062, source 39aef129c993810834528c7008c3efa3348a18f6; same-signer 10059 predecessor. [Receipt](evidence/internal-10062-receipt.json). Historical 10048/10049 remain archived checkpoints, not current candidates. No previous public release. Production candidate and signer decision absent. |
| Automated QA | Internal 10062 receipt records 442 Python checks, Android CI and separate Preview 200040 28 disconnected screenshots. Later isolated Preview 200043 preference recovery 6/6 and 200040→200043 upgrade/signer rejection U01–U09 passed; [receipt](evidence/preview-200043-signer-rejection.json). Actual Keystore instrumentation pending; E01–E09 not accepted. None constitutes exact production evidence. |
| Recovery | [Archive inventory](DURABLE_RECOVERY_ARCHIVE.md) prepared; Historical archive verification recorded in continuation receipts; permanent independent copies and owner signer recovery remain pending. Artifact availability is time-limited. |
| Physical | [54-case matrix](TWO_PHONE_ACCEPTANCE_MATRIX.md) 0/54; upgrade, retention, accessibility and physical icon acceptance pending. |
| Security | [Independent review brief](INDEPENDENT_SECURITY_REVIEW_BRIEF.md) prepared; independent review, negative transport tests, WAN capture and backup/restore not run. |
| Release engineering | Non-debug package, exact manifest and permissions, reviewed production capability admission, SBOM, signer and actual installed artifact verification pending. |
| Rights and data | Source registers and privacy draft prepared; exact shipped rights/dependency/data reconciliation and approved hosted policy pending. |
| Support and distribution | [Storefront preparation](PROFESSIONAL_STOREFRONT_READINESS.md); actual channel, publisher/contact, support and confidential route, live platform requirements, screenshots and pricing unresolved. |
| Owner authorization | Not granted; no publication. |

## Final authorization record (unfilled)
Product/channel; intended scope and supported devices; exact source SHA; build run/job and non-debug status; package, versionCode/name, installed signer SHA-256, exact APK/AAB and delivered APK hashes where applicable; prior accepted artifact or first-release rationale; archive verification and owner recovery status/date; exact-source CI and physical outcomes; upgrade/retention results; independent security report and remediation/retest; rights/privacy/support/platform evidence; remaining low-risk deferrals with owner rationale; explicit owner decision for exact artifact/channel/date; actual distribution/download verification. Never record private credentials, device identifiers or user content. New artifact invalidates affected evidence. No mandatory security, rights or data-loss gate may be waived.

## Execution backlog after preparation
1. Preserve exact recommended 10062/10059, historical 10048/10049 and Preview evidence before expiry where available; verify durable copies and owner recovery. If unavailable, record missing and do not substitute silently.
2. EDT-01 appearance hardening completed; 10062 is the selected controlled QA successor. Complete isolated Keystore and encrypted upgrade acceptance per [EC-I08 contract](ENCRYPTED_UPGRADE_ACCEPTANCE.md); distinguish debug storage from release stubs. Do not promote a new signing workflow output without an exact receipt and selection.
3. Execute consolidated two-phone acceptance and actual upgrade on verified artifacts; use synthetic content. Fix observed blockers, rerun affected checks.
4. Prepare non-debug packaging boundary and exact release identity; independent security review and physical evidence must cover final intended artifact before public beta. No enabling production flags just to build.
5. Resolve exact rights/data/support/storefront requirements and obtain explicit final authorization. Archive and verify distributed bytes only after approval.

Preparation complete only when this document passes review/CI; execution gates remain open. No release, signing change or runtime modification in this checkpoint.
