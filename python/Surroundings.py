class Surroundings:
    def __init__(self, front, left, back, right):
        # type: (TerrainTile, TerrainTile, TerrainTile, TerrainTile) -> self
        self.front = front
        self.left = left
        self.back = back
        self.right = right

    def __eq__(self, other):
        # type: (Surroundings) -> Boolean
        equal_0_degrees = other.front == self.front and other.left == self.left
        equal_0_degrees = equal_0_degrees and other.back == self.back and other.right == self.right
        if equal_0_degrees:
            return True

        equal_90_degrees = other.right == self.front and other.front == self.left
        equal_90_degrees = equal_90_degrees and other.left == self.back and other.back == self.right
        if equal_90_degrees:
            return True

        equal_180_degrees = other.back == self.front and other.right == self.left
        equal_180_degrees = equal_180_degrees and other.front == self.back and other.left == self.right
        if equal_180_degrees:
            return True

        equal_270_degrees = other.left == self.front and other.back == self.left
        equal_270_degrees = equal_270_degrees and other.right == self.back and other.front == self.right
        if equal_270_degrees:
            return True

        return False

    def __str__(self):
        # type: () -> String
        return "Front: " + str(self.front) + "\n" + \
               "Left: " + str(self.left) + "\n" + \
               "Back: " + str(self.back) + "\n" + \
               "Right: " + str(self.right)
