n=int(input())
sum_val=0

for i in range (n):
    num=int(input())
    sum_val+=num

num_list=list(str(sum_val))
front=num_list[0]
m=len(num_list)

for i in range(m):
    if i!=m-1:
        num_list[i]=num_list[i+1]
    else:
        num_list[m-1]=front

for i in num_list:
    print(i,end='')