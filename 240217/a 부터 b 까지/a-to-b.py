a,b=input().split()

a=int(a)
b=int(b)
i=a

while i<=b:
    print(i, end=" ")
    if i%2==1:
        i=i*2
    else:
        i=i+3