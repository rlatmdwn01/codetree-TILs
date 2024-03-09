def minutes_between_times(a, b, c):
    # 시작 시간과 비교할 시간
    start_time = (11, 11, 11)  # 11월 11일 11시 11분
    
    # 비교할 시간이 시작 시간보다 앞선 경우 -1 반환
    if (a, b, c) < start_time:
        return -1
    
    # 경과 시간 계산 (분 단위로 변환하여 계산)
    elapsed_minutes = (a - 11) * 24 * 60  # 일 수를 분 단위로 변환
    elapsed_minutes += (b - 11) * 60       # 시간을 분 단위로 변환
    elapsed_minutes += (c - 11)            # 분
    
    return elapsed_minutes

# 입력 처리
a, b, c = map(int, input().split())

# 결과 출력
print(minutes_between_times(a, b, c))