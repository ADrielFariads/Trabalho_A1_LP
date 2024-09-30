import sys, os
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import data_creator


class Test_count_moves(unittest.TestCase):

    def test_common_game_pawn(self):
        example = "e4 e5 Nf3 Nc6 Bb5 a6 Ba4 Nf6 O-O Be7 d4 d6 c3 O-O Re1 Nb8 Bc2 Nbd7 Nbd2 c6 Nf1 Qc7 Ng3 g6 Bh6 Re8 Qd2 Bf8 Bxf8 Nxf8 Qg5 Qe7 h4 h6 Qxh6 Ng4 Qd2 Kg7 h5 Nh7 dxe5 dxe5 Bb3 Be6 Bxe6 Qxe6 Rad1 Rad8 Qxd8 Rxd8 Rxd8 Qxa2 Rd7 Qxb2 hxg6 Qxf2+ Kh1 Qxg3 Rf7+ Kxg6 Rxb7 Ng5 Rf1 Nxf3 Rxf3 Qh4+ Kg1 Qe1+ Rf1 Qe3+ Kh1 Qh6+ Kg1 Qh2#"
        result = data_creator.count_moves(example, "pawn")
        self.assertEqual(result, 14)
    
    def test_common_game_knight(self):
        example = "e4 e5 Nf3 Nc6 Bb5 a6 Ba4 Nf6 O-O Be7 d3 d6 c3 O-O Nbd2 Nb8 Re1 Nbd7 Nf1 c6 Ng3 g6 d4 Qc7 h3 Re8 Bb3 Bf8 Ng5 Re7 f4 Bg7 f5 Nf8 Rf1 d5 Qf3 exd4 cxd4 dxe4 N3xe4 Bxf5 Bg5 Rxe4 Qxe4 Bxe4 Bf4 Qb6 Bxf7+ Kh8 Be5 Bxe5 Rae1 Qxd4+ Kh1 Qd2 Kh1 Qg3 Rxb7 Qh2#"
        result = data_creator.count_moves(example, "knight")
        self.assertEqual(result, 11)
        
    

if __name__ == "__main__":
    unittest.main()
    