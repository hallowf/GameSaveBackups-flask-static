from database import save_database


def generated_games():
    g = []
    for game in save_database:
        g.append(game.to_dict())
    return g
