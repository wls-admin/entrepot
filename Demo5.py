a=[1,5,21,30,15,9,30,24]
b=len(a)
h=0
while b>=0:
    if a[b-1]%5==0:
        h+=a[b-1]
    b=b-1
print(h)