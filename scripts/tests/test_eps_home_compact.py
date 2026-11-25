from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[2] / "app/src/main/java/com/edenpractical/comms"

class EpsHomeCompactTest(unittest.TestCase):
    def test_compact_modes(self):
        main = (ROOT / "MainActivity.kt").read_text()
        home = main.split("private fun HomeScreen(", 1)[1].split("private fun NearbyScreen(", 1)[0]
        tile = main.split("private fun CompactModeTile(", 1)[1].split("private fun FieldOption(", 1)[0]
        self.assertEqual(home.count("horizontal = true"), 2)
        self.assertIn("HomeModeLayout.shouldStack(", home)
        self.assertIn("heightIn(min = if (horizontal) 64.dp else 88.dp)", tile)
        self.assertIn("Column(Modifier.weight(1f)", tile)
        self.assertIn("clickable(role = Role.Button, onClick = onClick)", tile)
        self.assertIn("SCROLL FOR MORE", main)
        self.assertIn("ButtonDefaults.textButtonColors(contentColor = supportingAccent())",
                      (ROOT / "ui/FieldDisclosures.kt").read_text())

    def test_review4_home_spacing(self):
        main = (ROOT / "MainActivity.kt").read_text()
        self.assertIn('if (page == "home") 8.dp', main)
        self.assertIn("Session-only by default.", main)
        self.assertIn("Optional local encrypted history is available after pairing.", main)
