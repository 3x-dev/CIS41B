import unittest
from Rotor2Class import Rotor2

def brute_force_decryption(encrypted_message):
    common_words = [" THE ", " AND ", " IS ", " OF ", " TO ", " A ", " IN ", " THAT ", " IT "]
    for r1_start in range(96):
        for r2_start in range(96):
            rotor = Rotor2(rotor1_start=r1_start, rotor2_start=r2_start)
            decrypted_message = rotor.decrypt_message(encrypted_message)
            if r1_start % 10 == 0 and r2_start % 10 == 0:
                print(f"Rotor1: {r1_start}, Rotor2: {r2_start}, Decrypted: {decrypted_message[:50]}")
            if any(word in decrypted_message for word in common_words):
                return r1_start, r2_start, decrypted_message
    return None


class TestRotor2(unittest.TestCase):
    def test_brute_force_decryption(self):
        with open('E2Rotor.txt', 'r') as file:
            encrypted_message = file.read()

        result = brute_force_decryption(encrypted_message)
        
        if result:
            r1_start, r2_start, decrypted_message = result
            print(f"Rotor1 Start: {r1_start}, Rotor2 Start: {r2_start}")
            print(f"Decrypted Message: {decrypted_message}")
            self.assertTrue(any(word in decrypted_message for word in [" THE ", " AND ", " IS ", " OF ", " TO ", " A ", " IN ", " THAT ", " IT "]))
        else:
            self.fail("Initial positions not found.")

if __name__ == '__main__':
    unittest.main()