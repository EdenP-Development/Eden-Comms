from pathlib import Path
import unittest

MAIN = Path(__file__).resolve().parents[2] / "app/src/main/java/com/edenpractical/comms/MainActivity.kt"

class EpsSettingsVisualTest(unittest.TestCase):
    def test_theme_cards_and_privacy(self):
        settings = MAIN.read_text().split("private fun SettingsScreen(",1)[1].split("private fun PrivacyFutureStatus(",1)[0]
        for token in ("selectableGroup()", "role = Role.RadioButton", "onAppearanceChange(option)",
                      "RadioButton(selected = selected, onClick = null", "sample.secondary",
                      "sample.surfaceVariant", "onValueChange = onDarkModeChange", "role = Role.Switch", "onCheckedChange = null",
                      "ConversationPrivacyContent.currentExplanation", "Conversation privacy",
                      "DebugPeerMemoryStore(settingsContext).forgetAll()", "showForgetAllPeers = true"):
            self.assertIn(token, settings)
