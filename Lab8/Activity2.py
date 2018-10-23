import sys
import time
from math import *
from threading import Thread


class coordinates:
    def __init__(self, x, y):
        self.x = x
        self.y = y


xMean = 0


def setxMean(mean):
    global xMean
    xMean = mean


yMean = 0


def setyMean(mean):
    global yMean
    yMean = mean


slope = 0


def setSlope(slopeI):
    global slope
    slope = slopeI


def getXSD(Coordinates):
    CoordinatesList = []
    for x, c in enumerate(Coordinates):
        CoordinatesList.append(c.x)

    meanx = sum(CoordinatesList) / len(CoordinatesList)

    meansub = []
    for c in CoordinatesList:
        meansub.append((c - meanx) ** 2)

    meansubOflist = sum(meansub) / len(meansub)
    meansubOflist = sqrt(meansubOflist)

    return meansubOflist


def getYSD(Coordinates):
    CoordinatesList = []
    for y, c in enumerate(Coordinates):
        CoordinatesList.append(c.y)

    meany = sum(CoordinatesList) / len(CoordinatesList)

    meansub = []
    for c in CoordinatesList:
        meansub.append((c - meany) ** 2)

    meansubOflist = sum(meansub) / len(meansub)
    meansubOflist = sqrt(meansubOflist)

    return meansubOflist


def getYMean(corridinates):
    CorridinatesList = []
    for y, c in enumerate(corridinates):
        CorridinatesList.append(c.y)
    sum = 0
    for c in CorridinatesList:
        sum += c
    averageY = sum / len(CorridinatesList)
    setyMean(averageY)
    return averageY


def getXMean(Coordinates):
    CoordinatesList = []
    for x, c in enumerate(Coordinates):
        CoordinatesList.append(c.x)
    sum = 0
    for c in CoordinatesList:
        sum += c
    average = sum / len(CoordinatesList)
    setxMean(average)
    #set global val to avg and extra method jic
    return average


def getR(coordinatesList):
    #tech calculate slope but also correlation value
    amean = getXMean(coordinatesList)
    bmean = getYMean(coordinatesList)
    for x, c in enumerate(coordinatesList):
        coordinatesList[x] = coordinates(c.x - amean, c.y - bmean)
    ab = 0
    a2 = 0
    b2 = 0
    for x, c in enumerate(coordinatesList):
        ab = ab + (c.x * c.y)
        a2 = a2 + (c.x ** 2)
        b2 = b2 + (c.y ** 2)
    slope = ab / (a2)
    setSlope(slope)
    return slope




def getUserCoordinates():
    coordinateObjects = []
    print(
        "Please enter in your coordinate values in the form of \"x,y\" - If you would like to stop entering points, please enter a blank line")
    notNull = True
    while notNull:
        userInput = input("")
        if userInput == "":
            notNull = False
        else:
            split = userInput.split(",")
            #take user input and it all into the list full of coordinate objects
            coordinateObjects.append(coordinates(float(split[0]), float(split[1])))
    return coordinateObjects


def getValues(slope, b):
    #init and tell user how to enter in values
    print("Please enter in your values - If you would like to stop entering points, please enter a blank line")
    notNull = True
    while notNull: #while it's not null...
        userInput = input("")
        if userInput == "":
            notNull = False
        else:
            print("The point at " + userInput + " would be about " + str((float(userInput) * slope) + b) + ".")



coordinatesList = getUserCoordinates()

# divide all of the components into threads so that it will run faster
xmt = Thread(target=getXMean, args=(coordinatesList,))
ymt = Thread(target=getYMean, args=(coordinatesList,))
slopet = Thread(target=getR, args=(coordinatesList,))

xmt.start()
ymt.start()
slopet.start()

sys.stdout.flush()

done = False  # This will run if it's gonna take a while
while slopet.is_alive() or xmt.is_alive() or ymt.is_alive():
    while not done:
        sys.stdout.write("\rCalculating Equation.")
        time.sleep(.3)
        sys.stdout.write("\rCalculating Equation..")
        time.sleep(.3)
        sys.stdout.write("\rCalculating Equation...")
        time.sleep(.3)
        sys.stdout.flush()
        time.sleep(.3)
        if not (slopet.is_alive() and xmt.is_alive() and ymt.is_alive()):
            done = True
            print("\nEquation Calculated")

# calculate the y intercept
b = yMean - (slope * xMean)
# print out the equation calculated
print("The equation calculated is y=" + str(slope) + "x + " + str(b))
# allow users to get values
getValues(slope, b)
