# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: 		Jonathan Samuel
# Section:		510
# Assignment:	Lab7b
# Date:         10/11/18
def getVectors():
    A = input("Enter in the vector A in the format \'x,y\'")
    B = input("Enter in the vector B in the format \'x,y\'")
    return [[[int(A.split(",")[0])], [int(A.split(",")[1])]], [[int(B.split(",")[0])], [int(B.split(",")[1])]]]

def getMagnitude(vector):
    return ((int(vector[0][0])**2) + (int(vector[1][0])**2))**(1/2)

def addVectors(vectors):
    print("The vector of A + B is: {" + str(vectors[0][0][0] + vectors[1][0][0]) + "," + str(vectors[0][1][0] + vectors[1][1][0]) + ")")

def subVectors(vectors):
    print("The vector of A - B is: (" + str(vectors[1][0][0] - vectors[0][0][0]) + "," + str(vectors[1][1][0] - vectors[0][1][0]) + ")")

def dotVectors(vectors):
    print("The Dot product of A and B is: " + str((vectors[0][0][0] * vectors[1][0][0])+(vectors[0][1][0] * vectors[1][1][0])))

def start():
    vecs = getVectors()
    print("The magnitude of Vector A is: " + str(getMagnitude(vecs[0])))
    print("The magnitude of Vector B is: " + str(getMagnitude(vecs[1])))
    addVectors(vecs)
    subVectors(vecs)
    dotVectors(vecs)




start()
