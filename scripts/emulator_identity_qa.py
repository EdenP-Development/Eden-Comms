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

def verify_test_manifest(badging, manifest):
    # Instrumentation APKs do not necessarily declare an app versionName.
    packages = re.findall(r"(?m)^package:\s+name='([^']+)'", badging)
    if packages != [TEST_PACKAGE]:
        raise RuntimeError("Unexpected instrumentation APK package")
    # aapt xmltree exposes targetPackage as a manifest attribute.
    targets = re.findall(r'(?m)^\s*A: android:targetPackage(?:\(0x[0-9a-fA-F]+\))?="([^"]+)"', manifest)
    runners = re.findall(r'(?m)^\s*A: android:name(?:\(0x[0-9a-fA-F]+\))?="(androidx\.test\.runner\.AndroidJUnitRunner)"', manifest)
    if targets != [PACKAGE] or runners != ["androidx.test.runner.AndroidJUnitRunner"]:
        raise RuntimeError("Unexpected instrumentation target or runner")

def main():
    ui.require_emulator()
    app = Path("app/build/outputs/apk/debug/app-debug.apk")
    test = Path("app/build/outputs/apk/androidTest/debug/app-debug-androidTest.apk")
    aapt = sdk_tool("aapt")
    identity = parse_apk_badging(tool_output([aapt, "dump", "badging", str(app)]))
    if identity["application_id"] != PACKAGE or identity["version_code"] != 200001:
        raise RuntimeError("Unexpected application APK identity")
    verify_test_manifest(
        tool_output([aapt, "dump", "badging", str(test)]),
        tool_output([aapt, "dump", "xmltree", str(test), "AndroidManifest.xml"]),
    )
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
