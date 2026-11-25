package com.edenpractical.comms.appearance
import androidx.compose.material3.*
import androidx.compose.ui.graphics.Color
import androidx.compose.runtime.Composable
import androidx.compose.runtime.staticCompositionLocalOf
private val Graphite = Color(0xFF0D1112)
private val GraphiteSurface = Color(0xFF161B1D)
private val GraphiteRaised = Color(0xFF1F2628)
private val SoftIvory = Color(0xFFE6E8E6)
private val PaleSage = Color(0xFF8FAA6A)
private val LightSurface = Color(0xFFFFFFFF)
private val Ink = Color(0xFF232A25)

internal fun appearanceColors(appearance: AppearancePreference, darkMode: Boolean): ColorScheme {
    if (appearance == AppearancePreference.EPS) {
        return if (darkMode) darkColorScheme(
            primary = Color(0xFFD6A044), onPrimary = Color(0xFF111214),
            secondary = Color(0xFFC9A1EA), onSecondary = Color(0xFF251137),
            background = Color(0xFF111214), onBackground = Color(0xFFE9E8E4),
            surface = Color(0xFF1B1C1E), onSurface = Color(0xFFE9E8E4),
            surfaceVariant = Color(0xFF292B2D), onSurfaceVariant = Color(0xFFC4C5C4),
            outline = Color(0xFF898B8B)
        ) else lightColorScheme(
            primary = Color(0xFF80551A), onPrimary = Color.White,
            secondary = Color(0xFF71349E), onSecondary = Color.White,
            background = Color(0xFFF4F3F0), onBackground = Color(0xFF232426),
            surface = Color.White, onSurface = Color(0xFF232426),
            surfaceVariant = Color(0xFFE9E8E4), onSurfaceVariant = Color(0xFF454747),
            outline = Color(0xFF626565)
        )
    }
    return if (darkMode) {
        darkColorScheme(
            primary = PaleSage,
            onPrimary = Graphite,
            background = Graphite,
            onBackground = SoftIvory,
            surface = GraphiteSurface,
            onSurface = SoftIvory,
            surfaceVariant = GraphiteRaised,
            onSurfaceVariant = Color(0xFFAFB7B1),
            outline = Color(0xFF667269)
        )
    } else {
        lightColorScheme(
            primary = Color(0xFF536C4C),
            onPrimary = Color.White,
            background = Color(0xFFF5F6F2),
            onBackground = Ink,
            surface = LightSurface,
            onSurface = Ink,
            surfaceVariant = Color(0xFFECF0EA),
            onSurfaceVariant = Color(0xFF58665C),
            outline = Color(0xFFC5CEC5)
        )
    }

}

// Brand roles only: never use these as a connection, approval or error state.
internal val LocalAppearance = staticCompositionLocalOf { AppearancePreference.FIELD }

@Composable
internal fun supportingAccent(): Color = if (LocalAppearance.current == AppearancePreference.EPS)
    MaterialTheme.colorScheme.secondary else MaterialTheme.colorScheme.primary

@Composable
internal fun actionFill(): Color = if (LocalAppearance.current == AppearancePreference.EPS)
    Color(0xFFD6A044) else MaterialTheme.colorScheme.primary

@Composable
internal fun actionContent(): Color = if (LocalAppearance.current == AppearancePreference.EPS)
    Color(0xFF111214) else MaterialTheme.colorScheme.onPrimary
