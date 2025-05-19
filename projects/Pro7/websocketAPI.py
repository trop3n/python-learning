import asyncio
import websockets

async def connect_to_propresenter():
    uri = "ws://<ProPresenter_IP>:<port>/remote" # Replace with the actual WebSocket URI
    async with websockets.connect(uri) as websocket:
        # send a command (e.g. request slide data)
        await websocket.send('{"action"}: "getSlideData}')

        # recieve response
        response = await websocket.recv()
        print("Response:", response)

# Run the WebSocket client
asyncio.get_event_loop().run_until_complete(connect_to_propresenter())