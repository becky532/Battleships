import random

from battleships.gameBack import Board

class Game:
    def __init__(self, board: Board):

        self.currentPlayer = 0
        self.board = board

    def switchPlayer(self):
        if self.currentPlayer == 0:
            self.currentPlayer = 1
        else:
            self.currentPlayer = 0

    def fire(self, row, col, playerId):
        hit = False
        shipHit = False
        shipSunk = False
        gameOver = False

        if 0 <= row <= 6 and 0 <= col <= 6:
            validHit = True
            if self.currentPlayer == 0 and self.currentPlayer == playerId:

                hit, shipHit = self.board.checkHit(row, col, 0)
                shipSunk = self.board.checkSunk(shipHit, 0)
                gameOver = self.board.checkDefeated(0)

            elif self.currentPlayer == 1 and self.currentPlayer == playerId:
                hit, shipHit = self.board.checkHit(row, col, 1)
                shipSunk = self.board.checkSunk(shipHit, 1)
                gameOver = self.board.checkDefeated(1)
            else:
                return None

            if gameOver == False:
                self.switchPlayer()
        else:
            validHit = False

        return validHit, hit, shipHit, shipSunk, gameOver
    def showPlayerBoard(self):
        if self.currentPlayer == 0:
            self.board.printBoard(0)
        else:
            self.board.printBoard(1)

    def checkGameOver(self):
        if self.currentPlayer == 1:
            gameOver = self.board.checkDefeated(1)
        else:
            gameOver = self.board.checkDefeated(0)

        return gameOver

if __name__ == '__main__':
    pass
