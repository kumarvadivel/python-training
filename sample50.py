i=input()
j=i[1::]+i[0]

if i==j[::-1]:
    print("it is a quasi palindrome ")
else:
    print("it is not a quasi palindrome ")