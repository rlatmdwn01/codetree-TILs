n,m=input().split()

n=int(n)
m=int(m)

num_list=[[0 for _ in range(m)] for _ in range(n)]
num=0

for j in range(m):
    if  j%2==0:
        for i in range(n): #행
            num_list[i][j]=num
            num+=1
    else:
        for i in range(n-1,-1,-1):
            num_list[i][j]=num
            num+=1

for i in range(n):
    for j in range(m):
        print(num_list[i][j], end=' ')
    print()