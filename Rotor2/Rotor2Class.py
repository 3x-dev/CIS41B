class Rotor2:
    def __init__(self, initial_position_rotor1, initial_position_rotor2):
        self.rotor1_position = initial_position_rotor1
        self.rotor1_initial_position = initial_position_rotor1
        self.rotor2_position = initial_position_rotor2
        self.rotor2_initial_position = initial_position_rotor2

    def __str__(self):
        return f"Rotor2(rotor1_position={self.rotor1_position}, rotor2_position={self.rotor2_position})"

    def __repr__(self):
        return f"Rotor2({self.rotor1_initial_position}, {self.rotor2_initial_position})"

    def __eq__(self, other):
        if isinstance(other, Rotor2):
            return (self.rotor1_position == other.rotor1_position and 
                    self.rotor2_position == other.rotor2_position)
        return False

    def reset(self):
        self.rotor1_position = self.rotor1_initial_position
        self.rotor2_position = self.rotor2_initial_position

    def rotate_rotor1(self):
        self.rotor1_position = (self.rotor1_position + 1) % 96

    def rotate_rotor2(self):
        self.rotor2_position = (self.rotor2_position + 1) % 96

    def decrypt_character(self, encrypted_char, position_index):
        # Calculate hopping value
        x = self.rotor1_initial_position
        y = self.rotor2_position
        p = position_index + 1
        h = ((x + p - 1) + ((p - 1) // 95) + y)

        # Step 2
        encrypted_index = ord(encrypted_char) - 0x20
        d = (encrypted_index - h) % 95

        # Step 3
        decrypted_index = d + 0x20
        decrypted_char = chr(decrypted_index)
        
        return decrypted_char

    def decrypt_text(self, encrypted_text):
        decrypted_text = ""
        for i, char in enumerate(encrypted_text):
            decrypted_text += self.decrypt_character(char, i)
            self.rotate_rotor1()
            if self.rotor1_position == self.rotor1_initial_position:
                self.rotate_rotor2()
        return decrypted_text

    def set_initial_positions(self, position1, position2):
        self.rotor1_initial_position = position1
        self.rotor2_initial_position = position2
        self.reset()

    def get_positions(self):
        return self.rotor1_position, self.rotor2_position

    def get_initial_positions(self):
        return self.rotor1_initial_position, self.rotor2_initial_position