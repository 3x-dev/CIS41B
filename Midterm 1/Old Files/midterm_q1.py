class RotatingCaesarCipher:
    def __init__(self, shift):
        self.initial_shift = shift

    def encrypt(self, plain_text):
        shift = self.initial_shift
        encrypted_text = ""
        for char in plain_text:
            ascii_value = ord(char)
            new_value = 0x20 + (ascii_value + shift - 0x20) % (0x80 - 0x20)
            encrypted_text += chr(new_value)
            shift += 1
        return encrypted_text

    def decrypt(self, encrypted_text):
        shift = self.initial_shift
        decrypted_text = ""
        for char in encrypted_text:
            ascii_value = ord(char)
            new_value = 0x20 + (ascii_value - shift - 0x20) % (0x80 - 0x20)
            decrypted_text += chr(new_value)
            shift += 1
        return decrypted_text

# Example test:
cipher = RotatingCaesarCipher(5)
encrypted = cipher.encrypt("HELLO")
decrypted = cipher.decrypt(encrypted)

print("Encrypted message:", encrypted)
print("Decrypted message:", decrypted)