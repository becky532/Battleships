from battleships.gameBack import Board

class Game:
    def __init__(self, board: Board):

        self.currentPlayer = 1
        self.board = board

    def switchPlayer(self):
        if self.currentPlayer == 1:
            self.currentPlayer = 2
        else:
            self.currentPlayer = 1

    def fire(self, row, col):
        hit = None
        shipHit = None
        shipSunk = None

        if row <= 6 and col <= 6:
            validHit = True
            if self.currentPlayer == 1:

                hit, shipHit = self.board.checkHit(row, col, 1)
                shipSunk = self.board.checkSunk(shipHit, 1)
                gameOver = self.board.checkDefeated(1)


            else:
                hit, shipHit = self.board.checkHit(row, col, 0)
                shipSunk = self.board.checkSunk(shipHit, 0)
                gameOver = self.board.checkDefeated(0)


            if gameOver == False:
                self.switchPlayer()
        else:
            validHit = False

        return validHit, hit, shipHit, shipSunk
    def showPlayerBoard(self):
        if self.currentPlayer == 1:
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
