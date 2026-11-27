# EC-B02 — Data handling register (source review; NOT release clearance)

2026-11-27. Candidate internal 10049, source 50b506a71548be32d3c82a513f7f3bef1e7b8b45. See [receipt](evidence/internal-10049-receipt.json). Adapted from the hub DATA_HANDLING_REGISTER template. All implementation descriptions below are source-level observations or documented design, not an independent audit of packaged behavior.

| Feature | Data and purpose | Storage / retention | Transfer / recipient | Control / consent | Evidence / status |
|---|---|---|---|---|---|
| Appearance | Theme/palette preferences | Local settings until changed/reset | No intended peer transfer | Settings | AppearancePreference.kt; implemented/unverified |
| Pairing identity | Keystore key and public certificate/fingerprint | Local identity persists across sessions | Public pairing material to selected peer | Explicit setup/reset; no implicit trust | Charter and acceptance matrix; device behavior pending |
| QR and nearby discovery | Public identity, ephemeral pairing values, network/radio metadata, camera input | Temporary pairing state; no intended camera archive | Visible QR, selected peer and local radio/network infrastructure | Explicit scan/discovery, permissions and bilateral approval | Main/debug manifests; exact per-transport metadata audit pending |
| Text and receipts | Typed/received text, message IDs, local write/peer ACK status | Session-only by default | Selected approved peer via experimental TLS | Explicit send, disconnect; ACK is not read receipt | EC-R7 CI; physical pending |
| Voice | Microphone PCM and transient playback buffers | Volatile, bounded three-second turns; no intended saved voice | Approved peer; local speaker | Mic permission, explicit Talk and stop | EC-R8/R9 CI; physical latency and cleanup pending |
| Optional history | Text, direction, timestamps, message IDs, verified peer pin | Debug AES-256-GCM envelope in noBackupFilesDir; Keystore key; 1h/24h/7d/14d/30d choices; max 64 records per peer, 8 peers; no renewal on read | Intended local only | Opt-in per conversation; turn off, erase peer/all; reverify same peer before view | LocalHistoryPolicy.kt and DebugLocalHistoryStore.kt; independent review pending |
| Optional remembered peer | Public peer fingerprint and expiry | Separate opt-in local record; exact choices/storage verification pending | No intended external store | Forget/Forget all; fresh pairing still required | Acceptance C15; physical pending |
| QA counts | Local event counts, build evidence | Session state; user may copy summary | Clipboard and destinations chosen by user | Explicit copy; no real content in QA notes | C18; physical pending |
| Backup and OS | App files, preferences, identity, platform artifacts | allowBackup=false and exclusion rules; actual OEM behavior unknown | Android/OS/store/keyboard may process independently | Review OS settings; no guarantee of secure deletion | Source manifest; backup/restore pending |
| External services | No publisher-operated account/relay/ads/analytics intended in frozen scope | None intended | WAN/SDK/OS behavior not established | No new service approved | Charter; exact resolved SDK and WAN capture pending |

## Permissions and direct dependencies

Main source manifest: INTERNET (local TCP), ACCESS_NETWORK_STATE, CAMERA (QR). Debug additions: BLUETOOTH_SCAN and NEARBY_WIFI_DEVICES (neverForLocation declarations), BLUETOOTH_CONNECT, BLUETOOTH_ADVERTISE, ACCESS_WIFI_STATE, CHANGE_WIFI_STATE, CHANGE_NETWORK_STATE, ACCESS_FINE_LOCATION capped at API 32, RECORD_AUDIO. Location permission is for nearby discovery compatibility, not intended coordinate tracking. Actual merged manifest and denial/revocation tests required. No contacts permission declared in inspected source. Main cleartext disabled, backup disabled; not proof of network confinement or effective backup exclusion.

Direct Gradle declarations: Compose BOM 2026.09.00 (Material3, UI, foundation, tooling-preview; debug tooling), activity-compose 1.13.0, coroutines-android 1.10.2, ZXing core 3.5.4, CameraX core/camera2/lifecycle/view 1.6.2; JUnit 4.13.2 test-only. Resolved transitive tree, packaged components, notices, data behavior and SBOM not yet reviewed. No license clearance inferred.

## Verification and disclosure blockers

Exact packaged manifest/dependencies; WAN-on/off peer capture; denied permissions; actual retention/expiry/delete, reset, backup/restore, screen/keyboard and lifecycle evidence; independent protocol/security review; publisher and monitored support/privacy contact; audience/jurisdictions and live store declarations; durable approved HTTPS notice. Do not publish draft or use real private communication in tests. See PRIVACY_SECURITY_CHARTER.md; all no-ship gates remain.
