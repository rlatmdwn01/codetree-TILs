def season_of_date(Y, M, D):
    # 각 계절의 시작과 끝 날짜를 정의
    seasons = {
        'Spring': [(3, 1), (5, 31)],
        'Summer': [(6, 1), (8, 31)],
        'Fall': [(9, 1), (11, 30)],
        'Winter': [(12, 1), (2, 29)]
    }
    
    # 윤년 여부 확인
    def is_leap_year(year):
        if year % 400 == 0:
            return True
        if year % 100 == 0:
            return False
        if year % 4 == 0:
            return True
        return False
    
    # 해당 날짜가 존재하는지 확인
    def is_valid_date(year, month, day):
        if month < 1 or month > 12:
            return False
        if day < 1:
            return False
        if month == 2:
            if is_leap_year(year):
                return day <= 29
            else:
                return day <= 28
        elif month in [4, 6, 9, 11]:
            return day <= 30
        else:
            return day <= 31
    
    if not is_valid_date(Y, M, D):
        return -1
    
    # 해당 날짜가 어떤 계절에 속하는지 확인
    for season, dates in seasons.items():
        start_month, start_day = dates[0]
        end_month, end_day = dates[1]
        if (M == start_month and D >= start_day) or (M == end_month and D <= end_day) or (start_month < M < end_month):
            return season
    
    return -1

# 입력
Y, M, D = map(int, input().split())

# 결과 출력
result = season_of_date(Y, M, D)
if result == -1:
    print(-1)
else:
    print(result)