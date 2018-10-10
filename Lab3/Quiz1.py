# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: 		Jonathan Samuel
# Section:		510
# Assignment:	Lab 2b
# Date:		    9 13 2018
#Ask User how much coffee they want
userInput = input("How much pounds of coffee do you need?")
#get How much pounds of coffee they want
poundsOfCoffee = float(userInput)
#Calculate the price per pound of the coffee beans plus how much it costs to ship it
pricePerPound = 10.5 + .86
#Multiply the pounds by the price per pound
itemCost = poundsOfCoffee*pricePerPound
#shipping cost
shippingCost = 1.5
#calculate total cost
totalCost = shippingCost + itemCost

print("Your order will cost you $"+str(totalCost)+"!")
