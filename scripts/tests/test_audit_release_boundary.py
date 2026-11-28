import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import audit_release_boundary as qa

class ReleaseBoundaryTests(unittest.TestCase):
    def test_dex(self):
        qa.inspect_dex([b"dex\nclean"])
        for token in qa.FORBIDDEN:
            with self.assertRaises(ValueError):
                qa.inspect_dex([b"dex\nclean", b"dex\n" + token])
        for bad in ([], [b"invalid"]):
            with self.assertRaises(ValueError):
                qa.inspect_dex(bad)

    def test_manifest(self):
        expected = {"application_id": "com.edenpractical.comms", "version_code": 11,
                    "version_name": "test"}
        badging = "package: name='com.edenpractical.comms' versionCode='11' versionName='test'"
        tree = ("A: android:allowBackup(0x01010280)=(type 0x12)0x0\n"
                "A: android:usesCleartextTraffic(0x010104ec)=(type 0x12)0x0\n"
                "A: android:dataExtractionRules(0x0101063e)=@0x7f010001\n"
                "A: android:fullBackupContent(0x010104eb)=@0x7f010002")
        qa.inspect_manifest(badging, tree, expected)
        for bad, xml in ((badging + "\napplication-debuggable", tree),
                         (badging + "\nuses-permission: name='android.permission.RECORD_AUDIO'", tree),
                         (badging, tree + "\nE: instrumentation"),
                         (badging, tree.replace("0x0\n", "0xffffffff\n", 1)),
                         (badging, "")):
            with self.assertRaises(ValueError):
                qa.inspect_manifest(bad, xml, expected)
