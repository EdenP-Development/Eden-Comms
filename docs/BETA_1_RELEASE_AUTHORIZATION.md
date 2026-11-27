# EC-B11 — Beta 1 exact-artifact authorization
2026-11-27. Decision: NO-SHIP for public functional beta; internal controlled QA only. This is a preparation checkpoint, not an approval. Apply the [charter](PRIVACY_SECURITY_CHARTER.md), [release plan](BETA_1_RELEASE_PLAN.md) and hub PORT-10 release procedure.

## Current evidence and mandatory gates
| Gate | Evidence / current disposition |
|---|---|
| Scope and identity | Frozen debug internal 10049, source 50b506a71548be32d3c82a513f7f3bef1e7b8b45; same-signer 10048 predecessor. [Receipt](evidence/internal-10049-receipt.json). No previous public release. Production candidate and signer decision absent. |
| Automated QA | Internal receipt records 442 Python checks, Android CI and separate Preview 28 disconnected screenshots; not exact production evidence. |
| Recovery | [Archive inventory](DURABLE_RECOVERY_ARCHIVE.md) prepared; byte verification, independent copies and owner signer recovery pending. |
| Physical | [54-case matrix](TWO_PHONE_ACCEPTANCE_MATRIX.md) 0/54; upgrade, retention, accessibility and physical icon acceptance pending. |
| Security | [Independent review brief](INDEPENDENT_SECURITY_REVIEW_BRIEF.md) prepared; independent review, negative transport tests, WAN capture and backup/restore not run. |
| Release engineering | Non-debug package, exact manifest and permissions, reviewed production capability admission, SBOM, signer and actual installed artifact verification pending. |
| Rights and data | Source registers and privacy draft prepared; exact shipped rights/dependency/data reconciliation and approved hosted policy pending. |
| Support and distribution | [Storefront preparation](PROFESSIONAL_STOREFRONT_READINESS.md); actual channel, publisher/contact, support and confidential route, live platform requirements, screenshots and pricing unresolved. |
| Owner authorization | Not granted; no publication. |

## Final authorization record (unfilled)
Product/channel; intended scope and supported devices; exact source SHA; build run/job and non-debug status; package, versionCode/name, installed signer SHA-256, exact APK/AAB and delivered APK hashes where applicable; prior accepted artifact or first-release rationale; archive verification and owner recovery status/date; exact-source CI and physical outcomes; upgrade/retention results; independent security report and remediation/retest; rights/privacy/support/platform evidence; remaining low-risk deferrals with owner rationale; explicit owner decision for exact artifact/channel/date; actual distribution/download verification. Never record private credentials, device identifiers or user content. New artifact invalidates affected evidence. No mandatory security, rights or data-loss gate may be waived.

## Execution backlog after preparation
1. Preserve exact 10048/10049 and Preview evidence before expiry; verify durable copies and owner recovery. If unavailable, record missing and do not substitute silently.
2. Narrow non-sensitive appearance wrong-type preference fix (EDT-01): inspect both read sites, preserve existing migration/defaults, no writes or generic security fallback; test malformed types, missing values and valid settings. Use separate runtime PR and regression evidence; keep 10049 frozen until a verified successor is explicitly selected.
3. Execute consolidated two-phone acceptance and actual upgrade on verified artifacts; use synthetic content. Fix observed blockers, rerun affected checks.
4. Prepare non-debug packaging boundary and exact release identity; independent security review and physical evidence must cover final intended artifact before public beta. No enabling production flags just to build.
5. Resolve exact rights/data/support/storefront requirements and obtain explicit final authorization. Archive and verify distributed bytes only after approval.

Preparation complete only when this document passes review/CI; execution gates remain open. No release, signing change or runtime modification in this checkpoint.
