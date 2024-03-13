n=int(input())
offset=100
squ_list=[[0 for _ in range(201)] for _ in range(201)]
num=0
area=0

for _ in range(n):
    x1,y1,x2,y2=tuple(map(int,input().split()))
    x1+=100
    y1+=100
    x2+=100
    y2+=100
    num+=1
    for i in range(x1,x2):
        for j in range(y1,y2):
            if num%2==1:
                squ_list[i][j]=1
            else:
                squ_list[i][j]=2

for i in range(201):
    for j in range(201):
        if squ_list[i][j]==2:
            area+=1

print(area)