n=int(input())
satisfied=True

for i in range(2,n):
    if n%i==0:
        satisfied=False
    else:
        satisfied=True

if satisfied==True:
    print('P')
else:
    print('C')