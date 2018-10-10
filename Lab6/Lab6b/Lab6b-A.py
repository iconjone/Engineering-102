# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: 		Jonathan Samuel
# Section:		510
# Assignment:	Lab6b
Iterations = 0


def addIter():
    global Iterations  # Needed to modify global copy of globvar
    Iterations = Iterations + 1
    return Iterations


def getIter():
    global Iterations
    return Iterations

def getSequence(n):
    ret = []
    ret.append(int(n))
    while(n!=1):
        addIter()
        if(n%2 == 0):
            n = n/2
            ret.append(int(n))
        else:
            n = (3*n) + 1
    return ret

def arrToString(arr):
    ret = ', '.join(map(str, arr))
    return ret





def start():
    n = int(input("Please enter a int"))
    arr = getSequence(n)
    print("It took " + str(getIter()) + "Iterations to get 1! - >" + arrToString(arr))

start()