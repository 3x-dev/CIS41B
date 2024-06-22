class Rotor:
    def __init__(self, initial_position):
        self.position = initial_position
        print(f"Rotor initialized at position {self.position}")
    
    def rotate(self):
        self.position = (self.position + 1) % 96
        print(f"Rotor rotated to position {self.position}")

def decrypt_character(encrypted_char, rotor1, rotor2, position_index):
    # Step 1: Calculate hopping value
    x = rotor1.position
    y = rotor2.position
    p = position_index + 1
    h = ((x + p - 1) + ((p - 1) % 96) + y)

    # Step 2
    encrypted_index = ord(encrypted_char)
    o = (encrypted_index - h) % 96

    # Step 3
    decrypted_index = o + 0x20
    decrypted_char = chr(decrypted_index)
    
    print(f"Decrypting char '{encrypted_char}' to '{decrypted_char}' with Rotor1: {rotor1.position} and Rotor2: {rotor2.position}, position index: {position_index}")
    return decrypted_char

def is_meaningful_text(text):
    # Check for common English words and overall sense of the text
    common_words = ['the', 'math', 'and', 'comp', 'Alan', 'alan', 'that']
    word_count = sum(word in text for word in common_words)
    return word_count > 3  # Adjust threshold based on expected length of meaningful text

def find_initial_settings(encrypted_text):
    for initial_position1 in range(0x20, 0x7F + 1):
        for initial_position2 in range(0x20, 0x7F + 1):
            rotor1 = Rotor(initial_position1)
            rotor2 = Rotor(initial_position2)
            decrypted_text = ""
            for i, char in enumerate(encrypted_text):
                decrypted_text += decrypt_character(char, rotor1, rotor2, i)
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
    encrypted_text = read_encrypted_file('test.txt')
    find_initial_settings(encrypted_text)
