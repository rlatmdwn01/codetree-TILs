def find_lcm(n,m):
    if n>m:
        if n%m!=0:
            val=int(n%m)
        else:
            val=m

    else:
        if m%n!=0:
            val=int(m%n)
        else:
            val=n

    print(int((n*m)/val))

a,b=tuple(map(int,input().split()))
find_lcm(a,b)