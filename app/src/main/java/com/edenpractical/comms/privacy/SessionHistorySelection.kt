package com.edenpractical.comms.privacy

/**
 * In-memory selection for the current verified conversation only.
 * Not a trust/approval source, storage API, or persisted setting.
 * Caller must establish the actual confirmed channel before activate(),
 * and apply the requested storage change successfully before choose().
 */
internal class SessionHistorySelection private constructor(
    private val pin: ByteArray?,
    val durationMs: Long
) {
    fun peerPin(): ByteArray? = pin?.copyOf()

    fun activate(verifiedPin: ByteArray): SessionHistorySelection {
        require(PeerMemoryPolicy.validPin(verifiedPin))
        return SessionHistorySelection(verifiedPin.copyOf(), LocalHistoryPolicy.SESSION_ONLY)
    }

    fun choose(appliedDurationMs: Long): SessionHistorySelection {
        require(pin != null && LocalHistoryPolicy.supported(appliedDurationMs))
        return SessionHistorySelection(pin.copyOf(), appliedDurationMs)
    }

    fun reset(): SessionHistorySelection = fresh()

    fun maySave(disappearingEnabled: Boolean): Boolean =
        pin != null && durationMs != LocalHistoryPolicy.SESSION_ONLY && !disappearingEnabled

    companion object {
        fun fresh() = SessionHistorySelection(null, LocalHistoryPolicy.SESSION_ONLY)
    }
}
