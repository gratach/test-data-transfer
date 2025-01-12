from os import unlink
import socket
import asyncio

# Define the port on localhost
port = 13245


async def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('localhost', port))
        s.sendall(b'Hello, World')
        #data = await asyncio.to_thread(s.recv, 1024)
        data = s.recv(1024)
        print('Received', repr(data))

asyncio.run(main())