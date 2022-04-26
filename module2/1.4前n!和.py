#　用递归求前项阶乘和　５　　１５３
x = eval(input("请输入n："))
def foo(x):
    if x == 1:
        return 1
    else:
        return x*foo(x-1)
sum = 0
for i in range(5,0,-1):
    sum = sum + foo(i)
print(sum)