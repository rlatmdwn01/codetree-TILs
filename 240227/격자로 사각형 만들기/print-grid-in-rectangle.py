n=int(input())
num_list=[[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    num_list[0][i]=1
    num_list[i][0]=1

for i in range(1,n):
    for j in range(1,n):
        num_list[i][j]=num_list[i-1][j]+num_list[i][j-1]+num_list[i-1][j-1]

for i in range(n):
    for j in range(n):
        print(num_list[i][j],end=' ')
    print()