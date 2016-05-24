from pandas import DataFrame, ExcelWriter
import seaborn as sns
import numpy as np


def to_csv(terrain_map=None, score_map=None):
    full_map = terrain_map or score_map
    map_array = full_map.map
    width = full_map.width or full_map.width
    height = full_map.height or full_map.height
    two_D = np.reshape(map_array, (width, height))
    df = DataFrame(two_D)
    df.to_csv(r'test.csv', sep='\t')


def to_png(terrain_map=None):
    map_array2 = [i.terrain_type.value for i in terrain_map.map]
    map_array = [0 if i == 1 else 20 if i == 2 else 100 if i == 3 else 90 for i in map_array2]
    width = terrain_map.width
    height = terrain_map.height
    two_D = np.reshape(map_array, (width, height))
    df = DataFrame(two_D)
    sns_plot = sns.heatmap(df, cmap="brg", cbar=False, annot=False, xticklabels=False, yticklabels=False)
    fig = sns_plot.get_figure()
    fig.savefig("output.png")


def to_clipboard(terrain_map=None, score_map=None):
    full_map = terrain_map or score_map
    map_array = full_map.map
    width = full_map.width or full_map.width
    height = full_map.height or full_map.height
    two_D = np.reshape(map_array, (width, height))
    df = DataFrame(two_D)
    df.to_clipboard(excel=True)
