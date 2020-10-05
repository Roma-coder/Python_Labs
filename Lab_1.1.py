x = int(input("Enter x"))
e = float(input("Enter e"))
A = []
A.append(x) 
n = 1
if e > 0:
    while n < 100:
        A.append((A[n-1]+1)/(A[n-1]+2))
        if abs(A[n]-A[n-1]) < e:
            print(A[n])
            print(n) 
            break   
        n += 1

