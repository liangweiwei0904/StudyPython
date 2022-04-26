# 验证2000以内的正偶数都能分解成两个质数之和
# from math import sqrt
#
#
# def isPrime(x):
#     if x == 1:
#         return False
#     else:
#         k = int(sqrt(x))
#         for i in range(2, k + 1):
#             if x % i == 0:
#                 return False
#         return True
import isPrime

# 2000以内的所有质数
a = []
for i in range(1, 4001):
    if isPrime.isPrime(i):
        a.append(i)
        print(i)

for i in range(2000, 4001, 2):
    flag = 0
    for j in a:
        if i - j in a:
            flag = 1

            break
    if flag == 0:
        print("False", "i=", i, "j=", j)
        break

if flag == 0:
    print("False")
else:
    print("True")
