n=int(input())

cnt=1
for i in range(2*n-1):
    for _ in range(cnt):
        print("*",end="")
    print()
    print()

    if i<4:
        cnt+=1
    else:
        cnt-=1