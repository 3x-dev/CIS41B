class Rotor:
    def __init__(self, initial_position):
        self.position = initial_position
        print(f"Rotor initialized at position {self.position}")
    
    def rotate(self):
        self.position = (self.position + 1) % 96
        print(f"Rotor rotated to position {self.position}")

def decrypt_character(encrypted_char, rotor1, rotor2):
    encrypted_index = ord(encrypted_char) - 32
    decrypted_index = (encrypted_index - rotor1.position - rotor2.position) % 96
    decrypted_char = chr(decrypted_index + 32)
    print(f"Decrypting char '{encrypted_char}' to '{decrypted_char}' with Rotor1: {rotor1.position} and Rotor2: {rotor2.position}")
    return decrypted_char

def is_meaningful_text(text):
    # Check for common English words and overall sense of the text
    common_words = ['the', 'and', 'is', 'in', 'it', 'you', 'that', 'he', 'was', 'for', 'on', 'are', 'with', 'as', 'I', 'his', 'they', 'be', 'at', 'one', 'have', 'this', 'from']
    word_count = sum(word in text for word in common_words)
    return word_count > 10  # Adjust threshold based on expected length of meaningful text

def find_initial_settings(encrypted_text, subset_length=500):
    subset_text = encrypted_text[:subset_length]
    for initial_position1 in range(96):
        for initial_position2 in range(96):
            rotor1 = Rotor(initial_position1)
            rotor2 = Rotor(initial_position2)
            decrypted_text = ""
            for char in subset_text:
                decrypted_text += decrypt_character(char, rotor1, rotor2)
                rotor1.rotate()
                if rotor1.position == 0:
                    rotor2.rotate()
            if is_meaningful_text(decrypted_text):
                print(f"Possible decryption with Rotor1: {initial_position1} and Rotor2: {initial_position2}")
                print(decrypted_text)
                return decrypted_text
    return None

def read_encrypted_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

if __name__ == '__main__':
    encrypted_text = read_encrypted_file('E2Rotor.txt')
    find_initial_settings(encrypted_text)
