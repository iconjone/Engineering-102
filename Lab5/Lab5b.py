class calcObj:
    def __init__(self, xinitial, xfinal, yinitial, yfinal, xwanted):
        self.xinitial = xinitial
        self.xfinal = xfinal
        self.yinitial = yinitial
        self.yfinal = yfinal
        self.xwanted = xwanted


def getPoint(calc):
    slope = (calc.yfinal - calc.yinitial) / (calc.xfinal - calc.xinitial)
    b = calc.yinitial - (slope * calc.xinitial)
    p = (slope * calc.xwanted) + b
    return p


def getCalc(strain):
    if .265 < strain:
        return "The Structural steel has experienced a fracture"
    if 0 <= strain <= .01:
        return calcObj(0, .01, 0, 43, strain)
    if 0.01 < strain <= .06:
        return calcObj(.01, .06, 43, 45, strain)
    if 0.06 < strain <= .18:
        return calcObj(.06, .18, 45, 60, strain)
    if 0.18 < strain <= .265:
        return calcObj(.18, .265, 60, 54, strain)



def getStrain():
    strain = input("Please enter your strain level")
    strain = float(strain)
    if strain < 0 or not strain.isdigit():
        print("You can't have negative strain lol")
        return getStrain()
    else:
        return strain


strain = getStrain()


obj = getCalc(strain)
if type(obj) == str:
    print(obj)
else:
    print("The stress is at " + str(getPoint(obj)))
