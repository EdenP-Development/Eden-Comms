# EC-B06 — Shared toolkit applicability and adoption

2026-11-27. Internal 10049 remains the frozen runtime test candidate (source 50b506a71548be32d3c82a513f7f3bef1e7b8b45). Review hub DEVELOPMENT_TOOLKIT.md and versioned README contracts; no blanket shared library import, security code reuse or runtime changes at this checkpoint.

| Toolkit | Eden Comms evidence / decision |
|---|---|
| EDT-01 v0.2 | Relevant to non-sensitive appearance settings only. MainActivity.kt and NearbyAppearance.kt directly call getString/getBoolean for appearance_palette/dark_theme; wrong stored types can throw before AppearancePreference.resolve. Existing pure tests cover missing/unknown values and legacy defaults, not wrong Android types. Proposed narrowly scoped follow-up: catch ClassCastException on these two explicit reads, retain presence-based legacy behavior, no writes/reset, test both entry points. Do not use generic fallback in identity, approval, retention or transport. Android adapter instrumentation remains unverified; do not import entire toolkit or change frozen candidate without a new regression checkpoint. |
| EDT-02 v0.2 | Applicable read-only preflight for exact 10048→10049 private internal APKs; independent receipt hashes/package/signer/version already recorded. Hub reports 15 mocked tests; SDK/emulator execution not verified here (workflow endpoint unavailable). Existing app signing checks are authoritative for individual builds. Do not use synthetic fixture installer on personal phones or product APKs; static checks cannot prove data preservation. |
| EDT-03 | Already follows related startup pattern locally; EPS distinct approved 250/2500/250ms, skip, silent, no replay on ordinary resume/rotation, reduced-motion bypass, decode fallback and ON_STOP dismissal in EpsStartup.kt. Preserve EPS timing instead of adopting game duration. Physical accessibility/lifecycle/performance still open. |
| EDT-04 | Local AppearanceColors.kt and NearbyAppearance.kt implement theme roles; existing visual matrix passed four theme combinations and large text. Preserve independent security semantics, no game palette import; physical contrast and accessibility remain open. |
| EDT-08 v0.1 | Read-only trusted baseline file verification is useful for archived receipts/artwork. Requires independently preserved expected manifest; does not establish authenticity, rights or APK signer. No consumer run yet; do not regenerate expected hashes from candidate. |
| EDT-09 v0.5 | Relevant to exact packaged EPS PNG only if member path and byte-preserved contract established. Gradle already pins source SHA256 and verifies cached/downloaded bytes; does not establish packaged bytes. Toolkit supports explicit PNG members and expected APK hash; AAPT2 may transform resources. Inspect actual APK and use independent master hash, not self-derived expected hash. Native XML/adaptive icon outside this verifier. No consumer run claimed. |
| EDT-05/06/07 and GridMates progression/audio/identity | Not applicable to EPS communication utility; no game engine, simulation, cosmetics, shared player data or game networking import. |

## Bounded next actions
1. Preserve exact internal 10049 and prior same-signer 10048 evidence; verify durable archive and private owner recovery (EC-B07).
2. Run read-only APK preflight and packaged artwork check only with actual independently verified artifacts and trusted tooling. Record actual executed evidence or blocker; keep private artifacts outside Git.
3. Revisit narrow EDT-01 wrong-type appearance fix as separate runtime PR if needed, with actual Android tests and new candidate receipt. Do not supersede physical candidate merely for speculative refactoring.
4. Continue physical acceptance, independent security review and production packaging gates. No shared helper grants trust, changes retention, opens a network, or overrides charter.

No toolkit execution, code import, physical acceptance or new release in this checkpoint.
