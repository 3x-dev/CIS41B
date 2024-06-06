class Rotor:
    def __init__(self, start=0x20, end=0x80, initial_char=' '):
        self.start = int(start)
        self.end = int(end)
        self.range_length = self.end - self.start + 1
        self.set_initial_char(initial_char)
        self.reset()

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
        return chr(self.current_position)

    def decrement(self):
        self.current_position = (self.current_position - self.start - 1) % self.range_length + self.start
        if chr(self.current_position) == self.initial_char:
            self.num_rotations += 1
        return chr(self.current_position)

    def execute_n_times(self, n):
        if n >= 0:
            for _ in range(n):
                self.increment()
        else:
            for _ in range(-n):
                self.decrement()

    def get_position_index(self):
        return self.current_position - self.start

    def get_current_char(self):
        return chr(self.current_position)

    def increment_rotation_counter(self):
        return self.num_rotations

    def execute_command(self, command):
        op = command.op
        argv = command.argv

        if op == 0b000:
            self.reset()
        elif op == 0b001:
            return self.increment()
        elif op == 0b010:
            return self.decrement()
        elif op == 0b011:
            self.execute_n_times(argv)
        elif op == 0b100:
            return self.get_position_index()
        elif op == 0b101:
            return self.get_current_char()
        elif op == 0b110:
            return self.increment_rotation_counter()
        elif op == 0b111:
            return "Operation 111 executed"
        else:
            raise ValueError(f"Invalid operation code: {bin(op)}")

    def __str__(self):
        return f"Rotor(position={chr(self.current_position)}, rotations={self.num_rotations})"
    
    def __repr__(self):
        return f"{self.__class__.__name__}(start={self.start}, end={self.end}, initial_char='{self.initial_char}')"
