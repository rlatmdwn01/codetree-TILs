n=int(input())
num=1
num_list=[[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        num_list[j][i]=num
        num+=1

for i in range(n):
    for j in range(n):
        print(num_list[i][j], end=' ')
    print()