package com.edenpractical.comms.appearance
import org.junit.Assert.assertEquals
import org.junit.Test

class AppearancePreferenceTest {
    @Test fun freshAndLegacyDefaults() {
        assertEquals(AppearancePreference.EPS, AppearancePreference.resolve(null, false))
        assertEquals(AppearancePreference.FIELD, AppearancePreference.resolve(null, true))
    }
    @Test fun explicitSelectionWins() {
        assertEquals(AppearancePreference.EPS, AppearancePreference.resolve("eps_signature", true))
        assertEquals(AppearancePreference.FIELD, AppearancePreference.resolve("field_green", false))
    }
    @Test fun invalidValuesFallBackSafely() {
        assertEquals(AppearancePreference.EPS, AppearancePreference.resolve("unknown", false))
        assertEquals(AppearancePreference.FIELD, AppearancePreference.resolve("unknown", true))
    }
}
