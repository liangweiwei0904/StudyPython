# 1、2、3、4 组成的无重复3位数，从小到大输出
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if i!=j and j!=k and i!= k:
                print(i,j,k)