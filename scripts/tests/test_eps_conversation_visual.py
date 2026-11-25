from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[2] / "app/src"

class EpsConversationVisualTest(unittest.TestCase):
    def test_nearby_bubbles_keep_observed_status(self):
        for folder, name in (("bluetooth","DebugBluetoothTextPanel"), ("wifidirect","DebugWifiDirectTextPanel")):
            source = (ROOT / "debug/java/com/edenpractical/comms" / folder / (name + ".kt")).read_text()
            for token in ("ConversationBubble(", "outgoing = line.outgoing", "message = line.text",
                          "DebugNearbyTextUiCopy.lineStatus(line.outgoing, line.acknowledged)",
                          "DebugNearbyTextUiCopy.canSubmit(draft)", "onClick = onSend", "followNewest"):
                self.assertIn(token, source)
    def test_mode_switch_still_releases(self):
        source = (ROOT / "debug/java/com/edenpractical/comms/ui/DebugVerifiedConversationPanel.kt").read_text()
        for token in ('if (selection == "talk") onLeaveTalk()', "DisposableEffect(selection)",
                      "onClick = disconnect", "onDisconnect()", "colors = selectedColors"):
            self.assertIn(token, source)
