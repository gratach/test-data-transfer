from pathlib import Path
from os import unlink
import socket
import asyncio

port = 13245

async def handle_client(reader, writer):
    loop = asyncio.get_event_loop()
    print('handle_client')
    message = await reader.read(100)
    print('Received', repr(message))
    writer.write(b'I received: ' + message)
    await writer.drain()

async def run_server():
    loop = asyncio.get_event_loop()
    server = await asyncio.start_server(handle_client, 'localhost', port)
    print(f'Serving on localhost:{port}')
    async with server:
        await server.serve_forever()

asyncio.run(run_server())
