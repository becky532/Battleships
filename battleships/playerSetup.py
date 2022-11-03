from gameBack import Board


def firstPlayerSetup():

    print("Player1 Setup")

    firstPlayerBoard = Board()
    firstPlayerBoard.newBoard()
    listFirstPlayerPieces = list(firstPlayerBoard.shipsDict.keys())
    firstPlayerBoard.printBoard()


    while len(listFirstPlayerPieces) > 0:

        validInput = False

        print("")
        whichRow = input("Choose a row for your ship: ")
        whichCol = input("Choose a column for your ship: ")
        print(listFirstPlayerPieces)
        while validInput == False:
            whichShip = input("Choose the ship type: ")


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

    return firstPlayerBoard


def secondPlayerSetup():

    print("Player2 Setup")

    secondPlayerBoard = Board()
    secondPlayerBoard.newBoard()
    listSecondPlayerPieces = list(secondPlayerBoard.shipsDict.keys())
    secondPlayerBoard.printBoard()


    while len(listSecondPlayerPieces) > 0:

        validInput = False

        print("")
        whichRow = input("Choose a row for your ship: ")
        whichCol = input("Choose a column for your ship: ")
        print(listSecondPlayerPieces)
        while validInput == False:
            whichShip = input("Choose the ship type: ")


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

    return secondPlayerBoard


