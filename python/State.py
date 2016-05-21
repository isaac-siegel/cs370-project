from Direction import Direction
from Moves import Moves
from Point import Point


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

    def move(self, movement):
        facing_north_go_forward = self.direction == Direction(Direction.Directions.NORTH) and movement == Moves.FORWARD
        facing_north_go_backward = self.direction == Direction(
            Direction.Directions.NORTH) and movement == Moves.BACKWARD
        facing_north_go_left = self.direction == Direction(Direction.Directions.NORTH) and movement == Moves.LEFT
        facing_north_go_right = self.direction == Direction(Direction.Directions.NORTH) and movement == Moves.RIGHT
        facing_south_go_forward = self.direction == Direction(Direction.Directions.SOUTH) and movement == Moves.FORWARD
        facing_south_go_backward = self.direction == Direction(
            Direction.Directions.SOUTH) and movement == Moves.BACKWARD
        facing_south_go_left = self.direction == Direction(Direction.Directions.SOUTH) and movement == Moves.LEFT
        facing_south_go_right = self.direction == Direction(Direction.Directions.SOUTH) and movement == Moves.RIGHT
        facing_east_go_forward = self.direction == Direction(Direction.Directions.EAST) and movement == Moves.FORWARD
        facing_east_go_backward = self.direction == Direction(Direction.Directions.EAST) and movement == Moves.BACKWARD
        facing_east_go_left = self.direction == Direction(Direction.Directions.EAST) and movement == Moves.LEFT
        facing_east_go_right = self.direction == Direction(Direction.Directions.EAST) and movement == Moves.RIGHT
        facing_west_go_forward = self.direction == Direction(Direction.Directions.WEST) and movement == Moves.FORWARD
        facing_west_go_backward = self.direction == Direction(Direction.Directions.WEST) and movement == Moves.BACKWARD
        facing_west_go_left = self.direction == Direction(Direction.Directions.WEST) and movement == Moves.LEFT
        facing_west_go_right = self.direction == Direction(Direction.Directions.WEST) and movement == Moves.RIGHT

        if facing_north_go_forward or facing_south_go_backward or facing_west_go_right or facing_east_go_left:
            # Go NORTH
            self.point.x += 0
            self.point.y += -1
            self.direction = Direction(Direction.Directions.NORTH)
        elif facing_north_go_backward or facing_south_go_forward or facing_west_go_left or facing_east_go_right:
            # Go SOUTH
            self.point.x += 0
            self.point.y += 1
            self.direction = Direction(Direction.Directions.SOUTH)

        elif facing_north_go_right or facing_south_go_left or facing_west_go_backward or facing_east_go_forward:
            # Go EAST
            self.point.x += 1
            self.point.y += 0
            self.direction = Direction(Direction.Directions.EAST)
        elif facing_north_go_left or facing_south_go_right or facing_west_go_forward or facing_east_go_backward:
            # Go WEST
            self.point.x += -1
            self.point.y += 0
            self.direction = Direction(Direction.Directions.WEST)
    @staticmethod
    def copy(state):
        point = Point(state.point.x, state.point.y)
        direction = Direction(state.direction.direction)
        return State(point, direction)

# from python.Direction import Direction
# from python.Point import Point
# d1 = Direction(Direction.Directions.NORTH)
# p1 = Point(1,2)
# d2 = Direction(Direction.Directions.NORTH)
# p2 = Point(1,2)
# d3 = Direction(Direction.Directions.SOUTH)
# p3 = Point(3,2)
# s1 = State(p1, d1)
# s2 = State(p2, d2)
# s3 = State(p3, d3)
# #
# print(s1)
# print(s2)
# print(s3)
# #
#
# print("===TEST MOVE===")
#
# print("Move Backward")
# print(s1)
# s1.move(Moves.BACKWARD)
# print(s1)
#
# print()
#
# print("Move Left")
# print(s2)
# s2.move(Moves.LEFT)
# print(s2)
#
# print()
#
# print("Move Right")
# print(s2)
# s2.move(Moves.RIGHT)
# print(s2)

#
# print(s1 == s2)
# print(s2 == s3)
# print(s3 == s1)

# point
# direction
# toString()
# equals(state)
# Constructor
