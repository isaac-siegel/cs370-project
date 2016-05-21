class Surroundings:
    def __init__(self, front, left, back, right):
        # type: (TerrainTile, TerrainTile, TerrainTile, TerrainTile) -> self
        self.front = front
        self.left = left
        self.back = back
        self.right = right

    def __eq__(self, other):
        # type: (Surroundings) -> Boolean
        return self.front == other.front and self.left == other.left and self.back == other.back and self.right == other.right

    def __str__(self):
        # type: () -> String
        return "Front: " + str(self.front) + "\n" + \
               "Left: " + str(self.left) + "\n" + \
               "Back: " + str(self.back) + "\n" + \
               "Right: " + str(self.right)

    def __ne__(self, other):
        return not self.__eq__(other)
