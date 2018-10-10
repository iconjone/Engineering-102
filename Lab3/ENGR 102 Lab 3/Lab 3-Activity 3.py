# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: 		Jonathan Samuel
# Section:		510
# Assignment:	Lab 3b
# Date:		    9 18 2018
name = input("Enter in a name")
profession = input("Enter in a profession")
number = input("Enter in a number from 1-100")
inumber = int(number) + 99 #dalmations
verb = input("Enter in a verb ending in \"-ed\"")
adjective = input("Enter in an adjective")
city = input("Enter in a city")
sport = input("Enter in a sport")


output = "\t Hi my name is " + str(name) + ". I am a " + str(profession) + ". I have " + str(inumber) + " puppies. I " + str(verb) + " Anthony\'s but he is so " + str(adjective) + ". \n Because of this, I am moving to " + str(city) + " and I am going to do " + str(sport) + " professionally. Thank you for listening to my TED talk."

print(output)


