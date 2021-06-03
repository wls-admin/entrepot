Friuts = {
	'苹果':12.3,  # 水果和单价
	'草莓':4.5,
    '香蕉':6.3,
    '葡萄':5.8,
    '橘子':6.4,
    '樱桃':15.8
}
info = {
    '小明': {
        'fruits': {'苹果':4, '草莓':13, '香蕉':10},
        'money':0
    },
    '小刚': {
        'fruits': {'葡萄':19, '橘子':12, '樱桃':30},
        'money':0
    }
}
key=Friuts.keys()
ks=info.keys()
for i in ks:
    s = 0
    ity = info[i]['fruits'].keys()
    for j in ity:
        for ke in key:
            h=0
            if j==ke:
                h=h+(info[i]['fruits'][j])*(Friuts[ke])
                s=s+h
    info[i]['money']=s
print(info)
