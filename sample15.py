# co-prime logic 
import math
x,y=map(int,input().split())
gc=math.gcd(x,y)
if gc==1:
    print("co-prime")
else:
    print("not a coprime")
