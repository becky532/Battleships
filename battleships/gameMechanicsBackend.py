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

        if self.currentPlayer == self.firstPlayer:
            #if cell not alread chosen then try otherwise return already used
            hit, shipHit = self.secondPlayer.findSquare(row, col)
            # in console if hit is True, then replace with an x or if hit is false replace with a .
            #if ship now destroyed then return shipSunk
        else:
            hit, shipHit = self.firstPlayer.findSquare(row, col)

        return hit, shipHit


if __name__ == '__main__':
    firstBoard = Board()
    secondBoard = Board()
    secondBoard.placeShip(0, 0, 'Carrier')
    secondBoard.placeShip(1, 0, 'Destroyer')
    secondBoard.placeShip(2, 0, 'Submarine')
    secondBoard.placeShip(3, 0, 'Battleship')
    secondBoard.placeShip(4, 0, 'Cruiser')

    game = Game(firstBoard, secondBoard)
    game.secondPlayer.printBoard()

    noHit, ship = game.fire(0, 0)
    print(noHit)
    print(ship)
    game.secondPlayer.printBoard()



