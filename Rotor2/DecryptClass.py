class Decrypter:
    @staticmethod
    def decrypt_character(encrypted_char, rotor1, rotor2, position_index):
        # Calculate hopping value
        x = rotor1.initial_position
        y = rotor2.position
        p = position_index + 1
        h = ((x + p - 1) + ((p - 1) // 95) + y)

        # Step 2
        encrypted_index = ord(encrypted_char) - 0x20
        d = (encrypted_index - h) % 95

        # Step 3
        decrypted_index = d + 0x20
        decrypted_char = chr(decrypted_index)
        
        return decrypted_char

    @staticmethod
    def decrypt_text(encrypted_text, rotor1, rotor2):
        decrypted_text = ""
        for i, char in enumerate(encrypted_text):
            decrypted_text += Decrypter.decrypt_character(char, rotor1, rotor2, i)
            rotor1.rotate()
            if rotor1.position == rotor1.initial_position:
                rotor2.rotate()
        return decrypted_text