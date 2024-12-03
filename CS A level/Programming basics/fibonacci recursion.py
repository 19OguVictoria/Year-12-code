def fibonacci2(n):
    fibnumbers = [0, 1]      #list of first two fibonacci numbers
    # now append the sum of the two previous numbers to the list
    for i in range(2, n):
        fibnumbers. append(fibnumbers[i-1] + fibnumbers[i-2])
    return fibnumbers[n]

x = fibonacci2(8)
print(x)