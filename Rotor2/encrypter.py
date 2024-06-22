class Rotor:
    def __init__(self, initial_position):
        self.position = initial_position
        self.initial_position = initial_position
    
    def rotate(self):
        self.position = (self.position + 1) % 96

def encrypt_character(original_char, rotor1, rotor2, position_index):
    # Calculate hopping value
    x = rotor1.position
    y = rotor2.position
    p = position_index + 1
    h = ((x + p - 1) + ((p - 1) % 96) + y)

    # Step 2
    original_index = ord(original_char) - 0x20
    e = (original_index + h) % 96

    # Step 3
    encrypted_index = e + 0x20
    encrypted_char = chr(encrypted_index)
    
    return encrypted_char

def encrypt_text(original_text, rotor1_initial, rotor2_initial):
    rotor1 = Rotor(rotor1_initial)
    rotor2 = Rotor(rotor2_initial)
    encrypted_text = ""
    for i, char in enumerate(original_text):
        encrypted_text += encrypt_character(char, rotor1, rotor2, i)
        rotor1.rotate()
        if rotor1.position == rotor1.initial_position:
            rotor2.rotate()
    return encrypted_text

# Test the encryption on "hello"
original_text = "the"
rotor1_initial = 34  # Example initial position for Rotor1
rotor2_initial = 39  # Example initial position for Rotor2
encrypted_text = encrypt_text(original_text, rotor1_initial, rotor2_initial)
print(f"Original text: {original_text}")
print(f"Encrypted text: {encrypted_text}")
