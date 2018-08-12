from flask import Flask, render_template, Response, send_file, request
from app import app

### Page routes

@app.before_request
def before_req():
    #request.url

@app.route("/")
def index():
    return render_template("index.html")
