from Directions import Directions

MAX_SIZE = 100000

class Point(object):
    def __init__(self, x, y):
        # type: (int, int) -> self
        self.x = x
        self.y = y

    def __eq__(self, other):
        # type: (Point) -> Boolean
        if other is None:
            return False
        return self.x == other.x and self.y == other.y

    def __str__(self):
        # type: () -> String
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    def __hash__(self):
        return self.x * MAX_SIZE * 10 + self.y

    def move(self, move_direction):
        if move_direction == Directions.NORTH:
            self.x += 0
            self.y += -1
        elif move_direction == Directions.SOUTH:
            self.x += 0
            self.y += 1
        elif move_direction == Directions.EAST:
            self.x += 1
            self.y += 0
        elif move_direction == Directions.WEST:
            self.x += -1
            self.y += 0