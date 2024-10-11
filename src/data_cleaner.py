'''
Module that clean data and create new insights
'''

import pandas as pd
import Constants
import numpy as np


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

def cut_duplicates(df):
    '''
    Cuts lines with exact copies

    Parameters:
    --------------
    DataFrame being analyzed: pd.DataFrame

    Returns:
    --------------
    The DataFrame without duplicates
    
    '''
    try:
        assert isinstance(df, pd.core.frame.DataFrame)
        
        df = df.drop_duplicates(subset=["moves"])
        return df
    except AssertionError:
        print('The argument is not a DataFrame')
        return None

def cut_short_games(df):
    '''
    Cut the games that have less than three turns

    Parameters:
    --------------
    DataFrame being analyzed: pd.DataFrame

    Returns:
    --------------
    The DataFrame without short games
    
    '''
    try:
        assert isinstance(df, pd.core.frame.DataFrame)
        
        df = df[df['turns'] >= 3]
        return df
    except AssertionError:
        print('The argument is not a DataFrame')
        return None
    except KeyError:
        print('The DataFrame does not have the series (turns)')
        return None
    

def quantile(data, number_of_divisions : int) -> dict:
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
        assert isinstance(data[0], np.int64 | int | float)
        assert isinstance(number_of_divisions, int)

        quantis = {}  
        for i in range(0, number_of_divisions-1):
            quantis[i + 1] = np.percentile(data, (100/number_of_divisions)* (i + 1))
        return quantis
    
    except AssertionError:
        print('The arguments are not valid')


def add_black_white_level(df):
    '''
    Add two columns that separates the rating of the players with black and white pieces
    (one column to each) in low, medium or high by equally divided quantiles

    Parameters:
    -------------
    DataFrame being analyzed: pd.DataFrame

    Returns:
    -------------
    DataFrame with the series level_black_player and level_white_player added
    
    '''
    try:
        assert isinstance(df, pd.core.frame.DataFrame)

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
    except AssertionError:
        print('The argument is not a DataFrame')
        return None
    except KeyError:
        print('The DataFrame does not have the series (white_rating) and (black_rating)')
        return None
    except ValueError:
        print('white_rating and black_rating must be of the same length')
        return None
    

def add_game_level(df):
    '''
    Add the column game_level that separates the game level in low, medium and hard
    calculated by averaging rating columns by divided equally quantiles

    Parameters:
    -------------
    DataFrame being analyzed: pd.DataFrame

    Returns:
    -------------
    DataFreme with game_level series added
    
    '''
    try:
        assert isinstance(df, pd.core.frame.DataFrame)

        average_rating = (df['white_rating'] + df['black_rating'])/2
        avg_rating_quantiles = quantile(average_rating, 3)

        df['game_level'] = [
            'low' if game_rating < avg_rating_quantiles[1] else 'medium' if game_rating < avg_rating_quantiles[2]
            else 'high' for game_rating in average_rating
        ]
        return df
    
    except AssertionError:
        print('The argument is not a DataFrame')
        return None
    except KeyError:
        print('The DataFrame does not have the series (white_rating) and (black_rating)')
        return None
    except ValueError:
        print('white_rating and black_rating must be of the same length')
        return None
    

def add_game_duration(df):
    '''
    This function classifies the duration of the game into: low, medium and high
    calculated by turns using quantiles divided equally
    
    Parameters:
    -------------
    DataFrame being analyzed: pd.DataFrame

    Returns:
    ----------
    DataFrame with game_duration_in_turns series added

    '''
    try:
        assert isinstance(df, pd.core.frame.DataFrame)

        turns = df['turns']
        quantiles = quantile(turns, 3)

        df['game_duration_in_turns'] = [
            'low' if turn < quantiles[1] else 'medium' if turn < quantiles[2]
            else 'high' for turn in turns
        ]
        return df
    
    except AssertionError:
        print('The argument is not a DataFrame')
        return None
    except KeyError:
        print('The DataFrame does not have the turns series')
        return None
    

def resign_games_filter(df, resign=True):
    '''
    This function filters the DataFrame to show only resigned (or non resigned) games
    
    Parameters:
    -------------
    DataFrame: pd.DataFrame

    resign=True: Bool

    Returns:
    ----------
    DataFrame with only resigned or non resigned games 

    '''
    try:
        assert isinstance(df, pd.core.frame.DataFrame)
        assert isinstance(resign, bool)

        if resign == True:
            df = df[df["victory_status"]=="resign"]
            return df
        else:
            df = df[df["victory_status"]!="resign"]
            return df
    except AssertionError:
        print('The arguments are invalid')
    except Exception:
        print("an error occurred while filtering your dataframe")
        return None
    
def mate_games_filter(df):
    '''
    This function filters the DataFrame to show mate-only win games
    
    Parameters:
    -------------
    DataFrame: pd.DataFrame

    Returns:
    ----------
    Dataframe with mate-only win
    '''

    try:

        assert isinstance(df, pd.core.frame.DataFrame)
        df = df[df['victory_status'] == 'mate']

    except AssertionError:
        print('The argument is not a DataFrame')
        return None
    except KeyError:
        print('The DataFrame does not have the victory_status series')
        return None
    
    
def desv_pad_evaluate(games):
    desv_medium_reviews = []
    desv_high_reviews = []
    desv_low_reviews = []
    for game in games:
        if game["level"] == "medium":
            desv_medium_reviews.append(np.std(game["avaliacoes"]))
        elif game["level"] == "high":
            desv_high_reviews.append(np.std(game["avaliacoes"]))
        else:
            desv_low_reviews.append(np.std(game["avaliacoes"]))
    desvs = {
        "Low": sum(desv_low_reviews)/len(desv_low_reviews),
        "Medium" : sum(desv_medium_reviews)/len(desv_medium_reviews),
        "High": sum(desv_high_reviews)/len(desv_high_reviews)
        }
    view_boxplot({"Low": desv_low_reviews, "Medium": desv_medium_reviews, "High": desv_high_reviews})    

