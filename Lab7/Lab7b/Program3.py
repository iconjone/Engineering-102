# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: 		Jonathan Samuel
# Section:		510
# Assignment:	Lab7b
# Date:         10/11/18
dict ={}
user = []
pswd = []
num = input("How many user/pass pairs do u have")
for x in range(0,int(num)):
    user.append(input("Enter in user"))
for x in range(0,int(num)):
    pswd.append(input("Enter in pswd"))

for x in range(0,int(num)):
    dict[user[x]] = pswd[x]


unlocked = False
err = False
while not unlocked:
    user = input("Enter User to log in")
    password = input("Enter Password to log in")
    try:
        if(dict[user] == password):
            unlocked = True
            print("ur allowed into system")
    except:
        print("ur wrong try again")
        unlocked = False
        err = True
    if not err and not unlocked:
        print("ur wrong try again")
