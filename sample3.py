n=input()
for i in range(0,len(n)):
    if n[i].isalpha():
        print(n[i],"is a alphabet")
    elif n[i].isnumeric():
        print(n[i],"is a numeric")
    else:
        print(n[i],"is a special character")
