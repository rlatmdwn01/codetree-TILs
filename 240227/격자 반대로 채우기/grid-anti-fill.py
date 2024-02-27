n=int(input())
num_list=[[0 for _ in range (n)] for _ in range (n)]
num=1
k=n

if k%2==0:
    for j in range(n-1,-1,-1):
        if j%2==1:
            for i in range(n-1,-1,-1):
                num_list[i][j]=num
                num+=1

    else:
        for i in range(n):
            num_list[i][j]=num
            num+=1

else:
    for j in range(n-1,-1,-1):
        if j%2==0:
            for i in range(n-1,-1,-1):
                num_list[i][j]=num
                num+=1

        else:
            for i in range(n):
                num_list[i][j]=num
                num+=1

for i in range(n):
    for j in range(n):
        print(num_list[i][j], end=' ')
    print()