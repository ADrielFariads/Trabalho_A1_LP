import data_cleaner
import game

import Constants

df = data_cleaner.read_data_set()
df = data_cleaner.add_black_white_level(df)
df = data_cleaner.cut_duplicates(df)
df = data_cleaner.add_black_white_level(df)
df = data_cleaner.cut_short_games(df)
df = data_cleaner.add_game_level(df)

games = game.game_info(df)
game.stock_fish(games)






