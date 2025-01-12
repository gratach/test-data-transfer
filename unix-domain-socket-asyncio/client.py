from pathlib import Path
from os import unlink
import socket
import asyncio

# Get the current working directory and append the path to the unix-socket
root_dir = Path(__file__).parent
socket_path = root_dir / 'socket'

async def main():
    with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as s:
        s.connect(str(socket_path))
        s.sendall(b'Hello, World')
        #data = await asyncio.to_thread(s.recv, 1024)
        data = s.recv(1024)
        print('Received', repr(data))

asyncio.run(main())