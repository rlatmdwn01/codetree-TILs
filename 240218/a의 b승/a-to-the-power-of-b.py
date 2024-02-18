a,b=input().split()

a=int(a)
b=int(b)

prod=1

for _ in range(1,b+1):
    prod*=a

print(prod)