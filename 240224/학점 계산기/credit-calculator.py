n=int(input())

score_list=list(map(float,input().split()))

sum_val=sum(score_list)
aver=sum_val/n

if aver>=4.0:
    print("%.1f"%aver,'\nPerfect')

elif 3.0<=aver<4.0:
    print("%.1f"%aver,'\nGood')

else:
    print("%.1f"%aver,'\nPoor')