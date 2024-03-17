n,t = map(int, input().split())
r,c,d = input().split()
r, c = int(r), int(c)
mapper = {
    'R' : 0,
    'D' : 1,
    'U' : 2,
    'L' : 3
}

def in_range(x,y):
    return 0<= x and x < n and 0<=y and y<t

def move(x,y,time,t):
    c_dir = mapper[d]
    dxs, dys = [0,1,-1,0],[1,0,0,-1]
    while time < t:
        nx,ny = x + dxs[c_dir] , y + dys[c_dir]
        if not in_range(nx,ny):
            c_dir = 3 - c_dir
            time += 1
        x,y = x + dxs[c_dir],  y + dys[c_dir]
        time += 1
    return x,y

x,y = move(r-1,c-1,0,t)
print(x+1,y+1)