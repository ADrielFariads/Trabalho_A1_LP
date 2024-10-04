"""
Functions for graphs and visual features
"""

import pandas as pd
import numpy as np
import doctest
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import seaborn as sns



import data_creator

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



heat_map_generator(matriz)
plt.show()

