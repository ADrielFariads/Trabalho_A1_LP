import pandas as pd
import Constants
import numpy as np

df = pd.read_csv(Constants.Constants.path)

def read_data_set():
    df = pd.read_csv(Constants.Constants.path)
    return df

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
        print(df)
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




 