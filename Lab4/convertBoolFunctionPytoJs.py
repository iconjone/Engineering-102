# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: 		Jonathan Samuel
# Section:		510
# Assignment:	Lab 4 Activity 2
# Date:		    9 25 2018
boolfunc = input("Bool Function pls")
statement = str(boolfunc)
statement = statement.replace("not", "!")
statement = statement.replace("and", "&&")
statement = statement.replace("or", "||")
statement = statement.replace(" ", "")
print(statement)
#( !a && !c) || !b