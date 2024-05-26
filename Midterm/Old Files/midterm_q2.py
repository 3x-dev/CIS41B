import sqlite3
import unittest

class RotatingCaesarCipher:
    def __init__(self, shift):
        self.initial_shift = shift

    def encrypt(self, text):
        shift = self.initial_shift
        encrypted_text = ""
        for char in text:
            new_value = 0x20 + (ord(char) + shift - 0x20) % (0x80 - 0x20)
            encrypted_text += chr(new_value)
            shift += 1
        return encrypted_text

    def decrypt(self, text):
        shift = self.initial_shift
        decrypted_text = ""
        for char in text:
            new_value = 0x20 + (ord(char) - shift - 0x20) % (0x80 - 0x20)
            decrypted_text += chr(new_value)
            shift += 1
        return decrypted_text

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
            self.conn.commit()
            if query.strip().upper().startswith("SELECT"):
                return cursor.fetchall()
            print("Query executed successfully.")
        except sqlite3.Error as e:
            print(f"Error executing query: {e}")

    def query_builder(self, query_type, table_name, fields=None):
        queries = {
            "CREATE": lambda: f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join(f'{field} TEXT' for field in fields)})",
            "INSERT": lambda: f"INSERT INTO {table_name} ({', '.join(fields)}) VALUES ({', '.join(['?' for _ in fields])})",
            "SELECT": lambda: f"SELECT * FROM {table_name}"
        }
        return queries[query_type.upper()]()

class TestDatabaseAndCipher(unittest.TestCase):
    def test_encryption_decryption_query(self):
        db_manager = SQLiteManager(':memory:')
        fields = ['name', 'value']
        insert_query = db_manager.query_builder("INSERT", "test_table", fields)

        # Encrypt and decrypt the query
        cipher = RotatingCaesarCipher(5)
        encrypted_query = cipher.encrypt(insert_query)
        decrypted_query = cipher.decrypt(encrypted_query)

        self.assertEqual(decrypted_query, insert_query, "Decrypted query should match the original")

if __name__ == "__main__":
    unittest.main()
