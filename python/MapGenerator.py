from random import randint
from TerrainTile import TerrainTile
from Point import Point
from Directions import Directions
from State import State
import os
import sys



def random_from_list(list):
    # type: (list) -> object
    return list[randint(0, len(list) - 1)]


def get_tile_list():  # TODO make reference TerrainTile list
    # type: () -> Terrain[]
    return [i.value for i in TerrainTile.TerrainTypes]


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
    x = randint(0,width - 1)
    y = randint(0,height - 1)
    while not TerrainTile(TerrainTile.TerrainTypes(map[y * height + x])).is_traversable():
        x = randint(0, width - 1)
        y = randint(0, height - 1)
    random_direction = Directions(randint(1, len(Directions)))
    return State(Point(x,y), random_direction)

if __name__ == "__main__":
    # Generates new map file
    # No arguments given: generates 'test.map' with 100 x 100 array
    # 2 arguements given: generates 'test.map with argv[1] x argv[2] array
    # 3 arguements given: generates argv[3].map with argv[1] x argv[2] array

    if len(sys.argv) < 3:
        print("Usage: python MapGenerator.py [width height [name]]")
        width = 100
        height = 100
        file_name = "test"
    else:
        height = int(sys.argv[1])
        width = int(sys.argv[2])
        if len(sys.argv) > 3:
            file_name = sys.argv[3]
        else:
            file_name = "test"
    map = random_map(width, height)
    professor_state = get_random_professor_state(map, width, height)
    write_array_to_file(map, width, height, professor_state,file_name)
