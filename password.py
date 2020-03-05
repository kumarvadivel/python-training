x,y=map(str,input().split())
x=list(x)
y=list(y)
xy=0
fin=""
if len(x)>len(y):
	xy=1
elif len(y)>len(x):
	xy=-1
else:
	xy=0
ret=abs(len(x)-len(y))
if xy==1:
	for i in range(1,ret+1):
		y.append(str(i))
		
elif xy==-1:
	for i in range(1,ret+1):
		x.append(str(i))
for i in range(0,len(x)):
	fin=fin+x[i]+y[i]
print(fin)
#please check the sample input's output
 
