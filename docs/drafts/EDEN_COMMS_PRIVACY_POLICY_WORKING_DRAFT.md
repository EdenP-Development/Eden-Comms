# Eden Comms — Privacy Policy Working Draft (NOT PUBLISHED)

Revised November 27, 2026. Internal product/legal draft for source checkpoint 50b506a71548be32d3c82a513f7f3bef1e7b8b45, debug internal 10049. Supersedes the November 4 phrase-only prototype description; earlier revision remains in Git history. Not a governing public policy. See [data handling register](../DATA_HANDLING_REGISTER.md) and [security charter](../PRIVACY_SECURITY_CHARTER.md). Implementation descriptions are source/design evidence only, not an independent audit or production capability claim.

## Publication blockers
- Confirm exact legal publisher, monitored privacy/support contact, audience, regions, applicable legal requirements and effective date.
- Reconcile exact non-debug release artifact, merged manifest, SDKs/transitive dependencies, actual network behavior, retention/deletion, backup and device-transfer behavior.
- Complete physical acceptance and independent security review; resolve mandatory charter gates before public functional beta.
- Select approved stable HTTPS hosting and verify public access; link only approved policy from app/listing. Verify selected store's current declarations independently.
- No invented contacts, privacy assurances, or public distribution authorization.

## Draft for review

**Publisher:** [CONFIRM LEGAL PUBLISHER]  
**Effective date:** [CONFIRM ON PUBLICATION]  
**Privacy contact:** [CONFIRM MONITORED CONTACT]  
**Policy URL:** [CONFIRM APPROVED HOSTED URL]

### 1. About Eden Comms

Eden Comms is being developed for nearby, one-to-one communication on Android. The current experimental debug build includes same-Wi-Fi, Bluetooth Classic and Wi-Fi Direct pairing, typed messages and short push-to-talk voice transmissions. These functions are development tests, not approved production services. Do not use them for confidential or emergency-critical communication. The intended scope does not require a publisher-operated account, cloud message relay, advertising or analytics.

### 2. Information used

- **Identity and pairing:** Local cryptographic identity material is intended to remain on the device; public certificate fingerprints, QR pairing values and relevant network/radio information are exchanged to establish the selected connection. Anyone who sees a QR code may see its encoded public pairing data. Nearby infrastructure and peers may observe connection metadata.
- **Messages:** Typed and received text, message identifiers and delivery-related status are processed for the conversation. A peer-app acknowledgment is not a read receipt. Session-only is the default.
- **Voice:** Microphone input and received audio are processed for explicitly initiated short voice turns and playback. The intended limit is three seconds per transmission. Voice is not intended to be archived.
- **Optional local history:** After verification, you may choose to save subsequent confirmed text on your own phone using experimental local encryption. Records may include direction, timestamps, identifiers and the verified peer fingerprint. Choices range from one hour to 30 days; session-only remains the default for each new conversation.
- **Optional remembered peer:** A separate choice retains public peer fingerprint and expiry information locally. Remembering a phone does not grant approval or bypass fresh verification.
- **Settings and diagnostics:** Appearance preferences persist locally. A local QA summary may be explicitly copied; the clipboard and any destination you select are outside the app's exclusive control.

### 3. Permissions

Camera is intended for QR scanning; network permissions support local connections and network readiness; Bluetooth and nearby Wi-Fi permissions support selected discovery/connection methods. Older Android versions may require location permission for discovery compatibility; coordinate tracking is not an intended feature. Microphone permission supports explicit voice capture in debug tests. Denial/revocation should stop affected functionality. Review actual merged manifest and OS behavior before publishing this description.

### 4. Transfers and third parties

The intended communication path is directly between selected nearby phones using an experimental authenticated TLS transport, without a publisher-operated message relay. The other participant receives the content you send. Local network/radio observers may learn metadata; recipients can copy, record or photograph content. Android, device vendors, keyboards, stores and third-party components can process data independently. Actual WAN traffic and SDK behavior require verification; no claim of zero collection, zero network traffic or anonymity is made.

### 5. Retention and controls

Session-only text and voice are intended to be temporary. Optional encrypted text history has an absolute 30-day maximum under the source policy; viewing does not extend expiry. Turning history off, deleting local history, or forgetting remembered peers affects this device, not another person's copies. The app is designed to hide expired records before display; delayed cleanup or flash residue may remain. Local identity and preferences can persist between sessions; identity reset is separate from conversation deletion. Backup and device-transfer exclusions are configured, but actual Android/OEM behavior must be tested. No guarantee of irreversible erasure or remote deletion.

### 6. Security and limitations

QR verification, bilateral approval, TLS and local encryption are experimental in this build. They have not passed independent security review and full physical acceptance. No claim of audited end-to-end security, protection from compromised phones, invisibility, or guaranteed deletion is made. No emergency-service promise.

### 7. Audience, regions and inquiries

[CONFIRM intended audience and minors policy, supported jurisdictions, legally required disclosures and rights/request handling, verified monitored contact, effective date and revision process.] A separate accurate policy is required for the exact distributed build. Store declarations and policy links must match that build.

## Stop rule

Do not publish or link this draft, submit store declarations, or treat this update as legal clearance. Current functional builds remain internal debug QA only.
