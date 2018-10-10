def getProductions():
    day = 0
    ret =[]
    end = False
    while not end:
        day = day + 1
        measurement = float(input("Please enter widget production for day " + str(day) + " or negative number to end program"))
        if measurement < 0:
            end = True
        ret.append(measurement)

    if end:
        return ret

