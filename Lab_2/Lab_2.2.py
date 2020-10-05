import math

def comb(i, n):
    if i > n:
        return 0

    if i == 0 or n == i:
        return 1
    
    if n > i:
        return comb(i, n-1)+comb(i-1, n-1)

def sum(n):
    s = 0
    i = 1
    while i <= n:
        s += comb(i, n)
        i+=1
    return s

n = int(input("Enter n "))
print(sum(n))