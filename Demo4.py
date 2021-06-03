# 编写一个函数，传入一个列表，并统计每个数字出现的次数。返回字典数据：{21:3,56:9,10:3}
def statistics(list):
    b = {}
    for i in list:
        k=0
        for j in list:
            if i == j:
                k+=1
        b[i]=k
    return b

a=[1,4,7,5,8,2,1,3,4,5,9,7,6,1,10]
zidian=statistics(a)
print(zidian)