arr = input()

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
x, y = 0, 0           # 시작은 (0, 0) 입니다.
dir_num = 3           # 0: 오른쪽, 1: 아래쪽, 2: 왼쪽, 3: 위쪽
ans = -1
time = 0

for i in range(len(arr)):

    if arr[i] == 'L':
        dir_num = (dir_num + 3) % 4
        time += 1
    elif arr[i] == 'R':
        dir_num = (dir_num + 1) % 4
        time += 1
    elif arr[i] == 'F':
        # 그 다음 위치로 이동한 다음 배열에 올바른 값을 채워넣습니다.
        x, y = x + dxs[dir_num], y + dys[dir_num]
        time += 1
    
    if x == 0 and y == 0:
        ans = time
        break
        
print(ans)