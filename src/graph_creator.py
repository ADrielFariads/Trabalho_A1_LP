"""
Functions for graphs and visual features
"""

import pandas as pd
import numpy as np
import doctest
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import seaborn as sns


import Constants
import data_cleaner
import data_creator


df = pd.read_csv(Constants.Constants.path)

matriz = np.array([[1, 0, 0, 0, 2, 4, 3, 2],
       [1, 2, 1, 2, 0, 1, 0, 1],
       [0, 1, 1, 0, 1, 3, 2, 0],
       [1, 0, 0, 1, 1, 0, 1, 2],
       [0, 1, 0, 2, 1, 0, 2, 1],
       [1, 0, 2, 1, 3, 1, 2, 5],
       [0, 2, 1, 1, 2, 1, 1, 1],
       [1, 1, 0, 3, 1, 4, 1, 0]])

def heat_map_generator(game_matriz:np.array) -> plt:
    """
    Creates a plt of a heatmap, which represents how much each square is used in the game

    Parameters:
    ----------
    game_matriz: np.array

        an 8x8 array with the number each squares is a destination of a move in the game

    Returns: 
    -------
    plt
        a plt of a heatmap, built in seaborn


    """

    plt.figure(figsize=(8, 6), facecolor="gray")

    cmap = LinearSegmentedColormap.from_list("white_to_red", ["gray", "orange", "red"])

    ax = sns.heatmap(game_matriz, annot=False, cmap=cmap, cbar=True, linewidths=0, alpha=0.7)
    letter_squares = list("abcdefgh")
    number_squares = list("12345678")



    ax.set_xticklabels(letter_squares, fontsize=12)
    ax.set_yticklabels(number_squares, fontsize=12, rotation=0)
    ax.invert_yaxis()
    ax.set_title('Piece\'s moves ', fontsize=16)
    ax.set_xlabel('', fontsize=12)
    ax.set_ylabel('', fontsize=12)

    return plt

def graph_advantagexrating(games:pd.DataFrame) -> plt:
    df = games
    df = data_creator.advantage_column()
    df = data_cleaner.resign_games_filter(df, True)
    df = df[df["rated"] == True] 

    def final_value(list_target):
        return list_target[-1]
    
    df["last_advantage"] = df["advantage"].apply(final_value)
    df["rating_mean"] = (df["white_rating"] + df["black_rating"])/2

    print(len(df))
    

    return df

df = data_cleaner.read_data_set()
df = data_cleaner.add_black_white_level(df)
df = data_cleaner.cut_duplicates(df)
df = data_cleaner.add_black_white_level(df)
df = data_cleaner.cut_short_games(df)
df = data_cleaner.add_game_level(df)

graph_advantagexrating(df)



