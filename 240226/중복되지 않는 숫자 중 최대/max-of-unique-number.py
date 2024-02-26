n = int(input())

arr = list(map(int, input().split()))

new_arr = []

for elem in arr:

    if arr.count(elem) == 1:
        new_arr.append(elem)

if len(new_arr) == 0:

    print(-1)
else:

    print(max(new_arr))