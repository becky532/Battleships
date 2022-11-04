import unittest
from unittest import TestCase
from battleships.gameBack import Board
from battleships.gameMechanicsBackend import Game

class TestGame(TestCase):
    def test_gameOver(self):
        board = Board.instance()
        board.initialise()
        board.firstPlayerDict['Destroyer']['position'] = ['X', [6, 4]]
        board.firstPlayer = [['X', 'X', 'X', 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0],
                           ['X', 'X', 'X', 'X', 0, 0, 0],
                           [0, 0, 'X', 'X', 'X', 0, 0],
                           [0, 0, 0, 0, 0, 0, 0],
                           [0, 'X', 'X', 'X', 'X', 'X', 0],
                           [0, 0, 0, 'X', 5, 0, 0]]
        game = Game(board)
        game.currentPlayer = 2
        validHit, hit, shipHit, shipSunk = game.fire(6, 4)
        gameOver = game.checkGameOver()

        assert validHit == True
        assert hit == True
        assert shipHit == 'Destroyer'
        assert shipSunk == True
        assert gameOver == True
        assert game.currentPlayer == 2

    def test_fire(self):
        board = Board.instance()
        board.initialise()
        game = Game(board)
        game.currentPlayer = 2
        board.placeShip(0, 0, 'Carrier', 0)
        board.placeShip(1, 0, 'Battleship', 0)
        board.placeShip(2, 0, 'Cruiser', 0)
        board.placeShip(3, 0, 'Submarine', 0)
        board.placeShip(4, 0, 'Destroyer', 0)
        game.fire(0, 0)
        game.currentPlayer = 2
        game.fire(6, 6)

        assert board.firstPlayer[0][0] == 'X'
        assert board.firstPlayerDict['Carrier']['position'][0] == 'X'
        assert board.firstPlayer[6][6] == '.'

if __name__ == '__main__':
    unittest.main()