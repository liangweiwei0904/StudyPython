# 验证命题的正确性
flag = 1
for i in range(111,1000,37):
    # 第一次左移
    r = ( i % 100 ) * 10
    x = i // 100 + r
    if x % 37 != 0:
        flag = 0
        print("False")
        break
    else:
        # 第二次左移
        r = ( i % 10 ) * 100
        x = i // 10 + r
        if x % 37 != 0:
            flag = 0
            print("False")
            break
if flag == 1:
    print("命题正确")
else:
    print("命题不正确")