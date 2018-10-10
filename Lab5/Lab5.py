
# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Names: 	Evan Farkas
# 	 		Emmanuel Garcia
# 	 		Tarik Dawson
#			Jonathan Samuel
# Section:		510
# Assignment:	Lab Assignment 5
# Date:		2 10 2018
def getAgeLevelSpecified(ageCalc):
    if 20 <= ageCalc <= 34:
        return 0
    elif 35 <= ageCalc <= 39:
        return 1
    elif 40 <= ageCalc <= 44:
        return 2
    elif 45 <= ageCalc <= 49:
        return 3
    elif 50 <= ageCalc <= 54:
        return 4
    elif 55 <= ageCalc <= 59:
        return 5
    elif 60 <= ageCalc <= 64:
        return 6
    elif 65 <= ageCalc <= 69:
        return 7
    elif 70 <= ageCalc <= 74:
        return 8
    elif 75 <= ageCalc <= 79:
        return 9


def getAgeSpecifiedPoint(gender, ageLevelSpecific):
    male = [-9, 4, 0, 3, 6, 8, 10, 11, 12, 13]
    female = [-7, -3, 0, 3, 6, 8, 10, 12, 14, 16]
    if gender == "MALE":
        return male[ageLevelSpecific]
    if gender == "FEMALE":
        return female[ageLevelSpecific]


def getAgeLevel(ageCalc):
    if 20 <= ageCalc <= 39:
        return 0
    elif 40 <= ageCalc <= 49:
        return 1
    elif 50 <= ageCalc <= 59:
        return 2
    elif 60 <= ageCalc <= 69:
        return 3
    elif 70 <= ageCalc <= 79:
        return 4


def getCholesterolLevel(cholesterolCalc):
    if cholesterolCalc < 160:
        return 0
    elif 160 <= cholesterolCalc <= 199:
        return 1
    elif 200 <= cholesterolCalc <= 239:
        return 2
    elif 240 <= cholesterolCalc <= 279:
        return 3
    elif 280 <= cholesterolCalc:
        return 4


def getCholesterolPoint(gender, ageLevel, cholesterolLevel):
    male = [[0, 4, 7, 9, 11], [0, 3, 5, 6, 8], [0, 2, 3, 4, 5], [0, 1, 1, 2, 3], [0, 0, 0, 1, 1]]
    female = [[0, 4, 8, 11, 13], [0, 3, 6, 8, 10], [0, 2, 4, 5, 7], [0, 1, 2, 3, 4], [0, 1, 1, 2, 2]]
    cholesterolLevel = getCholesterolLevel(cholesterolLevel)
    if gender == "MALE":
        return male[ageLevel][cholesterolLevel]
    if gender == "FEMALE":
        return female[ageLevel][cholesterolLevel]


def getSmokerPoint(gender, smoker, ageLevel):
    if not smoker:
        return 0
    male = [8, 5, 3, 1, 1]
    female = [9, 7, 4, 2, 1]
    if gender == "MALE":
        return male[ageLevel]
    if gender == "FEMALE":
        return female[ageLevel]


def getHDLLevel(hdlCalc):
    if hdlCalc >= 60:
        return 0
    elif 59 >= hdlCalc >= 50:
        return 1
    elif 49 >= hdlCalc >= 40:
        return 2
    elif hdlCalc < 40:
        return 3


def getHdlPoint(HDLLevel):
    arr = [-1, 0, 1, 2]
    return arr[HDLLevel]


def getBPLevel(BPCalc):
    if BPCalc < 120:
        return 0
    elif 120 <= BPCalc <= 129:
        return 1
    elif 130 <= BPCalc <= 139:
        return 2
    elif 140 <= BPCalc <= 159:
        return 3
    elif 160 <= BPCalc:
        return 4


def getBPPoint(gender, BPLevel, BPtreated):
    male = [[0, 0, 1, 1, 2], [0, 1, 2, 2, 3]]
    female = [[0, 1, 2, 3, 4], [0, 3, 4, 5, 6]]
    BPIndex = 0
    if (BPtreated):
        BPIndex = 1
    if gender == "MALE":
        return male[BPIndex][BPLevel]
    if gender == "FEMALE":
        return female[BPIndex][BPLevel]


def getGender():
    genderInput = input(
        "Using the Framingham Point System we will calculate your 10 year risk! \n Please enter your gender!")
    if (str(genderInput) == "Male" or str(genderInput) == "M" or str(genderInput) == "m" or str(
            genderInput) == "MALE" or str(
        genderInput) == "Man" or str(genderInput) == "MAN" or str(genderInput) == "Men" or str(
        genderInput) == "MEN" or str(
        genderInput) == "dude" or str(genderInput) == "bro" or str(genderInput) == "boy" or str(genderInput) == "boi"):
        return "MALE"
    elif (str(genderInput) == "Female" or str(genderInput) == "F" or str(genderInput) == "f" or str(
            genderInput) == "FEMALE" or str(
        genderInput) == "Woman" or str(genderInput) == "WOMAN" or str(genderInput) == "Women" or str(
        genderInput) == "WOMEN" or str(
        genderInput) == "dudette" or str(genderInput) == "girl"):
        return "FEMALE"
    else:
        print("You must enter a gender that is either male or female... Try again")
        return getGender()


def getAge():
    ageInput = input(
        "Please enter your Age - If it has a decimal it will be converted into a Whole Number")
    if ageInput.isdigit() or ageInput.isdecimal():
        ageInput = int(ageInput)
    else:
        print("You did not enter a number - Are you dumb? Try again")
        return getAge()

    if (20 <= ageInput <= 79):
        return ageInput
    else:
        print(
            "Sorry - age must be between 20 and 79... if You're below 20 stop worrying and if you're above 79... start praying?")
        return getAge()


def getCholesterol():
    cholesterolInput = input(
        "Please enter your cholesterol level - If it has a decimal it will be converted into a Whole Number")
    if cholesterolInput.isdigit() or cholesterolInput.isdecimal():
        return int(cholesterolInput)
    else:
        print("You did not enter a number - Are you dumb? Try again")
        return getCholesterol()


def isSmoker():
    status = input("Are you a smoker?")
    if (
            status == "Yes" or status == "YES" or status == "Y" or status == "Yah" or status == "Yeah" or status == "YEAH" or status == "y" or status == "yup"):
        return True
    if (
            status == "Np" or status == "NO" or status == "N" or status == "Nah" or status == "Nay" or status == "NAY" or status == "n"):
        return False
    else:
        print("You must say yes or no... try again")
        return isSmoker()


def getHDL():
    HDLInput = input(
        "Please enter your HDL level - If it has a decimal it will be converted into a Whole Number")
    if HDLInput.isdigit() or HDLInput.isdecimal():
        return int(HDLInput)
    else:
        print("You did not enter a number - Are you dumb? Try again")
        return getHDL()


def getBP():
    BPInput = input(
        "Please enter your Systolic BP level - If it has a decimal it will be converted into a Whole Number")
    if BPInput.isdigit() or BPInput.isdecimal():
        return int(BPInput)
    else:
        print("You did not enter a number - Are you dumb? Try again")
        return getBP()


def isTreated():
    status = input("Are you a BP Treated?")
    if (
            status == "Yes" or status == "YES" or status == "Y" or status == "Yah" or status == "Yeah" or status == "YEAH" or status == "y" or status == "yup"):
        return True
    if (
            status == "Np" or status == "NO" or status == "N" or status == "Nah" or status == "Nay" or status == "NAY" or status == "n"):
        return False
    else:
        print("You must say yes or no... try again")
        return isTreated()


def getRisk(point, gender):
    if gender == "MALE" and (point < 0 or point >= 17):
        if(point<0):
            return "less than 1"
        if(point>=17):
            return "greater than or equal to 30"
    if gender == "FEMALE" and (point < 9 or point >= 25):
        if (point < 9):
            return "less than 1"
        if (point >= 25):
            return "greater than or equal to 30"
    malerisk = {
        "0": 1,
        "1": 1,
        "2": 1,
        "3": 1,
        "4": 1,
        "5": 2,
        "6": 2,
        "7": 3,
        "8": 4,
        "9": 5,
        "10": 6,
        "11": 8,
        "12": 10,
        "13": 12,
        "14": 16,
        "15": 20,
        "16": 25
        }
    femalerisk = {
        "9": 1,
        "10": 1,
        "11": 1,
        "12": 1,
        "13": 2,
        "14": 2,
        "15": 3,
        "16": 4,
        "17": 5,
        "18": 6,
        "19": 8,
        "20": 11,
        "21": 14,
        "22": 17,
        "23": 22,
        "24": 27
    }
    if gender == "MALE":
        return malerisk[str(point)]
    if gender == "FEMALE":
        return femalerisk[str(point)]


gender = getGender()

age = getAge()

cholesterol = getCholesterol()

smoker = isSmoker()

hdl = getHDL()

bp = getBP()

treated = isTreated()

point = getAgeSpecifiedPoint(gender, getAgeLevelSpecified(age)) + getCholesterolPoint(gender, getAgeLevel(age),
                                                                                      getCholesterolLevel(
                                                                                          cholesterol)) + getSmokerPoint(
    gender, smoker, getAgeLevel(age)) + getHdlPoint(getHDLLevel(hdl)) + getBPPoint(gender, getBPLevel(bp), treated)


risk = getRisk(point, gender)


print("You are at a risk of " + str(risk) + " percent.")

