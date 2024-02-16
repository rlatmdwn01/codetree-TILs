n=int(input())

for i in range(n,5*n+1,n):
    if i%n==0:
        print(i, end=' ')