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

    @staticmethod
    def move_to_direction(facing_direction, movement):
        # untested
        facing_north_go_forward =  facing_direction == Directions.NORTH and movement == Moves.FORWARD
        facing_north_go_backward = facing_direction == Directions.NORTH and movement == Moves.BACKWARD
        facing_north_go_left =     facing_direction == Directions.NORTH and movement == Moves.LEFT
        facing_north_go_right =    facing_direction == Directions.NORTH and movement == Moves.RIGHT

        facing_south_go_forward =  facing_direction == Directions.SOUTH and movement == Moves.FORWARD
        facing_south_go_backward = facing_direction == Directions.SOUTH and movement == Moves.BACKWARD
        facing_south_go_left =     facing_direction == Directions.SOUTH and movement == Moves.LEFT
        facing_south_go_right =    facing_direction == Directions.SOUTH and movement == Moves.RIGHT

        facing_east_go_forward =   facing_direction == Directions.EAST  and movement == Moves.FORWARD
        facing_east_go_backward =  facing_direction == Directions.EAST  and movement == Moves.BACKWARD
        facing_east_go_left =      facing_direction == Directions.EAST  and movement == Moves.LEFT
        facing_east_go_right =     facing_direction == Directions.EAST  and movement == Moves.RIGHT

        facing_west_go_forward =   facing_direction == Directions.WEST  and movement == Moves.FORWARD
        facing_west_go_backward =  facing_direction == Directions.WEST  and movement == Moves.BACKWARD
        facing_west_go_left =      facing_direction == Directions.WEST  and movement == Moves.LEFT
        facing_west_go_right =     facing_direction == Directions.WEST  and movement == Moves.RIGHT

        if facing_north_go_forward or facing_south_go_backward or facing_west_go_right or facing_east_go_left:
            # Go NORTH
            return Directions.NORTH
        elif facing_north_go_backward or facing_south_go_forward or facing_west_go_left or facing_east_go_right:
            # Go SOUTH
            return Directions.SOUTH

        elif facing_north_go_right or facing_south_go_left or facing_west_go_backward or facing_east_go_forward:
            # Go EAST
            return Directions.EAST
        elif facing_north_go_left or facing_south_go_right or facing_west_go_forward or facing_east_go_backward:
            # Go WEST
            return Directions.WEST

    @staticmethod
    def direction_to_move(facing_direction, move_direction):
        # untested
        facing_north_go_north =  facing_direction == Directions.NORTH and move_direction == Directions.NORTH
        facing_north_go_south =  facing_direction == Directions.NORTH and move_direction == Directions.SOUTH
        facing_north_go_east  =  facing_direction == Directions.NORTH and move_direction == Directions.EAST
        facing_north_go_west  =  facing_direction == Directions.NORTH and move_direction == Directions.WEST

        facing_south_go_north =  facing_direction == Directions.SOUTH and move_direction == Directions.NORTH
        facing_south_go_south =  facing_direction == Directions.SOUTH and move_direction == Directions.SOUTH
        facing_south_go_east  =  facing_direction == Directions.SOUTH and move_direction == Directions.EAST
        facing_south_go_west  =  facing_direction == Directions.SOUTH and move_direction == Directions.WEST

        facing_east_go_north  =  facing_direction == Directions.EAST  and move_direction == Directions.NORTH
        facing_east_go_south  =  facing_direction == Directions.EAST  and move_direction == Directions.SOUTH
        facing_east_go_east   =  facing_direction == Directions.EAST  and move_direction == Directions.EAST
        facing_east_go_west   =  facing_direction == Directions.EAST  and move_direction == Directions.WEST

        facing_west_go_north  =  facing_direction == Directions.WEST  and move_direction == Directions.NORTH
        facing_west_go_south  =  facing_direction == Directions.WEST  and move_direction == Directions.SOUTH
        facing_west_go_east   =  facing_direction == Directions.WEST  and move_direction == Directions.EAST
        facing_west_go_west   =  facing_direction == Directions.WEST  and move_direction == Directions.WEST

        if facing_north_go_north or facing_east_go_east or facing_south_go_south or facing_west_go_west:
            # Go FORWARD
            return Moves.FORWARD
        elif facing_north_go_south or facing_east_go_west or facing_south_go_north or facing_west_go_east:
            # Go BACKWARD
            return Moves.BACKWARD
        elif facing_north_go_west or facing_east_go_north or facing_south_go_east or facing_west_go_south:
            # Go LEFT
            return Moves.LEFT
        elif facing_north_go_east  or facing_east_go_south or facing_south_go_west or facing_west_go_north:
            # Go RIGHT
            return Moves.RIGHT


    def move(self, movement):
        move_direction = self.move_to_direction(self.direction, movement)

        self.point.move(move_direction)
        self.direction = move_direction


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
