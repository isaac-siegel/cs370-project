import numpy as np
import seaborn as sns
from pandas import DataFrame

from TerrainMap import TerrainMap
from ScoreMap import ScoreMap

class FileOut:
    @staticmethod
    def to_csv(terrain_map=None, score_map=None):
        full_map = terrain_map or score_map
        map_array = full_map.map
        width = full_map.width or full_map.width
        height = full_map.height or full_map.height
        two_D = np.reshape(map_array, (width, height))
        df = DataFrame(two_D)
        df.to_csv(r'test.csv', sep='\t')

    @staticmethod
    def to_png(terrain_map=None, score_map=None, possible_states=None, professor=None, file_name="output"):
        full_map = terrain_map or score_map
        width = full_map.width or full_map.width
        height = full_map.height or full_map.height

        if terrain_map:
            map_array2 = [i.terrain_type.value for i in full_map.map]
            map_array = [0 if i == 1 else 20 if i == 2 else 100 if i == 3 else 60 for i in map_array2]
            for state in possible_states:
                map_array[width * state.point.y + state.point.x] = 150
            if professor:
                map_array[professor.state.point.y * width + professor.state.point.x] = 200
        else:
            map_array2 = [score_tile.score if score_tile is not None else -1 for score_tile in full_map.map]
            map_array = [-100 if score_tile == -1 else score_tile for score_tile in map_array2]

        two_D = np.reshape(map_array, (width, height))
        df = DataFrame(two_D)
        sns_plot = sns.heatmap(df, cmap="brg", cbar=False, annot=False, xticklabels=False, yticklabels=False)
        fig = sns_plot.get_figure()
        fig.savefig(file_name + ".png")

    @staticmethod
    def to_clipboard(terrain_map=None, score_map=None):
        full_map = terrain_map or score_map
        map_array = full_map.map
        width = full_map.width or full_map.width
        height = full_map.height or full_map.height
        two_D = np.reshape(map_array, (width, height))
        df = DataFrame(two_D)
        df.to_clipboard(excel=True)


# FileOut.to_png(score_map=ScoreMap(TerrainMap(file_name="test.map")))