"""Static and mocked regression contracts; not Android upgrade evidence."""
import sys
from pathlib import Path
import unittest
import subprocess
from unittest.mock import patch
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
try:
    import emulator_preview_upgrade as upgrade
finally:
    sys.path.pop(0)

class PreviewUpgradeTest(unittest.TestCase):
    def test_exact_pinned_identity(self):
        self.assertEqual(set(upgrade.PINS), {200040, 200043})
        with patch.object(upgrade, "sha256", return_value="0"*64):
            with self.assertRaises(RuntimeError):
                upgrade.inspect_pinned(Path("unused"), 200040)
        for package, version, signer in (
            (upgrade.PACKAGE, 200040, upgrade.SIGNER),
            ("com.edenpractical.comms", 200040, upgrade.SIGNER),
            (upgrade.PACKAGE, 200043, upgrade.SIGNER),
            (upgrade.PACKAGE, 200040, "0"*64),
        ):
            with patch.object(upgrade, "sha256", return_value=upgrade.PINS[200040]), patch.object(upgrade, "sdk_tool", return_value="sdk"), patch.object(upgrade, "tool_output", return_value="unused"), patch.object(upgrade, "parse_apk_badging", return_value={"application_id":package,"version_code":version}), patch.object(upgrade, "parse_signer_fingerprint", return_value=signer):
                if (package, version, signer) == (upgrade.PACKAGE, 200040, upgrade.SIGNER):
                    self.assertEqual(upgrade.inspect_pinned(Path("unused"), 200040)["version_code"], 200040)
                else:
                    with self.assertRaises(RuntimeError):
                        upgrade.inspect_pinned(Path("unused"), 200040)

    def test_scoped_workflow_and_no_intermediate_reset(self):
        w = (ROOT / ".github/workflows/preview-upgrade-qa.yml").read_text()
        for token in ("workflow_dispatch:", "refs/heads/main", "actions: read", "15180578055", "15183588854", "sha256sum -c -", "emulator_preview_upgrade.py"):
            self.assertIn(token, w)
        self.assertIn("  push:\n    branches: [main]\n    paths:\n      - '.github/workflows/preview-upgrade-qa.yml'\n      - 'scripts/emulator_preview_upgrade.py'\n", w)
        self.assertIn("github.repository == 'EdenP-Development/Eden-Comms' && github.ref == 'refs/heads/main'", w)
        for token in ("  pull_request:", "  pull_request_target:", "  schedule:", "secrets."):
            self.assertNotIn(token, w)
        s = (ROOT / "scripts/emulator_preview_upgrade.py").read_text()
        for token in ("ui.require_emulator()", "recovery.preview_installed()", "compare_to_previous(new, old)", 'ui.adb("install", "-r", str(successor)', 'if owned:', 'ui.adb("uninstall", PACKAGE)'):
            self.assertIn(token, s)
        self.assertNotIn('"pm", "clear"', s)
        self.assertEqual(s.count('ui.adb("uninstall", PACKAGE)'), 1)
        self.assertGreater(s.index('ui.adb("uninstall", PACKAGE)'), s.index("finally:"))

    def test_signature_rejection_requires_specific_android_error(self):
        for diagnostic, accepted in (
            ("Failure [INSTALL_FAILED_UPDATE_INCOMPATIBLE: signatures do not match]", True),
            ("Failure [INSTALL_FAILED_VERSION_DOWNGRADE]", False),
            ("device offline", False),
        ):
            error = subprocess.CalledProcessError(1, ["adb"], output="", stderr=diagnostic)
            with patch.object(upgrade.ui, "adb", side_effect=error):
                if accepted:
                    upgrade.require_signature_rejection(Path("negative.apk"))
                else:
                    with self.assertRaises(AssertionError):
                        upgrade.require_signature_rejection(Path("negative.apk"))
        with patch.object(upgrade.ui, "adb", return_value="Success"):
            with self.assertRaises(AssertionError):
                upgrade.require_signature_rejection(Path("negative.apk"))
