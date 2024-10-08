import pandas as pd
import Constants
import numpy as np

df = pd.read_csv(Constants.Constants.path)

def read_data_set():
    '''
    Reads the database and returns the dataframe
    '''
    try:

        df = pd.read_csv(Constants.Constants.path)
        return df
    
    except FileNotFoundError:
        print('File not found, please enter a valid path')
        return None

def cut_short_games(df):
    '''
    Cut the games that have less than three turns

    Parameters:
    --------------
    DataFrame being analyzed

    Returns:
    --------------
    The DataFrame without short games
    
    '''
    try:
        isinstance(df, pd.core.frame.DataFrame)
        
        df = df[df['turns'] >= 3]
        return df
    except TypeError:
        print('the argument is not a DataFrame')
        return None
    except KeyError:
        print('The DataFrame does not have the series (turns)')
        return None

def add_black_white_level(df):
    '''
    Add two columns that separates the rating of the players with black and white pieces
    (one column to each) in low, medium or high by equally divided quantiles

    Parameters:
    -------------
    DataFrame being analyzed

    Returns:
    -------------
    DataFrame with the series level_black_player and level_white_player added
    
    '''
    try:
        isinstance(df, pd.core.frame.DataFrame)

        all_rating_players = pd.concat([df['white_rating'], df['black_rating']], ignore_index=True)
        all_rating_quantiles = quantile(all_rating_players, 3)

        df['level_black_player'] = [
        'low' if rating < all_rating_quantiles[1] else 'medium' if rating < all_rating_quantiles[2] else 'high' 
        for rating in df['black_rating']
        ]
        
        df['level_white_player'] = [
        'low' if rating < all_rating_quantiles[1] else 'medium' if rating < all_rating_quantiles[2] else 'high' 
        for rating in df['white_rating']
        ]
        return df
    except TypeError:
        print('the argument is not a DataFrame')
        return None
    except KeyError:
        print('The DataFrame does not have the series (white_rating) and (black_rating)')
        return None
    except ValueError:
        print('white_rating and black_rating must be of the same length')
        return None

def quantile(data, number_of_divisions : int) -> set:
    '''
    Calculates the quantiles of a data set for the desired number of divisions

    Parameters:
    -------------
    data: numerical data set
    number_of_divisions : int

    Returns:
    -------------
    Dict with key equal the number of the quantile containing the quantiles
    
    '''
    try:
        isinstance(data[0], np.int64 | int | float)
        isinstance(number_of_divisions, int)

        quantis = {}  
        for i in range(0, number_of_divisions):
            quantis[i + 1] = np.percentile(data, (100/number_of_divisions)* (i + 1))
        return quantis
    
    except TypeError:
        print('The arguments are not valid')
    





 