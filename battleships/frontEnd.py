from flask import render_template, Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'TeamTitanic'


@app.route('/')
def main():
    return render_template('battleship.html')


if __name__ == "__main__":
    app.run()
