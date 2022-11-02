import unittest
from unittest import TestCase
from battleships.gameBack import Board

class TestBoard(TestCase):

    def test_randomiseBoard(self):
        board = Board()
        board.randomiseBoard()
        listCells =[]
        for i in range(7):
            for j in range(7):
                listCells.append(board.board[i][j])

        totalCarrier = listCells.count(1)
        totalBattleship = listCells.count(2)
        totalCruiser = listCells.count(3)
        totalSubmarine = listCells.count(4)
        totalDestroyer = listCells.count(5)

        assert totalCarrier == 5
        assert totalBattleship == 4
        assert totalCruiser == 3
        assert totalSubmarine == 3
        assert totalDestroyer == 2


if __name__ == '__main__':
    unittest.main()