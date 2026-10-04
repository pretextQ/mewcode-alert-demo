"""Integration check: needs the docker-compose cache service (M2 W4).

Runs inside the sandbox container joined to the compose project network, so the
dependency is reached by its service name ("cache") - no host ports involved.
"""
import socket

with socket.create_connection(("cache", 6379), timeout=10) as sock:
    sock.sendall(b"PING\r\n")
    if b"PONG" not in sock.recv(1024):
        raise SystemExit("integration: cache did not answer PING")
    sock.sendall(b"SET mewcode ok\r\n")
    sock.recv(1024)
    sock.sendall(b"GET mewcode\r\n")
    if b"ok" not in sock.recv(1024):
        raise SystemExit("integration: cache lost the value")
print("integration ok: cache reachable and responsive")
