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

@app.route("/api/play/<path:song_path>")
def play(song_path):
    song_path = os.path.join("/home/cafalchio/portainer/downloads/lidarr", song_path)
    if os.path.isfile(song_path):
        try:
            # Using subprocess to play the song
            command = ["mpg123", "-a", "hw:CARD=rockchipes8388,DEV=0", song_path]
            subprocess.Popen(command)
            print(f"Playing {song_path}")
            return jsonify({"message": f"Playing {song_path}"}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    else:
        return jsonify({"error": "Song not found."}), 404


if __name__ == '__main__':
    app.run(debug=True)