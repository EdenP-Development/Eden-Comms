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

    @Test fun validAndMissingReadsPreserveDefaults() {
        assertEquals(AppearanceSelection(AppearancePreference.EPS, true),
            AppearanceSelection.read({ null }, false, { true }))
        assertEquals(AppearanceSelection(AppearancePreference.FIELD, false),
            AppearanceSelection.read({ null }, true, { false }))
        for (palette in AppearancePreference.entries) {
            for (dark in listOf(false, true)) {
                assertEquals(AppearanceSelection(palette, dark),
                    AppearanceSelection.read({ palette.stored }, true, { dark }))
            }
        }
    }

    @Test fun wrongPaletteTypePreservesValidDarkChoiceAndMigration() {
        assertEquals(AppearanceSelection(AppearancePreference.FIELD, false),
            AppearanceSelection.read({ throw ClassCastException() }, true, { false }))
        assertEquals(AppearanceSelection(AppearancePreference.EPS, true),
            AppearanceSelection.read({ throw ClassCastException() }, false, { true }))
    }

    @Test fun wrongDarkTypePreservesExplicitPalette() {
        for (palette in AppearancePreference.entries) {
            assertEquals(AppearanceSelection(palette, true),
                AppearanceSelection.read({ palette.stored }, true, { throw ClassCastException() }))
        }
    }

    @Test fun bothWrongTypesRetainLegacyPresenceRule() {
        assertEquals(AppearanceSelection(AppearancePreference.FIELD, true),
            AppearanceSelection.read({ throw ClassCastException() }, true, { throw ClassCastException() }))
    }

    @Test fun unknownPaletteWithWrongDarkTypeUsesLegacyDefault() {
        assertEquals(AppearanceSelection(AppearancePreference.FIELD, true),
            AppearanceSelection.read({ "unknown" }, true, { throw ClassCastException() }))
    }

    @Test(expected = IllegalStateException::class)
    fun unrelatedPaletteFailureIsNotSwallowed() {
        AppearanceSelection.read({ throw IllegalStateException() }, false, { true })
    }

    @Test(expected = IllegalStateException::class)
    fun unrelatedDarkFailureIsNotSwallowed() {
        AppearanceSelection.read({ null }, false, { throw IllegalStateException() })
    }
}
