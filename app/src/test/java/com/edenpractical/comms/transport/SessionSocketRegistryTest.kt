package com.edenpractical.comms.transport

import java.net.ServerSocket
import java.net.Socket
import java.net.SocketException
import java.util.concurrent.CountDownLatch
import java.util.concurrent.TimeUnit
import kotlin.concurrent.thread
import org.junit.Assert.assertFalse
import org.junit.Assert.assertNull
import org.junit.Assert.assertThrows
import org.junit.Assert.assertTrue
import org.junit.Test

class SessionSocketRegistryTest {
    @Test fun closesTrackedClientAndListenerWhenCancelled() {
        val registry = SessionSocketRegistry()
        val client = Socket()
        val listener = ServerSocket()
        registry.ownSocket(client)
        registry.ownServer(listener)
        registry.close()
        registry.close()
        assertTrue(client.isClosed)
        assertTrue(listener.isClosed)
        assertNull(registry.currentSocket())
        assertThrows(SocketException::class.java) { registry.requireOpen() }
    }

    @Test fun lateSocketsRejectedAndImmediatelyClosed() {
        val registry = SessionSocketRegistry()
        registry.close()
        val client = Socket()
        val server = ServerSocket()
        assertThrows(SocketException::class.java) { registry.ownSocket(client) }
        assertThrows(SocketException::class.java) { registry.ownServer(server) }
        assertTrue(client.isClosed)
        assertTrue(server.isClosed)
    }

    @Test fun tlsWrapperReplacementDoesNotPrematurelyCloseRawSocket() {
        val registry = SessionSocketRegistry()
        val raw = Socket()
        val wrapper = Socket()
        registry.ownSocket(raw)
        registry.ownSocket(wrapper)
        registry.releaseSocket(raw) // stale cleanup cannot disown the wrapper
        assertFalse(raw.isClosed)
        assertTrue(registry.currentSocket() === wrapper)
        registry.close()
        assertTrue(wrapper.isClosed)
        raw.close() // actual SSLSocket wrapper uses autoClose=true
    }

    @Test fun concurrentCancelAndRegistrationCannotLeakSocket() {
        repeat(40) {
            val registry = SessionSocketRegistry()
            val start = CountDownLatch(1)
            val done = CountDownLatch(1)
            val socket = Socket()
            val runner = thread {
                try {
                    start.await(3, TimeUnit.SECONDS)
                    try { registry.ownSocket(socket) } catch (_: SocketException) {}
                } finally { done.countDown() }
            }
            start.countDown()
            registry.close()
            assertTrue(done.await(3, TimeUnit.SECONDS))
            runner.join(1000)
            assertTrue("Socket leaked after cancellation", socket.isClosed)
        }
    }

    @Test fun staleListenerReleaseCannotDisownCurrentListener() {
        val registry = SessionSocketRegistry()
        val previous = ServerSocket()
        val current = ServerSocket()
        try {
            registry.ownServer(previous)
            registry.ownServer(current)
            registry.releaseServer(previous)
            registry.close()
            assertTrue(current.isClosed)
        } finally {
            registry.close()
            previous.close()
            current.close()
        }
    }

    @Test fun closingRegistryUnblocksRealLoopbackAccept() {
        val registry = SessionSocketRegistry()
        val listener = ServerSocket(0, 1, java.net.InetAddress.getLoopbackAddress())
        val ready = CountDownLatch(1)
        val done = CountDownLatch(1)
        val cancelled = java.util.concurrent.atomic.AtomicBoolean(false)
        registry.ownServer(listener)
        val worker = thread(isDaemon = true) {
            try {
                ready.countDown()
                listener.accept().close()
            } catch (_: SocketException) {
                cancelled.set(true)
            } finally { done.countDown() }
        }
        try {
            assertTrue(ready.await(3, TimeUnit.SECONDS))
            registry.close()
            assertTrue("Accept did not unblock", done.await(3, TimeUnit.SECONDS))
            assertTrue(cancelled.get())
        } finally {
            registry.close()
            worker.join(1000)
        }
    }

    @Test fun closingRegistryUnblocksRealLoopbackRead() {
        val address = java.net.InetAddress.getLoopbackAddress()
        ServerSocket(0, 1, address).use { listener ->
            Socket(address, listener.localPort).use { client ->
                listener.accept().use { peer ->
                    val registry = SessionSocketRegistry()
                    registry.ownSocket(client)
                    val ready = CountDownLatch(1)
                    val done = CountDownLatch(1)
                    val cancelled = java.util.concurrent.atomic.AtomicBoolean(false)
                    val worker = thread(isDaemon = true) {
                        try {
                            ready.countDown()
                            client.getInputStream().read()
                        } catch (_: SocketException) {
                            cancelled.set(true)
                        } finally { done.countDown() }
                    }
                    try {
                        assertTrue(ready.await(3, TimeUnit.SECONDS))
                        registry.close()
                        assertTrue("Read did not unblock", done.await(3, TimeUnit.SECONDS))
                        assertTrue(cancelled.get())
                    } finally {
                        registry.close()
                        worker.join(1000)
                    }
                }
            }
        }
    }
}
