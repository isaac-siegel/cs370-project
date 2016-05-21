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

# # score_map = ScoreMap(terrain_map)

prof = Professor(terrain_map)

possible_states = terrain_map.get_all_traversable_states()

while len(possible_states) > 1:
    current_surroundings = prof.get_surroundings()
    for possible_state in possible_states:
        if possible_state != current_surroundings:
            possible_states.remove(possible_state)

    # Now possible states have been trimmed down
    if len(possible_states) <= 1:
        break



    move = generate_random_valid_move(terrain_map, prof)
    prof.move(move)

    for possible_state in possible_states:
        possible_state.move(move)

print("FOUND_PROF")