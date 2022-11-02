from gameBack import Board

firstPlayerBoard = Board()
secondPlayerBoard = Board()

firstPlayerBoard.newBoard()
whichPiece = input('What piece would you like to put down?')

if whichPiece == 'Random':
    firstPlayerBoard.randomiseBoard()

# secondPlayerBoard.newBoard()
# secondPlayerBoard.placeShip(2, 1, 'Destroyer')
#
firstPlayerBoard.printBoard()
# print()
# secondPlayerBoard.printBoard()

