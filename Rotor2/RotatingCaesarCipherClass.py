import unittest
from Rotor2Class import Rotor2

class TestRotorDecryption(unittest.TestCase):
    def test_decryption(self):
        top_ten_words = {"the", "of", "to", "and", "a", "in", "is", "it", "you", "that"}
        
        # Read the encrypted text file E2Rotor.txt
        with open('E2Rotor.txt', 'r') as file:
            encrypted_text = file.read()
            print(f"Original encrypted text: {encrypted_text}")

        best_match = None
        max_top_ten_word_count = 0

        # Iterate over possible initial positions for rotors
        for i in range(0x20, 0x80):
            for j in range(0x20, 0x80):
                
                rotor2 = Rotor2(i, j)
                decrypted_text = rotor2.decrypt_text(encrypted_text)
                decrypted_words = decrypted_text.split()

                top_ten_word_count = sum(1 for word in decrypted_words if word in top_ten_words)

                if top_ten_word_count > max_top_ten_word_count:
                    max_top_ten_word_count = top_ten_word_count
                    best_match = (i, j, decrypted_text)

        # Print the best match with the most top ten words
        if best_match:
            rotor1_initial, rotor2_initial, decrypted_text = best_match
            print(f"\nBest decrypted text: {decrypted_text}\n\nBest Rotor 1 initial position: {rotor1_initial}\nBest Rotor 2 initial position: {rotor2_initial}")
        else:
            print("\nNo decrypted text contains any of the top ten words.")

if __name__ == '__main__':
    unittest.main()
