# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: 		Jonathan Samuel
# Section:		510
# Assignment:	Quiz2
# Date:		    9 20 2018


# Get Time from User Input and convert into minutes
def getTime():
    time = input("In minutes, what time is the fight at?")
    time = float(time)
    time = time * 60
    print(time)
    return time


# Get part of stage or return empty if it doesn't fall into constraints
def getStage(time):
    if 0.0 <= time <= 100.0:
        return "Stage 1"
    elif 100.0 <= time <= 170.0:
        return "Stage 2"
    elif 170.0 <= time <= 260.0:
        return "Stage 3"
    elif time > 260.0:
        return "Free Flight"
    else:
        return ""


# Start Program by getting time
time = getTime()
# Set Boolean to check if the number that has been entered is valid
done = False
# Make sure the loop runs until it's done
while not done:
    flight = getStage(time)
    if flight != "":
        print("The rocket is in " + flight)
        done = True
    else:
        print("Try again - You can't input a negative number")
        time = getTime()
