from pathlib import Path
from os import unlink
import socket

# Get the current working directory and append the path to the unix-sockets directory
root_dir = Path(__file__).parent
socket_path = root_dir / 'socket'

# If the socket file exists, remove it
if socket_path.exists():
    unlink(str(socket_path))

# Create a new socket file
with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as s:
    s.bind(str(socket_path))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                print('No more data received')
                break
            print('Received', repr(data))
            # Sent "I received: " + data back to the client
            conn.sendall(b'I received: ' + data)