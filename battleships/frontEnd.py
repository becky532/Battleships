from flask import render_template, Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'TeamTitanic'


@app.route('/')
def menu():
    return render_template('menu.html')


@app.route('/game/<gameType>')
def game(gameType):
    return render_template('battleship.html', gameType=gameType)


@app.route('/victory')
def victory():
    return render_template('victory.html')


@app.route('/defeat')
def defeat():
    return render_template('defeat.html')


if __name__ == "__main__":
    app.run()
