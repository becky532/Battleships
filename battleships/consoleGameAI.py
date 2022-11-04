from gameBack import Board
from gameMechanicsBackend import Game
from playerSetup import playerSetup
from classAI import AI
from consoleGame import game
import logging

logging.basicConfig(filename='battleships.log', level=logging.INFO, filemode='w', force=True)

def playerAttack(currentPlayer, gamePlaying: Game, boardPlaying: Board):
    prompt = input(f"Ready {currentPlayer}? ").title()
    logging.info(f"Current player: {currentPlayer}")
    gameOver = False

    if prompt == 'Yes':
        gamePlaying.showPlayerBoard()
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
                duplicateHit = boardPlaying.checkDuplicateAttack(row, col, currentPlayer)
                if duplicateHit == True:
                    print("Already hit this cell, try again!")
                    logging.info(f"{currentPlayer} has chosen cell [{row}, {col}] again.")
                    continue
                elif duplicateHit is None:
                    logging.info(f"{currentPlayer} has chosen a cell outside of grid")
                    continue

            attack = gamePlaying.fire(row, col, currentPlayer)
            if attack is not None:
                validHit = attack[0]
                hit = attack[1]
                shipHit = attack[2]
                shipSunk = attack[3]
                gameOver = attack[4]

                if validHit == True:
                    if hit == True:
                        if shipSunk == True:
                            print(f"You have sunk your opponent's {shipHit}")
                            logging.info(f"{currentPlayer} has sunk {currentPlayer}'s {shipHit}")
                        else:
                            print(f"You hit your opponent's {shipHit}")
                            logging.info(f"{currentPlayer} has hit {currentPlayer}'s {shipHit} at [{row},{col}]")
                    else:
                        print("You missed")
                        logging.info(f"{currentPlayer} failed to hit {currentPlayer} at [{row}, {col}]")
                else:
                    print("Invalid cell. Try again")
    return gameOver


def chooseSettings():
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
        chooseAI = input("Would you like to play the computer? ").title()
        if chooseAI == 'Yes':
            gameAI()
        elif chooseAI == 'No':
            game()
    else:
        print("What a loser.")
        return


def gameAI():
    board = Board.instance()
    board.initialise()
    board.firstPlayer = playerSetup(0)

    AIPlayer = AI.instance()
    AIPlayer.initialise()
    board.randomiseBoard(1)  ##making player 2 (AI) board
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

        if battleships.currentPlayer == 0:
            gameOver = playerAttack(battleships.currentPlayer, battleships, board)
        if battleships.currentPlayer == 1:
            row = AIPlayer.decideAttack()[0]
            col = AIPlayer.decideAttack()[1]
            AIAttack = battleships.fire(row, col, 1) ##need to then add to AI list!!!
            success = AIAttack[1]
            shipHit = AIAttack[2]
            shipSunk = AIAttack[3]
            gameOver = AIAttack[4]
            if success == True:
                AIPlayer.targets[shipHit].append([row, col])
                print(f"The computer has hit your {shipHit} at [{row}, {col}]")
            if shipSunk == True:
                AIPlayer.destroyed[shipHit] = True
                print(f"The computer has sunk your {shipHit}. Oh no!")

            print(AIAttack)


    print(f"Game is over. {currentPlayer} has won the game!")

chooseSettings()