package com.edenpractical.comms.appearance

import android.animation.ValueAnimator
import androidx.activity.compose.BackHandler
import androidx.compose.animation.core.Animatable
import androidx.compose.animation.core.LinearEasing
import androidx.compose.animation.core.tween
import androidx.compose.foundation.Image
import androidx.compose.foundation.background
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.alpha
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.layout.ContentScale
import androidx.compose.ui.platform.testTag
import androidx.compose.ui.graphics.ImageBitmap
import androidx.compose.ui.graphics.asImageBitmap
import androidx.compose.ui.platform.LocalContext
import android.graphics.BitmapFactory
import androidx.compose.ui.unit.dp
import androidx.lifecycle.compose.LocalLifecycleOwner
import androidx.lifecycle.Lifecycle
import androidx.lifecycle.LifecycleEventObserver
import com.edenpractical.comms.R
import kotlinx.coroutines.delay

internal const val EPS_FADE_MS = 250
internal const val EPS_HOLD_MS = 2500

@Composable
internal fun EpsStartup(showInitially: Boolean, content: @Composable () -> Unit) {
    val context = LocalContext.current
    val artwork: ImageBitmap? = remember {
        if (!showInitially || !ValueAnimator.areAnimatorsEnabled()) null
        else runCatching {
            BitmapFactory.decodeResource(context.resources, R.drawable.eps_v1_runtime)?.asImageBitmap()
        }.getOrNull()
    }
    var visible by remember { mutableStateOf(artwork != null) }
    val opacity = remember { Animatable(0f) }
    val lifecycle = LocalLifecycleOwner.current.lifecycle
    DisposableEffect(lifecycle) {
        val observer = LifecycleEventObserver { _, event ->
            if (event == Lifecycle.Event.ON_STOP) visible = false
        }
        lifecycle.addObserver(observer)
        onDispose { lifecycle.removeObserver(observer) }
    }
    BackHandler(visible) { visible = false }
    LaunchedEffect(visible) {
        if (!visible) return@LaunchedEffect
        if (!ValueAnimator.areAnimatorsEnabled()) {
            visible = false
            return@LaunchedEffect
        }
        opacity.animateTo(1f, tween(EPS_FADE_MS, easing = LinearEasing))
        delay(EPS_HOLD_MS.toLong())
        opacity.animateTo(0f, tween(EPS_FADE_MS, easing = LinearEasing))
        visible = false
    }
    if (visible) {
        Box(
            Modifier.fillMaxSize().background(Color(0xFF111214))
                .clickable(onClickLabel = "Skip startup") { visible = false }
                .testTag("eps_startup"),
            contentAlignment = Alignment.Center
        ) {
            if (artwork != null) {
                Image(
                    bitmap = artwork,
                    contentDescription = "Eden Practical Solutions",
                    contentScale = ContentScale.Fit,
                    modifier = Modifier.safeDrawingPadding().padding(24.dp)
                        .widthIn(max = 420.dp).fillMaxWidth(.82f)
                        .heightIn(max = 300.dp).alpha(opacity.value)
                )
            }
        }
    } else content()
}
