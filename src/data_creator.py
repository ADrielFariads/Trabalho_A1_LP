import pandas as pd
import numpy as np
import re
import doctest


def count_moves(game:str, piece:str) -> int:
    """
    Counts the number of moves made by a specific chess piece in a game represented in algebraic notation.

    Parameters:
    ----------
    game : str
        A string representing a chess game in algebraic notation.
        Example:
        "e4 e5 Nf3 Nc6 Bb5 a6 Ba4 Nf6 O-O Be7 d4 d6 c3 O-O Re1 Nb8 Bc2 Nbd7"
    
    piece : str
        The name of the chess piece to count moves for.
        Example: "pawn"
    Returns:
    -------
    int
        The number of moves made by the specified chess piece in the game.

    None
        If an invalid piece name is provided, the function returns None and prints an error message.

    Examples
    --------
    >>> game = "e4 e5 Nf3 Nc6 Bb5 a6 Ba4 Nf6 O-O Be7 d4 d6 c3 O-O Re1 Nb8 Bc2 Nbd7 Nbd2 c6"
    >>> count_moves(game, "pawn")
    8
    >>> count_moves(game, "knight")
    4
    >>> count_moves(game, "king")
    1
    >>> count_moves(game, "dragon")
    Houve um erro, selecione um nome válido de peça
    None
        """
    
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

def game_matrix(game:str) -> np.array:
    """
    creates an 8x8 matrix which represents the most visited squares in the chess game

    Parameters:

    ----------
    game: str
        a string which represents the following game with algebrial notation
        Example:
            "e4 e5 Nf3 Nc6 Bb5 a6 Ba4 Nf6 O-O Be7 d4 d6 c3 O-O Re1 Nb8 Bc2 Nbd7"

    Returns: 
    ----------
    np.array
        An array which represent the number of times each square was visited 


    """
    squares = {"a":0,
               "b":1, 
               "c":2, 
               "d":3, 
               "e":4, 
               "f":5, 
               "g":6, 
               "h":7}

    matrix = np.zeros((8,8), dtype=int)

    match_squares = re.sub(r'[KQNRBx+#=]', "", game)
    moves = match_squares.split()

    for i, each in enumerate(moves):

        if each == "1/2-1/2":
            continue

        elif each == "O-O":
            if i % 2 == 1:
                matrix[7][6] += 1
                matrix[7][5] += 1
            else:
                matrix[0][6] += 1
                matrix[0][5] += 1

        elif each == "O-O-O":
            if i % 2 == 1:
                matrix[7][2] += 1
                matrix[7][3] += 1
            else:
                matrix[0][2] += 1
                matrix[0][3] += 1


            
        elif each[0] in squares.keys():
            column = squares[each[0]]
            row = 8 - int(each[-1])
            matrix[row][column] += 1
        else:
            continue



    return matrix



