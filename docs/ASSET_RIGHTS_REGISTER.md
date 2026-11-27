# EC-B04 — Asset and dependency rights register

2026-11-27. Reviewed runtime candidate: internal 10049, source 50b506a71548be32d3c82a513f7f3bef1e7b8b45. Hub standard: [BUS-02](https://github.com/EdenP-Development/Eden-Development-Standards/blob/main/ASSET_LICENSING.md). This is an initial source inventory, not legal clearance or an exact packaged SBOM. No distribution authorization.

| Asset / source paths | Provenance and intended use | Rights status / next action |
|---|---|---|
| EPS startup PNG; generated res/drawable-nodpi/eps_v1_runtime.png | Exact hub runtime-transparent.png at ba9f28feac64d851b3b1df9d7dfd3a1e50416492; source SHA256 d144934346d77a6e04c1475dae361fc57cb28a95d7033a799bf6e2f256548516; owner accepted splash; Gradle pins and checks source before packaging | Review pending: establish creator/input/terms and authorized distribution scope; verify packaged drawable separately, preserve original and master kit |
| Product icon / storefront-master.svg; ic_eden_comms.xml, ic_eden_comms_background.xml, ic_eden_comms_foreground.xml, ic_eden_comms_monochrome.xml, mipmap-anydpi-v26/ic_launcher.xml | Owner-approved AI-assisted concept 2026-11-25; manually reconstructed native SVG/vectors, not pixel-identical; original PNG hash recorded in branding/product/v1.0/README.md, binary not archived in repo | Review pending: recover original, record provider/model if known, generation plan/terms, inputs and human edits; physical derivative and storefront raster acceptance pending; no claim of exclusive copyright |
| Other UI vectors: ic_eden_bluetooth.xml, ic_eden_chat.xml, ic_eden_info.xml, ic_eden_pairing_phones.xml, ic_eden_ptt.xml, ic_eden_radio_tower.xml, ic_eden_settings.xml, ic_eden_wifi.xml | Native XML geometry in main resources; individual origin not established by this inspection | Unknown: trace creation/history and any external icon sources, attribution or restrictions; replace only if justified and approved |
| Text, theme, layouts, source code | Repository source and Android platform theme; contribution and ownership history not reviewed | Review pending: document contributor authority and licensing decision; no top-level LICENSE/NOTICE found in inspected tree; public visibility is not permission to redistribute; do not add a project license without owner approval |
| Fonts, music, recorded effects, external datasets | No standalone font/audio/dataset asset found in inspected tree by extension; system/Compose typography and live PCM are distinct | Packaged transitive resources and generated assets still require review; no blanket absence claim |

## Direct dependency inventory

Source: app/build.gradle.kts and scripts/play_direct_dependency_baseline.txt. Versions below are declarations, not a resolved dependency graph. License metadata and notices are unverified; no legal conclusions inferred from library family.

| Dependency | Declared version / scope | Next action |
|---|---|---|
| androidx.compose:compose-bom | 2026.09.00 / platform | Resolve actual versions and inspect license metadata |
| androidx.compose.material3:material3 | BOM-managed / implementation | Resolve and review |
| androidx.compose.ui:ui | BOM-managed / implementation | Resolve and review |
| androidx.compose.foundation:foundation | BOM-managed / implementation | Resolve and review |
| androidx.compose.ui:ui-tooling-preview | BOM-managed / implementation | Resolve and review |
| androidx.activity:activity-compose | 1.13.0 / implementation | Resolve and review |
| org.jetbrains.kotlinx:kotlinx-coroutines-android | 1.10.2 / implementation | Resolve and review |
| com.google.zxing:core | 3.5.4 / implementation | Resolve and review |
| androidx.camera:camera-core, camera-camera2, camera-lifecycle, camera-view | 1.6.2 each / implementation | Resolve and review all four and transitive graph |
| androidx.compose.ui:ui-tooling | BOM-managed / debugImplementation | Debug-only declared; verify exclusion in actual release |
| junit:junit | 4.13.2 / testImplementation | Test-only declared; verify exclusion |

## Required evidence before distribution

- Resolve debug and release runtime classpaths separately and record exact graph with artifact coordinates/versions and hashes where obtainable. Build tools/plugins and test-only components remain separate. Generate a machine-readable SBOM from actual resolved artifacts and reconcile merged APK inventory; this register is not that SBOM.
- Verify upstream license text, notices, modification/redistribution obligations and vulnerabilities for exact versions; review embedded assets and transitive components; retain required notices. No new dependency or license decision authorized.
- Confirm creator and publisher authority, AI generation entitlement evidence, third-party inputs and original/master asset archives privately. Keep contracts, receipts and sensitive prompts outside public repositories.
- Screen EPS/Eden Practical Solutions and Eden Comms names/designs in intended territories and related goods/services before distribution; not searched in this checkpoint. No trademark clearance.
- Verify actual release icon exports, physical artwork and approved marketing screenshots; no new assets generated here.

All material rights questions remain open. Security charter, physical acceptance, signer recovery, durable artifact archive, exact data disclosures and owner approval remain independent mandatory gates.
