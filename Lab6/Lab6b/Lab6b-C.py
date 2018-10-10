# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: 		Jonathan Samuel
# Section:		510
# Assignment:	Lab6b
# Date:		    10 9 2018


def getDivisors(i):
    for x in range(2,i+1):
        if i%x == 0:
            print(str(x) + " divides " + str(i))

for i in range(2,101):
    getDivisors(i)