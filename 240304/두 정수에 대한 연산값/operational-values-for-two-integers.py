def calcul(a,b):
    if a>b:
        a=a+25
        b=b*2
    else:
        b=b+25
        a=a*2
    
    return a,b

n,m=input().split()
n=int(n)
m=int(m)

for i in calcul(n,m):
    print(i,end=' ')