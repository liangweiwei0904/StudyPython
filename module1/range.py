for i in range(1,10,2):
    print(i,end='\t')

s='python'
for c in s :
    print(c,end=" ")

#索引迭代
for i in range(len(s)) :
    print(s[i],end=" ")

#辗转相除法
x = eval(input('x='))
y = eval(input('y='))
if x < y:
    x,y=y,x
print(x,y)
while x % y != 0:
    r=x%y
    x=y
    y=r
print("最大公约数是：",y)