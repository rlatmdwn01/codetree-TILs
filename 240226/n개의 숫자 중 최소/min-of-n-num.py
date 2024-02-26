N=int(input())
num_list=list(map(int,input().split()))
cnt=0

min_val=num_list[0]
for i in num_list[1:]:
    if min_val>i:
        min_val=i

for j in num_list:
    if min_val==j:
        cnt+=1

print(min_val,cnt)