N, T = tuple(map(int, input().split()))
info = list(input())
arr = [ 
    list(map(int, input().split()))
    for _ in range(N)
]
x, y = N//2, N//2 # 가운데 위치에서 시작  

# 함수 선언 
def in_range(x,y): 
    return 0 <= x < N and 0 <= y < N 

hap = arr[x][y]
dir_num = 0 

# 북, 동, 남, 서 -> 시계 방향  
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for dr in info:  
    if dr == "L": 
        dir_num = (dir_num+3)%4  # 왼쪽으로 90도 전환
    elif dr == "R": 
        dir_num = (dir_num+1)%4  # 오른쪽으로 90도 전환 
    else: 
        nx = x + dx[dir_num]
        ny = y + dy[dir_num]
        if in_range(nx,ny): 
            hap += arr[nx][ny]
            x, y = nx, ny

# 출력
print(hap)