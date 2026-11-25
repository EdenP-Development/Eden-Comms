from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[2] / "app/src/main/java/com/edenpractical/comms"

class EpsSurfaceDepthTest(unittest.TestCase):
    def test_eps_only_depth_and_masthead(self):
        shared = (ROOT / "ui/FieldVisuals.kt").read_text()
        main = (ROOT / "MainActivity.kt").read_text()
        rule = shared.split("fun FieldHeaderRule()", 1)[1].split("fun FieldFrame(", 1)[0]
        self.assertIn("background(supportingAccent())", rule)
        self.assertIn("if (LocalAppearance.current == AppearancePreference.EPS)", rule)
        self.assertIn("background(actionFill())", rule)
        for source in (shared, main):
            self.assertIn("shadowElevation = if (LocalAppearance.current == AppearancePreference.EPS) 2.dp else 0.dp", source)
        self.assertIn("R.drawable.ic_eden_comms", main)
