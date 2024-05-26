import socket
import json
from ByteStreamsClass import StringConverter

class Client:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.host, self.port))
        self.converter = StringConverter()

    def send_request(self, query: str):
        self.converter.set_input_string(query)
        self.converter.send_byte_stream(self.client_socket)
        response = self.converter.receive_byte_stream(self.client_socket)
        return response

    def close(self):
        self.client_socket.close()

if __name__ == "__main__":
    client = Client('127.0.0.1', 65433)
    query = json.dumps({"sql": "SELECT * FROM users"})
    response = client.send_request(query)
    print(f"Response: {response}")
    client.close()
