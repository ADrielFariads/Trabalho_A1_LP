import pandas as pd
import Constants
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.interpolate import make_interp_spline

df = pd.read_csv(Constants.Constants.path)

def read_data_set() -> pd.DataFrame:
    """
    Read csv file

    Returns: 
    -------
    pd.DataFrame

        a pandas.DataFrame

    """
    df = pd.read_csv(Constants.Constants.path)
    return df

#elimina jogos com 3 ou menos turnos
def cut_short_games(df):
    """
    Eliminates games with 3 turns or less

    Parameters:
    ----------
    df: pd.Dataframe

        a DataFrame with the games

    Returns: 
    -------
    pd.Dataframe

        a pandas.DataFrame
        
    """
    
    df = df[df['turns'] >= 3]
    return df

#separa os ratings em niveis alto, médio e baixo, usando quantis
def shape_data_set(df):
    all_rating_players = pd.concat([df['white_rating'], df['black_rating']], ignore_index=True)
    average_rating = (df['white_rating'] + df['black_rating'])/2
    quantis = quantil(all_rating_players, 3)

    df['level_black_player'] = [
    'low' if rating < quantis[1] else 'medium' if rating < quantis[2] else 'high' 
    for rating in df['black_rating']
    ]
    
    df['level_white_player'] = [
    'low' if rating < quantis[1] else 'medium' if rating < quantis[2] else 'high' 
    for rating in df['white_rating']
    ]

    df['game_level'] = [
        'low' if game_rating < quantis[1] else 'medium' if game_rating < quantis[2]
        else 'high' for game_rating in average_rating
    ]
        

def quantil(data, amout_division):
    """
    Calculates quantiles

    Parameters:
    ----------
    data: pd.Dataframe

        a DataFrame with the games

    amout_division: int

        number of quantiles used in the division

    Returns: 
    -------
    pd.Dataframe

        a pandas.DataFrame

    """
    quantis = {}  
    for i in range(0, amout_division):
        quantis[i + 1] = np.percentile(data, (100/amout_division)* (i + 1))
    return quantis

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

def view_boxplot(df):
    sns.boxplot(data=df)
    plt.title('Plays evaluate')
    plt.ylabel('Values')
    plt.xlabel('Level')
    plt.xticks(ticks=[0, 1, 2], labels=['Low', 'Medium', 'High'])
    plt.show()
    
    












 