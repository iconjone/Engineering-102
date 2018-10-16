
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
class interval:
    def __init__(self, inc, dec, rangeDays, intervals):
        self.inc = inc
        self.dec = dec
        self.rangeDays = rangeDays
        self.intervals = intervals


def getProductions():
    day = 0
    ret = []
    end = False
    while not end:
        day = day + 1
        measurement = float(
            input("Please enter widget production for day " + str(day) + " or negative number to stop entering values"))
        if measurement < 0:
            end = True
        else:
            ret.append(measurement)

    if end:
        return ret


def getIntervals(arr, rangeDays):
    ret = interval(0, 0, 0, 0)
    ret.rangeDays = rangeDays
    for i in range(len(arr) - 1):
        if i + rangeDays < len(arr):
            ret.intervals = ret.intervals + 1
            # dont have to do less than and equal bc if its equal it just isnt increasing
            if arr[i] < arr[i + rangeDays]:
                ret.inc = ret.inc + 1
            elif arr[i] > arr[i + rangeDays]:
                ret.dec = ret.dec + 1
    return ret


def calcIntervals(arr):
    ret = []
    for i in range(1, len(arr)):
        # ret.append(getIntervals(arr,i))
        appendit = getIntervals(arr, i)
        ret.append(appendit)
    return ret


def printIntervals(arrIntervals):
    for i in arrIntervals:
        print(i.dec)
        print(i.intervals)
        print("For " + str(i.rangeDays) + "-day intervals " + str(round((i.inc / i.intervals) * 100, 1)) + "% were increasing and " + str(round((i.dec / i.intervals) * 100, 1)) + "% were decreasing")


def start():
    productions = getProductions()
    arrIntervals = calcIntervals(productions)
    printIntervals(arrIntervals)


start()
