from gameBack import Board
from gameMechanicsBackend import Game

firstPlayerBoard = Board()
firstPlayerBoard.randomiseBoard()
secondPlayerBoard = Board()
secondPlayerBoard.randomiseBoard()

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
            row = input("What row would you like to attack? ")
            col = input("What column would you like to attack? ")
            validHit, hit, shipHit, shipSunk = battleships.fire(int(row), int(col))
            if validHit == True:
                if hit == True:
                    if shipSunk == True:
                        print(f"You have sunk your opponent's {shipHit}")
                    else:
                        print(f"You hit your oppenent's {shipHit}")
                else:
                    print("You missed")
                gameOver = battleships.checkGameOver()
            else:
                print("Invalid cell. Try again")

    print(f"Game is over. {currentPlayer} has won the game!")
