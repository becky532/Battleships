from flask import render_template, Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'TeamTitanic'


@app.route('/<gameType>')
def main(gameType):
    return render_template('battleship.html', gameType=gameType)




if __name__ == "__main__":
    app.run()
