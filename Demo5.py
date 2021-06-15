import threading
import time
bakery = 500
price = 3
c = 0
class Person(threading.Thread):
    username = ""
    money = 0
    num = 0

    def run(self) -> None:
        global bakery, price, c
        while True:
            if bakery > 0:
                bakery -= 1
                self.num += 1
                self.money -= price
                time.sleep(3)
                print(self.username, "成功购买了一块面包")
            else:
                print(self.username, "一共抢到", self.num, "块面包，账户余额为", self.money, "元")
                c += 1
                break

p1 = Person()
p1.username = "张三"
p1.money = 600

p2 = Person()
p2.username = "李四"
p2.money = 600

p3 = Person()
p3.username = "王五"
p3.money = 600

p4 = Person()
p4.username = "赵流"
p4.money = 600

p1.start()
p2.start()
p3.start()
p4.start()

class Chef(threading.Thread):
    username = ""
    num = 0
    def run(self) -> None:
        global bakery, c
        while True:
            if bakery >= 500:
                time.sleep(3)
            elif bakery < 500:
                bakery += 1
                self.num += 1
                time.sleep(3)
                print(self.username,"造了一块面包")
            if bakery >= 500 and c==1:
                print(self.username, "造了",self.num, "个面包")
                break
chef1 = Chef()
chef1.username="66"

chef2 = Chef()
chef2.username="55"

chef3 = Chef()
chef3.username="44"

chef1.start()
chef2.start()
chef3.start()










