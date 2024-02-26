num_list=list(map(int,input().split()))

max_val=0

for i in num_list:
    if i>max_val:
        max_val=i

print(max_val)