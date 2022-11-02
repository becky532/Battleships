from flask import render_template, Blueprint, Flask
import json

app = Flask(__name__)


@app.route('/')
def main():

    return render_template('battleship.html')


@app.route('/validDrop/<coord>')
def checkCoord(coord):
    print(coord)
    # dropValid = checkDrop(coord)
    dropValid = True
    return json.dumps(dropValid)


if __name__ == "__main__":
    app.run()

