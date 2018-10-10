# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Names: 	Evan Farkis
# 	 		Emmanuel Garcia
# 	 		Tarik Dawson
#			Jonathan Samuel
# Section:		510
# Assignment:	Lab Assignment 4
# Date:		25 09 2018

# 8 Different Roundoff Errors
import math

tol = .00001

# 1
num1 = 1 / 12
theo1 = num1 * 12
x = num1 * 5
y = num1 * 7
exp1 = x + y
tf1 = exp1 == theo1
print("Is " + str(theo1) + " within tolerance of  " + str(exp1) + " " + str(abs(theo1 - exp1) <= tol))

# 2
num2 = 78 / 2
theo2 = num2 * 13
x = num2 * 6
y = num2 * 7
exp2 = x + y
tf2 = exp2 == theo2
print("Is " + str(theo2) + " within tolerance of  " + str(exp2) + " " + str(abs(theo2 - exp2) <= tol))

# 3
num3 = 1 / 10
theo3 = num3 ** 4
x = num3 ** (3 / 2)
y = num3 ** (5 / 2)
exp3 = x * y
tf3 = exp3 == theo3
print("Is " + str(theo3) + " within tolerance of  " + str(exp3) + " " + str(abs(theo3 - exp3) <= tol))

# 4
num4 = 78 / 2
theo4 = num4 ** 4
x = num4 ** (3 / 2)
y = num4 ** (5 / 2)
exp4 = x * y
tf4 = exp4 == theo4
print("Is " + str(theo4) + " within tolerance of  " + str(exp4) + " " + str(abs(theo4 - exp4) <= tol))

# 5
num5 = 67349
theo5 = (num5 ** (7 / 2)) / (34 / 32)
x = num5 ** (2 / 2)
y = num5 ** (10 / 4)
a = (3 / 16)
b = 28 / 32
bottom = a + b
exp5 = x * y
exp5 = exp5 / bottom
tf5 = exp5 == theo5
print("Is " + str(theo5) + " within tolerance of  " + str(exp5) + " " + str(abs(theo5 - exp5) <= tol))

# 6
num6 = 64234
theo6 = (num6 ** (4 / 9)) / (2 / 16)
x = num6 ** (1 / 3)
y = num6 ** (1 / 9)
a = (1 / 32)
b = 3 / 32
bottom = a + b
exp6 = x * y
exp6 = exp6 / bottom
tf6 = exp6 == theo6
print("Is " + str(theo6) + " within tolerance of  " + str(exp6) + " " + str(abs(theo6 - exp6) <= tol))

# 7
theo7 = 5 * 10
x = math.sqrt(10)
exp7 = 5 * x ** 2
tf7 = exp7 == theo7
print("Is " + str(theo7) + " within tolerance of  " + str(exp7) + " " + str(abs(theo7 - exp7) <= tol))

# 8
num8 = 84234
theo8 = (num8 ** (4 / 9)) / (2 / 16)
x = num8 ** (1 / 3)
y = num8 ** (1 / 9)
a = (1 / 32)
b = 3 / 32
bottom = a + b
exp8 = x * y
exp8 = exp8 / bottom
tf8 = exp8 == theo8
print("Is " + str(theo8) + " within tolerance of  " + str(exp8) + " " + str(abs(theo8 - exp8) <= tol))

# 9
num9 = 734 / 2
theo9 = num9 ** 6
x = num9 ** (3 / 2)
y = num9 ** (9 / 2)
exp9 = x * y
tf9 = exp9 == theo9
print("Is " + str(theo9) + " within tolerance of  " + str(exp9) + " " + str(abs(theo9 - exp9) <= tol))

# 10
theo10 = 5 * 12
x = math.sqrt(12)
exp10 = 5 * x ** 2
tf10 = exp10 == theo10
print("Is " + str(theo10) + " within tolerance of  " + str(exp10) + " " + str(abs(theo10 - exp10) <= tol))

print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")

tol = .0000000000001

x = 5 * 12
q = math.sqrt(12)
y = 5 * q ** 2


num = 84234
a = (num ** (4 / 9)) / (2 / 16)
c = num ** (1 / 3)
d = num ** (1 / 9)
e = (1 / 32)
f = 3 / 32
bottom = e + f
b = c * d
b = b / bottom



print("a:" + str(a))
print("b:" + str(b))
print("x:" + str(x))
print("y:" + str(y))
print("tolerance:" + str(tol))

print("A and B is within tolerance:" + str(abs(a - b) <= tol))
print("X and Y is within tolerance:" + str(abs(x - y) <= tol))



