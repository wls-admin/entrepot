students = [
    {'name':'张三','age':23,'score':88,'tel':'23423532','gender':'男'},
    {'name':'李四','age':26,'score':80,'tel':'12533453','gender':'女'},
    {'name':'王五','age':15,'score':58,'tel':'56453453','gender':'男'},
    {'name':'赵六','age':16,'score':57,'tel':'86786785','gender':'保密'},
    {'name':'小明','age':18,'score':98,'tel':'23434656','gender':'女'},
    {'name':'小红','age':23,'score':72,'tel':'67867868','gender':'女'},
]
# 1) 统计不及格学生的个数
for i in students:
    if i['score']<60:
        print(i['name'])
# 打印不及格学生的名字和对应的成绩
for i in students:
    if i['score']<60:
        print(i['name'],i['score'])
# 3) 统计未成年学生的个数
for i in students:
    if i['age']<18:
        print(i['name'])
# 4) 打印手机尾号是8的学生的名字
for i in students:
    if int(i['tel'])%10==8:
        print(i['name'])
# 5) 打印最高分和对应的学生的名字
f = ""
for i in students:
    for j in students:
        if i['score']<j['score']:
            f=j['name']
    break
print(f)
# 6) 将列表按学生成绩从大到小排序
maxscore=students[0].get('score')
num=0
for i in range(0,len(students)):
    for j in range(i+1,len(students)):
        if students[j].get('score')>maxscore:
            maxscore=students[j].get('score')
            num=j
    students[i],students[num]=students[num],students[i]
print(students)
# 7) 删除性别保密的所有学生
for i in students:
    if i['gender']=='保密':
        students.remove(i)
print(students)






