import asyncio
import signal
import websockets

HOST = "0.0.0.0"
PORT = 8080

async def echo(websocket, path):
    print(f"Client connected: {websocket.remote_address}")
    try:
        async for message in websocket:
            if isinstance(message, str):
                print(f"Received text message: {message}")
                await websocket.send(message)  # echo text
            elif isinstance(message, bytes):
                print(f"Received binary message ({len(message)} bytes)")
                await websocket.send(message)  # echo binary
            else:
                print("Unknown message type")
    except websockets.exceptions.ConnectionClosedOK:
        print("Connection closed normally.")
    except websockets.exceptions.ConnectionClosedError as e:
        print(f"Connection closed with error: {e}")
    finally:
        print(f"Client disconnected: {websocket.remote_address}")

async def main():
    async with websockets.serve(echo, HOST, PORT, max_size=None):
        print(f"Server started on ws://{HOST}:{PORT}")
        await asyncio.Future()  # run forever

def shutdown():
    print("Shutting down gracefully...")
    for task in asyncio.all_tasks():
        task.cancel()

if __name__ == "__main__":
    println("starting")
    loop = asyncio.get_event_loop()
    for sig in (signal.SIGINT, signal.SIGTERM):
        loop.add_signal_handler(sig, shutdown)
    try:
        loop.run_until_complete(main())
    except asyncio.CancelledError:
        pass
    finally:
        loop.close()
        print("Server closed.")
