# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: 		Jonathan Samuel
# Section:		510
# Assignment:	Lab 1b
# Date:		    1 9 2018
import math
print("")

#Function 1
print("This shows the evaluation of sin(x)/(x) evaluated close to x=0")
print("My guess is 1.0")
for i in range(0, 8):
    x = 1 * math.pow(10, -1 * i)
    print(math.sin(x) / x)
print("")

#Function 2
print("This shows the evaluation of (1-cos(x))/x^2 evaluated close to x=0")
print("My guess is 0.5")
for i in range(0, 8):
    x = 1 * math.pow(10, -1 * i)
    print((1-math.cos(x)) / (x**2))
print("")

#Function 3
print("This shows the evaluation of (1+(1/x))^x evaluated close to x=∞")
print("My guess is e")
for i in range(0, 8):
    x = 1 * math.pow(10, 1 * i)
    print((1+(1/x))**x)








