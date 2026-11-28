"""Fresh emulator only; same-source, same-signer version increase."""
from pathlib import Path
import re
import hashlib
import json
import os
import emulator_visual_qa as ui
import emulator_preference_recovery as recovery
from audit_apk_identity import parse_apk_badging, parse_signer_fingerprint, sdk_tool, tool_output

PACKAGE = recovery.PACKAGE
TEST_PACKAGE = PACKAGE + ".test"
CLASS = "com.edenpractical.comms.security.IdentityContinuityTest"

PRE_UPGRADE = (
    ("seed", "seedIdentity"),
    ("history_seed", "seedHistory"),
    ("peer_seed", "seedPeerMemory"),
    ("restart", "verifyIdentity"),
    ("history_pre_upgrade", "verifyHistory"),
    ("peer_pre_upgrade", "verifyPeerMemory"),
)
POST_UPGRADE = (
    ("upgrade", "verifyIdentity"),
    ("history_upgrade", "verifyHistory"),
    ("peer_upgrade", "verifyPeerMemory"),
    ("post_upgrade_restart", "verifyIdentity"),
    ("history_restart", "verifyHistory"),
    ("peer_restart", "verifyPeerMemory"),
    ("session_retained_data", "verifyRetainedDataDoesNotAuthorizeModel"),
    ("session_fresh_attempt", "verifyFreshAttemptRejectsOldModelApproval"),
    ("session_decline_peer", "verifyDeclineAndDifferentPeerModel"),
    ("history_expiry", "verifyHistoryExpiry"),
    ("peer_expiry", "verifyPeerMemoryExpiry"),
    ("peer_wrong_identity", "verifyPeerMemoryWrongIdentity"),
    ("history_corruption", "verifyHistoryCorruption"),
    ("history_missing_key", "verifyHistoryMissingKey"),
    ("peer_corruption", "verifyPeerCorruption"),
    ("peer_missing_key", "verifyPeerMissingKey"),
    ("retention_storage_selection", "verifyRetentionSelectionWithEncryptedStore"),
    ("identity_after_storage_failures", "verifyIdentity"),
)
REQUIRED_CASES = frozenset({
    "seed", "history_seed", "peer_seed", "restart", "history_pre_upgrade",
    "peer_pre_upgrade", "upgrade", "history_upgrade", "peer_upgrade",
    "post_upgrade_restart", "history_restart", "peer_restart", "history_expiry",
    "peer_expiry", "peer_wrong_identity", "history_corruption",
    "history_missing_key", "peer_corruption", "peer_missing_key",
    "identity_after_storage_failures",
    "session_retained_data", "session_fresh_attempt", "session_decline_peer",
    "retention_storage_selection",
})

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

def inspect_app(apk, version):
    identity = parse_apk_badging(tool_output([sdk_tool("aapt"), "dump", "badging", str(apk)]))
    if identity["application_id"] != PACKAGE or identity["version_code"] != version:
        raise RuntimeError("Unexpected application APK identity")

def installed_version(expected):
    result = ui.adb("shell", "dumpsys", "package", PACKAGE)
    versions = set(re.findall(r"(?m)^\s*versionCode=(\d+)\b", result))
    if versions != {str(expected)}:
        raise RuntimeError("Unexpected installed version")

def run_method(method):
    result = ui.adb("shell", "am", "instrument", "-w", "-r",
                    "-e", "edenDisposableQa", "true",
                    "-e", "class", CLASS + "#" + method,
                    TEST_PACKAGE + "/androidx.test.runner.AndroidJUnitRunner", timeout=120)
    if not re.search(r"(?m)^OK \(1 test\)\s*$", result) or "FAILURES!!!" in result:
        raise RuntimeError("Instrumentation did not report exactly one passing test: " + method)
    print(method + ": PASS")
    ui.adb("shell", "am", "force-stop", PACKAGE)

def main():
    ui.require_emulator()
    source = os.environ.get("GITHUB_SHA", "")
    if not re.fullmatch(r"[0-9a-f]{40}", source):
        raise RuntimeError("Missing exact CI source")
    app = Path("qa-inputs/predecessor.apk")
    test = Path("qa-inputs/instrumentation.apk")
    successor = Path("qa-inputs/successor.apk")
    inspect_app(app, 200001)
    inspect_app(successor, 200002)
    aapt = sdk_tool("aapt")
    verify_test_manifest(
        tool_output([aapt, "dump", "badging", str(test)]),
        tool_output([aapt, "dump", "xmltree", str(test), "AndroidManifest.xml"]),
    )
    cert = signer(app)
    if cert != signer(test) or cert != signer(successor):
        raise RuntimeError("Instrumentation or successor signer mismatch")
    inventory = ui.adb("shell", "pm", "list", "packages")
    if recovery.package_installed(inventory) or "package:" + TEST_PACKAGE in inventory.splitlines():
        raise RuntimeError("Existing test installation forbidden")
    owned = []
    cases = {}
    def execute(case, method):
        if case in cases:
            raise RuntimeError("Duplicate acceptance case")
        run_method(method)
        cases[case] = "PASS"
        print(case + ": PASS")
    try:
        for apk, package in ((app, PACKAGE), (test, TEST_PACKAGE)):
            ui.adb("install", str(apk), timeout=90)
            owned.append(package)
        installed_version(200001)
        for case, method in PRE_UPGRADE:
            execute(case, method)
        ui.adb("install", "-r", str(successor), timeout=90)
        installed_version(200002)
        for case, method in POST_UPGRADE:
            execute(case, method)
    finally:
        for package in reversed(owned):
            ui.adb("uninstall", package)
    if set(cases) != REQUIRED_CASES:
        raise RuntimeError("Incomplete acceptance execution")
    receipt = {
        "source_commit": source,
        "package": PACKAGE,
        "signer_sha256": cert,
        "predecessor_version": 200001,
        "successor_version": 200002,
        "apk_sha256": {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
                       for p in (app, test, successor)},
        "result": "PASS",
        "cases": cases,
        "scope": "Same source version increment; synthetic store, retention component and independent authorization model fixtures; no live transport, UI or physical acceptance",
    }
    out = Path("qa-results/identity-upgrade.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")

if __name__ == "__main__":
    main()
