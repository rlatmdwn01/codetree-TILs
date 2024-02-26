n=int(input())
num_list=list(map(int,input().split()))

idx_list=[]

for i in range(len(num_list)):
    if num_list[i]==2:
        idx_list.append(i+1)
        i=0

print(idx_list[2])