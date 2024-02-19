a,b=input().split()

a=int(a)
b=int(b)

satisfied=False

for i in range(a,b+1):
    if 1920%i==0 or 2880%i==0:
        satisfied=True

if satisfied==True:
    print(1)
else:
    print(0)