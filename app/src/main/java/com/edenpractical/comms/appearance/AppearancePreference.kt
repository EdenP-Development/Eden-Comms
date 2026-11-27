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

// Only these non-sensitive UI reads may recover from an incorrect stored type.
// The presence of a legacy dark choice remains independent of its value/type.
internal data class AppearanceSelection(val palette: AppearancePreference, val darkMode: Boolean) {
    companion object {
        fun read(
            readPalette: () -> String?,
            hasLegacyDarkChoice: Boolean,
            readDarkMode: () -> Boolean
        ): AppearanceSelection {
            val stored = try { readPalette() } catch (_: ClassCastException) { null }
            val dark = try { readDarkMode() } catch (_: ClassCastException) { true }
            return AppearanceSelection(AppearancePreference.resolve(stored, hasLegacyDarkChoice), dark)
        }
    }
}
