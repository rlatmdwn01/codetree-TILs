num_list=list(map(int,input().split()))
empty_list=[]

for i in num_list:
    if i<250:
        empty_list.append(i)
    else:
        break

n=len(empty_list)
sum_val=sum(empty_list)

print(sum_val,sum_val/n )