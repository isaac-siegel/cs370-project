from random import randint
import os
import sys


def random_from_list(list):
    # type: (list) -> object
    return list[randint(0, len(list) - 1)]


def get_tile_list():  # TODO make reference TerrainTile list
    # type: () -> Terrain[]
    return [i for i in range(1, 5)]


def write_array_to_file(array, width, height, file_name):
    # type: (int[], int, int, string) ->
    try:
        os.remove(file_name)
    except OSError:
        pass
    target = open(file_name + ".map", 'w+')
    for y in range(height):
        line = ""
        for x in range(width):
            line += str(array[y * width + x])
        target.write(line + "\n")
    target.close()


def random_map(width, height):
    # type: (int, int) -> int[][]
    tile_list = get_tile_list()
    return [tile_list[randint(0, len(tile_list) - 1)] for i in range(width * height)]


if __name__ == "__main__":
    # Generates new map file
    # No arguments given: generates 'test.map' with 100 x 100 array
    # 2 arguements given: generates 'test.map with argv[1] x argv[2] array
    # 3 arguements given: generates argv[3].map with argv[1] x argv[2] array

    if len(sys.argv) < 3:
        print "Usage: python MapGenerator.py [width height [name]]"
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
    write_array_to_file(map, width, height, file_name)
