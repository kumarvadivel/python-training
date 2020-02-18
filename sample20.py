n=int(input())
ini=0
ini1=1
prev=1
print(ini)
print(ini1)
for i in range(1,n-1):
    prev=ini1+ini
    ini=ini1
    ini1=prev
    print(prev)