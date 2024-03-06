N=int(input())

def num_twice(n):
    if n<10:
        return (n**2)
    return num_twice(n//10)+((n%10)**2)


print(num_twice(N))