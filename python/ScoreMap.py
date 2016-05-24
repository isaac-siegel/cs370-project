from Map import Map
from Point import Point
from TerrainMap import TerrainMap
from ScoreTile import ScoreTile
from TerrainTile import TerrainTile
from Directions import Directions

NON_TRAVERSABLE_SCORE = -1
INITIAL_SCORE = 1


class ScoreMap(Map):

    def create_score_array(self, terrain_map, height, width):
        score_array = [None] * (height * width)
        # Set scores of non traversable tiles to NON_TRAVERSABLE_SCORE
        for x in range(width):
            for y in range(height):
                p = Point(x, y)
                ndx = Map.point_to_index(p, width, height)
                t_tile = terrain_map.map[ndx]
                if not t_tile.is_traversable():
                    score_array[ndx] = ScoreTile(NON_TRAVERSABLE_SCORE, [])
        return score_array

    def needs_scoring(self, score_array, ndx):
        return score_array[ndx] is None

    def score_point(self, score_array, point, score, height, width):
        result_score = ScoreTile(score, [])
        ndx = Map.point_to_index(point, width, height)
        neighbors = Map.get_neighbors_static(point, width, height)
        #TODO Test THIS directions and score from surrounding tiles
        # for neighbor_point in neighbors:
        #     neighbor_ndx = map.point_to_index(neighbor_point, width, height)
        #     neighbor_tile = score_array[neighbor_ndx]
        #     if neighbor_tile
        # for neighbor in neighbors:
        # print(neighbor)
        # print(neighbors[neighbor])
        for direction in Directions:
            neighbor_point = neighbors[direction]
            if neighbor_point is not None:
                neighbor_ndx = Map.point_to_index(neighbor_point, width, height)
                neighbor_tile = score_array[neighbor_ndx]
                if neighbor_tile is not None:
                    if neighbor_tile.score < score and neighbor_tile.score != -1:
                        result_score.directions.append(direction)
        return result_score


    def __init__(self, terrain_map):
        height = terrain_map.height
        width = terrain_map.width
        score_array = self.create_score_array(terrain_map, height, width)

        to_score = set()  # stores the next tiles to update score in a set
        curr_score = INITIAL_SCORE

        # Set bottom row of scores to (1, [SOUTH]) or (NON_TRAVERSIBLE_SCORE, [])
        for i in range(width):
            p = Point(i, height - 1)
            ndx = Map.point_to_index(p, width, height)
            if self.needs_scoring(score_array, ndx):
                score_array[ndx] = ScoreTile(INITIAL_SCORE, [Directions.SOUTH])
                neighbors = Map.get_neighbors_static(p, width, height)
                for neighbor_key in neighbors:
                    neighbor_point = neighbors[neighbor_key]
                    if neighbor_point is not None:
                        neighbor_ndx = Map.point_to_index(neighbor_point, width, height)
                        if self.needs_scoring(score_array, neighbor_ndx):
                            to_score.add(neighbor_point)

        #TODO check that this works
        # Start scoring all other tiles
        while len(to_score) > 0:
            curr_score += 1
            currently_scoring = to_score
            to_score = set()
            for point in currently_scoring:
                ndx = Map.point_to_index(point, width, height)
                if self.needs_scoring(score_array, ndx):
                    score = self.score_point(score_array, point, curr_score, height, width)
                    score_array[ndx] = score
                    neighbors = Map.get_neighbors_static(point, width, height)
                    for neighbor_key in neighbors:
                        neighbor_point = neighbors[neighbor_key]
                        if neighbor_point is not None:
                            neighbor_ndx = Map.point_to_index(neighbor_point, width, height)
                            if self.needs_scoring(score_array, neighbor_ndx):
                                to_score.add(neighbor_point)

        #TODO check if there are any islands left of unscored tiles and init to score -1

        super(ScoreMap, self).__init__(score_array, width, height)

    def __str__(self):
        result = ''
        for j in range(self.height):
            for i in range(self.width):
                point = Point(i, j)
                tile = self.get_tile(point)
                if tile is not None:
                    if tile.score == -1:
                        result += '{   BLOCKED   }'
                    else:
                        result += '(SCORE=' + str(tile.score) + ', '
                        if Directions.NORTH in tile.directions:
                            result += '^'
                        else:
                            result += ' '
                        if Directions.EAST in tile.directions:
                            result += '>'
                        else:
                            result += ' '
                        if Directions.SOUTH in tile.directions:
                            result += 'v'
                        else:
                            result += ' '
                        if Directions.WEST in tile.directions:
                            result += '<'
                        else:
                            result += ' '
                        result += ')'
                else:
                    result += '{NEEDS SCORING}'
            result += '\n'
        return result
