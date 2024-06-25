import socket
import sqlite3
import json
import threading
from ByteStreamClass import StringConverter

class Server:
    def __init__(self, host: str, port: int, db_path: str):
        self.host = host
        self.port = port
        self.db_path = db_path
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        self.lock = threading.Lock()
        print(f"Server listening on {self.host}:{self.port}")

    def handle_client(self, client_socket: socket.socket):
        converter = StringConverter()
        while True:
            try:
                request = converter.receive_byte_stream(client_socket)
                if not request:
                    break
                print(f"Received request: {request}")
                response = self.process_request(request)
                converter.set_input_string(response)
                converter.send_byte_stream(client_socket)
            except Exception as e:
                print(f"Error handling client: {e}")
                break
        client_socket.close()

    def process_request(self, request: str) -> str:
        try:
            query = json.loads(request)
            year = query["year"]
            column = query["column"]
            result = self.execute_query(year, column)
            return json.dumps(result)
        except Exception as e:
            return json.dumps({"error": str(e)})

    def execute_query(self, year: str, column: str) -> dict:
        with self.lock:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute(f"SELECT {column} FROM AGGI WHERE Year = ?", (year,))
            row = cursor.fetchone()
            conn.close()
        if row:
            return {year: {column: row[0]}}
        else:
            return {year: {column: None}}

    def create_table(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS AGGI (
            Year TEXT,
            CO2 REAL,
            CH4 REAL,
            N2O REAL,
            CFCs REAL,
            HCFCs REAL,
            HFCs REAL
        )
        ''')
        conn.commit()
        conn.close()

    def start(self):
        self.create_table()
        while True:
            client_socket, addr = self.server_socket.accept()
            print(f"Connection from {addr}")
            client_handler = threading.Thread(target=self.handle_client, args=(client_socket,))
            client_handler.start()

if __name__ == "__main__":
    server = Server('127.0.0.1', 65433, 'aggi_data.db')
    server.start()
