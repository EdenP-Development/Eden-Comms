"""Regression contracts for the separate Android recovery harness."""
import importlib.util
from pathlib import Path
import sys
import unittest
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[2]
DRIVER = ROOT / "scripts/emulator_preference_recovery.py"

class PreferenceRecoveryTest(unittest.TestCase):
    def test_fixture_scope_and_expected_cases(self):
        sys.path.insert(0, str(DRIVER.parent))
        try:
            spec = importlib.util.spec_from_file_location("preference_recovery", DRIVER)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
        finally:
            sys.path.pop(0)
        self.assertEqual(module.PACKAGE, "com.edenpractical.comms.preview")
        for gap in (" ", "  ", "\t"):
            badging = gap.join(("package:", "name='com.edenpractical.comms.preview'", "versionCode='200041'", "versionName='0.2.12-preview-200041'"))
            self.assertEqual(module.parse_apk_badging(badging)["application_id"], module.PACKAGE)
        self.assertNotEqual(module.parse_apk_badging("package: name='com.edenpractical.comms' versionCode='11' versionName='debug'")["application_id"], module.PACKAGE)
        self.assertEqual(module.PREF, "shared_prefs/eden_comms_ui.xml")
        self.assertEqual(len(module.CASES), 5)
        for name, body, palette, dark in module.CASES:
            root = ET.fromstring(module.fixture(body))
            self.assertEqual(root.tag, "map")
            self.assertTrue(all(n.get("name") in ("appearance_palette", "dark_theme") for n in root))
        self.assertEqual(module.CASES[0][2:], ("EPS Signature", True))
        self.assertEqual(module.CASES[-1][2:], ("Field Green", True))

    def test_isolation_guards_and_independent_job(self):
        s = DRIVER.read_text()
        for token in ("ui.require_emulator()", "parse_apk_badging(badging)", "Refusing non-Preview APK",
                      "Preview APK checksum mismatch", "Preview already installed",
                      'ui.adb("install", str(apk)', 'if read_prefs() != before:',
                      'if installed:', 'ui.adb("uninstall", PACKAGE)'):
            self.assertIn(token, s)
        self.assertNotIn('ui.adb("install", "-r"', s)
        self.assertNotIn('ui.adb("shell", "pm", "clear"', s)
        w = (ROOT / ".github/workflows/offline-preview-apk.yml").read_text()
        job = w.split("  preference-recovery:", 1)[1]
        for token in ("needs: build-preview", "refs/heads/main", "recovery-preview",
                      "scripts/emulator_preference_recovery.py", "build-tools;36.0.0"):
            self.assertIn(token, job)
        self.assertNotIn("secrets.", job)

if __name__ == "__main__":
    unittest.main()
