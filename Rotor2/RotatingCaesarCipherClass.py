from Rotor2Class import Rotor

class RotatingCaesarCipher:
    def __init__(self, shift):
        self.shift = shift

    def encrypt(self, text):
        result = []

        for char in text:
            rotor = Rotor(initial_char=char)
            for i in range(self.shift):
                rotor.increment()

            result.append (rotor.get_current_char())
            #print("number of rotations: " + str(rotor.counter()))
            rotor.reset()

        return ''.join(result)
    
    def decrypt(self, text):
        result = []

        for char in text:
            rotor = Rotor(initial_char=char)
            for i in range(self.shift):
                rotor.decrement()

            result.append (rotor.get_current_char())
            #print("number of rotations: " + str(rotor.counter()))
            rotor.reset()

        return ''.join(result)

    def __call__(self, text, encrypt=True):
        return self.rotate(text, encrypt)
    
    def __len__(self):
        return self.shift

    def __str__(self):
        return f"RotatingCaesarCipher(shift={self.shift})"
    
    def __repr__(self):
        return f"{self.__class__.__name__}(shift={self.shift})"
    
    def __bool__(self):
        return self.shift != 0

def main():
    cipher = RotatingCaesarCipher(98)
    original = "HELLO"
    encrypted = cipher.encrypt(original)
    print(f"Original: {original}")
    print(f"Encrypted: {encrypted}")
    decrypted = cipher.decrypt(encrypted)
    print(f"Decrypted: {decrypted}")

if __name__ == "__main__":
    main()