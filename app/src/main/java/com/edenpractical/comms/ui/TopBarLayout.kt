package com.edenpractical.comms.ui

/**
 * Readable header policy only. Does not own navigation or session state.
 * Keep ordinary wide-screen headers short while allowing enlarged text.
 */
internal object TopBarLayout {
    fun maxTitleLines(availableWidthDp: Float, fontScale: Float): Int =
        if (availableWidthDp < 360f || fontScale >= 1.3f) 2 else 1
    // Publisher attribution is longer than the title and has less room beside the icon.
    fun maxPublisherLines(availableWidthDp: Float, fontScale: Float): Int =
        if (availableWidthDp < 400f || fontScale >= 1.3f) 3 else 1
}
