# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: 		Jonathan Samuel
# Section:		510
# Assignment:	Quiz 5
# Date:         10/11/2018
list = []
list.append(input("Enter your number 1 pop music star of the 2000s-2010s"))
list.append(input("Enter your number 2 pop music star of the 2000s-2010s"))
list.append(input("Enter your number 3 pop music star of the 2000s-2010s"))
list.append(input("Enter your number 4 pop music star of the 2000s-2010s"))
list.append(input("Enter your number 5 pop music star of the 2000s-2010s"))
contain = False
for i, c in enumerate(list):
    if c == "Justin Bieber":
        contain = True

if not contain:
    list.pop()
    list.insert(0, "Justin Bieber")
print("Ok, so you like ['" + list[0] + "', '" + list[1] + "', '" + list[2] + "', '" + list[3] + "', '" + list[4] + "']")
