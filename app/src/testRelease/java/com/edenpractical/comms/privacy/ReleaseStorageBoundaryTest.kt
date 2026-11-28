package com.edenpractical.comms.privacy

import android.content.ContextWrapper
import com.edenpractical.comms.BuildConfig
import org.junit.Assert.*
import org.junit.Test

/** JVM release-variant only. Android mock context must never be accessed. */
class ReleaseStorageBoundaryTest {
    private val own = ByteArray(32) { (it + 1).toByte() }
    private val peer = ByteArray(32) { (it + 65).toByte() }
    private val now = 1_800_000_000_000L

    private fun context(): ContextWrapper {
        assertFalse("Must run against release variant", BuildConfig.DEBUG)
        return ContextWrapper(null)
    }

    @Test fun historyRejectsEveryRetentionAndDirection() {
        val store = DebugLocalHistoryStore(context())
        for (choice in LocalHistoryPolicy.choices) {
            for (direction in LocalHistoryPolicy.Direction.entries) {
                assertFalse(store.save(peer, direction, 1L, "Synthetic QA", choice.durationMs, now))
            }
            assertFalse(store.changeRetention(peer, choice.durationMs, now))
            assertTrue(store.read(peer, now).isEmpty())
        }
        assertFalse(store.erasePeer(peer, now))
        assertFalse(store.eraseAll())
        assertTrue(DebugLocalHistoryStore(context()).read(peer, now).isEmpty())
    }

    @Test fun peerMemoryRejectsEverySupportedLifetime() {
        val store = DebugPeerMemoryStore(context())
        for (days in 1..30) {
            assertNull(store.remember(own, peer, days, now))
            assertNull(store.rememberedUntil(own, peer, now))
        }
        assertFalse(store.forget(own, peer, now))
        assertFalse(store.forgetAll())
        assertNull(DebugPeerMemoryStore(context()).rememberedUntil(own, peer, now))
    }

    @Test fun invalidInputsCannotActivateReleaseStorage() {
        val ctx = context()
        val history = DebugLocalHistoryStore(ctx)
        val memory = DebugPeerMemoryStore(ctx)
        for (pin in listOf(ByteArray(0), ByteArray(32), ByteArray(33), peer)) {
            assertFalse(history.save(pin, LocalHistoryPolicy.Direction.WRITTEN_HERE,
                -1L, "", Long.MAX_VALUE, -1L))
            assertTrue(history.read(pin, -1L).isEmpty())
            assertNull(memory.remember(own, pin, Int.MAX_VALUE, -1L))
            assertNull(memory.rememberedUntil(own, pin, -1L))
        }
    }
}
