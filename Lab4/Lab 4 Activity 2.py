# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: 		Jonathan Samuel
# Section:		510
# Assignment:	Lab 4 Activity 2
# Date:		    9 25 2018

a = input("Please Enter in either true or false for the Value A")
a = str(a)
if a.capitalize() == "T" or a.capitalize() == "TRUE" or a == "1":
    a = True
else:
    a = False

b = input("Please Enter in either true or false for the Value B")
b = str(b)
if b.capitalize() == "T" or b.capitalize() == "TRUE" or b == "1":
    b = True
else:
    b = False

c = input("Please Enter in either true or false for the Value C")
c = str(c)
if c.capitalize() == "T" or c.capitalize() == "TRUE" or c == "1":
    c = True
else:
    c = False

print("1:" + str(a and b and c))
print("2:" + str(a or b or c))
print("3:" + str((not (a and not b) or (not c and b)) and (not b) or (not a and b and not c) or (a and not b)))
# !((a & !b) || (!c & b)) & (! b) || (!a & b & !c) || (a & !b))
print("4" + str((not ((b or not c) and (not a or not c))) or (not (c or not (b and c))) or (a and not c) and (not a or (a and b and c) or (a and ((b and not c) or (not b))))))
# (!((b || !c) & (!a || !c))) || (!(c || !(b & c))) || (a && !c) & (!a || (a & b & c) or (a & ((b & ! c) or (! b)))))
print("5:" + str((a or b) and not (a == b)))
print("6:" + str((not (b and c) or (c and a) or (a and b))))
# (!(a &! b) || (!c & b ) & !b || (!a & b & !c) || (a & !b)
# !a & b or                !b || !(a & c) & b
# !(a||c) & b
# (!(a||c) & b ) & !b || (!a & b & !c) || (a & !b)
#                         !(a&c) & b || (a&!b)
#
print("7:" + str((not a and not c) or not b))
# (!((b || !c) & (!a || !c))) || (!(c || !(b & c))) || (a && !c) & (!a || (a & b & c) or (a & ((b & ! c) or (! b)))))
#  (!b&a||c) || (!c || b and c) || !a ||
print("8:" + str(a or(not b and c)))

