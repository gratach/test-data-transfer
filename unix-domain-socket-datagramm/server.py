from pathlib import Path
from os import unlink
import socket

# Get the current working directory and append the path to the unix-sockets directory
root_dir = Path(__file__).parent
server_socket_path = root_dir / 'server-socket'

# If the socket file exists, remove it
if server_socket_path.exists():
    unlink(str(server_socket_path))

# Create a new socket file
with socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM) as s:
    s.bind(str(server_socket_path))
    while True:
        data, addr = s.recvfrom(1024)
        print('Received', repr(data), 'from', addr)
        s.sendto(b'I received: ' + data, addr)