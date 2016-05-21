from Point import Point
from State import State


class Map(object):
    NEIGHBORING_INDEX_MODIFIERS = [[-1, 0], [0, -1], [1, 0], [0, 1]]

    def __init__(self, map, width, height):
        # type: (Object[], int, int) -> self
        self.width = width
        self.height = height
        self.map = map

    def get_tile(self, point):
        # type: (Point) -> Object
        if point is None:
            return None
        if self.map is None:
            raise TypeError("map is null")
        return self.map[Map.point_to_index(point, self.height, self.width)]

    def get_neighbors(self, point):
        # type: (Point, int, int) -> object[]
        if Map.is_valid_point(point, self.width, self.height):
            new_points = []
            for index_modifiers in Map.NEIGHBORING_INDEX_MODIFIERS:
                new_x = point.x + index_modifiers[0]
                new_y = point.y + index_modifiers[1]

                new_point = Point(new_x, new_y)
                if Map.is_valid_point(new_point, self.width, self.height):
                    new_points.append(new_point)
                else:
                    new_points.append(None)

            neighbors = {}
            neighbors["WEST"] = new_points[0]
            neighbors["NORTH"] = new_points[1]
            neighbors["EAST"] = new_points[2]
            neighbors["SOUTH"] = new_points[3]
            #WNES
            return neighbors
        else:
            print(point)
            raise IndexError

    def __str__(self):
        to_string = ""
        for i in range(self.height):
            to_string += "["
            for j in range(self.width):
                if j == self.width - 1:
                    to_string += str(self.map[i * self.width + j])
                else:
                    to_string += str(self.map[i * self.width + j]) + ", "
            to_string += "]\n"
        return to_string

    def is_valid_state(self, state):
        return self.is_valid_point(state.point, self.width, self.height)

    def is_valid_move(self, state, movement):
        move_state = State.copy(state)
        move_state.move(movement)
        return self.is_valid_state(move_state)


    @staticmethod
    def point_to_index(point, width, height):
        # type: (Point, int, int) -> int
        if Map.is_valid_point(point, width, height):
            return point.y * width + point.x
        else:
            raise IndexError

    @staticmethod
    def is_valid_point(point, width, height):
        # type: (Point, int, int) -> Boolean
        return height > point.y >= 0 and width > point.x >= 0
