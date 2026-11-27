#!/usr/bin/env python3
"""Disposable emulator-only appearance recovery; never use on personal devices."""
import argparse
import json
from pathlib import Path
import shlex
import xml.etree.ElementTree as ET
import emulator_visual_qa as ui

PACKAGE = "com.edenpractical.comms.preview"
PREF = "shared_prefs/eden_comms_ui.xml"
CASES = (
    ("missing", "", "EPS Signature", True),
    ("valid", '<string name="appearance_palette">field_green</string><boolean name="dark_theme" value="false"/>', "Field Green", False),
    ("wrong-palette", '<int name="appearance_palette" value="7"/><boolean name="dark_theme" value="false"/>', "Field Green", False),
    ("wrong-dark", '<string name="appearance_palette">eps_signature</string><string name="dark_theme">bad</string>', "EPS Signature", True),
    ("both-wrong", '<int name="appearance_palette" value="7"/><string name="dark_theme">bad</string>', "Field Green", True),
)

def read_prefs():
    return ui.adb("shell", "run-as", PACKAGE, "cat", PREF)

def fixture(body):
    return '<?xml version="1.0" encoding="utf-8" standalone="yes" ?><map>' + body + '</map>'

def inject(body):
    ui.adb("shell", "am", "force-stop", PACKAGE)
    # Only this fixed Preview path and hard-coded synthetic XML are written.
    command = "mkdir -p shared_prefs && rm -f " + PREF + ".bak && printf %s " + shlex.quote(fixture(body)) + " > " + PREF
    ui.adb("shell", "run-as " + PACKAGE + " sh -c " + shlex.quote(command))
    if ET.tostring(ET.fromstring(read_prefs())) != ET.tostring(ET.fromstring(fixture(body))):
        raise AssertionError("Synthetic preference injection mismatch")
    return read_prefs()

def selected_palette(root, label):
    for node in root.iter("node"):
        if node.get("checked") != "true" and node.get("selected") != "true":
            continue
        if ui.find(node, label):
            return True
    return False

def observe(palette, dark):
    ui.launch()
    ui.tap("Settings", scroll=True)
    ui.seek(palette, scroll=True)
    if not selected_palette(ui.dump_ui(), palette):
        raise AssertionError("Expected palette not selected")
    ui.seek("Dark appearance", scroll=True)
    root = ui.dump_ui()
    try:
        switch = ui.appearance_switch(root)
    except AssertionError:
        ui.swipe_up()
        switch = ui.appearance_switch(ui.dump_ui())
    if switch.get("checked") != str(dark).lower():
        raise AssertionError("Expected dark appearance state not observed")

def run(apk, output):
    ui.require_emulator()
    ui.PACKAGE = PACKAGE
    ui.ACTIVITY = PACKAGE + "/com.edenpractical.comms.MainActivity"
    # Require a fresh disposable install: never clear or replace an existing app.
    if ui.adb("shell", "pm", "path", PACKAGE).strip():
        raise RuntimeError("Preview already installed; use a fresh disposable emulator")
    output.mkdir(parents=True, exist_ok=True)
    report = {"package": PACKAGE, "result": "INCOMPLETE", "cases": [],
              "scope": "synthetic appearance only; no physical or security acceptance"}
    installed = False
    try:
        ui.adb("install", str(apk), timeout=90)
        installed = True
        if not ui.adb("shell", "pm", "path", PACKAGE).strip():
            raise AssertionError("Expected isolated Preview package absent")
        ui.configure()
        for name, body, palette, dark in CASES:
            before = inject(body)
            for _ in range(2):
                observe(palette, dark)
                ui.adb("shell", "am", "force-stop", PACKAGE)
                if read_prefs() != before:
                    raise AssertionError("Opening app rewrote appearance preferences")
            report["cases"].append({"name": name, "result": "PASS", "restart": True, "unchanged": True})
        observe("Field Green", True)
        ui.launch()
        ui.tap("Settings", scroll=True)
        ui.tap("EPS Signature", scroll=True)
        ui.set_dark_appearance(False)
        ui.adb("shell", "am", "force-stop", PACKAGE)
        prefs = ET.fromstring(read_prefs())
        if prefs.find("string[@name='appearance_palette']").text != "eps_signature" or prefs.find("boolean[@name='dark_theme']").get("value") != "false":
            raise AssertionError("Explicit selection not persisted")
        observe("EPS Signature", False)
        report["cases"].append({"name": "explicit-recovery", "result": "PASS"})
        report["result"] = "PASS"
    except Exception as exc:
        report["result"] = "FAILED"
        report["failure_type"] = type(exc).__name__
        raise
    finally:
        try:
            if installed:
                ui.adb("uninstall", PACKAGE)
            ui.configure()
        finally:
            (output / "summary.json").write_text(json.dumps(report, indent=2) + "\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apk", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    if not args.apk.is_file():
        parser.error("APK missing")
    run(args.apk.resolve(), args.out.resolve())
