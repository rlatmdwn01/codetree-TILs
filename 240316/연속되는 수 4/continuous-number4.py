n=int(input())
arr=[]

for _ in range(n):
    a=int(input())
    arr.append(a)

ans,cnt=0,1
for i in range(1,n-1):
    if arr[i-1]<arr[i]:
        cnt+=1
    else:
        cnt=1

    ans=max(ans,cnt)

print(cnt)