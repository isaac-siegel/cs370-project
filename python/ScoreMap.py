from python.Map import Map
from python.Point import Point
from python.TerrainMap import TerrainMap
from python.ScoreTile import ScoreTile
from python.TerrainTile import TerrainTile
from python.Directions import Directions

NON_TRAVERSABLE_SCORE = -1
INITIAL_SCORE = 1


class ScoreMap(Map):

    def create_score_array(self, terrain_map, height, width):
        score_array = [None] * (height * width)
        # Set scores of non traversable tiles to NON_TRAVERSABLE_SCORE
        for x in width:
            for y in height:
                p = Point(x, y)
                ndx = Map.point_to_index(p, width, height)
                t_tile = terrain_map.map[ndx]
                if not t_tile.is_traversable():
                    score_array[ndx] = ScoreTile(NON_TRAVERSABLE_SCORE, [])
        return score_array

    def needs_scoring(self, score_array, ndx):
        return score_array[ndx] is None

    def score_point(self, score_array, point, height, width):
        ndx = Map.point_to_index(point, width, height)
        neighbors = Map.get_neighbors(point)
        #TODO get directions and score from surrounding tiles
        return ScoreTile(-1, []) # dummy data being returned temporary


    def __init__(self, terrain_map):
        height = terrain_map.height
        width = terrain_map.width
        score_array = ScoreMap.create_score_array(terrain_map, height, width)

        to_score = set()  # stores the next tiles to update score in a set

        # Set bottom row of scores to (1, [SOUTH]) or (NON_TRAVERSABLE_SCORE, [])
        for i in range(width):
            p = Point(i, height - 1)
            ndx = Map.point_to_index(p, width, height)
            if ScoreMap.needs_scoring(score_array, ndx):
                score_array[ndx] = ScoreTile(INITIAL_SCORE, [Directions.SOUTH])
                neighbors = Map.get_neighbors(p)
                for neighbor_point in neighbors:
                    if neighbor_point is not None:
                        neighbor_ndx = Map.point_to_index(neighbor_point, width, height)
                        if ScoreMap.needs_scoring(score_array, neighbor_ndx):
                            to_score.add(neighbor_point)

        #TODO check that this works
        # Start scoring all other tiles
        while len(to_score) > 0:
            currently_scoring = to_score
            to_score = set()
            for point in currently_scoring:
                ndx = Map.point_to_index(point, width, height)
                if ScoreMap.needs_scoring(score_array, ndx):
                    score = ScoreMap.score_point(score_array, point, height, width)
                    score_array[ndx] = score
                    neighbors = Map.get_neighbors(p)
                    for neighbor_point in neighbors:
                        if neighbor_point is not None:
                            neighbor_ndx = Map.point_to_index(neighbor_point, width, height)
                            if ScoreMap.needs_scoring(score_array, neighbor_ndx):
                                to_score.add(neighbor_point)

        #TODO check if there are any islands left of unscored tiles

        super(ScoreMap, self).__init__(score_array, width, height)


