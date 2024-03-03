def find_lcm(n,m):
    for i in range(max(a,b),a*b+1):
        if i%a==0 and i%b==0:
            print(i)
            break
a,b=tuple(map(int,input().split()))
find_lcm(a,b)