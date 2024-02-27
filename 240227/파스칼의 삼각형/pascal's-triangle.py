n=int(input())

arr=[[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        arr[i][0]=1
        if i==j:
            arr[i][j]=1
        elif j<i:
            arr[i][j]=arr[i-1][j-1]+arr[i-1][j]

for i in range(n):
    for j in range(i+1):
        print(arr[i][j], end=" ")
    print()