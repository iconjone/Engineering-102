
# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Names: 	Evan Farkis
# 	 		Emmanuel Garcia
# 	 		Tarik Dawson
#			Jonathan Samuel
# Section:		510
# Assignment:	Lab Assignment 1
# Date:		30 08 2018

mark1 = 0; mark2 = 0; time1 = 0; time2 = 0; timeMid = 0; isInMiddle = None;
userInput = input('First Measurement Distance or press enter to use Default values')
if(userInput == ""):
    mark1 = 50
if((userInput != "")):
    mark1 = float(userInput)
userInput = input('First Measurement Time or press enter to use Default values')
if(userInput == ""):
    time1 = 30
if((userInput != "")):
    time1 = float(userInput)
userInput = input('Second Measurement Distance or press enter to use Default values')
if(userInput == ""):
    mark2 = 615
if((userInput != "")):
    mark2 = float(userInput)
userInput = input('Second Measurement Time or press enter to use Default values')
if(userInput == ""):
    time2 = 45
if((userInput != "")):
    time2 = float(userInput)

mark1 = mark1 % 3141.59
mark2 = mark2 % 3141.59


isInMiddle = False

while(isInMiddle == False):
    userInput = input('At what time do you want to know the distance - Press enter to use Default Value')
    timeMid = 37
    if ((userInput == "")):
        isInMiddle = True
    if ((userInput != "")):
        timeMid = float(userInput)
        if(timeMid>=time1 and timeMid<=time2):
            isInMiddle = True
        if (timeMid <= time1 or timeMid >= time2):
            print("Try again - Number is not in between " + str(mark1) + " and " + str(mark2))

v = (mark2-mark1) / (time2-time1)
b = mark1 - (v*time1)
p = (v*timeMid) + b

print(timeMid)

print("The car is " + str(p) + " meters from the starting line")

