import unittest
from unittest import TestCase
from battleships.gameBack import Board
from battleships.gameMechanicsBackend import Game

class TestGame(TestCase):
    def test_gameOver(self):
        firstPlayer = Board()
        secondPlayer = Board()
        secondPlayer.shipsDict['Destroyer']['position'] = ['X', [6, 4]]
        secondPlayer.board = [['X', 'X', 'X', 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0],
                           ['X', 'X', 'X', 'X', 0, 0, 0],
                           [0, 0, 'X', 'X', 'X', 0, 0],
                           [0, 0, 0, 0, 0, 0, 0],
                           [0, 'X', 'X', 'X', 'X', 'X', 0],
                           [0, 0, 0, 'X', 5, 0, 0]]
        game = Game(firstPlayer, secondPlayer)
        game.currentPlayer = firstPlayer
        validHit, hit, shipHit, shipSunk = game.fire(6, 4)
        gameOver = game.checkGameOver()

        assert validHit == True
        assert hit == True
        assert shipHit == 'Destroyer'
        assert shipSunk == True
        assert gameOver == True
        assert game.currentPlayer == firstPlayer





if __name__ == '__main__':
    unittest.main()