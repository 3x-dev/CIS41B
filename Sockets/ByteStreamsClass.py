import binascii
from typing import List

class StringConverter:
    def __init__(self, input_string: str = ""):
        self._input_string = input_string
        self._byte_array = self._to_byte_array()
        self._bit_string = self._to_bit_string()

    def _to_byte_array(self) -> bytearray:
        return bytearray(self._input_string, 'utf-8')

    def _to_bit_string(self) -> str:
        if self._input_string:
            bits = bin(int(binascii.hexlify(self._input_string.encode('utf-8')), 16))[2:]
            return bits.zfill(8 * ((len(bits) + 7) // 8))
        return ""

    def to_byte(self) -> bytes:
        return bytes(self._input_string, 'utf-8')

    def to_byte_array(self) -> bytearray:
        return self._byte_array

    def to_bit_string(self) -> str:
        return self._bit_string

    def from_byte(self, byte_data: bytes) -> str:
        return byte_data.decode('utf-8')

    def from_byte_array(self, byte_array_data: bytearray) -> str:
        return byte_array_data.decode('utf-8')

    def from_bit_string(self, bit_string: str) -> str:
        if bit_string:
            n = int(bit_string, 2)
            return binascii.unhexlify('%x' % n).decode('utf-8')
        return ""

    def send_byte_stream(self, stream) -> None:
        stream.send(self.to_byte())

    def receive_byte_stream(self, stream) -> str:
        received_data = stream.recv(1024)
        return self.from_byte(received_data)

    def __str__(self) -> str:
        return f'StringConverter(input_string="{self._input_string}")'

    def __iter__(self):
        return iter(self._byte_array)

    def set_input_string(self, input_string: str) -> None:
        self._input_string = input_string
        self._byte_array = self._to_byte_array()
        self._bit_string = self._to_bit_string()

    def get_input_string(self) -> str:
        return self._input_string
