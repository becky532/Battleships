from gameBack import Board
from gameMechanicsBackend import Game
from playerSetup import playerSetup
from classAI import AI
import logging
import time

def chooseSettings():
    logging.basicConfig(filename='battleships.log', level=logging.INFO, filemode='w', force=True)

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
            logging.info("Playing against computer")
            gameAI()
        elif chooseAI == 'No':
            game()
    else:
        print("What a loser.")
        return

def playerAttack(currentPlayer, gamePlaying: Game, boardPlaying: Board, AI):
    if currentPlayer == 0:
        player = 'Player 1'
        opponent = 'Player 2'
    elif currentPlayer == 1 and AI == True:
        player = 'Computer'
        opponent = 'Player 1'
    else:
        player = 'Player 2'
        opponent = 'Player 1'

    prompt = input(f"Ready {player} ").title()
    logging.info(f"Current player: {player}")
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
                logging.info(f"{player} has made an invalid cell choice")
                continue
            else:
                duplicateHit = boardPlaying.checkDuplicateAttack(row, col, currentPlayer)
                if duplicateHit == True:
                    print("Already hit this cell, try again!")
                    logging.info(f"{player} has chosen cell [{row}, {col}] again.")
                    continue
                elif duplicateHit is None:
                    logging.info(f"{player} has chosen a cell outside of grid")
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
                            logging.info(f"{player} has sunk {opponent}'s {shipHit}")
                        else:
                            print(f"You hit your opponent's {shipHit}")
                            logging.info(f"{player} has hit {opponent}'s {shipHit} at [{row},{col}]")
                    else:
                        print("You missed")
                        logging.info(f"{player} failed to hit {opponent} at [{row}, {col}]")
                else:
                    print("Invalid cell. Try again")
    return gameOver

def playerAI(AIPlayer: AI, game:Game, board: Board):
    duplicate = True
    while duplicate == True:
        [row, col] = AIPlayer.decideAttack()
        duplicate = board.checkDuplicateAttack(row, col, 1)

    AIAttack = game.fire(row, col, 1)  ##need to then add to AI list!!!
    logging.info(f"Computer attacked at [{row}, {col}]")

    success = AIAttack[1]
    shipHit = AIAttack[2]
    shipSunk = AIAttack[3]
    gameOver = AIAttack[4]

    if success == True:
        AIPlayer.targets[shipHit].append([row, col])
        print(f"The computer has hit your {shipHit} at [{row}, {col}]")
        logging.info(f"Computer hit player's {shipHit} at [{row}, {col}]")
    else:
        print("The computer failed to hit a ship")
        logging.info("Computer missed")
    if shipSunk == True:
        AIPlayer.destroyed[shipHit] = True
        print(f"The computer has sunk your {shipHit}. Oh no!")
        logging.info(f"Computer has sunk player's {shipHit}")

    return gameOver

def game():
    board = Board.instance()
    board.initialise()

    board.firstPlayer = playerSetup(0)
    board.secondPlayer = playerSetup(1)

    battleships = Game(board)
    gameOver = False
    AIPlaying = False

    while gameOver == False:

        gameOver = playerAttack(battleships.currentPlayer, battleships, board, AIPlaying)

    print(f"Game is over. {battleships.currentPlayer} has won the game!")

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
            AIPlaying = True
            gameOver = playerAttack(battleships.currentPlayer, battleships, board, AIPlaying)
        if battleships.currentPlayer == 1:
            print("Computer's turn to attack")
            time.sleep(2)
            gameOver = playerAI(AIPlayer, battleships, board)


    if gameOver == True and battleships.currentPlayer == 0:
        print("Congratulations, you beat the computer")
    elif gameOver == True and battleships.currentPlayer == 1:
        print("You lost!")

if __name__ == '__main__':
    chooseSettings()