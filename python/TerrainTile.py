from enum import Enum
from Tile import Tile
from TerrainTypes import TerrainTypes

class TerrainTile(Tile):

    def __init__(self, terrain_type):
        Tile.__init__(self)
        self.terrain_type = terrain_type

    def is_traversable(self):
        return self.terrain_type == TerrainTypes.OPEN or self.terrain_type == TerrainTypes.ROADWAY

    def __eq__(self, other):
        if other is None:
            return False
        return self.terrain_type == other.terrain_type

    def __str__(self):
        return "("+str(self.terrain_type)+")"



# tree_tile_1 = TerrainTile(TerrainTypes.TREE)
# tree_tile_2 = TerrainTile(TerrainTypes.TREE)
#
# cliff_tile = TerrainTile(TerrainTypes.CLIFF)
# roadway_tile = TerrainTile(TerrainTypes.ROADWAY)
#
# print(tree_tile_1.__eq__(tree_tile_2))
# print(tree_tile_1.__eq__(cliff_tile))
#
# print(tree_tile_2.is_traversable())
# print(roadway_tile.is_traversable())




