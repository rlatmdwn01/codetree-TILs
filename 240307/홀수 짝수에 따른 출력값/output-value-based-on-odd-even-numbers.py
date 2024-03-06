N=int(input())

def odd_and_even(n):
    if n<=2:
        return n
    return odd_and_even(n-2)+n

print(odd_and_even(N))