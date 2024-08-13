import os
import subprocess

from flask import Flask, render_template, jsonify
from data.library import get_local_library

app = Flask(__name__, template_folder='templates')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/library")
def library():
    files = get_local_library()
    return render_template("music.html", files=files)

@app.route("/api/play/<string:id>")
def play(id):
    print(f"Playing {id}")
    pass


if __name__ == '__main__':
    app.run(debug=True)