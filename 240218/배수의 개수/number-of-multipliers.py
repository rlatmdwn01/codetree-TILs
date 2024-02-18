three_cnt=0
five_cnt=0

for i in range(1,11):
    n=int(input())
    if n%3==0:
        three_cnt+=1
    if n%5==0:
        five_cnt+=1

print(three_cnt,five_cnt)