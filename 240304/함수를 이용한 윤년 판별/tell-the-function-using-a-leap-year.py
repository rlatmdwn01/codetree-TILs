def leap_year(n):
    if (y%100==0) and (y%4==0) and (y%400==0):
        if y<400:
            return False
        else:
            return True
    if (y%100==0) and (y%4==0):
        return False
    if y%4==0:
        return True

y=int(input())
if leap_year(y):
    print('true')
else:
    print('false')