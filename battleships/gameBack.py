class Ship:
    def __init__(self):
        self.col = []
        self.row = []

class Game:

    def __init__(self):
        self.board = []
        self.shipsDict = {'Carrier': {'length': 5, 'position': []},
                            'Battleship': {'length': 4, 'position': []},
                            'Cruiser': {'length': 3, 'position': []},
                            'Submarine': {'length': 3, 'position': []},
                            'Destroyer': {'length': 2, 'position': []}
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

    def rotateShip(self, shipType):
        shipPosition = self.shipsDict[shipType]['position']
        shipLength = self.shipsDict[shipType]['length']
        shipCol = shipPosition[0][1]
        for cell in range(1, shipLength):
            self.shipsDict[shipType]['position'][cell][0] = self.shipsDict[shipType]['position'][cell][1]
            self.shipsDict[shipType]['position'][cell][1] = shipCol

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





