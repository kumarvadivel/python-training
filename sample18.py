x,y=map(int,input().split())
sumx=0
sumy=0
for i in range(1,x):
    if(x%i==0):
        sumx=sumx+i
for j in range(1,y):
    if(y%j==0):
        sumy=sumy+j
if sumx==y:
    print(x,"and ",y,"are amicable numbers")
elif sumy==x:
    print(x,"and ",y,"are amicable numbers")
else:
    print(x,"and ",y,"are not amicable numbers")