package com.edenpractical.comms.security

import android.content.pm.ApplicationInfo
import android.os.Build
import androidx.test.platform.app.InstrumentationRegistry
import org.junit.Test
import com.edenpractical.comms.privacy.DebugLocalHistoryStore
import com.edenpractical.comms.privacy.LocalHistoryPolicy
import java.io.File
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
