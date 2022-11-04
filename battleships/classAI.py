import random
import logging
from gameMechanicsBackend import Game
from gameBack import Board

class AI:

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
        self.targets = {'Carrier': [],
                        'Battleship': [],
                        'Cruiser': [],
                        'Submarine': [],
                        'Destroyer': []
        }
        self.destroyed = {'Carrier': False,
                          'Battleship': False,
                          'Cruiser': False,
                          'Submarine': False,
                          'Destroyer': False
                          }

        self.playerId = 1

    def AIRandomAttackMoves(self):  ###just return
        guessRow = random.randint(0, 6)
        guessCol = random.randint(0, 6)
        # print([guessRow, guessCol])
        # alreadyHit = True
        # while alreadyHit == True:
        #     alreadyHit = self.board.checkDuplicateAttack(guessRow, guessCol, self.playerId)  ##AI always player 2
        #     attack = self.game.fire(guessRow, guessCol, self.playerId)
        #     hitSuccessful = attack[1]
        #     shipSunk = attack[3]
        #     shipHit = attack[2]
        #     if hitSuccessful == True:
        #         self.targets[shipHit].append([guessRow, guessCol])
        #
        #     if shipSunk == True:
        #         self.destroyed[shipHit] = True

        return guessRow, guessCol

    def AISmartAttackMoves(self):
        listShips = ['Carrier', 'Battleship', 'Cruiser', 'Submarine', 'Destroyer']
        for ship in listShips:
            if self.destroyed[ship] == True:
                listShips.remove(ship)
        cellsHit = {}
        for ship in listShips:
            cellsHit[ship] = len(self.targets[ship])

        shipToAttack = max(cellsHit, key=cellsHit.get)
        possibleMoves = []

        if len(self.targets[shipToAttack]) == 1:
            hitCells = self.targets[shipToAttack]
            hitRow = hitCells[0][0]
            hitCol = hitCells[0][1]  ###what if 0 or 6
            possibleMoves.extend([[hitRow, hitCol + 1], [hitRow + 1, hitCol]])

        elif len(self.targets[shipToAttack]) > 1:
            hitCells = self.targets[shipToAttack]
            hitRows = []
            hitCols = []

            for cell in hitCells:
                hitRows.append(cell[0])
                hitCols.append(cell[1])

            if len(hitCols) == len(set(hitCols)):
                orientation = 'horizontal'
            else:
                orientation = 'vertical'

            if orientation == 'horizontal':
                minCol = min(hitCols)
                maxCol = max(hitCols)
                row = hitCells[0][1]

                if minCol != 0:
                    possibleMoves.append([row, minCol - 1])
                if maxCol != 5:
                    possibleMoves.append([row, maxCol + 1])
            else:
                minRow = min(hitRows)
                maxRow = max(hitRows)
                col = hitCells[1][0]

                if minRow != 0:
                    possibleMoves.append([minRow - 1, col])
                if maxRow != 5:
                    possibleMoves.append([maxRow + 1, col])

        else:
            possibleMoves = None

        return possibleMoves

    def decideAttackType(self):
        a = any(self.targets.values())
        if a == True:
            possibleMoves = self.AISmartAttackMoves()
        else:
            possibleMoves = self.AIRandomAttackMoves()

        return possibleMoves



if __name__ == '__main__':
    board = Board.instance()
    board.initialise()
    game = Game(board)
    AI = AI.instance() ##player ID for AI is 1 (player 2)
    AI.initialise()
    moves = AI.decideAttackType()
    print(moves)







