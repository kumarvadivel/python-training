#sympy module  print count of prime nos
import sympy
l,r=map(int,input().split())
count=0
for i in range(l,r+1):
    if sympy.isprime(i):
        count=count+1
print(count," no if prime nos between ",l," to", r)
    