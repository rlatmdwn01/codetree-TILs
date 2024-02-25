n,m=input().split()
n=int(n)
m=int(m)

num_list=list(map(int,input().split()))

cnt=0

for i in range(n):
    if num_list[i]==m:
        cnt+=1

print(cnt)