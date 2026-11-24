"""Regression for actual Preview emulator landscape scroll gesture.
The Home overflow hint uses a nonoverlapping reserved bottom footer.
A gesture starting at 78% height on 720px landscape hit that footer,
not the real scrollable viewport; uiautomator couldn't find Voice/PTT.
This verifies the actual driver gesture, not a phone accessibility pass.
"""
import importlib.util
from pathlib import Path
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]
DRIVER = ROOT / "scripts/emulator_visual_qa.py"


class EmulatorScrollGestureBounds(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        spec = importlib.util.spec_from_file_location("eden_visual_swipe", DRIVER)
        cls.driver = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(cls.driver)

    def test_real_driver_starts_above_footer_on_landscape_and_compact(self):
        for width, height in ((1280, 720), (720, 1280), (1080, 2340)):
            with self.subTest(size=(width, height)):
                issued = []

                def fake_adb(*args, **kwargs):
                    issued.append(args)
                    if args == ("shell", "wm", "size"):
                        return f"Physical size: {width}x{height}\n"
                    return ""

                with patch.object(self.driver, "adb", side_effect=fake_adb):
                    self.driver.swipe_up()

                self.assertEqual(len(issued), 2)
                gesture = issued[-1]
                self.assertEqual(gesture[:3], ("shell", "input", "swipe"))
                start_x, start_y, end_x, end_y = map(int, gesture[3:7])
                self.assertEqual(start_x, width // 2)
                self.assertEqual(end_x, start_x)
                self.assertGreater(start_y, end_y)
                self.assertEqual(start_y, int(height * 0.64))
                self.assertEqual(end_y, int(height * 0.30))
                # Landscape footer begins at approximately 78% of
                # total screen height; stay clearly inside content.
                self.assertLess(start_y, height * .70)
                self.assertGreater(end_y, height * .25)
                self.assertEqual(gesture[-1], "400")

    def test_preview_label_search_still_swipes_and_respects_bound(self):
        source = DRIVER.read_text()
        self.assertIn('tap("Voice / PTT", scroll=True)', source)
        self.assertIn("if scroll and scrolls < 7:", source)
        self.assertIn("swipe_up()", source)
        self.assertIn("require_emulator()", source)
        self.assertIn("Refusing non-emulator Android device", source)
        self.assertNotIn("str(int(h * .78))", source)


if __name__ == "__main__":
    unittest.main()
