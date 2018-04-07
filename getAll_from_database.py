from database import save_database


def get_all_in_database():
    for game in save_database:
        yield game.to_dict()
