import unittest
from unittest.mock import Mock
from CaesarCipherClass import CaesarCipher
from ClientClass import Client
import json

class TestCaesarCipher(unittest.TestCase):
    def setUp(self):
        # Mock the Client class
        self.mock_client = Mock(spec=Client)
        self.cipher = CaesarCipher(self.mock_client)

    def mock_send_command(self, op, shift_amount):
        if op == 0b011:
            return json.dumps({"result": chr((self.current_char - 97 + shift_amount) % 26 + 97)})
        elif op == 0b010:
            return json.dumps({"result": chr((self.current_char - 97 - shift_amount) % 26 + 97)})

    def test_encrypt(self):
        original_text = "hello"
        shift = 3
        encrypted_text = ""

        for char in original_text:
            if char.isalpha():
                self.current_char = ord(char)
                if char.islower():
                    self.mock_client.send_command.side_effect = self.mock_send_command
                    encrypted_text += json.loads(self.mock_client.send_command(0b011, shift)).get("result")
                else:
                    self.mock_client.send_command.side_effect = self.mock_send_command
                    encrypted_text += json.loads(self.mock_client.send_command(0b011, shift % 26)).get("result")
            else:
                encrypted_text += char

        self.assertEqual(encrypted_text, "khoor", "The encrypted text does not match the expected output")

    def test_decrypt(self):
        encrypted_text = "khoor"
        shift = 3
        decrypted_text = ""

        for char in encrypted_text:
            if char.isalpha():
                self.current_char = ord(char)
                if char.islower():
                    self.mock_client.send_command.side_effect = self.mock_send_command
                    decrypted_text += json.loads(self.mock_client.send_command(0b010, shift)).get("result")
                else:
                    self.mock_client.send_command.side_effect = self.mock_send_command
                    decrypted_text += json.loads(self.mock_client.send_command(0b010, shift % 26)).get("result")
            else:
                decrypted_text += char

        self.assertEqual(decrypted_text, "hello", "The decrypted text does not match the expected output")

if __name__ == "__main__":
    unittest.main()
