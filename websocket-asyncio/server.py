import websockets
import asyncio

import websockets.exceptions

async def echo(websocket, path):
    try:
        while True:
            message = await websocket.recv()
            print(f"Received: {message}")
            response = f"I received: {message}"
            await websocket.send(response)
    except websockets.exceptions.ConnectionClosedOK:
        print('Connection closed')

async def main():
    async with websockets.serve(echo, "localhost", 8756):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())