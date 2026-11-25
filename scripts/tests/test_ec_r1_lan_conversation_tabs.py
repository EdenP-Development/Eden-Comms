"""Source guards for EC-R1; actual phone interaction remains unverified."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[2]
SCREEN = (ROOT / "app/src/main/java/com/edenpractical/comms/pairing/LocalPairingTestScreen.kt").read_text()

class LanConversationTabs(unittest.TestCase):
    def test_session_scoped_text_default_and_explicit_cancel(self):
        demo = SCREEN.split('"demo" -> {', 1)[1].split('"result" -> {', 1)[0]
        self.assertIn("var talkSelected by remember(attemptVersion) { mutableStateOf(false) }", demo)
        self.assertIn('if (talkSelected) leaveTalk()', demo)
        self.assertIn('cancelLiveVoiceCapture()', demo)
        self.assertIn('cancelVoiceCapture()', demo)
        self.assertIn('conversationFocus.clearFocus(force = true)', demo)
        self.assertIn('conversationKeyboard?.hide()', demo)
        self.assertIn('if (!talkSelected) {', demo)
        self.assertIn('DebugConversationPanel(', demo)
        self.assertIn('DebugHoldToTalkControl(', demo)
        self.assertIn('End chat and disconnect', demo)
        self.assertIn('if (showTestTools && !talkSelected)', demo)

if __name__ == "__main__":
    unittest.main()
