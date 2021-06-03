import random
city = {
    "北京":{
        "昌平":{
            "天通苑":["海底捞","呷哺呷哺"],
            "龙泽":["永辉超市","永旺超市"]
        },
        "海淀":{
            "公主坟":["军事博物馆","中华世纪园"],
            "科普场馆":["中国科技馆","北京天文馆"],
            "高校":["北京大学","清华大学"]
        },
        "朝阳":{
            "龙城":["鸟化石国家地质公园","朝阳南北塔"],
            "双塔":["朝阳凌河公园","朝阳凤凰山"]
        }
    },
    "上海":{}
}
commodity=[
    ["可乐", 12],
    ["冰激凌", 120],
    ["薯片", 50],
    ["汉堡", 25],
    ["卫龙辣条", 5],
    ["纪念品", 750]
]
coupon=["可乐 5折优惠卷!","冰激凌 5折优惠卷!","薯片 5折优惠卷!"
    ,"汉堡 5折优惠卷!","卫龙辣条 5折优惠卷!","纪念品  5折优惠卷!"]
c=random.randint(0,5)
shop=[]
i=0
k=0
def print_city(data):
    for i in data:
        print(i)
print("-----------------------欢迎来到不坑你坑谁旅游团---------------------------")
money=int(input("请输入您所带现金："))
if money<10000:
    print("没钱玩个锤子")
else:
    while True:
        print_city(city)
        chose1 = input("请选择您要去城市：")
        if chose1 =="北京":
            num1=random.randint(1000,5000)
            money-=num1
            if num1>=2500:
                print("近日旅游高峰期，本次航班已消费",num1,"账户余额为：",money)
            elif num1<2500:
                print("恭喜您抢到特价机票，本次航班已消费",num1,"账户余额为：",money)
            print_city(city[chose1])
            chose2=input("请选择您要去的区域：")
            if chose2 in city[chose1]:
                print_city(city[chose1][chose2])
                chose3 = input("请选择您要去的地点：")
                if chose3 in city[chose1][chose2]:
                    print_city(city[chose1][chose2][chose3])
                    chose4 = input("请选择您要去的景点：")
                    if chose4 in city[chose1][chose2][chose3]:
                        a=int(input("是否需要购物，如需购物输入1，不购物输入2"))
                        if a==1:
                            while True:
                                if k==0:
                                    print("恭喜您已获得",coupon[c])
                                    k+=1
                                for index, value in enumerate(commodity):
                                    print(index, value)
                                num = input("请选择您要购买的商品；")
                                if num.isdigit():  # 判断“56” 能不能看成  56
                                    num = int(num)
                                    if num > len(commodity) - 1:
                                        print("请输入正确的商品编号！")
                                    else:
                                        if money < commodity[num][1]:
                                            print("您的余额不足，请重新选择商品")
                                        else:
                                            if num == c and i == 0:
                                                i += 1
                                                shop.append(commodity[num])
                                                money -= (commodity[num][1] / 2)
                                                print("购买成功，您本次消费的商品为：", commodity[num], "账户余额为：", money)
                                            else:
                                                shop.append(commodity[num])
                                                money -= commodity[num][1]
                                                print("购买成功，您本次消费的商品为：", commodity[num], "账户余额为：", money)

                                elif num == 'q' or num == 'Q':
                                    print("欢迎下次光临！")
                                    break
                                else:
                                    print("输入非法！请重新输入！")

                        e=input("今日已结束，请输入q进行返回：")
                        if e == 'q' or e == 'Q':
                            print("本次旅行结束！")
                            break

        elif chose1 =="上海":
            if money<=60000:
                print("几个钱呀，够谁花呀！")
                break
            else:
                print("你好土豪")
                num2 = random.randint(1000, 5000)
                money -= num2
                print("不好意思，上海有疫情，为您办理返航","本次收取手续费为：",num2,"账户余额为：",money)
                break

        else:
            num3 = random.randint(1000, 5000)
            money-=num3
            print("输入非法","本次输入扣除手续费：",num3,"账户余额为：",money)
print("您本次的旅游购物情况如下：")
for index,value in enumerate(shop):
    print(index,"",value)
print("您的余额为：￥",money)
b=int(commodity[c][1])
if i==1:
    print("本次使用优惠卷为",coupon[c],"为您节省",b/2)
