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
        self.assertEqual(len(stages), 15)
        self.assertEqual(len({case for case, _ in stages}), 15)
        self.assertEqual({case for case, _ in stages}, qa.REQUIRED_CASES)
        self.assertIn(("peer_pre_upgrade", "verifyPeerMemory"), qa.PRE_UPGRADE)
        self.assertIn(("peer_upgrade", "verifyPeerMemory"), qa.POST_UPGRADE)
        self.assertIn(("peer_restart", "verifyPeerMemory"), qa.POST_UPGRADE)
        self.assertLess(qa.POST_UPGRADE.index(("peer_restart", "verifyPeerMemory")),
                        qa.POST_UPGRADE.index(("peer_expiry", "verifyPeerMemoryExpiry")))

