num_list=list(map(int,input().split()))
eval_list=[]
odd_list=[]

n=len(num_list)

for i in range (0,n,2):
    odd_list.append(num_list[i])
for j in range (1,n,2):
    eval_list.append(num_list[j])

sum_eval=sum(eval_list)
sum_odd=sum(odd_list)

if sum_eval>sum_odd:
    print(sum_eval-sum_odd)
else:
    print(sum_odd-sum_eval)