from flask import Flask, render_template, Response, send_file, request, jsonify
from app import app
from app.Database.fetch_all_games import convert_path as get_games, generate_games

### Page routes

@app.before_request
def before_req():
    #request.url
    pass

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/games")
def games():
    #import pdb; pdb.set_trace()
    user_id = request.args['user_id']
    return jsonify({
        "synced_game_list": get_games(user_id),
        "unsynced_game_list": generate_games(),
    })
