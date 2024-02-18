classroom_cnt=0
hall_cnt=0
bathroom_cnt=0

n=int(input())

for i in range(1,n+1):
    if i%2==0:
        classroom_cnt+=1
        if i%6==0:
            classroom_cnt-=1
    if i%3==0:
        hall_cnt+=1
        if i%12==0:
            hall_cnt-=1
    if i%12==0:
        bathroom_cnt+=1

print(classroom_cnt,hall_cnt,bathroom_cnt)