def count_leader_changes(N, M, A_moves, B_moves):
    # A와 B의 초기 위치
    A_position = 0
    B_position = 0
    leader_changes = 0
    
    # A와 B가 이동한 거리를 계산하고 선두가 바뀌었는지 확인
    for i in range(max(N, M)):
        if i < N:
            A_v, A_t = A_moves[i]
            A_position += A_v * A_t
        if i < M:
            B_v, B_t = B_moves[i]
            B_position += B_v * B_t
        
        # 선두가 바뀌는지 확인
        if A_position > B_position:
            if i == 0 or A_position - A_v * A_t > B_position:
                leader_changes += 1
        elif B_position > A_position:
            if i == 0 or B_position - B_v * B_t > A_position:
                leader_changes += 1
    
    return leader_changes

# 입력 받기
N, M = map(int, input().split())
A_moves = [list(map(int, input().split())) for _ in range(N)]
B_moves = [list(map(int, input().split())) for _ in range(M)]

# 결과 출력
print(count_leader_changes(N, M, A_moves, B_moves))