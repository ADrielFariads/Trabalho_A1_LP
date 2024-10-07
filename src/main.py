import pandas as pd
import data
import game
import Constants


key = input("Insira uma chave openIA: ")
Constants.Constants.key = key

df = data.read_data_set()
data.shape_data_set(df)
df = data.cut_short_games(df)
games = game.game_info(df)
game.stock_fish(games)







