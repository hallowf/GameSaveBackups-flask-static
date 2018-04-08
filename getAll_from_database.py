from database import save_database


def get_all_in_database():
    for game in save_database:
        print(game)
        game_dict = game.to_dict()
        yield game_dict
