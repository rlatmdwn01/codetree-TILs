n=int(input())
cnt=0
m=n

for i in range(1,n+1):
    if m//i>1:
        cnt+=1
        m=m//i
    else:
        break
print(cnt+1)