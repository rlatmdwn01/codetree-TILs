a,b=input().split()

a=int(a)
b=int(b)
print(a,end=' ')

for i in range(a,b+1):
    while a<b:
        if a%2==1:
            a=a*2
        else:
            a=a+3

        print(a,end=' ')