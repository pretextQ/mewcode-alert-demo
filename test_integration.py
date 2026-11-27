import socket

from app import configured_timeout

with socket.create_connection(("cache", 6379), timeout=configured_timeout()) as sock:
    with sock.makefile("rb") as replies:
        sock.sendall(b"PING\r\n")
        assert replies.readline() == b"+PONG\r\n"
        sock.sendall(b"SET mewcode-acceptance oksandbox\r\n")
        assert replies.readline() == b"+OK\r\n"
        sock.sendall(b"GET mewcode-acceptance\r\n")
        assert replies.readline() == b"$9\r\n"
        assert replies.readline() == b"oksandbox\r\n"
print("integration ok: Redis PING and SET/GET in the Compose network")
