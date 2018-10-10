# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: 		Jonathan Samuel
# Section:		510
# Assignment:	Lab 4b Program 1
# Date:		    9 25 2018

numbers = input("Please enter your numbers in the format \"x,y,z\"")
numbers = numbers.split(",")

num = -1
index = 0
for x in numbers:
    if num <= float(x):
        num = float(x)
        # index = x

print("The biggest number is " + str(num))
