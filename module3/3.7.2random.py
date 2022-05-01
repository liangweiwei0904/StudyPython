import random

a=[]
for i in range(500):
    t=str(random.randint(1,100))
    a.append(t)
b="\n".join(a)

with open("random.txt",mode="w") as f:
    f.write(b)
# with open("random.txt",mode='r') as f:
#     f.readlines()
# 找众数
print("500个数为：",a)
setNums=set(a)
lst=[0]*101
for i in setNums:
    c= a.count(i)

    lst[int(i)]=c
for i in range(len(lst)):
    if lst[i]==max(lst):
        print(i)

for i in a:
    print(i,"出现的次数",a.count(i))