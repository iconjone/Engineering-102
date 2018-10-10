import math


def toFloat(arr):
    for i in range(0, len(arr)):
        arr[i] = float(arr[i])


def getPoints():
    userInput = input('3D point of Observer \"x,y,z\" ')
    if ((userInput != "") and "," in userInput):
        observer = str(userInput)
        arrObserver = observer.split(",")
    else:
        print("You messed up - Try again")
        getPoints()

    userInput = input('First Observed 3D Point \"x,y,z\" ')
    if ((userInput != "") and "," in userInput):
        first = str(userInput)
        arrFirst = first.split(",")
    else:
        print("You messed up - Try again")
        getPoints()

    userInput = input('Second Observed 3D Point \"x,y,z\" ')
    if ((userInput != "") and "," in userInput):
        second = str(userInput)
        arrSecond = second.split(",")
    else:
        print("You messed up - Try again")
        getPoints()

    toFloat(arrObserver)
    toFloat(arrFirst)
    toFloat(arrSecond)

    return arrObserver, arrFirst, arrSecond


def calcVectors(observer, point):
    vec = [point[0] - observer[0], point[1] - observer[1], point[2] - point[2]]
    return vec


def getMagnitude(vec):
    return math.sqrt(vec[0] ** 2 + vec[1] ** 2 + vec[2] ** 2)


def normVector(vec):
    magnitude = getMagnitude(vec)
    vec = [vec[0] / magnitude, vec[1] / magnitude, vec[2] / magnitude]
    return vec


def dotProduct(vec1, vec2):
    #print(str(vec1[0]) + " " + str(vec2[0]))
    #print((vec1[0] * vec2[0]) + (vec1[1] * vec2[1]) + (vec1[2] * vec2[2]))
    return (vec1[0] * vec2[0]) + (vec1[1] * vec2[1]) + (vec1[2] * vec2[2])


points = getPoints()
vec1 = normVector(calcVectors(points[0], points[1]))
vec2 = normVector(calcVectors(points[0], points[2]))
#print("dot product is : " + str(dotProduct(vec1, vec2)))
#print(math.radians(dotProduct(vec1, vec2)))
#print(dotProduct(vec1, vec2))
print("The Angle is: " + str(math.degrees(math.acos(math.radians(dotProduct(vec1, vec2))))))