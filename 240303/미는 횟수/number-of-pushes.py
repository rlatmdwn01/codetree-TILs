A=input()
B=input()
cnt=0
n=len(A)

for i in range(n):
    if A!=B:
        B=B[-1]+B[:-1]
        cnt+=1
    elif A==B:
        print(cnt)
        break
    if cnt>n-1:
        print(-1)