N=int(input())

def facotrial(n):
    if n==0:
        return 1
    if n==1:
        return 1
    return facotrial(n-1)*n

print(facotrial(N))