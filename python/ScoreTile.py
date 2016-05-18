from Tile import Tile

class ScoreTile(Tile):
    def __init__(self, score, directions):
        Tile.__init__(self)
        self.score = score
        self.directions = directions

    def __str__(self):
        res = "-----ScoreTile----\n"
        res += "Score: "  + str(self.score) + "\n"
        res += "Directions: "
        for direction in self.directions:
            res += str(direction)
        return res