"""
Functions for graphs and visual features
"""

import pandas as pd
import numpy as np
import doctest
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import seaborn as sns
import data_cleaner

import Constants
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

def view_boxplot(df):
    sns.boxplot(data=df)
    plt.title('Plays evaluate')
    plt.ylabel('Values')
    plt.xlabel('Level')
    plt.xticks(ticks=[0, 1, 2], labels=['Low', 'Medium', 'High'])
    plt.show()

def stacked_column_graph(df):
    '''
    Create a stacked column chart that analyzes each player's probability of winning (black or white) 
    related to the duration of the game in turns (low, medium and high)
    with the count of occurrences in each block

    Parameters:
    -------------
    DataFrame being analyzed: pd.DataFrame

    Returns:
    ----------
    Create the stacked column graph

    '''
    try:
        assert isinstance(df, pd.core.frame.DataFrame)

        #organizing the categories in order
        df['game_duration_in_turns'] = pd.Categorical(
            df['game_duration_in_turns'], categories=['low', 'medium', 'high'], ordered= True)
                                                       
        count = df.groupby(['game_duration_in_turns', 'winner'], observed = True).size().unstack(fill_value=0)

        #Calculate percentage
        percentage = count.div(count.sum(axis=1), axis=0) * 100

        ax = percentage.plot(kind='bar', stacked=True)

        #Add count labels
        for i in range(len(percentage)):
            for j in range(len(percentage.columns)):
                current_count = count.iloc[i, j]
                #Centers the labels in the middle of the bar
                height = percentage.iloc[i, :j + 1].sum() - (percentage.iloc[i, j] / 2)
                ax.text(i, height, str(current_count), ha='center', va='center', color='white')

        #Graph settings
        plt.title('Win percentage by turn-based game duration',fontweight='bold')
        plt.ylabel('Percentage (%)', fontweight='bold')
        plt.xlabel('Game duration', fontweight='bold')
        plt.xticks(rotation=0)
        plt.legend(title='Winner' , loc = 'upper right',fontsize='small', borderpad=0.1)
        plt.ylim(0, 100)  
        plt.show()

    except AssertionError:
        print('The argument is not a DataFrame')
        return None
    except KeyError:
        print('The DataFrame does not have the game_duration_in_turns and/or winner series')
        return None


