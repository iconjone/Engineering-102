
# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Names: 	Evan Farkas
# 	 		Emmanuel Garcia
# 	 		Tarik Dawson
#			Jonathan Samuel
# Section:		510
# Assignment:	Lab Assignment 6
# Date:		9 10 2018
class coefficientsObjects:
    def __init__(self, A, B, C, D):
        self.A = A
        self.B = B
        self.C = C
        self.D = D


class rangeObjects:
    def __init__(self, a, b):
        self.a = a
        self.b = b


Iterations = 0


def addIter():
    global Iterations  # Needed to modify global copy of globvar
    Iterations = Iterations + 1
    return Iterations


def getIter():
    global Iterations
    return Iterations


# Make sure Corffcients are all numbers and make sure they are in the right format
def getCoefficients():
    coefficients = input("Please enter the coefficients of the equation AX^3+BX^2+CX+D in the format \"A,B,C,D\"")
    min = 0
    isGood = True
    for i in range(0, 3):
        if coefficients.find(",", min, len(coefficients)) != -1:
            min = coefficients.find(",", min, len(coefficients)) + 1
            if (i == 2):
                if coefficients.find(",", min, len(coefficients)) != -1:
                    isGood = False

        else:
            isGood = False

    list = coefficients.split(",")
    for r in range(0, len(list)):
        if (list[int(r)].replace('-', '').isdigit()):
            list[int(r)] = float(list[int(r)])
        else:
            isGood = False

    if not isGood:
        print("Try Again")
        return getCoefficients()
    return coefficientsObjects(list[0], list[1], list[2], list[3])


# Make sure ranges are all numbers and make one lower than the other
def getRange():
    ranges = input("Please enter the range of the equation in the form \"a,b\"")
    min = 0
    isGood = True
    for i in range(0, 1):
        if ranges.find(",", min, len(ranges)) != -1:
            min = ranges.find(",", min, len(ranges)) + 1
            if (i == 1):
                if ranges.find(",", min, len(ranges)) != -1:
                    isGood = False

        else:
            isGood = False

    list = ranges.split(",")
    for r in range(0, len(list)):
        if (list[int(r)]).replace('.', '').replace('-', '').isdigit():
            # if range needs to be only int change it to "list[int(r)] = int(list[int(r)])"
            list[int(r)] = float(list[int(r)])
        else:
            isGood = False

    if isGood:
        if list[0] == list[1]:
            isGood = False

    if not isGood:
        print("Try Again")
        return getRange()
    if isGood:
        if list[0] < list[1]:
            return rangeObjects(list[0], list[1])
        else:
            return rangeObjects(list[1], list[0])


def haveRoot(coefficientsObjects, rangeObjects):
    # print(type(rangeObjects.a))
    print(rangeObjects.a)
    low = (coefficientsObjects.A * (rangeObjects.a ** 3)) + (coefficientsObjects.B * (rangeObjects.a ** 2)) + (
            coefficientsObjects.C * (rangeObjects.a ** 1)) + (coefficientsObjects.D)
    high = (coefficientsObjects.A * (rangeObjects.b ** 3)) + (coefficientsObjects.B * (rangeObjects.b ** 2)) + (
            coefficientsObjects.C * (rangeObjects.b ** 1)) + (coefficientsObjects.D)

    lowdiv = (coefficientsObjects.A * 3 * (rangeObjects.a ** 2)) + (
                coefficientsObjects.B * 2 * (rangeObjects.a ** 1)) + (
                 coefficientsObjects.C)
    highdiv = (coefficientsObjects.A * 3 * (rangeObjects.b ** 2)) + (
            coefficientsObjects.B * 2 * (rangeObjects.b ** 1)) + (
                  coefficientsObjects.C)

    print("low:" + str(low))
    print("high:" + str(high))
    print("lowdiv:" + str(lowdiv))
    print("highdiv:" + str(highdiv))

    if lowdiv <= 0 and highdiv > 0 or lowdiv > 0 and highdiv <= 0:
        return True


    if (low <= 0 and high > 0) or (low > 0 and high <= 0):
        return True
    else:
        return False


def getPoint(coefficientsObjects, point):
    point = (coefficientsObjects.A * (point ** 3)) + (coefficientsObjects.B * (point ** 2)) + (
            coefficientsObjects.C * (point ** 1)) + (coefficientsObjects.D)
    return point


def midRange(rangeObjects):
    return (rangeObjects.a + rangeObjects.b) / 2


def isIntervalSmall(rangeObjects):
    ret = False
    if (rangeObjects.b - rangeObjects.a < 10 ** -6):
        ret = True
    return ret


def getRootRange(coefficentObjects, rangeObjectsInput):
    if haveRoot(coefficentObjects, rangeObjectsInput):
        print("Has Root! Calculating...")
        rootFound = False
        rangeTest = rangeObjectsInput
        while not rootFound:
            addIter()
            if isIntervalSmall(rangeTest):
                rootFound = True  # unessecary but eh
                return rangeTest
            mid = midRange(rangeTest)
            print(mid)
            if getPoint(coefficentObjects, mid) < 0:
                rangeTest = rangeObjects(mid, rangeTest.b)
            else:
                rangeTest = rangeObjects(rangeTest.a, mid)
    else:
        again = input("Sorry there is no root between these two ranges... try again? Yes or No")
        if (
                again == "Yes" or again == "YES" or again == "Y" or again == "Yah" or again == "Yeah" or again == "YEAH" or again == "y" or again == "yup"):
            start()
        else:
            return -1


def start():
    coefficients = getCoefficients()
    ranges = getRange()
    grange = getRootRange(coefficients, ranges)

    if grange != -1:
        print("Your root is " + str(midRange(grange)) + ". This took " + str(getIter()) + " iterations to calculate!")


start()
