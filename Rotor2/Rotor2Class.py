class Rotor:
    def __init__(self, initial_position):
        self.position = initial_position
        self.initial_position = initial_position

    def rotate(self):
        self.position = (self.position + 1) % 96