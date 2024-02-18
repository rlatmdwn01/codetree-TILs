sum_val=0

a,b=input().split()

a=int(a)
b=int(b)

for i in range(a,b+1):
    sum_val+=i

print(sum_val)