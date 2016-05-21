from State import State
from Directions import Directions
from Surroundings import Surroundings

class Professor:
    def __init__(self, terrain_map):
        self.state = terrain_map.get_prof_starting_state()
        self.terrain_map = terrain_map

    def move(self, movement):
        self.state.move(movement)

    def convert_neighbors_to_surroundings(self, neighbors, direction):
        surroundings = None

        north = self.terrain_map.get_tile(neighbors['NORTH'])
        south = self.terrain_map.get_tile(neighbors['SOUTH'])
        east = self.terrain_map.get_tile(neighbors['EAST'])
        west = self.terrain_map.get_tile(neighbors['WEST'])

        if direction == Directions.NORTH:
            surroundings = Surroundings(north, west, south, east)
        elif direction == Directions.SOUTH:
            surroundings = Surroundings(south, east, north, west)
        elif direction == Directions.EAST:
            surroundings = Surroundings(east, north, west,south)
        elif direction == Directions.WEST:
            surroundings = Surroundings(west,south, east, north)

        return surroundings

    def get_surroundings(self):
        # UNTESTED
        neighbors = self.terrain_map.get_neighbors(self.state.point)
        prof_direction = self.state.direction

        return self.convert_neighbors_to_surroundings(neighbors, prof_direction)


    def __str__(self):
        res = "----Professor----\n"
        res += "State: " + str(self.state)
        return res





