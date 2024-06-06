import unittest
from ServerClass import Server
from ClientClass import Client
import json
import threading
import sqlite3

def create_database(db_path: str):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
    ''')
    cursor.execute('''
        INSERT OR IGNORE INTO users (name, email) VALUES
        ('Alice', 'alice@example.com'),
        ('Bob', 'bob@example.com'),
        ('Charlie', 'charlie@example.com')
    ''')
    conn.commit()
    conn.close()

class TestClientServer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        create_database('Database.db')
        cls.server = Server('127.0.0.1', 65433, 'Database.db')
        cls.server_thread = threading.Thread(target=cls.server.start)
        cls.server_thread.daemon = True
        cls.server_thread.start()

    def setUp(self):
        self.client = Client('127.0.0.1', 65433)

    def test_query(self):
        query = json.dumps({"sql": "SELECT * FROM users"})
        response = self.client.send_request(query)
        data = json.loads(response)
        self.assertEqual(len(data), 3)
        self.assertEqual(data[0]["name"], "Alice")

    def tearDown(self):
        self.client.close()

if __name__ == "__main__":
    unittest.main()
