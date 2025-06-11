import tornado.ioloop
import tornado.websocket

class WebSocketClient:
    def __init__(self, io_loop):
        self.connection = None
        self.io_loop = io_loop

    def start(self):
        self.connect_and_read()

    def stop(self):
        if self.connection:
            self.connection.close()
        self.io_loop.stop()

    def connect_and_read(self):
        print("Reading...")
        tornado.websocket.websocket_connect(
            url=f"ws://localhost:8888/websocket/",
            callback=self.maybe_retry_connection,
            on_message_callback=self.on_message,
            ping_interval=10,
            ping_timeout=30,
        )

    def maybe_retry_connection(self, future) -> None:
        try:
            self.connection = future.result()
            print("Connected to WebSocket server.")
            self.connection.read_message(callback=self.on_message)
        except Exception as e:
            print(f"Could not connect, retrying in 3 seconds... Error: {e}")
            self.io_loop.call_later(3, self.connect_and_read)

    def on_message(self, message):
        if message is None:
            print("Disconnected, reconnecting...")
            self.connection = None # Clear connection
            self.io_loop.call_later(1, self.connect_and_read) # Attempt reconnect after 1 second
            return

        print(f"Received word from server: {message}")
        
        # Continue reading messages
        if self.connection:
            self.connection.read_message(callback=self.on_message)


def main():
    io_loop = tornado.ioloop.IOLoop.current()

    client = WebSocketClient(io_loop)
    io_loop.add_callback(client.start)

    try:
        io_loop.start()
    except KeyboardInterrupt:
        print("\nClient stopped by user.")
        client.stop() # Ensure client cleanup
        io_loop.stop() # Ensure ioloop stops fully

if __name__ == "__main__":
    main()