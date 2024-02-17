n=int(input())

for i in range(1,n+1):
    m=list(map(int,input().split()))
    for j in m:
        if (j%2==1) and (j%3==0):
            print(j)