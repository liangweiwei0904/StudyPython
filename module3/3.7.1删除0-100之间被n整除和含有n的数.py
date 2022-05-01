n = eval(input("请输入一个数（1-9）："))
count = 0
for i in range(101):
    if i % 6 != 0 and str(n) not in str(i):
        count+=1
        print(i,end=",")
        if count % 10 ==0:
            print("\n")