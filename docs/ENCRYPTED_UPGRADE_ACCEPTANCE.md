# EC-I08 — Encrypted upgrade acceptance contract

Status: initial process-restart instrumentation passed; full acceptance remains open. Source audited at 008d72a18ecfd341a1b74790378948a59fb5b5c2.
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
| E01 | Fresh isolated Preview identity created by explicit consent; synthetic challenge signed and verified | PARTIAL: direct test consent and signing passed; UI consent not tested |
| E02 | In-place same-signer version increase preserves public certificate fingerprint and usable key; no regeneration | PASS: isolated same-source 200001→200002 |
| E03 | Synthetic opted-in history retained with same content, direction, source ID, creation and expiry | PASS: isolated direct store fixture |
| E04 | Synthetic remembered peer retained with same original expiry and own identity | PASS: isolated direct store fixture |
| E05 | Expired history and peer records not exposed after upgrade; no read-driven renewal | PASS: isolated direct store fixtures |
| E06 | Session-only default on a new session; retained history does not restore retention selection | NOT RUN |
| E07 | Independent wrong-peer, wrong-own-pin, missing-key and corruption fixtures fail closed | PASS: isolated direct negative fixtures |
| E08 | No raw keys, plaintext, peer fingerprints or sensitive payloads in artifacts; boolean results only | NOT RUN |
| E09 | Release stubs remain disabled and no QA entrypoint in production APK | NOT RUN |

## Execution design

Stage A: inspect existing Android test infrastructure and available UI identity consent flow; implement real identity continuity first, using the same-package isolated Preview. Do not export private key material. Stage B: use test-only instrumentation exercising actual debug stores with synthetic data and controlled timestamps; explicitly distinguish direct store tests from end-to-end consent and peer re-verification tests. Do not introduce a shipped activity, broadcast receiver, bypass flag, or persistent QA command. If a two-version instrumented fixture requires new builds, record exact source, version and signer pins for both; no substitution for historical evidence. Stage C: separately establish real verified two-peer session, explicit history/remember consent and fresh authorization checks (EC-I09). Do not claim a store call establishes session authorization.

Historical Preview 200040/200043 original artifacts expire Nov 30 07:47/08:50 UTC. Preserve receipts; refresh exact inputs or retire the old automatic trigger deliberately. Existing U01–U09 evidence remains valid for its pinned pair. Do not commit APK binaries or temporary keys to Git. All emulator fixtures are disposable, with no physical devices, no reset between versions, and no public distribution. Output only pass/fail, test ID and nonsensitive scope; never dump app storage, screenshots of secrets, or raw exception payloads.

No app runtime or release feature changes authorized by this contract.

## EC-I08C actual evidence

Run [46099579809](https://github.com/EdenP-Development/Eden-Comms/actions/runs/46099579809), job 140838738160, exact source b3f22416d0ed9e433f5969480b174d8534dc1bfb: successful log lines seedIdentity: PASS and verifyIdentity: PASS. Same APK across process restarts, not upgrade. EC-I08D builds two same-source versions 200001/200002 using one disposable runner signer, verifies both and separate test APK before install, then verifies identity after in-place update and restart. No historical artifact dependency or release signer; only nonsensitive receipt uploaded. E02 passed: see receipt below.

## EC-I08D actual acceptance

[Verified receipt](evidence/identity-upgrade-200001-200002.json): run 46101049677, job 140843329337, all four cases passed. Original ZIP SHA-256 and CRC checked, receipt inspected; APK bytes not included. EC-I08E adds synthetic history seed, read before upgrade, read after upgrade and restart, and exact expiry boundary tests. No claim of live session consent or peer re-verification. E03 passed and E05 partial: see next checkpoint; E01 partial.

## EC-I08E actual acceptance

[Run evidence](evidence/identity-history-upgrade-run-46102155887.json): exact source d3093e11822dae0d4fe5cc5c1e202c0df35e155c, workflow 46102155887 job 140846787378, all nine log-reported stages passed. Artifact digest recorded from GitHub metadata; ZIP contents not independently inspected for this checkpoint. E03 passed within direct synthetic debug store scope; E05 partial (history expiration); E07 partial coverage (wrong peer lookup only). EC-I08F adds six peer-memory stages, actual local public identity binding, original expiry, no renewal, independent wrong-own-identity purge after expiry. E04 and expanded E05/E07 pending actual execution. No live authorization or production acceptance.

## EC-I08F execution discrepancy and correction

Run 46103430210 job 140850768313, source 8436b4814cc2b9ef772b7461fcd5d49b70556be0, succeeded but logs show only 13 of 15 planned method invocations. Source inspection confirms peer_upgrade and peer_restart were never called; static receipt incorrectly marked both PASS. Do not use that receipt as full acceptance. Four peer stages actually passed (seed, pre-upgrade, expiry, wrong-own-pin); all nine prior identity/history stages reran successfully. E04 remains pending direct post-upgrade reads; E05 peer expiry observed, E07 wrong-own-pin observed, other destructive cases pending. Corrected harness records only successful executions under distinct case IDs and refuses incomplete case sets. No runtime change. Repeat full suite before new destructive fixtures.

## EC-I08F.1 corrected acceptance

[Run evidence](evidence/identity-history-peer-run-46106176532.json): exact source 6a470a416865c5e8044f032514b1fa8dfbadc10b, run 46106176532 job 140859324394, all 15 distinct case IDs present in successful logs, including peer_upgrade and peer_restart. Supersedes incomplete run #6. E04/E05 pass within isolated direct debug store scope. E07 partial. EC-I08G adds four independent destructive fixtures after normal expiry/purge and a final identity signing proof. Tests flip ciphertext bytes or remove only the named debug storage AES alias, verify no disclosure or silent key recreation on read, and verify explicit new writes after missing-key loss. Never delete identity keys. Actual execution pending. No live consent or production acceptance.

## EC-I08G actual acceptance

[Evidence](evidence/encrypted-storage-run-46107109353.json): all twenty distinct case IDs passed in job 140862207612. E07 passed in isolated synthetic debug fixtures. Artifact digest from GitHub metadata; no independent ZIP inspection. EC-I08H adds unsigned release build and static manifest/DEX audit in regression CI; only report uploaded. Release stub behavior and complete E09 acceptance still require additional evidence. No capability activation or distribution.
