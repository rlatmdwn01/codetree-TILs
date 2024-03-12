n=int(input())
offset=100
num_list=[0]*(201)
for _ in range(n):
    a,b=tuple(map(int,input().split()))
    for i in range(a,b):
        num_list[i]+=1

print(max(num_list))