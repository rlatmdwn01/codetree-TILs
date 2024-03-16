n=int(input())
x,y=0,0
dx,dy=[1,-1,0,0],[0,0,-1,1] #동서남북

for _ in range(n):
    direction,distance=input().split()
    distance=int(distance)
    if direction=='N':
        x,y=x+dx[3], y+dy[3]*distance
    elif direction=='S':
        x,y=x+dx[2], y+dy[2]*distance
    elif direction=='W':
        x,y=x+dx[1]*distance, y+dy[1]*distance
    else:
        x,y=x+dx[0]*distance, y+dy[0]*distance


print(x,y)