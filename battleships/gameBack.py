import logging
import random

class Board:

    _instance = None
    def __init__(self):
        raise RuntimeError('Call instance() instead')
    @classmethod
    def instance(cls):
        if cls._instance is None:
            logging.basicConfig(filename='battleships.log', level=logging.INFO, filemode='w', force=True)
            logging.info('Creating new instance')
            cls._instance = cls.__new__(cls)
            cls._instance.initialise()
        return cls._instance

    def initialise(self):
        self.emptyBoard = [[0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0]]

        self.boardSize = 7
        self.lastIndex = 6
        self.firstPlayer = self.newBoard()
        self.secondPlayer = self.newBoard()
        self.listChosenCells = []
        self.firstPlayerDict = self.newShipDict()
        self.secondPlayerDict = self.newShipDict()
        self.firstPlayerList = []
        self.secondPlayerList = []

    def newBoard(self):

        self.board = [[0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0]]
        return self.board

    def newShipDict(self):
        self.shipsDict = {'Carrier': {'length': 5, 'position': [], 'orientation': 'horizontal', 'value': 1},
                          'Battleship': {'length': 4, 'position': [], 'orientation': 'horizontal', 'value': 2},
                          'Cruiser': {'length': 3, 'position': [], 'orientation': 'horizontal', 'value': 3},
                          'Submarine': {'length': 3, 'position': [], 'orientation': 'horizontal', 'value': 4},
                          'Destroyer': {'length': 2, 'position': [], 'orientation': 'horizontal', 'value': 5}
                          }
        return self.shipsDict
    def printBoard(self, player):

        board = self.checkBoard(player)[0]

        listRows = [6, 5, 4, 3, 2, 1, 0]

        for row in listRows:
            print(str(row) + '--', end='')
            for column in board[row]:
                print(str(column) + ' ', end='')
            print()
        print('   ' + '|', '|', '|', '|', '|', '|', '|')
        print('   ', end='')

        for i in range(7):
            print(str(i) + ' ', end='')
        print()

    def validateInitialPlacement(self, length, row, col, orientation, player):

        board = self.checkBoard(player)[0]
        placementValid = True
        if orientation == 'horizontal':
            endCol = col + (length - 1)
            if endCol <= self.lastIndex:
                for colInd in range(col, col + length):
                    if board[row][colInd] != 0:
                        placementValid = False
                        break
            else:
                placementValid = False

        elif orientation == 'vertical':
            endRow = row - (length - 1)
            if endRow >= 0:
                for rowInd in range(row, row-length, -1):
                    if board[rowInd][col] != 0:
                        placementValid = False
                        break
        else:
            placementValid = False

        return placementValid


    def checkBoard(self, player):

        if player == 0:
            board = self.firstPlayer
            shipDict = self.firstPlayerDict
            chosenCells = self.firstPlayerList
        else:
            board = self.secondPlayer
            shipDict = self.secondPlayerDict
            chosenCells = self.secondPlayerList

        return [board, shipDict, chosenCells]

    def placeShip(self, row, col, shipType, player):

        shipDict = self.checkBoard(player)[1]

        if 0 <= row <= self.lastIndex and 0 <= col <= self.lastIndex:
            shipLength = shipDict[shipType]['length']
            orientation = shipDict[shipType]['orientation']
            placementValid = self.validateInitialPlacement(shipLength, row, col, orientation, player)
            shipDict[shipType]['position'] = []

            if placementValid == True and orientation == 'horizontal':

                for cellCol in range(col, col + shipLength):
                    shipDict[shipType]['position'].append([row, cellCol])
                    self.place(shipType, player)

            elif placementValid == True and orientation == 'vertical':
                for cellRow in range(row - shipLength + 1, row + 1):
                    shipDict[shipType]['position'].append([cellRow, col])
                    self.place(shipType, player)
        else:

            placementValid = False

        return placementValid

    def remove(self, shipType, player):
        board = self.checkBoard(player)[0]
        shipDict = self.checkBoard(player)[1]

        position = shipDict[shipType]['position']
        for cell in position:
            board[cell[0]][cell[1]] = 0
        shipDict[shipType]['position'] = []

    def place(self, shipType, player):

        board = self.checkBoard(player)[0]
        shipDict = self.checkBoard(player)[1]

        position = shipDict[shipType]['position']
        value = shipDict[shipType]['value']

        for cell in position:
            board[cell[0]][cell[1]] = value

    def clearBoard(self, player):

        board = self.checkBoard(player)[0]
        shipDict = self.checkBoard(player)[1]

        for i in range(7):
            for j in range(7):
                board[i][j] = 0

        for ship in shipDict:
            shipDict[ship]['position'] = []
            shipDict[ship]['orientation'] = 'horizontal'

    def rotateShip(self, shipType, player):

        shipDict = self.checkBoard(player)[1]

        shipPosition = shipDict[shipType]['position']
        rotatingPoint = shipPosition[0]
        shipLength = shipDict[shipType]['length']
        shipOrientation = shipDict[shipType]['orientation']
        rotationValid = True

        shipCol = shipPosition[0][1]
        shipRow = shipPosition[0][0]

        checkCells = self.__checkRotation(shipLength, shipRow, shipCol, shipOrientation, rotatingPoint, player)

        if shipOrientation == 'horizontal' and len(checkCells) == shipLength:

            self.__rotate(shipType, checkCells, player)
            shipDict[shipType]['orientation'] = 'vertical'

        elif shipOrientation == 'vertical' and len(checkCells) == shipLength:

            self.__rotate(shipType, checkCells, player)
            shipDict[shipType]['orientation'] = 'horizontal'
        else:

            rotationValid = False

        return rotationValid, shipDict[shipType]['orientation']

    def __checkRotation(self, length, row, col, orientation, point, player):

        board = self.checkBoard(player)[0]

        checkCells = [point]
        for index in range(1, length):
            if orientation == 'horizontal':
                newCell = [row - index, col]
            elif orientation == 'vertical':
                newCell = [row, col + index]

            if 0 <= newCell[0] <= self.lastIndex and 0 <= newCell[1] <= self.lastIndex:

                if board[newCell[0]][newCell[1]] == 0:
                    checkCells.append(newCell)
                else:
                    break
            else:
                break

        return checkCells


    def __rotate(self, shipType, newPosition, player):

        shipDict = self.checkBoard(player)[1]

        self.remove(shipType, player)
        shipDict[shipType]['position'] = newPosition
        self.place(shipType, player)
        shipDict[shipType]['orientation'] = 'vertical'

    def randomiseBoard(self, player):

        board = self.checkBoard(player)[0]
        shipDict = self.checkBoard(player)[1]

        if board != self.emptyBoard:
            self.clearBoard(player)

        listShip = list(shipDict.keys())
        random.shuffle(listShip)
        for ship in listShip:
            shipPlace = False
            while shipPlace == False:
                row = random.randint(0, 6)
                col = random.randint(0, 6)
                shipPlace = self.placeShip(row, col, ship, player)
            rotate = random.randint(0, 1)
            if rotate == 1:
                self.rotateShip(ship, player)

    def checkOpponentBoard(self, player):
        if player == 0:
            board = self.secondPlayer
            shipDict = self.secondPlayerDict
            chosenCells = self.secondPlayerList
        else:
            board = self.firstPlayer
            shipDict = self.firstPlayerDict
            chosenCells = self.firstPlayerList

        return [board, shipDict, chosenCells]

    def checkHit(self, row, col, player):

        board = self.checkOpponentBoard(player)[0]

        if row <= self.lastIndex and col <= self.lastIndex:
            value = board[row][col]
            hit = True

            if value == 0:
                hit = False
                shipHit = None
                board[row][col] = '.'
            elif value == 1:
                shipHit = 'Carrier'
                self.knockOutCell(shipHit, row, col, player)
            elif value == 2:
                shipHit = 'Battleship'
                self.knockOutCell(shipHit, row, col, player)

            elif value == 3:
                shipHit = 'Cruiser'
                self.knockOutCell(shipHit, row, col, player)
            elif value == 4:
                shipHit = 'Submarine'
                self.knockOutCell(shipHit, row, col, player)
            else:
                shipHit = 'Destroyer'
                self.knockOutCell(shipHit, row, col, player)

            return hit, shipHit

    def knockOutCell(self, ship, row, col, player):

        board = self.checkOpponentBoard(player)[0]
        shipDict = self.checkOpponentBoard(player)[1]

        cell = shipDict[ship]['position'].index([row, col])
        shipDict[ship]['position'][cell] = 'X'
        board[row][col] = 'X'

    def checkSunk(self, shipType, player):

        shipDict = self.checkOpponentBoard(player)[1]

        shipSunk = False
        if shipType is not None:
            ship = shipDict[shipType]
            position = ship['position']
            length = ship['length']

            if position == ['X']*length:
                shipSunk = True

        return shipSunk

    def checkDefeated(self, player):

        board = self.checkOpponentBoard(player)[0]

        listCells = []
        for i in range(7):
            for j in range(7):
                listCells.append(board[i][j])
        allShipsDestroyed = listCells.count('X')
        if allShipsDestroyed == 17:
            gameOver = True
        else:
            gameOver = False

        return gameOver

    def checkAllPiecesPlaced(self, player):
        board = self.checkBoard(player)[0]
        countCarrier = 0
        countBattleship = 0
        countCruiser = 0
        countSubmarine = 0
        countDestroyer = 0

        for row in board:
            countCarrier += row.count(1)
            countBattleship += row.count(2)
            countCruiser += row.count(3)
            countSubmarine += row.count(4)
            countDestroyer += row.count(5)

        if countCarrier == 5 and countBattleship == 4 and countCruiser == 3 and countSubmarine == 3 and countDestroyer == 2:
            boardFilled = True
        else:
            boardFilled = False

        return boardFilled

    def checkDuplicateAttack(self, row, col, player):

        board = self.checkOpponentBoard(player)[0]

        if row <= self.lastIndex and col <= self.lastIndex:
            if board[row][col] == '.' or board[row][col] == 'X':
                alreadyHit = True
            else:
                alreadyHit = False
        else:
            alreadyHit = None

        return alreadyHit

if __name__ == '__main__':
    board = Board.instance()
    board.initialise()
    board.placeShip(0, 0, 'Carrier', 0)
    board.rotateShip('Carrier', 0)
    board.printBoard(0)
    board.placeShip(6, 0, 'Cruiser', 0)
    board.rotateShip('Cruiser', 0)
    board.printBoard(0)

