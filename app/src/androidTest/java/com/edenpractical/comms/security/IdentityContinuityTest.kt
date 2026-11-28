package com.edenpractical.comms.security

import android.content.pm.ApplicationInfo
import android.os.Build
import androidx.test.platform.app.InstrumentationRegistry
import org.junit.Test
import com.edenpractical.comms.privacy.DebugLocalHistoryStore
import com.edenpractical.comms.privacy.LocalHistoryPolicy
import com.edenpractical.comms.privacy.SessionHistorySelection
import com.edenpractical.comms.privacy.DebugPeerMemoryStore
import com.edenpractical.comms.privacy.PeerMemoryPolicy
import java.io.File
import java.security.KeyStore
import java.security.SecureRandom
import java.security.Signature

/** Separate test APK only. Never invoke against a personal installation. */
class IdentityContinuityTest {
    private fun guardedContext(): android.content.Context {
        val context = InstrumentationRegistry.getInstrumentation().targetContext
        check(context.packageName == "com.edenpractical.comms.preview")
        check(context.applicationInfo.flags and ApplicationInfo.FLAG_DEBUGGABLE != 0)
        check(Build.FINGERPRINT.contains("generic", ignoreCase = true) ||
              Build.FINGERPRINT.contains("sdk_gphone", ignoreCase = true))
        check(InstrumentationRegistry.getArguments().getString("edenDisposableQa") == "true")
        return context
    }

    private fun proveSigning(identity: LocalTlsIdentity) {
        val challenge = ByteArray(32).also { SecureRandom().nextBytes(it) }
        val signed = Signature.getInstance("SHA256withECDSA").run {
            initSign(identity.privateKey)
            update(challenge)
            sign()
        }
        check(Signature.getInstance("SHA256withECDSA").run {
            initVerify(identity.certificate.publicKey)
            update(challenge)
            verify(signed)
        }) { "Synthetic challenge verification failed" }
    }

    // Synthetic store-level fixture only: no live peer or session consent claim.
    private val peer = ByteArray(32) { (it + 1).toByte() }
    private val epoch = 1_800_000_000_000L
    private val fixture = "Eden synthetic history QA"
    @Test fun seedHistory() {
        val context = guardedContext()
        val history = DebugLocalHistoryStore(context)
        val path = File(context.noBackupFilesDir, "eden_comms_local_history_debug_v1/encrypted.ec1")
        check(!path.exists())
        check(history.read(peer, epoch).isEmpty())
        check(!path.exists())
        check(history.save(peer, LocalHistoryPolicy.Direction.WRITTEN_HERE,
            71L, fixture, LocalHistoryPolicy.ONE_DAY, epoch))
        check(history.save(peer, LocalHistoryPolicy.Direction.RECEIVED_HERE,
            72L, fixture, LocalHistoryPolicy.ONE_HOUR, epoch))
        check(path.isFile)
        check(!path.readBytes().toString(Charsets.ISO_8859_1).contains(fixture))
    }

    @Test fun verifyHistory() {
        val context = guardedContext()
        val history = DebugLocalHistoryStore(context)
        val rows = history.read(peer, epoch + 60_000L)
        check(rows.size == 2)
        check(rows[0] == LocalHistoryPolicy.SavedMessage(
            LocalHistoryPolicy.Direction.WRITTEN_HERE, 71L, fixture, epoch,
            epoch + LocalHistoryPolicy.ONE_DAY))
        check(rows[1] == LocalHistoryPolicy.SavedMessage(
            LocalHistoryPolicy.Direction.RECEIVED_HERE, 72L, fixture, epoch,
            epoch + LocalHistoryPolicy.ONE_HOUR))
        check(history.read(ByteArray(32) { 99 }, epoch + 60_000L).isEmpty())
    }

    @Test fun verifyHistoryExpiry() {
        val context = guardedContext()
        val history = DebugLocalHistoryStore(context)
        val rows = history.read(peer, epoch + LocalHistoryPolicy.ONE_HOUR)
        check(rows.size == 1 && rows[0].sourceId == 71L)
        check(rows[0].expiresAtMs == epoch + LocalHistoryPolicy.ONE_DAY)
        check(history.read(peer, epoch + LocalHistoryPolicy.ONE_DAY).isEmpty())
        check(!File(context.noBackupFilesDir,
            "eden_comms_local_history_debug_v1/encrypted.ec1").exists())
    }

    private fun ownPin(): ByteArray =
        checkNotNull(AndroidKeystoreIdentity().existing()).publicFingerprint()

    private val day = PeerMemoryPolicy.ONE_DAY_MS
    private val secondPeer = ByteArray(32) { (it + 65).toByte() }
    private fun memoryPath(context: android.content.Context) =
        File(context.noBackupFilesDir, "eden_comms_peer_memory_debug_v1/peers.ec1")

    @Test fun seedPeerMemory() {
        val context = guardedContext()
        val memory = DebugPeerMemoryStore(context)
        val own = ownPin()
        check(!memoryPath(context).exists())
        check(memory.rememberedUntil(own, peer, epoch) == null)
        check(!memoryPath(context).exists())
        check(memory.remember(own, own, 1, epoch) == null)
        check(!memoryPath(context).exists())
        check(memory.remember(own, peer, 1, epoch) == epoch + day)
        check(memory.remember(own, secondPeer, 2, epoch) == epoch + 2 * day)
        val file = memoryPath(context)
        check(file.isFile)
        val bytes = file.readBytes().toString(Charsets.ISO_8859_1)
        check(!bytes.contains(peer.toString(Charsets.ISO_8859_1)))
        check(!bytes.contains(secondPeer.toString(Charsets.ISO_8859_1)))
    }

    @Test fun verifyPeerMemory() {
        val context = guardedContext()
        val memory = DebugPeerMemoryStore(context)
        val own = ownPin()
        val now = epoch + 60_000L
        check(memory.rememberedUntil(own, peer, now) == epoch + day)
        check(memory.rememberedUntil(own, secondPeer, now) == epoch + 2 * day)
        check(memory.rememberedUntil(own, ByteArray(32) { 99 }, now) == null)
        // A longer explicit choice must not extend an existing record.
        check(memory.remember(own, peer, 30, now) == epoch + day)
    }

    @Test fun verifyPeerMemoryExpiry() {
        val context = guardedContext()
        val memory = DebugPeerMemoryStore(context)
        val own = ownPin()
        check(memory.rememberedUntil(own, peer, epoch + day) == null)
        check(memory.rememberedUntil(own, secondPeer, epoch + day) == epoch + 2 * day)
        check(memory.rememberedUntil(own, secondPeer, epoch + 2 * day) == null)
        check(!memoryPath(context).exists())
    }

    @Test fun verifyPeerMemoryWrongIdentity() {
        val context = guardedContext()
        val memory = DebugPeerMemoryStore(context)
        val own = ownPin()
        // Independent fixture after expiry; wrong identity intentionally purges.
        val now = epoch + 3 * day
        check(!memoryPath(context).exists())
        check(memory.remember(own, peer, 1, now) == now + day)
        val other = own.copyOf().also { it[0] = (it[0].toInt() xor 1).toByte() }
        check(memory.rememberedUntil(other, peer, now) == null)
        check(!memoryPath(context).exists())
        check(memory.rememberedUntil(own, peer, now) == null)
    }

    private fun historyPath(context: android.content.Context) =
        File(context.noBackupFilesDir, "eden_comms_local_history_debug_v1/encrypted.ec1")

    private fun keyStore() = KeyStore.getInstance("AndroidKeyStore").apply { load(null) }
    private val historyAlias = "eden_comms_debug_history_aes_1"
    private val memoryAlias = "eden_comms_debug_peer_memory_aes_1"

    private fun corrupt(file: File) {
        val bytes = file.readBytes()
        check(bytes.size > 16)
        bytes[bytes.lastIndex] = (bytes.last().toInt() xor 1).toByte()
        file.writeBytes(bytes)
    }

    // Each negative case seeds a fresh synthetic fixture after prior expiry/purge.
    // Never delete the identity alias or touch a personal installation.
    @Test fun verifyHistoryCorruption() {
        val context = guardedContext()
        val store = DebugLocalHistoryStore(context)
        val file = historyPath(context)
        val now = epoch + 4 * day
        check(!file.exists())
        check(store.save(peer, LocalHistoryPolicy.Direction.WRITTEN_HERE,
            81L, fixture, LocalHistoryPolicy.ONE_DAY, now))
        check(store.read(peer, now).size == 1)
        corrupt(file)
        check(store.read(peer, now).isEmpty())
        check(!file.exists())
        check(store.read(peer, now).isEmpty())
    }

    @Test fun verifyHistoryMissingKey() {
        val context = guardedContext()
        val store = DebugLocalHistoryStore(context)
        val file = historyPath(context)
        val now = epoch + 5 * day
        check(!file.exists())
        check(store.save(peer, LocalHistoryPolicy.Direction.WRITTEN_HERE,
            82L, fixture, LocalHistoryPolicy.ONE_DAY, now))
        check(store.read(peer, now).size == 1)
        check(keyStore().containsAlias(historyAlias))
        keyStore().deleteEntry(historyAlias)
        check(file.isFile && !keyStore().containsAlias(historyAlias))
        check(store.read(peer, now).isEmpty())
        check(!file.exists() && !keyStore().containsAlias(historyAlias))
        check(store.save(peer, LocalHistoryPolicy.Direction.WRITTEN_HERE,
            83L, fixture, LocalHistoryPolicy.ONE_DAY, now))
        check(store.read(peer, now).single().sourceId == 83L)
        check(store.eraseAll())
    }

    @Test fun verifyPeerCorruption() {
        val context = guardedContext()
        val store = DebugPeerMemoryStore(context)
        val file = memoryPath(context)
        val own = ownPin()
        val now = epoch + 4 * day
        check(!file.exists())
        check(store.remember(own, peer, 1, now) == now + day)
        check(store.rememberedUntil(own, peer, now) == now + day)
        corrupt(file)
        check(store.rememberedUntil(own, peer, now) == null)
        check(!file.exists())
        check(store.rememberedUntil(own, peer, now) == null)
    }

    @Test fun verifyPeerMissingKey() {
        val context = guardedContext()
        val store = DebugPeerMemoryStore(context)
        val file = memoryPath(context)
        val own = ownPin()
        val now = epoch + 5 * day
        check(!file.exists())
        check(store.remember(own, peer, 1, now) == now + day)
        check(store.rememberedUntil(own, peer, now) == now + day)
        check(keyStore().containsAlias(memoryAlias))
        keyStore().deleteEntry(memoryAlias)
        check(file.isFile && !keyStore().containsAlias(memoryAlias))
        check(store.rememberedUntil(own, peer, now) == null)
        check(!file.exists() && !keyStore().containsAlias(memoryAlias))
        check(store.remember(own, secondPeer, 1, now) == now + day)
        check(store.rememberedUntil(own, peer, now) == null)
        check(store.rememberedUntil(own, secondPeer, now) == now + day)
        check(store.forgetAll())
    }


    // Existing encrypted records are deliberately present. These tests exercise
    // independent in-memory models, not a live TLS adapter or consent UI.
    private fun retainedFixture(): ByteArray {
        val ctx = guardedContext()
        val own = ownPin()
        val now = epoch + 60_000L
        check(DebugLocalHistoryStore(ctx).read(peer, now).size == 2)
        check(DebugPeerMemoryStore(ctx).rememberedUntil(own, peer, now) == epoch + day)
        return own
    }

    @Test fun verifyRetainedDataDoesNotAuthorizeModel() {
        val own = retainedFixture()
        val gate = com.edenpractical.comms.transport.DebugApprovalGate()
        val policy = ProductionSessionAuthorization()
        val phase = ProductionSessionAuthorization.Phase.AWAITING_AUTHENTICATED_CHANNEL
        check(!gate.maySendPreset() && !gate.mayWriteConfirmation())
        check(!policy.approvalModelComplete)
        checkNotNull(policy.begin(own, peer))
        check(policy.phase == phase)
        check(!policy.approvalModelComplete)
        check(!policy.maySendProductionText && !policy.mayTransmitProductionVoice)
    }

    @Test fun verifyFreshAttemptRejectsOldModelApproval() {
        val own = retainedFixture()
        val policy = ProductionSessionAuthorization()
        val transcript = ByteArray(32) { 41 }
        val first = checkNotNull(policy.begin(own, peer))
        check(policy.onAuthenticatedChannel(first, peer, transcript))
        check(policy.localApproved(first, transcript))
        check(policy.onAuthenticatedRemoteApproval(first, transcript))
        check(policy.approvalModelComplete)
        check(!policy.maySendProductionText && !policy.mayTransmitProductionVoice)
        policy.transportLost(first)
        val next = checkNotNull(policy.begin(own, peer))
        check(first != next)
        check(!policy.onAuthenticatedChannel(first, peer, transcript))
        check(!policy.localApproved(first, transcript))
        check(!policy.onAuthenticatedRemoteApproval(first, transcript))
        policy.transportLost(first)
        val freshTranscript = ByteArray(32) { 42 }
        check(policy.onAuthenticatedChannel(next, peer, freshTranscript))
        check(policy.localApproved(next, freshTranscript))
        check(!policy.approvalModelComplete)
        check(!policy.onAuthenticatedRemoteApproval(first, transcript))
        check(!policy.approvalModelComplete)
        check(policy.onAuthenticatedRemoteApproval(next, freshTranscript))
        check(policy.approvalModelComplete)
        check(!policy.maySendProductionText && !policy.mayTransmitProductionVoice)
        policy.endSession()
        check(!policy.approvalModelComplete)
    }

    @Test fun verifyDeclineAndDifferentPeerModel() {
        val own = retainedFixture()
        val gate = com.edenpractical.comms.transport.DebugApprovalGate()
        gate.localWritten()
        gate.decline()
        gate.peerObserved()
        gate.localConfirmationWritten()
        gate.peerConfirmationObserved()
        check(!gate.maySendPreset())
        gate.close()
        check(!gate.maySendPreset())
        val fresh = com.edenpractical.comms.transport.DebugApprovalGate()
        check(!fresh.maySendPreset())
        val policy = ProductionSessionAuthorization()
        val attempt = checkNotNull(policy.begin(own, secondPeer))
        check(!policy.onAuthenticatedChannel(attempt, peer, ByteArray(32) { 43 }))
        check(policy.phase == ProductionSessionAuthorization.Phase.BLOCKED)
        check(!policy.approvalModelComplete)
        check(!policy.maySendProductionText && !policy.mayTransmitProductionVoice)
    }


    // Isolated fixture after the original storage failure cases: no changes
    // to the earlier upgrade/expiry fixtures and no live consent UI claim.
    @Test fun verifyRetentionSelectionWithEncryptedStore() {
        val context = guardedContext()
        val store = DebugLocalHistoryStore(context)
        val now = epoch + 6 * day
        check(!historyPath(context).exists())
        val direction = LocalHistoryPolicy.Direction.WRITTEN_HERE
        check(store.save(peer, direction, 91L, fixture, LocalHistoryPolicy.ONE_DAY, now))
        val original = store.read(peer, now).single()
        var selection = SessionHistorySelection.fresh().activate(peer)
        check(selection.durationMs == LocalHistoryPolicy.SESSION_ONLY)
        // Mirror the pairing callback's selection gate, not the callback itself.
        fun persistIfAllowed(id: Long, disappearing: Boolean): Boolean {
            val pin = selection.peerPin() ?: return false
            if (!selection.maySave(disappearing)) return false
            return store.save(pin, direction, id, fixture, selection.durationMs, now)
        }
        check(!persistIfAllowed(92L, false))
        check(!store.save(peer, direction, 92L, fixture, selection.durationMs, now))
        check(store.read(peer, now) == listOf(original))
        check(store.changeRetention(peer, LocalHistoryPolicy.THIRTY_DAYS, now))
        selection = selection.choose(LocalHistoryPolicy.THIRTY_DAYS)
        check(persistIfAllowed(93L, false))
        check(!persistIfAllowed(94L, true))
        val retained = store.read(peer, now)
        check(retained.size == 2 && retained[0] == original)
        check(retained[1].sourceId == 93L)
        check(retained[1].expiresAtMs == now + LocalHistoryPolicy.THIRTY_DAYS)
        selection = selection.reset()
        check(selection.peerPin() == null && !persistIfAllowed(95L, false))
        selection = selection.activate(peer)
        check(selection.durationMs == LocalHistoryPolicy.SESSION_ONLY)
        check(!persistIfAllowed(96L, false))
        check(store.read(peer, now) == retained)
        selection = selection.activate(secondPeer)
        check(selection.durationMs == LocalHistoryPolicy.SESSION_ONLY)
        check(!persistIfAllowed(97L, false))
        check(store.read(secondPeer, now).isEmpty())
        check(store.read(peer, now) == retained)
        // Explicit off is different from a fresh session's default: it purges.
        selection = selection.activate(peer)
        check(store.changeRetention(peer, LocalHistoryPolicy.SESSION_ONLY, now))
        selection = selection.choose(LocalHistoryPolicy.SESSION_ONLY)
        check(!persistIfAllowed(98L, false))
        check(store.read(peer, now).isEmpty())
        check(!historyPath(context).exists())
    }

    @Test fun seedIdentity() {
        val context = guardedContext()
        val marker = File(context.noBackupFilesDir, "eden-qa-identity-fingerprint")
        check(!marker.exists())
        val store = AndroidKeystoreIdentity()
        check(store.existing() == null) { "Expected fresh disposable identity" }
        // Explicit test consent only, not proof of the production consent UI.
        val identity = store.createWithConsent()
        proveSigning(identity)
        marker.writeBytes(identity.publicFingerprint())
        check(marker.length() == 32L)
    }

    @Test fun verifyIdentity() {
        val context = guardedContext()
        val marker = File(context.noBackupFilesDir, "eden-qa-identity-fingerprint")
        check(marker.isFile && marker.length() == 32L)
        val identity = checkNotNull(AndroidKeystoreIdentity().existing()) {
            "Identity missing after transition"
        }
        check(identity.publicFingerprint().contentEquals(marker.readBytes())) {
            "Identity changed after transition"
        }
        proveSigning(identity)
    }
}
