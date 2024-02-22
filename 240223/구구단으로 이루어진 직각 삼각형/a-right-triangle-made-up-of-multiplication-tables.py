n = int(input())  # n 입력 받기

for i in range(1, n + 1):
    for j in range(1, n - i + 2):
        if i+j==n+1:
            print(f"{i} * {j} = {i * j}", end = "\n")
        else:
            print(f"{i} * {j} = {i * j}", end = " / ")