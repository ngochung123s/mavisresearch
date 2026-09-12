"""Python startup guard used by offline build subprocesses."""
import socket

class NetworkEgressBlocked(RuntimeError):
    pass

def _blocked(*args, **kwargs):
    raise NetworkEgressBlocked("offline build blocked network egress")

socket.socket.connect = _blocked
socket.socket.connect_ex = _blocked
socket.create_connection = _blocked
socket.getaddrinfo = _blocked
