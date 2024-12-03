def calcsum(n):
    if n>0:
        n = n + calcsum(n-1)
    return n

print(calcsum(998))