from Database import database


def generated_games():
    g = []
    for game in database.save_database:
        g.append(game.to_dict())
    return g
