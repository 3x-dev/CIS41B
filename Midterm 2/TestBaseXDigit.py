import unittest
from BasexDigitClass import BaseXDigit

class TestBaseXDigit(unittest.TestCase):
    def setUp(self):
        self.bP = BaseXDigit("0P123")  # Base 25
        self.bJ = BaseXDigit("0J987")  # Base 19

    def test_addition(self):
        bPJ = self.bP + self.bJ
        self.assertEqual(bPJ.to_base10(), "0A4092")

    def test_subtraction(self):
        bPJ = self.bP + self.bJ
        bP_new = bPJ - self.bJ
        self.assertEqual(bP_new.to_base10(), self.bP.to_base10())

    def test_multiplication(self):
        result = self.bP * self.bJ
        self.assertEqual(result.to_base10(), "0A118848")

    def test_modulo(self):
        result = self.bP % self.bJ
        self.assertEqual(result.to_base10(), "0A123")

    def test_to_base(self):
        self.assertEqual(self.bP.to_base(16), "0G2H3")

if __name__ == "__main__":
    unittest.main()