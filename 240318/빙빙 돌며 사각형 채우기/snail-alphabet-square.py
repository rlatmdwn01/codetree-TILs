def fill_snail(n, m):
    # 사각형 초기화
    square = [[' ' for _ in range(m)] for _ in range(n)]

    # 달팽이 모양으로 알파벳 채우기
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 오른쪽, 아래, 왼쪽, 위
    direction_index = 0
    x, y = 0, 0
    num = ord('A')
    while True:
        square[x][y] = chr(num)
        num += 1
        if num > ord('Z'):
            num = ord('A')
        new_x = x + directions[direction_index][0]
        new_y = y + directions[direction_index][1]
        if 0 <= new_x < n and 0 <= new_y < m and square[new_x][new_y] == ' ':
            x, y = new_x, new_y
        else:
            direction_index = (direction_index + 1) % 4
            new_x = x + directions[direction_index][0]
            new_y = y + directions[direction_index][1]
            if not (0 <= new_x < n and 0 <= new_y < m) or square[new_x][new_y] != ' ':
                break
            x, y = new_x, new_y

    # 출력
    for row in square:
        print(' '.join(row))

# 입력 받기
n, m = map(int, input().split())

# 결과 출력
fill_snail(n, m)