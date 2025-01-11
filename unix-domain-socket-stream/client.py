from pathlib import Path
from os import unlink
import socket

# Get the current working directory and append the path to the unix-sockets directory
root_dir = Path(__file__).parent
socket_path = root_dir / 'socket'

# Connect to the server
with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as s:
    s.connect(str(socket_path))
    s.sendall(b'Here comes my custom message')
    message = input('Enter your message: ')
    s.sendall(message.encode())
    # The server returns the first message before it can receive the second message
    # This first returned message is written into the sockets buffer
    # The buffer has a limited size and blocks if it is full (https://unix.stackexchange.com/questions/283323/do-unix-domain-sockets-overflow)
    data = s.recv(1024)
    print('Received', repr(data))
    data = s.recv(1024)
    print('Received', repr(data))