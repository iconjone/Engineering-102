import random

f = open("bigFile.txt", "w+")
for x in range(0, 1000000):
    # print(str(random.randint(20,30)) + "," + str(random.randint(20,30)))
    f.write(str(random.randint(0,x)) + "," + str(random.randint(0,x)) + "\n")
f.close()
