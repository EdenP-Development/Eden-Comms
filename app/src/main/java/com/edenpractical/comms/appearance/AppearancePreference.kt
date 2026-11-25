package com.edenpractical.comms.appearance

internal enum class AppearancePreference(val stored: String, val label: String) {
    EPS("eps_signature", "EPS Signature"),
    FIELD("field_green", "Field Green");

    companion object {
        fun resolve(stored: String?, hasLegacyDarkChoice: Boolean): AppearancePreference =
            entries.firstOrNull { it.stored == stored }
                ?: if (hasLegacyDarkChoice) FIELD else EPS
    }
}
