
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
import math


class cubiccoefficientsObjects:
    def __init__(self, A, B, C, D):
        self.A = A
        self.B = B
        self.C = C
        self.D = D


class bicoefficientsObjects:
    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C


Iterations = 0


def addIter():
    global Iterations  # Needed to modify global copy of globvar
    Iterations = Iterations + 1
    return Iterations


def getIter():
    global Iterations
    return Iterations


def resetIter():
    global Iterations
    Iterations = 0


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
    return cubiccoefficientsObjects(list[0], list[1], list[2], list[3])


def cubictobi(cubiccoefficientsObjects):
    ret = bicoefficientsObjects(cubiccoefficientsObjects.A * 3, cubiccoefficientsObjects.B * 2,
                                cubiccoefficientsObjects.C)
    return ret


def returnAnal(bicoefficientsObjects, point):
    return (bicoefficientsObjects.A * (point ** 2)) + (bicoefficientsObjects.B * (point ** 1)) + bicoefficientsObjects.C


def getPointFunction(coefficientsObjects, point):
    point = (coefficientsObjects.A * (point ** 3)) + (coefficientsObjects.B * (point ** 2)) + (
            coefficientsObjects.C * (point ** 1)) + (coefficientsObjects.D)
    return point


def returnNumerA(cubiccoefficientsObjects, point):
    a = .1
    prev = ((getPointFunction(cubiccoefficientsObjects, point + a) - getPointFunction(cubiccoefficientsObjects,
                                                                                      point)) / a) + 1
    now = ((getPointFunction(cubiccoefficientsObjects, point + a) - getPointFunction(cubiccoefficientsObjects,
                                                                                     point)) / a)
    while (10 ** -6) < math.fabs(prev - now):
        addIter()
        a = a / 2
        prev = now
        now = ((getPointFunction(cubiccoefficientsObjects, point + a) - getPointFunction(cubiccoefficientsObjects,
                                                                                         point)) / a)
    return now


def executeFunction(exec, point):
    a = .1
    x = point
    exech = exec.replace("x", "(x+a)")
    prev = "( (" + exech + "-" + exec + ")" + "/a ) + 1"
    now = "(" + exech + "-" + exec + ")" + "/a"
    prev = eval(prev)
    now = eval(now)
    while (10 ** -6) < math.fabs(prev - now):
        addIter()
        a = a / 2
        prev = now
        now = "(" + exech + "-" + exec + ")" + "/a"
        now = eval(now)
    return now


def getPoint():
    point = input("Please Enter a point to compute derivatives at")
    if (point.replace("-", "").replace(".", "").isdigit()):
        return float(point)
    else:
        print("try again bozo")
        return getPoint()

def cleanUp(exec):
    exec = exec.replace("^", "**").replace("log(", "math.log(").replace("cos(", "math.cos(").replace("sin(",
                                                                                                    "math.sin(").replace(
        "tan(", "math.tan(").replace("sqrt(", "math.sqrt(").replace("pi", "math.pi").replace(" ", "")

    for i, c in enumerate(exec):
        if c== "x":
            if not(exec[i-1] == "*" or exec[i-1] == "/" or exec[i-1] == "(" or exec[i-1] == "+" or exec[i-1] == "-" or exec[i+1] == "^"):
                exec = exec[:i] + "*" + exec[i:]
                i = i+1
            if not(exec[i+1] == "*" or exec[i+1] == "/" or exec[i+1] == ")" or exec[i+1] == "+" or exec[i+1] == "-" or exec[i+1] == "^"):
                exec = exec[:i+1] + "*" + exec[i+1:]


    return exec

def start():
    cub = getCoefficients()
    point = getPoint()
    bi = cubictobi(cub)

    print("Part a computed by derivative is: " + str(returnAnal(bi, point)))
    print("Part b computed by numerical analysis is: " + str(returnNumerA(cub, point)) + " This took " + str(getIter()) + " Iterations to get")
    resetIter()

    userFunction = input("Please Enter a function with ti-84 or equivalent notation")
    userFunction = cleanUp(userFunction)
    point = getPoint()
    print("Part c computed by numerical analysis is: " + str(executeFunction(userFunction, point)) + " This took " + str(getIter()) + " Iterations to get")




start()
