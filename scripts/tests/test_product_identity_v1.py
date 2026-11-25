from pathlib import Path
import unittest
import xml.etree.ElementTree as ET
import math

ROOT = Path(__file__).resolve().parents[2]
DRAW = ROOT / "app/src/main/res/drawable"
A = "{http://schemas.android.com/apk/res/android}"

class ProductIdentityTest(unittest.TestCase):
    def test_layers(self):
        fg, mono, header = [ET.parse(DRAW / name).getroot() for name in (
            "ic_eden_comms_foreground.xml", "ic_eden_comms_monochrome.xml", "ic_eden_comms.xml")]
        paths = lambda root: [p.attrib[A+"pathData"] for p in root.iter("path")]
        self.assertEqual(paths(fg), paths(mono))
        self.assertEqual(paths(fg), paths(header))
        self.assertEqual({p.attrib[A+"fillColor"] for p in fg.iter("path")},
                         {"#D6A044", "#8B42BF", "#626565", "#E9E8E4"})
        self.assertEqual({p.attrib[A+"fillColor"] for p in mono.iter("path")}, {"#FFFFFF"})
        self.assertEqual(len(paths(header)), 5)
        group = fg.find("group")
        sx, sy, tx, ty = [float(group.attrib[A+k]) for k in ("scaleX","scaleY","translateX","translateY")]
        # Conservative bounding rectangle inside the nominal 66dp safe circle.
        for x in (249, 995):
            for y in (241, 998):
                self.assertLess(math.hypot(x*sx+tx-54,y*sy+ty-54), 33.1)
        self.assertIn("#111214", (DRAW/"ic_eden_comms_background.xml").read_text())
        self.assertIn("@drawable/ic_eden_comms_monochrome",
            (ROOT/"app/src/main/res/mipmap-anydpi-v26/ic_launcher.xml").read_text())
