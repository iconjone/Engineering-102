# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: 		Jonathan Samuel
# Section:		510
# Assignment:	Lab 4b Program 2
# Date:		    9 25 2018

height = input("Please enter the height of the patient in freedom units (Inches)")
height = float(height)
weight = input("Please enter the weight of the patient in freedom units (lb)")
weight = float(weight)

BMI = weight / (height ** 2) * 703

classification = ""
if BMI < 18.5:
    classification = "Underweight"
elif 18.5 <= BMI <= 24.9:
    classification = "Normal Weight"
elif 24.9 < BMI <= 29.9:
    classification = "Overweight"
elif 29.9 < BMI:
    classification = "Obese"


print("Patient is " + classification)
