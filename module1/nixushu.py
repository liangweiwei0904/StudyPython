x = eval(input('逆序数---请输入一个整数：'))
# 9876 % 10 = 6   9876 // 10 = 987
num = 0
while x // 10 != 0:
    r = x % 10
    print('r=',r)
    x = x // 10
    print('x=',x)
    num = num * 10 + r
    print('num=',num)
num = num * 10  + x
print('num=',num)

n = int(input("Enter a number: "))
m = n
s = 0
while n != 0:
    s = s * 10 + n % 10    # 例如n=123时，s在每一轮循环的变化为3，3*10+2=32，32*10+1=321
    n //= 10     # n不断截尾，例如当n=123时，循环从123变化为12，1，0
print("reversed({:d}) = {:d}".format(m, s))     # 字符串的format()方法中参数输出的位置和格式等由其前面字符串中的{}位置和格式(d表示十进制整数)决定