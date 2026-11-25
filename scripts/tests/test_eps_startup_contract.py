from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[2]
MAIN = ROOT / "app/src/main/java/com/edenpractical/comms"

class EpsStartupContract(unittest.TestCase):
    def test_startup_contract(self):
        ui = (MAIN / "appearance/EpsStartup.kt").read_text()
        for token in ("EPS_FADE_MS = 250", "EPS_HOLD_MS = 2500", "0xFF111214",
                      "ContentScale.Fit", "BackHandler(visible)", "Skip startup",
                      "ValueAnimator.areAnimatorsEnabled()", "Lifecycle.Event.ON_STOP",
                      "R.drawable.eps_v1_runtime", "safeDrawingPadding()", "else content()"):
            self.assertIn(token, ui)
        for token in ("http://", "https://", "MediaPlayer", "AudioTrack"):
            self.assertNotIn(token, ui)
        self.assertIn("val showStartup = savedInstanceState == null",
                      (MAIN / "MainActivity.kt").read_text())

    def test_artwork_pin(self):
        gradle = (ROOT / "app/build.gradle.kts").read_text()
        self.assertIn("ba9f28feac64d851b3b1df9d7dfd3a1e50416492", gradle)
        self.assertIn("d144934346d77a6e04c1475dae361fc57cb28a95d7033a799bf6e2f256548516", gradle)
        self.assertIn("digest(bytes) == expected", gradle)
        self.assertIn("dependsOn(prepareEpsArtwork)", gradle)
