from DBUtils import select,update,relaseConnect
import random
print(
    "        ´´´´´´´´██´´´´´´´\r\n" +
    "        ´´´´´´´████´´´´´´\r\n" +
    "        ´´´´´████████´´´´\r\n" +
    "        ´´`´███▒▒▒▒███´´´´´\r\n" +
    "        ´´´███▒●▒▒●▒██´´´\r\n" +
    "        ´´´███▒▒▒▒▒▒██´´´´´\r\n" +
    "        ´´´███▒▒▒▒██´                      项目：中国工商银行\r\n" +
    "        ´´██████▒▒███´´´´´                 语言： Python3.8.2\r\n" +
    "        ´██████▒▒▒▒███´´                   辑器： PyCharm\r\n" +
    "        ██████▒▒▒▒▒▒███´´´´                版本控制： Git\r\n" +
    "        ´´▓▓▓▓▓▓▓▓▓▓▓▓▓▒´´                 数据库:  mysql\r\n" +
    "        ´´▒▒▒▒▓▓▓▓▓▓▓▓▓▒´´´´´\r\n" +
    "        ´.▒▒▒´´▓▓▓▓▓▓▓▓▒´´´´´              \r\n" +
    "        ´.▒▒´´´´▓▓▓▓▓▓▓▒                   \r\n" +
    "        ..▒▒.´´´´▓▓▓▓▓▓▓▒                  \r\n" +
    "        ´▒▒▒▒▒▒▒▒▒▒▒▒                      \r\n" +
    "        ´´´´´´´´´███████´´´´´              \r\n" +
    "        ´´´´´´´´████████´´´´´´´\r\n" +
    "        ´´´´´´´█████████´´´´´´\r\n" +
    "        ´´´´´´██████████´´´´             大部分人都在关注你飞的高不高，却没人在乎你飞的累不累，这就是现实！\r\n" +
    "        ´´´´´´██████████´´´                     我从不相信梦想，我，只，相，信，自，己！\r\n" +
    "        ´´´´´´´█████████´´\r\n" +
    "        ´´´´´´´█████████´´´\r\n" +
    "        ´´´´´´´´████████´´´´´\r\n" +
    "        ________▒▒▒▒▒\r\n" +
    "        _________▒▒▒▒\r\n" +
    "        _________▒▒▒▒\r\n" +
    "        ________▒▒_▒▒\r\n" +
    "        _______▒▒__▒▒\r\n" +
    "        _____ ▒▒___▒▒\r\n" +
    "        _____▒▒___▒▒\r\n" +
    "        ____▒▒____▒▒\r\n" +
    "        ___▒▒_____▒▒\r\n" +
    "        ███____ ▒▒\r\n" +
    "        ████____███\r\n" +
    "        █ _███_ _█_███\r\n" +
    "——————————————————————————女神保佑，代码无bug——————————————————————")

# 银行的库
names = {}

# 开户行名称
bank_name = "中国工商银行昌平支行"

# 欢迎页面的模板
welcome = '''
    -----------------------------------------
    -     欢迎来到中国工商银行账户管理系统     -
    -----------------------------------------
    -   1.开户                               -
    -   2.存钱                               -
    -   3.取钱                               -
    -   4.转账                               -
    -   5.查询                               -
    -   6.Bye!                               -
    ------------------------------------------
'''

def getRandom():
    li = ["1","2","3","4","5","6","7","8","9","0","a","b","c","d","e","f"]
    string = ""
    for i in range(8):
        ch = li[random.randint(0,len(li) - 1)]
        string = string +  ch
    return string

# 银行的开户逻辑
def bank_addUser(account,username,password,money,country,province,street,door,bank_name):
    # 1.判断是否已满
    # if len(names)  >= 100:
    #     return 3
    # # 2.判断是否存在:用户名是否重复
    # if username in names:
    #     return 2
    # # 3.开户
    # names[username] = {
    #     "account":account,
    #     "username":username,
    #     "password":password,
    #     "money":money,
    #     "country":country,
    #     "province":province,
    #     "street":street,
    #     "door":door,
    #     "bank_name":bank_name
    # }
    # return 1
    sql1="select * from bank"
    p=[]
    f1=select(sql1, p)
    if len(f1) >= 100:
        return 3

    sql2 = "select * from bank where username=%s"
    p1 = [username]
    f2 = select(sql2, p1)
    if len(f2) == 1:
        return 2

    sql3="insert into bank values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    p2=(username,password,account,money,country,province,street,door,bank_name)
    update(sql3,p2)
    return 1


# 开户操作
def addUser():
    username = input("请输入您的姓名：")
    password = input("请输入你的密码：")
    money = int(input("请输入您的账户余额：")) # "123"  123
    print("下面请输入您的个人地址信息：")
    country = input("请输入您的国籍：")
    province =  input("请输入您的省份：")
    street = input("请输入您的居住街道：")
    door = input("请输入您的门牌号：")
    account = getRandom()
    status = bank_addUser(account,username,password,money,country,province,street,door,bank_name)
    if status == 1:
        print("恭喜开户成功！以下是您的个人信息：")
        info = '''
            ----------个人信息 【工商银行】--------
            用户名：%s,
            密码：%s,
            账号：%s,
            余额：%s,
            国家：%s,
            省份：%s,
            街道:%s,
            门牌号：%s
            开户行名称：%s
            ------------------------------------
        '''
        print(info % (username,password,account,money,country,province,street,door,bank_name))

    elif status == 2:
        print("对不起，您的账户已存在！请勿重复开户！")
    elif status == 3:
        print("对不起，用户库已满，请携带证件到其他银行办理！")

# 存钱操作
def addmoney():
    usernmae=input("请输入您的用户名：")
    money=int(input("请输入您要存入的金额："))
    b_m=bank_money(usernmae,money)
    if b_m ==False:
        print("您输入的账户不存在！")

# 银行存钱逻辑
def bank_money(username,money):
    # m=0
    # if username in names:
    #     m=money+names[username]['money']
    #     names[username]['money']=m
    #     print("恭喜您存款成功，当前账户余额为",names[username]['money'])
    sql1="select * from bank where username=%s"
    p1=[username]
    s1=select(sql1,p1)
    if len(s1)==1:
        sql2="update bank set balace = balace+%s where username=%s"
        p2 = [money,username]
        update(sql2,p2)

        sql3="select balace from bank where username=%s"
        p3= [username]
        print("恭喜您存款成功，当前账户余额为", select(sql3, p3))
        return True
    else:
        return False

# 取钱操作
def deletemoney():
    username=input("请输入您的用户名：")
    password=input("请输入您的密码：")
    dmoney=int(input("请输入您取款金额："))
    bdm=bank_delete_money(username,password,dmoney)
    if bdm==1:
        print("您输入的用户名不正确！")
    elif bdm==2:
        print("您输入的密码不正确！")
    elif bdm==3:
        print("您账户的余额已不足！")

# 银行取钱逻辑
def bank_delete_money(username,password,money):
    # if username not in names:
    #     return 1
    # if password not in names[username]["password"]:
    #     return 2
    # if money > names[username]["money"]:
    #     return 3
    # m=0
    # m=names[username]['money']-money
    # names[username]['money'] = m
    # print("恭喜您存款成功，当前账户余额为", names[username]['money'])
    # return 0
    sql1 = "select * from bank where username=%s"
    p1 = [username]
    s1 = select(sql1, p1)
    if len(s1) == 0:
        return 1

    sql2 = "select * from bank where username=%s and password=%s"
    p2 = [username, password]
    s2 = select(sql2, p2)
    if len(s2) == 0:
        return 2

    sql3 = "select * from bank where balace > %s and username=%s"
    p3 = [money, username]
    s3 = select(sql3, p3)
    if len(s3) == 0:
        return 3

    sql4 = "update bank set balace = balace - %s where username = %s"
    p4 = [money, username]
    update(sql4, p4)

    sql5 ="select balace from bank where username=%s"
    p5 = [username]
    s5 = select(sql5, p5)
    print("恭喜您取款成功，当前账户余额为", s5[0])
    return 0

# 转账操作
def transfermoney():
    username1=input("请输入转入账户：")
    username2=input("请输入转出账户：")
    password=input("请输入转出密码：")
    money=int(input("请输入转出金额："))
    btm=bank_transfer_money(username1,username2,password,money)
    if btm==1:
        print("您输入的转入账户不存在！")
    elif btm==2:
        print("您输入的转出账户不存在！")
    elif btm==3:
        print("您输入的转出账户密码不正确！")
    elif btm==4:
        print("您账户的余额已不足！")

# 银行转账逻辑
def bank_transfer_money(username1,username2,password,money):
    # if username1 not in names and username2 not in names:
    #     return 1
    # if password not in names[username2]["password"]:
    #     return 2
    # if money > names[username2]["money"]:
    #     return 3
    # m1 = 0
    # m2 = 0
    # m1 = names[username2]['money'] - money
    # names[username2]['money'] = m1
    # m2=names[username1]['money']+money
    # names[username1]['money']=m2
    # print("恭喜您转账成功",username1,"账户余额为",names[username1]['money'])
    # return 0
    sql1 = "select * from bank where username=%s"
    p1 = [username1]
    s1=select(sql1, p1)
    if len(s1)==0:
        return 1

    sql2 = "select * from bank where username=%s"
    p2 = [username2]
    s2=select(sql2, p2)
    if len(s2)==0:
        return 2

    sql3= "select * from bank where username=%s and password=%s"
    p3 = [username2, password]
    s3 = select(sql3, p3)
    if len(s3) == 0:
        return 3

    sql4 = "select * from bank where balace > %s and username=%s"
    p4 = [money, username2]
    p4 = select(sql4, p4)
    if len(p4) == 0:
        return 4

    sql5 = "update bank set balace=balace-%s where username=%s"
    p5 = [money, username2]
    update(sql5, p5)
    sql6 = "update bank set balace=balace+%s where username=%s"
    p6 = [money, username1]
    update(sql6, p6)

    sql7 = "select balace from bank where username=%s"
    p7 = [username2]
    s7 = select(sql7, p7)

    sql8 = "select balace from bank where username=%s"
    p8 = [username1]
    s8 = select(sql8, p8)

    print("恭喜您转账成功，转出账户余额为：",s7,"转入账户余额为：",s8)
    return 0


# 查询操作
def selectusername():
    username=input("请输入您的用户名：")
    password=input("请输入您的密码：")
    bsu=bank_select_username(username,password)
    if bsu==1:
        print("您输入的账户错误")
    if bsu==2:
        print("您输入的密码错误")

# 银行查询逻辑
def bank_select_username(username,password):
    # if username not in names:
    #     return 1
    # if password not in names[username]["password"]:
    #     return 2
    sql1 = "select * from bank where username=%s"
    p1 = [username]
    s1 = select(sql1, p1)
    if s1==0:
        return 1

    sql2 = "select * from bank where username=%s and password=%s"
    p2 = [username, password]
    s2 = select(sql2, p2)
    if s2==0:
        return 2


    # info = '''
    #     ----------个人信息 【工商银行】--------
    #     用户名：%s,
    #     密码：%s,
    #     账号：%s,
    #     余额：%s,
    #     国家：%s,
    #     省份：%s,
    #     街道:%s,
    #     门牌号：%s
    #     开户行名称：%s
    #     ------------------------------------
    # '''
    # print(info % (username, password, names[username]['account'], names[username]['money'], names[username]['country']
    # , names[username]['province'], names[username]['street'], names[username]['door'], bank_name))

    sql3 = "select * from bank where username=%s"
    p3 = [username]
    s3 = select(sql3, p3)
    print(s3)
    return 0

# 入口程序
while True:
    print(welcome)
    chose = input("请输入您的业务编号：")
    if chose == '1':
        addUser()
    elif chose == '2':
        addmoney()
    elif chose == '3':
        deletemoney()
    elif chose == '4':
        transfermoney()
    elif chose == '5':
        selectusername()
    elif chose == '6':
        relaseConnect()
        break
    else:
        print("输入非法！别瞎弄！")