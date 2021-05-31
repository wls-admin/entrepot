yw=["小明","小张","小黄","小杨"]
sx=["小黄","小李","小王","小杨","小周"]
yy=["小杨","小张","小吴","小冯","小周"]
p=[]
b=[]
c=[]
d=[]
e=[]
num=0
num2=0
num3=0
size=0
for i in yw:
    d.append(i)
    if i not in p:
        p.append(i)
        b.append(i)
        num+=1
        size+=1
    if i not in c:
        num2+=1
        c.append(i)
for i in sx:
    d.append(i)
    if i not in p:
        p.append(i)
        num += 1
for i in yy:
    d.append(i)
    if i not in p:
        p.append(i)
        num += 1
    if i not in c:
        c.append(i)
        num2+=1
for i in range(0,len(d)):
    count = 0
    if d[i] in d[:i] :
        continue
    for j in range(0,len(d)):
        if d[i] == d[j] :
            count = count + 1
    if count==1:
        e.append(d[i])
print("选修课学生共有",num,"名")
print("选择第一学科的数量为",size,"名,名字为",b)
print("只选了一门学科的学生的数量为",len(e),"名，名字为",e)
print("只选了语文和英语的学生的数量为",num2,"名对应的名字为",c)


