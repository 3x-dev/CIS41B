
import math

class RotatingCaesarCipher:
    def __init__(self, shift):
        self.initial_shift = shift

    def encrypt(self, plain_text):
        shift = self.initial_shift
        encrypted_text = ""
        range = 0x80 - 0x20 + 1
        if(shift < 0):
            shift = -(abs(shift) % range)
        else:
            shift = shift % range
        
        for char in plain_text:
            ascii_value = ord(char)
            print(ascii_value)
            new_value = ascii_value + shift
            if(new_value > 0x80):
                diff = new_value - 0x80
                new_value = 0x20 + diff - 1
            elif(new_value < 0x20):
                diff = 0x20 - new_value
                new_value = 0x80 - diff + 1
            encrypted_text += chr(new_value)
            shift += 1
        return encrypted_text

    def decrypt(self, encrypted_text):
        print(self.initial_shift)
        shift = -self.initial_shift
        print(shift)
        decrypted_text = ""
        range = 0x80 - 0x20 + 1
        if(shift < 0):
            shift = -(abs(shift) % range)
        else:
            shift = shift % range

        for char in encrypted_text:
            ascii_value = ord(char)
            
            print(ascii_value)
            new_value = ascii_value + shift
            print(new_value)
            if(new_value > 0x80):
                diff = new_value - 0x80
                new_value = 0x20 + diff - 1
            elif(new_value < 0x20):
                diff = 0x20 - new_value
                new_value = 0x80 - diff + 1
            decrypted_text += chr(new_value)
            shift += 1
        return decrypted_text
    
        
# Example test:
cipher = RotatingCaesarCipher(5)
encrypted = cipher.encrypt('HELLO')
decrypted = cipher.decrypt(encrypted)

print("Encrypted message:", encrypted)
print("Decrypted message:", decrypted)