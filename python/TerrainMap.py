from Map import Map
from Surroundings import Surroundings
from TerrainTile import TerrainTile
from Point import Point
from Direction import Direction
from State import State


class TerrainMap(Map):
    @staticmethod
    def read_file(file_name):
        # type: (string) -> Character[]
        return [line.rstrip('\n') for line in open(file_name)]

    @staticmethod
    def flatten_array(array):
        # type: (String[]) -> Character[]
        return [char for line in array for char in line]

    def __init__(self, file_name):
        # type: (String) -> self
        array = TerrainMap.read_file(file_name)
        height = len(array)
        width = len(array[0])
        array = TerrainMap.flatten_array(array)
        terrain_array = [TerrainTile(type) for type in array]
        super(TerrainMap, self).__init__(terrain_array, width, height)

    def get_all_traversable_states(self):
        states = []
        for x in range(self.width):
            for y in range(self.height):
                pnt = Point(x, y)
                ndx = Map.point_to_index(pnt, self.width, self.height)
                terrain = self.map[ndx]
                if terrain.isTraversable():
                    for dir in Direction.Directions:
                        state = State(pnt, dir)
                        states.append(state)
        return states
