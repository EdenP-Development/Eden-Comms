import sys
import unittest
import struct
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import audit_release_boundary as qa

class ReleaseBoundaryTests(unittest.TestCase):
    @staticmethod
    def dex(descriptor=b"Lsample/Clean;", trailing=b""):
        # Minimal table fixture for class-definition traversal, not executable DEX.
        blob = bytearray(152)
        blob[:8] = b"dex\n035\x00"
        for offset, value in ((36, 112), (40, 0x12345678), (56, 1),
                              (60, 112), (64, 1), (68, 116),
                              (96, 1), (100, 120), (112, 152)):
            struct.pack_into("<I", blob, offset, value)
        blob.extend(bytes([len(descriptor)]) + descriptor + b"\x00" + trailing)
        struct.pack_into("<I", blob, 32, len(blob))
        return bytes(blob)

    def test_dex(self):
        qa.inspect_dex([self.dex()])
        for token in qa.FORBIDDEN:
            with self.assertRaises(ValueError):
                qa.inspect_dex([self.dex(), self.dex(trailing=token)])
        for token in qa.DEBUG_ACTIVITIES:
            qa.inspect_dex([self.dex(trailing=token)])
            with self.assertRaises(ValueError):
                qa.inspect_dex([self.dex(b"Lsample/" + token + b";")])
        for bad in ([], [b"invalid"], [self.dex()[:-1]]):
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
