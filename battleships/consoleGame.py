from gameBack import Board
from gameMechanicsBackend import Game
from playerSetup import playerSetup

def menu():
    print("Hello!")
    print("Lets go on an adventure!")
    option = input('''
                                     ______________________________________________
                                  .-'                     _                        '.
                                .'                       |-'                        |
                              .'                         |                          |
                           _.'               p         _\_/_         p              |
                        _.'                  |       .'  |  '.       |              |
                   __..'                     |      /    |    \      |              |
             ___..'                         .T\    ======+======    /T.             |
          ;;;\::::                        .' | \  /      |      \  / | '.           |
          ;;;|::::                      .'   |  \/       |       \/  |   '.         |
          ;;;/::::                    .'     |   \       |        \  |     '.       |
                ''.__               .'       |    \      |         \ |       '.     |
                     ''._          <_________|_____>_____|__________>|_________>    |
                         '._     (___________|___________|___________|___________)  |
                            '.    \;;;;;;;;;;o;;;;;o;;;;;o;;;;;o;;;;;o;;;;;o;;;;/   |
                              '.~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~   |
                                '. ~ ~ ~ ~ ~ ~ ~ ~ ~Battleship ~ ~ ~ ~ ~ ~ ~ ~ ~ ~  |
                                  '-.______________________________________________.'


        Are you ready to fight?
        ''')

    if option == 'yes':
        game()
    else:
        print("What a loser.")
        return


def game():

    firstPlayerBoard = firstPlayerSetup()
    secondPlayerBoard = secondPlayerSetup()


    battleships = Game(firstPlayerBoard, secondPlayerBoard)
    gameOver = False

    while gameOver == False:

        if battleships.currentPlayer == battleships.firstPlayer:
            currentPlayer = 'Player 1'
        else:
            currentPlayer = 'Player 2'

        prompt = input(f"Ready {currentPlayer}? ").title()
        battleships.showPlayerBoard()
        if prompt == 'Yes':
            validHit = False
            while validHit == False:
                try:
                    row = input("What row would you like to attack? ")
                    col = input("What column would you like to attack? ")
                    row = int(row)
                    col = int(col)
                except ValueError:
                    print("Invalid input!")
                    continue
                else:
                    if [row, col] in battleships.currentPlayer.listChosenCells:
                        print("Have already chosen to attack this cell")
                        continue

                validHit, hit, shipHit, shipSunk = battleships.fire(row, col)
                if validHit == True:
                    if hit == True:
                        if shipSunk == True:
                            print(f"You have sunk your opponent's {shipHit}")
                            gameOver = battleships.checkGameOver()

                        else:
                            print(f"You hit your opponent's {shipHit}")
                    else:
                        print("You missed")
                else:
                    print("Invalid cell. Try again")
            print(battleships.currentPlayer)

    print(f"Game is over. {currentPlayer} has won the game!")

menu()