"""Fresh emulator only; no APK upgrade claim in this initial smoke test."""
from pathlib import Path
import re
import emulator_visual_qa as ui
import emulator_preference_recovery as recovery
from audit_apk_identity import parse_apk_badging, parse_signer_fingerprint, sdk_tool, tool_output

PACKAGE = recovery.PACKAGE
TEST_PACKAGE = PACKAGE + ".test"
CLASS = "com.edenpractical.comms.security.IdentityContinuityTest"

def signer(apk):
    return parse_signer_fingerprint(tool_output([sdk_tool("apksigner"), "verify", "--print-certs", str(apk)]))

def main():
    ui.require_emulator()
    app = Path("app/build/outputs/apk/debug/app-debug.apk")
    test = Path("app/build/outputs/apk/androidTest/debug/app-debug-androidTest.apk")
    for apk, expected in ((app, PACKAGE), (test, TEST_PACKAGE)):
        identity = parse_apk_badging(tool_output([sdk_tool("aapt"), "dump", "badging", str(apk)]))
        if identity["application_id"] != expected:
            raise RuntimeError("Unexpected APK package")
    if signer(app) != signer(test):
        raise RuntimeError("Instrumentation signer mismatch")
    inventory = ui.adb("shell", "pm", "list", "packages")
    if recovery.package_installed(inventory) or "package:" + TEST_PACKAGE in inventory.splitlines():
        raise RuntimeError("Existing test installation forbidden")
    owned = []
    try:
        for apk, package in ((app, PACKAGE), (test, TEST_PACKAGE)):
            ui.adb("install", str(apk), timeout=90)
            owned.append(package)
        for method in ("seedIdentity", "verifyIdentity"):
            result = ui.adb("shell", "am", "instrument", "-w", "-r",
                            "-e", "edenDisposableQa", "true",
                            "-e", "class", CLASS + "#" + method,
                            TEST_PACKAGE + "/androidx.test.runner.AndroidJUnitRunner", timeout=120)
            if not re.search(r"(?m)^OK \(1 test\)\s*$", result) or "FAILURES!!!" in result:
                raise RuntimeError("Instrumentation did not report exactly one passing test: " + method)
            print(method + ": PASS")
            ui.adb("shell", "am", "force-stop", PACKAGE)
    finally:
        for package in reversed(owned):
            ui.adb("uninstall", package)

if __name__ == "__main__":
    main()
