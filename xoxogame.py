import itertools
def print_game(k):
	for i in range(3):
		for j in range(3):
			print(k[3*i+j] ,end="")
			if j!=2:
				print("|",end="")
		print()
		if i!=2:
			print("------")
def valid(l):
	xmoves=[]
	ymoves=[]
	winpos=['1 2 3','4 5 6','7 8 9','1 4 7','2 5 8','3 6 9','1 5 9','7 8 9','3 5 7']
	for i in range(0,len(l)):
		if i%2==1:
			ymoves.append(l[i])
		else:
			xmoves.append(l[i])
	xs=" "
	xs=xs.join(xmoves)
	ys=" "
	ys=ys.join(ymoves)
	print("xmoves:",xmoves)
	print("ymoves:",ymoves)
	if xs in winpos:
		print("X wins")
	if ys in winpos:
		print("y wins")
			
	
k=[" "]*9
n=1
l=[]
while(n<=9):
	c='X' if n%2!=0 else 'O'
	d=int(input())
	
	n+=1
	if k[d-1]==" ":
		k[d-1]=c
		l.append(d)
		print_game(k)
		valid(l)
	else:
		print("invalid move")
		n-=1
	
	
	
