n,m=input().split()
n=int(n)
m=int(m)

arr=[[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(m):
    r,c=input().split()
    r=int(r)
    c=int(c)
    arr[r-1][c-1]=1

for i in range(n):
    for j in range(n):
        print(arr[i][j],end=' ')
    print()