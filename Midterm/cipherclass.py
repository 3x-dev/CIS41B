class RotatingCaesarCipher:
    def __init__(self, shift):
        """
        Initializes a new RotatingCaesarCipher object with a specified initial shift.
        
        :param shift: The initial shift for the cipher, determining how many places each character will be shifted.
        """
        self.initial_shift = shift

    def __str__(self):
        """
        Provides a string representation of the RotatingCaesarCipher object.
        
        :return: A string indicating the current shift of the cipher.
        """
        return f"RotatingCaesarCipher(shift={self.initial_shift})"

    def __repr__(self):
        """
        Provides an official string representation of the RotatingCaesarCipher object.
        
        :return: A string that could be used to recreate the object with its initial shift.
        """
        return f"{self.__class__.__name__}(initial_shift={self.initial_shift})"

    def rotate(self, text, mode='encrypt'):
        """
        Rotates each character in the given text by an increasing shift, either encrypting or decrypting.
        
        :param text: The text to be encrypted or decrypted.
        :param mode: A string specifying the mode of operation; 'encrypt' or 'decrypt'.
        :return: The transformed text after applying the rotating cipher.
        """
        current_shift = self.initial_shift
        result_text = ""
        for char in text:
            if mode == 'encrypt':
                new_value = 0x20 + (ord(char) + current_shift - 0x20) % (0x80 - 0x20 + 1)
            else:
                new_value = 0x20 + (ord(char) - current_shift - 0x20) % (0x80 - 0x20 + 1)

            result_text += chr(new_value)
            current_shift += 1
        return result_text

    def encrypt(self, plain_text):
        """
        Encrypts the provided text using the rotating cipher method.
        
        :param plain_text: The plain text to encrypt.
        :return: The encrypted text.
        """
        return self.rotate(plain_text, mode='encrypt')

    def decrypt(self, encrypted_text):
        """
        Decrypts the provided text that was encrypted using the rotating cipher method.
        
        :param encrypted_text: The text to decrypt.
        :return: The decrypted text.
        """
        return self.rotate(encrypted_text, mode='decrypt')

def main():
    cipher = RotatingCaesarCipher(5)
    
    encrypted = cipher.encrypt("HELLO")
    decrypted = cipher.decrypt(encrypted)

    print("Encrypted message:", encrypted)
    print("Decrypted message:", decrypted)

if __name__ == "__main__":
    main()
