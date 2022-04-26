# n为偶数，除以2，n为奇数，乘以3加1
n = eval(input("输入正整数n："))
while n != 1:
    if n % 2 == 0:
        print( n, '/2=', n//2)
        n = n // 2
    else:
        print(n,"*3+1=",n * 3 + 1)
        n = n * 3 + 1