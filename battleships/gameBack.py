import logging
import random


# class Player:
#
#     first
#     def opponent(self):
#         if self == Player.firstPlayer:
#             return Player.secondPlayer
#         else:
#             return Player.WHITE
class Board:

    def __init__(self):
        self.board = []
        self.shipsDict = {'Carrier': {'length': 5, 'position': [], 'orientation': ''},
                          'Battleship': {'length': 4, 'position': [], 'orientation': ''},
                          'Cruiser': {'length': 3, 'position': [], 'orientation': ''},
                          'Submarine': {'length': 3, 'position': [], 'orientation': ''},
                          'Destroyer': {'length': 2, 'position': [], 'orientation': ''}
                          }
        self.player = 1
        logging.basicConfig(filename='battleships.log', level=logging.INFO, filemode='w', force=True)
        self.boardSize = 7
        self.lastIndex = 6

    def newBoard(self):

        self.board = [[0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0]]


    def printBoard(self):

        listRows = [6, 5, 4, 3, 2, 1, 0]

        for row in listRows:
            print(str(row) + '--', end='')
            for column in self.board[row]:
                print(str(column) + ' ', end='')
            print()
        print('   ' + '|', '|', '|', '|', '|', '|', '|')
        print('   ', end='')

        for i in range(7):
            print(str(i) + ' ', end='')

    def validateInitialPlacement(self, length, row, col):

        placementValid = True
        if col + length <= self.lastIndex:
            for colInd in range(col, col + length):
                if self.board[row][colInd] == 1:
                    placementValid = False
                    break
        else:
            logging.info("Ship too long to place here")
            placementValid = False

        return placementValid

    def placeShip(self, row, col, shipType):
        #could be less than 0

        if row <= self.lastIndex and col <= self.lastIndex:
            shipLength = self.shipsDict[shipType]['length']
            placementValid = self.validateInitialPlacement(shipLength, row, col)

            if placementValid == True:
                logging.info(f'Valid placement of {shipType}')
                shipLength = self.shipsDict[shipType]["length"]

                for cellCol in range(col, col + shipLength):
                    self.shipsDict[shipType]['position'].append([row, cellCol])

                self.place(shipType)
                self.shipsDict[shipType]['orientation'] = 'horizontal'
            else:
                logging.info(f'Invalid placement of {shipType}')

        else:
            logging.info("Invalid square chosen")
            placementValid = False

        return placementValid

    def remove(self, shipType):
        position = self.shipsDict[shipType]['position']
        for cell in position:
            self.board[cell[0]][cell[1]] = 0
        self.shipsDict[shipType]['position'] = []

    def place(self, shipType):
        position = self.shipsDict[shipType]['position']
        for cell in position:
            self.board[cell[0]][cell[1]] = 1

    def clearBoard(self):
        self.newBoard()
        for ship in self.shipsDict:
            self.shipsDict[ship]['position'] = []
            self.shipsDict[ship]['orientation'] = 'horizontal'


    def rotateShip(self, shipType):
        shipPosition = self.shipsDict[shipType]['position']
        rotatingPoint = shipPosition[0]
        shipLength = self.shipsDict[shipType]['length']
        shipOrientation = self.shipsDict[shipType]['orientation']
        rotationValid = True

        shipCol = shipPosition[0][1]
        shipRow = shipPosition[0][0]

        checkCells = self.__checkRotation(shipLength, shipRow, shipCol, shipOrientation, rotatingPoint)

        if shipOrientation == 'horizontal' and len(checkCells) == shipLength:

            self.__rotate(shipType, checkCells)
            self.shipsDict[shipType]['orientation'] = 'vertical'
        elif shipOrientation == 'vertical' and len(checkCells == shipLength):

            self.__rotate(shipType, checkCells)
            self.shipsDict[shipType]['orientation'] = 'horizontal'
        else:
            logging.info(f"Ship {shipType} could not be rotated")
            rotationValid = False

        return rotationValid

    def __checkRotation(self, length, row, col, orientation, point):

        checkCells = [point]
        for index in range(1, length):
            if orientation == 'horizontal':
                newCell = [row + index, col]
            elif orientation == 'vertical':
                newCell = [row, col + index]

            if newCell[0] <= self.lastIndex and newCell[1] <= self.lastIndex:

                if self.board[newCell[0]][newCell[1]] == 0:
                    checkCells.append(newCell)
                else:
                    break
            else:
                break

        return checkCells

    def __rotate(self, shipType, newPosition):
        self.remove(shipType)
        self.shipsDict[shipType]['position'] = newPosition
        self.place(shipType)
        self.shipsDict[shipType]['orientation'] = 'vertical'
        logging.info(f"Piece {shipType} has been rotated")

    def randomiseBoard(self):
        listShip = list(self.shipsDict.keys())
        random.shuffle(listShip)
        for ship in listShip:
            shipPlace = False
            while shipPlace == False:
                row = random.randint(0, 6)
                col = random.randint(0, 6)
                shipPlace = self.placeShip(row, col, ship)
            rotate = random.randint(0, 1)
            if rotate == 1:
                self.rotateShip(ship)


        return listShip

if __name__ == '__main__':

    board = Board()
    board.newBoard()
    # board.placeShip(0, 0, 'Carrier')
    # board.placeShip(1, 0, 'Battleship')
    # board.printBoard()
    # board.clearBoard()
    # board.printBoard()
    board.randomiseBoard()
    board.printBoard()
    print(board.shipsDict)

