import pandas as pd
import numpy as np
import re


def count_moves(game, piece):
  
  pieces = {
    "pawn": [" a", " b", " c", " d", " e", " f", " g", " h"],
    "king": "K",
    "queen": "Q",
    "knight": "N",
    "bishop": "B",
    "rook": "R"
}
  
  try:
      if piece.lower() == "pawn":
          result = 0
          if game[0] in "a b c d e f g h".split():
            result +=1
          for each in pieces["pawn"]:
              moves = game.count(each)
              result += moves
          return result
      else:
          piece = piece.lower()
          piece_code = pieces[piece]

          moves = game.count(piece_code)
          return moves
  except KeyError:
    print("Houve um erro, selecione um nome válido de peça")
    return None
