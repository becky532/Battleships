from battleships.gameBack import Board

class Game:
    def __init__(self, board1: Board, board2: Board):
        self.firstPlayer = board1
        self.secondPlayer = board2
        self.currentPlayer = self.firstPlayer

    def switchPlayer(self):
        if self.currentPlayer == self.firstPlayer:
            self.currentPlayer = self.secondPlayer
        else:
            self.currentPlayer = self.firstPlayer

    def fire(self, row, col):
        hit = None
        shipHit = None
        shipSunk = None

        if row <= 6 and col <= 6:
            validHit = True
            if self.currentPlayer == self.firstPlayer:

                hit, shipHit = self.secondPlayer.checkHit(row, col)
                shipSunk = self.secondPlayer.checkSunk(shipHit)
                gameOver = self.secondPlayer.checkDefeated()
                self.firstPlayer.listAttacks(row, col)

            else:
                hit, shipHit = self.firstPlayer.checkHit(row, col)
                shipSunk = self.firstPlayer.checkSunk(shipHit)
                gameOver = self.firstPlayer.checkDefeated()
                self.secondPlayer.listAttacks(row, col)

            if gameOver == False:
                self.switchPlayer()
        else:
            validHit = False

        return validHit, hit, shipHit, shipSunk
    def showPlayerBoard(self):
        if self.currentPlayer == self.firstPlayer:
            self.firstPlayer.printBoard()
        else:
            self.secondPlayer.printBoard()
    def checkGameOver(self):
        if self.currentPlayer == self.firstPlayer:
            gameOver = self.secondPlayer.checkDefeated()
        else:
            gameOver = self.firstPlayer.checkDefeated()

        return gameOver

if __name__ == '__main__':
    pass
