from flask import render_template, Blueprint, Flask
import json

app = Flask(__name__)


@app.route('/')
def main():

    return render_template('battleship.html')


if __name__ == "__main__":
    app.run()

