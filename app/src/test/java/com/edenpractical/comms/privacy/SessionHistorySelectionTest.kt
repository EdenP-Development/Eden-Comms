package com.edenpractical.comms.privacy

import org.junit.Assert.*
import org.junit.Test

class SessionHistorySelectionTest {
    private val peer = ByteArray(32) { 1 }
    private val other = ByteArray(32) { 2 }

    @Test fun freshAndNewPeerNeverInheritRetention() {
        val fresh = SessionHistorySelection.fresh()
        assertNull(fresh.peerPin())
        assertFalse(fresh.maySave(false))
        val selected = fresh.activate(peer).choose(LocalHistoryPolicy.ONE_DAY)
        assertTrue(selected.maySave(false))
        assertFalse(selected.maySave(true))
        for (pin in listOf(peer, other)) {
            val next = selected.activate(pin)
            assertEquals(LocalHistoryPolicy.SESSION_ONLY, next.durationMs)
            assertArrayEquals(pin, next.peerPin())
            assertFalse(next.maySave(false))
        }
        val ended = selected.reset()
        assertNull(ended.peerPin())
        assertEquals(LocalHistoryPolicy.SESSION_ONLY, ended.durationMs)
        assertFalse(ended.maySave(false))
    }

    @Test fun validChoicesAndExplicitSessionOnly() {
        val active = SessionHistorySelection.fresh().activate(peer)
        for (choice in LocalHistoryPolicy.choices) {
            val selected = active.choose(choice.durationMs)
            assertEquals(choice.durationMs, selected.durationMs)
            assertEquals(choice.durationMs != 0L, selected.maySave(false))
            assertFalse(selected.maySave(true))
        }
        assertFalse(active.choose(LocalHistoryPolicy.ONE_DAY).choose(0L).maySave(false))
    }

    @Test fun invalidInputAndNoActivePeerRejectSelection() {
        assertThrows(IllegalArgumentException::class.java) {
            SessionHistorySelection.fresh().choose(LocalHistoryPolicy.ONE_DAY)
        }
        assertThrows(IllegalArgumentException::class.java) {
            SessionHistorySelection.fresh().activate(ByteArray(32))
        }
        assertThrows(IllegalArgumentException::class.java) {
            SessionHistorySelection.fresh().activate(peer).choose(-1L)
        }
    }

    @Test fun pinIsDefensivelyCopied() {
        val input = peer.copyOf()
        val active = SessionHistorySelection.fresh().activate(input)
        input.fill(0)
        active.peerPin()!!.fill(0)
        assertArrayEquals(peer, active.peerPin())
    }
}
