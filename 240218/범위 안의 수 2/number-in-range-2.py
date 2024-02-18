sum_val=0
cnt=0

for _ in range(1,11):
    n=int(input())
    if 0<=n<=200:
        sum_val+=n
        cnt+=1

print(sum_val,"%.1f"%((sum_val)/cnt))