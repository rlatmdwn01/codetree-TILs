n=int(input())
num_list=list(map(int,input().split()))
new_list=[]

for i in range(n):
    for j in range(i+1,n):
        num=num_list[j]-num_list[i]
        new_list.append(num)

print(min(new_list))