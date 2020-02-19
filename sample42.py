n=int(input())
user1score=user2score=tiescore=0
for i in range(0,n):
    us1=input()
    us2=input()
    c1=0
    if us1=="rock":
        if us2=="rock":
            c1=0
        if us2=="paper":
            c1=1
        if us2=="scissor":
            c1=-1

    elif us1=="paper":
        if us2=="rock":
            c1=1
        if us2=="paper":
            c1=0
        if us2=="scissor":
            c1=1
    elif us1=="scissor":
        if us2=="rock":
            c1=1
        if us2=="paper":
            c1=1
        if us2=="scissor":
            c1=0
    if c1==0:
        print("its a tie ")
        tiescore=tiescore+1
    elif c1==-1:
        print("user1 wins ")
        user1score=user1score+1
    elif c1==1:
        print("user2 wins")
        user2score=user2score+1

print("score board")
print("user1:",user1score)
print("user2:",user2score)
print("ties:",tiescore)