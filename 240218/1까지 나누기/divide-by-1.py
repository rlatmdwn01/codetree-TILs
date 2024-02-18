n=int(input())
cnt=1

for i in range(1,n+1):
    cnt+=1
    n=n/cnt
    if n<=1:
        break
    
print(i+1)