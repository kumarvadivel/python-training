n=int(input())
o=n
for i in range(1,n+1):
    e=str(i)+" "
    print(" "*o+e*i)
    o=o-1
o=1
for r in range(n-1,0,-1):
    p=" "+str(r)
    print(" "*o+p*r)
    o=o+1