import os
import pathlib
from .Database import app


def make_zip(games):
    for game in games:
        print(game)


make_zip(app.Database.fetch_all_games.generate_games())
