import sys, os
import unittest
import numpy as np
import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import data_creator


class Test_count_moves(unittest.TestCase):

    #test function in common cases
    def test_common_game_pawn(self):
        example = "e4 e5 Nf3 Nc6 Bb5 a6 Ba4 Nf6 O-O Be7 d4 d6 c3 O-O Re1 Nb8 Bc2 Nbd7 Nbd2 c6 Nf1 Qc7 Ng3 g6 Bh6 Re8 Qd2 Bf8 Bxf8 Nxf8 Qg5 Qe7 h4 h6 Qxh6 Ng4 Qd2 Kg7 h5 Nh7 dxe5 dxe5 Bb3 Be6 Bxe6 Qxe6 Rad1 Rad8 Qxd8 Rxd8 Rxd8 Qxa2 Rd7 Qxb2 hxg6 Qxf2+ Kh1 Qxg3 Rf7+ Kxg6 Rxb7 Ng5 Rf1 Nxf3 Rxf3 Qh4+ Kg1 Qe1+ Rf1 Qe3+ Kh1 Qh6+ Kg1 Qh2#"
        result = data_creator.count_moves(example, "pawn")
        self.assertEqual(result, 14)
    
    def test_common_game_knight(self):
        example = "e4 e5 Nf3 Nc6 Bb5 a6 Ba4 Nf6 O-O Be7 d3 d6 c3 O-O Nbd2 Nb8 Re1 Nbd7 Nf1 c6 Ng3 g6 d4 Qc7 h3 Re8 Bb3 Bf8 Ng5 Re7 f4 Bg7 f5 Nf8 Rf1 d5 Qf3 exd4 cxd4 dxe4 N3xe4 Bxf5 Bg5 Rxe4 Qxe4 Bxe4 Bf4 Qb6 Bxf7+ Kh8 Be5 Bxe5 Rae1 Qxd4+ Kh1 Qd2 Kh1 Qg3 Rxb7 Qh2#"
        result = data_creator.count_moves(example, "knight")
        self.assertEqual(result, 11)

    def test_common_game_bishop(self):
        example = "e4 e5 Nf3 Nc6 Bb5 a6 Ba4 Nf6 O-O Be7 d3 d6 c3 O-O Nbd2 Nb8 Re1 Nbd7 Nf1 c6 Ng3 g6 d4 Qc7 h3 Re8 Bb3 Bf8 Ng5 Re7 f4 Bg7 f5 Nf8 Rf1 d5 Qf3 exd4 cxd4 dxe4 N3xe4 Bxf5 Bg5 Rxe4 Qxe4 Bxe4 Bf4 Qb6 Bxf7+ Kh8 Be5 Bxe5 Rae1 Qxd4+ Kh1 Qd2 Kh1 Qg3 Rxb7 Qh2#"
        result = data_creator.count_moves(example, "bishop")
        self.assertEqual(result, 13)

    def test_common_game_rook(self):
        example = "d4 d5 c4 c6 Nf3 Nf6 Nc3 dxc4 a4 Bf5 e3 e6 Bxc4 Bb4 O-O O-O Qe2 Nbd7 Rd1 Qc7 h3 e5 dxe5 Nxe5 Nxe5 Qxe5 Bd2 Rad8 Be1 Bd6 f4 Qe7 Bh4 Bc5 Rxd8 Rxd8 Re1 Qd6 Kh1 Bg6 e4 Qxf4 Bxf6 Qxf6 e5 Qe7 Ne4 Bd4 Nd6 Bxe5 Qxe5 Qxd6"
        result = data_creator.count_moves(example, "rook")
        self.assertEqual(result, 5)

    def test_common_game_queen(self):
        example = "d4 d5 c4 c6 Nf3 Nf6 Nc3 dxc4 a4 Bf5 e3 e6 Bxc4 Bb4 O-O O-O Qe2 Nbd7 Rd1 Qc7 h3 e5 dxe5 Nxe5 Nxe5 Qxe5 Bd2 Rad8 Be1 Bd6 f4 Qe7 Bh4 Bc5 Rxd8 Rxd8 Re1 Qd6 Kh1 Bg6 e4 Qxf4 Bxf6 Qxf6 e5 Qe7 Ne4 Bd4 Nd6 Bxe5 Qxe5 Qxd6"
        result = data_creator.count_moves(example, "queen")
        self.assertEqual(result, 10)

    def test_common_game_king(self):

        example = "e4 c5 Nf3 d6 d4 cxd4 Nxd4 Nf6 Nc3 a6 Be2 e5 Nb3 Be7 O-O O-O Be3 Be6 f4 exf4 Bxf4 Nc6 Kh1 Qc7 Nd4 Nxd4 Qxd4 Rad8 Rad1 b5 a3 Rfe8 Bf3 Bc4 Rfe1 Nd7 Qf2 Ne5 Be3 Nxf3 Qxf3 Bf6 Bd4 Bxd4 Rxd4 d5 Red1 dxe4 Rxd8 Rxd8 Rxd8+ Qxd8 Nxe4 Bd5 Qf4 h6 Nc3 Bc6 h3 Qe7 Kh2 Qe6 Qd4 a5 Qf4 b4 axb4 axb4 Nd1 b3 c3 Qe2 Nf2 Qxb2 Qb8+ Kh7 Qf4 Qc2 Qd4 b2 Qd3+ Qxd3 Nxd3 b1=Q"
        result = data_creator.count_moves(example, "king")
        self.assertEqual(result, 3)

    #test the function for a wrong key name
    def test_not_a_piece_name(self):

        example = "e4 c5 Nf3 d6 d4 cxd4 Nxd4 Nf6 Nc3 a6 Be2 e5 Nb3 Be7 O-O O-O Be3 Be6 f4 exf4 Bxf4 Nc6 Kh1 Qc7 Nd4 Nxd4 Qxd4 Rad8 Rad1 b5 a3 Rfe8 Bf3 Bc4 Rfe1 Nd7 Qf2 Ne5 Be3 Nxf3 Qxf3 Bf6 Bd4 Bxd4 Rxd4 d5 Red1 dxe4 Rxd8 Rxd8 Rxd8+ Qxd8 Nxe4 Bd5 Qf4 h6 Nc3 Bc6 h3 Qe7 Kh2 Qe6 Qd4 a5 Qf4 b4 axb4 axb4 Nd1 b3 c3 Qe2 Nf2 Qxb2 Qb8+ Kh7 Qf4 Qc2 Qd4 b2 Qd3+ Qxd3 Nxd3 b1=Q"
        result = data_creator.count_moves(example, "viking")
        self.assertEqual(result, None)



class Test_game_matrix(unittest.TestCase):

    #testthe function for a common game
    def test_common_game(self):
        example = "e4 e5 Nf3 Nc6 Bb5 a6 Ba4 Nf6 O-O Be7 d4 d6 c3 O-O Re1 Nb8 Bc2 Nbd7 Nbd2 c6 Nf1 Qc7 Ng3 g6 Bh6 Re8 Qd2 Bf8 Bxf8 Nxf8 Qg5 Qe7 h4 h6 Qxh6 Ng4 Qd2 Kg7 h5 Nh7 dxe5 dxe5 Bb3 Be6 Bxe6 Qxe6 Rad1 Rad8 Qxd8 Rxd8 Rxd8 Qxa2 Rd7 Qxb2 hxg6 Qxf2+ Kh1 Qxg3 Rf7+ Kxg6 Rxb7 Ng5 Rf1 Nxf3 Rxf3 Qh4+ Kg1 Qe1+ Rf1 Qe3+ Kh1 Qh6+ Kg1 Qh2#"
        result = data_creator.game_matrix(example)
        expected_result = np.array([[1, 1, 0, 3, 1, 4, 1, 0],
        [0, 2, 1, 1, 2, 1, 1, 1],
       [1, 0, 2, 1, 3, 1, 2, 5],
       [0, 1, 0, 2, 1, 0, 2, 1],
       [1, 0, 0, 1, 1, 0, 1, 2],
       [0, 1, 1, 0, 1, 3, 2, 0],
       [1, 2, 1, 2, 0, 1, 0, 1],
       [1, 0, 0, 0, 2, 4, 3, 2]])
        
        np.testing.assert_equal(result, expected_result) #function for compare arrays


    def test_not_a_string(self):
        example =  {
    1: {"white": "e4", "black": "e5"},
    2: {"white": "Nf3", "black": "Nc6"},
    3: {"white": "Bb5", "black": "a6"},
    4: {"white": "Ba4", "black": "Nf6"},
    5: {"white": "O-O", "black": "Be7"},
    6: {"white": "d4", "black": "d6"},
    7: {"white": "c3", "black": "O-O"},
    8: {"white": "Re1", "black": "Nb8"},
    9: {"white": "Bc2", "black": "Nbd7"},
    10: {"white": "Nbd2", "black": "c6"},
    11: {"white": "Nf1", "black": "Qc7"},
    12: {"white": "Ng3", "black": "g6"},
    13: {"white": "Bh6", "black": "Re8"},
    14: {"white": "Qd2", "black": "Bf8"},
    15: {"white": "Bxf8", "black": "Nxf8"},
    16: {"white": "Qg5", "black": "Qe7"},
    17: {"white": "h4", "black": "h6"},
    18: {"white": "Qxh6", "black": "Ng4"},
    19: {"white": "Qd2", "black": "Kg7"},
    20: {"white": "h5", "black": "Nh7"},
    21: {"white": "dxe5", "black": "dxe5"},
    22: {"white": "Bb3", "black": "Be6"},
    23: {"white": "Bxe6", "black": "Qxe6"},
    24: {"white": "Rad1", "black": "Rad8"},
    25: {"white": "Qxd8", "black": "Rxd8"},
    26: {"white": "Rxd8", "black": "Qxa2"},
    27: {"white": "Rd7", "black": "Qxb2"},
    28: {"white": "hxg6", "black": "Qxf2+"},
    29: {"white": "Kh1", "black": "Qxg3"},
    30: {"white": "Rf7+", "black": "Kxg6"},
    31: {"white": "Rxb7", "black": "Ng5"},
    32: {"white": "Rf1", "black": "Nxf3"},
    33: {"white": "Rxf3", "black": "Qh4+"},
    34: {"white": "Kg1", "black": "Qe1+"},
    35: {"white": "Rf1", "black": "Qe3+"},
    36: {"white": "Kh1", "black": "Qh6+"},
    37: {"white": "Kg1", "black": "Qh2#"}
}
        result = data_creator.game_matrix(example)
        self.assertEqual(result, None)


class Test_piece_matrix(unittest.TestCase):
    def test_common_moves_pawn(self):
        example = "e4 e5 Nf3 Nc6 Bb5 a6 Ba4 Nf6"
        result = data_creator.piece_matrix(example, "pawn")
        expected_result = np.array([[0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
       [1, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 1, 0, 0, 0],
       [0, 0, 0, 0, 1, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0]])
        np.testing.assert_equal(result, expected_result)

    def test_common_moves_knight(self):
        example = "e4 e5 Nf3 d4 Bb5 a6 Ba4 Nf6"
        result = data_creator.piece_matrix(example, "knight")
        expected_result = np.array([[0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 1, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 1, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0]])
        np.testing.assert_equal(result, expected_result)
        
    def test_not_a_valid_game_piece(self):
        example = "e4 e5 Nf3 d4 Bb5 a6 Ba4 Nf6"
        result = data_creator.piece_matrix(example, "cavalo")
        self.assertEqual(result, None)
        
        





if __name__ == "__main__":
    unittest.main()
    