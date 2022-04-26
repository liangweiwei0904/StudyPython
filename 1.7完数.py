
for i in range(1,1001):
    sum = 0
    # 求因子
    for j in range(1,i//2+1):
        if i % j == 0:
            sum = sum + j
            #print("sum",sum)
    if sum == i :
        print("完数：",sum)