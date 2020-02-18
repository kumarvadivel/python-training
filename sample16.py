#program to find strong number
import math
i=int(input())
j=str(i)
sum=0
for z in range(0,len(j)):
    w=int(j[z])
    q=math.factorial(w)
    sum=sum+q
    
if sum==i:
    print(i,"is a strong number")
else:
    print(i,"is not a strong number")