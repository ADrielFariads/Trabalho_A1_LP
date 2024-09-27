import pandas as pd
import Constants
import numpy as np


def read_data_set():
    df = pd.read_csv(Constants.Constants.path)
    return df

def shape_data_set(df):
    all_rating_players = pd.concat([df['white_rating'], df['black_rating']], ignore_index=True)
    quantis = quantil(all_rating_players, 3)

    df['level_black_player'] = [
    'easy' if rating < quantis[1] else 'medium' if rating < quantis[2] else 'hard' 
    for rating in df['black_rating']
    ]
    
    df['level_white_player'] = [
    'easy' if rating < quantis[1] else 'medium' if rating < quantis[2] else 'hard' 
    for rating in df['white_rating']
    ]
        

def quantil(dados, quantidade_divisão):
    quantis = {}  
    for i in range(0, quantidade_divisão):
        quantis[i + 1] = np.percentile(dados, (100/quantidade_divisão)* (i + 1))
    return quantis


 
