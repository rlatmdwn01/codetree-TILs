a,b=input().split()
a=int(a)
b=int(b)
c=a+b
c=str(c)
c_list=list(c)
cnt=0

for i in c_list:
    if i=='1':
        cnt+=1

print(cnt)