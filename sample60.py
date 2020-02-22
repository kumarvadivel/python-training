o=int(input())
a=97
s=" "
fi=""

for i in range(0,o):
    fi=fi+chr(a)
    a=a+1
'''print(fi[0::])
print(fi[1::])
print(fi[2::])
print(fi[3::])'''
for i in range(0,o+1):
    
    print(" "*i+fi[i::])
    
