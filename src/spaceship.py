class Spaceship:
    def __init__(self, x=0, y=0, z=0, direction='N'):
        self.x = x
        self.y = y
        self.z = z
        self.direction = direction

    def move_forward(self):
        if self.direction == 'N':
            self.y += 1
        elif self.direction == 'S':
            self.y -= 1
        elif self.direction == 'E':
            self.x += 1
        elif self.direction == 'W':
            self.x -= 1
        elif self.direction == 'Up':
            self.z += 1
        elif self.direction == 'Down':
            self.z -= 1

    def move_backward(self):
        if self.direction == 'N':
            self.y -= 1
        elif self.direction == 'S':
            self.y += 1
        elif self.direction == 'E':
            self.x -= 1
        elif self.direction == 'W':
            self.x += 1
        elif self.direction == 'Up':
            self.z -= 1
        elif self.direction == 'Down':
            self.z += 1

    def turn_left(self):
        if self.direction == 'N':
            self.direction = 'W'
        elif self.direction == 'S':
            self.direction = 'E'
        elif self.direction == 'E':
            self.direction = 'N'
        elif self.direction == 'W':
            self.direction = 'S'

    def turn_right(self):
        if self.direction == 'N':
            self.direction = 'E'
        elif self.direction == 'S':
            self.direction = 'W'
        elif self.direction == 'E':
            self.direction = 'S'
        elif self.direction == 'W':
            self.direction = 'N'

    def turn_up(self):
        self.direction = 'Up'

    def turn_down(self):
        self.direction = 'Down'

    def get_position(self):
        return self.x, self.y, self.z

    def get_direction(self):
        return self.direction

    def execute_command(self, command):
        if command == 'f':
            self.move_forward()
        elif command == 'b':
            self.move_backward()
        elif command == 'l':
            self.turn_left()
        elif command == 'r':
            self.turn_right()
        elif command == 'u':
            self.turn_up()
        elif command == 'd':
            self.turn_down()
        else:
            raise ValueError('Invalid command')
