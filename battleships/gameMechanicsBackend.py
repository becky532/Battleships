from gameBack import Board
from enum import Enum, auto

# class Player(Enum):
#
#     firstPlayer = auto()
#     secondPlayer = auto()
#
#     def opponent(self):
#         if self == Player.firstPlayer: return Player.secondPlayer
#         else: return Player.firstPlayer

class Game:
    def __init__(self, board1: Board, board2: Board):
        self.firstPlayer = board1
        self.secondPlayer = board2
        self.currentPlayer = self.firstPlayer

    def switchPlayer(self):
        if self.currentPlayer == self.firstPlayer:
            self.currentPlayer = self.secondPlayer
        else:
            self.currentPlayer = self.secondPlayer

    def fire(self, row, col):
        hit = None
        shipHit = None
        shipSunk = None

        if row <= 6 and col <= 6:
            validHit = True
            if self.currentPlayer == self.firstPlayer:

                hit, shipHit = self.secondPlayer.checkHit(row, col)
                shipSunk = self.secondPlayer.checkSunk(shipHit)

            else:
                hit, shipHit = self.firstPlayer.checkHit(row, col)
                shipSunk = self.firstPlayer.checkSunk(shipHit)

            self.switchPlayer()
        else:
            validHit = False

        return validHit, hit, shipHit, shipSunk
    def showPlayerBoard(self):
        if self.currentPlayer == self.firstPlayer:
            self.firstPlayer.printBoard()
        else:
            self.secondPlayer.printBoard()

    # def checkGameOver(self):
    #



if __name__ == '__main__':
    pass
