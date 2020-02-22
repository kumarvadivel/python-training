n=int(input())
l=1
p="*"
q=" "
r="* "*(n)
t=len(r)//2
print(r)  
for i in range(1,n-1):
    if i==n:
        print(p)
    elif i<n:
        print(p,q*(t)+"*")
        t=t-1
print("  *")
       

   