n=int(input())
n=str(n)
count=0
flag=0
fincount=0
for i in range(0,len(n)):
    if n[i]=='1':
        count=count+1
        fincount=fincount+1
        flag=0
    else:
        count=0
        fincount=fincount-1
        flag=-1
if flag==-1:
	print(flag)
else:
	print(fincount)