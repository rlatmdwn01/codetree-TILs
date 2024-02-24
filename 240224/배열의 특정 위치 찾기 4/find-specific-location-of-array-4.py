num_list=list(map(int,input().split()))
new_list=[]
eval_list=[]

for i in num_list:
    if i!=0:
        new_list.append(i)
    else:
        break

for j in new_list:
    if j%2==0:
        eval_list.append(j)

n=len(eval_list)
sum_val=sum(eval_list)

print(n,sum_val)