#!/usr/bin/env python3
"""Test only the exact historical Preview pair on a disposable emulator."""
import argparse
import json
from pathlib import Path
import re
import subprocess
import tempfile
import emulator_visual_qa as ui
import emulator_preference_recovery as recovery
from audit_apk_identity import (parse_apk_badging, parse_signer_fingerprint,
                                sdk_tool, tool_output, sha256, compare_to_previous)

PACKAGE = recovery.PACKAGE
SIGNER = "a40da80a59d170caa950cf15c18c454d47a39b26989d8b640ecd745ba71bf5dc"
PINS = {
    200040: "8f9beac121cbc44d67f604a7b6d4ab01426f376cc34c2ef0baf1c290a80fa7a7",
    200043: "ef6a76c9ac622a76e8f1b9573e99652bd29342635784a322c63f89a6fefdad84",
}

def inspect_pinned(apk, version):
    if sha256(apk) != PINS[version]:
        raise RuntimeError("Pinned APK checksum mismatch")
    identity = parse_apk_badging(tool_output([sdk_tool("aapt"), "dump", "badging", str(apk)]))
    signer = parse_signer_fingerprint(tool_output([sdk_tool("apksigner"), "verify", "--print-certs", str(apk)]))
    if identity["application_id"] != PACKAGE or identity["version_code"] != version or signer != SIGNER:
        raise RuntimeError("Pinned Preview identity mismatch")
    return dict(identity, schema="eden-comms.debug-apk-identity.v1", signer_certificate_sha256=signer)

def installed_version():
    listing = ui.adb("shell", "dumpsys", "package", PACKAGE)
    versions = set(re.findall(r"(?m)^\s*versionCode=(\d+)\b", listing))
    if len(versions) != 1:
        raise RuntimeError("Installed version ambiguous")
    return int(versions.pop())

def require_disconnected():
    ui.launch()
    ui.seek("Not connected")
    ui.seek("No active conversation")

def require_signature_rejection(candidate):
    try:
        ui.adb("install", "-r", str(candidate), timeout=90)
    except subprocess.CalledProcessError as exc:
        diagnostic = (exc.stdout or "") + "\n" + (exc.stderr or "")
        if not re.search(r"\bINSTALL_FAILED_UPDATE_INCOMPATIBLE\b", diagnostic):
            raise AssertionError("Upgrade failed for a reason other than incompatible signature") from exc
        return
    raise AssertionError("Android accepted an incompatible signer")

def test_incompatible_signer(successor, before):
    # Re-sign only the pinned public Preview APK with a disposable test key.
    # Never access production keys or publish the temporary APK or keystore.
    with tempfile.TemporaryDirectory(prefix="eden-negative-signer-") as temp:
        directory = Path(temp)
        key = directory / "negative.p12"
        candidate = directory / "negative.apk"
        password = "disposable-test-only"
        tool_output(["keytool", "-genkeypair", "-alias", "negative", "-keyalg", "RSA",
                     "-keysize", "2048", "-validity", "2", "-dname", "CN=Disposable Preview QA",
                     "-storetype", "PKCS12", "-keystore", str(key),
                     "-storepass", password, "-keypass", password, "-noprompt"])
        tool_output([sdk_tool("apksigner"), "sign", "--ks", str(key), "--ks-key-alias", "negative",
                     "--ks-pass", "pass:" + password, "--key-pass", "pass:" + password,
                     "--out", str(candidate), str(successor)])
        identity = parse_apk_badging(tool_output([sdk_tool("aapt"), "dump", "badging", str(candidate)]))
        signer = parse_signer_fingerprint(tool_output([sdk_tool("apksigner"), "verify", "--print-certs", str(candidate)]))
        if identity["application_id"] != PACKAGE or identity["version_code"] != 200043 or signer == SIGNER:
            raise AssertionError("Negative fixture is not the expected alternate-signer Preview")
        # Equal versionCode isolates signing rejection from downgrade rejection.
        require_signature_rejection(candidate)
        if installed_version() != 200043 or recovery.read_prefs() != before:
            raise AssertionError("Existing Preview changed after rejected upgrade")
        recovery.observe("Field Green", False)
        ui.adb("shell", "am", "force-stop", PACKAGE)
        if recovery.read_prefs() != before:
            raise AssertionError("Existing preferences changed after restart")

def run(previous, successor, output):
    ui.require_emulator()
    ui.PACKAGE = PACKAGE
    ui.ACTIVITY = PACKAGE + "/com.edenpractical.comms.MainActivity"
    output.mkdir(parents=True, exist_ok=True)
    report = {"result": "INCOMPLETE", "cases": [], "package": PACKAGE,
              "previous": 200040, "successor": 200043,
              "scope": "appearance, disconnected Home and alternate-signer rejection only; no identity/history/physical acceptance"}
    def passed(case):
        report["cases"].append({"id": case, "result": "PASS"})
    owned = False
    try:
        old = inspect_pinned(previous, 200040)
        new = inspect_pinned(successor, 200043)
        passed("U01")
        compare_to_previous(new, old)
        passed("U02")
        if recovery.preview_installed():
            raise RuntimeError("Preview already installed; use fresh emulator")
        ui.adb("install", str(previous), timeout=90)
        owned = True
        if installed_version() != 200040:
            raise RuntimeError("Predecessor version not installed")
        passed("U03")
        ui.configure()
        ui.launch()
        ui.tap("Settings", scroll=True)
        ui.tap("Field Green", scroll=True)
        ui.set_dark_appearance(False)
        recovery.observe("Field Green", False)
        ui.adb("shell", "am", "force-stop", PACKAGE)
        before = recovery.read_prefs()
        passed("U04")
        ui.adb("install", "-r", str(successor), timeout=90)
        if installed_version() != 200043:
            raise RuntimeError("Successor version not installed")
        passed("U05")
        if recovery.read_prefs() != before:
            raise AssertionError("Appearance storage changed during upgrade")
        recovery.observe("Field Green", False)
        passed("U06")
        recovery.observe("Field Green", False)
        ui.adb("shell", "am", "force-stop", PACKAGE)
        if recovery.read_prefs() != before:
            raise AssertionError("Appearance storage changed after cold restart")
        passed("U07")
        require_disconnected()
        passed("U08")
        ui.adb("shell", "am", "force-stop", PACKAGE)
        test_incompatible_signer(successor, before)
        passed("U09")
        report["result"] = "PASS"
    except Exception as exc:
        report["result"] = "FAILED"
        report["failure_type"] = type(exc).__name__
        raise
    finally:
        try:
            if owned:
                ui.adb("uninstall", PACKAGE)
                ui.configure()
        finally:
            (output / "summary.json").write_text(json.dumps(report, indent=2) + "\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous", required=True, type=Path)
    parser.add_argument("--successor", required=True, type=Path)
    parser.add_argument("--out", required=True, type=Path)
    args = parser.parse_args()
    run(args.previous.resolve(), args.successor.resolve(), args.out.resolve())
