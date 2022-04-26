from math import sqrt
def isprime(x):
    if x == 1:
        return False
    k = int(sqrt(x))
    for j in range(2, k + 1):
        if x % j == 0:
            return False
    else:
        return True
print(isprime(1))

def isPrime(x):
    if x == 1:
        return False
    else:
        k = int(sqrt(x))
        for i in range(2,k+1):
            if x % i == 0:
                return False
        return True
for m in range(2,20):
    if isPrime(m):
        print('素数',m)

