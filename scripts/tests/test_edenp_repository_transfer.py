"""Post-transfer regression: repository guards moved, security gates did not.

This is static/workflow test evidence. It does not prove that private
organization secrets exist, verify a private signer, or test hardware.
"""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[2]
ORG_REPO = "EdenP-Development/Eden-Comms"
OLD_REPO = "PlayerEden/Eden-Comms"


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


class EdenPRepositoryTransfer(unittest.TestCase):
    def test_preview_is_org_only_main_only_and_preserves_public_signer(self):
        w = read(".github/workflows/offline-preview-apk.yml")
        self.assertEqual(w.count("github.repository == '" + ORG_REPO + "'"), 2)
        self.assertNotIn("github.repository == '" + OLD_REPO + "'", w)
        self.assertIn("github.ref == 'refs/heads/main'", w)
        self.assertIn("workflow_dispatch:", w)
        self.assertIn("branches: [main]", w)
        self.assertIn("public AOSP", w)
        self.assertIn("586c1bd5cf96f9358f36b37ea98fef93f4d0a8e3", w)
        self.assertIn("e242d83e2bf72169ab0abd5280d4d455caef71eb", w)
        self.assertIn("com.edenpractical.comms.preview", w)
        self.assertIn("scripts/emulator_visual_qa.py", w)
        self.assertNotIn("${{ secrets.", w)

    def test_private_internal_signing_retains_protected_scope(self):
        w = read(".github/workflows/android-internal-test-apk.yml")
        self.assertIn('test "$GITHUB_REPOSITORY" = "' + ORG_REPO + '"', w)
        self.assertNotIn(OLD_REPO, w)
        self.assertIn('test "$GITHUB_ACTOR" = "PlayerEden"', w)
        self.assertIn('test "$GITHUB_REF" = "refs/heads/main"', w)
        self.assertIn("  workflow_dispatch:", w)
        self.assertIn("  push:\n    branches: [main]", w)
        self.assertIn("github.repository == 'EdenP-Development/Eden-Comms' && github.ref == 'refs/heads/main' && github.actor == 'PlayerEden'", w)
        for banned_trigger in ("  pull_request:", "  pull_request_target:",
                               "  workflow_run:", "  schedule:"):
            self.assertNotIn(banned_trigger, w)
        self.assertIn("environment: internal-test", w)
        self.assertIn("permissions:\n  contents: read", w)
        self.assertIn("EC_INTERNAL_KEYSTORE_BASE64", w)
        self.assertEqual(set(re.findall(r"secrets\.([A-Z0-9_]+)", w)),
                         {"EC_INTERNAL_KEYSTORE_BASE64", "EC_INTERNAL_KEYSTORE_PASSWORD"})
        self.assertIn("EC_INTERNAL_KEY_ALIAS: eden-comms-internal-test", w)
        self.assertIn("EC_INTERNAL_KEY_PASSWORD: ${{ secrets.EC_INTERNAL_KEYSTORE_PASSWORD }}", w)
        self.assertIn("signing/internal-test-cert-sha256.txt", w)
        self.assertRegex(read("signing/internal-test-cert-sha256.txt").strip(),
                         r"^[0-9a-f]{64}$")
        self.assertIn('[[ "$pin" =~ ^[0-9a-f]{64}$ ]]', w)
        self.assertIn('--expected-signer-sha256 "$EXPECTED_CERT_SHA256"', w)
        self.assertIn("--expected-signer-sha256", w)
        self.assertIn("scripts/sign_internal_test_apk.sh", w)

    def test_manual_emulator_is_not_released_on_untrusted_prs(self):
        w = read(".github/workflows/m4-ui07-manual-emulator.yml")
        self.assertIn('test "$GITHUB_REPOSITORY" = "' + ORG_REPO + '"', w)
        self.assertNotIn(OLD_REPO, w)
        self.assertIn('test "$GITHUB_REF" = "refs/heads/main"', w)
        self.assertIn("  workflow_dispatch:", w)
        self.assertNotIn("  pull_request:", w)
        self.assertNotIn("  push:", w)

    def test_owner_assisted_private_setup_keeps_never_overwrite_policy(self):
        setup = read("scripts/setup_internal_test_signing.py")
        self.assertIn('REPOSITORY = "' + ORG_REPO + '"', setup)
        self.assertNotIn('REPOSITORY = "' + OLD_REPO + '"', setup)
        self.assertIn('owner.get("login") != "PlayerEden"', setup)
        self.assertIn("Legacy uploader disabled", setup)
        self.assertNotIn('"gh", "secret", "set"', setup)
        self.assertIn("Selected deployment branch policies must contain exactly main", setup)
        self.assertIn("gh\", \"secret\", \"list", setup)
        self.assertIn("--env", setup)

    def test_identity_never_changes_to_another_game_or_prod_enabled(self):
        gradle = read("app/build.gradle.kts")
        self.assertIn('applicationId = "com.edenpractical.comms"', gradle)
        self.assertIn('applicationIdSuffix = ".preview"', gradle)
        self.assertIn('versionCode = 11', gradle)
        flags = read(
            "app/src/main/java/com/edenpractical/comms/model/ReleaseCapabilities.kt"
        )
        for name in ("CAN_CONNECT", "CAN_SEND_MESSAGES", "CAN_TRANSMIT_VOICE"):
            self.assertIn("const val " + name + " = false", flags)


if __name__ == "__main__":
    unittest.main()
