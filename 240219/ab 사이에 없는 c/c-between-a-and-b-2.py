a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)

satisfied=False

for i in range(a,b+1):
    if i%c==0:
        satisfied=True

if satisfied==True:
    print('NO')
else:
    print('YES')