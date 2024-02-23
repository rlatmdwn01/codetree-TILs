a,b=input().split()
a=int(a)
b=int(b)
result=0

for i in range(a,b+1):
    cnt=0
    for j in range(1,i+1):
        if i%j==0:
            cnt+=1
    if cnt==3:
        result+=1

print(result)