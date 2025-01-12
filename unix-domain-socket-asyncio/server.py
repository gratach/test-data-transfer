from pathlib import Path
from os import unlink
import socket
import asyncio

# Get the current working directory and append the path to the unix-socket
root_dir = Path(__file__).parent
socket_path = root_dir / 'socket'

# If the socket file exists, remove it
if socket_path.exists():
    unlink(str(socket_path))

async def handle_client(reader, writer):
    loop = asyncio.get_event_loop()
    print('handle_client')
    message = await reader.read(100)
    print('Received', repr(message))
    writer.write(b'I received: ' + message)
    await writer.drain()

async def run_server():
    loop = asyncio.get_event_loop()
    server = await asyncio.start_unix_server(handle_client, str(socket_path))
    print(f'Serving on {socket_path}')
    async with server:
        await server.serve_forever()

asyncio.run(run_server())
