a,b=input().split()
a=int(a)
b=int(b)

sum_val=0

for i in range(a,b+1):
    if i%5==0:
        sum_val+=i

print(sum_val)