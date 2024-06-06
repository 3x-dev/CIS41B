import socket
import json
from ByteStreamsClass import StringConverter
from CommandClass import Command
from RotorClass import Rotor

class Server:
    def __init__(self, host: str, port: int, db_path: str):
        self.host = host
        self.port = port
        self.db_path = db_path
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print(f"Server listening on {self.host}:{self.port}")
        self.rotor = Rotor()

    def handle_client(self, client_socket: socket.socket):
        converter = StringConverter()
        while True:
            request = converter.receive_byte_stream(client_socket)
            if not request:
                break
            print(f"Received request: {request}")
            response = self.process_request(request)
            converter.set_input_string(response)
            converter.send_byte_stream(client_socket)
        client_socket.close()

    def process_request(self, request: str) -> str:
        try:
            data = json.loads(request)
            op = data.get("op")
            argv = data.get("argv", 0)
            command = Command(op, argv)
            result = self.rotor.execute_command(command)
            return json.dumps({"result": result})
        except Exception as e:
            return json.dumps({"error": str(e)})

    def start(self):
        while True:
            client_socket, addr = self.server_socket.accept()
            print(f"Connection from {addr}")
            self.handle_client(client_socket)

if __name__ == "__main__":
    server = Server('127.0.0.1', 65433, 'Database.db')
    server.start()
