from pathlib import Path
import unittest

MAIN = Path(__file__).resolve().parents[2] / "app/src/main/java/com/edenpractical/comms/MainActivity.kt"

class EpsConnectionVisualTest(unittest.TestCase):
    def test_method_presentation(self):
        screen = MAIN.read_text().split("private fun NearbyScreen(",1)[1].split("private fun PushToTalkScreen()",1)[0]
        for token in ("R.drawable.ic_eden_wifi", "R.drawable.ic_eden_bluetooth",
                      "R.drawable.ic_eden_pairing_phones", 'if (enabled) "TEST ONLY" else "UNAVAILABLE"',
                      "enabled = enabled", "onClick = onAction", "tint = supportingAccent()",
                      'ConnectionStatus("Not connected"', "No saved peer record can skip"):
            self.assertIn(token, screen)
        self.assertIn("OutlinedButton(", screen)
        self.assertEqual(3, screen.count("NearbyMethodCatalog.select("))
