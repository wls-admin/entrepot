dict = {"k1":"v1","k2":"v2","k3":"v3"}
num=dict.keys()
for i in dict:
    print(i)
for j in num:
    print(dict.get(j))
dict["k4"]="v4"
print(dict)