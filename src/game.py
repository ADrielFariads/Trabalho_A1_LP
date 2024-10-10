import chess
import pandas as pd
import chess.engine
import Constants
import json
import sys

def game_info(df: pd.DataFrame) -> list:
    """
    Creates a dictionary with information about each game

    Parameters:
    ----------
    df: Dataframe

        a DataFrame with the games

    Returns: 
    -------
    list

        a dictionary list with matchs informations

    """
    games_list = []
    for index, row in df.iterrows():
        if( not row["moves"] or not row["game_level"]):
            continue
        obj = {"notation": row["moves"].split(), "level": row["game_level"], "board": chess.Board(), "reviews": [], "white_check": 0, "black_check": 0, "jumped_plays": 0}
        games_list.append(obj)
    return games_list

def evaluate_games(games, motor, time, depth):
    """
    Evaluate the games with stockfish

    Parameters:
    ----------
    games: List
        a dictionary list with matchs informations
    motor: chess.engine.SimpleEngine
        a interface for stockfish
    time: 
        time for position analysis
    depth: depth of analysis, number of plies analysys
    
    Returns: 
    -------
    List
        a dictionary list with matchs informations
    """
    games_num = 0
    for game in games:
        print(game)
        for movimento in game["notation"]:
            game["board"].push_san(movimento)
            try:
                resultado = motor.analyse(game["board"], chess.engine.Limit(time=time, depth=depth))
                score = resultado['score']
                if score.is_mate():
                    if game["board"].turn == True:
                        game["white_check"] =  game["white_check"] + 1 
                    else: 
                        game["black_check"] = game["white_check"] + 1
                if not isinstance(score.relative.score() , int):
                    continue
                game["reviews"].append(score.relative.score() / 100)  # Converts centipawns to pawns
            except TimeoutError: 
                game["jumped_plays"] = game["jumped_plays"] + 1
                continue
        games_num = games_num + 1
        print(games_num)
    return games
    
    

def stock_fish(dic_list):
    """
    Starts stockfish and calls another function to evaluate the games or returns the games evaluated at the desired depth.

    Parameters:
    ----------
    dic_list: List
        a dictionary list with matchs informations

    Returns: 
    -------
    list:
        a dictionary list with matchs informations

    """
    while True:
        use_stockfish = input("Do you want to use Stockfish? (Y/N)") 
        if(use_stockfish == "Y" or use_stockfish == "y"):
            while True:                
                try:
                    depth = int(input("What is the depth of analysis desired?? (1-99)"))
                    time = int(input("time for position analysis? (0.01-20)"))
                    if(depth < 0.01 or depth > 99):
                        print("Invalid number entered!! Enter a number from 1 to 99")
                        continue
                    elif (time < 0.01 or time > 20):
                        print("Invalid number entered!! Enter a number from 0.01 to 20")
                        continue
                    else:
                        try:
                            engine = chess.engine.SimpleEngine.popen_uci(Constants.Constants.stockfish_path) # Engine initiation
                            with engine as motor:
                                return evaluate_games(dic_list, motor, time, depth)  # Passes the engine as an argument
                        except chess.engine.EngineTerminatedError as error:
                                print(f"Couldn't start the engine: {error}")
                                sys.exit(1)
                        except FileNotFoundError as error:
                            print(f"Path given to stockfish invalid: {error}")
                            sys.exit(1)
                except ValueError:
                        print("Invalid caracter entered!!")
                        continue
        elif (use_stockfish) == "N" or use_stockfish == "n":
            try:
                with open("games.json", "r") as file:
                    games = json.load(file) # Loads the pre-processed data
                    return games        
            except FileNotFoundError:
                print("Arquivo pré processado não foi encontrado!!")    
                sys.exit(1)   
        else:
            print("Invalid character!!! Enter Y or N")
            continue
        

    

