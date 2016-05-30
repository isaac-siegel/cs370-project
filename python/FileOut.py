import numpy as np
import seaborn as sns
from pandas import DataFrame

from TerrainTypes import TerrainTypes
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

            color_map = {}

            light_blue = 0
            mid_blue = 10
            light_green = 20
            dark_green = 30
            dark_pink = 40
            red_orange = 50
            light_orange = 65
            legit_purple = 80
            light_purple  = 85
            yellowish = 90
            darker_yellowish = 92
            brown  = 100

            color_map[TerrainTypes.OPEN.value]  = yellowish
            color_map[TerrainTypes.ROADWAY.value]  = darker_yellowish
            color_map[TerrainTypes.CLIFF.value] = red_orange
            color_map[TerrainTypes.TREE.value]  = dark_pink

            map_array = [color_map[i] for i in map_array2]
            for state in possible_states:
                map_array[width * state.point.y + state.point.x] = dark_green
            if professor:
                map_array[professor.state.point.y * width + professor.state.point.x] = legit_purple
        else:
            map_array2 = [score_tile.score if score_tile is not None else -1 for score_tile in full_map.map]
            map_array = [-100 if score_tile == -1 else score_tile for score_tile in map_array2]

        two_D = np.reshape(map_array, (width, height))
        df = DataFrame(two_D)
        sns_plot = sns.heatmap(df, cmap="Paired", vmin=0,vmax=100, cbar=False, annot=False, xticklabels=False, yticklabels=False, square=True)
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
