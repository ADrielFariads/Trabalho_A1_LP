import data
import game

df = data.read_data_set()
data.shape_data_set(df)
df = data.cut_short_games(df)
games = game.game_info(df)
game.stock_fish(games)







