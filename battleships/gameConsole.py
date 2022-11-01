from gameBack import Game

game = Game()
game.createBoard()

game.placeShip(1, 1, 'Carrier')
print(game.shipsDict['Carrier'])
game.placeShip(0, 1, 'Battleship')
print(game.board)
game.rotateShip('Carrier')
print(game.shipsDict['Carrier'])

def checkRotation(self, length, row, col, orientation, point):

    checkCells = [point]
    for index in range(1, length):
        if orientation == 'horizontal':
            newCell = [row + index, col]
        else:
            newCell = [row, col + index]
        if self.board[newCell[0]][newCell[1]] == 0 and newCell[0] <= self.lastIndex:
            checkCells.append(newCell)
        else:
            break
    return