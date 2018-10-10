# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: 		Jonathan Samuel
# Section:		510
# Assignment:	Lab 2b
# Date:		    9 10 2018
import math
# Question A
print("Jonathan Samuel UIN:" + str(427005068) + " Section Number:" + str(510))
#Question B
print("I play the piano")
#Question C
resistance = 20
current = 5
voltage = current*resistance
print(voltage)
#Question D
mass = 100
velocity = 21
kineticEnergy = .5*100*(math.pow(velocity , 2))
print(kineticEnergy)
#Question E
velocity = 100
kinematicViscosity = 1.2
linearDimension = 2.5
reynoldsNumber = (velocity*linearDimension)/(kinematicViscosity)
print(reynoldsNumber)
#Question F
temperature=2200
stefanBoltzmannConstant = 5.67 * math.pow(10, -8)
energy = stefanBoltzmannConstant * math.pow(temperature, 4)
print(energy)
#Question G
days = 20
initialProductionRate = 100
declineRate = 2
hyperbolicConstant =.8
production = initialProductionRate * math.pow(1 + (hyperbolicConstant * (declineRate) * days), -1 / hyperbolicConstant)
print(production)
#Question H
lam = 20
mu = 35
poissonPacket = lam/mu
length = poissonPacket/(1-poissonPacket)
print(length)
#Question I
stress=20
cohesion=2
angle=35
shearStress = stress*math.tan(angle) + cohesion
print(shearStress)
#Question J
wavelength = 7.5 * math.pow(10 , -7)
distance = 1 * math.pow(10, -6)
angle = math.degrees(math.asin(wavelength/(2*distance)))
print(angle)


