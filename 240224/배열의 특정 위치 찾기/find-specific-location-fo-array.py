num_list=list(map(int,input().split()))
eval_list=[]
three_list=[]

for i in range(1,10,2):
    eval_list.append(num_list[i])

for j in range(2,10,3):
    three_list.append(num_list[j])

sum_val=sum(eval_list)
n=len(three_list)
three_sum_val=sum(three_list)
aver=three_sum_val/n

print(sum_val,"%.1f"%aver)