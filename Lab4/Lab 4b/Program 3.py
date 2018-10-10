# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: 		Jonathan Samuel
# Section:		510
# Assignment:	Lab 4b Program 3
# Date:		    9 25 2018
print("Formula was taken from this resource: https://academy.paulmueller.com/how-does-the-reynolds-number-affect"
      "-mixer-design")
fv = input("Please enter the Fluid Velocity")
fv = float(fv)
kv = input("Please enter the kinematic viscosity")
kv = float(kv)
cld = input("Please enter the characteristic linear dimension")
cld = float(cld)

RE = fv * cld / kv

classification = ""
if RE < 100:
    classification = "Laminar "
elif 100 <= RE < 10000:
    classification = "Transition "
elif 10000 <= RE:
    classification = "Turbulent "


print("The Flow is" + classification)
