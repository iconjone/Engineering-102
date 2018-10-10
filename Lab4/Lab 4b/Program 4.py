# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: 		Jonathan Samuel
# Section:		510
# Assignment:	Lab 4b Program 4
# Date:		    9 25 2018

day = input("Please enter the day wanted")
day = int(day)

widgets = 0

if day <= 10:
    widgets = day * 10
elif 11 <= day <= 60:
    widgets = (day-10)*40 + 100
elif 61 <= day <= 99:
    widgets = 100 + (50*40)
    daysLeft = day - 60
    for x in range(daysLeft + 1):
        widgets = widgets + (40-x)
elif 100 <= day:
    widgets = 2920


print("The Flow is " + str(widgets))
