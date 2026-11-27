"""Static and mocked regression contracts; not Android upgrade evidence."""
import sys
from pathlib import Path
import unittest
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

    def test_manual_workflow_and_no_intermediate_reset(self):
        w = (ROOT / ".github/workflows/preview-upgrade-qa.yml").read_text()
        for token in ("workflow_dispatch:", "refs/heads/main", "actions: read", "15180578055", "15183588854", "sha256sum -c -", "emulator_preview_upgrade.py"):
            self.assertIn(token, w)
        for token in ("  push:", "  pull_request:", "  schedule:", "secrets."):
            self.assertNotIn(token, w)
        s = (ROOT / "scripts/emulator_preview_upgrade.py").read_text()
        for token in ("ui.require_emulator()", "recovery.preview_installed()", "compare_to_previous(new, old)", 'ui.adb("install", "-r", str(successor)', 'if owned:', 'ui.adb("uninstall", PACKAGE)'):
            self.assertIn(token, s)
        self.assertNotIn('"pm", "clear"', s)
        self.assertEqual(s.count('ui.adb("uninstall", PACKAGE)'), 1)
        self.assertGreater(s.index('ui.adb("uninstall", PACKAGE)'), s.index("finally:"))
