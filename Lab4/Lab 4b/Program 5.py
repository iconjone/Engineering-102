# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: 		Jonathan Samuel
# Section:		510
# Assignment:	Lab 4b Program 5
# Date:		    9 25 2018

def toFloat(arr):
    for i in range(0, len(arr)):
        arr[i] = float(arr[i])
        return arr


day = input("Please enter the coefficients of the equation Ax^2+Bx+C like so: A/B/C")
day = day.split("/")

day = toFloat(day)
a = day[0]
b = day[1]
c = day[2]
imaginaryCheck = (b ** 2) - (4 * a * c)
if a == 0 and b == 0 and c == 0:
    print("There are infinite roots")
elif a == 0 and b == 0 and c != 0:
    print("There are no roots")
elif imaginaryCheck == 0 and a != 0:
    print("The roots are " + str(complex((b ** 2) - (4 * a * c))))
elif imaginaryCheck < 0:
    print("The roots are " + str(complex((b ** 2) - (4 * a * c))))
elif imaginaryCheck > 0:
    discriminate = (imaginaryCheck ** (1 / 2))
    root1 = (-b + discriminate) / (2 + a)
    root2 = (-b - discriminate) / (2 + a)
    print("The roots are " + str(root1) + " and " + str(root2))
