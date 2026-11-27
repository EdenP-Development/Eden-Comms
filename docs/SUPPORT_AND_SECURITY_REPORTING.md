# EC-B05 — Support, troubleshooting and confidential reporting readiness

2026-11-27. Status: internal documentation, active development. No public support service, contact, SLA or storefront established. Applies hub [BUS-06](https://github.com/EdenP-Development/Eden-Development-Standards/blob/main/CUSTOMER_SUPPORT.md) and [support intake template](https://github.com/EdenP-Development/Eden-Development-Standards/blob/main/templates/SUPPORT_INTAKE.md); stricter [Privacy and Security Charter](PRIVACY_SECURITY_CHARTER.md) governs.

## Tester help — draft, not public service

Use harmless test content only. Internal 10049 is the consolidated runtime candidate; see [exact receipt](evidence/internal-10049-receipt.json). Debug functionality is not a production secure messenger or emergency service. Physical compatibility and independent security review remain open.

| Symptom | Safe first action |
|---|---|
| APK cannot install/update | Check package, channel, version and signer against the exact receipt. Do not uninstall, clear data, downgrade or use a different signer to force installation. Preserve existing data; stop if identity differs. Preview and internal packages are separate. |
| Same Wi-Fi cannot connect | Ensure both phones explicitly select the same method and share the intended local Wi-Fi. Guest/client isolation may prevent local peer traffic. Do not disable security controls, expose ports to WAN or use an untrusted network to troubleshoot. |
| Bluetooth or Wi-Fi Direct fails | Check selected method's Android permission/radio readiness; follow local recovery guidance. If temporary group cleanup is unconfirmed, check Android Wi-Fi Direct settings before starting a fresh attempt. |
| QR or approval fails | Cancel on both phones and perform a fresh in-person exchange and separate approvals. Never bypass failed verification or reuse expired proof. Remembered peers do not replace approval. |
| Message not acknowledged | Distinguish local queue/write and peer-app ACK. Do not interpret ACK as read receipt or automatically resend uncertain messages. Start a fresh verified session if stopped. |
| Talk unavailable or interrupted | Check explicit mic permission and floor status; release Talk, stop the session if unexpected behavior occurs. Never grant unrelated permissions. Actual audio latency/intelligibility remains unverified. |
| Unexpected microphone activity, approval bypass or retained content | Stop testing and disconnect; revoke affected permission if appropriate. Do not continue the affected workflow; treat as a confidential security/privacy report. Preserve only minimal safe evidence. |
| History or remembered peer concern | Use the relevant local retention/erase/forget controls. Identity reset is separate and may invalidate pairing. Do not promise remote deletion, secure flash erasure or recovery of expired content. |
| Large text or navigation problem | Report device/OS, orientation and font scaling; share only sanitized disconnected-screen evidence. Do not capture private conversation or QR screens. |

## Minimal intake

For an ordinary bug record version/build, channel, Android major version and device model if useful (no serial), method, host/join role, sanitized steps, expected and observed behavior, frequency and safe workaround. Use synthetic text/audio; optional screenshots must contain no QR, conversations, identifiers or sensitive settings. Do not request raw logs, keys, passwords, full backups, actual recordings, addresses or private message bodies. QA counts may be copied explicitly and reviewed before sharing. No automatic telemetry.

Public issues are for sanitized non-sensitive defects only. Confidential reports require an owner-approved private route. GitHub private vulnerability reporting is a candidate, not verified/enabled by this work; no confidential details should be posted publicly. Until a route is confirmed, do not solicit confidential reports through the draft or promise public support.

## Internal triage and incident workflow

| Priority | Examples | Action |
|---|---|---|
| P0 critical | Credible authentication bypass, plaintext disclosure, unauthorized recording, material data loss or active serious exposure | Stop affected testing/distribution; contain, preserve minimal restricted evidence, assess affected versions, seek qualified security/legal assistance as needed |
| P1 high | Core workflow unavailable, repeatable teardown failure, significant privacy/accessibility defect | Prioritize reproduction and safe containment; evaluate charter no-ship gate |
| P2 normal | Noncritical usability or compatibility issue | Reproduce with synthetic fixture and track fix |
| P3 feedback | Cosmetic or feature suggestion | Evaluate against frozen scope; no promise |

Use Reported / Investigating / Reproduced / Planned / Fixed pending verification / Verified / Closed with rationale. Distinguish allegations, reproduced failures and verified fixes. Confidential evidence remains in restricted owner-controlled storage, never public issues. Assess applicable notification/disclosure duties promptly with qualified help when needed; communicate verified facts, limitations and affected versions only. No automated monitoring or remote disable mechanism.

Fixes follow exact-source CI, appropriate physical regression, signing/upgrade checks and release receipts. No silent artifact replacement. No refunds/payment process established; use actual approved storefront procedure if later applicable.

## Readiness checklist (not executed)

- [ ] Confirm owner-approved legal publisher and monitored support contact.
- [ ] Verify confidential security/privacy route with harmless independent-account test; verify access restrictions and recovery.
- [ ] Establish proportionate support record retention, deletion and access rules before collection.
- [ ] Run synthetic ordinary bug, data-loss and security-report routing drills; do not use real customer data.
- [ ] Approve accurate version-specific help and privacy pages, durable HTTPS hosting and app/store links.
- [ ] Confirm maintenance capacity and actual storefront refund/support requirements, if applicable.
- [ ] Record actual evidence and owner approval. No public contacts invented, account settings changed or service activated.

See [physical acceptance](TWO_PHONE_ACCEPTANCE_MATRIX.md), [data handling register](DATA_HANDLING_REGISTER.md), [working privacy draft](drafts/EDEN_COMMS_PRIVACY_POLICY_WORKING_DRAFT.md) and [release readiness](BETA_1_READINESS_CHECKLIST.md).
