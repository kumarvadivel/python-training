def primefactors(y):
	l=[]
	i=2
	while i<=y:
		while(y%i==0):
			l.append(i)
			y//=i
		i=i+1
	l=list(set(l))
	for i in range(0,len(l)):
		while y==0:
			y//=2
			

x,y=map(int,input().split())
fac=primefactors(y)