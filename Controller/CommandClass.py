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
