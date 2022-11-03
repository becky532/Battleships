from gameBack import Board


def firstPlayerSetup():

    print("Player1 Setup")

    firstPlayerBoard = Board()
    firstPlayerBoard.newBoard()
    listFirstPlayerPieces = list(firstPlayerBoard.shipsDict.keys())
    firstPlayerBoard.printBoard()

    while len(listFirstPlayerPieces) > 0:

        validInput = False

        print(listFirstPlayerPieces)
        while validInput == False:
            whichShip = input("Choose the ship type: ")
            whichRow = input("Choose a row for your ship: ")
            whichCol = input("Choose a column for your ship: ")
            row = int(whichRow)
            col = int(whichCol)

            shipType = str(whichShip)

            if shipType not in listFirstPlayerPieces:
                print("try again")
            else:
                validInput = True

        validPosition = firstPlayerBoard.placeShip(row, col, shipType)
        if validPosition == False:
            print("Cannot place ship here")
            continue
        else:
            firstPlayerBoard.printBoard()
            listFirstPlayerPieces.remove(whichShip)
            rotate = input("Would you like to rotate your ship?").title()
            if rotate == 'Yes':
                rotateValid = firstPlayerBoard.rotateShip(whichShip)
                if rotateValid == True:
                    print(f"{whichShip} Rotated")
                    firstPlayerBoard.printBoard()
                else:
                    print(f"{whichShip} can't be rotated")
            else:
                continue

    return firstPlayerBoard


def secondPlayerSetup():

    print("Player2 Setup")

    secondPlayerBoard = Board()
    secondPlayerBoard.newBoard()
    listSecondPlayerPieces = list(secondPlayerBoard.shipsDict.keys())
    secondPlayerBoard.printBoard()

    while len(listSecondPlayerPieces) > 0:

        validInput = False

        print(listSecondPlayerPieces)
        while validInput == False:
            whichShip = input("Choose the ship type: ")
            whichRow = input("Choose a row for your ship: ")
            whichCol = input("Choose a column for your ship: ")
            row = int(whichRow)
            col = int(whichCol)

            shipType = str(whichShip)

            if shipType not in listSecondPlayerPieces:
                print("try again")
            else:
                validInput = True

        validPosition = secondPlayerBoard.placeShip(row, col, shipType)
        if validPosition == False:
            print("Cannot place ship here")
            continue
        else:
            secondPlayerBoard.printBoard()
            listSecondPlayerPieces.remove(whichShip)
            rotate = input("Would you like to rotate your ship?").title()
            if rotate == 'Yes':
                rotateValid = secondPlayerBoard.rotateShip(whichShip)
                if rotateValid == True:
                    print(f"{whichShip} Rotated")
                    secondPlayerBoard.printBoard()
                else:
                    print(f"{whichShip} can't be rotated")
            else:
                continue

    return secondPlayerBoard



