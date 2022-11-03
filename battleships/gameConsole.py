from gameBack import Board
import os

firstPlayerBoard = Board()
secondPlayerBoard = Board()

def menu():
    print("Hello!")
    print("Lets go on an adventure!")
    option = input('''
                                 ______________________________________________
                              .-'                     _                        '.
                            .'                       |-'                        |
                          .'                         |                          |
                       _.'               p         _\_/_         p              |
                    _.'                  |       .'  |  '.       |              |
               __..'                     |      /    |    \      |              |
         ___..'                         .T\    ======+======    /T.             |
      ;;;\::::                        .' | \  /      |      \  / | '.           |
      ;;;|::::                      .'   |  \/       |       \/  |   '.         |
      ;;;/::::                    .'     |   \       |        \  |     '.       |
            ''.__               .'       |    \      |         \ |       '.     |
                 ''._          <_________|_____>_____|__________>|_________>    |
                     '._     (___________|___________|___________|___________)  |
                        '.    \;;;;;;;;;;o;;;;;o;;;;;o;;;;;o;;;;;o;;;;;o;;;;/   |
                          '.~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~   |
                            '. ~ ~ ~ ~ ~ ~ ~ ~ ~Battleship ~ ~ ~ ~ ~ ~ ~ ~ ~ ~  |
                              '-.______________________________________________.'
    
    
    What mode you want to play? :
    1) Player VS Player
    2) Player VS Random
    ''')

    if option == '1':
        firstPlayerSetup()
        secondPlayerSetup()
    else:
        return

def firstPlayerSetup():

    print("Player1 Setup")

    firstPlayerBoard.newBoard()
    listFirstPlayerPieces = list(firstPlayerBoard.shipsDict.keys())
    firstPlayerBoard.printBoard()


    while len(listFirstPlayerPieces) > 0:

        validInput = False

        print("")
        whichRow = input("Choose a row for your ship: ")
        whichCol = input("Choose a column for your ship: ")
        print(listFirstPlayerPieces)
        while validInput == False:
            whichShip = input("Choose the ship type: ")


            row = int(whichRow)
            col = int(whichCol)
            shipType = str(whichShip)

            if shipType not in listFirstPlayerPieces:
                print("try again")
            else:
                validInput = True



        validPosition = firstPlayerBoard.placeShip(row, col, shipType)
        if validPosition == False:
            print("Cannot place ship here")
            continue
        else:
            firstPlayerBoard.printBoard()
            listFirstPlayerPieces.remove(whichShip)


def secondPlayerSetup():

    print("Player1 Setup")

    secondPlayerBoard.newBoard()
    listSecondPlayerPieces = list(secondPlayerBoard.shipsDict.keys())
    secondPlayerBoard.printBoard()


    while len(listSecondPlayerPieces) > 0:

        validInput = False

        print("")
        whichRow = input("Choose a row for your ship: ")
        whichCol = input("Choose a column for your ship: ")
        print(listSecondPlayerPieces)
        while validInput == False:
            whichShip = input("Choose the ship type: ")


            row = int(whichRow)
            col = int(whichCol)
            shipType = str(whichShip)

            if shipType not in listSecondPlayerPieces:
                print("try again")
            else:
                validInput = True



        validPosition = firstPlayerBoard.placeShip(row, col, shipType)
        if validPosition == False:
            print("Cannot place ship here")
            continue
        else:
            secondPlayerBoard.printBoard()
            listSecondPlayerPieces.remove(whichShip)


menu()
