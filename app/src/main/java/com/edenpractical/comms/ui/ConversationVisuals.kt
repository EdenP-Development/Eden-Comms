package com.edenpractical.comms.ui

import androidx.compose.foundation.layout.*
import androidx.compose.foundation.shape.CutCornerShape
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.semantics.semantics
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import com.edenpractical.comms.appearance.supportingAccent

/** Presentation only; caller owns every message and observation. No trust or I/O. */
@Composable
internal fun ConversationBubble(
    outgoing: Boolean,
    message: String,
    observation: String
) {
    Row(
        modifier = Modifier.fillMaxWidth(),
        horizontalArrangement = if (outgoing) Arrangement.End else Arrangement.Start
    ) {
        Surface(
            modifier = Modifier.fillMaxWidth(.88f).semantics(mergeDescendants = true) {},
            shape = CutCornerShape(8.dp),
            color = if (outgoing) supportingAccent().copy(alpha = .14f)
                else MaterialTheme.colorScheme.surfaceVariant
        ) {
            Column(Modifier.padding(horizontal = 12.dp, vertical = 10.dp),
                verticalArrangement = Arrangement.spacedBy(4.dp)) {
                Text(if (outgoing) "You" else "Other phone",
                    style = MaterialTheme.typography.labelMedium,
                    fontWeight = FontWeight.SemiBold,
                    color = MaterialTheme.colorScheme.onSurface)
                Text(message, style = MaterialTheme.typography.bodyMedium,
                    color = MaterialTheme.colorScheme.onSurface)
                Text(observation, style = MaterialTheme.typography.labelSmall,
                    color = MaterialTheme.colorScheme.onSurfaceVariant)
            }
        }
    }
}
