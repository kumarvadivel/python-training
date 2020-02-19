lis=input().split(",")
ucnt=nuc=lcnt=sccnt=0
sc="#$@"
for i in range(0,len(lis)):
    l=len(lis[i])
    s=lis[i]
    if l>=6 and l<=12:
        for j in range(0,len(s)):
            if s[j].isupper():
                ucnt=ucnt+1
            elif s[j].islower():
                lcnt=lcnt+1
            elif s[j].isnumeric():
                nuc=nuc+1
            else:
                if s[j] in sc:
                    sccnt=sccnt+1
        if ucnt<1 or lcnt<1 or nuc<1 or sccnt<1:
            print("invalid password=",s)
        else:
            print("valid password=",s)
    else:
        print("invalid password=",s)

            