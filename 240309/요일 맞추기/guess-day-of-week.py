m1,d1,m2,d2=list(map(int,input().split()))

def calc_day(m,d):
    days_list=[0,31,28,31,30,31,30,31,31,30,31,30,31]
    total_days=0

    for i in range(1,m):
        total_days+=days_list[i]

    total_days+=d

    return total_days

left_days = (calc_day(m2, d2) - calc_day(m1, d1))

if left_days==-1 or left_days==6:
    print('Sun')

elif left_days==-2 or left_days==5:
    print('Sat')

elif left_days==-3 or left_days==4:
    print('Fri')

elif left_days==-4 or left_days==3:
    print('Thu')
elif left_days==-5 or left_days==2:
    print('Wed')
elif left_days==-6 or left_days==1:
    print('Tue')
elif left_days==0:
    print('Mon')