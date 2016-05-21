import random

from TerrainMap import TerrainMap
from Moves import Moves
from Professor import Professor
from Directions import Directions
from Point import Point
from State import State
from time import time, sleep


def generate_move():
    choice = int(random.uniform(1,5))
    return Moves(choice)

def generate_random_valid_move(terrain_map, prof):
    move = generate_move()
    while not terrain_map.is_valid_move(prof.state, move):
        move = generate_move()
    return move

t1 = time()

terrain_map = TerrainMap("test.map")
# print(terrain_map)

# # score_map = ScoreMap(terrain_map)

prof = Professor(terrain_map)
print("====STARTING PLACE====")
print(prof)

possible_states = terrain_map.get_all_traversable_states()

print("Starting Amount of possible_states: ",len(possible_states))


while len(possible_states) > 1:
    current_surroundings = prof.get_surroundings()
    next_possible_states = []
    # print("current surroundings",current_surroundings)
    # print()
    for possible_state in possible_states:
        test_state = State(Point(0,0), Directions.EAST)

        neighbors = terrain_map.get_neighbors(possible_state.point)
        possible_state_surroundings = prof.convert_neighbors_to_surroundings(neighbors, possible_state.direction)

        if possible_state_surroundings == current_surroundings:
            # print("found matching state: ")
            # print(possible_state)
            next_possible_states.append(possible_state)

    possible_states = next_possible_states

    print("Num possible states: ",len(possible_states))
    # Now possible states have been trimmed down
    if len(possible_states) <= 1:
        break

    move = generate_random_valid_move(terrain_map, prof)
    print(prof)
    print(move)
    prof.move(move)

    for possible_state in possible_states:
        possible_state.move(move)

print("\n\n====RESTING PLACE===")
print(prof)

print("FOUND_PROF")
t2 = time()
print('time take: {} seconds'.format(t2 - t1))