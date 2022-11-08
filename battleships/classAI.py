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
        logging.basicConfig(filename='battleships.log', level=logging.INFO, filemode='w', force=True)
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

        return guessRow, guessCol

    def removeShipAsTarget(self, shipSunk):
        del self.targets[shipSunk]
        self.destroyed[shipSunk] = True

    def AISmartAttackMoves(self):
        listShips = list(self.targets.keys())

        cellsHit = {}
        for ship in listShips:
            cellsHit[ship] = len(self.targets[ship])

        shipToAttack = max(cellsHit, key=cellsHit.get)
        possibleMoves = []

        if len(self.targets[shipToAttack]) == 1:
            hitCells = self.targets[shipToAttack]
            hitRow = hitCells[0][0]
            hitCol = hitCells[0][1]
            if hitRow != 0:
                possibleMoves.append([hitRow - 1, hitCol])
            if hitRow != 6:
                possibleMoves.append([hitRow + 1, hitCol])
            if hitCol != 0:
                possibleMoves.append([hitRow, hitCol - 1])
            if hitCol != 6:
                possibleMoves.append([hitRow, hitCol + 1])

        elif len(self.targets[shipToAttack]) > 1:
            hitCells = self.targets[shipToAttack]
            hitRows = []
            hitCols = []

            for cell in hitCells:
                hitRows.append(cell[0])
                hitCols.append(cell[1])

            if len(hitCols) == len(set(hitCols)):
                orientation = 'horizontal'
                logging.info(f"{shipToAttack} identified as horizontal")
            else:
                orientation = 'vertical'
                logging.info(f"{shipToAttack} identified as vertical")

            if orientation == 'horizontal':
                minCol = min(hitCols)
                maxCol = max(hitCols)
                row = hitCells[0][0]

                if minCol != 0:
                    possibleMoves.append([row, minCol - 1])
                if maxCol != 6:
                    possibleMoves.append([row, maxCol + 1])
            else:
                minRow = min(hitRows)
                maxRow = max(hitRows)
                col = hitCells[0][1]

                if minRow != 0:
                    possibleMoves.append([minRow - 1, col])
                if maxRow != 6:
                    possibleMoves.append([maxRow + 1, col])

        else:
            possibleMoves = None


        return possibleMoves

    def decideAttack(self):
        #if a is True and the ship is not destroyed then do a smart attack
        a = any(self.targets.values())
        if a == True:
            possibleMoves = self.AISmartAttackMoves()
            logging.info(f"Computer's possible moves were:'{possibleMoves}")
            move = random.choice(possibleMoves)

        else:
            move = self.AIRandomAttackMoves()

        return move



if __name__ == '__main__':
    board = Board.instance()
    board.initialise()
    game = Game(board)
    AI = AI.instance() ##player ID for AI is 1 (player 2)
    AI.initialise()
    moves = AI.decideAttack()
    print(moves)







