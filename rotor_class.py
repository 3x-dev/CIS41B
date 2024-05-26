class Rotor:
    def __init__(self, start=0x20, end=0x80, initial_char=' '):
        self.start = int(start)
        self.end = int(end)
        self.range_length = self.end - self.start + 1
        self.set_initial_char(initial_char)

        self.current_position = ord(self.initial_char)
        self.num_rotations = 0

    def set_initial_char(self, initial_char):
        if not (self.start <= ord(initial_char) <= self.end):
            raise ValueError(f"Initial character must be within ASCII range {chr(self.start)} to {chr(self.end)}")
        self.initial_char = initial_char

    def reset(self):
        self.current_position = ord(self.initial_char)
        self.num_rotations = 0

    def increment(self):
        self.current_position = (self.current_position - self.start + 1) % self.range_length + self.start
        if chr(self.current_position) == self.initial_char:
            self.num_rotations += 1

    def decrement(self):
        self.current_position = (self.current_position - self.start - 1) % self.range_length + self.start
        if chr(self.current_position) == self.initial_char:
            self.num_rotations += 1

    def counter(self):
        return self.num_rotations

    def get_current_char(self):
        return chr(self.current_position)

    def __str__(self):
        return f"Rotor(position={chr(self.current_position)}, rotations={self.num_rotations})"
    
    def __repr__(self):
        return f"{self.__class__.__name__}(start={self.start}, end={self.end}, initial_char='{self.initial_char}')"