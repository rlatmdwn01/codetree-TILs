N,K=tuple(map(int,input().split()))
num_list=[0]*N
for _ in range(K):
    A,B=tuple(map(int,input().split()))
    for i in range(A,B+1):
        num_list[i]+=1

print(max(num_list))