from flask import Flask, render_template, Response, send_file
from app import app

### Page routes

@app.route("/")
def index():
    return render_template("index.html")
