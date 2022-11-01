class Ship:
    def __init__(self):
        self.col = []
        self.row = []

class Game:

    def __init__(self):
        self.board = []
        self.shipsDict = {'Carrier': {'length': 5, 'position': [], 'orientation': ''},
                            'Battleship': {'length': 4, 'position': [], 'orientation': ''},
                            'Cruiser': {'length': 3, 'position': [], 'orientation': ''},
                            'Submarine': {'length': 3, 'position': [], 'orientation': ''},
                            'Destroyer': {'length': 2, 'position': [], 'orientation': ''}
                            }

    def createBoard(self):
        self.boardSize = 7
        for row in range(self.boardSize):
            self.board.append([0]*self.boardSize)

    def validatePlacement(self, length, row, col):
        placementValid = True
        if col + length + 1 <= self.boardSize:
            for rowInd in range(row, length + 1):
                if self.board[row][rowInd] == 1:
                    print("Invalid placement")
                    placementValid = False
                    break
        else:
            print("Ship too long to place here")
            placementValid = False
        return placementValid

    def placeShip(self, row, col, shipType): ### starting at 0,0
        shipLength = self.shipsDict[shipType]["length"]
        placementValid = self. validatePlacement(shipLength, row, col)
        if placementValid == True:
                print('Valid placement')
                for cellCol in range(col, shipLength + 1):
                    self.board[row][cellCol] = 1
                    self.shipsDict[shipType]['position'].append([row, cellCol])
                self.shipsDict[shipType]['orientation'] = 'horizontal'

    def rotateShip(self, shipType):
        shipPosition = self.shipsDict[shipType]['position']
        shipLength = self.shipsDict[shipType]['length']
        shipOrientation = self.shipsDict[shipType]['orientation']
        if shipOrientation == 'horizontal':
            shipCol = shipPosition[0][1]
            checkCells = [shipPosition[0]]
            for cell in range(1, shipLength):
                checkCells.append([self.shipsDict[shipType]['position'][cell][1], shipCol])
            positionValid = self.validatePlacement(shipLength, checkCells[0], checkCells[1])
            if positionValid == True:
                for position in range(1, shipLength):
                    self.shipsDict[shipType]['position'][position][0] = self.shipsDict[shipType]['position'][cell][1]
                    self.shipsDict[shipType]['position'][position][1] = shipCol
                    self.shipsDict[shipType]['orientation'] = 'vertical'

                #validate cells
                #remove 1 from horizontal and add to new cells

# rotate ship once placed on board, clear a piece off of the board, create a randomized placement of ships

if __name__ == '__main__':
    game = Game()
    game.createBoard()
    game.placeShip(1, 1, 'Carrier')
    print(game.shipsDict['Carrier'])
    game.placeShip(0, 1, 'Battleship')
    # print(game.board)
    game.rotateShip('Carrier')
    print(game.shipsDict['Carrier'])





