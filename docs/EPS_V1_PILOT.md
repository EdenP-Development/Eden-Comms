# EPS v1.0 — Eden Comms pilot

## Current checkpoint — EPS Visual Review 2 (2026-11-25)

Owner physically reviewed internal 10015 (source c673600b0eff13134ee6546c4ab6d742f2fff190). EPS/Field Green light and dark screens observed; visual acceptance NOT granted. Owner selected concept C, Modular Comms, as the product-icon direction, not final artwork. Preserve fixed EPS publisher startup art, existing launcher until replacement accepted, app IDs/signing/data and security gates. See docs/EPS_VISUAL_REVIEW_1_FEEDBACK.md and docs/EPS_VISUAL_REFINEMENT_PLAN.md. Next VIS-01 semantic color roles and compact Home design, VIS-02 icon candidates; consolidate visual review rather than small APK churn.

Verified baseline: PR #186 merged; CI #532, exact artwork SHA-256 d144934346d77a6e04c1475dae361fc57cb28a95d7033a799bf6e2f256548516, 426 Python checks passed. Main CI 45556205473, private signing 45556203782, disconnected Preview emulator 45556203668 all passed. [Internal 10015](https://github.com/EdenP-Development/Eden-Comms/actions/runs/45556203782/artifacts/14994963791), [Preview 200022](https://github.com/EdenP-Development/Eden-Comms/actions/runs/45556203668/artifacts/14996375061). Startup physical approval, persistence, accessibility, physical 54-case acceptance, independent security and release engineering remain open. No public release.


Owner brief received November 24, 2026 (local). Sole EPS pilot; no automatic publishing or other app rollout. Central standards: https://github.com/EdenP-Development/Eden-Development-Standards/blob/main/BRAND_IDENTITY.md and branding/eps/v1.0/README.md.

## Startup contract
Exact stacked runtime PNG from central commit ba9f28feac64d851b3b1df9d7dfd3a1e50416492, blob 34ea8cebc26331bea90dabb803e0b6640e072030, SHA-256 d144934346d77a6e04c1475dae361fc57cb28a95d7033a799bf6e2f256548516. Independently verify bundled bytes; no regeneration or emblem substitution. Near-black #111214, centered aspect fit, safe areas, 250 ms fade in, 1000 ms hold, 250 ms fade out, nominal 1500 ms. Tap anywhere or Back skips; silent, reduced motion, no ordinary resume/rotation replay, offline, no extra wording. Timing subject to owner physical approval.

## Appearance contract
EPS Signature default for new installs; Field Green preserves original colors, migrate explicit legacy dark preference without resetting data. Keep light/dark selection. Shared semantic palette across Main and nearby activities; amber #D6A044, violet #8B42BF, gunmetal #626565, white #E9E8E4, black #111214. Use restrained accents, independent security/status/error semantics, contrast-safe derived colors. Settings preview and immediate local persistence; no recreation or communication interruption. Preserve product launcher icon, package, signing, protocols, permissions and release gates.

## Acceptance and handoff
Test migration, invalid preferences, persistence, contrast, large text, portrait/landscape, startup timing/skip/reduced motion/resume/rotation/offline/performance, navigation and communication regressions. Exact-head CI and signed internal QA candidate; owner physical visual approval before receipt for central branding chat. Physical two-phone and independent security gates unchanged. No claim of implementation or acceptance until evidence exists.

## Current checkpoint
Branch feature/eps-appearance-pilot, initial pure preference model committed at 1c0a545. Shared palette, selector, runtime artwork and startup still pending. About EPS attribution merged in PR #184. Keep this document, CURRENT_HANDOFF and WORK_LOG current.
