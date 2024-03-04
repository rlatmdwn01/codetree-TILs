def ten(N):
    sum_val=0
    for i in range(1,N+1):
        sum_val+=i
    return int(sum_val//10)

a=int(input())
print(ten(a))