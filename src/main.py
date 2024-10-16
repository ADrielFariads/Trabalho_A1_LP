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

graph_creator.boxplot_deviation_reviews(desvs, desvs_mean).show(block=False)

graph_creator.boxplot_all_games_reviews(games).show(block=False)

graph_creator.rating_resign_graph(df).show(block=False)

graph_creator.violin_plot(df).show()





