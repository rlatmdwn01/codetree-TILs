n=int(input())

for i in range(n):
    for j in range(1,6-i):
        if i+j==n:
            print(f"{i+1} * {j} = {(i+1)*j}",end='\n')
        else:
            print(f"{i+1} * {j} = {(i+1)*j}",end=' / ')