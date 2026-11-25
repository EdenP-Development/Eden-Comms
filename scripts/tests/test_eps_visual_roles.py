from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[2]
MAIN = ROOT / "app/src/main/java/com/edenpractical/comms"

def luminance(rgb):
    values = [int(rgb[i:i+2], 16) / 255 for i in (0, 2, 4)]
    linear = [x / 12.92 if x <= .04045 else ((x + .055) / 1.055) ** 2.4 for x in values]
    return sum(a*b for a,b in zip(linear, (.2126,.7152,.0722)))

class EpsVisualRoles(unittest.TestCase):
    def test_contrast(self):
        for fg, bg in (("111214","D6A044"), ("C9A1EA","111214"), ("C9A1EA","1B1C1E"),
                       ("71349E","F4F3F0"), ("71349E","FFFFFF")):
            a,b = sorted((luminance(fg), luminance(bg)))
            self.assertGreaterEqual((b+.05)/(a+.05),4.5)
    def test_roles_are_used(self):
        ui = (MAIN / "MainActivity.kt").read_text()
        for token in ("LocalAppearance provides appearance", "containerColor = actionFill()", "contentColor = actionContent()", "EDEN PRACTICAL SOLUTIONS", "tint = supportingAccent()"):
            self.assertIn(token,ui)
        self.assertIn("else MaterialTheme.colorScheme.primary", (MAIN / "appearance/AppearanceColors.kt").read_text())
