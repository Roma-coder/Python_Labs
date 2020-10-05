import numpy as np

import random

def countС(row):
    sum = 0
    for x in row: 
        if x < 0: 
            sum += abs(x)
    return sum

n = int(input('Enter n: '))
A = np.array([[random.randrange(-10, 10) for j in range(n)] for i in range(n)])
print(A)
print("---------------------------------")
B = np.array(sorted(A.tolist(), key=countС))
print(B)