# EC-B07 — Durable recovery archive
2026-11-27. Inventory verified via Actions metadata; archive custody and byte verification NOT RUN. Internal 10049 remains frozen. No public release.

## Priority downloads (UTC expiry)
| Item | Exact artifact | ZIP SHA-256 reported by Actions | Expiry UTC |
|---|---|---|---|
| Disconnected visual evidence | [15103426213](https://github.com/EdenP-Development/Eden-Comms/actions/runs/45791275281/artifacts/15103426213) | 5f2a158c26e34c98d49889e2b9576d7a7d337bf1498b9b1384196347f7805c6c | 2026-11-28 09:30:22 |
| Isolated Preview 200038 | [15102462820](https://github.com/EdenP-Development/Eden-Comms/actions/runs/45791275281/artifacts/15102462820) | 94fa25c12f0decd7a992ac4c3c0cb34375b3be858c41246bf63063ad82c8517f | 2026-11-29 09:23:51 |
| Internal 10048 | [15098365262](https://github.com/EdenP-Development/Eden-Comms/actions/runs/45779827314/artifacts/15098365262) | c9a3e1977a6c1dd1f696a550b87c37233544970658cb699a79479867ce35791d | 2026-12-03 08:04:31 |
| Internal 10049 | [15102478507](https://github.com/EdenP-Development/Eden-Comms/actions/runs/45791275284/artifacts/15102478507) | 57da6c481390825661508bedfe623cd50a734c337d0a79db3c78b03b0e051b3a | 2026-12-03 09:23:58 |

## Owner custody and restore drill
1. Download original ZIPs while available into private off-repository storage; retain original names and separate copies on two independent encrypted storage locations. Do not publish internal or Preview builds. Preserve independent expected hashes from [receipt](evidence/internal-10049-receipt.json) and this inventory before verification. On Windows use `Get-FileHash -Algorithm SHA256 -LiteralPath 'path-to-file'` on ZIPs and extracted APKs; mismatch means quarantine, not update expected hash.
2. Inspect ZIP paths before extraction; extract to isolated directories. Record byte sizes, SHA-256 and verification date. Verify APK using Android SDK `apksigner verify --verbose --print-certs APK` and `aapt dump badging APK`. For internal 10048 and 10049 expect package com.edenpractical.comms, respective version codes, certificate SHA-256 dad2159585f8bc804c47de056bf8a2c2f546ad25893cb64e0448eb0cf8676d06. APK hashes: 10048 733ef69fff28cf9b2877e50abe22d830cd5b575a873fe943d9801cfe9be1b6dc; 10049 978f72ddfa91cb86e43618d5d3950c515ca321a619c09438e4c3e6eb99434e4e. Preview is separate package/signer; not an upgrade predecessor. EDT-02/08/09 may supplement verification, not replace signer checks.
3. Preserve source history using a fresh private mirror clone and git bundle --all; verify bundle and restore to a separate directory. Verify candidate commit 50b506a71548be32d3c82a513f7f3bef1e7b8b45 and predecessor 5fb119d11dec4eccd0ce33646cf5beb1d185cf39 exist. Preserve build tool versions, dependency locks where present, CI receipts/logs and exact pinned branding source plus master/rights provenance from hub. A bundle does not include external LFS objects or remote dependencies; separately inventory and preserve required bytes. Rebuilds are not substitutes for exact archived signed APKs.
4. Owner alone verifies existing offline signing backup and credentials, locally, using the current M2L guide; compare certificate fingerprint and prove private-key possession with a locally signed disposable test artifact. Never generate a replacement or overwrite existing secrets to test recovery. No keys, passwords, personal chats or pairing material in Git, tickets, chat or ordinary archive. Keep signing backup separate from build archive.
5. Restore a second copy to a clean location and repeat hash, package and signer checks. Record non-secret receipt of archive location label, custody, date, files, expected/observed hashes, sizes, restore result and exceptions. Never report PASS without observed evidence. If expired, mark missing; rebuilding creates a different artifact.
6. EC-B08 physical install-over remains separate: use authorized test devices and synthetic data only, preserve existing identity and history, no uninstall to bypass signer mismatch. No production capability change.

## Status
Metadata inventory complete; local downloads, independent ZIP/APK verification, actual durable storage, source/branding recovery, owner signer recovery and restore drill pending. Physical 0/54; independent security and release authorization remain open.

## EC-I03 recovery results — 2026-11-27
Seven exact original ZIPs downloaded through Actions; local SHA-256 compared to previously recorded Actions digests, ZIP CRC checked, five embedded APK hashes compared to prior CI receipts. All matched. Identity JSON read back; no independent apksigner/aapt available. All five APKs measured 17722719 bytes. Temporary working copies only; no durable owner storage, independent restore or signing-key recovery verified.

| Artifact | ZIP bytes | SHA-256 (observed = expected) |
|---|---:|---|
| Internal 10048 | 16833427 | c9a3e1977a6c1dd1f696a550b87c37233544970658cb699a79479867ce35791d |
| Internal 10049 | 16833640 | 57da6c481390825661508bedfe623cd50a734c337d0a79db3c78b03b0e051b3a |
| Internal 10059 | 16836584 | e112ba75b0dcf7b300c9631afc87b50334203d900bcbfcc2938d46bbc535ebb5 |
| Preview 200038 | 16833757 | 94fa25c12f0decd7a992ac4c3c0cb34375b3be858c41246bf63063ad82c8517f |
| Preview 200039 | 16836791 | a441567606f8e713623c3c22d07fa40f49c80967f03b1799611717fe9046e6ce |
| Visual 200038 (28 PNG) | 4568283 | 5f2a158c26e34c98d49889e2b9576d7a7d337bf1498b9b1384196347f7805c6c |
| Visual 200039 (28 PNG) | 4542700 | 985c0a842672a2c6a9e6669ebefbaa87f6b2c3b06dc85b2487c1715bc5f15da1 |

New artifact URLs/expiry and APK hashes in [10059 receipt](evidence/internal-10059-receipt.json). Preserve privately on two independent encrypted locations; rehash after transfer. Physical 0/54, qualitative visual review, source/branding restoration, independent security and release gates still open. No public distribution.
