l=input()
l=l.split()
f=[]
for i in range(0,len(l)):
    if int(l[i])%2==0:
        f.append(l[i])
print(f)