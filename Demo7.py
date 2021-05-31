i=9
while i>=1:
    j=1
    while j<=i:
        print(j,"*",i,"=",(i*j)," ",end="")
        j+=1
    print()
    i-=1