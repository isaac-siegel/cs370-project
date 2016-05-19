from TerrainMap import TerrainMap

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

    move = generate_move()
    prof.move(move)

    for possible_state in possible_states:
        possible_state.move(move)

print("FOUND_PROF")








