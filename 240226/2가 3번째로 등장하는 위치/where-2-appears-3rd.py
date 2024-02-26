n=int(input())
num_list=list(map(int,input().split()))

idx_list=[]

for i in num_list:
    if i==2:
        idx_list.append(num_list[i]+1)

print(idx_list[2])