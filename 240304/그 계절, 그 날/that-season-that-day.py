def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

def get_season(M):
    if 3 <= M <= 5:
        return 'Spring'
    elif 6 <= M <= 8:
        return 'Summer'
    elif 9 <= M <= 11:
        return 'Fall'
    else:
        return 'Winter'

# 입력
Y, M, D = map(int, input().split())

# 유효한 날짜인지 확인
if M < 1 or M > 12 or D < 1 or D > 31:
    print(-1)
else:
    if M == 2:
        if is_leap_year(Y):
            if D <= 29:
                print(get_season(M))
            else:
                print(-1)
        elif D <= 28:
            print(get_season(M))
        else:
            print(-1)
    elif M in [4, 6, 9, 11]:
        if D <= 30:
            print(get_season(M))
        else:
            print(-1)
    else:
        print(get_season(M))