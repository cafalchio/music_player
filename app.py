from flask import Flask, render_template, jsonify
from data import library
from api.api_calls import get_library_data, local_play
from data.library import get_local_library

app = Flask(__name__, template_folder='templates')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/library")
def library():
    files = get_local_library()
    return jsonify(files)



if __name__ == '__main__':
    app.run(debug=True)