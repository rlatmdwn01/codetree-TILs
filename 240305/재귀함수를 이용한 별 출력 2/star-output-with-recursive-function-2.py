n=int(input())

def print_star1(n):
    if n==0:
        return
    print('* '*n)
    print_star1(n-1)

def print_star2(n):
    if n==0:
        return
    print_star2(n-1)
    print('* '*n)

print_star1(n)
print_star2(n)