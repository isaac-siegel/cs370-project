class State(object):
    def __init__(self, point, direction):
        # type: (point, direction) -> self
        self.point = point
        self.direction = direction

    def __eq__(self, other):
        # type: (State) -> Boolean
        return self.point == other.point and self.direction == other.direction

    def __str__(self):
        # type: () -> String
        return "(" + str(self.point) + ", " + str(self.direction) + ")"

# from python import Direction as Direction
# from python import Point as Point
# d1 = Direction.Direction(Direction.Direction.Directions.NORTH)
# p1 = Point.Point(1,2)
# d2 = Direction.Direction(Direction.Direction.Directions.NORTH)
# p2 = Point.Point(1,2)
# d3 = Direction.Direction(Direction.Direction.Directions.SOUTH)
# p3 = Point.Point(3,2)
# s1 = State(p1, d1)
# s2 = State(p2, d2)
# s3 = State(p3, d3)
#
# print(s1)
# print(s2)
# print(s3)
#
# print(s1 == s2)
# print(s2 == s3)
# print(s3 == s1)

# point
# direction
# toString()
# equals(state)
# Constructor
