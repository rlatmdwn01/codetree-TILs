n = int(input())

x, y = 0,0 
dxs, dys = [1,0,-1,0], [0,-1,0,1]
time = 0
ans = -1
flag = False

for _ in range(n):
    direction, dis = tuple(input().split())
    dis = int(dis)

    if direction == 'E':
        move = 0

    elif direction == 'S':
        move = 1
    
    elif direction == 'W':
        move = 2
        
    else:
        move =3

    for _ in range(dis):    
        x, y = x+dxs[move], y+dys[move]
        time +=1


        if x==0 and y ==0:
            flag = True
            ans=time
            break
    if flag:
        break           
print(ans)

if flag ==False:
    print(-1)