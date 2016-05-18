from enum import Enum


class Direction(object):

    class Directions(Enum):
        NORTH = 1
        EAST = 2
        SOUTH = 3
        WEST = 4

    def __init__(self, direction):
        # type: (Directions) -> self
        self.direction = direction

    def __eq__(self, other):
        # type: (Direction) -> Boolean
        return self.direction == other.direction

    def __str__(self):
        # type: () -> String
        return "(" + str(self.direction) + ")"

# d1 = Direction(Direction.Directions.NORTH)
# d2 = Direction(Direction.Directions['EAST'])
# d3 = Direction(Direction.Directions.EAST)
#
# print(d1)
# print(d2)
# print(d3)
#
# print(d1 == d2)
#print(d2 == d3)




# ENUM N,E,S,W
# Constructor
# Getter
# Comparator (equals)
# ToString()