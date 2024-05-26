import unittest
from cipherclass import RotatingCaesarCipher  # Import from cipherclass.py
from databases import SQLiteManager  # Import from databases.py

class TestDatabaseAndCipher(unittest.TestCase):
    def test_encryption_decryption_query(self):
        db_manager = SQLiteManager(':memory:')
        fields = ['name', 'value']
        insert_query = db_manager.query_builder("INSERT", "test_table", fields)
        cipher = RotatingCaesarCipher(5)
        encrypted_query = cipher.encrypt(insert_query)
        decrypted_query = cipher.decrypt(encrypted_query)
        self.assertEqual(decrypted_query, insert_query, "Decrypted query should match the original")

if __name__ == "__main__":
    unittest.main()
