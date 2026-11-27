# EC-I08 — Encrypted upgrade acceptance contract

Status: design only; every test below NOT RUN. Source audited at 008d72a18ecfd341a1b74790378948a59fb5b5c2.
Prior evidence: EC-I05 6/6 and EC-I06/07 U01–U09 passed on isolated Preview. Original internal 10062 remains recommended; physical 0/54; NO-SHIP.

## Source boundaries

- AndroidKeystoreIdentity.kt: existing() never creates keys; createWithConsent() retains existing identity. v1/v2 alias migration requires explicit consent and changes fingerprint. No private-key export. Test stable public fingerprint AND signing of a synthetic challenge, not just existence of a certificate. Never migrate or reset identity as part of an ordinary upgrade.
- DebugLocalHistoryStore.kt (debug): AES-256-GCM key, package-bound AAD, noBackupFilesDir, opt-in writes, read only for reverified peer at UI boundary. Reads can rewrite encrypted bytes to persist clock/purges; compare semantic rows and expiry, NOT ciphertext equality after reads.
- DebugPeerMemoryStore.kt (debug): separate AES key/AAD/storage, bound to own public pin. Expiry cannot be extended by reads or repeated save; never a trust or authorization source. Wrong own pin can purge store, so destructive negative cases require independent fixtures.
- LocalHistoryPolicy.kt: session-only default per new session, no inherited retention choice; max 30 days, 64 records per peer, 8 peers; no renewal by read. PeerMemoryPolicy.kt delegates max age to PeerTrustExpiry; do not assume history choices apply to peer memory. Both policies tolerate at most 60 seconds of backward clock jitter.
- Release variants of both stores are no-op stubs. Debug acceptance does not authorize enabling release persistence.

## Proposed automated acceptance

| ID | Required observation | Status |
|---|---|---|
| E01 | Fresh isolated Preview identity created by explicit consent; synthetic challenge signed and verified | NOT RUN |
| E02 | In-place same-signer version increase preserves public certificate fingerprint and usable key; no regeneration | NOT RUN |
| E03 | Synthetic opted-in history retained with same content, direction, source ID, creation and expiry | NOT RUN |
| E04 | Synthetic remembered peer retained with same original expiry and own identity | NOT RUN |
| E05 | Expired history and peer records not exposed after upgrade; no read-driven renewal | NOT RUN |
| E06 | Session-only default on a new session; retained history does not restore retention selection | NOT RUN |
| E07 | Independent wrong-peer, wrong-own-pin, missing-key and corruption fixtures fail closed | NOT RUN |
| E08 | No raw keys, plaintext, peer fingerprints or sensitive payloads in artifacts; boolean results only | NOT RUN |
| E09 | Release stubs remain disabled and no QA entrypoint in production APK | NOT RUN |

## Execution design

Stage A: inspect existing Android test infrastructure and available UI identity consent flow; implement real identity continuity first, using the same-package isolated Preview. Do not export private key material. Stage B: use test-only instrumentation exercising actual debug stores with synthetic data and controlled timestamps; explicitly distinguish direct store tests from end-to-end consent and peer re-verification tests. Do not introduce a shipped activity, broadcast receiver, bypass flag, or persistent QA command. If a two-version instrumented fixture requires new builds, record exact source, version and signer pins for both; no substitution for historical evidence. Stage C: separately establish real verified two-peer session, explicit history/remember consent and fresh authorization checks (EC-I09). Do not claim a store call establishes session authorization.

Historical Preview 200040/200043 original artifacts expire Nov 30 07:47/08:50 UTC. Preserve receipts; refresh exact inputs or retire the old automatic trigger deliberately. Existing U01–U09 evidence remains valid for its pinned pair. Do not commit APK binaries or temporary keys to Git. All emulator fixtures are disposable, with no physical devices, no reset between versions, and no public distribution. Output only pass/fail, test ID and nonsensitive scope; never dump app storage, screenshots of secrets, or raw exception payloads.

No app runtime or release feature changes authorized by this contract.
