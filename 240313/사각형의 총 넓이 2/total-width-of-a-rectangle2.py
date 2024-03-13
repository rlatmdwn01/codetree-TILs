N=int(input())
offset=100
num_list=[[0 for _ in range(201)]for _ in range(201)]
for _ in range(N):
    x1,y1,x2,y2=tuple(map(int,input().split()))
    for x in range(x1,x2):
        for y in range(y1,y2):
            if num_list[x][y]==0:
                num_list[x][y]+=1
            else:
                num_list[x][y]=1

cnt=0
for i in range(201):
    for j in range(201):
        if num_list[i][j]==1:
            cnt+=1

print(cnt)