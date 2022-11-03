from gameBack import Board


def playerSetup(player):

    print("Player1 Setup")
    board = Board.instance()
    board.initialise()
    if player == '1':
        listPlayerPieces = list(board.firstPlayerDict.keys())
    else:
        listPlayerPieces = list(board.secondPlayerDict.keys())
    board.printBoard(player)

    while len(listPlayerPieces) > 0:

        validInput = False

        print("")
        whichRow = input("Choose a row for your ship: ")
        whichCol = input("Choose a column for your ship: ")
        print(listPlayerPieces)
        while validInput == False:
            whichShip = input("Choose the ship type: ")

            row = int(whichRow)
            col = int(whichCol)
            shipType = str(whichShip)

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

    return board


# def secondPlayerSetup():
#
#     print("Player2 Setup")
#
#     secondPlayerBoard = Board()
#     secondPlayerBoard.newBoard()
#     listSecondPlayerPieces = list(secondPlayerBoard.shipsDict.keys())
#     secondPlayerBoard.printBoard()
#
#
#     while len(listSecondPlayerPieces) > 0:
#
#         validInput = False
#
#         print("")
#         whichRow = input("Choose a row for your ship: ")
#         whichCol = input("Choose a column for your ship: ")
#         print(listSecondPlayerPieces)
#         while validInput == False:
#             whichShip = input("Choose the ship type: ")
#
#
#             row = int(whichRow)
#             col = int(whichCol)
#             shipType = str(whichShip)
#
#             if shipType not in listSecondPlayerPieces:
#                 print("try again")
#             else:
#                 validInput = True
#
#
#
#         validPosition = secondPlayerBoard.placeShip(row, col, shipType)
#         if validPosition == False:
#             print("Cannot place ship here")
#             continue
#         else:
#             secondPlayerBoard.printBoard()
#             listSecondPlayerPieces.remove(whichShip)
#
#     return secondPlayerBoard


