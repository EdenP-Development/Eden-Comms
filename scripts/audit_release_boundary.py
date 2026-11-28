"""Static inspection of an unsigned release APK; never authorizes distribution."""
import argparse
import json
import os
import re
import zipfile
import struct
from pathlib import Path
from audit_apk_identity import parse_apk_badging, source_identity, sdk_tool, tool_output, sha256

FORBIDDEN = (
    b"eden_comms_debug_history_aes_1",
    b"eden_comms_debug_peer_memory_aes_1",
    b"eden_comms_local_history_debug_v1",
    b"eden_comms_peer_memory_debug_v1",
    b"IdentityContinuityTest",
    b"edenDisposableQa",
 )
DEBUG_ACTIVITIES = (
    b"DebugBluetoothDiscoveryActivity",
    b"DebugWifiDirectPreflightActivity",
    b"DebugWifiDirectDiscoveryActivity",
    b"DebugWifiDirectGroupHostActivity",
    b"DebugWifiDirectQrActivity",
    b"DebugLocalPttActivity",
)
FORBIDDEN_PERMISSIONS = (
    "BLUETOOTH_SCAN", "BLUETOOTH_CONNECT", "BLUETOOTH_ADVERTISE",
    "NEARBY_WIFI_DEVICES", "ACCESS_FINE_LOCATION", "RECORD_AUDIO",
    "ACCESS_WIFI_STATE", "CHANGE_WIFI_STATE", "CHANGE_NETWORK_STATE",
)

def require(condition, reason):
    if not condition:
        raise ValueError(reason)

def inspect_manifest(badging, tree, expected):
    require(parse_apk_badging(badging) == expected, "Release package/version mismatch")
    require("application-debuggable" not in badging, "Debuggable application")
    require(not re.search(r"(?m)^\s*E: instrumentation\b", tree), "Instrumentation entrypoint")
    for name in ("allowBackup", "usesCleartextTraffic"):
        matches = re.findall(r"(?m)^\s*A: android:" + name + r"(?:\(0x[0-9a-fA-F]+\))?=\(type 0x12\)(0x[0-9a-fA-F]+)", tree)
        require(len(matches) == 1 and int(matches[0], 16) == 0, "Missing false manifest restriction: " + name)
    for name in ("dataExtractionRules", "fullBackupContent"):
        require(re.search(r"(?m)^\s*A: android:" + name + r"(?:\(0x[0-9a-fA-F]+\))?=@", tree), "Missing backup rule reference: " + name)
    for permission in FORBIDDEN_PERMISSIONS:
        require("android.permission." + permission not in badging, "Debug permission: " + permission)
    for token in FORBIDDEN + DEBUG_ACTIVITIES:
        require(token.decode() not in tree, "Debug manifest token")

def defined_classes(blob):
    # DEX class_defs reference type_ids, which reference string_ids.
    # Only class definitions are authoritative here, not arbitrary strings.
    require(len(blob) >= 112 and blob.startswith(b"dex\\n"), "Invalid DEX header")
    def u32(offset):
        return struct.unpack_from("<I", blob, offset)[0]
    require(u32(32) == len(blob) and u32(36) == 112 and u32(40) == 0x12345678,
            "Unsupported DEX format")
    def table(offset, stride):
        count, start = u32(offset), u32(offset + 4)
        require(start <= len(blob) and count <= (len(blob) - start) // stride,
                "Invalid DEX table")
        return count, start
    sc, so = table(56, 4)
    tc, to = table(64, 4)
    cc, co = table(96, 32)
    result = []
    for i in range(cc):
        ti = u32(co + i * 32)
        require(ti < tc, "Invalid class type index")
        si = u32(to + ti * 4)
        require(si < sc, "Invalid descriptor string index")
        pos = u32(so + si * 4)
        # Skip bounded ULEB128 UTF-16 length; descriptors are ASCII here.
        for _ in range(5):
            require(pos < len(blob), "Invalid descriptor offset")
            byte = blob[pos]
            pos += 1
            if byte < 128:
                break
        else:
            raise ValueError("Invalid descriptor length")
        end = blob.find(b"\\x00", pos)
        require(end >= pos, "Unterminated descriptor")
        result.append(blob[pos:end])
    return result

def inspect_dex(blobs):
    require(bool(blobs), "No packaged DEX")
    for blob in blobs:
        classes = defined_classes(blob)
        for token in FORBIDDEN:
            require(token not in blob, "Forbidden packaged token: " + token.decode())
        for descriptor in classes:
            for name in DEBUG_ACTIVITIES:
                require(name not in descriptor, "Forbidden defined activity: " + name.decode())

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--apk", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    source = os.environ.get("GITHUB_SHA", "")
    require(re.fullmatch(r"[0-9a-f]{40}", source), "Missing exact source revision")
    expected = source_identity(Path("app/build.gradle.kts").read_text())
    aapt = sdk_tool("aapt")
    inspect_manifest(tool_output([aapt, "dump", "badging", str(args.apk)]),
                     tool_output([aapt, "dump", "xmltree", str(args.apk), "AndroidManifest.xml"]), expected)
    with zipfile.ZipFile(args.apk) as archive:
        names = archive.namelist()
        require(len(names) == len(set(names)), "Duplicate ZIP entries")
        require(archive.testzip() is None, "APK ZIP integrity failure")
        dex = [archive.read(n) for n in names if re.fullmatch(r"classes(?:[0-9]+)?\.dex", n)]
        inspect_dex(dex)
    report = {"source_commit": source, "apk_sha256": sha256(args.apk), **expected,
              "dex_count": len(dex), "result": "PASS",
              "scope": "Static release manifest and DEX token inspection only; no signature, runtime or distribution acceptance"}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + "\n")
    print("Release boundary static inspection: PASS")

if __name__ == "__main__":
    main()
