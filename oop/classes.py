import os
import random


class Field:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self._food = set()

    def generate_food(self, *, outside_of: 'Snake'):
        r, c = outside_of.cells[0]
        while (r, c) in outside_of.cells:
            r = random.randint(0, self.height - 1)
            c = random.randint(0, self.width - 1)
        self._food.add((r, c))

    def check_new_head(self, cell):
        if cell in self._food:
            self._food.remove(cell)
            return True
        return False

    @property
    def matrix(self):
        output = [['.'] * self.width for _ in range(self.height)]
        for cell in self._food:
            output[cell[0]][cell[1]] = 'O'
        return output


class SnakeIsDeadException(Exception):
    pass


class Snake:
    def __init__(self, name, field: Field):
        self.cells = [(0, 0)]
        self.name = name
        self.field = field

    def draw(self):
        output = self.field.matrix
        for cell in self.cells:
            output[cell[0]][cell[1]] = '*'
        for row in output:
            print(''.join(row))

    # (0, 1), (0, -1), (1, 0), (-1, 0)
    def _move(self, direction):
        head = self.cells[0]
        new_head = (
            (head[0] + direction[0]) % self.field.height,
            (head[1] + direction[1]) % self.field.width
        )
        if new_head in self.cells:
            raise SnakeIsDeadException()

        tail = self.cells[:-1]
        if self.field.check_new_head(new_head):
            tail.append(self.cells[-1])
            self.field.generate_food(outside_of=self)

        self.cells = [new_head] + tail

    def __str__(self):
        return f'Snake {self.name} ({len(self.cells)} cells)'


os.system('clear')

field = Field(10, 10)
snake = Snake('Stewart', field)
field.generate_food(outside_of=snake)
print(snake)

snake.draw()
# Snake.print(snake)  # одно и то же

DIRS = {
    '<': (0, -1),
    '>': (0, 1),
    '^': (-1, 0),
    'v': (1, 0)
}

while True:
    cmd = input()
    os.system('clear')
    if cmd == 'exit': break
    try:
        snake._move(DIRS[cmd])
        snake.draw()
    except SnakeIsDeadException:
        print('Wasted')
        break
