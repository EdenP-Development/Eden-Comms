# Eden Comms — verified EdenP Development transfer receipt

**Recorded:** November 24, 2026. Source of truth: live
[EdenP-Development/Eden-Comms](https://github.com/EdenP-Development/Eden-Comms),
not an older repository redirect or earlier chat.

## Transfer and continuity

- GitHub **repository ID 1445090231** before and after transfer.
- Historical main source before fixes:
  `fb495a27ad2150a16c2aa17671ff55c21bfe6b2c`.
- **162** inherited branches, all **10** open issues including
  [#167](https://github.com/EdenP-Development/Eden-Comms/issues/167),
  and full merged PR history preserved.
- Verified ChatGPT connector read/write/admin to new repository by
  successful new branch, edits, PR #169, PR #170 and squash merges.
- No repo recreation, deletion, asset replacement, data reset, app
  identity change or production capability enablement.

## Technical verification completed

| Evidence | Verified outcome |
|---|---|
| [Org migration PR #169](https://github.com/EdenP-Development/Eden-Comms/pull/169) | Workflow exact-owner guards, mock tests, signing helper target and active links updated; merged main `75bd9d8f075c3590e9796771f68d6fc0de38dbd9` |
| [PR-head Android CI](https://github.com/EdenP-Development/Eden-Comms/actions/runs/45490337692) | **SUCCESS** |
| [Independent main CI](https://github.com/EdenP-Development/Eden-Comms/actions/runs/45490751352) | **SUCCESS** |
| [First org-hosted Preview 200015](https://github.com/EdenP-Development/Eden-Comms/actions/runs/45490751311) | Signed APK build **SUCCESS**; separate emulator job **FAILED** at Voice/PTT landscape lookup (13 real scenes saved) |
| [Observed Home layout fix #170](https://github.com/EdenP-Development/Eden-Comms/pull/170) | Overlay replaced with measured footer; PR-head Android/JVM/Python **SUCCESS**, merged main `a0952f602fa8482ecdc84a8220d4f5a7673f64f5` |
| [Main Android CI after fix](https://github.com/EdenP-Development/Eden-Comms/actions/runs/45492143260) | **SUCCESS** |
| [New Preview 200016](https://github.com/EdenP-Development/Eden-Comms/actions/runs/45492143156) | Signed APK build **SUCCESS**; latest emulator visual acceptance needs separate confirmation |

**Org Preview 200016 APK:** `com.edenpractical.comms.preview`,
`0.2.12-preview-200016`, code `200016`, exact source
`a0952f602fa8482ecdc84a8220d4f5a7673f64f5`, APK SHA-256
`0a3e10354328aec1054c06a62c49439dcd4d3ee7846ee8da041b0ed1ee77ee39`,
public-test certificate SHA-256
`a40da80a59d170caa950cf15c18c454d47a39b26989d8b640ecd745ba71bf5dc`.
[Signed artifact](https://github.com/EdenP-Development/Eden-Comms/actions/runs/45492143156/artifacts/14965554625).
The last-known pre-transfer certificate was exactly the same.
This is signing identity continuity evidence, **not** actual
installed-phone upgrade acceptance.

## Signing custody (do not confuse channels)

- **Preview**: existing stable, publicly known AOSP test certificate,
  not secure or private, signed on org CI. No private GitHub
  Actions secrets required; debug test data only.
- **Ordinary original-package debug**:
  `com.edenpractical.comms`, Gradle baseline code 11, default
  disposable CI signing; upgrade over existing instances not promised.
- **Original-package protected internal QA**: retained existing manual
  `internal-test` workflow and five `EC_INTERNAL_*` secret names.
  Guarded by exact org repository, `main`, `PlayerEden`
  authorized actor and protected environment. Original private-key
  custody, org-secret permissions, actual private signer fingerprint
  and compatible physical upgrade **UNVERIFIED**. No new key generated
  or substituted; no successful protected private-signing job asserted.
  If the owner later configures org Actions secrets, they must be
  restricted to **this repository** and privately backed up; check
  for same-named environment-secret overrides first.
- **Production**: not signed/published; `ReleaseCapabilities.CAN_CONNECT`,
  `CAN_SEND_MESSAGES` and `CAN_TRANSMIT_VOICE` stay **FALSE**.
  No independent crypto/security assessment.

The shared [APP_REGISTRY](https://github.com/EdenP-Development/Eden-Development-Standards/blob/main/APP_REGISTRY.json)
holds these **non-secret verified** channel facts. Other app records
were preserved using fresh-SHA, single-entry updates. No user
keystores/private settings/keys were copied into this public hub.

## Existing roadmap — do not restart the product

**Actual UI next:** [#167](https://github.com/EdenP-Development/Eden-Comms/issues/167)
is an observed layout bug on real emulator screenshots, not a
speculative network improvement. The Home scroll hint originally
covered Connect in landscape and Text on compact. PR #170 moves it
into a reserved footer; wait for actual new screenshots and owner
feedback before calling the issue closed.

**Actual functional next:** one consolidated
[18 cases × 3 transport two-phone acceptance](TWO_PHONE_ACCEPTANCE_MATRIX.md),
same Wi-Fi, Bluetooth and Wi-Fi Direct; real separate approvals,
Text/peer-app ACK, audible PTT and disconnect/negative cases.
Independent protocol/crypto, accessibility and backup/deletion review
are distinct release gates; **NOT RUN**.

**Continuity:** read [CONTINUE_HERE](../CONTINUE_HERE.md),
[CURRENT_HANDOFF](CURRENT_HANDOFF.md),
[Design Bible](EDEN_COMMS_DESIGN_BIBLE.md),
[full quality audit](OVERALL_QUALITY_AUDIT_2026_11_10.md),
[chronological work log](WORK_LOG.md),
and the [pre-transfer inventory](EDENP_DEVELOPMENT_INTEGRATION_2026_11_24.md).
Do not treat an expiring workflow artifact as an archival private
signing backup. No automatic itch.io or Google Play publication.
