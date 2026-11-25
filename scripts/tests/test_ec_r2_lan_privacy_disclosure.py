"""Source regression only; physical UI and privacy acceptance remain open."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[2]
PANEL = (ROOT / "app/src/main/java/com/edenpractical/comms/pairing/DebugConversationPanel.kt").read_text()

class LanPrivacyDisclosure(unittest.TestCase):
    def test_composer_precedes_optional_settings(self):
        self.assertIn("var showLocalPrivacy by remember { mutableStateOf(false) }", PANEL)
        self.assertLess(PANEL.index("onClick = onSend"), PANEL.index("SHOW LOCAL PRIVACY OPTIONS"))
        self.assertLess(PANEL.index("SHOW LOCAL PRIVACY OPTIONS"), PANEL.index("Disappear on this phone"))
        self.assertIn("if (!hidden && showLocalPrivacy && confirmHistoryErase)", PANEL)
        self.assertIn("Save new messages: ", PANEL)

    def test_hidden_state_closes_transient_controls(self):
        reset = PANEL.split("LaunchedEffect(hidden) {", 1)[1].split("LaunchedEffect(scroll)", 1)[0]
        for flag in ("showLocalPrivacy", "showDisappearOptions", "showHistoryOptions", "showHistoryEntries", "confirmHistoryErase"):
            self.assertIn(flag + " = false", reset)
        self.assertIn("ConversationPrivacyButton(hidden, onToggleHidden", PANEL)
        self.assertIn("onHistoryDurationChange(choice.durationMs)", PANEL)
        self.assertIn("onHistoryErase()", PANEL)
        self.assertNotIn("rememberSaveable", PANEL)

if __name__ == "__main__":
    unittest.main()
