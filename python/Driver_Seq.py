import random

from TerrainMap import TerrainMap
from Moves import Moves
from Professor import Professor

def generate_move():
    moves = [Moves.LEFT, Moves.RIGHT, Moves.FOWARD, Moves.BACKWARDS]
    choice = int(random.uniform(0,4))
    return moves[choice]

def generate_random_valid_move(terrain_map, prof):
    move = generate_move()
    while not terrain_map.is_valid_move(prof.state, move):
        move = generate_move()
    return move


terrain_map = TerrainMap("test.map")
# print(terrain_map)

# # score_map = ScoreMap(terrain_map)

prof = Professor(terrain_map)
print(prof)

possible_states = terrain_map.get_all_traversable_states()
print("Starting Amount of possible_states: ",len(possible_states))

while len(possible_states) > 1:
    current_surroundings = prof.get_surroundings()
    for possible_state in possible_states:
        neighbors = terrain_map.get_neighbors(possible_state.point)
        possible_state_surroundings = prof.convert_neighbors_to_surroundings(neighbors, possible_state.direction)
        if possible_state_surroundings != current_surroundings:
            possible_states.remove(possible_state)

    # Now possible states have been trimmed down
    if len(possible_states) <= 1:
        break

    move = generate_random_valid_move(terrain_map, prof)
    prof.move(move)

    for possible_state in possible_states:
        possible_state.move(move)

print(prof)

print("FOUND_PROF")