from database import save_database


def get_all_in_database():
    for game in save_database:
        print(game)
        game_dict = game.to_dict()
        yield game_dict


def generated_games():
    for game in save_database:
        g = yield game.to_dict()
    return g

    #print ("Generating games")
    #gen_games = get_all_in_database()
    #print("Games = ", gen_games)
    #return gen_games
