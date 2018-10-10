# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Names: 	Emmanuel Garcia
#			Jonathan Samuel
# Section:		510
# Assignment:	Lab 3
# Date:		 09 13 2018
name = []
date = []
for i in range(1, 5):
    userInput = input("Enter name and Birthday Number " + str(i) + ". Enter in each name and birthday seperated by "
                                                                   "commas and birthday seperated by slashes \"First "
                                                                   "Last,mm/dd/yyyy\" ")
    name.append(userInput.split(",")[0])
    date.append(userInput.split(",")[1].split("/"))
biggest = 0
biggestIndex = 0
for i in range(0, 4):
    if len(name[i]) > biggest:
        biggest = len(name[i])
        biggestIndex = i

for i in range(0, 4):
    addSpace = ""
    repeat = biggest - len(name[i])
    for x in range(0, repeat):
        addSpace = addSpace + " "
    print(addSpace + name[i] + " | " + date[i][0] + "/" + date[i][1] + "/" + date[i][2])
