import json

class CaesarCipher:
    def __init__(self, client):
        self.client = client

    def encrypt(self, text, shift):
        encrypted_text = ""
        for char in text:
            if char.isalpha():
                shift_amount = shift if char.islower() else shift % 26
                op = 0b011 if shift > 0 else 0b010
                response = self.client.send_command(op, shift_amount)
                encrypted_char = json.loads(response).get("result")
                encrypted_text += encrypted_char
            else:
                encrypted_text += char
        return encrypted_text

    def decrypt(self, text, shift):
        return self.encrypt(text, -shift)
