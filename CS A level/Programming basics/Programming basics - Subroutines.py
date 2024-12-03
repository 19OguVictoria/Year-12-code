def multiples(table, startnum, endnum, pupilname):
    print("Hi, ", pupilname, " here is your times table")
    for i in range(startnum, endnum + 1):
        print(table, " x ", i, " = ", i*table)
        