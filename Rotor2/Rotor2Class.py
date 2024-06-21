class Rotor2:
    def __init__(self, rotor1_start, rotor2_start):
        self.start_rotor1_position = rotor1_start
        self.start_rotor2_position = rotor2_start
        self.rotor1_position = rotor1_start
        self.rotor2_position = rotor2_start
        self.rotor1_size = 96  # ASCII range 32-127
        self.rotor2_size = 96

    def rotate_rotor1(self):
        self.rotor1_position = (self.rotor1_position + 1) % self.rotor1_size
        if self.rotor1_position == 0:
            self.rotate_rotor2()

    def rotate_rotor2(self):
        self.rotor2_position = (self.rotor2_position + 1) % self.rotor2_size

    def encrypt_char(self, char):
        ascii_val = ord(char) - 32  # Normalize to 0-95 range
        encrypted_val = (ascii_val + self.rotor1_position + self.rotor2_position) % self.rotor1_size
        self.rotate_rotor1()
        return chr(encrypted_val + 32)  # Convert back to ASCII range

    def decrypt_char(self, char):
        ascii_val = ord(char) - 32  # Normalize to 0-95 range
        decrypted_val = (ascii_val - self.rotor1_position - self.rotor2_position) % self.rotor1_size
        if decrypted_val < 0:
            decrypted_val += self.rotor1_size
        self.rotate_rotor1()
        return chr(decrypted_val + 32)  # Convert back to ASCII range

    def encrypt_message(self, message):
        self.rotor1_position = self.start_rotor1_position
        self.rotor2_position = self.start_rotor2_position
        return ''.join([self.encrypt_char(c) for c in message])

    def decrypt_message(self, message):
        self.rotor1_position = self.start_rotor1_position
        self.rotor2_position = self.start_rotor2_position
        decrypted_message = []
        for char in message:
            decrypted_message.append(self.decrypt_char(char))
        return ''.join(decrypted_message)
