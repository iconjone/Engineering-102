# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: 		Jonathan Samuel
# Section:		510
# Assignment:	Lab 1
# Date:		    30 08 2018



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


from math import *
import math
one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
arr = [one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve]

arr[0] = (6//5) + 0.0
arr[1] =  (math.sqrt(9%5))
arr[2] =  (math.fabs((3-7)/2-1))
arr[3] =  (2/(math.sin(math.pi/6))) - (1/(math.pow(10,15)))  #(1/1000000000000000) #14 0s
arr[4] =  (1+math.log10(10000))
arr[5] =  (6*math.cos(0))
arr[6] =  (49**(1/2))
arr[7] =  (math.tan(math.pi/4)+7)
arr[8] =  (math.exp(4)//6)
arr[9] =  (fabs((100//9) -21))
arr[10] = (3563 - ((7*9)+ sqrt(250000)))/(30*(100//10)) +1
arr[11] = sqrt(140+(2*2))


for x in range(0,12):
    print("Should be: " + str(x+1) + "    Is: " + str(arr[x]))
    #print(x+1)
