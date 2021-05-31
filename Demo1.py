import random
commodity=[
    ["Iphone 12 pro", 12000],
    ["HUAWEI watch", 2000],
    ["lenovo PC", 5000],
    ["Mac pc", 13000],
    ["卫龙辣条", 5],
    ["老干妈", 7.5]
]
coupon=["Iphone 12 pro 5折优惠卷!","HUAWEI watch 5折优惠卷!","lenovo PC 5折优惠卷!"
    ,"Mac pc 5折优惠卷!","卫龙辣条 5折优惠卷!","老干妈  5折优惠卷!"]
money=int(input("请输入您的余额："))
shop=[]
c=random.randint(0,5)
print("恭喜您已获得",coupon[c])
i=0
while True:
    for index, value in enumerate(commodity):
        print(index, value)
    num=input("请选择您要购买的商品！")
    if num.isdigit():  # 判断“56” 能不能看成  56
        num = int(num)
        if num > len(commodity)-1:
            print("请输入正确的商品编号！")
        else:
            if money < commodity[num][1]:
                print("您的余额不足，请重新选择商品")
            else:
                if num == c and i == 0:
                    i += 1
                    shop.append(commodity[num])
                    money -= (commodity[num][1]/2)
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

print("您本次的购物情况如下：")
for index,value in enumerate(shop):
    print(index,"",value)
print("您的余额为：￥",money)
b=int(commodity[c][1])
if i==1:
    print("本次使用优惠卷为",coupon[c],"为您节省",b/2)




