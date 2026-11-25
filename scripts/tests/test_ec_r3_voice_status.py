"""Source checks, not physical microphone or radio evidence."""
from pathlib import Path
import unittest
ROOT = Path(__file__).resolve().parents[2] / "app/src"

class VoiceStatus(unittest.TestCase):
    def test_lan_permission_and_tap_recording(self):
        s = (ROOT / "main/java/com/edenpractical/comms/pairing/LocalPairingTestScreen.kt").read_text()
        for marker in ("micAllowed = granted", "ALLOW MICROPHONE FOR THIS TEST",
                       "enabled = micAllowed && !voiceFinalizing",
                       'talking && liveVoiceHandle != null -> "TRANSMITTING',
                       'talking -> "RECORDING', "The Android permission prompt may interrupt"):
            self.assertIn(marker, s)
    def test_nearby_pending_status_tracks_every_floor_transition(self):
        root = ROOT / "debug/java/com/edenpractical/comms/audio"
        owner = (root / "DebugNearbyVoiceOwner.kt").read_text()
        panel = (root / "DebugNearbyVoicePanel.kt").read_text()
        import re
        for m in re.finditer(r"(?m)^\s*pendingFloor = (true|false)\n", owner):
            self.assertTrue(owner[m.end():].lstrip().startswith("awaitingFloor = " + m[1]))
        self.assertIn("owner.awaitingFloor", panel)
        self.assertIn("MIC OFF", panel)
        self.assertIn("READY TO REQUEST TALK", panel)

if __name__ == "__main__":
    unittest.main()
