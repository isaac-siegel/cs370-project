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
        if direction == Directions.NORTH:
            surroundings = Surroundings(neighbors['NORTH'], neighbors['WEST'], neighbors['SOUTH'], neighbors['EAST'])
        elif direction == Directions.SOUTH:
            surroundings = Surroundings(neighbors['SOUTH'], neighbors['EAST'], neighbors['NORTH'], neighbors['WEST'])
        elif direction == Directions.EAST:
            surroundings = Surroundings(neighbors['EAST'], neighbors['NORTH'], neighbors['WEST'], neighbors['SOUTH'])
        elif direction == Directions.WEST:
            surroundings = Surroundings(neighbors['WEST'], neighbors['SOUTH'], neighbors['EAST'], neighbors['NORTH'])

        print(surroundings)
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





