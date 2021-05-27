name="root"
password="admin"
a=0
while True:
    name1 = input("请输入您的账号")
    password2 = input("请输入您的密码")
    a=a+1
    if a == 3:
        print("输入账户或者密码3次错误")
        break
    elif name1!=name and password2!=password:
        print("您输入的账号错误")
    else:
        print("登录成功")
        break
