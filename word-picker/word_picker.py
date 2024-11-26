from random import choice
from flask import Flask

app = Flask(__name__)

options = ["first", "second", "third"]

@app.route("/")
def pick_word():
    return choice(options)