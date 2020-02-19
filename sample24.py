#to add item to tuple
t=(4,6,7,8,9,0)
print(t)
t=t[:5]+(15,20,9)+t[5:]
print(t)
x=list(t)
x.append(10)
t=tuple(x)
print(t)