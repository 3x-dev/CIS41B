class Rotor:
    def __init__(self, initial_position):
        self.position = initial_position
        self.initial_position = initial_position
    
    def rotate(self):
        self.position = (self.position + 1) % 96

def encrypt_character(original_char, rotor1, rotor2, position_index):
    # Calculate hopping value
    x = rotor1.initial_position
    y = rotor2.position
    p = position_index + 1
    h = ((x + p - 1) + ((p - 1) // 96) + y)
    # print(f"x: {x}, y: {y}, p: {p}, h: {h}")

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

def decrypt_character(encrypted_char, rotor1, rotor2, position_index):
    # Calculate hopping value
    x = rotor1.initial_position
    y = rotor2.position
    p = position_index + 1
    h = ((x + p - 1) + ((p - 1) // 96) + y)
    #print(f"x: {x}, y: {y}, p: {p}, h: {h}")

    # Step 2
    encrypted_index = ord(encrypted_char) - 0x20
    
    if(encrypted_index > 0x7F):
        print(f"encrypted_index: {encrypted_index}")
    d = (encrypted_index - h) % 96
    # print(f"d: {d}")

    # Step 3
    decrypted_index = d + 0x20
    decrypted_char = chr(decrypted_index)
    
    return decrypted_char

def decrypt_text(encrypted_text, rotor1_initial, rotor2_initial):
    rotor1 = Rotor(rotor1_initial)
    rotor2 = Rotor(rotor2_initial)
    decrypted_text = ""
    for i, char in enumerate(encrypted_text):
        decrypted_text += decrypt_character(char, rotor1, rotor2, i)
        rotor1.rotate()
        if rotor1.position == rotor1.initial_position:
            rotor2.rotate()
    return decrypted_text

def test1():
    top_ten_words = {"the", "be", "to", "of", "and", "a", "in", "that", "have", "I"}

    # Read the original text from test.txt
    with open('test1.txt', 'r') as file:
        original_text = file.read().strip()
        print(f"Original text: {original_text}")

    # Encrypt the text with rotor positions 49 and 50
    encrypted_text = encrypt_text(original_text, 49, 50)
    print(f"Encrypted text: {encrypted_text}")

    found_valid_decryption = False

    for i in range(0x20, 0x80):
        for j in range(0x20, 0x80):
            rotor1_initial = i
            rotor2_initial = j
            
            decrypted_text = decrypt_text(encrypted_text, rotor1_initial, rotor2_initial)
            
            words = decrypted_text.split(' ')
            if any(word in top_ten_words for word in words):
                found_valid_decryption = True
                print(f"Decrypted text with rotor1_initial={rotor1_initial} and rotor2_initial={rotor2_initial}: {decrypted_text}")
                break
        if found_valid_decryption:
            break

    if not found_valid_decryption:
        print("No valid decryption found that contains any of the top ten words.")


def test2():
    top_ten_words = {"the", "be", "to", "of", "and", "a", "in", "that", "have", "I"}
    
    # Read the original text from E2Rotor.txt
    with open('E2Rotor.txt', 'r') as file:
        encrypted_text = file.read()
        print(f"Original text: {encrypted_text}")

    # Iterate over possible initial positions for rotors
    for i in range(0x20, 0x80):
        for j in range(0x20, 0x80):
            rotor1_initial = i  # Example initial position for Rotor1
            rotor2_initial = j  # Example initial position for Rotor2
            
            decrypted_text = decrypt_text(encrypted_text, rotor1_initial, rotor2_initial)
            
            if decrypted_text.startswith("Alan") and any(word in decrypted_text for word in top_ten_words):
                print(f"Decrypted text with rotor1_initial={rotor1_initial} and rotor2_initial={rotor2_initial}: {decrypted_text}")

# Run the test2 function
test2()