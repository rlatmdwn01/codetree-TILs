n=int(input())
sum_val=0
cnt=0

for _ in range(1,n+1):
    i=int(input())
    sum_val+=i
    cnt+=1

print(sum_val,"%.1f"%(sum_val/cnt))