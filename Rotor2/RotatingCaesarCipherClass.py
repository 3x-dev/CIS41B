import unittest
from Rotor2Class import read_encrypted_file, find_initial_settings

class TestRotorDecryption(unittest.TestCase):
    def test_decryption(self):
        encrypted_text = read_encrypted_file('test.txt')
        result = find_initial_settings(encrypted_text)
        self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main()
