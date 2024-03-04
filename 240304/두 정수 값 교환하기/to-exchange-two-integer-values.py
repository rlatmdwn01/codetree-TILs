def change_num(n,m):
    n,m=m,n
    return n,m

a,b=input().split()
a=int(a)
b=int(b)
for i in change_num(a,b):
    print(i, end=' ')