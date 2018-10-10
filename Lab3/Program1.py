# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: 		Jonathan Samuel
# Section:		510
# Assignment:	Lab 2b
# Date:		    9 13 2018
import math

# Question D
print("Kinetic Energy Of Object Calculator")
mass = float(input('Please enter your mass'))
velocity = float(input('Please enter your velocity'))
kineticEnergy = .5 * 100 * (math.pow(velocity, 2))
print("The Kinetic Energy is: " + str(kineticEnergy))
# Question I
print("Shear Stress Calculator")
stress = float(input('Please enter Normal Stress'))
cohesion = float(input('Please enter cohesion value'))
angle = float(input('Please enter angle of internal friction'))
shearStress = stress * math.tan(angle) + cohesion
print("The Shear Stress is: " + str(shearStress))
# Question G
print("Well Production Calculator")
days = float(input('Please enter Number of Days'))
initialProductionRate = float(input('Please Enter initial Production Rate'))
declineRate = float(input('Please Enter decline Rate'))
hyperbolicConstant = float(input('Please Enter hyperbolic constant'))
production = initialProductionRate * math.pow(1 + (hyperbolicConstant * declineRate * days), -1 / hyperbolicConstant)
print('The Production rate is: ' + str(production))
# Question H
print("Average Length of M/M/1 queue Calculator")
lam = float(input('Please Enter Arrival Rate'))
mu = float(input('Please Enter Service Rates'))
poissonPacket = lam / mu
length = poissonPacket / (1 - poissonPacket)
print('The average length is: ' + str(length))
