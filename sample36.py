x,y,z=map(int,input().split(","))
if x==y or y==z or z==x:
    print("0")
else:
    print(x+y+z)