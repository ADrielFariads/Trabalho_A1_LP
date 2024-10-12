import unittest
import chess
import pandas as pd
import game
import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'games.csv')))

class TestGameInfo(unittest.TestCase):
    
    def setUp(self):
        file = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'games.csv'))
        
        self.df = pd.read_csv(file)

    def test_all_elements_completed(self):
        
        self.df.loc[0:4, "game_level"] = "value" # Assumes that the shape dataset function works correctly
        result = game.game_info(self.df[0:5])        
        list = []
        for index, row in self.df[0:5].iterrows():
            row["game_level"] = "value" # Assumes that the shape dataset function works correctly
            list.append({"notation": row["moves"].split(), "level": row["game_level"], "board": chess.Board(), "reviews": [], "white_check": 0, "black_check": 0, "jumped_plays": 0})
        self.assertEqual(list, result)

    def test_without_moves(self):
        self.df.loc[0:4, "game_level"] = "value" # Assumes that the shape dataset function works correctly
        self.df.loc[0:4, "moves"] = None
        result = game.game_info(self.df[0:5])
        self.assertEqual(result, [])
    
    def test_without_moves(self):
        self.df.loc[0:4, "game_level"] = "value" # Assumes that the shape dataset function works correctly
        self.df.loc[0:4, "game_level"] = None
        result = game.game_info(self.df[0:5])
        self.assertEqual(result, [])
               


          