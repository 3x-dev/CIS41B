class Rotor:
    def __init__(self, initial_position):
        self.position = initial_position
    
    def rotate(self):
        self.position = (self.position + 1) % 96  # Assuming 96 characters in the ASCII table used

def decrypt_character(encrypted_char, rotor1, rotor2):
    encrypted_index = ord(encrypted_char) - 32
    decrypted_index = (encrypted_index - rotor1.position - rotor2.position) % 96
    decrypted_char = chr(decrypted_index + 32)
    return decrypted_char

def find_initial_settings(encrypted_text):
    for initial_position1 in range(96):
        for initial_position2 in range(96):
            rotor1 = Rotor(initial_position1)
            rotor2 = Rotor(initial_position2)
            decrypted_text = ""
            for char in encrypted_text:
                decrypted_char = decrypt_character(char, rotor1, rotor2)
                decrypted_text += decrypted_char
                rotor1.rotate()
                if rotor1.position == 0:
                    rotor2.rotate()
            if " the " in decrypted_text or " and " in decrypted_text:
                print(f"Possible decryption with Rotor1: {initial_position1} and Rotor2: {initial_position2}")
                print(decrypted_text[:100])  # Print the first 100 characters for debugging
                return decrypted_text
    return None

def read_encrypted_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

if __name__ == '__main__':
    encrypted_text = read_encrypted_file('/mnt/data/E2Rotor.txt')
    find_initial_settings(encrypted_text)