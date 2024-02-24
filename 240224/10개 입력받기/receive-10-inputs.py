num_list=list(map(int,input().split()))
new_list=[]

for i in num_list:
    if i!=0:
        new_list.append(i)
    else:
        break

sum_val=sum(new_list)
n=len(new_list)
aver=sum_val/n

print(sum_val,"%.1f"%aver)