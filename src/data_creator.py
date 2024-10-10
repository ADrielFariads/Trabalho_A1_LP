""""
Functions for making new data
"""

import pandas as pd
import numpy as np
import re
import doctest
import json

import Constants
import data_cleaner


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
        assert isinstance(game, str)
        assert isinstance(piece, str)

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
        print("There was an error, please select a valid piece name")
        return None
    except AssertionError:
        print("The arguments are not valid")
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
    -------
    np.array
        An array which represent the number of times each square was visited 


    """
    try:
        assert isinstance(game, str)
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

            if each == "1/2-1/2": #draw cases
                continue

            elif each == "O-O": #castle moves
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


                
            elif each[0] in squares.keys(): #usual moves
                column = squares[each[0]]
                row = 8 - int(each[-1])
                matrix[row][column] += 1
            else:
                continue
    except AssertionError:
        print("The game must be provided in string format!")
        return None

    return matrix

def piece_matrix(game:str, piece:str) -> np.array:
    """
    Generates an 8x8 matrix counting the movements of a specific piece in a chess game.

    Parameters:
    ----------
    game : str
        A string representing the moves of the game, where each move is in chess notation.
    piece : str
        The type of piece to analyze (e.g., "pawn", "king", "queen", "knight", "bishop", or "rook").

    Returns:
    -------
    np.array
        An 8x8 matrix where each element represents the number of times the specified piece has been 
        moved to the respective square on the chessboard. Returns `None` if the parameters are not of the correct type.

    """
    try:
        assert isinstance(game, str)
        assert isinstance(piece, str)
        squares = {"a":0, "b":1, "c":2, "d":3, "e":4, "f":5, "g":6, "h":7}
        pieces = {
        "pawn": [" a", " b", " c", " d", " e", " f", " g", " h"],
        "king": "K",
        "queen": "Q",
        "knight": "N",
        "bishop": "B",
        "rook": "R"}

        matrix = np.zeros((8,8), dtype=int)
        match_squares = re.sub(r'[+#=]', "", game)
        moves = match_squares.split()
        

        for each in moves:
            if piece == "pawn":
                if len(each) == 2:  
                    row = 8 - int(each[1]) 
                    column = squares[each[0]]
                    matrix[row][column] += 1

            else:
                if each[0] == pieces[piece]:  
                    row = 8 - int(each[-1]) 
                    column = squares[each[-2]]
                    matrix[row][column] += 1

        return matrix
    except AssertionError:
        return None

def pieces_columns_generator(games:pd.DataFrame) -> pd.DataFrame:
    """
    Creates columns for each piece's moves

    Parameters:
    ----------
    game : pd.DataFrame
         A data frame with chess' games, the DataFrame must have the column "moves", which is in algebric notation
    Returns:
    -------
    pd.DataFrame
         a dataframe with columns for each piece, each column contains the number of moves for that piece
    """
    df = games
    pieces = {
    "pawn": [" a", " b", " c", " d", " e", " f", " g", " h"],
    "king": "K",
    "queen": "Q",
    "knight": "N",
    "bishop": "B",
    "rook": "R"}
    for piece in pieces.keys():
        try:
            df[f"{piece}_moves"] = df["moves"].apply(count_moves, piece = piece)
            return df
        except KeyError:
            print("Houve um erro, selecione um nome válido de peça")
            return None
        

def advantage_column():
    with open("data\\games.json", 'r') as file:
        stockfish_data = json.load(file)

    advantage = [game.get('avaliacoes', None) for game in stockfish_data]

    df = data_cleaner.read_data_set()
    df = data_cleaner.add_black_white_level(df)
    df = data_cleaner.add_black_white_level(df)
    df = data_cleaner.cut_short_games(df)
    df = data_cleaner.add_game_level(df)
    df['advantage'] = advantage
    df = data_cleaner.cut_duplicates(df)

    return df






