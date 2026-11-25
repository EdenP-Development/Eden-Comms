"""Source contract only; physical permission revocation still requires testing."""
from pathlib import Path
import unittest

UI = (Path(__file__).resolve().parents[2] / "app/src/main/java/com/edenpractical/comms/pairing/LocalPairingTestScreen.kt").read_text()

class LanMicBoundary(unittest.TestCase):
    def test_grant_rechecks_before_capture(self):
        for start, end, release, capture in (
            ("fun beginLiveCaptureWithFloor(", "fun startLiveVoiceCapture(", "session.cancelUnstartedVoiceFloor()", "session.startLiveVoice()"),
            ("fun beginTapCaptureWithFloor(", "fun startVoiceCapture(", "live.cancelUnstartedVoiceFloor()", "voiceAudio.startCapture(")):
            body = UI.split(start, 1)[1].split(end, 1)[0]
            self.assertLess(body.index("if (!microphonePermitted())"), body.index(release))
            self.assertLess(body.index(release), body.index(capture))
    def test_audio_submission_checks_permission(self):
        self.assertIn("microphonePermitted() && handle.offerPcm(pcm)", UI)
        self.assertIn("if (microphonePermitted()) live.sendVoiceBurst(clip)", UI)
        self.assertIn("val result = sendGate.submitIfActive {", UI)

if __name__ == "__main__":
    unittest.main()
