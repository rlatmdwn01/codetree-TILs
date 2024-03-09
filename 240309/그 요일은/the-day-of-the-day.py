import datetime

# 입력 처리
m1, d1, m2, d2 = map(int, input().split())
start_day_of_week = input().strip()

# 시작 날짜의 요일 계산
start_date = datetime.datetime(2024, m1, d1)
start_day_of_week_index = start_date.weekday()

# 목표 요일의 인덱스 계산
days_of_week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
target_day_index = days_of_week.index(start_day_of_week)

# 목표 요일이 시작 요일부터 끝 날짜까지 등장하는 횟수 계산
delta_days = (datetime.datetime(2024, m2, d2) - start_date).days + 1
num_occurrences = delta_days // 7

# 시작 요일부터 남은 일수 계산
remaining_days = delta_days % 7

# 남은 일수만큼 목표 요일이 등장하는지 확인
for i in range(remaining_days):
    if (start_day_of_week_index + i) % 7 == target_day_index:
        num_occurrences += 1

# 결과 출력
print(num_occurrences)