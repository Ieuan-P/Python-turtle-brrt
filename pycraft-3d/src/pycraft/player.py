class Player:
    def __init__(self, position=(0, 0, 0), speed=5.0):
        self.position = list(position)
        self.speed = speed

    def move(self, direction):
        if direction == 'forward':
            self.position[2] -= self.speed
        elif direction == 'backward':
            self.position[2] += self.speed
        elif direction == 'left':
            self.position[0] -= self.speed
        elif direction == 'right':
            self.position[0] += self.speed
        elif direction == 'up':
            self.position[1] += self.speed
        elif direction == 'down':
            self.position[1] -= self.speed

    def get_position(self):
        return tuple(self.position)

    def set_position(self, position):
        self.position = list(position)