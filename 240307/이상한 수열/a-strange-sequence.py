N=int(input())

def odd_sequence(n):
    if n==1:
        return 1
    if n==2:
        return 2
    return odd_sequence(n//3)+odd_sequence(n-1)

print(odd_sequence(N))