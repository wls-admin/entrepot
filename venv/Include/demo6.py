import random

num1=random.randint(0,100)

a=0
b=5000

while True:
    a=a+1
    if a == 11:
        print("账户余额不足")
        break
    b=b-500
    num2=int(input("请输入1-100的数字："))
    if num2>num1:
        print("大了")
    elif num2 < num1:
        print("小了")
    else:
        if num2==num1:
            b=b+200
        print("恭喜您猜对了,一共输入",a,"次","账户余额为：",b)
        break

