"""Source-level help contract; visual and physical acceptance are separate."""
from pathlib import Path
import unittest

UI = (Path(__file__).resolve().parents[2] / "app/src/main/java/com/edenpractical/comms/MainActivity.kt").read_text()

class HomeHelp(unittest.TestCase):
    def test_home_introduction_and_honest_state(self):
        home = UI.split("private fun HomeScreen(", 1)[1].split("private fun NearbyScreen(", 1)[0]
        for s in ("Nearby text and voice, without an account", "session-only by default", 'ConnectionStatus("Not connected"', "CONNECT NEARBY", "Do not send secrets"):
            self.assertIn(s, home)

    def test_help_explains_choice_recovery_and_permission(self):
        help = UI.split("private fun HelpScreen(", 1)[1].split("private fun PrivacyInfoScreen(", 1)[0]
        for s in ("Which connection should I choose?", "What if a connection stops?", "fresh QR exchange", "Both people must approve again", "does not reconnect automatically", "Can I listen without microphone permission?", "Production messaging and voice are not enabled"):
            self.assertIn(s, help)

if __name__ == "__main__":
    unittest.main()
