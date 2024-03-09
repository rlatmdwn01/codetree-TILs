def days_between_dates(m1, d1, m2, d2):
    # 각 달의 날짜 수를 딕셔너리로 저장
    days_in_month = {
        1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }
    
    # 첫 번째 날짜부터 마지막 날짜까지의 총 일 수 계산
    total_days = 0
    # 시작 날짜의 남은 일수
    total_days += days_in_month[m1] - d1 + 1
    # 시작 날짜 다음 달부터 마지막 달 전까지의 일 수
    for month in range(m1 + 1, m2):
        total_days += days_in_month[month]
    # 마지막 달의 시작부터 마지막 날짜까지의 일 수
    total_days += d2
    return total_days

# 입력 처리
m1, d1, m2, d2 = map(int, input().split())

# 결과 출력
print(days_between_dates(m1, d1, m2, d2))