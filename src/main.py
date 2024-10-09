import Trabalho_A1.Trabalho_A1_LP.src.data_cleaner as data_cleaner
import game


df = data_cleaner.read_data_set()
data_cleaner.add_black_white_level(df)
df = data_cleaner.cut_duplicates(df)
df = data_cleaner.cut_short_games(df)
games = game.game_info(df)
game.stock_fish(games)






