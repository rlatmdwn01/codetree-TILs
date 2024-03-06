N=int(input())

def left_100(n):
    if n==1:
        return 2
    if n==2:
        return 4

    return ((left_100(n-1)*left_100(n-2))%100)

print(left_100(N))