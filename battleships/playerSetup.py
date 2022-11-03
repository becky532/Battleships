from gameBack import Board


def playerSetup(player):
    board = Board.instance()
    if player == 0:
        print('Player 1 Setup')
    else:
        print('Player 2 Setup')

    listPlayerPieces = ['Carrier', 'Battleship', 'Cruiser', 'Submarine', 'Destroyer']

    random = input("Random? ").title()
    if random == 'Yes':
        board.randomiseBoard(player)
        board.printBoard(player)
    else:
        while len(listPlayerPieces) > 0:

            validInput = False

            print("")
            print(listPlayerPieces)
            while validInput == False:

                try:
                    whichShip = input("Choose the ship type: ")
                    whichRow = input("Choose a row for your ship: ")
                    whichCol = input("Choose a column for your ship: ")
                except ValueError:
                    print("Invalid input!")
                    continue

                row = int(whichRow)
                col = int(whichCol)

                shipType = whichShip

                if shipType not in listPlayerPieces:
                    print("try again")
                else:
                    validInput = True

            validPosition = board.placeShip(row, col, shipType, player)

            if validPosition == False:
                print("Cannot place ship here")
                continue
            else:
                board.printBoard(player)
                listPlayerPieces.remove(whichShip)

                rotate = input("Would you like to rotate your ship?").title()
                if rotate == 'Yes':
                    rotateValid = board.rotateShip(whichShip, player)
                    if rotateValid == True:
                        print(f"{whichShip} Rotated")
                        board.printBoard(player)
                    else:
                        print(f"{whichShip} can't be rotated")
                else:
                    continue
    if player == 0:
        return board.firstPlayer
    else:
        return board.secondPlayer


