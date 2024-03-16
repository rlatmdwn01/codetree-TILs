n,t=tuple(map(int,input().split()))
num_list=list(map(int,input().split()))
ans,cnt=0,0

for i in range(n):
    if num_list[i]>t:
        cnt+=1
    else:
        ans=max(ans,cnt)
        cnt=0
    ans=max(ans,cnt)

print(ans)