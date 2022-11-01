import logging


# class Player:
#
#     WHITE = auto()
#     BLACK = auto()
#
#     def opponent(self):
#         if self == Player.WHITE: return Player.BLACK
#         else: return Player.WHITE
class Game:

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

    def createBoard(self):
        self.boardSize = 7
        self.lastIndex = 6

        for row in range(self.boardSize):
            self.board.append([0] * self.boardSize)

    def printBoard(self):

        listRows = [6, 5, 4, 3, 2, 1, 0]

        for row in listRows:
            for column in self.board[row]:
                print(column, end='')
            print()

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

    def remove(self, shipType):
        position = self.shipsDict[shipType]['position']
        for cell in position:
            self.board[cell[0]][cell[1]] = 0

    def place(self, shipType):
        position = self.shipsDict[shipType]['position']
        for cell in position:
            self.board[cell[0]][cell[1]] = 1

    def rotateShip(self, shipType):
        shipPosition = self.shipsDict[shipType]['position']
        rotatingPoint = shipPosition[0]
        shipLength = self.shipsDict[shipType]['length']
        shipOrientation = self.shipsDict[shipType]['orientation']

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

    def __checkRotation(self, length, row, col, orientation, point):

        checkCells = [point]
        for index in range(1, length):
            if orientation == 'horizontal':
                newCell = [row + index, col]
            else:
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


# create a randomized placement of ships

if __name__ == '__main__':
    game = Game()
    game.createBoard()
    game.placeShip(0, 0, 'Submarine')
    game.placeShip(1, 0, 'Destroyer')
    game.placeShip(4, 2, 'Cruiser')
    game.printBoard()

    print(game.shipsDict['Submarine'])
    game.rotateShip('Submarine')
    print(game.shipsDict['Submarine'])
    print(game.board)
    print(game.board)
    game.rotateShip('Cruiser')
    game.printBoard()
