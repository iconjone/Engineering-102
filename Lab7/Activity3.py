# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Names: 	Evan Farkas
# 	 		Emmanuel Garcia
# 	 		Tarik Dawson
#			Jonathan Samuel
# Section:		510
# Assignment:	Lab Assignment 7
# Date:		10 11 2018

# Not needed - Just if I ever mess up the board
def generate():
    chessboard = "RNBQKBNR PPPPPPPP ........ ........ ........ ........ pppppppp rnbqkbnr"
    split = chessboard.split(" ")
    string = "["
    for c in split:

        string = string + " ["
        for x in range(0, len(c)):
            string = string + "\"" + c[x] + "\", "
        string = string[0:len(string) - 1] + "],"
    string = string[0:len(string) - 1] + "]"
    print(string)


class location:
    def __init__(self, x, y):
        self.x = x
        self.y = y


chessboard = [["R", "N", "B", "Q", "K", "B", "N", "R", ], ["P", "P", "P", "P", "P", "P", "P", "P", ],
              [".", ".", ".", ".", ".", ".", ".", ".", ], [".", ".", ".", ".", ".", ".", ".", ".", ],
              [".", ".", ".", ".", ".", ".", ".", ".", ], [".", ".", ".", ".", ".", ".", ".", ".", ],
              ["p", "p", "p", "p", "p", "p", "p", "p", ], ["r", "n", "b", "q", "k", "b", "n", "r", ]]


def printInstructions():
    chessboardInstructions = [[".", "1", "2", "3", "4", "5", "6", "7", "8"],
                              ["1", "R", "N", "B", "Q", "K", "B", "N", "R", ],
                              ["2", "P", "P", "P", "P", "P", "P", "P", "P"],
                              ["3", ".", ".", ".", ".", ".", ".", ".", ".", ],
                              ["4", ".", ".", ".", ".", ".", ".", ".", ".", ],
                              ["5", ".", ".", ".", ".", ".", ".", ".", ".", ],
                              ["6", ".", ".", ".", ".", ".", ".", ".", ".", ],
                              ["7", "p", "p", "p", "p", "p", "p", "p", "p", ],
                              ["8", "r", "n", "b", "q", "k", "b", "n", "r", ]]
    for r in chessboardInstructions:
        printRet = ""
        for c in r:
            printRet = printRet + c
        print(printRet)


def changeChessboard(location1, location2):
    global chessboard  # Needed to modify global copy of globvar
    print(location1.y)
    print(chessboard[0][7])
    if chessboard[location1.x][location1.y] == ".":
        return False
    else:
        chessboard[location2.x][location2.y] = chessboard[location1.x][location1.y]
        chessboard[location1.x][location1.y] = "."
        return True


def printChessboard():
    global chessboard
    for r in chessboard:
        printRet = ""
        for c in r:
            printRet = printRet + c
        print(printRet)
    print("--------")


def movePiece():
    # account for the wierd stuff that people will do and subrtact user int by 1
    moves = input("Enter Movement")
    moves = moves.split("-")
    location1 = location(int(moves[0].split(",")[0][1]) - 1, int(moves[0].split(",")[1][0]) - 1)
    location2 = location(int(moves[1].split(",")[0][1]) - 1, int(moves[1].split(",")[1][0]) - 1)
    print(int(moves[1].split(",")[0][1]))

    return changeChessboard(location1, location2)


def start():
    print("Enter in the movement that you want in the form of: (firstx,firsty),(secondx,secondy)")
    print(
        "This means if you would like to move the black left rook to the white right rook, you would enter \"(8/1)-"
        "(1/8)\"")
    print("Here is a map of the chess board for your convenience - (down, right)")
    printInstructions()
    good = True
    while good:
        good = movePiece()
        printChessboard()
    print("Game had a mistake! Try again")


start()
