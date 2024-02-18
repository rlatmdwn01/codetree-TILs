n=int(input())
cnt=1
m=n

for i in range(1,n+1):
    if m//cnt>1:
        cnt+=1
        m=m//cnt
    else:
        break
print(cnt+1)