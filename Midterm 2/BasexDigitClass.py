from BaseConverterClass import BaseConverter

class BaseXDigit:
    def __init__(self, base_prefixed_number):
        self.converter = BaseConverter()
        self.base_prefixed_number = base_prefixed_number
        self.base, self.number = self.converter.detect_base(base_prefixed_number)
        self.decimal_value = self.converter.any_base_to_decimal(self.number, self.base)

    def to_base10(self):
        return f"0A{self.decimal_value}"

    def __add__(self, other):
        if not isinstance(other, BaseXDigit):
            raise ValueError("Operands must be BaseXDigit instances")
        result_decimal = self.decimal_value + other.decimal_value
        return BaseXDigit(f"0A{result_decimal}")

    def __sub__(self, other):
        if not isinstance(other, BaseXDigit):
            raise ValueError("Operands must be BaseXDigit instances")
        result_decimal = self.decimal_value - other.decimal_value
        return BaseXDigit(f"0A{result_decimal}")

    def __mul__(self, other):
        if not isinstance(other, BaseXDigit):
            raise ValueError("Operands must be BaseXDigit instances")
        result_decimal = self.decimal_value * other.decimal_value
        return BaseXDigit(f"0A{result_decimal}")

    def __mod__(self, other):
        if not isinstance(other, BaseXDigit):
            raise ValueError("Operands must be BaseXDigit instances")
        result_decimal = self.decimal_value % other.decimal_value
        return BaseXDigit(f"0A{result_decimal}")

    def to_base(self, target_base):
        base_10_value = self.decimal_value
        converted_value = self.converter.decimal_to_any_base(base_10_value, target_base)
        return self.converter.prepend_base_prefix(converted_value, target_base)

    def __str__(self):
        return self.base_prefixed_number
