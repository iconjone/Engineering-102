# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: 		Jonathan Samuel
# Section:		510
# Assignment:	Lab6b
number = 0


def addNumb():
    global number  # Needed to modify global copy of globvar
    number = number + 1
    return number


def getNumb():
    global number
    return number


Min = 0
Max = 0
Avg = 0
end = False
while not end:
    measurement = float(input("Please enter a measurement or negative number to end program"))
    if measurement < 0:
        end = True
        print("The Minimum Number is " + str(Min) + ", The Maximum Number is " + str(Max) + " and the Average is" + str(
            Avg))
    if Min > measurement:
        Min = measurement
    if Max < measurement:
        Max = measurement
    Avg = (Avg*getNumb())+measurement
    addNumb()
    Avg = Avg/getNumb()
