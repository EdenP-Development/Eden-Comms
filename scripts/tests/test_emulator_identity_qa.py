import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import emulator_identity_qa as qa

class InstrumentationIdentityTest(unittest.TestCase):
    def test_manifest_without_version_name(self):
        badging = "package: name='com.edenpractical.comms.preview.test' versionCode='' versionName=''\n"
        manifest = '    A: android:name(0x01010003)="androidx.test.runner.AndroidJUnitRunner" (Raw: "androidx.test.runner.AndroidJUnitRunner")\n    A: android:targetPackage(0x01010021)="com.edenpractical.comms.preview"\n'
        qa.verify_test_manifest(badging, manifest)
        for bad, xml in (
            (badging.replace(".preview.test", ".test"), manifest),
            (badging + badging, manifest),
            (badging, manifest.replace(".preview", "")),
            (badging, manifest.replace("AndroidJUnitRunner", "OtherRunner")),
            (badging, manifest + manifest),
            (badging, ""),
        ):
            with self.assertRaises(RuntimeError):
                qa.verify_test_manifest(bad, xml)

    def test_stage_contract(self):
        stages = qa.PRE_UPGRADE + qa.POST_UPGRADE
        self.assertEqual(len(stages), 25)
        self.assertEqual(len({case for case, _ in stages}), 25)
        self.assertEqual({case for case, _ in stages}, qa.REQUIRED_CASES)
        self.assertIn(("peer_pre_upgrade", "verifyPeerMemory"), qa.PRE_UPGRADE)
        self.assertIn(("peer_upgrade", "verifyPeerMemory"), qa.POST_UPGRADE)
        self.assertIn(("peer_restart", "verifyPeerMemory"), qa.POST_UPGRADE)
        self.assertLess(qa.POST_UPGRADE.index(("peer_restart", "verifyPeerMemory")),
                        qa.POST_UPGRADE.index(("peer_expiry", "verifyPeerMemoryExpiry")))


        self.assertEqual(qa.POST_UPGRADE[6:9], (
            ("session_retained_data", "verifyRetainedDataDoesNotAuthorizeModel"),
            ("session_fresh_attempt", "verifyFreshAttemptRejectsOldModelApproval"),
            ("session_decline_peer", "verifyDeclineAndDifferentPeerModel"),
        ))
        self.assertEqual(qa.POST_UPGRADE[-7:], (
            ('history_corruption', 'verifyHistoryCorruption'),
            ('history_missing_key', 'verifyHistoryMissingKey'),
            ('peer_corruption', 'verifyPeerCorruption'),
            ('peer_missing_key', 'verifyPeerMissingKey'),
            ('retention_storage_selection', 'verifyRetentionSelectionWithEncryptedStore'),
            ('shared_stream_consent', 'verifySharedStreamConsent'),
            ('identity_after_storage_failures', 'verifyIdentity'),
        ))

    def test_safe_stream_failure_allowlist(self):
        self.assertEqual(qa.safe_stream_failure("secret\nEC_QA_STREAM approve_pair TLS_PIN START SSL\nprivate"),
                         "approve_pair TLS_PIN START SSL")
        self.assertIsNone(qa.safe_stream_failure("EC_QA_STREAM approve_pair PRIVATE START SSL"))
        self.assertIsNone(qa.safe_stream_failure("EC_QA_STREAM approve_pair START START SSLsecret"))
        self.assertIsNone(qa.safe_stream_failure("EC_QA_STREAM approve_pair START START SSL\nEC_QA_STREAM decline_pair START START IO"))
