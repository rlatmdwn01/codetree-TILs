dir_dis=list(input())
dir_num=3
x,y=0,0
dx,dy=[1,0,-1,0],[0,-1,0,1] #동서남북

for i in dir_dis:
    if i=='L':
        dir_num=(dir_num+3)%4
    elif i=='R':
        dir_num=(dir_num+1)%4
    elif i=='F':
        if dir_num==3:
            x,y=x,y+1
        elif dir_num==2:
            x,y=x-1,y
        elif dir_num==1:
            x,y=x,y-1
        else:
            x,y=x+1,y


print(x,y)