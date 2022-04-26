# BMI=体重/身高的平方  kg/m2
# weight=eval(input('体重：'))
# height=eval(input('身高：'))
weight,height=eval(input())
BMI=weight/(height**2)
print('weight=',weight,'height=',height,'BMI=',BMI,end='')
if BMI < 18.5:
    print("过轻")
elif 18.5<=BMI <=23.9:
    print("正常")
elif 24<=BMI<=27.9:
    print("过重")
else:
    print("肥胖")