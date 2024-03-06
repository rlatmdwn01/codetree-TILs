N=int(input())

def three_one(n):
    cnt=0
    while n!=1:
        if n%2==0:
            n=n//2
            cnt+=1
        else:
            n=3*n+1
            cnt+=1
    return cnt

print(three_one(N))