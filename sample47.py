import array as ar
n=ar.array('i',[1,2,3,4,5,6,7])
n[2:5]=ar.array('i',[8,8,8])
print(n)
del n[2:5]
print(list(n))
