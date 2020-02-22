i=int(input())
for k in range(i,0,-1):
    if k%2==1:
        if i%2==1:
            print("1"*k)
        else:
            print("0"*k)
    else:
        if i%2==1:
            print("0"*k)
        else:
            print("1"*k)