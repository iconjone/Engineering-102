# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: 		Jonathan Samuel
# Section:		510
# Assignment:	Quiz4
# Date:		    10 4 2018
def getUpperLimit():
    upperlimit = input("Input upper limit")
    # Clean out any wrong parts
    if upperlimit.replace("-", "").replace(".", "").isdigit():
        # Return the int
        return int(upperlimit.replace("-", ""))
    else:
        # Tell them to try again
        print("Try Again")
        return getUpperLimit()


def getString(upperLimit):
    ret = ""
    # Set it so that it tries every number but make it easy on me and offset it by 1 than the usual 0
    for x in range(1, upperLimit + 1):
        # If it's the last one I dont want an extra comma so have a special check (I couldnt figure out the substring methiod in pythin but thqat would be easier)
        if x == upperLimit:
            if x % 3 == 0:
                ret = ret + "Fizz"
            elif x % 5 == 0:
                ret = ret + "Buzz"
            elif x % 3 == 0 and x % 5 == 0:
                ret = ret + "FizzBuzz"
            elif x % 3 != 0 and x % 5 != 0:
                ret = ret + str(x)
            elif x == 1:
                ret = "1"

        elif x % 3 == 0 and x % 5 == 0:
            ret = ret + "FizzBuzz, "
        elif x % 3 == 0:
            ret = ret + "Fizz, "
        elif x % 5 == 0:
            ret = ret + "Buzz, "
        elif x == 1:
            ret = "1, "
        else:
            ret = ret + str(x) + ", "

    return ret


def start():
    upperLimit = getUpperLimit()
    string = getString(upperLimit)
    print(string)


start()
