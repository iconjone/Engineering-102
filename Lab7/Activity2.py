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
playerNumber = 0


def addPlayNumb():
    global playerNumber  # Needed to modify global copy of globvar
    playerNumber = playerNumber + 1
    return playerNumber


def getPlayNumb():
    global playerNumber
    return playerNumber


class player:
    def __init__(self, name, first, second, cut, avg):
        self.name = name
        self.first = first
        self.second = second
        self.cut = cut
        self.avg = avg


def getPlayers():
    ret = []
    check = True
    while check:
        playAdd = player("-1", -1, -1, False, -1)
        addPlayNumb()
        first = int(
            input("Please enter the first score of Player " + str(
                getPlayNumb()) + " or negative number to end collection"))
        if first < 0:
            check = False
        elif first >= 0:
            playAdd.first = first
            second = int(input("Please enter the second score of Player " + str(getPlayNumb())))
            playAdd.second = second
            name = str(input("Please enter the name of Player " + str(getPlayNumb())))
            playAdd.name = name
            playAdd.avg = (playAdd.first + playAdd.second) / 2
            ret.append(playAdd)

    return ret


def getMax(playerList):
    max = 0
    for i, c in enumerate(playerList):
        if (max < c.avg):
            max = c.avg
        return max


def sort(playerList):
    ret = []
    max = getMax(playerList)
    while (len(playerList) != 0):
        for i, c in enumerate(playerList):
            maxIndex = 0
            if (max <= c.avg):
                max = c.avg
                maxIndex = i

        ret.insert(0, playerList.pop(maxIndex))

    return ret


def getMedian(playerList):
    if (len(playerList) % 2 != 0):
        return playerList[int((len(playerList) / 2)) + 1].avg
    else:
        return (playerList[int((len(playerList) / 2)) + 1].avg + playerList[int((len(playerList) / 2))].avg) / 2


def setPlayersCut(playerList, median):
    for i, c in enumerate(playerList):
        if median > c.avg:
            c.cut = True
    return playerList


def dividePlayers(listPlayers):
    ret = [[], []]
    for i, c in enumerate(listPlayers):
        if c.cut == False:
            ret[1].append(c)
        else:
            ret[0].append(c)
    return ret


def start():
    listPlayers = sort(getPlayers())
    median = getMedian(listPlayers)
    listPlayers = dividePlayers(setPlayersCut(listPlayers, median))
    for i, c in enumerate(listPlayers[0]):
        print(c.name + " made the cut.")
    for i, c in enumerate(listPlayers[1]):
        print(c.name + " did not make the cut.")


start()
