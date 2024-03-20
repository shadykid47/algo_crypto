import websocket, json, gzip, pickle, datetime
from websocket import create_connection

orderly_account_id = 'asdasd'

socket = f'wss://ws-evm.orderly.org/ws/stream/{orderly_account_id}'

def on_message(ws, message):
    print(message)

def on_close(ws):
    print("### closed ###")

# ws = websocket.WebSocketApp(socket, on_message=on_message, on_close=on_close)

sub_data = {
    "id": 'asasdasd',
    "topic": "markprices",
    "event": "subscribe"
}

if __name__ == '__main__':

    ws = create_connection(socket)

    ws.send(json.dumps(sub_data))
    # response
    while True:
        data = ws.recv()
        with gzip.open(f'../tick_data/{datetime.datetime.now()}.pkl.gz', 'wb') as f:
            pickle.dump(data, f)
        print("Received '%s'" % data)
