from random import randint
from TerrainTile import TerrainTile
from Point import Point
from Directions import Directions
from State import State
from TerrainMap import TerrainMap
from ScoreMap import ScoreMap
from TerrainTypes import TerrainTypes
import os
import sys

SIZE = 100
WIDTH = SIZE
HEIGHT = SIZE


def random_from_list(list):
    # type: (list) -> object
    return list[randint(0, len(list) - 1)]


def get_tile_list():  # TODO make reference TerrainTile list
    # type: () -> Terrain[]
    array = [i.value for i in TerrainTypes]
    array.append(TerrainTypes.OPEN.value)
    array.append(TerrainTypes.OPEN.value)
    return array


def write_array_to_file(array, width, height, professor_state, file_name):
    # type: (int[], int, int, string) ->
    try:
        os.remove(file_name)
    except OSError:
        pass
    target = open(file_name + ".map", 'w+')
    target.write(str(professor_state.point.x) + "\n")
    target.write(str(professor_state.point.y) + "\n")
    target.write(str() + str(professor_state.direction.value) + "\n")
    for y in range(height):
        line = ""
        for x in range(width):
            line += str(array[y * width + x])
        target.write(line + "\n")
    target.close()


def random_map(width, height):
    # type: (int, int) -> int[][]
    tile_list = get_tile_list()
    map = [tile_list[randint(0, len(tile_list) - 1)] for i in range(width * height)]
    return map


def get_random_professor_state(map, width, height):
    x = randint(0, width - 1)
    y = randint(0, height - 1)
    while not TerrainTile(TerrainTypes(map[y * height + x])).is_traversable():
        x = randint(0, width - 1)
        y = randint(0, height - 1)
    random_direction = Directions(randint(1, len(Directions)))
    return State(Point(x, y), random_direction)


def get_professor_state(map, width, height):
    for i in range(width):
        map[height * (height - 1) + i] = "#"
        # TerrainTypes.ROADWAY.value
    professor_point_index = width * (height - 1) + randint(0, width)
    move_count = int(height * .75)
    while move_count > 0:
        move_count -= 1
        professor_point_index += get_random_move(professor_point_index, width, height)
        map[professor_point_index] = "#"
    professor_point = Point(professor_point_index % width, professor_point_index / width)
    random_direction = Directions(randint(1, len(Directions)))
    return State(professor_point, random_direction)


def get_random_move(professor_point, width, height):
    moves = [-width, width, 1, -1]
    good_point = False
    # 10PM ENGAGE FULL STUPID MODE
    while not good_point:
        move_index = randint(0, len(moves) + 1)
        if move_index > len(moves):
            move_index = 0
        move = professor_point + moves[move_index % len(moves)]
        if (height - 1) * (width) > move > 0:
            # print("hi")
            good_point = True
    return moves[move_index % len(moves)]


def array_to_terrain_map(array, width, height, professor_state):
    return TerrainMap(None, array, height, width, professor_state)

# def terrain_map_to_score_map():

if __name__ == "__main__":
    # Generates new map file
    # No arguments given: generates 'test.map' with 100 x 100 array
    # 2 arguements given: generates 'test.map with argv[1] x argv[2] array
    # 3 arguements given: generates argv[3].map with argv[1] x argv[2] array

    if len(sys.argv) < 3:
        print("Usage: python MapGenerator.py [width height [name]]")
        file_name = "test"
    else:
        HEIGHT = int(sys.argv[1])
        WIDTH = int(sys.argv[2])
        if len(sys.argv) > 3:
            file_name = sys.argv[3]
        else:
            file_name = "test"
    score = -1
    while score == -1 or score == None:
        print("Map Generated Without Professor Route")
        map = random_map(WIDTH, HEIGHT)
        professor_state = get_random_professor_state(map, WIDTH, HEIGHT)
        terrain_map = array_to_terrain_map(map,WIDTH,HEIGHT,professor_state)
        score_map = ScoreMap(terrain_map)
        score = score_map.get_tile(professor_state.point)
    print(score_map)
    print(professor_state)
    print(score)
    write_array_to_file(map,WIDTH,HEIGHT,professor_state, file_name)
    # write_array_to_file(map, WIDTH, HEIGHT, professor_state,file_name)
