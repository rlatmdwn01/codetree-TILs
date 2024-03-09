def date_to_day(m,d):
    day_of_month= [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total_day=d
    for i in range(1,m):
        total_day+=day_of_month[i]
    return total_day

m1,d1,m2,d2=map(int,input().split())
print(date_to_day(m2,d2)-date_to_day(m1,d1)+1)