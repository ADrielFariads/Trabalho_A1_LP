import chess
import chess.engine
import Constants

def game_info(df):
    dic_list = []
    for index, row in df.iterrows():
        obj = {"notation": row["moves"].split(), "level": row["game_level"], "tabuleiro": chess.Board(), "avaliacoes": [], "white_check": 0, "black_check": 0, "jumped_plays": 0}
        dic_list.append(obj)
    return dic_list

def avaliar_jogo(games, motor):
    games_num = 0
    for game in games:
        for movimento in game["notation"]:
            game["tabuleiro"].push_san(movimento)
            try:
                resultado = motor.analyse(game["tabuleiro"], chess.engine.Limit(time=1.0, depth=15))
                score = resultado['score']
                if score.is_mate():
                    if game["tabuleiro"].turn == True:
                        game["white_check"] =  game["white_check"] + 1 
                    else: 
                        game["black_check"] = game["white_check"] + 1
                if not isinstance(score.relative.score() , int):
                    continue
                game["avaliacoes"].append(score.relative.score() / 100)  # Converte centipawns para peões
            except TimeoutError: 
                game["jumped_plays"] = game["jumped_plays"] + 1
                continue
        games_num = games_num + 1
        print(games_num)
    print(games)
    
    

def stock_fish(dic_list):
    dic_list = dic_list[:100]
    print(dic_list)
    try:
        engine = chess.engine.SimpleEngine.popen_uci(Constants.Constants.stockfish_path)
        with engine as motor:
                x = avaliar_jogo(dic_list, motor)  # Passa o motor como argumento
    except chess.engine.EngineTerminatedError as error:
        print(f"Ocorreu um erro ao iniciar o motor: {error}")
        

    
