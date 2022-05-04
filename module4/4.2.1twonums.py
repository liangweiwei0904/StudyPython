def twonums(n,lst):
    flag = 0
    for xbi,i in enumerate(lst):
        if flag == 1:
            break
        for xbj,j in enumerate(lst):
            if i + j == n:
                print(i,"+",j,"下标为：",xbi,xbj)
                flag = 1
                break
    else:
        if flag == 0:
            print("没找到")
lst = [1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 18, 19, 20, 21, 29, 34, 54, 65]
n = eval(input("input n: "))
twonums(n,lst)

