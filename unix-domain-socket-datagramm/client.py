from pathlib import Path
from os import unlink
import socket

# Get the current working directory and append the path to the unix-sockets directory
root_dir = Path(__file__).parent
server_socket_path = root_dir / 'server-socket'
client_socket_path = root_dir / 'client-socket'

# If the socket file exists, remove it
if client_socket_path.exists():
    unlink(str(client_socket_path))

# Connect to the server
with socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM) as s:
    s.bind(str(client_socket_path))
    s.sendto(b'Here comes my custom message', str(server_socket_path).encode())
    message = input('Enter your message: ')
    s.sendto(message.encode(), str(server_socket_path).encode())
    data = s.recv(1024)
    print('Received', repr(data))
    data = s.recv(1024)
    print('Received', repr(data))