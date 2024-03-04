def compelete_num(n):
    if n%2==0:
        return False
    if n%10==5:
        return False
    if n%3==0 and n%9!=0:
        return False
    return True

a,b=input().split()
a=int(a)
b=int(b)
cnt=0

for i in range(a,b+1):
    if compelete_num(i):
        cnt+=1
print(cnt)