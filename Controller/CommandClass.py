class Command:
    def __init__(self, op, argv):
        self.op = op
        self.argv = argv

    def _set(self, cmd):
        self.op = cmd['op']
        self.argv = cmd['argv']

    def _get(self):
        return {'op': self.op, 'argv': self.argv}

    def __str__(self):
        return f"Command(op={bin(self.op)}, argv={self.argv})"

    def add(self, other_command):
        if isinstance(other_command, Command):
            return Command(self.op | other_command.op, self.argv + other_command.argv)
        raise ValueError("Can only add another Command instance")

    def multiply(self, factor):
        if isinstance(factor, int):
            return Command(self.op, self.argv * factor)
        raise ValueError("Factor must be an integer")
    
    def invert_op(self):
        return Command(~self.op & 0b111, self.argv)
    
    def increment_op(self):
        return Command((self.op + 1) % 8, self.argv)
