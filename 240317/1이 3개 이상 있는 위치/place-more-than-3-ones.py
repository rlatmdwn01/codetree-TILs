# 변수 선언 및 입력
n = int(input())    # 격자의 크기를 의미하는 변수
arr = [             # 격자를 저장하는 2차원 배열
    list(map(int, input().split()))
    for _ in range(n)
]

dxs = [0, 1,  0, -1]
dys = [1, 0, -1,  0]


def in_range(x, y):  # x행 y열이 격자에 존재하는 지 확인하는 함수
    return 0 <= x and x < n and 0 <= y and y < n

# 각 칸을 탐색합니다.
ans = 0  # 주변에 1이 3개 이상 있는 격자의 개수

# 모든 칸 탐색하기!
for i in range(n):      # 이번에 탐색할 행의 번호
    for j in range(n):  # i번 행에서 이번에 탐색할 열 번호

        # 현재 나는 (i 행, j 열) 탐색하는 중이다.
        cnt = 0         # i행 j열 주변에 있는 1의 개수

        for dir_num in range(4):  # 인접한 방향을 결정
            
            # ni, nj 가 dir_num 방향으로 인접한 격자의 행, 열 번호
            ni, nj = i + dxs[dir_num], j + dys[dir_num]

            # (nx, ny)가 유효하고, 1이 써 있는 격자라면
            if in_range(ni, nj) and arr[ni][nj] == 1:
                cnt += 1  # 1의 개수를 하나 늘려준다.
        
        if cnt >= 3:  # 주변에 1이 3개 이상 있다면
            ans += 1  # 정답을 1 증가시킨다.
    
print(ans)