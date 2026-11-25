package com.edenpractical.comms.appearance

import android.content.Context
import androidx.compose.material3.MaterialTheme
import androidx.compose.runtime.Composable
import androidx.compose.runtime.CompositionLocalProvider
import androidx.compose.runtime.remember
import androidx.compose.ui.platform.LocalContext

@Composable
internal fun NearbyAppearance(content: @Composable () -> Unit) {
    val context = LocalContext.current
    val preferences = remember(context) {
        context.getSharedPreferences("eden_comms_ui", Context.MODE_PRIVATE)
    }
    val palette = AppearancePreference.resolve(
        preferences.getString("appearance_palette", null), preferences.contains("dark_theme")
    )
    CompositionLocalProvider(LocalAppearance provides palette) {
        MaterialTheme(colorScheme = appearanceColors(palette, preferences.getBoolean("dark_theme", true)), content = content)
    }
}
