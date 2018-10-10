# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: 		Jonathan Samuel
# Section:		510
# Assignment:	Quiz3
# Date:		    9 27 2018


# Get the values for a, b, and c via function that will make sure that they are entering the value and if it isnt
# right it will repeat that function until its good
def getBoola():
    tf = input("Please enter true or false for Boolean A")
    if (tf == "t" or tf == "T" or tf == "true" or tf == "TRUE" or tf == "1"):
        return True
    if (tf == "f" or tf == "F" or tf == "false" or tf == "FALSE" or tf == "0"):
        return False
    else:
        print("Try again - please enter true or false!")
        return getBoola()


def getBoolb():
    tf = input("Please enter true or false for Boolean B")
    if (tf == "t" or tf == "T" or tf == "true" or tf == "TRUE" or tf == "1"):
        return True
    if (tf == "f" or tf == "F" or tf == "false" or tf == "FALSE" or tf == "0"):
        return False
    else:
        print("Try again - please enter true or false!")
        return getBoolb()


def getBoolc():
    tf = input("Please enter true or false for Boolean C")
    if (tf == "t" or tf == "T" or tf == "true" or tf == "TRUE" or tf == "1"):
        return True
    if (tf == "f" or tf == "F" or tf == "false" or tf == "FALSE" or tf == "0"):
        return False
    else:
        print("Try again - please enter true or false!")
        return getBoolc()


# Test and append tf variables to list
def testBools(A, B, C):
    arr = []
    arr.append((A and B) and C)
    arr.append((A and B) or C)
    arr.append((A or B) and C)
    arr.append((A or B) or C)
    arr.append(A and (B and C))
    arr.append(A and (B or C))
    arr.append(A or (B and C))
    arr.append(A or (B or C))

    return arr


A = getBoola()
B = getBoolb()
C = getBoolc()

t = 0
f = 0

arr = testBools(A, B, C)

#for every variable in arr check if t or f and add 1 to variable when it gets it
for x in arr:
    if x:
        t = t+1
    elif not x:
        f = f+1

print("For A=" + str(A) + ", B=" + str(B) + ", C=" + str(C) + " the number of Trues is " + str(t) + " and the number of Falses is " + str(f))
