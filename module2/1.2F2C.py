# 将华氏度转换成摄氏度  C=1.8*(F-32)
F = eval(input("请输入华氏度F的值："))
def F2C(x):
    return 1.8 * (x- 32)

print("转换后的摄氏度值为：",F2C(F))
print("华氏度与摄氏度对照表")
for i in range(0,301,20):
    print("F:",i,'C:',F2C(i))