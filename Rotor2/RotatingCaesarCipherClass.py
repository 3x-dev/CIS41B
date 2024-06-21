import unittest
from Rotor2Class import read_encrypted_file, find_initial_settings

class TestRotorDecryption(unittest.TestCase):
    def test_decryption(self):
        encrypted_text = read_encrypted_file('/mnt/data/E2Rotor.txt')
        result = find_initial_settings(encrypted_text)
        self.assertIsNotNone(result)
        self.assertTrue(" the " in result or " and " in result)  # Adding a basic validation for common English words

if __name__ == '__main__':
    unittest.main()