N=int(input())

def go_to_1(n):
    cnt=0
    while n!=1:
        if n%2==0:
            n=int(n//2)
            cnt+=1
        else:
            n=int(n//3)
            cnt+=1
    return cnt

print(go_to_1(N))