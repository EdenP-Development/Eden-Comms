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
| E09 | Release stubs remain disabled and no QA entrypoint in production APK | PASS within static APK and targeted release JVM task scope; installed release not tested |

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

## EC-I08H first compiled inspection

CI #684 run 46108113789 built unsigned release successfully and passed manifest inspection, but raw DEX token search rejected DebugBluetoothDiscoveryActivity. Shared MainActivity contains class-name strings guarded by debug selection/FLAG_DEBUGGABLE; a name string does not establish a defined class. Revised audit traverses DEX class definitions via type/string tables for named debug activities; manifest exclusions and raw storage/test marker exclusions remain strict. Regression fixtures distinguish a string reference from a class definition and reject malformed tables. Actual revised audit pending; no runtime or release changes.

## EC-I08H compiled release acceptance

Exact main c324f86be07116e352e8b37f52327966b6c85bcb, CI #688 run 46109723772: actual unsigned release static inspection PASS and 451 Python tests passed. PR #254 CI #687 also passed. This confirms named manifest exclusions, compiled debug activity class exclusions, storage/test marker exclusions and manifest restrictions within the static audit scope. No release APK distributed. EC-I08H.2 adds three release-only JVM tests using the unmodified release stubs and mock Android ContextWrapper; valid/invalid writes, reads, retention, peer memory and erase operations must refuse or return empty. BuildConfig.DEBUG must be false. Tests are not an installed-device runtime or backup test. Actual execution pending.

## EC-I08H.2 test component correction

CI #689 run 46110116773 failed before executing release tests: testReleaseUnitTest task missing. AGP 9 defaults to only enabling the tested build type's unit-test component (debug). Set android.onlyEnableUnitTestForTheTestedBuildType=false per official AGP 9 migration notes (https://developer.android.com/build/releases/agp-9-0-0-release-notes). Tests use a constructor-free mockable Android ContextWrapper instance confined to JVM test source; Android method access remains fail-fast. No global return-default-values switch, runtime or signing changes. Actual execution pending.

## EC-I08H.2B shared test source isolation

CI #691 run 46115728820 reached release test compilation, confirming the release test component is now enabled. Compilation failed because the legacy shared test source set references debug-only classes (including DebugWifiDirectTargetLinkGate and DebugWifiDirectTcpProbe). Isolate shared Java/Kotlin test sources only during an explicit edenReleaseStubQa invocation; keep normal debug suite intact and release-only test source set enabled. Do not add debug implementation classes to release or relax production boundaries. Actual retest pending.

## EC-I09A/B — retained storage and independent authorization models

Exact main 4e712bd989f7c937ab9be4437ccf8c8d0b154548: CI #693 run 46116989169 passed release-specific JVM task and static APK inspection; instrumentation #9 run 46116989213 job 140892915919 logged all 20 required case IDs PASS. Individual release XML not inspected. EC-I09 adds three guarded instrumentation methods after peer_restart and before history_expiry, using retained synthetic records and fresh independent DebugApprovalGate/ProductionSessionAuthorization instances. Checks no automatic model approval, stale attempt rejection, fresh synthetic authenticated-channel notifications and both approvals, decline/close, wrong-peer rejection, and disabled production flags. 23 required case IDs. These independent model tests do not exercise actual adapter wiring, TLS/QR or human consent, or UI retention reset. E06 remains open, E08 remains open; live session acceptance remains open. No runtime changes. Actual new suite execution pending.

## EC-I09C/D actual model evidence and retention lifecycle

[Run evidence](evidence/session-model-run-46122387170.json): exact main 57d67004e317db50d985730d62441c411edbc5f8, run 46122387170 job 140909500830, all 23 distinct case IDs PASS. GitHub digest metadata only. Independent model tests passed with actual retained debug data present; no live TLS/consent/UI acceptance. EC-I09D introduces in-memory SessionHistorySelection actually used by LocalPairingTestScreen for fresh/confirmed/reset/explicit successful selection and save suppression. Existing stage checks and storage calls remain in UI. Four JVM tests cover new peer/same peer reset, valid choices, disappearing suppression, invalid input, defensive public-pin copies. Public pins are not secrets; old immutable copies may persist until GC; no secure erasure claim. E06 partial pending actual test execution and live session UI acceptance. No production capability changes.

## EC-I09D source guard correction

CI #696 run 46123077173 job 140911584580 compiled debug and passed JVM task and signing smoke, then failed the existing source guard (legacy inline retention variable assertions). Release checks skipped. Update the guard to require actual UI use of fresh/activate/choose/reset/maySave and the component's default, valid selection and suppression rules; keep all other storage and release checks. No further runtime changes. Retest pending.

## EC-I09D.2 regression assertion correction

CI #697 run 46123381782 passed the revised security shell guard but Python F5-A source regression errored on the removed activeHistoryPin name (451 run, one error). Preserve approval/activation/event/save ordering, callback admission, explicit choice, reset and disappearing suppression assertions against the actual integrated component and UI. No runtime change in this correction. Retest pending.

## EC-I09E — integrated retention and encrypted storage

Exact main 58fee0db51f5415a77a7b2612dda0e2ec7b4f79c Android CI #699 and private signing #86 completed successfully. Add one guarded Android instrumentation method using the same SessionHistorySelection component as the pairing screen plus actual DebugLocalHistoryStore. Independent synthetic fixture after prior destructive tests, before final identity proof. Checks session-only save refusal, successful explicit retention change, new record expiry, unchanged old expiry on lengthening, disappearing suppression through mirrored callback gate, disconnect/same-peer/different-peer reset, and distinction between fresh session-only default (preserves prior records) and explicit off (purges peer history). 24 required stages; execution pending. No actual UI callback or live consent claim. E06 remains partial, E08 open. No runtime changes.
