n=int(input())

num_list=list(map(int,input().split()))
eval_list=[]

for i in num_list:
    if i%2==0:
        eval_list.append(i)

for j in eval_list[::-1]:
    print(j, end=' ')