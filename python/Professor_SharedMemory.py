from State import State
from Directions import Directions
from Surroundings import Surroundings
from Point import Point
from Map import Map
from multiprocessing import Process, Array


class Professor_SharedMemory:
    def __init__(self, terrain_map):
        self.state = terrain_map.get_prof_starting_state()
        self.terrain_map = terrain_map

    def move(self, movement):
        self.state.move(movement)

    def convert_neighbors_to_surroundings(self, neighbors, direction):
        surroundings = None

        north = self.terrain_map.get_tile(neighbors[Directions.NORTH])
        south = self.terrain_map.get_tile(neighbors[Directions.SOUTH])
        east = self.terrain_map.get_tile(neighbors[Directions.EAST])
        west = self.terrain_map.get_tile(neighbors[Directions.WEST])

        if direction == Directions.NORTH:
            surroundings = Surroundings(north, west, south, east)
        elif direction == Directions.SOUTH:
            surroundings = Surroundings(south, east, north, west)
        elif direction == Directions.EAST:
            surroundings = Surroundings(east, north, west, south)
        elif direction == Directions.WEST:
            surroundings = Surroundings(west, south, east, north)

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

    def is_possible_state(self, state, professor_surroundings):
        neighbors = self.terrain_map.get_neighbors(state.point)
        possible_state_surroundings = self.convert_neighbors_to_surroundings(neighbors, state.direction)
        return possible_state_surroundings == professor_surroundings

    # def get_all_possible_states(self):
    #     states = []
    #     professor_surroundings = self.get_surroundings()
    #     for x in range(self.terrain_map.width):
    #         for y in range(self.terrain_map.height):
    #             point = Point(x, y)
    #             terrain = self.terrain_map.get_tile(point)
    #             if terrain.is_traversable():
    #                 for dir in Directions:
    #                     state = State(point, dir)
    #                     if self.is_possible_state(state, professor_surroundings):
    #                         states.append(state)
    #     return states

    def get_all_possible_states(self, num_proc):
        size = self.terrain_map.width * self.terrain_map.height
        professor_surroundings = self.get_surroundings()
        x = Array('i', size)
        y = Array('i', size)
        direction = Array('i', size)
        proc = [Process] * num_proc
        for i in range(num_proc):
            proc[i] = Process(target=self.fill_states,
                              args=(
                              int(i * self.terrain_map.height / num_proc), int(self.terrain_map.height / num_proc),
                              int(size * i / num_proc), x, y, direction, professor_surroundings))
            proc[i].start()
        for i in range(num_proc):
            proc[i].join()
        states = []
        i = 0
        while i < size:
            if direction[i] is not 0:
                point = Point(x[i],y[i])
                dir = Directions(direction[i])
                state = State(point,dir)
                states.append(state)
                i += 1
            else:
                index = int(i / int(size / num_proc))
                i = (index + 1) * int(size / num_proc)

        return states

    def fill_states(self, y_index, length, state_index, x_array, y_array, direction_array, professor_surroundings):
        for y in range(y_index, y_index + length):
            for x in range(0, self.terrain_map.width):
                point = Point(x, y)
                terrain = self.terrain_map.get_tile(point)
                if terrain.is_traversable():
                    for dir in Directions:
                        state = State(point, dir)
                        if self.is_possible_state(state, professor_surroundings):
                            x_array[state_index] = x
                            y_array[state_index] = y
                            direction_array[state_index] = dir.value
                            state_index += 1

    def is_valid_move(self, movement):
        move_state = State.copy(self.state)
        move_state.move(movement)
        return self.terrain_map.is_valid_state(move_state) and self.terrain_map.get_tile(
            self.state.point).is_traversable()
