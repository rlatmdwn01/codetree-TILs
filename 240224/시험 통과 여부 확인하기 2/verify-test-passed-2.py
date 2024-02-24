n=int(input())

cnt=0

for i in range(n):
    score_list=list(map(int,input().split()))

    sum_val=sum(score_list)
    n=len(score_list)
    aver=sum_val/n

    if aver>=60:
        print('pass')
        cnt+=1
    else:
        print('fail')

print(cnt)