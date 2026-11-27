# Eden Comms — consolidated two-phone acceptance

**State: NOT RUN.** This is one reproducible test plan for the experimental
**debug APK**, not a claim of tested interoperability or cryptographic
security. [Continue here](../CONTINUE_HERE.md) ·
[Current handoff](CURRENT_HANDOFF.md) ·
[Work log](WORK_LOG.md).

## Candidate and installation preflight (November 27, EC-I03)

Recommended controlled QA candidate: [internal 10059](https://github.com/EdenP-Development/Eden-Comms/actions/runs/45955191768/artifacts/15178756017), source 68e81d53edc42117a93e1c7edd9d36f5a3cff915, package com.edenpractical.comms, version 0.2.12-internal-10059, APK SHA-256 057f2161caacdf5f18732b1aa1bf67f968247f602e58ade40edb4aac88c84447. See [receipt](evidence/internal-10059-receipt.json). Original archive bytes recovered and hash matched; independent SDK signature and actual device upgrade pending. Preview is separate.

Use [10049](https://github.com/EdenP-Development/Eden-Comms/actions/runs/45791275284/artifacts/15102478507) as same-signer predecessor, APK SHA-256 978f72ddfa91cb86e43618d5d3950c515ca321a619c09438e4c3e6eb99434e4e. Verify package, signer, version and exact bytes with [read-only preflight](M3B_READ_ONLY_DEVICE_UPGRADE_PREFLIGHT.md). On authorized test phones preserve non-sensitive appearance and test identity/history status; upgrade only with explicit consent. Verify persistence, expiry, no restored session/approval and fresh pairing. Never uninstall, clear data, downgrade or bypass signer mismatch. If already on 10059 use separate eligible device or mark upgrade NOT RUN. Add malformed appearance preference exercise only on disposable QA environment, not personal app data; valid settings, missing and wrong types should retain safe defaults without automatic writes. Actual Android injection pending.

Record each C01–C18 outcome independently for LAN, Bluetooth Classic and Wi-Fi Direct (54 cases). For a failure record candidate source/version, method, case, host/join role, Android major version, observed behavior and reproducibility, without messages, QR contents, audio or device identifiers. Prioritize authorization, microphone teardown, retention and disconnect failures before cosmetic issues. No result may be inferred from CI. This is preparation only; all physical cases remain NOT RUN.

## What to bring to the one consolidated test

Two physical Android phones, each with the *same verified APK revision*.
Prefer at least one Android 12+ and a second device/OEM if available.
Capture each device's Android version, debug APK **source revision and signer
fingerprint** from the existing build-evidence controls. Name them **Phone A**
and **Phone B**; do not put names, phone numbers, addresses, QR screenshots,
certificate fingerprints, private keys, message text, microphone samples or
device identifiers in shared test notes. Never use actual secrets or
emergency conversations.

Use the existing LAN **Copy this phone's test summary** on the result
screen. Bluetooth and Wi-Fi Direct now expose **Advanced: This phone's test
counts → Copy this phone's QA counts** *only after a real verified channel*.
Each report contains locally observed counts, not other phone's claims,
audible audio proof, read receipts or audit evidence. Clipboard access is
visible to Android/other apps; paste intentionally into private test notes.

For each method, start with **fresh QR exchange on both phones**, and finish
with **Disconnect on both**. Do not shortcut one device's independent
APPROVE/DECLINE. Never infer identity from a radio discovery name, a
remembered public pin or a previously copied code.

### Test-result vocabulary

- **NOT RUN**: no physical device evidence.
- **PASS**: observed on *both* specified devices with expected user behavior
  and no unexpected persistent data.
- **FAIL**: reproducible wrong behavior; preserve build/role/step and
  redacted observations in a GitHub issue.
- **BLOCKED**: environment/device/OEM/permission prevents this case; record
  reason instead of calling it a pass.
- **NOT APPLICABLE**: justified in notes, not silently skipped.

Only real-device results may change this status. Green GitHub CI, a JVM TLS
fixture, an emulator or a screenshot of a disconnected preview is **NOT PASS**.

## Single test run, three methods

| Order | Method | Phone A | Phone B | Internet/router expectation |
|---|---|---|---|---|
| 1 | Same Wi-Fi | Host | Join | Same local Wi-Fi, **internet not required** |
| 2 | Bluetooth Classic | Host | Join | Nearby Bluetooth, **no shared router** |
| 3 | Wi-Fi Direct | Group host | Group join | Direct Android Wi-Fi P2P, **no shared router** |

Repeat the real chat/voice/stop essentials after swapping Host and Join
when practical. On Wi-Fi Direct, use actual readiness/permission preflight
and verify Android temporary-group cleanup.

### Required evidence checklist per method

| ID | Action | Expected result / failure criterion |
|---|---|---|
| C01 | Open **Connect nearby** on each phone and choose same method | Method selection alone never searches, connects, records, or claims verified |
| C02 | Deny/skip a required radio, camera or microphone permission | Explicit recovery; no forced permission, hidden recording or fake connected state |
| C03 | Perform fresh bilateral in-person QR exchange | No stale QR or stored peer record can skip the proof |
| C04 | Try a wrong/expired QR or mismatched identity in a separate negative attempt | Fail closed; **no TEXT/TALK** or local-history writing before renewed real verification |
| C05 | Have just one person APPROVE; then independently DECLINE in a separate attempt | Nobody can chat or speak unless **both** approve and encrypted confirmation succeeds |
| C06 | Both approve fresh verification and enter actual conversation | Same authenticated session enables Text and Talk; no preview-only chat |
| C07 | A→B and B→A send distinct short harmless text; look for peer-app ACK | Both phones observe arrival and ACK counts. ACK is **not** a read receipt |
| C08 | On each phone hold Talk for 1–2 seconds | Live audio frames sent while held; remote speech audible and intelligible, max three seconds; floor release afterward |
| C09 | Simultaneously request Talk; then try joiner while host speaks | Only one floor owner; other mic remains OFF, gets denial/busy, no overlapping playback |
| C10 | Request Talk and release before a delayed GRANT | No late mic activation; next fresh request still works |
| C11 | While speaking, select **Text** tab; repeat with pending Talk request | Microphone/floor is stopped/canceled, no invisible transmission; Text still works afterward |
| C12 | During talk or text, background/lock/switch apps, turn off radio, or disconnect | All current microphone/speaker and active socket/session state stops; no auto-reconnect |
| C13 | Turn on optional history only *after* verified chat; choose 1h and send harmless text | Default session-only never saved; only subsequent confirmed text is locally encrypted; no voice archived |
| C14 | View history only after new fresh verified session; turn retention OFF and delete | Local history can be viewed/cleared; old QR, peer record or remote device cannot bypass verification |
| C15 | Independently opt into **Remember this phone** for 1 day then Forget, then Forget all | Only public fingerprint/expiry; no implicit approval; fresh QR/TLS/dual-consent still required |
| C16 | Disconnect, reopen, rotate device and use large-font/screen reader | State clearly describes disconnected/new session; touch targets understandable, no stale approval restored |
| C17 | Stop Wi-Fi Direct host/join then switch back to LAN and Bluetooth | Android P2P group and receiver resources cleaned; other transports not accidentally kept active |
| C18 | Copy **local QA summary** by explicit action on both phones | Counts match observed local events where applicable; report has no actual text/PCM/QR/peer identifiers |

## Additional negative and privacy passes

Use throwaway test messages/devices only. Re-run C04/C05/C10/C12 after an
interrupted handshake and after rotating/backgrounding during a QR scan.
Check identity reset and expired saved data on the SAME local device, and
that Android backup/restore does not recover debug history or peer-memory
data. Confirm a 30-day absolute maximum and that re-reading a record does
not renew its expiry. Clock rollback, flash erasure, OEM Keystore hardware
behavior and deleted ciphertext residue require **separate security/privacy
review**, not conclusions drawn from UI disappearance.

Test both voice directions with the two roles swapped. Observe actual
speech audibility and dropouts: seeing START/DATA/END or speaker-start
counters alone does **not** show that a person heard speech. Record the
point of failure for each: permissions, QR/approval, TLS ready, channel
send, remote receive, or actual speaker.

### M6-F keyboard and screen-capture addendum — NOT RUN

During the **same** C07/C11/C12/C16 acceptance session (not an extra
uncoordinated phone test), use harmless sample text and exercise the
actual approved Bluetooth and Wi-Fi Direct Text fields with the Android
keyboard open. Try a full 280-code-point emoji message, a rejected
over-limit paste, landscape rotation, enlarged font (up to 200%),
small-screen keyboard overlap and Jump to latest while reading back.
The Send and Disconnect controls must remain discoverable. When
switching Text → Talk, keyboard/focus must close and the microphone
must **not** start on its own; when switching Talk → Text,
pending/active mic floor must cancel or release. Verify a failed
local queue attempt preserves the typed draft without claiming
delivery, and any new conversation after a forced disconnect starts
with no stale queue hint.

For Bluetooth, check Android screenshot/Recents behavior in a private
local QA session: its debug QR and chat Activity now requests
`FLAG_SECURE`. **Do not collect, copy, publish or upload real
QR codes, identifiers or conversation screenshots**. Record only
`PASS / FAIL / BLOCKED / NOT RUN` and a sanitized cause. Actual
OS/OEM privacy protection remains unverified until observed. See
[M6-F source audit](M6_F_NEARBY_IME_CAPTURE_RECOVERY_AUDIT.md).

### M6-G failure/restart guidance addendum — NOT RUN

Within the **same consolidated** C02/C04/C05/C07/C12/C16/C17
session (not a new preliminary phone batch), observe the actual
Bluetooth stopped-link view after a timeout, declined human
approval, permission loss, and radio interruption. Its guidance
should say the test has ended and that **both phones must exchange
fresh QR codes and approve again**. If Bluetooth permission is
missing it should direct the user to Android's permission control.
The instructions must never reconnect by themselves.

For Wi-Fi Direct host/join, separately interrupt discovery,
authentication, and temporary group cleanup. An Android host
`CLEANING` stage must never claim the group is gone, and
`CLEANUP_UNCONFIRMED` must direct the user to check Android
Wi-Fi Direct settings. On a newly **user-started** host/search
attempt, the previous STOPPED status, message draft, queue hint
and ACKs must not reappear. New search/group formation is
**not verified chat**, which still requires QR/TLS proof and
both human approvals. Do not report the retry successful
unless actual two-phone text and user-observed voice work.
Record sanitized outcomes without QR, peer IDs, message
bodies or screenshots of sensitive screens. See
[M6-G source audit](M6_G_RECOVERY_GUIDANCE_AND_STATE_RESET_AUDIT.md).

### M6-H one-use Wi-Fi Direct three-QR proof — NOT RUN

During the **existing consolidated** C03/C04/C05/C06/C12/C17
acceptance pass, cause one harmless host-side and one joiner-side
connection failure, denial, or timeout **after** the valid three-QR
transcript was actually handed to the transport. Without creating new
codes, a second TLS request from that old transcript must be
rejected (no silently reused pins/nonces, no automatic retry).
Then have **both** phones explicitly start a new three-code
exchange and observe fresh mutual pinned TLS, both human approvals
and encrypted confirmations before text/talk. Also interrupt the
asynchronous group-info step. Never copy raw QR, identity, TLS
material or actual messages into evidence. Code/JVM CI does not
substitute for this on-device acceptance.
[Source audit](M6_H_SINGLE_USE_WIFI_DIRECT_QR_REQUEST_AUDIT.md).

### M6-I interrupted Wi-Fi Direct join callbacks — NOT RUN

During the **same** C04/C05/C07/C12/C16/C17 device acceptance session,
interrupt the Wi-Fi Direct **joiner's** pending Android connection-info
or group-info phase after the one-use three-QR request was offered.
Try background, Wi-Fi radio off, permission revocation, cancel and
link timeout in separate harmless cases. After its former group is
cleaned up, explicitly prepare a new three-QR exchange, choose the
new radio and obtain both new approvals. A *late* callback from the
old controller must not terminate or overwrite the new owner's
status, message/ACK state, voice, optional local privacy or QR
metadata. Also observe a stale callback after the old request
was already promoted into an authenticated TLS session. Record
PASS/FAIL/BLOCKED/NOT RUN without identifying the phones, QR pins,
audio, raw message bodies or sensitive screenshots. Source/JVM
callback-race tests alone are not phone acceptance.
[Source audit](M6_I_P2P_INTERRUPTED_CALLBACK_ISOLATION_AUDIT.md).

### EC-R4 microphone permission and EC-R1/R2 conversation parity — NOT RUN

Within C02/C08/C10/C11/C12/C16 on each transport, deny microphone permission, verify text remains usable, then explicitly grant and start a new verified session if Android interrupted the old one. On a disposable test device attempt permission loss while awaiting a grant and while capturing; expect no new microphone capture or audio submission after permission is observed lost, release or terminate the floor, and no stale ready state. If Android kills the app or cannot reproduce the timing, record that observation or BLOCKED rather than claiming a race was tested. For LAN also test tap-record-then-send cancellation. In C11/C13/C14 confirm Text/Talk switching preserves only intended session state, optional LAN history controls start collapsed, hide closes transient saved-history views and deletion confirmation, and disconnect remains reachable. No permission change should be required merely to receive audio. Physical evidence only.

## Recording one test case

Copy one line per test/transport/role; do not upload raw messages or QR:

| Field | Example format |
|---|---|
| Test | `Bluetooth / A-host B-join / C09` |
| APK revision | `short main SHA confirmed on BOTH devices` |
| Device context | `Android API level, general OEM/model; no hardware ID` |
| Result | `NOT RUN / PASS / FAIL / BLOCKED / N/A` |
| Observation | `Host mic on; joiner denied; other mic stayed off` |
| Evidence | `A and B local redacted QA counts; sanitized screenshots if safe` |
| Issue or follow-up | `GitHub issue/PR number, or none` |

**Release block:** completing this matrix still does not constitute an
independent security/cryptographic audit. Keep release CAN_CONNECT,
CAN_SEND_MESSAGES and CAN_TRANSMIT_VOICE **false** until hardware QA,
data-retention/restore tests, accessibility acceptance, and external
security review are resolved. Do not label test APK communication safe
for secrets or emergencies.

## Fix/retest loop

For each FAIL or BLOCKED item: open a narrowly scoped GitHub issue with
method, roles, APK commit, symptom, expected behavior and **redacted**
evidence. Repair in a focused PR, require Android/JVM/security CI, retest
the failed case plus C04/C05/C08/C11/C12 and the original method's C07,
and update the work log. Prefer reusing the same verified APK/version across
both phones; do not mix debug and release package or signing identity.

### EC-R6–R9 reliability addendum — NOT RUN

Within the existing C07/C08/C09/C10/C11/C12/C16/C17 cases on each method, exercise rapid disconnect/reconnect, concurrent messages, peer ACK versus local write labeling, released or expired talk requests, microphone/speaker startup cancellation and repeated turns. Use harmless content. Verify no stale session can affect the new session, no automatic resend/reconnect, no unexpected microphone or speaker activity after cancellation, and no controls stuck busy. Note cancellation latency and OEM-specific behavior without claiming precise timing unless measured. Stop on unexpected microphone activity, approval bypass or retention; preserve redacted observations. JVM queue tests are not physical connection cycles. Review runtime resource usage separately if instrumentation is available. All 54 physical outcomes remain NOT RUN.
