import unittest
from unittest import TestCase
from battleships.gameBack import Board

class TestBoard(TestCase):

    def test_randomiseBoard(self):
        board = Board.instance()
        board.initialise()
        board.randomiseBoard(0)
        listCells =[]
        for i in range(7):
            for j in range(7):
                listCells.append(board.firstPlayer[i][j])

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

    def test_placePiece(self):
        board = Board.instance()
        board.initialise()
        board.placeShip(0, 2, 'Carrier', 0)
        board.placeShip(0, 1, 'Destroyer', 0)

        assert board.firstPlayerDict['Carrier']['position'] == [[0, 2], [0, 3], [0, 4], [0, 5], [0, 6]]
        assert board.firstPlayer[0][6] == 1
        assert board.firstPlayer[0][1] == 0

    def test_rotateShip(self):
        board = Board.instance()
        board.initialise()
        board.placeShip(6, 0, 'Carrier', 0)
        board.rotateShip('Carrier', 0)
        board.placeShip(0, 0, 'Battleship', 0)
        board.rotateShip('Battleship', 0)

        assert board.firstPlayerDict['Carrier']['position'] == [[6, 0], [5, 0], [4, 0], [3, 0], [2, 0]]
        assert board.firstPlayer[4][0] == 1
        assert board.firstPlayer[0][3] == 2

    def test_allPiecesDown(self):
        board = Board.instance()
        board.initialise()
        board.randomiseBoard(0)
        complete = board.checkAllPiecesPlaced(0)
        board.placeShip(0, 0, 'Carrier', 1)
        complete2 = board.checkAllPiecesPlaced(1)

        assert complete == True
        assert complete2 == False

    def test_duplicateAttack(self):
        board = Board.instance()
        board.initialise()
        board.placeShip(0, 0, 'Carrier', 0)
        board.firstPlayer[0][0] = 'X'
        board.firstPlayer[1][0] = '.'
        attack1 = board.checkDuplicateAttack(0, 0, 1)
        attack2 = board.checkDuplicateAttack(1, 0, 1)
        attack3 = board.checkDuplicateAttack(0, 1, 1)

        assert attack1 == True
        assert attack2 == True
        assert attack3 == False







if __name__ == '__main__':
    unittest.main()