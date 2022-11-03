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
        self.shipsDict = {'Carrier': {'length': 5, 'position': [], 'orientation': '', 'value': 1},
                          'Battleship': {'length': 4, 'position': [], 'orientation': '', 'value': 2},
                          'Cruiser': {'length': 3, 'position': [], 'orientation': '', 'value': 3},
                          'Submarine': {'length': 3, 'position': [], 'orientation': '', 'value': 4},
                          'Destroyer': {'length': 2, 'position': [], 'orientation': '', 'value': 5}
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

    def validateInitialPlacement(self, length, row, col, player):

        board = self.checkBoard(player)[0]

        placementValid = True
        if col + length - 1 <= self.lastIndex:
            for colInd in range(col, col + length):
                if board[row][colInd] != 0:
                    placementValid = False
                    break
        else:
            logging.info("Ship too long to place here")
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

        if row <= self.lastIndex and col <= self.lastIndex:
            shipLength = shipDict[shipType]['length']
            placementValid = self.validateInitialPlacement(shipLength, row, col, player)

            if placementValid == True:
                logging.info(f'Valid placement of {shipType}')
                shipLength = shipDict[shipType]["length"]

                for cellCol in range(col, col + shipLength):
                    shipDict[shipType]['position'].append([row, cellCol])

                self.place(shipType, player)
                shipDict[shipType]['orientation'] = 'horizontal'
            else:
                logging.info(f'Invalid placement of {shipType}')

        else:
            logging.info("Invalid square chosen")
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
            logging.info(f"Ship {shipType} could not be rotated")
            rotationValid = False

        return rotationValid

    def __checkRotation(self, length, row, col, orientation, point, player):

        board = self.checkBoard(player)[0]

        checkCells = [point]
        for index in range(1, length):
            if orientation == 'horizontal':
                newCell = [row + index, col]
            elif orientation == 'vertical':
                newCell = [row, col + index]

            if newCell[0] <= self.lastIndex and newCell[1] <= self.lastIndex:

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
        logging.info(f"Piece {shipType} has been rotated")

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



    def checkHit(self, row, col, player):

        board = self.checkBoard(player)[0]

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

        board = self.checkBoard(player)[0]
        shipDict = self.checkBoard(player)[1]

        cell = shipDict[ship]['position'].index([row, col])
        shipDict[ship]['position'][cell] = 'X'
        board[row][col] = 'X'

    def checkSunk(self, shipType, player):

        shipDict = self.checkBoard(player)[1]

        shipSunk = False
        if shipType is not None:
            ship = shipDict[shipType]
            position = ship['position']
            length = ship['length']

            if position == ['X']*length:
                shipSunk = True

        return shipSunk

    def checkDefeated(self, player):

        board = self.checkBoard(player)[0]

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

    def listAttacks(self, row, col, player):
        listChosenCells = self.checkBoard(player)[2]
        listChosenCells.append([row, col])

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
        board = self.checkBoard(player)[0]
        if board[row][col] == '.' or board[row][col] == 'X':
            alreadyHit = True
        else:
            alreadyHit = False

        return alreadyHit



if __name__ == '__main__':
    pass


    # board = Board.instance()
    # board.initialise()
    # list = board.randomiseBoard(0)
    # print(list)
    # board.printBoard(0)