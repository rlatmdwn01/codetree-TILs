n=int(input())
sum_val=0


for _ in range(1,n+1):
    i=int(input())
    if i%3==0:
        sum_val+=i


print(sum_val)