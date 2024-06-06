import sqlite3
from bs4 import BeautifulSoup

class SQLiteManager:
    def __init__(self, db_path):
        self.db_path = db_path
        self.conn = None

    def connect(self):
        self.conn = sqlite3.connect(self.db_path)
        print(f"Connected to {self.db_path} successfully.")

    def disconnect(self):
        if self.conn:
            self.conn.close()
            print("Database connection closed.")

    def execute_query(self, query, params=None):
        try:
            cursor = self.conn.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            if query.strip().upper().startswith("SELECT"):
                return cursor.fetchall()
            self.conn.commit()
            print("Query executed successfully.")
        except sqlite3.Error as e:
            print(f"Error executing query: {e}")

    def query_builder(self, query_type, table_name, fields=None):
        queries = {
            "CREATE": lambda fields: f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join(f'{field} TEXT' for field in fields)})",
            "INSERT": lambda fields: f"INSERT INTO {table_name} ({', '.join(fields)}) VALUES ({', '.join(['?' for _ in fields])})",
            "SELECT": lambda fields: f"SELECT * FROM {table_name}"
        }
        return queries[query_type.upper()](fields if fields else [])

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()