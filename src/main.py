import data_cleaner
import game
import graph_creator
import data_creator

df = data_cleaner.read_data_set()
data_cleaner.add_black_white_level(df)
df = data_cleaner.cut_duplicates(df)
df = data_cleaner.add_black_white_level(df)
df = data_cleaner.cut_short_games(df)
df = data_cleaner.add_game_level(df)

games = game.game_info(df)
games = game.stockfish(games)
desvs, desvs_mean = data_creator.desvpad_evaluate(games)

graph_creator.view_boxplot(desvs, desvs_mean)






