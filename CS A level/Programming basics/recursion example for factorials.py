#recursive function to find factorial n
def calcFactorial(n):
    print("n =",n)
    if n == 0:
        factorial = 1
    else:
        factorial = n * calcFactorial(n-1)
    print("At A ",factorial)                #line A
    return factorial
#end sub

#main body
x = calcFactorial(500)
print("At B ",x)                            #line B