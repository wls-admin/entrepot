import random
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
def bank_addUser(account,username,password,money,country,province,street,door):
    # 1.判断是否已满
    if len(names)  >= 100:
        return 3
    # 2.判断是否存在:依据是用户名
    if username in names:
        return 2
    # 3.开户
    names[username] = {
        "account":account,
        "username":username,
        "password":password,
        "money":money,
        "country":country,
        "province":province,
        "street":street,
        "door":door,
        "bank_name":bank_name
    }
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
    status = bank_addUser(account,username,password,money,country,province,street,door)
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
    m=0
    if username in names:
        m=money+names[username]['money']
        names[username]['money']=m
        print("恭喜您存款成功，当前账户余额为",names[username]['money'])
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
    if username not in names:
        return 1
    if password not in names[username]["password"]:
        return 2
    if money > names[username]["money"]:
        return 3
    m=0
    m=names[username]['money']-money
    names[username]['money'] = m
    print("恭喜您存款成功，当前账户余额为", names[username]['money'])
    return 0

# 转账操作
def transfermoney():
    username1=input("请输入转出账户：")
    username2=input("请输出转出账户：")
    password=input("请输出转出密码：")
    money=int(input("请输出转出金额："))
    btm=bank_transfer_money(username1,username2,password,money)
    if btm==1:
        print("您输入的用户名不正确！")
    elif btm==2:
        print("您输入的密码不正确！")
    elif btm==3:
        print("您账户的余额已不足！")

# 银行转账逻辑
def bank_transfer_money(username1,username2,password,money):
    if username1 not in names and username2 not in names:
        return 1
    if password not in names[username2]["password"]:
        return 2
    if money > names[username2]["money"]:
        return 3
    m1 = 0
    m2 = 0
    m1 = names[username2]['money'] - money
    names[username2]['money'] = m1
    m2=names[username1]['money']+money
    names[username1]['money']=m2
    print("恭喜您转账成功",username1,"账户余额为",names[username1]['money'])
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
    if username not in names:
        return 1
    if password not in names[username]["password"]:
        return 2
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
    print(info % (username, password, names[username]['account'], names[username]['money'], names[username]['country']
    , names[username]['province'], names[username]['street'], names[username]['door'], bank_name))
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
        break
    else:
        print("输入非法！别瞎弄！")