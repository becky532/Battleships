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

    def validatePlacement(self, length, row, col):

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

    def getShipPosition(self, row, col, shipType):  # starting at 0,0
        shipLength = self.shipsDict[shipType]['length']
        placementValid = self.validatePlacement(shipLength, row, col)
        if placementValid == True:
            logging.info(f'Valid placement of {shipType}')
            shipLength = self.shipsDict[shipType]["length"]

            for cellCol in range(col, col + shipLength):
                self.shipsDict[shipType]['position'].append([row, cellCol])

            self.placeShip(shipType)
            self.shipsDict[shipType]['orientation'] = 'horizontal'
        else:
            logging.info(f'Invalid placement of {shipType}')
    def removeShip(self, shipType):
        position = self.shipsDict[shipType]['position']
        for cell in position:
            self.board[cell[0]][cell[1]] = 0
    def placeShip(self, shipType):
        position = self.shipsDict[shipType]['position']
        for cell in position:
            self.board[cell[0]][cell[1]] = 1

    def checkRotateShip(self, shipType):
        shipPosition = self.shipsDict[shipType]['position']
        rotatingPoint = shipPosition[0]
        shipLength = self.shipsDict[shipType]['length']
        shipOrientation = self.shipsDict[shipType]['orientation']

        shipCol = shipPosition[0][1]
        shipRow = shipPosition[0][0]
        checkCells = [rotatingPoint]

        if shipOrientation == 'horizontal':
            for index in range(1, shipLength):
                newCell = [shipRow + index, shipCol]
                if self.board[newCell[0]][newCell[1]] == 0 and newCell[0] <= self.lastIndex:
                    checkCells.append(newCell)
                else:
                    break

            if len(checkCells) == shipLength:
                self.rotate(shipType, checkCells)
                self.shipsDict[shipType]['orientation'] = 'vertical'
            else:
                logging.info(f"Ship {shipType} could not be rotated")

        if shipOrientation == 'vertical':
            for index in range(1, shipLength):
                newCell = [shipRow, shipCol + index]
                if self.board[newCell[0]][newCell[1]] == 0 and newCell[1] <= self.lastIndex:
                    checkCells.append(newCell)
                else:
                    break

            if len(checkCells) == shipLength:
                self.rotate(shipType, checkCells)
                self.shipsDict[shipType]['orientation'] = 'horizontal'
            else:
                logging.info(f"Ship {shipType} could not be rotated")

    def rotate(self, shipType, newPosition):
        self.removeShip(shipType)
        self.shipsDict[shipType]['position'] = newPosition
        self.placeShip(shipType)
        self.shipsDict[shipType]['orientation'] = 'vertical'
        logging.info(f"Piece {shipType} has been rotated")







#create a randomized placement of ships

if __name__ == '__main__':
    game = Game()
    game.createBoard()
    print(game.board)
    game.getShipPosition(0, 0, 'Submarine')
    print(game.shipsDict['Submarine'])
    game.rotateShip('Submarine')
    print(game.shipsDict['Submarine'])
    print(game.board)
