"""Source checks only: real permission revocation remains physical QA."""
from pathlib import Path
import unittest
ROOT = Path(__file__).resolve().parents[2]
OWNER = (ROOT / "app/src/debug/java/com/edenpractical/comms/audio/DebugNearbyVoiceOwner.kt").read_text()

class MicPermissionBoundary(unittest.TestCase):
    def test_permission_rechecked_at_request_grant_and_capture(self):
        for start, end in (("fun beginCapture()", "fun floorGranted()"),
                           ("fun floorGranted()", "fun floorDenied()"),
                           ("private fun startGrantedMicrophone()", "fun release()")):
            self.assertIn("!micPermitted()", OWNER.split(start, 1)[1].split(end, 1)[0])
        self.assertIn("current(ticket) && micPermitted() && allowed?.invoke() == true", OWNER)
        self.assertIn("appContext.checkSelfPermission(Manifest.permission.RECORD_AUDIO)", OWNER)

    def test_rejected_grant_releases_floor_and_resets_press(self):
        grant = OWNER.split("fun floorGranted()", 1)[1].split("fun floorDenied()", 1)[0]
        self.assertIn("pressed = false", grant)
        self.assertIn("cancelFloor?.invoke()", grant)
        self.assertLess(grant.index("!micPermitted()"), grant.index("startGrantedMicrophone()"))

if __name__ == "__main__":
    unittest.main()
