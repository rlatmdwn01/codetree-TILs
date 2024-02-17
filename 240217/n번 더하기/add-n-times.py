a,n=input().split()

a=int(a)
n=int(n)

for i in range(a+n,(a+n)+n*(n-1)+1,n):
    print(i)