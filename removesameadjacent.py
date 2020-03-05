n=list(input())
l=['@']
for i in n:
	if i==l[-1]:
		l.pop()
	else:
		l.append(i)
if len(l)==1:
	print(-1)
else:
	print(*l[1:])
