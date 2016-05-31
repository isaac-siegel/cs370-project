import random

from TerrainMap import TerrainMap
from Moves import Moves
from Professor import Professor
from Directions import Directions
from Point import Point
from State import State
from time import time, sleep
from FileOut import FileOut
from ScoreMap import ScoreMap
from random import randint

FILE_OUT = False
PRINT_ADVANCED_TIMING = False
PRINT_ADVANCED_STATEMENTS = False
PRINT_LOOP_STATEMENTS = False


def generate_move():
    choice = int(random.uniform(1, 5))
    return Moves(choice)


def generate_random_valid_move(prof):
    rand_move = generate_move()
    while not prof.is_valid_move(rand_move):
        rand_move = generate_move()
    return rand_move


def get_smart_move(score_map, possible_states):
    # UNTESTED
    move_counts = {}
    move_counts[Moves.FORWARD]  = 0
    move_counts[Moves.BACKWARD] = 0
    move_counts[Moves.LEFT]     = 0
    move_counts[Moves.RIGHT]    = 0

    for possible_state in possible_states:
        if score_map.get_tile(possible_state.point) is None: continue
        desired_directions = score_map.get_tile(possible_state.point).directions
        for desired_direction in desired_directions:
            desired_move = State.direction_to_move(possible_state.direction, desired_direction)
            move_counts[desired_move] += 1

    max_count = -1
    max_moves_ties = []
    for move in Moves:
        move_count = move_counts[move]
        if move_count > max_count:
            max_count = move_count
            max_moves_ties = [move]
        elif move_count == max_count:
            # tie between max_move and move
            if PRINT_ADVANCED_STATEMENTS:
                print("********TIE********")
            max_moves_ties.append(move)
            pass

    return max_moves_ties[randint(0, len(max_moves_ties) - 1)]


def primary_driver_logic(map_file_name):
    t1 = time()
    t0 = time()
    print("Creating Terrain Map")
    terrain_map = TerrainMap(map_file_name)
    # print(terrain_map)
    if PRINT_ADVANCED_TIMING:
        print('time take: {} seconds'.format(time() - t1))
        t1 = time()
    print("Creating Score Map")
    score_map = ScoreMap(terrain_map)
    if PRINT_ADVANCED_TIMING:
        print('time take: {} seconds'.format(time() - t1))
        t1 = time()
    print("Creating Prof")
    prof = Professor(terrain_map)
    if PRINT_ADVANCED_TIMING:
        print('time take: {} seconds'.format(time() - t1))
        t1 = time()
    if PRINT_ADVANCED_STATEMENTS:
        print("====STARTING PLACE====")
        print(prof)

    # possible_states = terrain_map.get_all_traversable_states()
    print("Generating Initial possible_states")
    possible_states = prof.get_all_possible_states()
    if PRINT_ADVANCED_TIMING:
        print('time take: {} seconds'.format(time() - t1))
        t1 = time()
    if PRINT_ADVANCED_STATEMENTS:
        print("Starting Amount of possible_states: ", len(possible_states))

    i = 0
    print_once = False

    print("===Starting Primary Loop===")
    while prof.state.point.y < terrain_map.height - 1:
        current_surroundings = prof.get_surroundings()
        next_possible_states = []
        if PRINT_ADVANCED_TIMING:
            t1 = time()
        if PRINT_LOOP_STATEMENTS:
            print("Narrowing States")
        for possible_state in possible_states:
            if prof.is_possible_state(possible_state, current_surroundings):
                next_possible_states.append(possible_state)

        if PRINT_ADVANCED_TIMING:
            print('time take: {} seconds'.format(time() - t1))
        possible_states = next_possible_states
        if len(possible_states) > 1:
            if FILE_OUT:
                FileOut.to_png(terrain_map=terrain_map, possible_states=possible_states, professor=prof,
                               file_name="steps/step" + str(i))
            i += 1

        if PRINT_ADVANCED_STATEMENTS:
            print("Num possible states: ", len(possible_states))
        # Now possible states have been trimmed down
        if len(possible_states) <= 1 and not print_once:
            print("+++++FOUND PROFESSOR+++++\nNow routing him home")
            if PRINT_ADVANCED_STATEMENTS:
                print('Current Score:', score_map.get_tile(prof.state.point).score)
            print_once = True

        if PRINT_ADVANCED_STATEMENTS:
            print(prof)
            print("isTraversible() ", terrain_map.get_tile(prof.state.point).is_traversable())

        if PRINT_LOOP_STATEMENTS:
            print("Getting Smart Move")
        if PRINT_ADVANCED_TIMING:
            t1 = time()
        move = get_smart_move(score_map, possible_states)
        if PRINT_ADVANCED_TIMING:
            print('time take: {} seconds'.format(time() - t1))
            t1 = time()
        if PRINT_LOOP_STATEMENTS:
            print("Got Smart Move")

        # move = generate_random_valid_move(prof)
        if PRINT_ADVANCED_STATEMENTS:
            print(move)
        prof.move(move)

        if PRINT_LOOP_STATEMENTS:
            print("Moving All possible_states")
        for possible_state in possible_states:
            possible_state.move(move)

        if FILE_OUT:
            FileOut.to_png(terrain_map=terrain_map, possible_states=possible_states, professor=prof,
                           file_name="steps/step" + str(i))

        i += 1
        if FILE_OUT and i > terrain_map.height * 1.25:
            print("NOT DONE YET BUT SAVING ISAAC'S SSD")
            break

    print("\n====RESTING PLACE===")
    print(prof)

    print("Professor has been routed successfully!")
    t2 = time()
    print('total time take: {} seconds'.format(t2 - t0))
    return t2 - t0


# primary_driver_logic()
