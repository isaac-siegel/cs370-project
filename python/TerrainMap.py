from Map import Map
from Surroundings import Surroundings
from TerrainTile import TerrainTile


class TerrainMap(Map):
    @staticmethod
    def read_file(file_name):
        # type: (string) -> Character[]
        return [line.rstrip('\n') for line in open(file_name)]

    @staticmethod
    def flatten_array(array):
        # type: (String[]) -> Character[]
        return [char for line in array for char in line]

    def get_surroundings(self, point):
        # type: (Point) -> Surroundings
        return Surroundings(*self.get_neighbors(point))

    def __init__(self, file_name):
        # type: (String) -> self
        array = TerrainMap.read_file(file_name)
        height = len(array)
        width = len(array[0])
        array = TerrainMap.flatten_array(array)
        terrain_array = [TerrainTile(type) for type in array]
        super(TerrainMap, self).__init__(terrain_array, width, height)