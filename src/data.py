import pandas as pd
import Constants
import numpy as np

df = pd.read_csv(Constants.Constants.path)

def read_data_set():
    df = pd.read_csv(Constants.Constants.path)
    return df

#elimina jogos com 3 ou menos turnos
def cut_short_games(df):
    
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
        

def quantil(dados, quantidade_divisão):
    quantis = {}  
    for i in range(0, quantidade_divisão):
        quantis[i + 1] = np.percentile(dados, (100/quantidade_divisão)* (i + 1))
    return quantis





 