from Map import Map
from Surroundings import Surroundings
from TerrainTile import TerrainTile
from Point import Point
from Directions import Directions
from State import State
from TerrainTypes import TerrainTypes


class TerrainMap(Map):
    @staticmethod
    def read_file(file_name):
        # type: (string) -> Character[]
        file = open(file_name)
        array = [line.rstrip('\n') for line in file]
        file.close()
        return array

    @staticmethod
    def flatten_array(array):
        # type: (String[]) -> Character[]
        return [char for line in array for char in line]

    def __init__(self, file_name, map_array=None, height=None, width=None, professor_state=None):
        # type: (String) -> self
        if map_array == None:
            array = TerrainMap.read_file(file_name)
            professor_x = int(array[0])
            professor_y = int(array[1])
            professor_direction = Directions(int(array[2]))
            self.professor_start_state = State(Point(professor_x,professor_y), professor_direction)
            array = array[3:] #Removes the first two lines which represent the prof state
            height = len(array)
            width = len(array[0])
            array = TerrainMap.flatten_array(array)
            terrain_array = [TerrainTile(TerrainTypes(int(type))) for type in array]
            super(TerrainMap, self).__init__(terrain_array, width, height)
        else:
            self.professor_start_state = professor_state
            terrain_array = [TerrainTile(TerrainTypes(int(type))) for type in map_array]
            super(TerrainMap, self).__init__(terrain_array, width, height)

    def get_all_traversable_states(self):
        states = []
        for x in range(self.width):
            for y in range(self.height):
                pnt = Point(x, y)
                ndx = Map.point_to_index(pnt, self.width, self.height)
                terrain = self.map[ndx]
                if terrain.is_traversable():
                    for dir in Directions:
                        state = State(pnt, dir)
                        states.append(state)
        return states
    def get_prof_starting_state(self):
        return self.professor_start_state