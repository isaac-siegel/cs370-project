from Directions import Directions
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
        facing_north_go_forward =  self.direction == Directions.NORTH and movement == Moves.FORWARD
        facing_north_go_backward = self.direction == Directions.NORTH and movement == Moves.BACKWARD
        facing_north_go_left =     self.direction == Directions.NORTH and movement == Moves.LEFT
        facing_north_go_right =    self.direction == Directions.NORTH and movement == Moves.RIGHT

        facing_south_go_forward =  self.direction == Directions.SOUTH and movement == Moves.FORWARD
        facing_south_go_backward = self.direction == Directions.SOUTH and movement == Moves.BACKWARD
        facing_south_go_left =     self.direction == Directions.SOUTH and movement == Moves.LEFT
        facing_south_go_right =    self.direction == Directions.SOUTH and movement == Moves.RIGHT

        facing_east_go_forward =   self.direction == Directions.EAST  and movement == Moves.FORWARD
        facing_east_go_backward =  self.direction == Directions.EAST  and movement == Moves.BACKWARD
        facing_east_go_left =      self.direction == Directions.EAST  and movement == Moves.LEFT
        facing_east_go_right =     self.direction == Directions.EAST  and movement == Moves.RIGHT

        facing_west_go_forward =   self.direction == Directions.WEST  and movement == Moves.FORWARD
        facing_west_go_backward =  self.direction == Directions.WEST  and movement == Moves.BACKWARD
        facing_west_go_left =      self.direction == Directions.WEST  and movement == Moves.LEFT
        facing_west_go_right =     self.direction == Directions.WEST  and movement == Moves.RIGHT

        if facing_north_go_forward or facing_south_go_backward or facing_west_go_right or facing_east_go_left:
            # Go NORTH
            self.point.x += 0
            self.point.y += -1
            self.direction = Directions.NORTH
        elif facing_north_go_backward or facing_south_go_forward or facing_west_go_left or facing_east_go_right:
            # Go SOUTH
            self.point.x += 0
            self.point.y += 1
            self.direction = Directions.SOUTH

        elif facing_north_go_right or facing_south_go_left or facing_west_go_backward or facing_east_go_forward:
            # Go EAST
            self.point.x += 1
            self.point.y += 0
            self.direction = Directions.EAST
        elif facing_north_go_left or facing_south_go_right or facing_west_go_forward or facing_east_go_backward:
            # Go WEST
            self.point.x += -1
            self.point.y += 0
            self.direction = Directions.WEST
    @staticmethod
    def copy(state):
        point = Point(state.point.x, state.point.y)
        direction = state.direction
        return State(point, direction)

# point
# direction
# toString()
# equals(state)
# Constructor
