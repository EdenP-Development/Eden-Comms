from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[2]
UI = (ROOT / "app/src/main/java/com/edenpractical/comms/MainActivity.kt").read_text()

class AboutEps(unittest.TestCase):
    def test_about_is_local_and_truthful(self):
        settings = UI.split("private fun SettingsScreen(", 1)[1].split("private fun PrivacyFutureStatus(", 1)[0]
        for phrase in ('NavigationRow("About Eden Comms"', 'Text("Eden Practical Solutions"', 'BuildConfig.VERSION_NAME', 'Production messaging and voice remain disabled', 'Not independently security reviewed', 'showAbout = false'):
            self.assertIn(phrase, settings)
        self.assertNotIn("Spudacus", settings)
        self.assertNotIn("GridMates", settings)
        self.assertNotIn("Eden Practical LLC", settings)

if __name__ == "__main__":
    unittest.main()
