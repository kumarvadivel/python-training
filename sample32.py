x,y,z=map(int,input().split(","))
if x==y and y==z and x==z:
    sum=(x+y+z)*3
else:
    sum=x+y+z
print(sum)
