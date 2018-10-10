# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: 		Jonathan Samuel
# Section:		510
# Assignment:	Lab 2b
# Date:		    9 10 2018
p1 = ""; p2 = ""; y1=0; y2=0; z1 = 0; z2 = 0; time1 = 0; time2 = 0; timeMid = 0;
userInput = input('First point \"x1,y1,z1\" or press enter to use Default values')
if(userInput == ""):
    p1 = "1,3,7"
if((userInput != "")):
    p1 = str(userInput)
arr1 = p1.split(",")
userInput = input('First Measurement Time or press enter to use Default values')
if (userInput == ""):
   time1 = 13
if ((userInput != "")):
    time1 = float(userInput)
userInput = input('Second point \"x2,y2,z2\" or press enter to use Default values')
if(userInput == ""):
    p2 = "23,-5,10"
if((userInput != "")):
    p2 = str(userInput)
arr2 = p2.split(",")
userInput = input('Second Measurement Time or press enter to use Default values')
if(userInput == ""):
    time2 = 84
if((userInput != "")):
    time2 = float(userInput)
userInput = input('Enter Wanted Measurement Time or press enter to use Default values')
if(userInput == ""):
    timeMid = 50
if((userInput != "")):
    timeMid = float(userInput)


def getPoint(i,f,ti,tf,tw):
    v = (f-i) / (tf-ti)
    b = i - (v * ti)
    p = (v * tw) + b
    return p

answer = []
for i in range(0, 3):
    answer.append(getPoint(float(arr1[i]), float(arr2[i]), time1, time2, timeMid))

print(answer)


