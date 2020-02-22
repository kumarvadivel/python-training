n=int(input())
l=1
p=" "*n+" *"
q=" "*l+"* "
r=" * "*n
for i in range(n+1,1,-1):
    if i==n:
        print(p)
        p=p[1::]
    elif i<n:
        print(p,q)
        l=l+1
        q=" "*l+q
        p=p[1::]
print(r)  
   

    