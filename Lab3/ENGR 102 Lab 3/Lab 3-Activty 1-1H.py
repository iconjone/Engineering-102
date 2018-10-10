# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Names: 	Evan Farkis
# 	 		Emmanuel Garcia
# 	 		Tarik Dawson
#			Jonathan Samuel
# Section:		510
# Assignment:	Lab Assignment 3
# Date:		13 09 2018
from math import *


def getEnergy(scale):
    return pow(10, ((1.5 * scale) + 4.8))


userInput = input("First richter scale value")
richter_scale_value1 = float(userInput)
userInput = input("Second richter scale value")
richter_scale_value2 = float(userInput)
energy_released1 = getEnergy(richter_scale_value1)
energy_released2 = getEnergy(richter_scale_value2)
if(energy_released1>energy_released2):
    print(energy_released1-energy_released2)
if(energy_released2>energy_released1):
    print(energy_released2-energy_released1)
