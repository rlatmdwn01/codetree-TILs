num_list=list(map(int,input().split()))
max_val=num_list[0]
min_val=num_list[0]

for i in num_list:
    if i==999 or i==-999:
        break
    else:
        if i>max_val:
            max_val=i

        elif min_val>i:
            min_val=i

print(max_val,min_val)