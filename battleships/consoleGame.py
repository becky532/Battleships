from gameBack import Board
from gameMechanicsBackend import Game
from playerSetup import playerSetup
import logging

logging.basicConfig(filename='battleships.log', level=logging.INFO, filemode='w', force=True)

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
        ''').title()

    if option == 'Yes':
        logging.info("Game started")
        game()
    else:
        print("What a loser.")
        return


def game():

    board = Board.instance()
    board.initialise()

    board.firstPlayer = playerSetup(0)
    board.secondPlayer = playerSetup(1)

    battleships = Game(board)
    gameOver = False

    while gameOver == False:

        if battleships.currentPlayer == 0:
            currentPlayer = 'Player 1'
            playerID = 0
            opponent = 'Player 2'
        else:
            currentPlayer = 'Player 2'
            opponent = 'Player 1'
            playerID = 1

        prompt = input(f"Ready {currentPlayer}? ").title()
        logging.info(f"Current player: {currentPlayer}")

        if prompt == 'Yes':
            battleships.showPlayerBoard()
            validHit = False
            while validHit == False:
                try:
                    row = input("What row would you like to attack? ")
                    col = input("What column would you like to attack? ")
                    row = int(row)
                    col = int(col)
                except ValueError:
                    print("Invalid input!")
                    logging.info(f"{currentPlayer} has made an invalid cell choice")
                    continue
                else:
                    duplicateHit = board.checkDuplicateAttack(row, col, playerID)
                    if duplicateHit == True:
                        print("Already hit this cell, try again!")
                        logging.info(f"{currentPlayer} has chosen cell [{row}, {col}] again.")
                        continue
                    elif duplicateHit is None:
                        logging.info(f"{currentPlayer} has chosen a cell outside of grid")
                        continue

                attack = battleships.fire(row, col, playerID)
                if attack is not None:
                    validHit = attack[0]
                    hit = attack[1]
                    shipHit = attack[2]
                    shipSunk = attack[3]

                    if validHit == True:
                        if hit == True:
                            if shipSunk == True:
                                print(f"You have sunk your opponent's {shipHit}")
                                logging.info(f"{currentPlayer} has sunk {opponent}'s {shipHit}")
                                gameOver = battleships.checkGameOver()

                            else:
                                print(f"You hit your opponent's {shipHit}")
                                logging.info(f"{currentPlayer} has hit {opponent}'s {shipHit} at [{row},{col}]")
                        else:
                            print("You missed")
                            logging.info(f"{currentPlayer} failed to hit {opponent} at [{row}, {col}]")
                    else:
                        print("Invalid cell. Try again")

    print(f"Game is over. {currentPlayer} has won the game!")

menu()