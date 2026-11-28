package com.edenpractical.comms.security

import android.content.pm.ApplicationInfo
import android.os.Build
import androidx.test.platform.app.InstrumentationRegistry
import org.junit.Test
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
