m=int(input())


for i in range(m):
    n=int(input())
    cnt=0
    while n!=1:
        if n%2==0:
            n=int(n//2)
            cnt+=1

        elif n%2==1 and n!=1:
            n=3*n+1
            cnt+=1
        elif n==1:
            break

print(cnt)