i=0
while i<=7:
    x = 7
    while x>=i:
        j = 0
        print(" ",end="")
        x-=1
    while j<=i:
        print("* ",end="")
        j+=1
    print()
    i += 1