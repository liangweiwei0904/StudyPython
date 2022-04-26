
n = int(input('Enter a number: '))
print(n, '=', end = ' ')
i = 2      # i是第一个测试的n可能的因子
while n != 1:
    if n % i == 0:    # 把n的所有因子i全部处理完，因为因子可能相同例如8有3个相同的因子2
        n //= i       # 如果n%i等于0表示i是n的因子，因此需要用n//i将此因子去掉
        if n == 1:    # 已判断完，输出最后一个因子，因子后不需要再加*
            print('{:d}'.format(i))
        else:         # 仍然可能有因子，因此输出因子和*
            print('{:d} *'.format(i), end = ' ')
    else:
        i += 1        # 因子i判断并去掉后接着判断下一个数，例如判断完了2接着判断3

x = eval(input('分解质因数---请输入一个整数：'))
i = 2
while x != 1:
    if x % i == 0:
        x = x // i
        print("因子:",i)
    else:
        i= i +1
print('结束')