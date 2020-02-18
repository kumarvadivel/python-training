n=int(input())
x=int(input())
sum=1.0
for i in range(2,n+1):
    sum=sum+(x**i)/i
print(round(sum,2))