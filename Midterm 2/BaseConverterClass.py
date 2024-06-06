import re

class BaseConverter:
    def __init__(self):
        self.digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def char_to_value(self, char):
        return self.digits.index(char)

    def value_to_char(self, value):
        return self.digits[value]

    def any_base_to_decimal(self, number, base):
        number = number.upper()
        decimal_value = 0
        length = len(number)
        for i in range(length):
            decimal_value += self.char_to_value(number[i]) * (base ** (length - i - 1))
        return decimal_value

    def decimal_to_any_base(self, decimal, base):
        if decimal == 0:
            return "0"
        result = ""
        while decimal > 0:
            result = self.value_to_char(decimal % base) + result
            decimal //= base
        return result

    def convert_base(self, number, from_base, to_base):
        if from_base == to_base:
            return number
        decimal_value = self.any_base_to_decimal(number, from_base)
        return self.decimal_to_any_base(decimal_value, to_base)

    def detect_base(self, number):
        match = re.match(r"0([2-9A-Z])(.+)", number)
        if match:
            base_char = match.group(1)
            number_body = match.group(2)
            from_base = self.char_to_value(base_char)
            return from_base, number_body
        raise ValueError("Invalid base prefix")

    def prepend_base_prefix(self, number, base):
        base_char = self.value_to_char(base)
        return f"0{base_char}{number}"

    def convert(self, input_number, target_base):
        from_base, number_body = self.detect_base(input_number)
        converted_number = self.convert_base(number_body, from_base, target_base)
        return self.prepend_base_prefix(converted_number, target_base)
