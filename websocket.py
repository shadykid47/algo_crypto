import websocket
import json

# Define WebSocket endpoint
websocket_url = "wss://testnet-ws-evm.orderly.org/ws/stream/{account_id}".format(account_id="0x94db19933b524c2624c9216ed3e0fef400876b3bd1756210822a2254fe7f1414")

# Define topics to subscribe
topics = ["orderbook", "trade"]

# Function to handle incoming WebSocket messages
def on_message(ws, message):
    print("Received message:")
    print(json.loads(message))

# Function to handle WebSocket open event
def on_open(ws):
    print("WebSocket connection established")
    
    # Subscribe to topics
    subscribe_msg = json.dumps({"op": "subscribe", "topics": topics})
    ws.send(subscribe_msg)
    print("Subscribed to topics:", topics)

# Function to handle WebSocket close event
def on_close(ws):
    print("WebSocket connection closed")

# Function to handle WebSocket error event
def on_error(ws, error):
    print("Error:", error)

# Create WebSocket connection
ws = websocket.WebSocketApp(websocket_url,
                            on_message=on_message,
                            on_error=on_error,
                            on_close=on_close)

ws.on_open = on_open

# Run WebSocket client
ws.run_forever()
