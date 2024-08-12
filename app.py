import os

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

@app.route("/api/play/<song>")
def play(song):
    os.system(f"mpg123 -a hw:CARD=rockchipes8388,DEV=0 {song}")
    print(f"Playing {song}")


if __name__ == '__main__':
    app.run(debug=True)