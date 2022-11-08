from flask import render_template, Blueprint, Flask

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('menu.html')

if __name__ == "__main__":
    app.run()